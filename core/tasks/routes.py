from fastapi import APIRouter, Path, Depends, HTTPException, Query, status
from fastapi.responses import JSONResponse
from typing import List, Annotated
from sqlalchemy.orm import Session
from core.database import get_db
from tasks.schemas import (
    TodoCreateSchema,
    TodoResponseSchema,
    TodoUpdateSchema,
)
from tasks.models import Todos


router = APIRouter(tags=["Todos"])


@router.get("/todos", response_model=List[TodoResponseSchema])
async def todos_list(db: Annotated[Session, Depends(get_db)]):
    query = db.query(Todos).all()
    return query



@router.post("/todos")
async def create_todo(request: TodoCreateSchema, db: Annotated[Session, Depends(get_db)]):
    todo_obj = Todos(**request.model_dump())
    
    db.add(todo_obj)
    db.commit()
    db.refresh(todo_obj)
 
    return todo_obj



@router.get("/todos/{todo_id}")
async def retrieve_todo_by_id(
    db: Annotated[Session, Depends(get_db)],
    todo_id: int = Path(..., gt=0), 
    ):
    todo_obj = db.query(Todos).filter_by(id= todo_id).first()
    
    if todo_obj:
        return todo_obj
    





