from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from free.models import Free
from .decorators import *
from .models import User
from django.views.generic import View
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from .forms import LawRegisterForm, RegisterForm, CustomUserChangeForm, CheckPasswordForm, CustomSetPasswordForm, CustomPasswordChangeForm
from django.views.generic import CreateView
from .forms import LoginForm
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth import logout
from django.views.generic import FormView
from django.views.generic import TemplateView
from .forms import RecoveryIdForm
from django.views.generic import View
import json
from django.core.serializers.json import DjangoJSONEncoder
from .forms import RecoveryPwForm


@method_decorator(logout_message_required, name='dispatch')
class AgreementView(View):
    def get(self, request, *args, **kwargs):
        request.session['agreement'] = False
        return render(request, 'users/agreement.html')

    def post(self, request, *args, **kwarg):
        if request.POST.get('agreement1', False) and request.POST.get('agreement2', False):
            request.session['agreement'] = True

            if request.POST.get('lawregister') == 'lawregister':
                return redirect('/users/lawregister/')
            else:
                return redirect('/users/register/')
        else:
            messages.info(request, "약관에 모두 동의해주세요.")
            return render(request, 'users/agreement.html')

class LawRegisterView(CreateView):
    model = User
    template_name = 'users/lawregister.html'
    form_class = LawRegisterForm

    def get(self, request, *args, **kwargs):
        if not request.session.get('agreement', False):
            raise PermissionDenied
        request.session['agreement'] = False
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, "회원가입 성공.")
        return redirect('users:login')

    def form_valid(self, form):
        self.object = form.save()
        return redirect(self.get_success_url())
# 변호사 회원가입후에 변호사 신상 입력하는 란으로 넘어가게

# 일반 회원가입
class RegisterView(LawRegisterView):
    template_name = 'users/register.html'
    form_class = RegisterForm

# 로그인 뷰
@method_decorator(logout_message_required, name='dispatch')
class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        user_id = form.cleaned_data.get("user_id")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=user_id, password=password)

        if user is not None:
            self.request.session['user_id'] = user_id
            login(self.request, user)

        return super().form_valid(form)

# 로그아웃 뷰
def logout_view(request):
    logout(request)
    return redirect('/')

# 메인화면(로그인 후)
@login_message_required
class homeview(TemplateView):
    template_name = 'home/home.html'
    success_url = '/home/home/'

# 아이디 찾기 뷰
@method_decorator(logout_message_required, name='dispatch')
class RecoveryIdView(View):
    template_name = 'users/recovery_id.html'
    recovery_id = RecoveryIdForm

    def get(self, request):
        if request.method=='GET':
            form_id = self.recovery_id(None)
            # print(recovery_id)
        return render(request, self.template_name, { 'form_id' : form_id, })

# 아이디 찾기 ajax 뷰
def ajax_find_id_view(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    result_id = User.objects.get(name=name, email=email)

    return HttpResponse(json.dumps({"result_id": result_id.user_id}, cls=DjangoJSONEncoder), content_type = "application/json")

#비번찾기
@method_decorator(logout_message_required, name='dispatch')
class RecoveryPwView(View):
    template_name = 'users/recovery_pw.html'
    recovery_pw = RecoveryPwForm

    def get(self, request):
        if request.method=='GET':
            form_pw = self.recovery_pw(None)
            return render(request, self.template_name, { 'form_pw': form_pw, })

def ajax_find_pw_view(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    user_id = request.POST.get('user_id')
    result_pw = User.objects.get(user_id=user_id, name=name, email=email)

    return HttpResponse(json.dumps({"result_pw": result_pw.password}, cls=DjangoJSONEncoder), content_type = "application/json")

def pw_reset_view(request):
    if request.method == 'POST':
        reset_password_form = CustomSetPasswordForm(request.user, request.POST)
        if reset_password_form.is_valid():
            user = reset_password_form.save()
            messages.success(request, "비밀번호 변경완료! 변경된 비밀번호로 로그인하세요.")
            logout(request)
            return redirect('users:login')
        else:
            logout(request)
    else:
        reset_password_form = CustomSetPasswordForm(request.user)

    return render(request, 'users/password_reset.html', {'form': reset_password_form})


# 프로필 보기
@login_message_required
def profile_view(request):
    if request.method == 'GET':
        return render(request, 'users/profile.html')

# 프로필 수정
@login_message_required
def profile_update_view(request):
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance = request.user)

        if user_change_form.is_valid():
            user_change_form.save()
            messages.success(request, '회원정보가 수정되었습니다.')
            return render(request, 'users/profile.html')
    else:
        user_change_form = CustomUserChangeForm(instance = request.user)

    return render(request, 'users/profile.html', {'user_change_form':user_change_form})


# 회원탈퇴
@login_message_required
def profile_delete_view(request):
    if request.method == 'POST':
        password_form = CheckPasswordForm(request.user, request.POST)

        if password_form.is_valid():
            request.user.delete()
            logout(request)
            messages.success(request, "회원탈퇴가 완료되었습니다.")
            return redirect('/')
    else:
        password_form = CheckPasswordForm(request.user)

    return render(request, 'users/profile_delete.html', {'password_form': password_form}) #html 경로 보기

# 비밀번호 수정
@login_message_required
def password_edit_view(request):
    if request.method == 'POST':
        password_change_form = CustomPasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)
            # logout(request)
            messages.success(request, "비밀번호를 성공적으로 변경하였습니다.")
            return redirect('/')
    else:
        password_change_form = CustomPasswordChangeForm(request.user)

    return render(request, 'users/profile.html', {'password_change_form':password_change_form})


def mypost(request):
        blogs = Free.objects.all()
        blog_list = blogs.filter(username=request.user.user_id) # 내가 쓴글만
        # blog_list = Blog.objects.all().order_by('-id') # 블로그 객체 다 가져오기
        paginator = Paginator(blog_list, 6) # 3개씩 잘라내기
        page = request.GET.get('page') # 페이지 번호 알아오기
        if page is None:
                page = 1
        else:
                page = int(page)
        firstPage= (page//10) * 10 +1   # 페이지 시작
        LastPage= firstPage+10           # 페이지 끝
        posts = paginator.get_page(page) # 페이지 번호 인자로 넘겨주기
        count = [1,2,3]
        if LastPage>posts.paginator.num_pages:
                LastPage=posts.paginator.num_pages+1
        pageRange=range(firstPage,LastPage)
        return render(request, 'profile.html', {'blogs' :blogs, 'posts': posts, 'pageRange':pageRange, 'count':count})

