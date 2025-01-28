from json import loads
from seleniumwire import webdriver
from typing import Dict


class BrowserUtil:
    def __init__(self, host: str = "localhost", port: str = 5500) -> None:
        self.__driver = webdriver.Firefox()
        self.__prefix = f"http://{host}:{port}/"

    def open_page(self, endpoint: str) -> None:
        self.__driver.get(url=f"{self.__prefix}{endpoint}")

    def close_page(self) -> None:
        self.__driver.close()

    def get_request_info(self, endpoint: str) -> Dict:
        for request in self.__driver.requests:
            if request.response:
                if endpoint in request.url:
                    response_body = request.response.body.decode("utf-8")
                    return loads(response_body)

        return {}
