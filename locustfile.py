from locust import HttpUser, TaskSet, task, between


# UserBehavior 클래스는 TaskSet을 상속받아 사용자 행동을 정의합니다.
class UserBehavior(TaskSet):
    # on_start 메서드는 테스트 시작 시 호출되며, 로그인 작업을 수행합니다.
    def on_start(self):  # ✅ 이 메서드는 테스트가 시작될 때 자동으로 호출됩니다. (TaskSet 클래스에 정의 되어 있음.)
        self.login()  # ✅ 이 메서드는 self.login()을 호출하여 로그인 작업을 수행합니다.

    # login 메서드는 로그인 요청을 보내고, 성공 여부를 확인합니다.
    def login(self):  # ✅ 이 메서드는 실제로 로그인 요청을 웹사이트에 보냅니다.
        response = self.client.post("/login", json={"username": "user", "password": "password"},
                                    headers={"Content-Type": "application/json", "accept": "*/*"})
        if response.status_code == 200 and response.json().get("message") == "Login successful":
            self.logged_in = True  # ✅ 로그인에 성공하면 self.logged_in을 True로 설정합니다.
        else:
            print("로그인에 실패했습니다:", response.text)  # ✅ 로그인에 실패하면 실패 메시지를 출력합니다.
            self.logged_in = False  # ✅ 로그인에 실패하면 self.logged_in을 False로 설정합니다.

    # get_users 메서드는 로그인된 상태에서 /users 엔드포인트에 GET 요청을 보냅니다.
    @task(50)  # ✅ 이 코드는 Locust가 이 작업을 50번 반복하도록 설정합니다.
    def get_users(self):
        if self.logged_in:  # ✅ 사용자가 로그인된 상태인지 확인합니다.
            # time.sleep(5)  # 인위적인 지연 추가 (성능병목현상 테스트 목적)
            self.client.get("/users", headers={"accept": "*/*"})  # ✅ /users 주소로 GET 요청을 보냅니다.
            print("get_users")  # ✅ "get_users"라는 메시지를 출력합니다.
        else:
            print("로그인에 실패하여 작업을 수행할 수 없습니다.")  # ✅ 로그인되지 않은 상태에서 메시지를 출력합니다.

    # get_current_date 메서드는 로그인된 상태에서 /users/currentDate 엔드포인트에 GET 요청을 보냅니다.
    @task(1)  # ✅ 이 코드는 Locust가 이 작업을 1번 수행하도록 설정합니다.
    def get_current_date(self):
        if self.logged_in:  # ✅ 사용자가 로그인된 상태인지 확인합니다.
            self.client.get("/users/currentDate", headers={"accept": "*/*"})  # ✅ /users/currentDate 주소로 GET 요청을 보냅니다.
            print("get_current_date")  # ✅ "get_current_date"라는 메시지를 출력합니다.
        else:
            print("로그인에 실패하여 작업을 수행할 수 없습니다.")  # ✅ 로그인되지 않은 상태에서 메시지를 출력합니다.

    # force_global_exception 메서드는 로그인된 상태에서 /users/forceGlobalException 엔드포인트에 GET 요청을 보냅니다.
    @task(1)  # ✅ 이 코드는 Locust가 이 작업을 1번 수행하도록 설정합니다.
    def force_global_exception(self):
        if self.logged_in:  # ✅ 사용자가 로그인된 상태인지 확인합니다.
            self.client.get("/users/forceGlobalException",
                            headers={"accept": "*/*"})  # ✅ /users/forceGlobalException 주소로 GET 요청을 보냅니다.
            print("force_global_exception")  # ✅ "force_global_exception"라는 메시지를 출력합니다.
        else:
            print("로그인에 실패하여 작업을 수행할 수 없습니다.")  # ✅ 로그인되지 않은 상태에서 메시지를 출력합니다.

    # force_exception 메서드는 로그인된 상태에서 /users/forceException 엔드포인트에 GET 요청을 보냅니다.
    @task(1)  # ✅ 이 코드는 Locust가 이 작업을 1번 수행하도록 설정합니다.
    def force_exception(self):
        if self.logged_in:  # ✅ 사용자가 로그인된 상태인지 확인합니다.
            self.client.get("/users/forceException",
                            headers={"accept": "*/*"})  # ✅ /users/forceException 주소로 GET 요청을 보냅니다.
            print("force_exception")  # ✅ "force_exception"라는 메시지를 출력합니다.
        else:
            print("로그인에 실패하여 작업을 수행할 수 없습니다.")  # ✅ 로그인되지 않은 상태에서 메시지를 출력합니다.

    # create_user 메서드는 로그인된 상태에서 /users/create 엔드포인트에 POST 요청을 보냅니다.
    @task(1)  # ✅ 이 코드는 Locust가 이 작업을 1번 수행하도록 설정합니다.
    def create_user(self):
        if self.logged_in:  # ✅ 사용자가 로그인된 상태인지 확인합니다.
            self.client.post("/users/create?name=John%20Doe&email=john.doe%40example.com", headers={"accept": "*/*"},
                             data="")  # ✅ /users/create 주소로 POST 요청을 보냅니다.
            print("create_user")  # ✅ "create_user"라는 메시지를 출력합니다.
        else:
            print("로그인에 실패하여 작업을 수행할 수 없습니다.")  # ✅ 로그인되지 않은 상태에서 메시지를 출력합니다.

    # update_user 메서드는 로그인된 상태에서 /users/1 엔드포인트에 PUT 요청을 보냅니다.
    @task(1)  # ✅ 이 코드는 Locust가 이 작업을 1번 수행하도록 설정합니다.
    def update_user(self):
        if self.logged_in:  # ✅ 사용자가 로그인된 상태인지 확인합니다.
            self.client.put("/users/1?name=Jane%20Doe1&email=jane.doe%40example.com1",
                            headers={"accept": "*/*"})  # ✅ /users/1 주소로 PUT 요청을 보냅니다.
            print("update_user")  # ✅ "update_user"라는 메시지를 출력합니다.
        else:
            print("로그인에 실패하여 작업을 수행할 수 없습니다.")  # ✅ 로그인되지 않은 상태에서 메시지를 출력합니다.

    # delete_user 메서드는 로그인된 상태에서 /users/{user_id} 엔드포인트에 DELETE 요청을 보냅니다.
    @task(1)  # ✅ 이 코드는 Locust가 이 작업을 1번 수행하도록 설정합니다.
    def delete_user(self):
        if self.logged_in:  # ✅ 사용자가 로그인된 상태인지 확인합니다.
            for user_id in range(1, 11):
                self.client.delete(f"/users/{user_id}",
                                   headers={"accept": "*/*"})  # ✅ /users/{user_id} 주소로 DELETE 요청을 보냅니다.
                print(f"delete_user {user_id}")  # ✅ "delete_user {user_id}"라는 메시지를 출력합니다.
        else:
            print("로그인에 실패하여 작업을 수행할 수 없습니다.")  # ✅ 로그인되지 않은 상태에서 메시지를 출력합니다.

    # 비동기 작업 테스트 (10% 확률로 실행) - async_process 메서드는 /async/process 엔드포인트에 GET 요청을 보냅니다.
    @task(10)  # ✅ 이 코드는 Locust가 이 작업을 10% 확률로 수행하도록 설정합니다.
    def async_process(self):  # ✅ 이 메서드는 /async/process 엔드포인트에 GET 요청을 보냅니다.
        if self.logged_in:  # ✅ 사용자가 로그인된 상태인지 확인합니다.
            response = self.client.get("/async/process",
                                       headers={"accept": "*/*"})  # ✅ /async/process 주소로 GET 요청을 보냅니다.
            if response.status_code == 200:  # ✅ 응답 코드가 200인지 확인합니다.
                print("async_process 성공")  # ✅ "async_process 성공"이라는 메시지를 출력합니다.
            else:
                print(f"async_process 실패: {response.status_code}, {response.text}")  # ✅ 실패 메시지를 출력합니다.
        else:
            print("로그인에 실패하여 작업을 수행할 수 없습니다.")  # ✅ 로그인되지 않은 상태에서 메시지를 출력합니다.


# WebsiteUser 클래스는 HttpUser를 상속받아 사용자 시뮬레이션을 정의합니다.
class WebsiteUser(HttpUser):
    tasks = [UserBehavior]  # ✅ UserBehavior 클래스를 사용하여 사용자의 행동을 정의합니다.
    wait_time = between(1, 5)  # ✅ 사용자가 다음 행동을 하기 전에 기다리는 시간을 설정합니다.
    host = "http://localhost:8080"  # ✅ 테스트할 웹사이트의 주소를 설정합니다.

    # on_start 메서드는 부하 테스트 시작 시 호출됩니다.
    def on_start(self):
        print("부하테스트가 시작합니다.")  # ✅ "부하테스트가 시작합니다."라는 메시지를 출력합니다.

    # on_stop 메서드는 부하 테스트 종료 시 호출됩니다.
    def on_stop(self):
        print("부하테스트가 끝났습니다.")  # ✅ "부하테스트가 끝났습니다."라는 메시지를 출력합니다.
