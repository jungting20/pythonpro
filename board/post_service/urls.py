from django.conf.urls import url

from post_service import views
from user_manager.views import login,login_validate
#사실 이자리에 함수가 생기는데 이걸 블록 지정한다음 alt shift v를
#이용하여 views.py로 옮겼다



urlpatterns = [
    url(r'^$',views.post_list),
    #알트 엔터눌러서 함수만들었음

]