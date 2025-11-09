class Urls:
    BASE_URL = "https://qa-scooter.praktikum-services.ru"
    
    # Courier endpoints
    CREATE_COURIER = "/api/v1/courier"
    LOGIN_COURIER = "/api/v1/courier/login"
    DELETE_COURIER = "/api/v1/courier/{id}"
    
    # Order endpoints
    CREATE_ORDER = "/api/v1/orders"
    GET_ORDERS = "/api/v1/orders"
    CANCEL_ORDER = "/api/v1/orders/cancel"
    
    # Utils endpoints
    PING = "/api/v1/ping"
    SEARCH_STATIONS = "/api/v1/stations/search"