from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from datetime import date
from flask_login import login_user, LoginManager, current_user, logout_user
from dotenv import load_dotenv
from models import User, db
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import os


load_dotenv()
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
Bootstrap5(app)


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI", "sqlite:///spendmap.db")
db.init_app(app)


# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)


with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
  return db.get_or_404(User, user_id)


@app.route("/")
def home():
  return render_template("index.html")


if __name__ == "__main__":
  app.run(debug=True)