from flask import Flask
from app.models import db
from app.routes import routes
from migrator import run_migrations

app = Flask(__name__)
app.config.from_object("config.Config")

db.init_app(app)
app.register_blueprint(routes)

if __name__ == "__main__":
    run_migrations()
    app.run(debug=True)
