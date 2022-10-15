# DJANGO BASIC

## Dynamic Web Page
- 사용자의 요청에 따라 웹 페이지에 추가적인 수정이 되어 클라이언트에게 전달되는 웹 페이지
- 웹 페이지의 내용을 바꿔주는 주체 == 서버
- 서버에서 동작하고 있는 프로그램이 웹 페이지를 변경해줌
## MVT패턴
- MVC패턴의 기반으로 변형된 패턴
  - model(데이터) -view(화면) - controller(명령연결)
  - 관심사 분리, 독립적 개발, 개발의 효율성 및 유지보수의 장점
- 장고의 MVT 디자인 패턴
  - model : 데이터 로직 관리
  - template : 레이아웃과 화면 처리
  - view : 로직 처리, 응답 반환, 클라이언트의 요청에 대해 처리를 분기하는 역할
    - 데이터가 필요하면 모델에 접근해서 데이터를 가져옴
    - 가져온 데이터를 템플릿으로 보내 화면을 구성하고
    - 구성된 화면을 응답으로 만들어 클라이언트에게 반환
## view
### render()
주어진 템플릿을 주어진 컨텍스트 데이터와 결합하고 렌더링 된 텍스트와 함께 HttpRespones(응답) 객체를 반환하는 함수
1. request
- 응답을 생성하는 데 사용되는 요청 객체
2. template_name
- 템플릿의 전체 이름 또는 템플릿 이름의 경로 
3. context
- 템플릿에서 사용할 데이터 (딕셔너리 타입으로 작성)
## Template
데이터 표현을 제어하는 도구이자 표현에 관련된 로직
장고 템플릿을 이용한 html 정적 부분과 동적 컨텐츠 삽입
### django template language(DTL)
장고에서 제공하는 빌트인 템플릿 시스템
- 조건, 반복, 변수 치환, 필터 등
- 파이썬 처럼 일부 프로그래밍 구조(if,for)를 사용 할 수 있지만, 파이썬 코드로 실행되는 것이 아님
#### DTL Syntax
1. Variable
- {{ variable }}
- 변수명은 영어, 숫자와 밑줄의 조합으로 구성, 밑줄로 시작 불가, 공백이나 구두점 불가
- *dot(.)를 사용하여 변수 속성에 접근 가능* 인덱스 및 딕셔너리 키값에 접근
- render()의 세번째 인자로 {'key':value} 와 같이 딕셔너러 형태로 넘겨주며, 여기서 정의한 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
2. Filters
- {{ variable | filter}}
- 표시할 변수를 수정 할 때 사용
- 60개의 빌트인 필터 제공, 일부 필터는 인자를 받기도 함
3. Tags
- {% tag %}
- 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일 수행
- 일부 태그는 시작과 종료 필요
4. Comments
- {# #}
- {% comment %}{% endcomment %}
- 주석
### Template inheritance
템플릿 상속
코드의 재사용성, 하위 템플릿이 재정의 할 수 있는 블록을 정의하는 가본 'skeleton' 템플릿을 만들 수 있음
- {% extends '' %} 자식이 부모 템플릿을 확장한다는 것을 알림
- *반드시 최상단에 작성되어야 함(두 개 이상 사용 불가)*
- {% block content %}{% endblock content %}
- 하위 템플릿에서 재지정 할 수 있는 블록 정의
- 하위 템플릿이 채울 수 있는 공간
- 가독성을 높이기 위해 선택적으로 엔드블록 태그에 이름 지정
- 템플릿 경로 추가하기
  - 기본 템플릿 경로가 아닌 다른 경로를 추가하기 위해 다음과 같은 코드 작성
  - settings.py > TEMPLATES = [ { 'DIRS': [BASE_DIR / 'templates']},]
  - 최상단에 templates 폴더 생성 후 base.html 넣기
- BASE_DIR : settings.py에서 특정 경로를 절대 경로로 편하게 작성할 수 있도록 장고에서 미리 지정해 둔 경로 값
## Sending form data
### form
데이터가 전송되는 방법을 정의
웹에서 사용자가 정보를 입력하는 여러 방식을 제공하고, 사용자로부터 할당된 데이터를 서버로 전송하는 역할
1. action
- 입력 데이터가 전송될(어디로 보낼래?) URL(유효한)을 지정
- 지정하지 않으면 현재 form이 잇는 페이지의 url로 보내짐
2. method
- 데이터를 어떻게 보낼 것인지 정의
- 입력 데이터의 HTTP request methods를 지정
- HTML form 데이터는 오직2가지 방법으로만 전송 가능 (GET, POST)
3. input
- 사용자로부터 데이터를 입력 받기 위해 사용
- 'type' 속성에 따라 동작 방식 달라짐(기본값:text)
- name
  - form을 통해 데이터를 제출 했을 때 name 속성에 설정된 값을 서버로 전송하고, 서버는 name 속성에 설정된 값을 통해 사용자가 입력한 데이터 값에 접근 가능
  - 주요 용도는 GET/POST 방식으로 서버에 전달하는 파라미터(name=key,value=value)로 매핑하는 것
  - GET방식에서는 URL에서 '?key=value&key=value/'형식으로 데이터를 전달
### HTTP
- HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약)
- 웹에서 이루어지는 모든 데이터 교환의 기초
- HTTP는 주어진 리소스가 수행 할 원하는 작업을 나타내는 request method를 정의
#### HTTP request methods
- 자원에 대한 행위(수행하고자하는 동작)을 정의
- 주어진 리소스(자원)에 수행하길 원하는 행동을 나타냄
### GET
서버로부터 정보를 *조회*하는 데 사용
- 서버에게 리소스를 요청하기 위해 사용
- 데이터를 가져올 때만 사용해야 함
- 데이터를 서버로 전송할 때 쿼리스트링파라미터를 통해 전송
  - *데이터는 URL에 포함되어 서버로 보내짐*
- Query String Parameters
  - 사용자가 입력 데이터를 전달하는 방법 중 하나로, url주소에 데이터를 파라미터를 통해 넘기는 것
  - 이 문자열은 &로 연경된 키=밸류 쌍으로 구성되며 기본URL과 ?로 구분
  - Query String 이라고도 함
  - 정해진 주소 이후에 물음표를 쓰는 것으로 Query String이 시작함을 알림
  - 파라미터가 여러 개일 경우 &를 붙여 여러개의 파라미터를 넘길 수 있음
### Retrieving the data (Server)
데이터 가져오기(검색하기)
- 서버는 클라이언트로부터 받은 키밸류 쌍의 목록과 같은 데이터를 받게 됨
- 이 목록에 접근하는 방법은 사용하는 특정 프레임워크에 따라 다름
- *모든 요청 데이터는 뷰 함수의 첫번째 인자 request에 들어있다*
### Request and Respones objects
요청과 응답 객체 흐름
1. 페이지가 요청되면 장고는 요청에 대한 메타데이터를 포함하는 HttpRequest object를 생성
2. 해당하는 적절한 뷰 함수를 로드하고 HttpRequest를 첫번째 인자로 전달
3. 마지막으로 뷰 함수는 HttpRequest object를 반환
## URLS
웹 어플리케이션은 URL을 통한 클라인언트의 요청에서부터 시작
### Trailing URL Slashes
- 장고는 url끝에 / 가 없다면 자동으로 붙여주는 것이 기본 설정.
- 복수의 페이지에서 같은 콘텐츠가 존재하는 것을 방지하기 위해 정규 URL을 명시
### Variable routing
- URL주소를 변수로 사용하는 것
- URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음
- 변수 값에 따라 하나의 path에 따라 여러 페이지를 연결 시킬 수 있음
- *변수는 <>에 정의, 뷰 함수의 인자로 할당 됨*
- Variable routing으로 할당된 변수를 뷰함수에서 인자로 받고 템플릿 변수로 사용 할 수 있음
- 라우팅: 어떤 네트워크 안에서 통신 데이터를 보낼 때 최적의 경로를 선택하는 과정
1. str
- /를 제외하고 비어있지 않은 모든 문자열, 작성하지 않을 경우 기본 값
2. int
- 0또는 양의 정수
### App URL mapping
- 앱이 많아졌을 떄 urls.py를 각 앱에 매핑하는 방법
- 앱의 뷰함수가 많아지면 사용하는 path() 또한 많아지고, 앱또한 더 많이 작성되기 때문에 프로젝트의 urls.py에서 모두 관리하는 것은 프로젝트 유지보수에 좋지 않음
- 각 앱안에 urls.py를 만들고 프로젝트 urls.py에서 각 앱의 urls.py 파일로 URL매핑을 위탁할 수 있음
#### including other URLconfs
- urlpattern은 언제든지 다른 URLconf 모듈을 포함 할 수 있음
- *include 되는 앱의 urls.py에 urlpatterns가 작성되어 있지 않으면 에러가 발생하므로 빈 리스트라도 있어야 함* 
- include()
  - 다른 URLconf들을 참조 할 수 있도록 돕는 함수
  - include()를 만나면 URL의 그 시점까지 일치하는 부분을 잘라내고, 남은 문자열 부분을 후속 처리를 위해 include된 URLconf로 전달
#### Naming URL patterns
- 링크에 URL을 직접 작성하는 것이 아니라 path()함수의 name인자를 정의해서 사용
- {% url ''%} 
  - 주어진 url패턴 이름 및 선택적 매개 변수와 일치하는 절대 경로 주소를 반환
  - 템플릿에 URL을 하드 코딩하지 않고 DRY원칙(Don't Repeat Yourself) 위반하지 않으면서 링크 출력하는 방법
#### Namespace
- url namespace를 사용하면 서로 다른 앱에서 동일한 url 이름을 사용하는 경우에도 이름이 지정된url 을 고유하게 사용가능
  ```
  from django.urls import path
  from . import views
  app_name = '앱이름'
  urlpatterns = [
      path('<변수 >/html이름 /', views.함수 , name='url이름'),
  ]
  ```
- 장고는 기본적으로 app_name/templates/경로에 있는 templates 파일들만 찾을 수 있으며, settings.py의 INSTALLED_APPS 에 작성한 순서로 template 검색 후 렌더링 함
- url tag 를   ``` <form action="{% url '앱이름:url이름' %}"> ``` 로 적는다.
  - 저렇게 안하면 NoReverseMatch
- 폴더구조
  - app_name/templates/app_name/
- views.py 함수 리턴 경로
  ```
  return render(request, '앱이름/html이름.html')
  ```
## 장고 설계 철학
1. 표현과 로직을 분리
- 템플릿 시스템은 표현을 제어하는 도구이자 표현에 관련된 로직일 뿐
2. 중복을 배제
- 공통되는 디자인은 한 곳에 저장하기 쉽게 하여 중복코드를 없애야 함

## Database

### Schema 스키마

- 뼈대(Structure)

- 데이터베이스에서 자료의 구조, 표현방법, 관계 등을 정의한 구조

### Table 테이블

- 필드와 레코드를 사용해 조직된 데이터 요소들의 집합

- 관계(Relation) 라고도 부름
  
  1. 필드(field)
     
     - 속성,컬럼(Column)
     
     - 각 필드에 고유한 데이터 형식 지정
  
  2. 레코드(record)
     
     - 튜플,행(Row)
     
     - 데이터 저장
  
  3. PK(Primary Key)
     
     - 기본 키
     
     - 각 레코드의 고유값(식별자로 사용)
     
     - 다른 항목과 중복되지 않는 단일 값

### Query 쿼리

- 데이터를 조회하기 위한 명령어

- 조건에 맞는 데이터를 추출하거나 조작하는 명령어

- 쿼리를 날린다. = 데이터베이스를 조작한다.

## Model

- 개요
  
  - *웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 도구*
  
  - 장고는 모델을 통해 데이터에 접속하고 관리
  
  - 단일한 데이터에 대한 정보 가짐
  
  - 사용자가 저장하는 데이터들의 필수적인 필드들과 동작 포함
  
  - 저장된 데이터 베이스의 구조
  
  - 일반적으로 각각의 모델은 하나의 데이터 베이스 테이블에 매핑
    
    - 매핑 : 하나의 값을 다른 값으로 대응시킴
  
  - 모델 클래스 작성 == 테이블 스키마 정의
  
  - 모델 클래스1개 == 데이터 베이스 테이블 1개

- 이해 
  
  - 각 모델은 django.db.models 모듈의 Model클래스 상속
    
    ```
    from django.db import models
    
    class 클래스이름 (models.Model): # 상속 
        클래스 변수(속성)명 (#DB필드의 이름) = models.db필드의 데이터 타입(#클래스 변수 값. models모듈의 field클래스 )### Django Model Field
    ```

### Django Model Field

[Model field reference | Django documentation | Django](https://docs.djangoproject.com/en/3.2/ref/models/fields/)

- 장고는 모델 필드를 통해 테이블의 필드(컬럼)에 저장할 데이터 유형을 정의

- 데이터 유형에 따라 다양한 모델 필드 정의

- CharField
  
  - CharField(*max_length=None*, ***options*)
  
  - 길이의 제한이 있는 문자열 넣을때 사용
  
  - max_length
    
    - 필드 최대 길이(문자)
    
    - 필수 인자
    
    - *유효성검사* 에 활용

- TextField(**options)
  
  - 글자 수 많을 때 사용
  
  - *유효성 검증 안함*
  
  - max_length옵션 작성 시 사용자 입력 단계에서는 반영되지만, 모델과 데이터베이스 단계에서는 적용 안됨

- DateTimeField
  
  - DateField 상속받는 클래스
  
  - DateTimeField(auto_now_add=True)
    
    - 최초 생성 일자
  
  - DateTimeField(auto_now=True)
    
    - 최종 수정 일자

### Migrations

- 모델의 청사진을 만들고 이를 통해 테이블을 생성하는 일련의 과정

- 장고가 모델에 생긴 변화를 DB에 반영하는 방법
  
  #### makemigrations
  
  - 모델을 작성, 변경한 것에 기반한 새로운 설계도를 만들 때 사용
  
  - python manage.py makemigrations
  
  - migrations/0001_initial.py 생성됨
  
  #### migrate
  
  - 설계도를 실제 db.sqlite3 DB파일에 반영하는 과정
  
  - 모델과 DB의 동기화
  
  - python manage.py migrate

```
models.py
def __str__(self):
    return self.title
```

표준 파이썬 클래스 메서드인 str()을 정의하여 각각의 오브젝트가 사람이 읽을 수 있는 문자열을 반환

### ORM

- Object-Relational-Mapping

- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 (Django <-> SQL) 데이터를 변환하는 프로그래밍 기술

- 객체 지향 프로그래밍에서 데이터베이스를 연동할 때, 데이터 베이스와 객체 지향 프로그래밍 언어 기능이 호환되지 않는 데이터를 변환하는 프로그래밍 기법

- 장고는 내장 장고 orm을 사용
  
  - 장점 : SQL을 몰라도 객체지향 언어로 DB조작 가능, **높은 생산성**
  
  - 단점 : ORM만으로 완전한 서비스 구현 여러움

## QuerySet API

*쿼리셋과 상호작용하기 위해 사용하는 도구(네서드, 연산자 등)*

- Database API
  
  - 모델의 만들면 장고는 객체들을 만들고 읽고 수정하고 지울 수 있는 DB API를 자동으로 만듦
  
  - ModelClass.Manager.QuerysetAPI()

- 'objects' manager
  
  - 장고 모델이 데이터베이스 쿼리 작업을 가능하게  하는 인터페이스
  
  - 장고는 기본적으로 모든 장고 모델 클래스에 대해 오브젝츠라는 매니저 객체를 자동으로 추가함
  
  - 이 매니저(오브젝츠)를 통해 특정 데이터를 조작 할 수 있음
  
  - *DB를 파이썬 클래스로 조작 할 수 있도록 여러 메서드를제공하는 매니저*

- Query
  
  - 데이터 베이스에 특정한 데이터를 보여 달라는 요청
  
  - 쿼리문을 작성한다 : 원하는 데이터를 얻기 이해 데이터 베이스에 요청을 보낼 코드를 작성한다.
  
  - 이 때, 파이썬으로 작성한 코드가 ORM에 의해 SQL로 변환되어 데이터베이스에 전달되며, 데이터 베이스의 응답 데이터를 ORM이 QuerySet이라는 자료 형태로 변화하여 우리에게 전달

- QuerySet
  
  - *데이터 베이스에게서 전달 받은 객체 목록(데이터 모음)*
  
  - 순회가능, 1개 이상 데이터를 불러와 사용 가능
  
  - 장고 ORM을 통해 만들어진 자료형
  
  - 필터를 걸거나 정렬 등을 수행할 수 있음
  
  - 오브젝츠 매니저를 사용하여 복수의 데이터를 가져오는 쿼리셋 매서드를 사용 할 때 반환되는 객체
  
  - 단, 데이터베이스가 단일한 객체를 반환 할 때는 쿼리셋이 아닌 모델의 클래스 인스턴스로 반환된다.

- QuerySet API
  
  - QuerySet과 상호작용하기 위해 사용하는 도구

### Create

- 방법 1
  
  - 클래스를 통한 인스턴스 생성 
  
  - 클래스 변수명과 같은 이름의 인스턴스 변수를 생성 후 값 할당
  
  - 인스턴스 세이브 메서드 호출
  
  ```
  article = Article()
  article.title = 'data'
  article.save()
  ```

- 방법 2
  
  - 인스턴스 생성 시 초기 값을 함께 작성하여 생성
  
  - 인스턴스 세이브 메서드 호출
  
  ```
  article = Article(title='data',content='data')
  article.save()
  ```

- 방법 3
  
  - create() 메서드 사용
  
  ```
  Article.objects.create(title='data',content='data')
  ```

### READ

- all()
  
  - 전체 데이터 조회
  
  - Article.objects.all()

- get()
  
  - **단일** 데이터 조회
  
  - 못찾으면 *DoseNotExist*
  
  - 둘 이상이면 *MultipleObjectsReturned*
  
  - *고유성을 보장(pk)하는 조회에 사용*
  
  - Article.objects.get(pk=1)
  
  - Article.objects.get(title='data')

- filter()
  
  - 지정된 조회 매개 변수와 일치하는 객체를 포함하는 새 쿼리셋 반환
  
  - 조회된 객체가 없거나 1개여도 쿼리셋 반환
  
  - Article.objects.filter(title='data')

- Field lookups
  
  - 특정 레코드에 대한 조건을 설정하는 방법
  
  - 쿼리셋 메서드 필터,익스클루드 및 겟에 대한 키워드 인자로 지정됨
  
  - ex)  Article.objects.filter(content__contains='dj')
  
  - [QuerySet API reference | Django documentation | Django](https://docs.djangoproject.com/en/4.1/ref/models/querysets/#field-lookups)

### UPDATE

1. 수정하고자 하는 인스턴스 객체를 조회 후 반환 값을 저장

2.  인스턴스 객체의 인스턴스 변수 값을 새로운 값으로 할당

3.  save() 메서드 호출

### DELETE

1.  삭제하고자 하는 인스턴스 객체를 조회 후 반환 값 저장

2.  delete() 인스턴스 메서드 호출

### redirect()

- 인자에 작성된 곳으로 요청을 보냄
  
  1. 클라이언트가 요청을 보냄
  
  2. 뷰 함수의 redirect 함수가 302status code 를 응답(브라우저는 사용지를 해당 url페이지로 이동시킴)
  
  3. 응답 받은 브라우저는 redirect 인자에 담긴 주소로 사용자를 이동시키기 위해 url로 장고에 재요청
  
  4. 페이지 정상 응답 200status code

### HTTP request method

- get
  
  - 특정 리소스를 가져오도록 요청할 때 사용
  
  - 반드시 데이터를 가져올 때만 사용
  
  - DB에 변화 주지 않음
  
  - Read 역할

- post
  
  - 서버로 데이터 전송할 때 사용
  
  - 서버에 변경사항 만듦
  
  - 리소스를 생성/변경하기 위해 데이터를 HTTP body에 담아 전송
  
  - get쿼리 스트링 파라미터와 다르게 url로 보내지지 않음
  
  - C/U/D 역할

- 403Forbidden
  
  - 서버에 요청이 전달되었지만, 권한 때문에 거절되었다는 의미
  
  - 작성자가 누군지 몰라서 함부로 작성 못해

- CSRF
  
  - cross-site-request-forgery
  
  - 사이트 간 요청 위조
  
  - 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 보안에 취약하게 하거나 수정, 삭제 들의 작업을 하게 만드는 공격 방법
  
  - Security Token
    
    - 사용자의 데이터에 임의의 난수 값을 부여해 매 요청마다 해당 난수 값을 포함시켜 전송
    
    - 이후 서버에서 요청 받을 때마다 전달된 토큰 값이 유효한지 검증
    
    - 일반적으로 데이터 변경이 가능한 post,patch,delete 등에 적용
  
  - {% csrf_token %}
    
    - 이 태그가 없으면 403Forbidden
    
    - 템플릿에서 내부 url로 향하는 postform 사용하는 경우에 사용
    
    - 외부 url로 향하는 post form은 토큰이 유출되어 취약성 유발, 사용 금지

## Admin

- 모델의 레코드를 보기 위해서는 admin.py에 등록 필요
  
  ```
  from django.contrib import admin
  from .models import 모델명
  admin.site.register(모델)
  ```