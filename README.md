# 프로젝트 이름

이 프로젝트는 Locust를 사용하여 웹 애플리케이션의 부하 테스트를 수행하는 예제입니다.

## 설치 및 실행 방법

### 요구 사항

- Python 3.x
- Locust

### 설치

다음 명령어를 사용하여 필요한 패키지를 설치합니다:

```bash
pip install locust
```

### 실행

다음 명령어를 사용하여 Locust 부하 테스트를 실행합니다:

```bash
locust -f locustfile.py
```

웹 브라우저에서 `http://localhost:8089`에 접속하여 부하 테스트를 시작할 수 있습니다.

## 코드 설명

### `locustfile.py`

이 파일은 Locust를 사용하여 부하 테스트를 수행하는 스크립트입니다. 주요 클래스와 메서드는 다음과 같습니다:

- `UserBehavior`: 사용자 행동을 정의하는 클래스입니다. 로그인, 사용자 정보 조회, 사용자 생성, 업데이트, 삭제 등의 작업을 수행합니다.
- `WebsiteUser`: Locust의 `HttpUser`를 상속받아 사용자 시뮬레이션을 정의하는 클래스입니다.

### 주요 메서드

- `on_start`: 테스트 시작 시 호출되며, 로그인 작업을 수행합니다.
- `login`: 로그인 요청을 보내고, 성공 여부를 확인합니다.
- `get_users`: 로그인된 상태에서 `/users` 엔드포인트에 GET 요청을 보냅니다.
- `get_current_date`: 로그인된 상태에서 `/users/currentDate` 엔드포인트에 GET 요청을 보냅니다.
- `create_user`: 로그인된 상태에서 `/users/create` 엔드포인트에 POST 요청을 보냅니다.
- `update_user`: 로그인된 상태에서 `/users/1` 엔드포인트에 PUT 요청을 보냅니다.
- `delete_user`: 로그인된 상태에서 `/users/{user_id}` 엔드포인트에 DELETE 요청을 보냅니다.