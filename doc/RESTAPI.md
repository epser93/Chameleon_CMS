# REST API 명세서

| url                                           | GET                 | POST               | PUT           | DELETE        |
| --------------------------------------------- | ------------------- | ------------------ | ------------- | ------------- |
| accounts/                                     | 자신의 정보         |                    |               |               |
| accounts/search/?조건식                       | 유저 검색(필터링)   |                    |               |               |
| accounts/department/                          | 부서 정보           |                    |               |               |
| accounts/login/                               |                     | 로그인             |               |               |
| accounts/signup/                              |                     | 회원가입           |               |               |
| accounts/logout/                              |                     | 로그아웃           |               |               |
| accounts/manage/<user_id>/                    |                     | 회원가입 승인      | 회원권한 수정 |               |
| products/main/                                | 메인페이지 상세     |                    |               |               |
| products/main/carousel/                       |                     | 대표페이지 등록    |               |               |
| products/template/                            | 템플릿 정보         |                    |               |               |
| products/category/                            | 카테고리 리스트     | 카테고리 생성      |               |               |
| products/category/<category_id>/              | 카테고리 물품리스트 |                    | 카테고리 수정 | 카테고리 삭제 |
| products/product/                             |                     | 제품생성(임시까지) |               |               |
| products/product/<product_id>/                | 제품 상세정보       | 임시정보 생성      | 임시제품 적용 | 제품 삭제     |
| products/serarch/?type=<>&content=<>&order=<> | 검색                |                    |               |               |
| services/notices/                             | 공지사항 리스트     | 공지사항 생성      |               |               |
| services/notices/<notices_id>/                | 공지사항 상세       |                    | 공지사항 수정 | 공지사항 삭제 |
| services/event/                               | 이벤트 리스트       | 이벤트 생성        |               |               |
| services/event/<event_id>/                    | 이벤트 상세         |                    | 이벤트 수정   | 이벤트 삭제   |
| services/log/                                 | 로그데이터          |                    |               |               |



## 로그인

```
주소/api/accounts/login/(post)
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
주소/api/accounts/login/(post)
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
주소/api/accounts/signup/(post)
```

- Body

```json
{
    "username": "test",
    "password1": "test1234!",
    "password2": "test1234!",
    "first_name": "내이름",
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
    "message": "이름이 없습니다.",
	"message": "존재하는 아이디 입니다.",
    "message": "비밀번호가 일치하지 않습니다.",
    "message": "잘못된 이메일 입니다.",
    "message": "존재하는 이메일 입니다.",
    "message": "비밀번호가 조건에 부합하지 않습니다.",
}
```



## 회원가입 승인

```
주소/api/accounts/manage/<int:user_id>/(post)
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



## 회원 권한 변경

```
주소/api/accounts/manage/<int:user_id>/(put)
```

- Body

```json
{
    "is_producter": "False",
    "is_logger": "True",
    "is_eventer": "False",
    "is_marketer": "False"
}
```

- 성공 Response

```json
{
    "id": 3,
    "username": "test1",
    "first_name": "",
    "is_superuser": false,
    "is_access": true,
    "is_logger": true,
    "is_eventer": false,
    "is_producter": false,
    "is_marketer": false,
    "department": {
        "id": 1,
        "name": "인사과"
    },
    "last_login": "2020-11-03T10:19:53.021080+09:00",
    "employee_number": 0
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
        "name": "노트북A",
        "price": 1280000,
        "is_temp": false,
        "is_active": true,
        "created_date": "2020-11-04T00:28:57.816001+09:00",
        "update_date": "2020-11-04T00:28:57.816001+09:00",
        "cms_user": {
            "id": 2,
            "username": "test",
            "first_name": ""
        },
        "descriptions": [
            {
                "content": "AMD",
                "item": 1,
                "category_description": {
                    "id": 1,
                    "name": "제조사"
                }
            }
        ],
        "images": []
    }
]
```





## 아이템 생성(이미지 미완성)

```
주소/api/products/product/(POST)
```



- Body

```json
{
    "name": "노트북A",
    "price": 1280000,
    "is_temp": "False",
    "category": 1,
    "template": 2,
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
    "id": 1,
    "name": "노트북A",
    "price": 1280000,
    "is_temp": false,
    "is_active": true,
    "created_date": "2020-11-04T00:28:57.816001+09:00",
    "update_date": "2020-11-04T00:28:57.816001+09:00",
    "cms_user": {
        "id": 2,
        "username": "test",
        "first_name": ""
    },
    "descriptions": [
        {
            "content": "AMD",
            "item": 1,
            "category_description": {
                "id": 1,
                "name": "제조사"
            }
        }
    ],
    "images": []
}
```



## 아이템 상세 정보

```
주소/api/products/<int:pk>/(GET)
```

- Response

```json
{
    "id": 1,
    "name": "노트북A",
    "price": 1280000,
    "is_temp": false,
    "is_active": true,
    "created_date": "2020-11-04T00:28:57.816001+09:00",
    "update_date": "2020-11-04T00:28:57.816001+09:00",
    "cms_user": {
        "id": 2,
        "username": "test",
        "first_name": ""
    },
    "descriptions": [
        {
            "content": "AMD",
            "item": 1,
            "category_description": {
                "id": 1,
                "name": "제조사"
            }
        }
    ],
    "images": []
}
```





## 아이템 수정(미완성)



## 아이템 삭제(미완성)



## 이벤트 리스트 읽기

```
주소/api/services/event/(GET)
```

- Response

```json
[
    {
        "id": 20,
        "title": "이벤트",
        "start_date": "2020-11-03T18:00:00+09:00",
        "end_date": "2020-11-05T18:00:00+09:00",
        "thumbnail_image": "/media/erd.png",
        "create_date": "2020-11-03T20:59:53.770623+09:00",
        "update_date": "2020-11-03T20:59:53.770623+09:00",
        "priority": 1,
        "user": 2,
        "detail": [
            {
                "image": "/media/KakaoTalk_20201019_093205576.png",
                "content": "테스트1",
                "priority": 1
            },
            {
                "image": "/media/KakaoTalk_20200907_134019738.jpg",
                "content": "테스트2",
                "priority": 2
            }
        ]
    }
]
```





## 이벤트 읽기

```
주소/api/services/event/<int:pk>/(POST)
```

- Response

```json
{
    "id": 20,
    "title": "이벤트",
    "start_date": "2020-11-03T18:00:00+09:00",
    "end_date": "2020-11-05T18:00:00+09:00",
    "thumbnail_image": "/media/erd.png",
    "create_date": "2020-11-03T20:59:53.770623+09:00",
    "update_date": "2020-11-03T20:59:53.770623+09:00",
    "priority": 1,
    "user": 2,
    "detail": [
        {
            "image": "/media/KakaoTalk_20201019_093205576.png",
            "content": "테스트1",
            "priority": 1
        },
        {
            "image": "/media/KakaoTalk_20200907_134019738.jpg",
            "content": "테스트2",
            "priority": 2
        }
    ]
}
```



## 이벤트 생성

```
주소/api/services/event/<int:pk>/(POST)
```

- Body(form-data)

```json
{
    "thumbnail": "썸네일 이미지",
    "title": "이벤트 이름",
    "strat_date": "2020-11-03 18:00:00",
    "end_date": "2020-11-05 18:00:00",
    "images": ["디테일에 들어갈 여러 이미지"],
    "contents": ["이미지와 같이들어갈 글"],
}
```

- Response

```json
{
    "id": 21,
    "title": "이벤트 이름",
    "start_date": "2020-11-03T18:00:00+09:00",
    "end_date": "2020-11-05T18:00:00+09:00",
    "thumbnail_image": "/media/erd_lnMaLcv.png",
    "create_date": "2020-11-03T21:38:16.990359+09:00",
    "update_date": "2020-11-03T21:38:16.990359+09:00",
    "priority": 1,
    "user": 2,
    "detail": [
        {
            "image": "/media/KakaoTalk_20201019_093205576_PxySHT2.png",
            "content": "테스트1",
            "priority": 1
        },
        {
            "image": "/media/KakaoTalk_20200907_134019738_BqgSpGX.jpg",
            "content": "테스트2",
            "priority": 2
        }
    ]
}
```



## 이벤트 수정(미완)

```

```

- Body

```json

```

- Response

```json

```





## 이벤트 삭제

```
주소/api/services/event/<int:pk>/(DELETE)
```

- Response

```json
{
    "message": "이벤트가 삭제되었습니다."
}
```





## 공지 리스트 읽기

```
주소/api/services/notices/(GET)
```

- Response

```json
[
    {
        "id": 4,
        "title": "테스트",
        "content": "테스트1",
        "create_date": "2020-11-03T22:39:28.063168+09:00",
        "update_date": "2020-11-03T22:39:28.063168+09:00",
        "is_active": true,
        "user": 2,
        "image": "/media/KakaoTalk_20200907_134019738_CnpdyfJ.jpg"
    }
]
```



## 공지사항 읽기

```
주소/api/services/event/<int:pk>/(GET)
```

- Response

```json
{
    "id": 4,
    "title": "테스트",
    "content": "테스트1",
    "create_date": "2020-11-03T22:39:28.063168+09:00",
    "update_date": "2020-11-03T22:39:28.063168+09:00",
    "is_active": true,
    "user": 2,
    "image": "/media/KakaoTalk_20200907_134019738_CnpdyfJ.jpg"
}
```





## 공지 생성

```
주소/api/services/notices/(post)
```

- Body(form-data)

```json
{
    "title": "제목",
    "content": "내용",
    "image": "이미지데이터"
}
```

- Response

```json
{
    "id": 4,
    "title": "테스트",
    "content": "테스트1",
    "create_date": "2020-11-03T22:39:28.063168+09:00",
    "update_date": "2020-11-03T22:39:28.063168+09:00",
    "is_active": true,
    "user": 2,
    "image": "/media/KakaoTalk_20200907_134019738_CnpdyfJ.jpg"
}
```



## 공지 수정(미완)

```

```

- Body

```json

```

- Response

```json

```



## 공지 삭제

```
주소/api/services/event/<int:pk>/(DELETE)
```

- Response

```json
{
    "message": "공지가 삭제되었습니다."
}
```



## 로그데이터 가져오기(미완)

```

```

- Body

```json

```

- Response

```json

```



## 유저 필터링

```
주소/api/accounts/search/?type=abc&content
```

> type 종류
>
> - all  - 전체유저 정보
> - is_access - 승인 여부에 따라 유저 정보 검색 content에 True, False 입력
> - name - content에 들어가있는 이름으로 검색
> - department - content에 들어가있는 부서명으로 검색
>
> ex) `주소/api/accounts/search/?type=department&content=생산관리`

- Response

```json
[
    {
        "id": 7,
        "username": "songsong",
        "first_name": "송은석",
        "is_superuser": false,
        "is_access": false,
        "is_logger": false,
        "is_eventer": false,
        "is_producter": false,
        "is_marketer": false,
        "department": {
            "id": 3,
            "name": "생산관리"
        },
        "last_login": "2020-11-04T11:22:32.481028+09:00",
        "employee_number": 123414141
    },
    {
        "id": 9,
        "username": "test6",
        "first_name": "은석",
        "is_superuser": false,
        "is_access": false,
        "is_logger": false,
        "is_eventer": false,
        "is_producter": false,
        "is_marketer": false,
        "department": {
            "id": 3,
            "name": "생산관리"
        },
        "last_login": "2020-11-04T11:31:24.566257+09:00",
        "employee_number": 749172
    }
]
```





## 템플릿 정보(미완성)

```

```

- Body

```json

```

- Response

```json

```





## 부서 정보

```
주소/api/accounts/department/
```

- Response

```json
[
    {
        "id": 1,
        "name": "인사과"
    },
    {
        "id": 2,
        "name": "기획과"
    },
    {
        "id": 3,
        "name": "생산관리"
    }
]
```
