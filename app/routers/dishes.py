from app.db import get_db
from app.schemas import CreateDish, DishInfo
from app.cache import get_cache, AbstractCache
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from app.routers import service

router = APIRouter()


@router.get("/", response_model=list[DishInfo])
def get_dish(
    target_submenu_id: str,
    db: Session = Depends(get_db),
    cache: AbstractCache = Depends(get_cache),
):
    return service.get_dish(target_submenu_id, db, cache)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=DishInfo)
def create_dish(
    details: CreateDish,
    target_submenu_id: str,
    db: Session = Depends(get_db),
    cache: AbstractCache = Depends(get_cache),
):
    return service.create_dish(details, target_submenu_id, db, cache)


@router.get("/{id}", response_model=DishInfo)
def get_dish_by_id(
    id: str, db: Session = Depends(get_db), cache: AbstractCache = Depends(get_cache)
):
    return service.get_dish_by_id(id, db, cache)


@router.delete("/{id}")
def delete_dish(
    id: str, db: Session = Depends(get_db), cache: AbstractCache = Depends(get_cache)
):
    return service.delete_dish(id, db, cache)


@router.patch("/{id}", response_model=DishInfo)
def update_dish(
    id: str,
    dish: CreateDish,
    db: Session = Depends(get_db),
    cache: AbstractCache = Depends(get_cache),
):
    return service.update_dish(id, dish, db, cache)
