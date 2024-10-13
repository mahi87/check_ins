from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from . import db
from .user import User


class Contractor(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id), index=True)
    name: Mapped[str] = mapped_column(nullable=False)
    occupation: Mapped[str]
    salary: Mapped[int]
    payout_at: Mapped[datetime]
