from json import loads
from seleniumwire import webdriver
from typing import Dict, Optional


class BrowserUtil:
    def __init__(self, host: str = "localhost", port: str = 5500) -> None:
        self.__driver: Optional[webdriver.Firefox] = None
        self.__prefix = f"http://{host}:{port}/"

    def open_page(self, endpoint: str) -> None:
        if self.__driver is None:
            self.__driver = webdriver.Firefox()

        self.__driver.get(url=f"{self.__prefix}{endpoint}")

    def close_page(self) -> None:
        if self.__driver:
            self.__driver.close()
            self.__driver = None

    def get_request_info(self, endpoint: str) -> Dict:
        if self.__driver is None:
            return {}

        for request in self.__driver.requests:
            if request.response:
                if endpoint in request.url:
                    response_body = request.response.body.decode("utf-8")
                    return loads(response_body)

        return {}
