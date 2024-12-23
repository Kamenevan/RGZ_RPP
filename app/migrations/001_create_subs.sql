# Создание таблицы подписок
CREATE TABLE subscriptions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    name VARCHAR(100) NOT NULL,
    amount FLOAT NOT NULL,
    periodicity VARCHAR(50) NOT NULL,
    start_date DATE NOT NULL,
    next_billing_date DATE
);
