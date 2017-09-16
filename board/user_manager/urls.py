from django.conf.urls import url

from user_manager.views import login, login_validate, join_page

#사실 이자리에 함수가 생기는데 이걸 블록 지정한다음 alt shift v를
#이용하여 views.py로 옮겼다



urlpatterns = [
    url(r'^login/$', login),
    url(r'^login/validate/$', login_validate),
    url(r'^join/$', join_page)

]