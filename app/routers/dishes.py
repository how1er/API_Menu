from app.models import Dish
from app.db import get_db
from app.schemas import CreateDish, DishInfo


from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status


router = APIRouter()

@router.get("/", response_model=list[DishInfo])
def get_submenu(target_submenu_id: str, db: Session = Depends(get_db)):
    return db.query(Dish).filter(Dish.submenu_id == target_submenu_id).all()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model= DishInfo)
def create_submenu(details: CreateDish, target_submenu_id: str, db: Session = Depends(get_db)):
    to_create = Dish(
        submenu_id = target_submenu_id,
        title=details.title,
        description = details.description,
        price = details.price
    )
    db.add(to_create)
    db.commit()
    return to_create


@router.get("/{id}", response_model=DishInfo)
def get_submenu_by_id(id: str, db: Session = Depends(get_db)):
    stored_dish = db.query(Dish).filter(Dish.id == id).first()
    if not stored_dish:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'dish not found')
    return stored_dish
    


@router.delete("/{id}")
def delete_menu(id: str, db: Session = Depends(get_db)):
    db.query(Dish).filter(Dish.id == id).delete()
    db.commit()
    return { "success": True }

@router.patch("/{id}", response_model=DishInfo)
def update_dish(id: str, dish: CreateDish, db: Session = Depends(get_db)):
    dish_query = db.query(Dish).filter(Dish.id == id)
    stored_dish = dish_query.first()
    if not stored_dish:
        raise HTTPException(status_code=status.HTTP_200_OK,
                            detail=f'No dish with this id: {id} found')
    update_data = dish.dict(exclude_unset=True)
    dish_query.filter(Dish.id == id).update(update_data, synchronize_session=False)
    db.commit()
    db.refresh(stored_dish)
    return stored_dish
