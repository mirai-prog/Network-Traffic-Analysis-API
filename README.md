# Network-Traffic-Analysis-API

### 1. **Project Description**

A FastAPI application that allows uploading network traffic dumps (e.g., PCAP files), analyzes them, and provides information about:

- Suspicious IP addresses.
- Protocols in use.
- Potential threats.

---

### 2. **Main Features**

1. **File Upload**:
   - Endpoint for uploading PCAP files.
   - File size limit and format validation.
2. **Traffic Analysis**:
   - Uses the Scapy library for packet analysis.
   - Visualizes data on protocol types and packet counts.
3. **Reports**:
   - Endpoint to retrieve a JSON report with analysis results.
   - Information on suspicious IPs, unusual packets, and recommendations.
4. **Real-Time Analysis (Optional)**:
   - Enables live logging for real-time packet monitoring (via WebSocket).

---

### 3. **Technology Stack**

- **FastAPI**: API implementation.
- **Scapy**: Network traffic analysis.
- **SQLAlchemy**: Stores upload and analysis history in the database.
- **Redis (optional)**: Caching requests and temporary data.
- **Uvicorn**: Runs the application.
- **Plotly/Dash**: Visualization (can embed graphs in the frontend).

---

### 4. **Project Structure**

#### **4.1. Overall Project Structure**
```plaintext
project/
├── app/                      # Core application logic
│   ├── main.py               # Application entry point
│   ├── routers/              # API routes
│   │   ├── __init__.py
│   │   ├── upload.py         # File upload endpoint
│   │   ├── analysis.py       # File analysis endpoint
│   │   ├── reports.py        # Report generation endpoint
│   ├── services/             # Business logic
│   │   ├── __init__.py
│   │   ├── file_service.py   # File operations (saving, validation)
│   │   ├── analysis_service.py # Packet analysis
│   │   ├── report_service.py # Report generation
│   ├── models.py             # Database models
│   ├── schemas.py            # Pydantic schemas for requests and responses
│   ├── config.py             # Application configuration
│   ├── utils.py              # Utilities (common functions)
├── tests/                    # Application tests
│   ├── __init__.py
│   ├── test_upload.py        # File upload tests
│   ├── test_analysis.py      # Traffic analysis tests
│   ├── test_reports.py       # Report tests
├── data/                     # Test data (e.g., sample PCAP files)
│   ├── sample.pcap
├── requirements.txt          # Dependency list
├── README.md                 # Project documentation
├── Dockerfile                # Docker configuration
├── .env                      # Environment variables
```

---

#### **4.2. Main Modules**
1. **`main.py`**  
   - Entry point for the application.  
   - Configures the FastAPI app, routes, database, and middlewares.  

2. **Routers (`routers/`)**  
   - Each functional block has its own router.  
   - **`upload.py`**: Handles file uploads (POST /upload).  
   - **`analysis.py`**: Runs file analysis (GET /analysis/{file_id}).  
   - **`reports.py`**: Generates reports (GET /reports/{file_id}).  

3. **Services (`services/`)**  
   - Implements business logic:  
     - **`file_service.py`**: Validates uploaded files, saves, and deletes them.  
     - **`analysis_service.py`**: Analyzes traffic using Scapy.  
     - **`report_service.py`**: Generates JSON reports and graphs.  

4. **Models (`models.py`)**  
   - SQLAlchemy models for the database:  
     - Stores information about uploaded files.  
     - Tracks requests and analysis history.  

5. **Schemas (`schemas.py`)**  
   - Defines input and output data using Pydantic:  
     - Requests (e.g., file upload).  
     - Responses (e.g., analysis results).  

6. **Configuration (`config.py`)**  
   - Stores all application settings:  
     - File storage paths.  
     - Database settings.  
     - Secret keys (loaded from `.env`).  

---

#### **4.3. Technology Stack**
- **FastAPI**: Core application.  
- **SQLAlchemy/SQLite**: Data storage for files and reports.  
- **Scapy**: Network traffic analysis.  
- **Plotly**: Data visualization.  
- **Redis (optional)**: Request and temporary data caching.  
- **Pytest**: For writing tests.  

---

#### **4.4. Module Interaction Example**
1. A user uploads a PCAP file through the `/upload` endpoint.
   - The file is validated in `file_service.py` and saved to disk.  
   - A record of the file is stored in the database.  

2. The user requests file analysis through `/analysis/{file_id}`.  
   - The file is retrieved from storage.  
   - `analysis_service.py` uses Scapy to parse the packets.  
   - Analysis results are saved in the database.  

3. The user requests a report through `/reports/{file_id}`.  
   - `report_service.py` generates a JSON response with the data.  
   - Visualization (if needed) is added using Plotly.  

---

### 5. **Development Stages**

1. **Set Up FastAPI Project**:
   - Create the base server.
   - Add routing and structure.
2. **Implement File Upload**:
   - Develop an endpoint for file uploads.
   - Store files temporarily or in the database.
3. **Analyze Network Traffic**:
   - Use Scapy to parse PCAP files.
   - Extract information on IPs, protocols, and anomalies.
4. **Generate Reports**:
   - Create a JSON schema for returning results.
   - Add data visualization (e.g., protocol distribution charts).
5. **Testing and Optimization**:
   - Write API tests.
   - Optimize large file processing.

---

### 6. **API Examples**

- **POST /upload**: Upload a PCAP file.
- **GET /report/{file_id}**: Retrieve a JSON report.
- **GET /stats**: Retrieve general statistics.

---

### **Key Objectives of Network Traffic Analysis**

1. **Monitor Network Performance**:
   - Examine the types of transmitted data (HTTP, DNS, FTP, etc.).
   - Assess traffic volumes and data transfer speeds.
2. **Detect Security Threats**:
   - Identify suspicious IP addresses that may be sources of attacks.
   - Analyze anomalous patterns, such as DDoS attacks, port scans, or malware injections.
3. **Troubleshoot Network Issues**:
   - Locate configuration errors.
   - Identify devices causing load or failures.
4. **Gather Information for Investigations**:
   - Log traffic for incident investigations.
   - Analyze event chronology during network attacks.

# Network-Traffic-Analysis-API RUS version

### 1. **Описание проекта**

FastAPI-приложение, которое позволяет загружать дампы сетевого трафика (например, PCAP-файлы), анализирует их и возвращает информацию о:

- Подозрительных IP-адресах.
- Используемых протоколах.
- Потенциальных угрозах.

### 2. **Основные функции**

1. **Загрузка файлов**:
    
    - Эндпоинт для загрузки PCAP-файла.
    - Ограничение на размер файла и проверка формата.
2. **Анализ трафика**:
    
    - Использование библиотеки Scapy для анализа пакетов.
    - Визуализация данных о типах протоколов и количестве пакетов.
3. **Отчеты**:
    
    - Эндпоинт для получения JSON-отчета с результатами анализа.
    - Информация о подозрительных IP, странных пакетах и рекомендациях.
4. **Реальное время (опционально)**:
    
    - Возможность подключить live-логирование для мониторинга пакетов в реальном времени (через WebSocket).

---

### 3. **Технологический стек**

- **FastAPI**: реализация API.
- **Scapy**: анализ сетевого трафика.
- **SQLAlchemy**: сохранение истории загрузок и анализа в базу данных.
- **Redis (опционально)**: кэширование запросов и временных данных.
- **Uvicorn**: запуск приложения.
- **Plotly/Dash**: визуализация (можно встроить графики через фронт).

---

### 4. **Структура проекта**

### **4.1. Общая структура проекта**
```plaintext
project/
├── app/                      # Основная логика приложения
│   ├── main.py               # Точка входа в приложение
│   ├── routers/              # Маршруты API
│   │   ├── __init__.py
│   │   ├── upload.py         # Эндпоинт загрузки файлов
│   │   ├── analysis.py       # Эндпоинт анализа файлов
│   │   ├── reports.py        # Эндпоинт генерации отчетов
│   ├── services/             # Бизнес-логика
│   │   ├── __init__.py
│   │   ├── file_service.py   # Работа с файлами (сохранение, валидация)
│   │   ├── analysis_service.py # Анализ пакетов
│   │   ├── report_service.py # Генерация отчетов
│   ├── models.py             # Модели базы данных
│   ├── schemas.py            # Pydantic-схемы для запросов и ответов
│   ├── config.py             # Настройки приложения
│   ├── utils.py              # Утилиты (общие функции)
├── tests/                    # Тесты для приложения
│   ├── __init__.py
│   ├── test_upload.py        # Тесты загрузки файлов
│   ├── test_analysis.py      # Тесты анализа трафика
│   ├── test_reports.py       # Тесты отчетов
├── data/                     # Данные для тестов (например, примеры PCAP)
│   ├── sample.pcap
├── requirements.txt          # Список зависимостей
├── README.md                 # Документация проекта
├── Dockerfile                # Конфигурация Docker
├── .env                      # Переменные окружения
```

---

### **4.2. Основные модули**
1. **`main.py`**  
   - Точка входа в приложение.  
   - Настройка FastAPI-приложения, подключение роутеров, базы данных и middlewares.  

2. **Роутеры (`routers/`)**  
   - Каждый функциональный блок имеет отдельный роутер.  
   - **`upload.py`**: обработка загрузки файлов (POST /upload).  
   - **`analysis.py`**: запуск анализа файлов (GET /analysis/{file_id}).  
   - **`reports.py`**: генерация отчетов (GET /reports/{file_id}).  

3. **Сервисы (`services/`)**  
   - Реализация всей бизнес-логики:  
     - **`file_service.py`**: проверка загружаемых файлов, сохранение и удаление.  
     - **`analysis_service.py`**: анализ трафика с использованием Scapy.  
     - **`report_service.py`**: формирование JSON-отчетов и графиков.

4. **Модели (`models.py`)**  
   - SQLAlchemy-модели для базы данных:  
     - Сохранение информации о загруженных файлах.  
     - История запросов и анализа.  

5. **Схемы (`schemas.py`)**  
   - Описание входных и выходных данных с помощью Pydantic:  
     - Запросы (например, загрузка файла).  
     - Ответы (например, результаты анализа).  

6. **Конфигурация (`config.py`)**  
   - Хранение всех настроек приложения:  
     - Путь к хранилищу файлов.  
     - Настройки базы данных.  
     - Секретные ключи (считываются из `.env`).  

---

### **4.3. Технологический стек**
- **FastAPI**: Основное приложение.  
- **SQLAlchemy/SQLite**: Для хранения данных о файлах и отчетах.  
- **Scapy**: Для анализа сетевого трафика.  
- **Plotly**: Для визуализации данных.  
- **Redis (опционально)**: Кэширование запросов и временных данных.  
- **Pytest**: Для написания тестов.  

---

### **4.4. Пример взаимодействия модулей**
1. Пользователь загружает PCAP-файл через эндпоинт `/upload`.
   - Файл проверяется в `file_service.py` и сохраняется на диск.  
   - Запись о файле сохраняется в базу данных.  

2. Пользователь запрашивает анализ файла через `/analysis/{file_id}`.  
   - Файл извлекается из хранилища.  
   - `analysis_service.py` запускает Scapy для разбора пакетов.  
   - Результаты анализа сохраняются в базу данных.

3. Пользователь запрашивает отчет через `/reports/{file_id}`.  
   - `report_service.py` формирует JSON-ответ с данными.  
   - Визуализация (если требуется) добавляется через Plotly.  

---

### 5. **Этапы разработки**

1. **Настройка FastAPI-проекта**:
    
    - Создать базовый сервер.
    - Добавить роутинг и структуру.
2. **Реализация загрузки файлов**:
    
    - Эндпоинт для загрузки файла.
    - Хранение файлов временно или в базе данных.
3. **Анализ сетевого трафика**:
    
    - Использование Scapy для разбора PCAP.
    - Создать функции для выделения IP, протоколов и аномалий.
4. **Генерация отчетов**:
    
    - Создать JSON-схему для возвращения результатов.
    - Добавить визуализацию данных (например, распределение протоколов).
5. **Тестирование и оптимизация**:
    
    - Написать тесты для API.
    - Оптимизировать обработку больших файлов.

---

### 6. **Пример API**

- **POST /upload**: загрузка PCAP-файла.
- **GET /report/{file_id}**: получить JSON-отчет.
- **GET /stats**: получить общую статистику.

---

### **Основные цели анализа сетевого трафика:**

1. **Мониторинг производительности сети**:
    
    - Изучение типов передаваемых данных (HTTP, DNS, FTP и т. д.).
    - Оценка объемов трафика и скорости передачи данных.
2. **Обнаружение угроз безопасности**:
    
    - Выявление подозрительных IP-адресов, которые могут быть источниками атак.
    - Анализ аномальных паттернов, таких как DDoS-атаки, попытки сканирования портов или внедрения вредоносного кода.
3. **Отладка сетевых проблем**:
    
    - Поиск ошибок в конфигурации сети.
    - Определение устройств, вызывающих нагрузку или сбои.
4. **Сбор информации для расследования**:
    
    - Логирование трафика помогает исследовать инциденты.
    - Анализ хронологии событий в случае сетевых атак.
