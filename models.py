from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin


class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

class User(UserMixin, db.Model):
  __tablename__ = "users"
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  email: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
  passwrod: Mapped[str] = mapped_column(String(128), nullable=False)
  first_name: Mapped[str] = mapped_column(String(128), nullable=False)
  last_name: Mapped[str] = mapped_column(String(128), nullable=False)