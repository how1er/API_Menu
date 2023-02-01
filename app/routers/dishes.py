from app.db import get_db
from app.schemas import CreateDish, DishInfo
from app.cache import get_cache, AbstractCache
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from app.routers import service

router = APIRouter()


@router.get("/", response_model=list[DishInfo])
def get_dishes(
    target_submenu_id: str,
    db: Session = Depends(get_db),
    cache: AbstractCache = Depends(get_cache),
):
    return service.get_dishes(target_submenu_id, db, cache)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=DishInfo)
def create_dish(
    details: CreateDish,
    target_submenu_id: str,
    target_menu_id: str,
    db: Session = Depends(get_db),
    cache: AbstractCache = Depends(get_cache),
):
    return service.create_dish(details, target_submenu_id, target_menu_id, db, cache)


@router.get("/{id}", response_model=DishInfo)
def get_dish_by_id(
    id: str, db: Session = Depends(get_db), cache: AbstractCache = Depends(get_cache)
):
    return service.get_dish_by_id(id, db, cache)


@router.delete("/{id}")
def delete_dish_by_id(
    id: str, target_submenu_id: str, target_menu_id: str, db: Session = Depends(get_db), cache: AbstractCache = Depends(get_cache)
):
    return service.delete_dish_by_id(id, target_submenu_id, target_menu_id, db, cache)


@router.patch("/{id}", response_model=DishInfo)
def update_dish_by_id(
    id: str,
    dish: CreateDish,
    db: Session = Depends(get_db),
    cache: AbstractCache = Depends(get_cache),
):
    return service.update_dish_by_id(id, dish, db, cache)
