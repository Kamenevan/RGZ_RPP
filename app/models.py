from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)

class Subscription(db.Model):
    __tablename__ = 'subscriptions'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    periodicity = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    next_billing_date = db.Column(db.Date)

class MigrationLog(db.Model):
    __tablename__ = 'migrations_log'
    id = db.Column(db.Integer, primary_key=True)
    migration_id = db.Column(db.Integer, nullable=False, unique=True)
    file_path = db.Column(db.String(255), nullable=False)
