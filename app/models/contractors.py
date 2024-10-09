from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from . import db


class Contractor(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    occupation: Mapped[str]
    salary: Mapped[int]
    payout_at: Mapped[datetime]
