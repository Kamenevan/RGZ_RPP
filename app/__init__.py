import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Инициализация базы данных
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Конфигурация приложения
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Подключение базы данных
    db.init_app(app)

    # Регистрация маршрутов
    from .routes import routes
    app.register_blueprint(routes)

    return app
