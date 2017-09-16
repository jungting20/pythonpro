from django import forms


# 이게 forms.form 이있고
# forms.modelform 이있음 이건 보통 게시판 할때 사용하는 듯
#폼만들고 항상 shell에서 폼 잘되나 확인 ㄱㄱ
#클래스는 생성하면서 딕셔너리로 넣어줌
#생성후에는 다양한 작업을 할 수 있다
#is_valid 같은걸 할 수 있다
#그리고 에러가뭔지도 알 수 있음
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    id = forms.CharField(label="ID", max_length=12)
    password = forms.CharField(label="PASSWORD", max_length=12, widget=forms.PasswordInput)

#이렇게 객체로 해서 넣어주면 된다
password_errormessages={
    'required':'해당 항목은 필수 입니다!',
    'min_length':'최소 %(limit_value)d자 이상 입력해 주세요'
}
class JoinForm(forms.Form):
    #아 이 라벨을 템플릿에서 .으로 접근해서 쓴다!!
    #그리고 보니까 각 속성마다 에러가 있네
    id = forms.CharField(label="ID", max_length=12, required=True,error_messages=password_errormessages)
    password = \
        forms.CharField(label="PASSWORD", max_length=12,
                        widget=forms.PasswordInput, min_length=6, required=True,
                        error_messages=password_errormessages)
    password_check = \
        forms.CharField(label="PASSWORD(again)", max_length=12,
                        widget=forms.PasswordInput,
                        required=True, min_length=6,
                        error_messages=password_errormessages)
#
# class JoinForm(forms.ModelForm):
#
#     class Meta:
#         #여기에 모델 명 적어주고
#         model = User
#         #여기에 필드명 적어주는거임
#         #그럼 그 필드명에 정의된 타입을 보고 form을 만들어줌
#          필드에 __all__이 가능하다
#         fields = ('username','password')
#         widgets={
#             'username' :
#         }
#         #이렇게 오버라이드 할 수 있음 음..뭐가 더 편한지는 모르겠다
#         labels

