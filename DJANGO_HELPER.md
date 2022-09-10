# DJANGO

## 가상환경 설정

1. python -m venv venv

2. source venv/Scripts/activate

3. pip install -r requirements.txt
   
   - requirements 파일 없으면
   
   - pip install django==3.2.13
   
   - pip install ipython
   
   - pip install django-extensions
     
     - settings.py > INSTALLED_APP > 'django-extensions',
   
   - pip freeze > requirements.txt

## 프로젝트&app생성

1. django-admin startproject {'project name'} [.]
2. (manage.py 가 있는 경로에서 ) python manage.py startapp {'app name'}
   - 앱네임은 복수형으로 만들기
3. settings.py  > INSTALLED_APP >  'appname'

## 인증 시스템 설정

1. python manage.py startapp accounts

2. settings.py > INSTALLED_APP > 'accounts'

3. accounts/urls.py
   
   ```
   from django.urls import path
   from . import views
   
   app_name = 'accounts'
    urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    ]
   ```

4. 프로젝트폴더/urls.py
   
   ```
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
    path('admin/', admin.site.urls),
    path('앱이름/', include('앱이름.urls')),
    path('accounts/', include('accounts.urls')),
    ]
   ```

5. settings.py > AUTH_USER_MODEL = 'accounts.User'

6. accounts/models.py

```
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
 pass
```

7. accounts/admin.py

```
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```

8. python manage.py makemigrations

9. python manage.py migrate

## 관리자 계정생성

1. 관리자 계정생성

2. python manage.py createsuperuser

3. 각 application/admin.py에 Model 추가하기

4. admin.site.register(Article)

## base.html

1. templates 폴더 생성

2. templates 폴더 안에 base.html 만들기

3. 부트스트랩 CDN 작성

4. ```
   {% block content %}
   {% endblock content %}
   ```

5. settings.py > TEMPLATES > DIRS > [BASE_DIR, 'templates',],

6. 각 앱 하위폴더 생성 templates 생성후 하위에 앱이름으로 폴더 생성

7. 각 앱 html 파일에 {% extends 'base.html' %} 를 제일 위에 작성

8.     {% block content %} 과   {% endblock content %} 사이에 내용 작성

## URLS

1. 각 앱에 urls.py 파일 만들기

2. urls.py 작성
   
   ```
   from django.urls import path
   from . import views
   
   app_name = '앱이름'
   urlpatterns = [
      path('<변수>/','html이름/', views.함수이름 , name='함수이름'),
   ]
   ```

3. 앱네임 지정후 *url태그* 에서 반드시 *app_name:url_name* 형태로만 사용

## MODEL

1. 앱/models.py
   
   ```
   class 대문자로시작하는앱이름으로정의(models.Model):
       col_name = models.필드데이터타입(속성)
   ```

2. python manage.py makemigrations

3. python manage.py migrate

4. python manage.py showmigrations

5. models.py 에 변경사항이 생기면 python manage.py makemigrations

6. 빈 값으로 추가 될 수 없어서 기본값 설정해야 함
   
   - 다음화면에서 직접입력
   
   - 현제과정에서 나가고 모델필드에 디폴트 속성 직접작성

7. python manage.py migrate

## MODEL FORM

1. 앱 폴더에 forms.py 생성
   
   ```
   from django import forms
   from .models import Article
   
   class 앱이름Form(forms.ModelForm):
       col_name = forms.필드데이터타입(위젯)
   
       class Meta:
           model = Article
           fields = '__all__'
   ```

2. views.py
   
   ```
   from .forms import 방금만든폼이름
   def 함수이름(request):
       form = 방금만든폼이름()
       context = {
       'form' : form,
       }
       return
   ```

3. 템플릿 업데이트
   
   ```
     <form action="{% url '앱이름:보낼곳' 보낼인자 %}" method="POST">
       {% csrf_token %}
       {{ form.as_p }}
       <input type="submit">
     </form>
   ```
