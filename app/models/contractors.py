from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from app.models import db


class Contractor(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    occupation: Mapped[str]
    salary: Mapped[int]
    payout_at: Mapped[datetime]
