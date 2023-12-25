import time 
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    @task
    def integration(self):
        self.client.get("https://webapp-scaling.azurewebsites.net/integration")