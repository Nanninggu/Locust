import time

from locust import HttpUser, TaskSet, task, between


class UserBehavior(TaskSet):
    def on_start(self):
        self.login()

    def login(self):
        response = self.client.post("/login", json={"username": "user", "password": "password"},
                                    headers={"Content-Type": "application/json", "accept": "*/*"})
        if response.status_code == 200 and response.json().get("message") == "Login successful":
            self.logged_in = True
        else:
            print("로그인에 실패했습니다:", response.text)
            self.logged_in = False

    @task(30)
    def get_users(self):
        if self.logged_in:
            self.client.get("/users", headers={"accept": "*/*"})
            print("get_users")
        else:
            print("로그인에 실패하여 작업을 수행할 수 없습니다.")

    @task(10)
    def get_current_date(self):
        time.sleep(60)  # 인위적인 지연 추가 (성능병목현상 테스트 목적)
        if self.logged_in:
            self.client.get("/users/currentDate", headers={"accept": "*/*"})
            print("get_current_date")
        else:
            print("로그인에 실패하여 작업을 수행할 수 없습니다.")

    @task(1)
    def force_global_exception(self):
        if self.logged_in:
            self.client.get("/users/forceGlobalException", headers={"accept": "*/*"})
            print("force_global_exception")
        else:
            print("로그인에 실패하여 작업을 수행할 수 없습니다.")

    @task(1)
    def force_exception(self):
        if self.logged_in:
            self.client.get("/users/forceException", headers={"accept": "*/*"})
            print("force_exception")
        else:
            print("로그인에 실패하여 작업을 수행할 수 없습니다.")

    @task(1)
    def create_user(self):
        if self.logged_in:
            self.client.post("/users/create?name=John%20Doe&email=john.doe%40example.com", headers={"accept": "*/*"},
                             data="")
            print("create_user")
        else:
            print("로그인에 실패하여 작업을 수행할 수 없습니다.")

    @task(1)
    def update_user(self):
        if self.logged_in:
            self.client.put("/users/update?name=John%20Doe&email=john.doe%40example.com", headers={"accept": "*/*"},
                            data="")
            print("update_user")
        else:
            print("로그인에 실패하여 작업을 수행할 수 없습니다.")

    @task(1)
    def delete_user(self):
        if self.logged_in:
            self.client.delete("/users/delete?name=John%20Doe", headers={"accept": "*/*"},
                               data="")
            print("delete_user")
        else:
            print("로그인에 실패하여 작업을 수행할 수 없습니다.")

    # 성능병목현상 테스트 목적 (성능 테스트 목적)
    @task(5)
    def get_bottleneck(self):
        if self.logged_in:
            self.client.get("/users/bottleneck", headers={"accept": "*/*"})
            print("get_bottleneck")
        else:
            print("로그인에 실패하여 작업을 수행할 수 없습니다.")

class WebsiteUser(HttpUser):
    tasks = {UserBehavior}
    wait_time = between(1, 5)
    host = "http://localhost:8080"

    def on_start(self):
        print("Starting Load Test")

    def on_stop(self):
        print("Stopping Load Test")
