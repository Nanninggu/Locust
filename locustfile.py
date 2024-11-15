from locust import HttpUser, TaskSet, task, between

# UserBehavior 클래스는 TaskSet을 상속받아 사용자 행동을 정의합니다.
class UserBehavior(TaskSet):
    # on_start 메서드는 테스트 시작 시 호출되며, 로그인 작업을 수행합니다.
    def on_start(self):
        self.login()

    # login 메서드는 로그인 요청을 보내고, 성공 여부를 확인합니다.
    def login(self):
        response = self.client.post("/login", json={"username": "user", "password": "password"},
                                    headers={"Content-Type": "application/json", "accept": "*/*"})
        if response.status_code == 200 and response.json().get("message") == "Login successful":
            self.logged_in = True
        else:
            print("로그인에 실패했습니다:", response.text)
            self.logged_in = False

    # get_users 메서드는 로그인된 상태에서 /users 엔드포인트에 GET 요청을 보냅니다.
    @task(50)
    def get_users(self):
        if self.logged_in:
            # time.sleep(5)  # 인위적인 지연 추가 (성능병목현상 테스트 목적)
            self.client.get("/users", headers={"accept": "*/*"})
            print("get_users")
        else:
            print("로그인에 실패하여 작업을 수행할 수 없습니다.")

    # get_current_date 메서드는 로그인된 상태에서 /users/currentDate 엔드포인트에 GET 요청을 보냅니다.
    @task(1)
    def get_current_date(self):
        if self.logged_in:
            self.client.get("/users/currentDate", headers={"accept": "*/*"})
            print("get_current_date")
        else:
            print("로그인에 실패하여 작업을 수행할 수 없습니다.")

    # force_global_exception 메서드는 로그인된 상태에서 /users/forceGlobalException 엔드포인트에 GET 요청을 보냅니다.
    @task(1)
    def force_global_exception(self):
        if self.logged_in:
            self.client.get("/users/forceGlobalException", headers={"accept": "*/*"})
            print("force_global_exception")
        else:
            print("로그인에 실패하여 작업을 수행할 수 없습니다.")

    # force_exception 메서드는 로그인된 상태에서 /users/forceException 엔드포인트에 GET 요청을 보냅니다.
    @task(1)
    def force_exception(self):
        if self.logged_in:
            self.client.get("/users/forceException", headers={"accept": "*/*"})
            print("force_exception")
        else:
            print("로그인에 실패하여 작업을 수행할 수 없습니다.")

    # create_user 메서드는 로그인된 상태에서 /users/create 엔드포인트에 POST 요청을 보냅니다.
    @task(1)
    def create_user(self):
        if self.logged_in:
            self.client.post("/users/create?name=John%20Doe&email=john.doe%40example.com", headers={"accept": "*/*"},
                             data="")
            print("create_user")
        else:
            print("로그인에 실패하여 작업을 수행할 수 없습니다.")

    # update_user 메서드는 로그인된 상태에서 /users/1 엔드포인트에 PUT 요청을 보냅니다.
    @task(1)
    def update_user(self):
        if self.logged_in:
            self.client.put("/users/1?name=Jane%20Doe1&email=jane.doe%40example.com1", headers={"accept": "*/*"})
            print("update_user")
        else:
            print("로그인에 실패하여 작업을 수행할 수 없습니다.")

    # delete_user 메서드는 로그인된 상태에서 /users/{user_id} 엔드포인트에 DELETE 요청을 보냅니다.
    @task(1)
    def delete_user(self):
        if self.logged_in:
            for user_id in range(1, 11):
                self.client.delete(f"/users/{user_id}", headers={"accept": "*/*"})
                print(f"delete_user {user_id}")
        else:
            print("로그인에 실패하여 작업을 수행할 수 없습니다.")

# WebsiteUser 클래스는 HttpUser를 상속받아 사용자 시뮬레이션을 정의합니다.
class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
    host = "http://localhost:8080"

    # on_start 메서드는 부하 테스트 시작 시 호출됩니다.
    def on_start(self):
        print("부하테스트가 시작합니다.")

    # on_stop 메서드는 부하 테스트 종료 시 호출됩니다.
    def on_stop(self):
        print("부하테스트가 끝났습니다.")