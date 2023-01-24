from app.models import Dish
from app.db import get_db
from app.schemas import CreateDish, DishInfo

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from app.routers import crud

router = APIRouter()

@router.get("/", response_model=list[DishInfo])
def get_dish(target_submenu_id: str, db: Session = Depends(get_db)):
    return crud.get_dish(target_submenu_id, db)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model= DishInfo)
def create_dish(details: CreateDish, target_submenu_id: str, db: Session = Depends(get_db)):
    return crud.create_dish(details, target_submenu_id, db)


@router.get("/{id}", response_model=DishInfo)
def get_dish_by_id(id: str, db: Session = Depends(get_db)):
    return crud.get_dish_by_id(id, db)
    

@router.delete("/{id}")
def delete_dish(id: str, db: Session = Depends(get_db)):
    return crud.delete_dish(id, db)


@router.patch("/{id}", response_model=DishInfo)
def update_dish(id: str, dish: CreateDish, db: Session = Depends(get_db)):
    return crud.update_dish(id, dish, db)
