from locust import HttpUser, between, task
import uuid
import random

token = ""


class WebsiteUser(HttpUser):
    # host = "http://213.233.179.83"
    host = "http://localhost:3000"

    @task(1)
    def addUser(self):
        result = self.client.post(
            "/sign_up",
            json={"email": "efpyi@example.com",
                  "password": "123",
                  "firstName": "shahab",
                  "lastName": "hoseeini",
                  "gender": "M",
                  "phoneNumber": "09161234123"
                  }).json()

        assert result["token"] is not None
        token = result["token"]

        @task(2)
        def getCities(self):
            result = self.client.get("/cities")
            assert result.status_code == 200

        @task(3)
        def logOut(self):
            result = self.client.post("/logout", headers={"Token": token})
            assert result.status_code == 200
