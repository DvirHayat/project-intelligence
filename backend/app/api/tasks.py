"""Task management endpoints."""
from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter()


@router.get("/tasks")
async def get_tasks():
    """Get all tasks."""
    return {"tasks": []}


@router.post("/tasks")
async def create_task(task: dict):
    """Create a new task."""
    return {"id": 1, **task}


@router.get("/tasks/{task_id}")
async def get_task(task_id: int):
    """Get a specific task."""
    return {"id": task_id}


@router.put("/tasks/{task_id}")
async def update_task(task_id: int, task: dict):
    """Update a task."""
    return {"id": task_id, **task}


@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    """Delete a task."""
    return {"deleted": True}
