from django.contrib import auth
from django.contrib.auth.models import User
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.context_processors import csrf

from user_manager.forms import LoginForm,JoinForm

def login(request):
    #모델처럼 폼을 정의한다음 이걸 리턴해주면 바로 만들 수 있음

    return render(request,'login_form.html',context={
        'login_form':LoginForm
    })

def login_validate(request):
    login_form_date = LoginForm(request.POST)
    #찾아보니 값이 있으면 이거임 없으면 false
    #하나라도 비어있으면 false 리턴함
    #아 헷갈리게 일반 로그인폼은 저렇게 넣어주면 그 값들을 .cleaned_data여기로
    #받나보다
    if login_form_date.is_valid():
        user = auth.authenticate(username=login_form_date.cleaned_data['id']
                                 ,password=login_form_date.cleaned_data['password'])
        if user is not None:
            if user.is_active:
                auth.login(request,user)

                return HttpResponseRedirect('갈곳')
            else:
                return HttpResponse('사용자가 없거나 비밀번호를 잘못')
        else:
            return HttpResponse('로그인 폼이 비정상 적 입니다')

        return HttpResponse('알 수 없는 오류 입니다')


#내가 사실 뭐 변경할게 많지 않으면 modelform_factory
#이건 함수로 정의 되어있어서 그냥 바로 쓰면됨 클래스로 정의 ㄴㄴ염
#포스트,겟 은 보통 뷰에서 한번에 처리 함
def join_page(request):
    if request.method == 'POST':
        form_data = JoinForm(request.POST)

        if form_data.is_valid():
            #모델폼이었으면
            #aa = form_data.save(commit=False)
            #를 하고 그냥 aa.로 바로 접근가능
            username = form_data.cleaned_data['id']
            password = form_data.cleaned_data['password']
            User.objects.create_user(username=username,password=password)

            return redirect('/user/login/')
    else:
        form_data = JoinForm()

    print('폼데이타',form_data)
    return render(request,'join_page.html',context={
        'join_form':form_data
    })