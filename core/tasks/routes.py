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


@router.get("/todos-list", response_model=List[TodoResponseSchema])
async def todos_list(db: Annotated[Session, Depends(get_db)]):
    query = db.query(Todos).all()
    return query