import time
import random
from locust import task, constant, events, run_single_user
from locust_plugins.users.webdriver import WebdriverUser
from locust_plugins.listeners import RescheduleTaskOnFail
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class UPRUser(WebdriverUser):
    wait_time = constant(5)
    command_executor = "http://selenium-hub:4444/wd/hub"

    def __init__(self, environment, *args, **kwargs):
        super().__init__(environment)
        self.base_url = environment.host

    def on_start(self):
        self.client.set_window_size(1536, 920)
        self.client.implicitly_wait(5)
        self.login()

    def login(self):
        self.client.get(f"{self.base_url}/login")
        self.client.find_element(By.ID, "username").send_keys("upr")
        self.client.find_element(By.ID, "password").send_keys("upr")
        self.client.find_element(
            By.XPATH, "//div[@id='root']/form/main/div[2]/div/div[2]/button").click()

    @task
    def view_dashboard(self):
        with self.request(name="Navigate to Dashboard") as request:
            request.client.get(f"{self.base_url}/")

    @task
    def view_resource_details(self):
        with self.request(name="Navigate to Resource Details") as request:
            # resource id could be a random number
            resource_id = random.randint(1, 100)
            request.client.get(f"{self.base_url}/resources/{resource_id}")

    @task
    def view_alerts(self):
        with self.request(name="Navigate to Alerts") as request:
            request.client.get(f"{self.base_url}/alerts")


@events.init.add_listener
def on_locust_init(environment, **kwargs):
    RescheduleTaskOnFail(environment)
