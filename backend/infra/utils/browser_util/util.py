from selenium import webdriver


class BrowserUtil:
    def __init__(self) -> None:
        self.__driver = webdriver.Firefox()

    def open_page(self, url: str) -> None:
        self.__driver.get(url=url)

    def close_page(self) -> None:
        self.__driver.close()
