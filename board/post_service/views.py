from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from post_service.models import Post


# Create your views here.


def post_list(request):
    page_data = Paginator(Post.objects.all(),5)
    #겟방식으로 넘어온 파라미터 값 얻어오기!
    page = request.GET.get('page')
    if page is None:
        page = 1
    try:
        #페이지 네이터에 페이지 속성에 값을 넘겨주면 그 페이지에 해당하는 리스트를
        posts = page_data.page(page)
    except PageNotAnInteger:
        #숫자가아니면 1페이지
        posts = page_data.page(1)
    except EmptyPage:
        #페이지가 범위를 벗어나면 마지막페이지로 해줌
        #그니까 원래 10개의 페이지가있는데 12 막 이런걸로 들어오면 10으로
        #num_pages이거는 페이지중 마지막이 나옴
        posts = page_data.page(page_data.num_pages)
    return render(request, 'post_list.html', context={
        'post_list': posts,
        #템플릿에서 사용하려고 인트넣어줌
        'current_page':int(page),
        #요대로 넘겨줘야함
        'total_page':range(1,page_data.num_pages+1)
    })