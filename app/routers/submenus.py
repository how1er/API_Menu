from app.db import get_db
from app.schemas import CreateSubMenu, SubMenuInfo

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from app.cache import get_cache, AbstractCache
from app.routers import service

router = APIRouter()


@router.get("/", response_model=list[SubMenuInfo])
def get_submenus(
    target_menu_id: str,
    db: Session = Depends(get_db),
    cache: AbstractCache = Depends(get_cache),
):
    return service.get_submenus(target_menu_id, db, cache)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=SubMenuInfo)
def create_submenu(
    details: CreateSubMenu,
    target_menu_id: str,
    db: Session = Depends(get_db),
    cache: AbstractCache = Depends(get_cache),
):
    return service.create_submenu(details, target_menu_id, db, cache)


@router.get("/{id}", response_model=SubMenuInfo)
def get_submenu_by_id(
    id: str, db: Session = Depends(get_db), cache: AbstractCache = Depends(get_cache)
):
    return service.get_submenu_by_id(id, db, cache)


@router.delete("/{id}")
def delete_submenu_by_id(
    id: str, target_menu_id: str, db: Session = Depends(get_db), cache: AbstractCache = Depends(get_cache)
):
    return service.delete_submenu_by_id(id, target_menu_id, db, cache)


@router.patch("/{id}", response_model=SubMenuInfo)
def update_submenu_by_id(
    id: str,
    submenu: CreateSubMenu,
    db: Session = Depends(get_db),
    cache: AbstractCache = Depends(get_cache),
):
    return service.update_submenu_by_id(id, submenu, db, cache)
