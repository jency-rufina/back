from sqlalchemy.orm import Session
import models, schemas

def get_tasks(db: Session):
    return db.query(models.Task).all()

def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int):
    task = db.query(models.Task).get(task_id)
    if task:
        db.delete(task)
        db.commit()
        return {"message": "Deleted successfully"}
    else:
        raise Exception("Task not found")

def update_task(db: Session, task_id: int, task: schemas.TaskCreate):
    db_task = db.query(models.Task).get(task_id)
    if db_task:
        db_task.title = task.title
        db_task.description = task.description
        db.commit()
        return db_task
    else:
        raise Exception("Task not found")
