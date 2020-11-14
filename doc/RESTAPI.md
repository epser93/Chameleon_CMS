# REST API 명세서

## Admin url

| url                                     | GET                      | POST               | PUT             | DELETE              |
| --------------------------------------- | ------------------------ | ------------------ | --------------- | ------------------- |
| accounts/                               | 자신의 정보              |                    |                 |                     |
| accounts/login/                         |                          | 로그인             |                 |                     |
| accounts/logout/                        |                          | 로그아웃           |                 |                     |
| accounts/signup/                        |                          | 회원가입           |                 |                     |
| accounts/manage/<user_id>/              |                          | 회원가입 승인      | 회원권한 수정   |                     |
| accounts/department/                    | 부서 정보                |                    |                 |                     |
| accounts/search/?type=<>&content=<>     | 유저 검색(필터링)        |                    |                 |                     |
| accounts/validation/?type=<>&content=<> | 아이디, 이메일 여부 확인 |                    |                 |                     |
| accounts/logs/                          | 로그데이터               |                    |                 |                     |
| products/category/                      | 카테고리 리스트          | 카테고리 생성      |                 |                     |
| products/category/<category_id>/        | 카테고리 물품리스트      | 카테고리 활성화    | 카테고리 수정   | 카테고리 비활성화   |
| products/product/                       |                          | 제품생성(임시까지) |                 |                     |
| products/product/<product_id>/          | 제품 상세정보            | 제품 활성화        | 임시제품 적용   | 제품 비활성화       |
| products/temp_product/<product_id>/     | 제품 히스토리 조회       | 제품 임시정보 생성 |                 |                     |
| products/template/                      | 템플릿 정보              |                    |                 |                     |
| products/search/?content=<>             | 물건 검색                |                    |                 |                     |
| services/event/                         | 이벤트 리스트            | 이벤트 생성        |                 |                     |
| services/event/<event_id>/              | 이벤트 상세              | 이벤트 활성화      | 이벤트 수정     | 이벤트 비활성화     |
| services/notices/                       | 공지사항 리스트          | 공지사항 생성      |                 |                     |
| services/notices/<notices_id>/          | 공지사항 상세            | 공지사항 활성화    | 공지사항 수정   | 공지사항 비활성화   |
| servicies/main/                         | 메인아이템 모든 정보     | 메인 아이템 생성   |                 |                     |
| servicies/main/<main_id>                | 메인아이템 상세정보      | 메인아이템 활성화  | 메인아이템 수정 | 메인아이템 비활성화 |
| servicies/carousel/                     | 케로셀 모든정보          | 케로셀 생성        |                 |                     |
| servicies/carousel/<carousel_id>        | 캐로셀 상세정보          | 케로셀 활성화      | 케로셀 수정     | 케로셀 비활성화     |

## Customer url

| url                                              | get                   |
| ------------------------------------------------ | --------------------- |
| services/customer/search/?content=<>             | 아이템 및 이벤트 검색 |
| products/customer/categories/                    | 카테고리 리스트       |
| /api/products/customer/categories/<category_id>/ | 카테고리 속한 아이템  |
| products/customer/product/<product_id>/          | 아이템 상세정보       |
| services/customer/event/                         | 메인 아이템 조회      |
| services/customer/carousel/                      | 케로셀 아이템 조회    |
| services/customer/event/                         | 이벤트 리스트 조회    |
| services/customer/event/<event_id>/              | 이벤트 디테일 조회    |
| services/customer/notices/                       | 공지리스트 조회       |



## Admin API

### 자기 정보 얻기

```
주소/api/accounts/ (GET)
```

- Response

```json
{
    "id": 2,
    "username": "test",
    "first_name": "김유기",
    "is_superuser": true,
    "is_access": true,
    "is_logger": false,
    "is_eventer": false,
    "is_producter": false,
    "is_marketer": false,
    "department": {
        "id": 1,
        "name": "인사과"
    },
    "last_login": "2020-11-13T09:51:31.532713+09:00",
    "employee_number": 0
}
```







### 로그인

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



### 로그아웃

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



### 회원가입

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



### 회원가입 승인

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



### 회원 권한 변경

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





### 부서 정보

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



### 유저 필터링

```
주소/api/accounts/search/?type=<>&content=<>
```

> type 종류
>
> - all  - 승인된 유저중에서 부서상관없이 이름으로 검색
> - is_access - 승인되지 않은 유저들만 검색
>
> - 부서명 - 해당 부서명으로 검색, content가 필수이다.
>
> name - content에 들어가있는 이름으로 검색
>
> ex) `주소/api/accounts/search/?type=생산관리&content=은석`

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



### 이메일,아이디 여부

```
주소/api/accounts/validation/?type=<>&content=<>
```

> type
>
> - id - content에 사용할 id를 입력한다.
> - email - content에 사용할 email을 입력한다.

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



### 로그데이터

```
주소/api/accounts/logs/(GET)
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





### 카테고리 리스트

```
주소/api/products/categories/
```

- Response

```json
[
    {
        "id": 1,
        "name": "노트북",
        "is_active": true,
        "image": null,
        "priority": 1,
        "template": {
            "id": 1,
            "name": "카테고리 아이템 특화",
            "type": 1
        },
        "created_date": "2020-11-09T10:18:57.056219+09:00",
        "update_date": "2020-11-09T13:10:28.686958+09:00",
        "cms_user": {
            "id": 1,
            "username": "admin",
            "first_name": ""
        },
        "description": [
            {
                "id": 14,
                "name": "제조사"
            }
        ]
    },
    {
        "id": 2,
        "name": "마우스",
        "is_active": true,
        "image": null,
        "priority": 1,
        "template": {
            "id": 1,
            "name": "카테고리 아이템 특화",
            "type": 1
        },
        "created_date": "2020-11-09T12:52:14.675112+09:00",
        "update_date": "2020-11-09T13:53:14.170752+09:00",
        "cms_user": {
            "id": 3,
            "username": "test930",
            "first_name": "임선빈"
        },
        "description": [
            {
                "id": 1,
                "name": "크기,무게,블루투스"
            }
        ]
    },
    {
        "id": 3,
        "name": "스마트폰",
        "is_active": true,
        "image": "/media/202005071135281269924.jpg",
        "priority": 1,
        "template": {
            "id": 2,
            "name": "카테고리 이미지 특화",
            "type": 1
        },
        "created_date": "2020-11-09T12:57:33.931910+09:00",
        "update_date": "2020-11-09T14:36:28.438922+09:00",
        "cms_user": {
            "id": 3,
            "username": "test930",
            "first_name": "임선빈"
        },
        "description": [
            {
                "id": 15,
                "name": "화소"
            },
            {
                "id": 16,
                "name": "화소"
            },
            {
                "id": 17,
                "name": "화소"
            }
        ]
    },
    {
        "id": 4,
        "name": "키보드",
        "is_active": true,
        "image": "/media/NISI20191010_0015689491.jpg",
        "priority": 1,
        "template": {
            "id": 2,
            "name": "카테고리 이미지 특화",
            "type": 1
        },
        "created_date": "2020-11-09T14:36:57.686405+09:00",
        "update_date": "2020-11-09T16:46:46.044283+09:00",
        "cms_user": {
            "id": 3,
            "username": "test930",
            "first_name": "임선빈"
        },
        "description": [
            {
                "id": 18,
                "name": "크기"
            },
            {
                "id": 20,
                "name": "크기"
            }
        ]
    },
    {
        "id": 5,
        "name": "한꺼번에수정",
        "is_active": true,
        "image": "/media/%EB%A7%88%EC%9A%B0%EC%8A%A4.jpg",
        "priority": 1,
        "template": {
            "id": 2,
            "name": "카테고리 이미지 특화",
            "type": 1
        },
        "created_date": "2020-11-09T14:41:05.917856+09:00",
        "update_date": "2020-11-09T16:46:56.865772+09:00",
        "cms_user": {
            "id": 3,
            "username": "test930",
            "first_name": "임선빈"
        },
        "description": [
            {
                "id": 24,
                "name": "굿굿"
            },
            {
                "id": 25,
                "name": "라면"
            },
            {
                "id": 26,
                "name": "왜"
            }
        ]
    }
]
```





### 카테고리 생성

```
주소/api/products/categories/(POST)
```

- Body

```json
{
    "name": "노트북",
    "descriptions": [
        "제조사"
    ],
    "image": "이미지 파일",
    "template": 1,
    "priority": 1
}
```

- Response

```json
{
    "id": 1,
    "name": "노트북",
    "is_active": true,
    "image": null,
    "priority": 1,
    "template": {
        "id": 1,
        "name": "카테고리 아이템 특화",
        "type": 1
    },
    "created_date": "2020-11-09T10:18:57.056219+09:00",
    "update_date": "2020-11-09T13:10:28.686958+09:00",
    "cms_user": {
        "id": 1,
        "username": "admin",
        "first_name": ""
    },
    "description": [
        {
            "id": 14,
            "name": "제조사"
        }
    ]
},
```



### 카테고리 수정

```
주소/api/products/categories/<int:pk>/(PUT)
```

- Body

```json
{
    "name": "김치냉장고 v2",
    "descriptions_update_id": [
        25
    ],
    "descriptions_update_name": [
        "전력소모량"
    ],
    "descriptions_delete": [
        23, 24
    ],
    "descriptions_add": [
        "테스트1234"
    ],
    "image": "이미지 파일",
    "template": 1,
    "priority": 1
}
```

- Response

```json
{
    "id": 1,
    "name": "노트북",
    "is_active": true,
    "image": null,
    "priority": 1,
    "template": {
        "id": 1,
        "name": "카테고리 아이템 특화",
        "type": 1
    },
    "created_date": "2020-11-09T10:18:57.056219+09:00",
    "update_date": "2020-11-09T13:10:28.686958+09:00",
    "cms_user": {
        "id": 1,
        "username": "admin",
        "first_name": ""
    },
    "description": [
        {
            "id": 14,
            "name": "제조사"
        }
    ]
},
```



### 카테고리 활성화

```
주소/api/products/categories/<int:pk>/(POST)
```

- Response

```json
{
    "id": 1,
    "name": "노트북",
    "is_active": true,
    "image": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/KakaoTalk_20200921_091027148_BpDjCOu.png",
    "priority": 1,
    "template": {
        "id": 1,
        "name": "카테고리 이미지 특화",
        "type": 1
    },
    "created_date": "2020-11-13T11:44:09.394979+09:00",
    "update_date": "2020-11-13T11:53:47.055341+09:00",
    "cms_user": {
        "id": 2,
        "username": "test",
        "first_name": "김유기"
    },
    "description": [
        {
            "id": 1,
            "name": "제조사"
        },
        {
            "id": 2,
            "name": "디스플레이"
        }
    ]
}
```



### 카테고리 비활성화

```
주소/api/products/categories/<int:pk>/(DELETE)
```

- Response

```json
{
    "message": "비활성화 되었습니다."
}
```



### 카테고리 속한 아이템 보기(수정필요, 관리자, 사용자 분리)

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
        "category": {
            "id": 1,
            "name": "노트북"
        },
        "template": {
            "id": 2,
            "name": "카테고리 이미지 특화",
            "type": 1
        },
        "created_date": "2020-11-09T10:39:27.052224+09:00",
        "update_date": "2020-11-09T16:32:06.213925+09:00",
        "cms_user": {
            "id": 2,
            "username": "test",
            "first_name": "김유기"
        },
        "descriptions": [
            {
                "content": "AMD",
                "item": 1,
                "category_description": {
                    "id": 14,
                    "name": "제조사"
                }
            }
        ],
        "images": []
    },
    {
        "id": 2,
        "name": "노트북A",
        "price": 1280000,
        "is_temp": false,
        "is_active": true,
        "category": {
            "id": 1,
            "name": "노트북"
        },
        "template": {
            "id": 2,
            "name": "카테고리 이미지 특화",
            "type": 1
        },
        "created_date": "2020-11-09T10:39:44.786263+09:00",
        "update_date": "2020-11-09T16:32:01.078872+09:00",
        "cms_user": {
            "id": 2,
            "username": "test",
            "first_name": "김유기"
        },
        "descriptions": [],
        "images": [
            {
                "id": 1,
                "item_image": "/media/KakaoTalk_20201019_093205576_ni0qpZF.png",
                "is_thumbnail": true,
                "priority": 1,
                "created_date": "2020-11-09T10:39:44.898264+09:00",
                "update_date": "2020-11-09T10:39:44.898264+09:00"
            }
        ]
    }
]
```





### 아이템 생성

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
    "descriptions_id": [
        20
    ],
    "descriptions_content": [
        "AMD"
    ]
}
```

- Response

```json
{
    "id": 2,
    "name": "노트북A",
    "price": 1280000,
    "is_temp": false,
    "is_active": true,
    "category": {
        "id": 1,
        "name": "노트북"
    },
    "template": {
        "id": 2,
        "name": "카테고리 이미지 특화",
        "type": 1
    },
    "created_date": "2020-11-09T10:39:44.786263+09:00",
    "update_date": "2020-11-09T16:32:01.078872+09:00",
    "cms_user": {
        "id": 2,
        "username": "test",
        "first_name": "김유기"
    },
    "descriptions": [
        {
            "content": "AMD",
            "item": 1,
            "category_description": {
                "id": 14,
                "name": "제조사"
            }
        }
    ],
    "images": [
        {
            "id": 1,
            "item_image": "/media/KakaoTalk_20201019_093205576_ni0qpZF.png",
            "is_thumbnail": true,
            "priority": 1,
            "created_date": "2020-11-09T10:39:44.898264+09:00",
            "update_date": "2020-11-09T10:39:44.898264+09:00"
        }
    ]
}
```



### 아이템 상세 정보

```
주소/api/products/<int:pk>/(GET)
```

- Response

```json
{
    "id": 2,
    "name": "LG그램3",
    "price": 3,
    "is_temp": false,
    "is_active": true,
    "category": {
        "id": 1,
        "name": "노트북"
    },
    "template": {
        "id": 3,
        "name": "아이템 이미지 특화",
        "type": 2
    },
    "created_date": "2020-11-13T13:22:31.025746+09:00",
    "update_date": "2020-11-13T14:00:46.523156+09:00",
    "cms_user": {
        "id": 6,
        "username": "zjohn99",
        "first_name": "장좐"
    },
    "descriptions": [
        {
            "content": "LGff",
            "item": 2,
            "category_description": {
                "id": 1,
                "name": "제조사"
            }
        },
        {
            "content": "헬지",
            "item": 2,
            "category_description": {
                "id": 2,
                "name": "디스플레이"
            }
        }
    ],
    "images": [
        {
            "id": 41,
            "item_image": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/202005071135281269924_SrlMFuk.jpg",
            "is_thumbnail": true,
            "priority": 1,
            "created_date": "2020-11-13T14:00:46.576187+09:00",
            "update_date": "2020-11-13T14:00:46.576187+09:00"
        },
        {
            "id": 42,
            "item_image": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/image_6963812281481439508693_mvocTBT.jpg",
            "is_thumbnail": true,
            "priority": 1,
            "created_date": "2020-11-13T14:00:46.616156+09:00",
            "update_date": "2020-11-13T14:00:46.616156+09:00"
        },
        {
            "id": 43,
            "item_image": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/%EB%84%88%EA%B5%AC%EB%A6%AC.png",
            "is_thumbnail": false,
            "priority": 1,
            "created_date": "2020-11-13T14:00:46.659300+09:00",
            "update_date": "2020-11-13T14:00:46.660335+09:00"
        },
        {
            "id": 44,
            "item_image": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/%EC%84%B8%EC%85%98%ED%95%98%EC%9D%B4%EC%9E%AC%ED%82%B9.PNG",
            "is_thumbnail": false,
            "priority": 1,
            "created_date": "2020-11-13T14:00:46.704447+09:00",
            "update_date": "2020-11-13T14:00:46.704447+09:00"
        }
    ]
}
```





### 아이템 수정

```
주소/api/products/<int:pk>/(PUT)
```

> 바꾸고 싶은 임시저장 아이템 id를 Body에 입력한다.
>
> url 주소에는 바꿀 원본 아이템 id를 넣는다.

- Body

```json
{
    "id": 2
}
```

- Response

```json
{
    "id": 2,
    "name": "LG그램3",
    "price": 3,
    "is_temp": false,
    "is_active": true,
    "category": {
        "id": 1,
        "name": "노트북"
    },
    "template": {
        "id": 3,
        "name": "아이템 이미지 특화",
        "type": 2
    },
    "created_date": "2020-11-13T13:22:31.025746+09:00",
    "update_date": "2020-11-13T14:00:46.523156+09:00",
    "cms_user": {
        "id": 6,
        "username": "zjohn99",
        "first_name": "장좐"
    },
    "descriptions": [
        {
            "content": "LGff",
            "item": 2,
            "category_description": {
                "id": 1,
                "name": "제조사"
            }
        },
        {
            "content": "헬지",
            "item": 2,
            "category_description": {
                "id": 2,
                "name": "디스플레이"
            }
        }
    ],
    "images": [
        {
            "id": 41,
            "item_image": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/202005071135281269924_SrlMFuk.jpg",
            "is_thumbnail": true,
            "priority": 1,
            "created_date": "2020-11-13T14:00:46.576187+09:00",
            "update_date": "2020-11-13T14:00:46.576187+09:00"
        },
        {
            "id": 42,
            "item_image": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/image_6963812281481439508693_mvocTBT.jpg",
            "is_thumbnail": true,
            "priority": 1,
            "created_date": "2020-11-13T14:00:46.616156+09:00",
            "update_date": "2020-11-13T14:00:46.616156+09:00"
        },
        {
            "id": 43,
            "item_image": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/%EB%84%88%EA%B5%AC%EB%A6%AC.png",
            "is_thumbnail": false,
            "priority": 1,
            "created_date": "2020-11-13T14:00:46.659300+09:00",
            "update_date": "2020-11-13T14:00:46.660335+09:00"
        },
        {
            "id": 44,
            "item_image": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/%EC%84%B8%EC%85%98%ED%95%98%EC%9D%B4%EC%9E%AC%ED%82%B9.PNG",
            "is_thumbnail": false,
            "priority": 1,
            "created_date": "2020-11-13T14:00:46.704447+09:00",
            "update_date": "2020-11-13T14:00:46.704447+09:00"
        }
    ]
}
```



### 아이템 비활성화

```
주소/api/products/product/<int:pk>/(DELETE)
```

- Response

```json
{
    "message": "비활성화 되었습니다."
}
```



### 아이템 활성화

```
주소/api/products/product/<int:pk>/(POST)
```

- Response

```json
{
    "id": 2,
    "name": "LG그램3",
    "price": 3,
    "is_temp": false,
    "is_active": true,
    "category": {
        "id": 1,
        "name": "노트북"
    },
    "template": {
        "id": 3,
        "name": "아이템 이미지 특화",
        "type": 2
    },
    "created_date": "2020-11-13T13:22:31.025746+09:00",
    "update_date": "2020-11-13T14:00:46.523156+09:00",
    "cms_user": {
        "id": 6,
        "username": "zjohn99",
        "first_name": "장좐"
    },
    "descriptions": [
        {
            "content": "LGff",
            "item": 2,
            "category_description": {
                "id": 1,
                "name": "제조사"
            }
        },
        {
            "content": "헬지",
            "item": 2,
            "category_description": {
                "id": 2,
                "name": "디스플레이"
            }
        }
    ],
    "images": [
        {
            "id": 41,
            "item_image": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/202005071135281269924_SrlMFuk.jpg",
            "is_thumbnail": true,
            "priority": 1,
            "created_date": "2020-11-13T14:00:46.576187+09:00",
            "update_date": "2020-11-13T14:00:46.576187+09:00"
        },
        {
            "id": 42,
            "item_image": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/image_6963812281481439508693_mvocTBT.jpg",
            "is_thumbnail": true,
            "priority": 1,
            "created_date": "2020-11-13T14:00:46.616156+09:00",
            "update_date": "2020-11-13T14:00:46.616156+09:00"
        },
        {
            "id": 43,
            "item_image": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/%EB%84%88%EA%B5%AC%EB%A6%AC.png",
            "is_thumbnail": false,
            "priority": 1,
            "created_date": "2020-11-13T14:00:46.659300+09:00",
            "update_date": "2020-11-13T14:00:46.660335+09:00"
        },
        {
            "id": 44,
            "item_image": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/%EC%84%B8%EC%85%98%ED%95%98%EC%9D%B4%EC%9E%AC%ED%82%B9.PNG",
            "is_thumbnail": false,
            "priority": 1,
            "created_date": "2020-11-13T14:00:46.704447+09:00",
            "update_date": "2020-11-13T14:00:46.704447+09:00"
        }
    ]
}
```



### 아이템 히스토리 기록보기

```
주소/api/products/temp_product/<int:pk>/(GET)
```

- Response

```json
[
    {
        "id": 2,
        "name": "노트북A",
        "price": 1280000,
        "is_temp": false,
        "is_active": true,
        "category": {
            "id": 1,
            "name": "노트북"
        },
        "template": 2,
        "created_date": "2020-11-09T10:39:44.821264+09:00",
        "update_date": "2020-11-09T10:39:44.855303+09:00",
        "cms_user": {
            "id": 2,
            "username": "test",
            "first_name": "김유기"
        },
        "copy_descriptions": [],
        "copy_images": [
            {
                "id": 1,
                "item_image": "/media/KakaoTalk_20201019_093205576_ni0qpZF.png",
                "is_thumbnail": true,
                "priority": 1,
                "created_date": "2020-11-09T10:39:44.932300+09:00",
                "update_date": "2020-11-09T10:39:44.932300+09:00"
            }
        ]
    }
]
```



### 아이템 임시 저장

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
>  is_thubnails의 길이는 추가된 이미지 개수만큼이다.
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
    "number": 2,
    "image0": "이미지1",
    "image1": "이미지2",
    "descriptions_id": [
        20
    ],
    "descriptions_content": [
        "AMD"
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



### 템플릿 정보

```
주소/api/products/template/(GET)
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
        "name": "카테고리 아이템 특화",
        "type": 1
    },
    {
        "id": 3,
        "name": "아이템 이미지 특화",
        "type": 2
    },
    {
        "id": 4,
        "name": "아이템 설명 특화",
        "type": 2
    }
]
```



### 물건 검색

```
주소/api/products/search/?type=<>&content=<>
```

> type
>
> - all : 카테고리에 상관없이 content가 들어간 아이템을 검색
> - 카테고리이름 : 해당 카테고리에 속해있는 content가 들어간 아이템을 검색
>
> content에 검색할 물건 이름을 넣는다.

- Response

```json
[
    {
        "id": 2,
        "name": "LG그램3",
        "price": 3,
        "is_temp": false,
        "is_active": true,
        "category": {
            "id": 1,
            "name": "노트북"
        },
        "template": {
            "id": 3,
            "name": "아이템 이미지 특화",
            "type": 2
        },
        "created_date": "2020-11-13T13:22:31.025746+09:00",
        "update_date": "2020-11-13T14:00:46.523156+09:00",
        "cms_user": {
            "id": 6,
            "username": "zjohn99",
            "first_name": "장좐"
        },
        "descriptions": [
            {
                "content": "LG",
                "item": 2,
                "category_description": {
                    "id": 1,
                    "name": "제조사"
                }
            },
            {
                "content": "헬지",
                "item": 2,
                "category_description": {
                    "id": 2,
                    "name": "디스플레이"
                }
            }
        ],
        "images": [
            {
                "id": 49,
                "item_image": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/202005071135281269924_SrlMFuk.jpg",
                "is_thumbnail": true,
                "priority": 1,
                "created_date": "2020-11-13T14:07:16.270239+09:00",
                "update_date": "2020-11-13T14:07:16.270284+09:00"
            },
            {
                "id": 50,
                "item_image": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/image_6963812281481439508693_mvocTBT.jpg",
                "is_thumbnail": true,
                "priority": 1,
                "created_date": "2020-11-13T14:07:16.276447+09:00",
                "update_date": "2020-11-13T14:07:16.276489+09:00"
            },
            {
                "id": 51,
                "item_image": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/%EB%84%88%EA%B5%AC%EB%A6%AC.png",
                "is_thumbnail": false,
                "priority": 1,
                "created_date": "2020-11-13T14:07:16.282466+09:00",
                "update_date": "2020-11-13T14:07:16.282504+09:00"
            },
            {
                "id": 52,
                "item_image": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/%EC%84%B8%EC%85%98%ED%95%98%EC%9D%B4%EC%9E%AC%ED%82%B9.PNG",
                "is_thumbnail": false,
                "priority": 1,
                "created_date": "2020-11-13T14:07:16.288197+09:00",
                "update_date": "2020-11-13T14:07:16.288233+09:00"
            }
        ]
    }
]
```



### 이벤트 리스트 읽기

```
주소/api/services/event/(GET)
```

- Response

```json
[
    {
        "id": 1,
        "title": "테스트",
        "content": "테스트",
        "start_date": "2020-11-04T00:00:00+09:00",
        "is_active": true,
        "end_date": "2020-11-04T23:59:59+09:00",
        "thumbnail_image": "/media/KakaoTalk_20200807_125333367_IjSlCrP.png",
        "create_date": "2020-11-09T12:31:22.526031+09:00",
        "update_date": "2020-11-09T13:46:16.542326+09:00",
        "priority": 1,
        "user": 3,
        "images": [
            {
                "id": 1,
                "image": "/media/KakaoTalk_20200807_125333367_urZx5Yl.png",
                "priority": 1
            }
        ],
        "url": "test"
    }
]
```





### 이벤트 읽기

```
주소/api/services/event/<int:pk>/(GET)
```

- Response

```json
[
    {
        "id": 1,
        "title": "초특가 이벤트",
        "content": "전 제품 65% 할인",
        "start_date": "2020-11-14T00:00:00+09:00",
        "is_active": true,
        "end_date": "2020-11-15T23:59:59+09:00",
        "thumbnail_image": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/458-600x250.jpg",
        "create_date": "2020-11-13T12:56:22.074587+09:00",
        "update_date": "2020-11-13T13:12:31.636391+09:00",
        "priority": 1,
        "user": 5,
        "images": [
            {
                "id": 1,
                "image": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/vertical1.jpg",
                "priority": 1
            },
            {
                "id": 2,
                "image": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/vertical2.jpg",
                "priority": 2
            },
            {
                "id": 3,
                "image": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/vertical3.jpg",
                "priority": 3
            }
        ],
        "url": "test"
    }
]
```



### 이벤트 생성

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
    "image1": "이미지",
    "url": "",
}
```

- Response

```json
{
    "id": 1,
    "title": "테스트",
    "content": "테스트",
    "start_date": "2020-11-04T00:00:00+09:00",
    "is_active": true,
    "end_date": "2020-11-04T23:59:59+09:00",
    "thumbnail_image": "/media/KakaoTalk_20200807_125333367_IjSlCrP.png",
    "create_date": "2020-11-09T12:31:22.526031+09:00",
    "update_date": "2020-11-09T13:46:16.542326+09:00",
    "priority": 1,
    "user": 3,
    "images": [
        {
            "id": 1,
            "image": "/media/KakaoTalk_20200807_125333367_urZx5Yl.png",
            "priority": 1
        }
    ],
    "url": "test"
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



### 이벤트 활성화

```
주소/api/services/event/<int:pk>/(POST)
```

- Response

```json
{
    "id": 1,
    "title": "테스트",
    "content": "테스트",
    "start_date": "2020-11-04T00:00:00+09:00",
    "is_active": true,
    "end_date": "2020-11-04T23:59:59+09:00",
    "thumbnail_image": "/media/KakaoTalk_20200807_125333367_IjSlCrP.png",
    "create_date": "2020-11-09T12:31:22.526031+09:00",
    "update_date": "2020-11-09T13:46:16.542326+09:00",
    "priority": 1,
    "user": 3,
    "images": [
        {
            "id": 1,
            "image": "/media/KakaoTalk_20200807_125333367_urZx5Yl.png",
            "priority": 1
        }
    ],
    "url": "test"
}
```





### 이벤트 비활성화

```
주소/api/services/event/<int:pk>/(DELETE)
```

- Response

```json
{
    "message": "이벤트가 비활성화 되었습니다."
}
```





### 공지 리스트 읽기

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



### 공지사항 읽기

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





### 공지 생성

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



### 공지 수정

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

### 공지 활성화

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



### 공지 비활성화

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













### 메인화면 아이템 모든 정보

```
주소/api/services/main/(GET)
```

- Response

```json
[
    {
        "id": 14,
        "priority": 1,
        "is_active": true,
        "create_date": "2020-11-14T18:54:13.253926+09:00",
        "update_date": "2020-11-14T18:54:13.253926+09:00",
        "item": {
            "id": 17,
            "name": "테스트",
            "thumbnail": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/2020-11-14_174143_KakaoTalk_20200921_091027148.png"
        },
        "user": {
            "id": 2,
            "username": "test",
            "first_name": "김유기"
        }
    },
    {
        "id": 11,
        "priority": 1,
        "is_active": false,
        "create_date": "2020-11-13T17:22:06.955081+09:00",
        "update_date": "2020-11-14T18:51:02.756084+09:00",
        "item": {
            "id": 12,
            "name": "갤럭시 S20",
            "thumbnail": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/sec-galaxy-s20-fe-5g-g781-sm-g781nlvakoo--307316192.jpg"
        },
        "user": {
            "id": 5,
            "username": "test930",
            "first_name": "임선빈"
        }
    },
    {
        "id": 10,
        "priority": 2,
        "is_active": true,
        "create_date": "2020-11-13T17:22:02.685343+09:00",
        "update_date": "2020-11-14T18:10:43.871750+09:00",
        "item": {
            "id": 13,
            "name": "갤럭시탭A7",
            "thumbnail": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/sec-galaxy-tab-a7-t500-sm-t500nzaekoo-----------306748675.jpg"
        },
        "user": {
            "id": 5,
            "username": "test930",
            "first_name": "임선빈"
        }
    },
    {
        "id": 9,
        "priority": 3,
        "is_active": true,
        "create_date": "2020-11-13T17:21:59.116707+09:00",
        "update_date": "2020-11-14T18:19:15.989505+09:00",
        "item": {
            "id": 14,
            "name": "갤럭시탭S7",
            "thumbnail": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/sec-galaxy-tab-s7-plus-5g-t976-sm-t976nznhkoo-frontmysticbronze-295760031.jpg"
        },
        "user": {
            "id": 7,
            "username": "zinxi12",
            "first_name": "진시황"
        }
    },
    {
        "id": 8,
        "priority": 4,
        "is_active": true,
        "create_date": "2020-11-13T17:20:27.145244+09:00",
        "update_date": "2020-11-14T18:10:35.560233+09:00",
        "item": {
            "id": 9,
            "name": "맥북",
            "thumbnail": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/login1_LGw1qzC.png"
        },
        "user": {
            "id": 4,
            "username": "songsong",
            "first_name": "송은석"
        }
    }
]
```





### 메인화면 아이템 생성

```
주소/api/services/main/(POST)
```

> id는 아이템의 id 이다.

- Body

```json
{
    "priority": 1,
    "is_active": "False",
    "id": 1
}
```

- Response

```json
{
    "id": 7,
    "priority": 1,
    "is_active": true,
    "create_date": "2020-11-13T16:34:01.761616+09:00",
    "update_date": "2020-11-13T16:36:52.915709+09:00",
    "item": {
        "id": 5,
        "name": "오디세이",
        "thumbnail": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/KakaoTalk_20200921_091027148_d7tAwaw.png"
    },
    "user": {
        "id": 2,
        "username": "test",
        "first_name": "김유기"
    }
}
```



### 메인화면 아이템 상세 정보

```
주소/api/services/main/<int:pk>/(GET)
```

- Response

```json
{
    "id": 7,
    "priority": 1,
    "is_active": true,
    "create_date": "2020-11-13T16:34:01.761616+09:00",
    "update_date": "2020-11-13T16:36:52.915709+09:00",
    "item": {
        "id": 5,
        "name": "오디세이",
        "thumbnail": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/KakaoTalk_20200921_091027148_d7tAwaw.png"
    },
    "user": {
        "id": 2,
        "username": "test",
        "first_name": "김유기"
    }
}
```



### 메인화면 아이템 활성화

```
주소/api/services/main/<int:pk>/(POST)
```

- Response

```json
{
    "id": 7,
    "priority": 1,
    "is_active": true,
    "create_date": "2020-11-13T16:34:01.761616+09:00",
    "update_date": "2020-11-13T16:36:52.915709+09:00",
    "item": {
        "id": 5,
        "name": "오디세이",
        "thumbnail": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/KakaoTalk_20200921_091027148_d7tAwaw.png"
    },
    "user": {
        "id": 2,
        "username": "test",
        "first_name": "김유기"
    }
}
```



### 메인화면 아이템 수정

```
주소/api/services/main/<int:pk>/(PUT)
```

- Body

```json
{
    "priority": 2,
    "is_active": "False",
    "id": 1
}
```

- Response

```json
{
    "id": 7,
    "priority": 1,
    "is_active": true,
    "create_date": "2020-11-13T16:34:01.761616+09:00",
    "update_date": "2020-11-13T16:36:52.915709+09:00",
    "item": {
        "id": 1,
        "name": "오디세이",
        "thumbnail": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/KakaoTalk_20200921_091027148_d7tAwaw.png"
    },
    "user": {
        "id": 2,
        "username": "test",
        "first_name": "김유기"
    }
}
```



### 메인화면 아이템 비활성화

```
주소/api/services/main/<int:pk>/(DELETE)
```

- Response

```json
{
    "message": "해당 메인 아이템을 비활성화 했습니다."
}
```





### 케로셀 아이템 모든 정보

```
주소/api/services/carousel/(GET)
```

- Response

```json
[
    {
        "id": 3,
        "title": "대나무 이미지",
        "priority": 1,
        "image": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/844-1920x600_fgfeLej.jpg",
        "is_active": false,
        "url": "",
        "create_date": "2020-11-13T15:13:20.821196+09:00",
        "update_date": "2020-11-13T15:13:20.821242+09:00",
        "user": {
            "id": 5,
            "username": "test930",
            "first_name": "임선빈"
        }
    },
    {
        "id": 2,
        "title": "시계 이미지",
        "priority": 1,
        "image": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/157-1920x600_3uT1JVu.jpg",
        "is_active": true,
        "url": "",
        "create_date": "2020-11-13T12:51:35.725746+09:00",
        "update_date": "2020-11-13T12:51:39.580436+09:00",
        "user": {
            "id": 5,
            "username": "test930",
            "first_name": "임선빈"
        }
    },
    {
        "id": 1,
        "title": "더미 이미지",
        "priority": 1,
        "image": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/dummy-img_3wnOEpr.png",
        "is_active": true,
        "url": "",
        "create_date": "2020-11-13T12:44:09.960828+09:00",
        "update_date": "2020-11-13T12:44:13.543429+09:00",
        "user": {
            "id": 5,
            "username": "test930",
            "first_name": "임선빈"
        }
    }
]
```



### 케로셀 아이템 생성

```
주소/api/services/carousel/(POST)
```

- Body

```json
{
    "image": "이미지 파일",
    "url": "입력 url",
    "is_active": "True",
    "priority": 1
}
```

- Response

```json
{
    "id": 1,
    "priority": 1,
    "image": "/media/KakaoTalk_20201019_093205576_0AlpIJQ.png",
    "is_active": true,
    "url": "naver.com",
    "create_date": "2020-11-09T10:44:02.906764+09:00",
    "update_date": "2020-11-09T10:44:02.906764+09:00",
    "user": {
        "id": 2,
        "username": "test",
        "first_name": "김유기"
    }
}
```



### 케로셀 아이템 상세조회

```
주소/api/services/carousel/<int:pk>/(GET)
```

- Response

```json
{
    "id": 1,
    "priority": 1,
    "image": "/media/KakaoTalk_20201019_093205576_0AlpIJQ.png",
    "is_active": true,
    "url": "naver.com",
    "create_date": "2020-11-09T10:44:02.906764+09:00",
    "update_date": "2020-11-09T10:44:02.906764+09:00",
    "user": {
        "id": 2,
        "username": "test",
        "first_name": "김유기"
    }
}
```



### 케로셀 아이템 활성화

```
주소/api/services/carousel/<int:pk>/(POST)
```

- Response

```json
{
    "id": 1,
    "priority": 1,
    "image": "/media/KakaoTalk_20201019_093205576_0AlpIJQ.png",
    "is_active": true,
    "url": "naver.com",
    "create_date": "2020-11-09T10:44:02.906764+09:00",
    "update_date": "2020-11-09T11:00:31.064391+09:00",
    "user": {
        "id": 2,
        "username": "test",
        "first_name": "김유기"
    }
}
```



### 케로셀 아이템 수정

```
주소/api/services/carousel/<int:pk>/(PUT)
```

- Body

```json
{
    "image": "이미지 파일",
    "url": "입력 url",
    "is_active": "True",
    "priority": 1
}
```

- Response

```json
{
    "id": 1,
    "priority": 1,
    "image": "/media/KakaoTalk_20201019_093205576_0AlpIJQ.png",
    "is_active": true,
    "url": "naver.com",
    "create_date": "2020-11-09T10:44:02.906764+09:00",
    "update_date": "2020-11-09T11:00:31.064391+09:00",
    "user": {
        "id": 2,
        "username": "test",
        "first_name": "김유기"
    }
}
```





### 케로셀 아이템 비활성화

```
주소/api/services/carousel/<int:pk>/(DELETE)
```

- Response

```json
{
    "message": "케로셀 아이템이 비활성화 되었습니다."
}
```





## Custmoer API

### item, event search

```
주소/api/services/customer/search/?content=<>
```

- Response

```json
{
    "items": [
        {
            "id": 1,
            "name": "노트북A",
            "price": 1280000,
            "template": 2,
            "images": [],
            "descriptions": [
                {
                    "id": 1,
                    "category_description": {
                        "id": 14,
                        "name": "제조사"
                    },
                    "content": "AMD"
                }
            ]
        },
        {
            "id": 2,
            "name": "노트북A",
            "price": 1280000,
            "template": 2,
            "images": [
                {
                    "id": 1,
                    "item_image": "/media/KakaoTalk_20201019_093205576_ni0qpZF.png",
                    "is_thumbnail": true,
                    "priority": 1
                }
            ],
            "descriptions": []
        }
    ],
    "events": [
        {
            "id": 1,
            "title": "테스트",
            "start_date": "2020-11-04T00:00:00+09:00",
            "end_date": "2020-11-04T23:59:59+09:00",
            "thumbnail_image": "/media/KakaoTalk_20200807_125333367_IjSlCrP.png",
            "priority": 1
        }
    ]
}
```



### 카테고리 리스트

```
주소/api/products/customer/categories/(GET)
```

- Response

```json
[
    {
        "id": 1,
        "name": "노트북",
        "image": null
    }
]
```



### 카테고리에 속한 아이템 리스트

```
주소/api/products/customer/categories/<int:pk>/ (GET)
```

- Response

```json
{
    "id": 1,
    "name": "노트북",
    "image": null,
    "template": 1,
    "items": [
        {
            "id": 1,
            "name": "노트북A",
            "price": 1280000,
            "template": 2,
            "images": [],
            "descriptions": [
                {
                    "id": 1,
                    "category_description": {
                        "id": 14,
                        "name": "제조사"
                    },
                    "content": "AMD"
                }
            ]
        },
        {
            "id": 2,
            "name": "노트북A",
            "price": 1280000,
            "template": 2,
            "images": [
                {
                    "id": 1,
                    "item_image": "/media/KakaoTalk_20201019_093205576_ni0qpZF.png",
                    "is_thumbnail": true,
                    "priority": 1
                }
            ],
            "descriptions": []
        }
    ]
}
```



### 아이템 상세정보

```
주소/products/customer/product/<int:pk>/ (GET)
```

- Response

```json
{
    "id": 1,
    "name": "노트북A",
    "price": 1280000,
    "template": 2,
    "images": [],
    "descriptions": [
        {
            "id": 1,
            "category_description": {
                "id": 14,
                "name": "제조사"
            },
            "content": "AMD"
        }
    ]
}
```



### 메인아이템 조회

```
주소/api/services/customer/event/(GET)
```

- Response

```json
[
    {
        "id": 14,
        "priority": 1,
        "item": {
            "id": 17,
            "name": "테스트",
            "thumbnail": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/2020-11-14_174143_KakaoTalk_20200921_091027148.png"
        }
    },
    {
        "id": 10,
        "priority": 2,
        "item": {
            "id": 13,
            "name": "갤럭시탭A7",
            "thumbnail": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/sec-galaxy-tab-a7-t500-sm-t500nzaekoo-----------306748675.jpg"
        }
    },
    {
        "id": 9,
        "priority": 3,
        "item": {
            "id": 14,
            "name": "갤럭시탭S7",
            "thumbnail": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/sec-galaxy-tab-s7-plus-5g-t976-sm-t976nznhkoo-frontmysticbronze-295760031.jpg"
        }
    },
    {
        "id": 8,
        "priority": 4,
        "item": {
            "id": 9,
            "name": "맥북",
            "thumbnail": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/login1_LGw1qzC.png"
        }
    }
]
```



### 케로셀 아이템 조회

```
주소/api/services/customer/carousel/(GET)
```

- Response

```json
[
    {
        "id": 1,
        "image": "/media/KakaoTalk_20201019_093205576_0AlpIJQ.png",
        "url": "naver.com"
    }
]
```



### 이벤트 리스트 조회

```
주소/api/services/customer/event/(GET)
```

- Response

```json
[
    {
        "id": 1,
        "title": "테스트",
        "start_date": "2020-11-04T00:00:00+09:00",
        "end_date": "2020-11-04T23:59:59+09:00",
        "thumbnail_image": "/media/KakaoTalk_20200807_125333367_IjSlCrP.png",
        "priority": 1
    }
]
```



### 이벤트 상세 조회

```
주소/api/services/customer/event/<int:pk>/(GET)
```

- Response

```json
{
    "id": 1,
    "title": "테스트",
    "start_date": "2020-11-04T00:00:00+09:00",
    "end_date": "2020-11-04T23:59:59+09:00",
    "thumbnail_image": "/media/KakaoTalk_20200807_125333367_IjSlCrP.png",
    "priority": 1,
    "content": "테스트",
    "url": "test",
    "images": [
        {
            "id": 1,
            "image": "/media/KakaoTalk_20200807_125333367_urZx5Yl.png",
            "priority": 1
        }
    ]
}
```



### 공지사항 리스트 조회

```
주소/services/customer/notices/(GET)
```

- Response

```json
[
    {
        "id": 3,
        "title": "1번 공지",
        "content": "1번 공지",
        "start_date": "2020-11-13T14:14:37.004201+09:00",
        "image": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/login1_piqculY.png"
    },
    {
        "id": 4,
        "title": "2번 공지",
        "content": "2번 공지",
        "start_date": "2020-11-13T15:12:04.673845+09:00",
        "image": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/cat_4xuOtqq.jpg"
    },
    {
        "id": 8,
        "title": "유기 test",
        "content": "134",
        "start_date": "2020-11-13T16:00:09.995162+09:00",
        "image": "https://ssafycmss3bucket.s3.ap-northeast-2.amazonaws.com/media/cat.jpg"
    }
]
```

