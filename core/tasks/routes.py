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


@router.get("/todos", response_model=List[TodoResponseSchema], status_code=status.HTTP_200_OK)
async def todos_list(db: Annotated[Session, Depends(get_db)]):
    query = db.query(Todos).all()
    return query


@router.post("/todos", status_code=status.HTTP_201_CREATED)
async def create_todo(request: TodoCreateSchema, db: Annotated[Session, Depends(get_db)]):
    todo_obj = Todos(**request.model_dump())
    
    db.add(todo_obj)
    db.commit()
    db.refresh(todo_obj)
 
    return todo_obj


@router.get("/todos/{todo_id}", status_code=status.HTTP_200_OK)
async def retrieve_todo_by_id(
    db: Annotated[Session, Depends(get_db)],
    todo_id: int = Path(..., gt=0), 
    ):
    todo_obj = db.query(Todos).filter(Todos.id == todo_id).first()
    
    if not todo_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found."
        )
        
    return todo_obj



@router.put("/todos/{todo_id}")
async def update_todo(
    db: Annotated[Session, Depends(get_db)],
    request: TodoUpdateSchema,
    todo_id: int = Path(..., gt=0)
):
    todo_obj = db.query(Todos).filter(Todos.id == todo_id).first()

    if not todo_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found."
        )

    for field, value in request.model_dump(exclude_unset=True).items():
        setattr(todo_obj, field, value)

    db.commit()
    db.refresh(todo_obj)

    return todo_obj


@router.delete("/todos/{todo_id}")
async def delete_todo(
    db: Annotated[Session, Depends(get_db)],
    todo_id: int = Path(..., gt=0)
):
    todo_obj = db.query(Todos).filter(Todos.id == todo_id).first()
    
    if not todo_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found."
        )
    
    db.delete(todo_obj)
    db.commit()
    
    return JSONResponse(
        content={"detail": "Todo deleted successfully."},
        status_code=status.HTTP_204_NO_CONTENT,
    )