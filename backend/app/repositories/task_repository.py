"""Task repository for data access."""
from sqlalchemy.orm import Session
from app.models.task import Task, TaskStatus


class TaskRepository:
    """Repository for task operations."""

    def __init__(self, db: Session):
        """Initialize repository with database session."""
        self.db = db

    def get_task(self, task_id: int) -> Task:
        """Get a task by ID."""
        return self.db.query(Task).filter(Task.id == task_id).first()

    def get_all_tasks(self) -> list[Task]:
        """Get all tasks."""
        return self.db.query(Task).all()

    def get_tasks_by_sprint(self, sprint_id: int) -> list[Task]:
        """Get tasks by sprint ID."""
        return self.db.query(Task).filter(Task.sprint_id == sprint_id).all()

    def get_tasks_by_assignee(self, assignee_id: int) -> list[Task]:
        """Get tasks by assignee ID."""
        return self.db.query(Task).filter(Task.assignee_id == assignee_id).all()

    def create_task(self, task_data: dict) -> Task:
        """Create a new task."""
        db_task = Task(**task_data)
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task

    def update_task(self, task_id: int, task_data: dict) -> Task:
        """Update a task."""
        db_task = self.get_task(task_id)
        if db_task:
            for key, value in task_data.items():
                setattr(db_task, key, value)
            self.db.commit()
            self.db.refresh(db_task)
        return db_task

    def delete_task(self, task_id: int) -> bool:
        """Delete a task."""
        db_task = self.get_task(task_id)
        if db_task:
            self.db.delete(db_task)
            self.db.commit()
            return True
        return False
