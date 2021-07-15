from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from .choice import *

class UserManager(BaseUserManager):

    def create_user(self, user_id, password, email, phone_number, name, department, auth, **extra_fields):
        if not user_id:
            raise ValueError('user_id Required!')

        user = self.model(
            user_id=user_id,
            password=password,
            email=email,
            phone_number=phone_number,
            name=name,
            department=department,
            auth=auth,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, password, email=None, phone_number=None, name=None, department=None, auth=None):
        user = self.create_user(user_id, password, email, phone_number, name, department, auth)
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.level = 0
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    user_id = models.CharField(max_length=20, verbose_name="아이디", unique=True)
    password = models.CharField(max_length=256, verbose_name="비밀번호")
    email = models.EmailField(max_length=128, verbose_name="이메일", null=True, unique=True)
    phone_number = models.IntegerField(verbose_name="핸드폰번호", null=True, unique=True)
    name = models.CharField(max_length=10, verbose_name="이름", null=True)
    level = models.CharField(choices=LEVEL_CHOICES, max_length=18, verbose_name="등급", default=3)
    department = models.CharField(choices=DEPARTMENT_CHOICES, max_length=24, verbose_name="가입유형", null=True)
    auth = models.CharField(max_length=10, verbose_name="인증번호", null=True)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='가입일', null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = "회원목록"
        verbose_name = "사용자"
        verbose_name_plural = "사용자"