from app.schemas import MenuInfo, CreateMenu
from app.models import Menu
from app.db import get_db
from app.cache import get_cache, AbstractCache
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from app.routers import service

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[MenuInfo])
def get_menu(db: Session = Depends(get_db), cache: AbstractCache = Depends(get_cache)):
    return service.get_menu(db, cache)


@router.get("/{id}", response_model=MenuInfo)
def get_menu_by_id(
    id: str, db: Session = Depends(get_db), cache: AbstractCache = Depends(get_cache)
):
    return service.get_menu_by_id(id, db, cache)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=MenuInfo)
def create_menu(
    details: CreateMenu,
    db: Session = Depends(get_db),
    cache: AbstractCache = Depends(get_cache),
):
    return service.create_menu(details, db, cache)


@router.delete("/{id}")
def delete_menu(
    id: str, db: Session = Depends(get_db), cache: AbstractCache = Depends(get_cache)
):
    return service.delete_menu(id, db, cache)


@router.patch("/{id}", response_model=MenuInfo)
def update_menu(
    id: str,
    menu: CreateMenu,
    db: Session = Depends(get_db),
    cache: AbstractCache = Depends(get_cache),
):
    return service.update_menu(id, menu, db, cache)


@router.delete("/")
def delete_menu(db: Session = Depends(get_db)):
    db.query(Menu).delete()
    db.commit()
    return {"success": True}
