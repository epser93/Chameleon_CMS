# REST API 명세서

| url                                           | GET                      | POST               | PUT           | DELETE            |
| --------------------------------------------- | ------------------------ | ------------------ | ------------- | ----------------- |
| accounts/                                     | 자신의 정보              |                    |               |                   |
| accounts/search/?type=<>&content=<>           | 유저 검색(필터링)        |                    |               |                   |
| accounts/validation/?type=<>&content=<>       | 아이디, 이메일 여부 확인 |                    |               |                   |
| accounts/department/                          | 부서 정보                |                    |               |                   |
| accounts/login/                               |                          | 로그인             |               |                   |
| accounts/signup/                              |                          | 회원가입           |               |                   |
| accounts/logout/                              |                          | 로그아웃           |               |                   |
| accounts/manage/<user_id>/                    |                          | 회원가입 승인      | 회원권한 수정 |                   |
| products/main/                                | 메인페이지 상세          |                    |               |                   |
| products/main/carousel/                       |                          | 대표페이지 등록    |               |                   |
| products/template/                            | 템플릿 정보              |                    |               |                   |
| products/category/                            | 카테고리 리스트          | 카테고리 생성      |               |                   |
| products/category/<category_id>/              | 카테고리 물품리스트      |                    | 카테고리 수정 | 카테고리 삭제     |
| products/product/                             |                          | 제품생성(임시까지) |               |                   |
| products/product/<product_id>/                | 제품 상세정보            | 제품 활성화        | 임시제품 적용 | 제품 비활성       |
| products/temp_product/<product_id>/           | 제품 히스토리 조회       | 제품 임시정보 생성 |               |                   |
| products/serarch/?type=<>&content=<>&order=<> | 검색                     |                    |               |                   |
| services/notices/                             | 공지사항 리스트          | 공지사항 생성      |               |                   |
| services/notices/<notices_id>/                | 공지사항 상세            | 공지사항 활성화    | 공지사항 수정 | 공지사항 비활성화 |
| services/event/                               | 이벤트 리스트            | 이벤트 생성        |               |                   |
| services/event/<event_id>/                    | 이벤트 상세              |                    | 이벤트 수정   | 이벤트 삭제       |
| services/logs/                                | 로그데이터               |                    |               |                   |



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





## 카테고리 생성

```
주소/api/products/categories/(POST)
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



## 카테고리 수정

```
주소/api/products/categories/<int:pk>/(PUT)
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



## 카테고리 삭제

```
주소/api/products/categories/<int:pk>/(DELETE)
```

- Response

```json
{
    "message": "비활성화 되었습니다."
}
```



## 카테고리 속한 아이템 보기(수정필요, 관리자, 사용자 분리)

```
주소/api/products/categories/<int:pk>/(get)
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
        "images": [],
        "category": {
            
        }
    }
]
```





## 아이템 생성

```
주소/api/products/product/(POST)
```

> number는 이미지 개수이다.
>
> 이미지를 보낼때는 image 뒤에 넘버를 붙여서 보낸다.

- Body

```json
{
    "name": "노트북A",
    "price": 1280000,
    "is_temp": "False",
    "category": 1,
    "template": 2,
    "is_thumbnails": [
        "True", "True", "False",
    ],
    "number": 3,
    "image0": "이미지1",
    "image1": "이미지2",
    "image2": "이미지3",
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
    "images": [
        {
            "id": 18,
            "item_image": "/media/KakaoTalk_20200907_134019738.jpg",
            "is_thumbnail": false,
            "priority": 1,
            "created_date": "2020-11-06T15:12:53.601044+09:00",
            "update_date": "2020-11-06T15:12:53.601044+09:00"
        }
    ]
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
    "images": [
        {
            "id": 18,
            "item_image": "/media/KakaoTalk_20200907_134019738.jpg",
            "is_thumbnail": false,
            "priority": 1,
            "created_date": "2020-11-06T15:12:53.601044+09:00",
            "update_date": "2020-11-06T15:12:53.601044+09:00"
        }
    ]
}
```





## 아이템 수정

```
주소/api/products/<int:pk>/(PUT)
```

> 바꾸고 싶은 임시저장 아이템 id를 입력한다.

- Body

```json
{
    "id": 2
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
    "images": [
        {
            "id": 18,
            "item_image": "/media/KakaoTalk_20200907_134019738.jpg",
            "is_thumbnail": false,
            "priority": 1,
            "created_date": "2020-11-06T15:12:53.601044+09:00",
            "update_date": "2020-11-06T15:12:53.601044+09:00"
        }
    ]
}
```



## 아이템 비활성화

```
주소/api/products/product/<int:pk>/(DELETE)
```

- Response

```json
{
    "message": "비활성화 되었습니다."
}
```



## 아이템 활성화

```
주소/api/products/product/<int:pk>/(POST)
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
    "images": [
        {
            "id": 18,
            "item_image": "/media/KakaoTalk_20200907_134019738.jpg",
            "is_thumbnail": false,
            "priority": 1,
            "created_date": "2020-11-06T15:12:53.601044+09:00",
            "update_date": "2020-11-06T15:12:53.601044+09:00"
        }
    ]
}
```



## 아이템 히스토리 기록보기

```
주소/api/products/temp_product/<int:pk>/(GET)
```

- Response

```json
[
    {
        "id": 3,
        "name": "오디세이(수정)",
        "price": 1920000,
        "is_temp": false,
        "is_active": true,
        "category": {
            "id": 1,
            "name": "노트북"
        },
        "template": 2,
        "created_date": "2020-11-06T15:12:53.508331+09:00",
        "update_date": "2020-11-06T15:12:53.550339+09:00",
        "cms_user": {
            "id": 2,
            "username": "test",
            "first_name": "김유기"
        },
        "copy_descriptions": [],
        "copy_images": [
            {
                "id": 6,
                "item_image": "/media/KakaoTalk_20200907_134019738.jpg",
                "is_thumbnail": false,
                "priority": 1,
                "created_date": "2020-11-06T15:12:53.641773+09:00",
                "update_date": "2020-11-06T15:12:53.641773+09:00"
            }
        ]
    },
    {
        "id": 6,
        "name": "오디세이",
        "price": 192000,
        "is_temp": false,
        "is_active": true,
        "category": {
            "id": 1,
            "name": "노트북"
        },
        "template": 2,
        "created_date": "2020-11-06T16:20:21.701843+09:00",
        "update_date": "2020-11-06T16:20:21.741099+09:00",
        "cms_user": {
            "id": 2,
            "username": "test",
            "first_name": "김유기"
        },
        "copy_descriptions": [],
        "copy_images": [
            {
                "id": 7,
                "item_image": "/media/erd.png",
                "is_thumbnail": false,
                "priority": 1,
                "created_date": "2020-11-06T16:20:21.778874+09:00",
                "update_date": "2020-11-06T16:20:21.778874+09:00"
            }
        ]
    },
    {
        "id": 7,
        "name": "오디세이_임시3",
        "price": 152000,
        "is_temp": false,
        "is_active": true,
        "category": {
            "id": 1,
            "name": "노트북"
        },
        "template": 2,
        "created_date": "2020-11-06T16:22:54.925281+09:00",
        "update_date": "2020-11-06T16:22:54.960288+09:00",
        "cms_user": {
            "id": 2,
            "username": "test",
            "first_name": "김유기"
        },
        "copy_descriptions": [],
        "copy_images": [
            {
                "id": 8,
                "item_image": "/media/erd_IjdJt6m.png",
                "is_thumbnail": false,
                "priority": 1,
                "created_date": "2020-11-06T16:22:54.997536+09:00",
                "update_date": "2020-11-06T16:22:54.997536+09:00"
            }
        ]
    }
]
```



## 아이템 임시 저장

```
주소/api/products/temp_product/<int:pk>/(POST)
```

>  is_original : 변경하는 아이템정보가 원본기반인지 임시저장 기반인지
>
>  원본기반이라면 images_type에 원본 이미지 id를 넣어야 한다.
>
>  임시저장 기반이라면 images_type에 임시저장 이미지 id를 넣어야 한다.
>
>  새로추가되는 이미지라면 -1로 입력한다.
>
>  images_type과 is_thubnails의 길이는 같아야 한다.
>
>  이미지의 개수만큼 number에 입력한다.
>
>  image 뒤에는 넘버가 붙는다.

- Body

```json
{
    "name": "오디세이",
    "price": 1280000,
    "is_temp": "False",
    "category": 1,
    "template": 2,
    "is_original": "True",
    "images_type": [
      -1, -1
    ],
    "is_thumbnails": [
      "True","False",
    ],
    "number": 3,
    "image0": "이미지1",
    "image1": "이미지2",
    "image2": "이미지3",
    "descriptions": [
        {
            "id": 1,
            "content": "AMD"
        }
    ]
}
```

- Response

```json
{
    "id": 7,
    "name": "오디세이",
    "price": 128000,
    "is_temp": false,
    "is_active": true,
    "category": {
        "id": 1,
        "name": "노트북"
    },
    "template": 2,
    "created_date": "2020-11-06T16:22:54.925281+09:00",
    "update_date": "2020-11-06T16:22:54.960288+09:00",
    "cms_user": {
        "id": 2,
        "username": "test",
        "first_name": "김유기"
    },
    "copy_descriptions": [
        {
            "content": "AMD",
            "category_description": {
                "id": 1,
                "name": "제조사"
            }
        }
    ],
    "copy_images": [
        {
            "id": 8,
            "item_image": "/media/erd_IjdJt6m.png",
            "is_thumbnail": false,
            "priority": 1,
            "created_date": "2020-11-06T16:22:54.997536+09:00",
            "update_date": "2020-11-06T16:22:54.997536+09:00"
        }
    ]
}
```



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
        ],
        "url": null
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
    ],
    "url": null
}
```



## 이벤트 생성

```
주소/api/services/event/<int:pk>/(POST)
```

> number는 이미지 개수이다.
>
> 이미지를 보낼때는 image 뒤에 넘버를 붙여서 보낸다.

- Body(form-data)

```json
{
    "thumbnail": "썸네일 이미지",
    "title": "이벤트",
    "content": "이벤트 내용",
    "strat_date": "2020-11-03 18:00:00",
    "end_date": "2020-11-05 18:00:00",
    "number": 2,
    "image0": "이미지",
    "image1": "이미지"
    "url": "",
}
```

- Response

```json
{
    "id": 2,
    "title": "이벤트",
    "content": "이벤트 내용",
    "start_date": "2020-11-09T11:00:00+09:00",
    "is_active": true,
    "end_date": "2020-11-10T12:00:00+09:00",
    "thumbnail_image": "/media/erd_RL2NJeG.png",
    "create_date": "2020-11-07T20:55:43.037011+09:00",
    "update_date": "2020-11-07T20:55:43.037011+09:00",
    "priority": 1,
    "user": 2,
    "detail": [
        {
            "id": 1,
            "image": "/media/erd_uMjhx20.png",
            "priority": 1
        }
    ],
    "url": null
}
```



## 이벤트 수정(미완)

```
주소/api/services/event/<int:pk>/(PUT)
```

- Body

```json

```

- Response

```json

```



## 이벤트 활성화

```
주소/api/services/event/<int:pk>/(POST)
```

- Response

```json
{
    "id": 2,
    "title": "이벤트",
    "content": "이벤트 내용",
    "start_date": "2020-11-09T11:00:00+09:00",
    "is_active": true,
    "end_date": "2020-11-10T12:00:00+09:00",
    "thumbnail_image": "/media/erd_RL2NJeG.png",
    "create_date": "2020-11-07T20:55:43.037011+09:00",
    "update_date": "2020-11-07T20:55:43.037011+09:00",
    "priority": 1,
    "user": 2,
    "detail": [
        {
            "id": 1,
            "image": "/media/erd_uMjhx20.png",
            "priority": 1
        }
    ],
    "url": null
}
```





## 이벤트 비활성화

```
주소/api/services/event/<int:pk>/(DELETE)
```

- Response

```json
{
    "message": "이벤트가 비활성화 되었습니다."
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
    "title": "공지",
    "content": "공지내용",
    "image": "이미지데이터",
}
```

- Response

```json
{
    "id": 3,
    "title": "공지",
    "content": "공지 내용",
    "start_date": "2020-11-09T11:00:00+09:00",
    "end_date": "2020-11-10T12:00:00+09:00",
    "create_date": "2020-11-07T21:00:31.419455+09:00",
    "update_date": "2020-11-07T21:00:31.419455+09:00",
    "is_active": true,
    "is_temp": true,
    "user": 2,
    "image": "/media/erd_q0JEL7H.png"
}
```



## 공지 수정

```
주소/api/services/notices/<int:pk>/
```

- Body

```json
{
    "title": "공지 수정",
    "content": "공지 수정 내용",
    "image": "바꿀 이미지 없으면 안넣어도 무방함"
}
```

- Response

```json
{
    "id": 3,
    "title": "공지 수정",
    "content": "공지 내용수정",
    "start_date": "2020-11-07T21:13:12.600386+09:00",
    "end_date": null,
    "create_date": "2020-11-07T21:00:31.419455+09:00",
    "update_date": "2020-11-07T21:20:30.407538+09:00",
    "is_active": true,
    "is_temp": false,
    "user": 2,
    "image": "/media/erd_q0JEL7H.png"
}
```

## 공지 활성화

```
주소/api/services/notices/<int:pk>/(POST)
```

> 활성화시 start_date가 자동으로 입력된다.
>
> 공지를 종료하지 않았기때문에 end가 null로 설정된다.
>
> 활성화시 is_temp가 True로 변경됨
>
> 활성화시 is_active가 True로 변경됨

- Response

```json
{
    "id": 3,
    "title": "공지 수정",
    "content": "공지 내용수정",
    "start_date": "2020-11-07T21:27:28.459164+09:00",
    "end_date": null,
    "create_date": "2020-11-07T21:00:31.419455+09:00",
    "update_date": "2020-11-07T21:27:28.468088+09:00",
    "is_active": true,
    "is_temp": false,
    "user": 2,
    "image": "/media/erd_q0JEL7H.png",
}
```



## 공지 비활성화

```
주소/api/services/notices/<int:pk>/(DELETE)
```

> 비활성화시 end_date가 입력된다.
>
> is_active가 False로 입력된다.
>
> is_temp가 True일경우 공지가 삭제된다.

- Response

```json
{
    "message": "공지가 비활성화 되었습니다."
}
```



## 로그데이터

```
주소/api/accounts/logs/(GEt)
```

- Response

```json
[
    {
        "type": "회원가입",
        "register_ip": "0.0.0.0",
        "create_date": "2020-11-06T15:02:08.835470+09:00",
        "cms_user": 2
    },
    {
        "type": "로그인",
        "register_ip": "0.0.0.0",
        "create_date": "2020-11-06T15:02:39.444308+09:00",
        "cms_user": 2
    },
    {
        "type": "회원가입",
        "register_ip": "0.0.0.0",
        "create_date": "2020-11-06T15:04:58.221495+09:00",
        "cms_user": 3
    },
    {
        "type": "로그인",
        "register_ip": "0.0.0.0",
        "create_date": "2020-11-06T15:05:39.168803+09:00",
        "cms_user": 3
    },
    {
        "type": "로그아웃",
        "register_ip": "0.0.0.0",
        "create_date": "2020-11-06T15:12:48.820754+09:00",
        "cms_user": 3
    }
]
```

- 실패 Response(403)

```json
{
    "message": "권한이 없습니다."
}
```



## 유저 필터링

```
주소/api/accounts/search/?type=<>&content=<>
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





## 템플릿 정보

```
주소/api/products/template/(get)
```

- Response

```json
[
    {
        "id": 1,
        "name": "카테고리 이미지 특화",
        "type": 1
    },
    {
        "id": 2,
        "name": "아이템 이미지 특화",
        "type": 2
    }
]
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



## 이메일,아이디 여부

```
주소/api/accounts/validation/?type=<>&content=<>
```

- 성공 Response

```json
{
    "message": "사용이 가능합니다."
}
```

- 실패 Response(400)

```json
{
    message: "너무 짧은 아이디 입니다.",
    message: "존재하는 아이디 입니다.",
    message: "존재하는 이메일 입니다."
}
```



## 메인화면 아이템 설정







## 메인화면 캐로셀 아이템 설정





