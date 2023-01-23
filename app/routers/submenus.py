
from app.models import SubMenu
from app.db import get_db
from app.schemas import CreateSubMenu, SubMenuInfo

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status



router = APIRouter()

@router.get("/", response_model=list[SubMenuInfo])
def get_submenu(target_menu_id: str, db: Session = Depends(get_db)):
    return db.query(SubMenu).filter(SubMenu.menu_id == target_menu_id).all()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model= SubMenuInfo)
def create_submenu(details: CreateSubMenu, target_menu_id: str, db: Session = Depends(get_db)):
    to_create = SubMenu(
        menu_id = target_menu_id,
        title=details.title,
        description = details.description
    )
    db.add(to_create)
    db.commit()
    return to_create



@router.get("/{id}", response_model=SubMenuInfo)
def get_submenu_by_id(id: str, db: Session = Depends(get_db)):
    stored_submenu = db.query(SubMenu).filter(SubMenu.id == id).first()
    if not stored_submenu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'submenu not found')
    return stored_submenu

    


@router.delete("/{id}")
def delete_menu(id: str, db: Session = Depends(get_db)):
    db.query(SubMenu).filter(SubMenu.id == id).delete()
    db.commit()
    return { "success": True }

@router.patch("/{id}")
def update_submenu(id: str, menu: CreateSubMenu, db: Session = Depends(get_db)):
    menu_query = db.query(SubMenu).filter(SubMenu.id == id)
    stored_submenu = menu_query.first()
    if not stored_submenu:
        raise HTTPException(status_code=status.HTTP_200_OK,
                            detail=f'No submenu with this id: {id} found')
    update_data = menu.dict(exclude_unset=True)
    menu_query.filter(SubMenu.id == id).update(update_data, synchronize_session=False)
    db.commit()
    db.refresh(stored_submenu)
    return stored_submenu





