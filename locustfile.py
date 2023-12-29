import time 
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    @task
    def integration(self):
        self.client.get("https://lab2-function-app.azurewebsites.net/api/httpfunctionapp")