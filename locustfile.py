import time 
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    @task
    def integration(self):
        self.client.get("http://127.0.0.1:5000/integration")