# pw-python-playground

Учебный проект для практики автоматизации тестирования на **Python + Playwright**  
в качестве тренировочной площадки используется [DemoQA](https://demoqa.com/).

## Цели проекта
- Отработка навыков написания автотестов на Python.
- Практика работы с Playwright.

## Стек технологий
- **Python 3.10+**
- **Playwright**
- **Pytest**
- **Allure**

## Структура проекта
- ...

## Установка
1. Клонировать репозиторий:
    ```bash
    git clone https://github.com/Grav3Lord/pw-python-playground.git
    cd pw-python-playground
2. Установить зависимости:
    ```bash
    pip install -r requirements.txt
3. Установить движки браузеров:
    ```bash
    playwright install
   
## Запуск тестов
Все основные параметры уже вынесены в `pytest.ini`, поэтому достаточно запустить:
```bash
pytest
```

## Генерация отчета
```bash
allure serve allure-results
```