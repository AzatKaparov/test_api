from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
import time
from rest_framework.permissions import AllowAny
from instagram import Account, WebAgent
import json
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.views import APIView

from insta.models import AccountList, Account as Akk, Post
from insta.serializers import PostSerializer

BASE_INST_URL = 'https://www.instagram.com/'


users = AccountList.objects.all()


class AccountPostsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        try:
            name = request.GET.get("name", "")
            akk = get_object_or_404(Akk, username=name)
            posts = Post.objects.filter(account=akk)
            slr = PostSerializer(posts, many=True, context={'request': request})
            return JsonResponse(slr.data, safe=False)
        except:
            return HttpResponse('There is no account with this name!\n Please check your request one more time')


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


def parse_list(massive):
    for i in massive:
        agent = WebAgent()
        add_posts(i.username, agent)


def add_posts(account, agent):
    account = Account(account)
    media = agent.get_media(account, pointer=None, count=50, limit=200, delay=0)
    user, created = Akk.objects.get_or_create(username=account.username,
                                              user_id=account.id,
                                              full_name=account.full_name)
    print(media)
    for i in media[0]:
        if i.is_video:
            pass
            # Post.objects.update_or_create(
            #     media=i.video_url,
            #     text=i.caption,
            #     date=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(i.date)),
            #     post_url=BASE_INST_URL + i.base_url + i.code,
            #     post_id=i.id,
            #     account=user
            # )
        elif i.is_album:
            # print('\nЭто альбом\n')
            album = []
            for j in i.album:
                if j.is_video:
                    album.append(j.video_url)
                elif j.is_ad:
                    pass
                elif j.is_album:
                    pass
                else:
                    album.append(j.display_url)
            # Post.objects.update_or_create(
            #     media=album,
            #     text=i.caption,
            #     date=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(i.date)),
            #     post_url=BASE_INST_URL + i.base_url + i.code,
            #     post_id=i.id,
            #     account=user,
            # )
            print(album)
        elif i.is_ad:
            pass
        else:
            pass
            # Post.objects.update_or_create(
            #     media=i.display_url,
            #     text=i.caption,
            #     date=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(i.date)),
            #     post_url=BASE_INST_URL + i.base_url + i.code,
            #     post_id=i.id,
            #     account=user
            # )


# parse_list(users)

# acc = Account('azat_kaparov')
# agent = WebAgent()
# media2 = agent.get_media(acc, count=50, limit=50, delay=0)


