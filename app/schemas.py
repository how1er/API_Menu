from pydantic import BaseModel
import uuid

class CreateMenu(BaseModel):
    title: str
    description: str


class MenuInfo(BaseModel):
    id: uuid.UUID
    title: str
    description: str
    submenus_count: int
    dishes_count: int
 

    class Config:
        orm_mode = True

class CreateSubMenu(BaseModel):
    title: str
    description: str


class SubMenuInfo(BaseModel):
    id: uuid.UUID
    title: str
    description: str
    dishes_count: int
 

    class Config:
        orm_mode = True



class CreateDish(BaseModel):
    title: str
    description: str
    price: str


class DishInfo(BaseModel):
    id: uuid.UUID
    title: str
    description: str
    price: str
 

    class Config:
        orm_mode = True
