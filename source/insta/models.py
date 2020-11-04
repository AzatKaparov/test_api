from django.db import models


class Post(models.Model):
    media = models.CharField(max_length=5000, verbose_name='Медиа', blank=True, null=True)
    text = models.TextField(verbose_name='Текст поста', blank=True, null=True)
    date = models.DateTimeField(auto_now=False, verbose_name='Дата', null=False, blank=False)
    post_url = models.CharField(max_length=5000, verbose_name='Ссылка на пост', blank=False, null=False)
    post_id = models.DecimalField(verbose_name="ID", max_digits=100, decimal_places=0,)
    account = models.ForeignKey('insta.Account', related_name='posts', verbose_name='Аккаунт', on_delete=models.PROTECT,
                                default="")

    def __str__(self):
        if self.text:
            return f"{self.account.username}: {self.text[:15]}..."
        return f"{self.account.username}"

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        ordering = ('-date',)


class Account(models.Model):
    username = models.CharField(max_length=100, verbose_name='Никнейм', null=False, blank=False)
    user_id = models.DecimalField(verbose_name='ID', max_digits=100, decimal_places=0, null=False, blank=False)
    full_name = models.CharField(max_length=150, verbose_name='Имя', null=True, blank=True)

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'аккаунт'
        verbose_name_plural = 'аккаунты'
        ordering = ('username', )


class AccountList(models.Model):
    username = models.CharField(max_length=100, verbose_name='Никнейм', null=False, blank=False)

    def __str__(self):
        return f'{self.username}'
