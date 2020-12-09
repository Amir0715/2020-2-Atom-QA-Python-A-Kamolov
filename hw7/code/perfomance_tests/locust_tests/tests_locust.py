from locust import HttpUser, TaskSet, task, between


class IOSUserBehavior(TaskSet):
    login = "yno"

    def on_start(self):
        r = self.client.get("/", auth=(self.login, 333))
        self.client.headers.update({'Authorization': r.request.headers['Authorization']})

    def on_stop(self):
        self.client.get("/logout")

    @task
    def profile(self):
        self.client.get("/profile")

    @task
    def photos(self):
        for i in range(5):
            self.client.get(f"/photos/{i}")

    @task
    def shareware(self):
        self.client.get("/shareware")

class AndroidUserBehavior(TaskSet):
    login = "amir"

    def on_start(self):
        r = self.client.get("/", auth=(self.login, 123))
        self.client.headers.update({'Authorization': r.request.headers['Authorization']})

    def on_stop(self):
        self.client.get("/logout")

    @task
    def shareware(self):
        self.client.get("/shareware")

    @task
    def photos(self):
        self.client.get("/photos")

    @task
    def emails(self):
        self.client.get(f"/profile/{self.login}")

class DesktopUserBehavior(TaskSet):
    login = "alex"

    def on_start(self):
        r = self.client.get("/", auth=(self.login, 321))
        self.client.headers.update({'Authorization': r.request.headers['Authorization']})

    def on_stop(self):
        self.client.get("/logout")

    @task
    def shareware(self):
        self.client.get("/shareware")

    @task
    def photos(self):
        for i in range(12):
            self.client.get(f"/photos/{i}")

    @task
    def emails(self):
        self.client.get(f"/profile/{self.login}")


class WebsiteUser(HttpUser):
    tasks = [IOSUserBehavior, AndroidUserBehavior, DesktopUserBehavior]
    wait_time = between(1, 2)