from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from .decorators import *
from .models import User
from django.views.generic import View
from django.contrib import messages

from django.core.exceptions import PermissionDenied
from .forms import LawRegisterForm, RegisterForm
from django.views.generic import CreateView

from .forms import LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.views.generic import FormView
from django.views.generic import TemplateView

from .forms import RecoveryIdForm
from django.views.generic import View
import json
from django.core.serializers.json import DjangoJSONEncoder


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
    success_url = '/users/home/'

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

# 아이디 찾기 뷰
@method_decorator(logout_message_required, name='dispatch')
class RecoveryIdView(View):
    template_name = 'users/recovery_id.html'
    form = RecoveryIdForm

    def get(self, request):
        if request.method=='GET':
            form_id = self.recovery_id(None)
            print(recovery_id)
        return render(request, self.template_name, { 'form_id':form_id, })

# 아이디 찾기 ajax 뷰
def ajax_find_id_view(request):
    name = request.POST.get('name')
    email = request.POST.GET('email')
    result_id = User.objects.get(name=name, email=email)

    return HttpResponse(json.dumps({"result_id": result_id.user_id}, cls=DjangoJSONEncoder), content_type = "application/json")