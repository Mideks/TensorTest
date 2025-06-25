# 🧪 TensorTest

Тестовое задание на позицию разработчика в
тестировании (Программист-тестировщик).

## 📦 Используемые технологии

- Python 3.11+
- Pytest
- Selenium WebDriver
- Page Object Model (POM)

## 🚀 Запуск проекта

### 1. Клонировать репозиторий
```bash
git clone https://github.com/mideks/TensorTest.git
cd TensorTest
````

### 2. Создать виртуальное окружение и активировать его

```bash
python -m venv venv
venv\Scripts\activate  # для Windows
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Запустить тесты

```bash
pytest -v
```

## ⚙️ Структура проекта

```
TensorTest/
├── pages/                     # PageObject-классы для разных страниц
│   ├── main_page.py
│   ├── tensor_page.py
│   ├── contacts_page.py
│   └── downloads_page.py
├── tests/                     # Тестовые сценарии
│   └── test_tensor.py         # Задание 1
│   └── test_location.py       # Задание 2
│   └── test_download          # Задание 3    
├── conftest.py                # Общие для тестов (например, WebDriver)
├── pytest.ini                 # Настройка путей и опций pytest
├── requirements.txt           # Зависимости проекта
├── config.py                  # Некоторые конфигурации для скриптов
├── utils.py                   # Инструменты необходимые для работы тестов (работа с файлами)
├── .gitignore                 # Какие файлы должен игнорировать гит
└── README.md                  # Этот файл
```

## 📝 Примечание
Это мой первый опыт работы с Selenium и написания UI-тестов.  
Я постарался сделать проект максимально понятным и рабочим, хотя в некоторых местах (например, с `sleep`) решение получилось не самым изящным 😅  
Возможно, код можно улучшить с точки зрения надёжности и архитектуры, и я буду рад любым советам или замечаниям.  
Спасибо за понимание!
