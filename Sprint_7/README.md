# Sprint 7: Автоматизированные тесты API для сервиса Scooter

# Протестированные API эндпоинты

- API Курьеров:
  - Создание курьера (`POST /api/v1/courier`)
  - Логин курьера (`POST /api/v1/courier/login`) 
  - Удаление курьера (`DELETE /api/v1/courier/:id`)

- API Заказов:
  - Создание заказа (`POST /api/v1/orders`)
  - Получение списка заказов (`GET /api/v1/orders`)
  - Получение заказа по трек-номеру (`GET /api/v1/orders/track`)
  - Принятие заказа (`PUT /api/v1/orders/accept/:id`)
  - Отмена заказа (`PUT /api/v1/orders/cancel`)
  - Завершение заказа (`PUT /api/v1/orders/finish/:id`)

- Вспомогательные API:
  - Пинг сервера (`GET /api/v1/ping`)
  - Поиск станций (`GET /api/v1/stations/search`)