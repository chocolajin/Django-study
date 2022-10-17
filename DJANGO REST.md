# DJANGO REST

## HTTP

- HyperText Transfer Protocol

- HTML 문서와 같은 리소스(resource, 자원들을 가져올 수 있도록 하는 프로토콜(규칙, 약속)

- 웹 상에서 컨텐츠를 전송하기 위한 약속

-  웹에서 이루어지는 모든 데이터 교환의 기초가 됨

- "클라이언트-서버 프로토콜"이라고도 부름

- 클라이언트와 서버는 다음과 같은 개별적인 메시지 교환에 의해 통신
  
  - 요청(request) : 클라이언트에 의해 전송되는 메시지
  
  - 응답(response) : 서버에서 응답으로 전송되는 메시지

- Stateless (무상태)
  
  - 동일한 연결(connection)에서 연속적으로 수행되는 두 요청 사이에 링크가 없음
  
  - 응답을 마치고 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며
    상태 정보가 유지되지 않음
  
  - 쿠키와 세션을 사용해 서버 상태를 요청과 연결하도록 함

### HTTP Request Methods

- 리소스에 대한 행위를 정의

- 리소스에 대해 수행할 원하는 작업을 나타내는 메서드 모음을 정의

- HTTP verbs 라고도 함

- resource : HTTP요청의 대상
1. GET
   
   - 서버에 리소스의 표현을 요청
   
   - 데이터 검색만 해야함

2. POST
   
   - 데이터를 지정된 리소스에 제출
   
   - 서버의 상태를 변경

3. PUT
   
   - 요청한 주소의 리소스를 수정

4. DELETE
   
   - 지정된 리소스를 삭제

### HTTP response status codes

- 특정 요청이 성공적으로 완료 되었는지 여부를 나타냄
1. Informational responses (100-199)

2. Successful responses (200-299)

3. Redirection messages (300-399)

4. Client error responses (400-499)

5. Server error responses (500-599)

## Identifying resources on the Web

- HTTP요청의 대상을 리소스라고함

- 리소스는 문서, 사진 등 어떤것이 될 수 있음

- 각 리소스는 식별을 위해 URI로 식별됨

### URI

- Uniform Resource Identifier (통합 자원 식별자)

- 인터넷에서 하나의 리소스를 가리키는 문자열

- 가장 일반적인 uri는 웹 주소로 알려진 url

- 특정 이름공간에서 이름으로 리소스를 식별하는 URI는 URN

### URL

- Uniform Resource Locator (통합 자원 위치)

- 웹에서 주어진 리소스의 주소

- 네트워크 상에 리소스가 어디있는지를 알려주기 위한 약속
  
  - 이러한 리소스는 HTML,CSS,이미지 등이 될 수 있음

## Response JSON

### Serialization

- 데이터 구조나 객체 상태를 동일 혹은 다른 컴퓨터 환경에 저장하고, 나중에 재구성 할 수 있는 포맷으로 변환하는 과정

- *어떠한 환경에서도 나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정*

#### serializer()

- 쿼리셋 및 모델 인스턴스와 같은 복잡한 데이터를 JSON,XML 등의 유형으로 쉽게 변환할 수 있는 파이썬 데이터 타입으로 만들어줌

### DRF (django REST framework)

- 장고에서 레스트풀 API서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리

- 장고의 폼 및 모델폼과 유사하게 작동

- pip install djanorestframework

- settings.py > INSTALLES_APPS = ['rest_framework',]

#### ModelSerializer

- ModelSerializer 클래스는 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shortcut제공
  
  1. 모델 정보에 맞춰 자동으로 필드 생성
  
  2. serializer 에 대한 유효성 검사기를 자동으로 생성
  
  3.  .create() 및 .update()의 간단한 기본 구현이 포함됨

- 앱폴더에 serializers.py 파일 생성
  
  ```django
  from rest_framework import serializers
  from .models import Article, Commen
  
  class ArticleListSerializer(serializers.ModelSerializer):
  
      class Meta:
          model = Article
          fields = ('id', 'title', 'content',)
  
  
  class CommentSerializer(serializers.ModelSerializer):
  
      class Meta:
          model = Comment
          fields = '__all__'
          read_only_fields = ('article',)
  
  
  class ArticleSerializer(serializers.ModelSerializer):
      # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
      comment_set = CommentSerializer(many=True, read_only=True)
      comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
  
      class Meta:
          model = Article
          fields = '__all__'
  
  
  ```

- many옵션
  
  - 단일 객체 인스턴스 대신 쿼리센 또는 객체 목록을 serializer하려면 many=True

#### Build RESTful API

- api_view decorator
  
  - DRF view 함수가 응답해야 하는 HTTP 메서드 목록 받음
  
  - 기본적으로 GET메서드만 허용되며 다른 메서드 요청에 대해서는 405 Method Not Allowed로 응답

- 게시글 데이터 생성
  
  - 요청에 대한 데이터 생성이 성공한 경우 201 Created, 실패한경우 400 Bad request응답

- Raising an exception on invalid data
  
  - 유효하지 않은 데이터에 대해 예외 발생시키기
  
  -  is_valid()는 유효성 검사 오류가 있는 경우 ValidationError 예외를 발생시키는
    선택적 raise_exception 인자를 사용할 수 있음
  
  - DRF에서 제공하는 기본 예외 처리기에 의해 자동으로 처리되며
    기본적으로 HTTP 400 응답을 반환

- 게시글 데이터 삭제
  
  - 요청에 대한 데이터 삭제가 성공 했을 경우 204 No Content

- 게시글 수정
  
  - 요청에 대한 데이터 수정이 성공 했을 경우 200 OK

- .save()
  
  - 세이브 메서드는 특정 Serializer 인스턴스를 저장하는 과정에서 추가적인 데이터를 받을 수 있음

- read_only_fields
  
  - 외래 키 필드를 읽기 전용 필드로 설정
  
  - 읽기 전용 필드는 데이터를 전송하는 시점에 해당 필드를 유효성 검사에서 제와시키고 데이터 조회 시에는 출력하도록 함

- 특정 게시글에 작성된 댓글 목록 출력하기
  
  - 기존 필드 override
  
  - 게시글 조회 시 해당  게시글의 댓글 목록까지 함께 출력하기
  
  - Serializer는 기존 필드를 override하거나 추가적인 필드를 구성 할 수 있음
    
    1. PrimaryKeyRelatedField()
    
    2. Nested relationships
       
       - 모델 관계상으로 참조 된 대상은 참조하는 대상의 표현에 포함되거나 중첩 될 수 있음
       
       - 이러한 중첩 관계는 serializers를 필드로 사용하여 표현 가능
       
       - 두 클래스의 상/하 위치 변경

- 특정  게시글에 작성된 댓글의 개수 출력
  
  - 새로운 필드 추가
  
  - source
    
    - 필드를 채우는데 사용할 속성의 이름
    
    - 점 표기법을 사용하여 속성을 탐색할 수 있음

- 특정 필드를 오버라이드 혹은 추가한 경우 리드온리필드가 동작하지 않으니 주의

- get_object_or_404()
  
  - 모델 매니저 오브젝츠에서 get()을 호출하지만, 해당 객체가 없을 땐 기존 DoseNotExist 예외대신 Http404를 raise함

- get_list_or_404()
  
  - 모델 매니저 오브젝츠에서 filter()의 결과를 반환하고, 해당 객체 목록이 없을 땐 Http404를 raise함

```django

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment




@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        # comments = Comment.objects.all()
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    


@api_view(['POST'])
def comment_create(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

```


