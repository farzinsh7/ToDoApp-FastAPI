from core.database import Base
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import (
    String,
    Integer,
    Text,
    Boolean,
    DateTime,
    func,
    ForeignKey,
)


class Todos(Base):
    __tablename__ = "todos"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    priority: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    is_completed: Mapped[bool] = mapped_column(Boolean, default=False)
    
    created_date: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_date: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), server_onupdate=func.now()
    )
    