
from django.http.response import HttpResponse
from blog.models import Post
from rest_framework.generics import GenericAPIView
from rest_framework import serializers,mixins

def blog_page(request):
    post_list = Post.objects.all()
    return HttpResponse('Hello'+post_list[0].title)

#시리얼라이저는 모델을 어떻게 주고 받을 것인가를 정의하기 위한 클래스
#모델시리얼라이저는 모델전체를 자동으로 변환해준다네
#포인트는 레스트풀로 개발할때는 항상 시리얼라이저가 있어야함
class PostSerializer(serializers.ModelSerializer):
        class Meta:
            model = Post
            fields = ('title','content','reg_date')



#mixins.ListModelMixin 이건 GenericAPIVIEW에 있는 쿼리셋과 시리얼라이즈
#클래스를 기반으로 하여 데이터 LIST 를 만들어 준다
class blog_api(GenericAPIView,mixins.ListModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    #여기서 리스트메서드는 ListModelMixin여기서 상속받은 메서드임임
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)




