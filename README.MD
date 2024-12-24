다음은 주어진 코드를 기반으로 작성된 `README.md` 파일입니다.

## 사용법

1. `locustfile.py` 파일을 실행합니다.

```bash
locust -f locustfile.py
```

2. 웹 브라우저를 열고 `http://localhost:8089`에 접속합니다.

3. 웹 인터페이스에서 테스트할 사용자 수와 스폰 속도를 설정한 후, "Start swarming" 버튼을 클릭하여 테스트를 시작합니다.

## 코드 설명

### UserBehavior 클래스

`UserBehavior` 클래스는 사용자의 행동을 정의합니다. 각 메서드는 특정 HTTP 요청을 수행합니다.

- `on_start`: 테스트 시작 시 로그인 메서드를 호출합니다.
- `login`: `/login` 엔드포인트로 POST 요청을 보내어 로그인합니다.
- `get_users`: `/users` 엔드포인트로 GET 요청을 보냅니다.
- `get_current_date`: `/users/currentDate` 엔드포인트로 GET 요청을 보냅니다. (인위적인 지연 포함)
- `force_global_exception`: `/users/forceGlobalException` 엔드포인트로 GET 요청을 보냅니다.
- `force_exception`: `/users/forceException` 엔드포인트로 GET 요청을 보냅니다.
- `create_user`: `/users/create` 엔드포인트로 POST 요청을 보냅니다.
- `update_user`: `/users/update` 엔드포인트로 PUT 요청을 보냅니다.
- `delete_user`: `/users/delete` 엔드포인트로 DELETE 요청을 보냅니다.
- `get_bottleneck`: `/users/bottleneck` 엔드포인트로 GET 요청을 보냅니다. (성능 병목 현상 테스트 목적)

### WebsiteUser 클래스

`WebsiteUser` 클래스는 Locust의 `HttpUser` 클래스를 상속받아 사용자의 행동을 정의합니다.

- `tasks`: 사용자의 행동으로 `UserBehavior` 클래스를 설정합니다.
- `wait_time`: 각 요청 사이의 대기 시간을 설정합니다.
- `host`: 테스트할 서버의 호스트 주소를 설정합니다.
- `on_start`: 테스트 시작 시 호출됩니다.
- `on_stop`: 테스트 종료 시 호출됩니다.

## 주의사항

- 테스트를 실행하기 전에 `host` 변수를 실제 테스트할 서버의 주소로 변경해야 합니다.
- 로그인 정보는 `login` 메서드에서 설정할 수 있습니다.

이 프로젝트는 Locust를 사용하여 HTTP 서버의 성능을 테스트하는 데 유용합니다. 각 메서드는 특정 엔드포인트에 대한 요청을 수행하며, 이를 통해 서버의 응답 시간을 측정하고 성능 병목 현상을 식별할 수 있습니다.
```