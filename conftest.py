# Управление фикстурами
import pytest
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    """
    Добавляет пользовательские опции sh для запуска тестов с Playwright.
    :param parser: Объект парсера Pytest, используемый для регистрации новых опций.

    Опции:
        --browser (str): выбор браузера для запуска тестов. Доступные значения:
            - chromium (по умолчанию)
            - firefox
            - webkit
        --headed (flag): запуск браузера в headed-режиме (с графическим интерфейсом).
                         По умолчанию браузер запускается headless.
    """
    parser.addoption("--browser", action="store", default="chromium",
                     help="Browser: chromium, firefox, webkit")
    parser.addoption("--headed", action="store_true",
                     help="Run browser in headed mode")


@pytest.fixture(scope="function")
def page(request):
    """
    Создаёт экземпляр браузера Playwright, открывает новый контекст и страницу
    для выполнения тестов. Настройки браузера и режима запуска (headed/headless)
    берутся из параметров командной строки Pytest.

    После завершения теста автоматически закрывает контекст и браузер.
    """
    browser_name = request.config.getoption("--browser")
    headed = request.config.getoption("--headed")
    headless = not headed

    with sync_playwright() as p:
        browser = getattr(p, browser_name).launch(headless=headless)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()
