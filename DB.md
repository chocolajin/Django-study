# DB

## Intro
- 데이터베이스는 많은 형태가 있지만 실제 가장 많이 쓰이는 유형은 Relational DataBase 관계형 데이터베이스
- 데이터베이스를 사용하면 데이터를 안전하고 편리하고 빠르게 보관하고 사용할 수있음
- Database
  - 체계화된 데이터의 모임
  - 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합
  - 검색, 구조화 등의 작업을 보다 쉽게함
  - 데이터베이스를 조작하는 프로그램 = DBMS (Database Management System)
### RDB 관계형 데이터베이스
- 데이터를 테이블 행, 열 등으로 나누어 구조화 하는 방식
- 자료를 여러 테이블로 나누어 관리하고, 이 테이블 간 관계를 설정해 여러 데이터를 쉽게 조작할 수 있다는 장점
- SQL을 사용하여 데이터를 조회하고 조작
- 데이터를 직관적으로 표현
- 쉬운 접근
- 대량의 데이터도 효율적으로 관리가능
1. 스키마
- 테이블의 구조
- 데이터베이스에서 자료의 구조, 표현방법, 관계 등 전반적인 명세를 기술
2. 테이블
- 필드와 레코드를 사용해 조직된 데이터 요소들의 집합
  1. 필드
  - 속성 혹은 컬럼
  - 각 필드에는 고유한 데이터 형식 지정
  2. 레코드
  - 튜플 혹은 행
  - 테이블의 대이터는 레코드에 저장
  3. PK (primary key)
  - 기본 키
  - 각 레코드의 고유한 값
  - 단일 값
## SQL
- structured query language
- RBDMS의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어
- 데이터와 상호작용하는 방법
- ### SQL Commands
1. DDL(data definition language) - 데이터 정의 언어
- 테이블, 스키마를 생성, 수정, 삭제하기 위한 명령어
- CREATE DROP ALTER
2. DML(data manipulation language) - 데이터 조작 언어
- 데이터를 추가, 조회, 변경, 삭제하기 위한 명령어
- INSERT SELECT UPDATE DELETE
3. DCL(data control language) - 데이터 제어 언어
- 데이터의 보안, 수행제어, 사용자 권한 부여등을 정의하기 위한 명령어
- GRANT REVOKE COMMIT ROLLBACK
### SQL Syntax
- 모든 sql문(statement)은 키워드로 시작하고, 하나의 문은 세미콜론(;)으로 끝남
- 대소문자 구분 않지만 대문자 작성 권장
- statement는 clause절로 구성 됨
## DDL
### CREATE TABLE

1. mydb.sqlite3 파일 만들기

2. DDL.sql 파일 만들기

3. 2번파일에서 우클릭 > use database > 1번파일 클릭

4. 테이블 만들기

```
CREATE TABLE 테이블이름(
컬럼이름 데이터타입 제약조건,
컬럼이름 데이터타입 제약조건);
```

- 실행하고자하는 테이블 문장 안안에서 우클릭 후 run selested query

- 1번파일 우클릭 > open database > 좌측하단 SQLITE EXPLORER 에서 확인
- id 컬럼은 직접 기본키 역할의 컬럼을 정의하지 않으면 자동으로 rowid라는 컬럼으로 만들어짐
- 
### DATA TYPES

1. NULL : 정보가 없거나 알 수 없음

2. INTEGER : 정수

3. REAL : 실수

4. TEXT : 문자

5. BLOB : 입력된 데이터 덩어리

6. Boolean 은 0과1로 저장

7. 날짜는 함수로 처리

#### TYPE AFFINITY

타입선호도 : 특정 컬럼에 저장된 데이터에 권장되는 타입

다른 데이터 베이스엔진간의 호환성 최대화

- INTEGER TEXT BLOB REAL NUMERIC

### CONSTRAINTS

- 제약조건
  
  - 입력하는 자료에 대한 제약을 정하고 맞지 않으면 입력 거부
  
  - 사용자가 원하는 조건의 데이터만 유지하기 위한, 데이터의 무결성을 유지하기 위한 보편적인 방법으로 테이블의 특정 컬럼에 설정하는 제약

- 데이터 무결성
  
  - 데이터 베이스 내의 데이터에 대한 정확성, 일관성을 보장하기 위해 데이터 변경 혹은 수정 시 여러 제한을 두어 데이터의 정확성을 보장하는 것
  
  - 무결성이란 데이터의 정확성, 일관성을 나타냄
  
  - 데이터 베이스에 저장된 데이터 무결성을 보장하고 데이터베이스의 상태를 일관되게 유지하는 것이 목적
1. NOT NULL
   
   - 컬럼이 NULL값을 허용하지 않도록 지정
   
   - 기본적으로 테이블의 모든 컬럼은 NULL값을 허용

2. UNIQUE 
   
   - 컬럼의 모든 값이 서로 구별되거나 고유한 값이 되도록 함

3. PRIMARY KEY 
   
   - 테이블에서 행의 고유성을 식별하는 데 사용되는 컬럼
   
   - 각 테이블에는 하나의 기본 키만 있음
   
   - 암시적으로 NOT NULL 제약 조건이 포함되어있음
   
   -  INTEGER 타입에만 사용가능

4. AUTOINCREMENT
   
   - 사용되지 않은 값이나 이전에 삭제된 행의 값의 재사용 방지
   
   - 장고에서 테이블 생성 시 ID컬럼에 기본적으로 사용하는 제약조건
   
   - INTEGER PRIMARY KEY 다음에 작성하면 해당rowid를 다시 재사용하지 못하도록 함 
     
     - 테이블 생성 시 rowid라는 암시적 자동 증가 컬럼이 자동으로 생성
     
     - 테이블의 행을 고유하게 식별하는 64비트 부호 있는 정수 값
     
     - 테이블에 새 행을 삽입할 때마다 정수 값을 자동으로 할당
     
     - 1에서 시작
     - 데이터 삽입 시에 rowid 또는 INTEGER PRIMARY KEY 컬럼에 명시적으로
값이 지정되지 않은 경우, SQLite는 테이블에서 가장 큰 rowid보다 하나 큰
다음 순차 정수를 자동으로 할당 (AUTOINCREMENT와 관계없이)
     
     - 만약 INTEGER PRIMARY KEY 키워드를 가진 컬럼을 직접 만들면 이 컬럼은 rowid 컬럼의
별칭(alias)이 됨
즉, 새 컬럼 이름으로 rowid에 액세스 할 수 있으며 rowid 이름으로도 여전히 액세스 가
능
     - 데이터가 최대 값에 도달하고 새 행을 삽입하려고 하면 SQLite는 사용되지 않는 정수를 찾아
사용
     - 만약 SQLite가 사용되지 않은 정수를 찾을 수 없으면 SQLITE_FULL 에러가 발생
     - 또한 일부 행을 삭제하고 새 행을 삽입하면 SQLite는 삭제된 행에서 rowid 값을
재사용하려고 시도
### ALTER TABLE
- 기존의 테이블 구조를 수정
1. ALTER TABLE RENAME : 테이블 이름 변경
```
 ALTER TABLE tablename RENAME TO newtablename
```
2. ALTER TABLE RENAME COLUMN : 컬럼명 변경
```
ALTER TABLE tablename RENAME COLUMN columnname TO newcolumnname;
```
3. ALTER TABLE ADD COLUMN : 새 컬럼 추가
```
ALTER TABLE tablename ADD COLUMN column_definition;
```
- 테이블에 기존 테이터가 있을 경우 다음과 같은 에러 발생
  - Cannot and NOT NULL column with default value NULL
  - 새로 추가되는 컬럼에 낫널 제약조건 때문에 기본 값 없이는 주가 될 수 없음
  - default 제약 조건으로 해결
  - 예시 `ALTER TABLE tablename ADD COLUMN address TEXT NOT NULL DEFAULT 'no address;`
4. ALTER TABLE DROP COLUMN : 컬럼 삭제
```
ALTER TABLE tablename DROP COLUMN columnname;
```
- 삭제 불가한 경우
  - 컬럼이 다흔 부분에서 참조되는 경우(외래키)
  - PK
  - UNIQUE
### DROP TABLE
```
DROP TABLE tablename;
```
- 존재하지 않는 테이블을 제거하면 오류발생
- 한 번에 하나의 테이블만 삭제
- 여러테이블 제거하려면 DROP TABLE문을 실행
- 취소나 복구 불가
## DML
### Simple query
- select문으로 데이터 조회
```
- SELECT column1, column2 FROM tablename;
```
1. SELECT절에서 컬럼 또는 쉼표로 구분된 컬럼 목록 지정
2. FROM 절에서 데이터를 가져올 테이블 지정
```SELECT * FROM tablename;```
3. 전체 데이터 조회
### Sorting rows
#### ORDER BY 
  - 쿼리셋을 정렬한 결과 반환
```
SELECT column1, column2 FROM tablename ORDER BY column1 ASC, column2 DESC;
```
- ASC : 오름차순
- DESC : 내림차순
- NULL의 정렬 : 다른 값보다 작은 것으로 간주
### Filtering data
데이터를 필터링하여 중복제거, 조건 설정 등 쿼리 제어
#### DISTINCT
- 조회 결과에서 중복된 행 제거
1. SELECT 바로 뒤
2. DISTINCT 뒤에 컬럼 또는 컬럼 목록 작성
```
SELECT DISTINCT column1, column2 FROM tablename;
SELECT DISTINCT column1, column2 FROM tablename ORDER BY column1;
```
- NULL을 중복 값으로 간주
- NULL값이 있는 컬럼에 DISTINCT절을 사용하면 NULL 값의 한 행을 유자
#### WHERE
```
SELECT column1, column2 FROM tablename WHERE search_condition;
```
- 조회 시 특정 조건 지정
- update, delete 문에도 사용 가능
- from 절 뒤에 작성
- 검색 조건 작성 형식
  - 비교 연산자: = <= >= != < >
  - 논리 연산자
    - 1,0 또는 NULL 반환
    - ALL AND ANY BETWEEN IN LIKE NOT OR
##### LIKE
- 패턴 일치를 기바능로 데이터 조회
- SELECT, DELETE, UPDATE 문의 WHERE 절에서 사용
- 대소문자 구분 않음
- % : 0개 이상의 문자가 올 수 있음
  - '김%' : 김으로 시작하는 모든 문자열과 일치
  - '%김' : 김으로 끝나는 모든 문자열과 일치
  - '%강원%' : 강원을 포함하는 모든 문자열과 일치
- _ : 단일(1개) 문자 있음
  - '김_' : 김으로 시작하고 총 2자리인 문자열과 일치
  - '__김' : 김으로 끝나고 총 3자리인 문자열과 일치
- _2% : 첫 째 자리 아무값, 두번째가 2로 시작하는 패턴 최소2자리
- 2_%_% OR 2__% : 2로 시작하는 최소3자리 패턴
##### IN
- 값이 값 목록에 있는 값과 일치하는지 확인
- true false 반환
- 부정 NOT IN
```
SELECT column1, column2 FROM tablename WHERE column1 IN (list of value);
```
##### BETWEEN
- 값이 범위에 있는지 테스트
- 지정된 범위에 있으면 true 반환
- SELECT, DELETE, UPDATE 문의 WHERE 절에서 사용
- 부정 NOT BETWEEN
- test_expression BETWEEN low_expression AND high_expression
#### LIMIT
```
SELECT column1, column2 FROM tablename LIMIT row_count;
```
- 쿼리에서 반환되는 행 수 제한
- row_count는 반환되는 행 수를 지정하는 양의 정수
##### OFFSET
- 특정 지정된 위치에서부터 데이터 조회
```
SELECT column1, column2 FROM tablename LIMIT row_count OFFSET num;
```
- 11 번째부터 20번째 데이터 조회
### Grouping data
```
SELECT column_1, aggregate_function(column_2)
FROM table_name
GROUP BY column_1, column_2;
```
- "Make a set of summary rows from a set of rows."
- 선택된 컬럼 값을 기준으로 데이터(행)들의 공통 값을 묶어서 결과로 나타냄
- SELECT 문에서 선택적으로 사용가능한 절
- SELECT 문의 FROM 절 뒤에 작성
- WHERE 절이 포함된 경우 WHERE 절 뒤에 작성해야 함
- 각 그룹에 대해 MIN, MAX, SUM, COUNT 또는 AVG와 같은 집계 함수(aggregate function)를 적용하여
각 그룹에 대한 추가적인 정보를 제공할 수 있음
#### Aggregate function
- 값 집합에 대한 계산을 수행하고 단일 값을 반환
- SELECT 문의 GROUP BY 절과 함께 종종 사용됨
- AVG(), COUNT(), MAX(), MIN(), SUM()
- AVG(), MAX(), MIN(), SUM()는 숫자를 기준으로 계산이 되어져야 하기 때문에 반드시
컬럼의 데이터 타입이 숫자(INTEGER)일 때만 사용 가능
- COUNT 참고사항
  - 이전 쿼리에서 COUNT(), COUNT(age), COUNT(last_name) 등 어떤 컬럼을 넣어도 결과는 같음
  - 현재 쿼리에서는 그룹화된 country를 기준으로 카운트 하는 것이기 때문에 어떤 컬럼을 카운트해도 전체 개수는 동일하기 때문
### Changing data
#### INSERT
```
INSERT INTO tablename (col1, col2,...) VALUES (val1,val2,...);
```
- 새 행을 테이블에 삽입
1. INSERT INTO 키워드 뒤에 데이터를 삽입할 데이블 이름 지정
2. 테이블 이름 뒤에 쉼표로 구분된 컬럼 목록 추가
3. 밸류 키워드 뒤에 쉼표로 구분된 값 목록 추가
- 만약 컬럼 목록 생략하는 경우 값 목록의 모든 컬럼에 대한 값 지정해야 함
- 값 목록의 개수는 컬럼 목록의 개수와 같아야 함
#### UPDATE
```
UPDATE tablename
SET col1 = newval1,
    col2 = newval2
WHERE
    search condition;
```
- 테이블에 있는 기존 행의 데이터를 업데이트 한다
1. 업데이트 절 이후에 업데이트 할 테이블 지정
2. SET 절에서 테이블의 각컬럼에 대해 새 값 설정
3. WHERE 절 조건 사용하여 업데이트 할 행 지정 (생략하면 모든 행 업데이트)
4. 선택적으로 ORDER BY 및 LIMIT 절 사용하여 업데이트 할 행 수 지정
#### DELETE
```
DELETE FROM tablename WHERE search condition;
```
- 테이블에서 (하나, 여럿, 모든)행 제거
1. 딜리트 프롬 뒤에 행을 제거하려는 테이블의 이름 지정
2. WHERE 절에 검색 조건 추가하여 제거할 행 식별(생략하면 모든 행 삭제)
3. 선택적으로 ORDER BY 및 LIMIT 절 사용하여 삭제할 행 수 지정