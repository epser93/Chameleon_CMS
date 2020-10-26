# REST API 명세서

| url                                           | GET                 | POST               | PUT                 | DELETE        |
| --------------------------------------------- | ------------------- | ------------------ | ------------------- | ------------- |
| accounts/login/                               |                     | 로그인             |                     |               |
| accounts/signup/                              |                     | 회원가입           |                     |               |
| accounts/management/                          |                     | 회원가입 승인      | 회원권한 수정       |               |
| accounts/log                                  | 로그데이터          |                    |                     |               |
| products/main/                                | 메인페이지 상세     |                    |                     |               |
| products/main/carousel/                       |                     | 대표페이지 등록    |                     |               |
| products/category/                            | 카테고리 리스트     | 카테고리 생성      |                     |               |
| products/category/<category_id>/              | 카테고리 물품리스트 |                    | 카테고리 수정       | 카테고리 삭제 |
| products/product/                             |                     | 제품생성(임시까지) |                     |               |
| products/product/<product_id>/                | 제품 상세정보       |                    | 제품 수정           | 제품 삭제     |
| products/serarch/?type=<>&content=<>&order=<> | 검색                |                    |                     |               |
| products/notices/                             | 공지사항 리스트     | 공지사항 생성      |                     |               |
| products/notices/<notices_id>/                | 공지사항 상세       |                    | 공지사항 수정       | 공지사항 삭제 |
| products/event/                               | 이벤트 리스트       | 이벤트 생성        |                     |               |
| products/event/<event_id>/                    | 이벤트 상세         |                    | 이벤트 수정         | 이벤트 삭제   |
| products/faq/                                 | FAQ 리스트          | FAQ 생성           |                     |               |
| products/faq/<faq_id>/                        | FAQ 상세            |                    | FAQ 수정            | FAQ 삭제      |
| products/company/                             | 회사 정보           |                    | 회사 정보 수정      |               |
| products/contect/                             | contact 정보        |                    | contact 이미지 수정 |               |
| manual/                                       | 메뉴얼 페이지       |                    |                     |               |

