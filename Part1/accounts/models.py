from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUser(AbstractUser, UserManager):

    email = models.EmailField(verbose_name="メールアドレス", unique=True, blank=False, null=False)  #emailを必須＆ユニークに設定
    thumbnail = models.ImageField(upload_to="images/thumbnail/", verbose_name="サムネイル", blank=True, null=True)
    USERNAME_FIELD = 'email'   #ログオンIDをユーザ名→Emailへ変更
    REQUIRED_FIELDS = ['username']       #ユーザーを作成するために必要なキーを指定

    def __str__(self):
        return self.email