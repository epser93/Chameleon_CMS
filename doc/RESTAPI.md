# REST API 명세서

| url                                           | GET                 | POST               | PUT                 | DELETE        |
| --------------------------------------------- | ------------------- | ------------------ | ------------------- | ------------- |
| accounts/login/                               |                     | 로그인             |                     |               |
| accounts/signup/                              |                     | 회원가입           |                     |               |
| accounts/logout/                              |                     | 로그아웃           |                     |               |
| accounts/management/                          |                     | 회원가입 승인      | 회원권한 수정       |               |
| products/main/                                | 메인페이지 상세     |                    |                     |               |
| products/main/carousel/                       |                     | 대표페이지 등록    |                     |               |
| products/category/                            | 카테고리 리스트     | 카테고리 생성      |                     |               |
| products/category/<category_id>/              | 카테고리 물품리스트 |                    | 카테고리 수정       | 카테고리 삭제 |
| products/product/                             |                     | 제품생성(임시까지) |                     |               |
| products/product/<product_id>/                | 제품 상세정보       |                    | 제품 수정           | 제품 삭제     |
| products/serarch/?type=<>&content=<>&order=<> | 검색                |                    |                     |               |
| services/notices/                             | 공지사항 리스트     | 공지사항 생성      |                     |               |
| services/notices/<notices_id>/                | 공지사항 상세       |                    | 공지사항 수정       | 공지사항 삭제 |
| services/event/                               | 이벤트 리스트       | 이벤트 생성        |                     |               |
| services/event/<event_id>/                    | 이벤트 상세         |                    | 이벤트 수정         | 이벤트 삭제   |
| services/faq/                                 | FAQ 리스트          | FAQ 생성           |                     |               |
| services/faq/<faq_id>/                        | FAQ 상세            |                    | FAQ 수정            | FAQ 삭제      |
| services/company/                             | 회사 정보           |                    | 회사 정보 수정      |               |
| services/contact/                             | contact 정보        |                    | contact 이미지 수정 |               |
| services/manual/                              | 메뉴얼 데이터       |                    |                     |               |
| services/log/                                 | 로그데이터          |                    |                     |               |



## 로그인

```
주소/api/accounts/login/
```

- Body

```json
{
    "username": "test",
    "password": "test1234!",
}
```

- 성공시 Response

```json
{
    "key": "d32bb74f1bb24bbf3bed0540cf1a88cbe1b0f608"
}
```

- 실패시(아래중에서 나옵니다.)

```json
{
    "message": "존재하지 않는 아이디 입니다.",
    "message": "잘못된 비밀번호 입니다.",
    "message": "관리자 승인이 필요합니다."
}
```



## 로그아웃

```
주소/api/accounts/login/
```

- 성공 Response

```json
{
    "message": "로그아웃 되었습니다."
}
```

- 실패 Response(토큰을 보내지 않을경우)

```json
{
    "message": "로그인되지 않은 유저입니다."
}
```

- 실패 Response(잘못된 토큰을 보내는 경우)

```json
{
    "detail": "토큰이 유효하지 않습니다."
}
```



## 회원가입

```
주소/api/accounts/signup/
```

- Body

```json
{
    "username": "test",
    "password": "test1234!",
    "password1": "test1234!",
    "password2": "test1234!",
    "is_logger": "False",
    "is_eventer": "False",
    "is_producter": "False",
    "is_maketer": "False",
    "department": "인사과",
    "email": "abc@naver.com",
    "employee_number": 749172
}
```

- 성공 Response

```json
{
	"messge": "회원가입이 완료되었습니다. 관리자 승인 후 로그인 해주세요.""
}
```

- 실패 response(아래 중 하나, 400 error)

```json
{
	"messge": "존재하는 아이디 입니다.",
    "messge": "비밀번호가 일치하지 않습니다.",
    "messge": "잘못된 이메일 입니다.",
    "messge": "존재하는 이메일 입니다.",
    "messge": "비밀번호가 조건에 부합하지 않습니다.",
}
```



## 회원가입 승인

```
주소/api/accounts/manage/
```



- Body

```json
{
    "users": [
        1,
        2
    ]
}
```

- 성공 Response

```json
{
    "message" : "승인이 완료되었습니다."
}
```

- 실패 Response(403 error)

```json
{
    "message" : "권한이 없습니다."
}
```





## 카테고리 리스트(수정필요, 관리자, 사용자 분리)

```
주소/api/proudcts/categories/
```

- Response

```json
[
    {
        "id": 1,
        "name": "노트북",
        "is_active": true,
        "priority": 1,
        "created_date": "2020-10-28T17:44:41.924474+09:00",
        "update_date": "2020-10-28T17:44:41.924474+09:00",
        "cms_user": {
            "id": 1,
            "username": "admin",
            "is_access": false,
            "is_eventer": false,
            "is_producter": false,
            "is_marketer": false,
            "department": null
        }
    }
]
```





## 카테고리 생성(수정 필요)

```
주소/api/products/categories/
```

- Body

```json
{
    "name": "김치냉장고",
    "descriptions": [
        "제조사", "디스플레이", "CPU", "GPU", "RAM"
    ],
    "template": 1,
    "priority": 3
}
```

- Response

```json
{
    "id": 6,
    "name": "김치냉장고",
    "is_active": true,
    "priority": 3,
    "created_date": "2020-10-30T16:29:20.547623+09:00",
    "update_date": "2020-10-30T16:29:20.547623+09:00",
    "cms_user": {
        "id": 2,
        "username": "test",
        "is_access": false,
        "is_eventer": false,
        "is_producter": false,
        "is_marketer": false,
        "department": null
    }
}
```



## 카테고리 수정(수정 필요)

```
주소/api/products/categories/6/
```

- Body

```json
{
    "name": "김치냉장고 v2",
    "descriptions_update": [
        {
            "id": 25,
            "name": "전력소모량"
        }
    ],
    "descriptions_delete": [
        23, 24
    ],
    "descriptions_add": [
        "테스트1234"
    ],
    "template": 1,
    "priority": 1
}
```

- Response

```json
{
    "id": 6,
    "name": "김치냉장고 v2",
    "is_active": true,
    "priority": 1,
    "created_date": "2020-10-30T16:29:20.547623+09:00",
    "update_date": "2020-10-30T16:34:14.215469+09:00",
    "cms_user": {
        "id": 2,
        "username": "test",
        "is_access": false,
        "is_eventer": false,
        "is_producter": false,
        "is_marketer": false,
        "department": null
    }
}
```



## 카테고리 삭제(수정필요)

```
주소/api/products/categories/6/
```

- Response

```json
{
    "삭제완료"
}
```



## 카테고리 속한 아이템 보기(수정필요, 관리자, 사용자 분리)

```
주소/api/products/categories/1/
```

- Response

```json
[
    {
        "id": 1,
        "name": "삼성 오디세이",
        "price": 22800000,
        "is_temp": false,
        "is_active": true,
        "created_date": "2020-10-28T17:50:19.413411+09:00",
        "update_date": "2020-10-28T17:50:19.413411+09:00",
        "cms_user": {
            "id": 1,
            "username": "admin",
            "is_access": false,
            "is_eventer": false,
            "is_producter": false,
            "is_marketer": false,
            "department": null
        }
    },
    {
        "id": 5,
        "name": "노트북123",
        "price": 1280000,
        "is_temp": true,
        "is_active": true,
        "created_date": "2020-10-30T15:15:58.430740+09:00",
        "update_date": "2020-10-30T15:15:58.430740+09:00",
        "cms_user": {
            "id": 2,
            "username": "test",
            "is_access": false,
            "is_eventer": false,
            "is_producter": false,
            "is_marketer": false,
            "department": null
        }
    }
]
```





## 아이템 생성

```
주소/api/products/product/
```



- Body

```json
{
    "name": "노트북11",
    "price": 380000,
    "is_temp": "False",
    "category": 1,
    "template": 1,
    "descriptions": [
        {
            "id": 20,
            "content": "AMD"
        }
    ]
}
```

- Response

```json
{
    "id": 7,
    "name": "노트북11",
    "price": 380000,
    "is_temp": false,
    "is_active": true,
    "created_date": "2020-10-30T16:59:20.284650+09:00",
    "update_date": "2020-10-30T16:59:20.284650+09:00",
    "cms_user": {
        "id": 2,
        "username": "test",
        "is_access": false,
        "is_eventer": false,
        "is_producter": false,
        "is_marketer": false,
        "department": null
    }
}
```





## 아이템 수정



## 아이템 삭제

