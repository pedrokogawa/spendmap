from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime, Numeric, func
from flask_login import UserMixin
from datetime import datetime, date
from decimal import Decimal


class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

class User(UserMixin, db.Model):
  __tablename__ = "users"
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  email: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
  password: Mapped[str] = mapped_column(String(128), nullable=False)
  first_name: Mapped[str] = mapped_column(String(128), nullable=False)
  last_name: Mapped[str] = mapped_column(String(128), nullable=False)
  created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
  updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())


class Expense(UserMixin, db.Model):
  __tablename__="expenses"
  id: Mapped[int] = mapped_column(Integer, primare_key=True)
  amount: Mapped[Decimal] = mapped_column(Numeric(precision=100, scale=2), nullable=False)
  description: Mapped[str] = mapped_column(String(250), nullable=True)
  date: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
