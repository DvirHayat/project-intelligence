"""Dependency model for task dependencies."""
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.sql import func

from app.core.database import Base


class Dependency(Base):
    """Task dependency model."""

    __tablename__ = "dependencies"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"), index=True)
    depends_on_task_id = Column(Integer, ForeignKey("tasks.id"), index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
