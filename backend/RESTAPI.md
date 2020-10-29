# REST API 명세서

| url                                           | GET             | POST               | PUT              | DELETE        |
| --------------------------------------------- | --------------- | ------------------ | ---------------- | ------------- |
| accounts/login/                               |                 | 로그인             |                  |               |
| accounts/signup/                              |                 | 회원가입           |                  |               |
| accounts/management/                          |                 | 회원가입 승인      | 회원권한 수정    |               |
| products/category/                            | 카테고리 리스트 | 카테고리 생성      |                  |               |
| products/category/<category_id>/              |                 |                    | 카테고리 수정    | 카테고리 삭제 |
| products/product/                             |                 | 제품생성(임시까지) |                  |               |
| products/product/<product_id>/                | 제품 상세정보   |                    | 제품 수정        | 제품 삭제     |
| products/serarch/?type=<>&content=<>&order=<> | 검색            |                    |                  |               |
| templates/                                    | 템플릿 정보     |                    |                  |               |
| templates/<templates_id>/                     |                 |                    | 템플릿 수정      |               |
| templates/main/<item_num>/                    | 메인 정보       |                    | 메인 아이템 수정 |               |



## Accounts

### 로그인

```
주소/api/accounts/login/
```

- Body

```json
{
    "username": "username",
    "password": "password"
}
```

- Response

```json
{
    "key": "c06a4c99de9e8d75c6e6bb4ca543bf0e267942ba"
}
```



### 로그아웃

```
주소/api/accounts/logout/
```

- Response

```json
{
    "detail": "로그아웃되었습니다."
}
```



### 회원가입

```
주소/api/accounts/signup/
```

- Body

```json
{
    "username": "test2",
    "password1": "test1234!",
    "password2": "test1234!",
    "is_logger": "False",
    "is_eventer": "False",
    "is_producter": "False",
    "is_maketer": "False",
    "department": "인사과",
    "employee_number": 749172
}
```



- 승인시 Response

```json
{
    "username": "test2"
}
```



- ID 중복 Response

```json
{
	"username": [
        "해당 사용자 이름은 이미 존재합니다."
    ]
}
```



- passwrod 문제 Response

```json
{
    "password1": [
        "비밀번호가 너무 짧습니다. 최소 8 문자를 포함해야 합니다.",
        "비밀번호가 너무 일상적인 단어입니다."
    ]
}
```



### 회원가입 승인

```
주소/api/accounts/management/
```



- Body

```json
{
    "users": [
        1, 2, 3
    ] 
}
```



- 성공 Response

```json
{
    "message": "승인 완료"
}
```



- superuser가 아닐경우 Response

```json
{
	"message": "권한 없음"
}
```

