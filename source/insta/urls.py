from django.urls import path
from insta.api.v1 import get_token_view, AccountPostsView

app_name = 'insta'

urlpatterns = [
    path('get_token/', get_token_view, name='get_token'),
    path('accounts/', AccountPostsView.as_view(), name='get_account_posts')
]


