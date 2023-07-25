from sqlalchemy.types import  String, Numeric
from sqlalchemy.sql.schema import Column
from app.db  import Base

import uuid
from sqlalchemy import TIMESTAMP, Column, ForeignKey, String, Boolean, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property




class Menu(Base):
    __tablename__ = 'menus'
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False,
                default=uuid.uuid4)
    title = Column(String,  nullable=False)
    description = Column(String,  nullable=False)
    submenus = relationship('SubMenu', back_populates="menu")
    
    @hybrid_property
    def submenus_count(self):
        return len(self.submenus)
    
    @hybrid_property
    def dishes_count(self):
        count = 0
        for submenu in self.submenus:
            count = count+len(submenu.dishes)
        return count


class SubMenu(Base):
    __tablename__ = 'submenus'
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False,
                default=uuid.uuid4)
    menu_id = Column(UUID(as_uuid=True), ForeignKey(
        'menus.id', ondelete='CASCADE'), nullable=False)
    title = Column(String,  nullable=False)  
    description = Column(String,  nullable=False)
    menu = relationship("Menu", back_populates = "submenus")
    dishes = relationship("Dish", back_populates = "submenu")

    @hybrid_property
    def dishes_count(self):
        return len(self.dishes)

class Dish(Base):
    __tablename__ = 'dishes'
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False,
                default=uuid.uuid4)
    submenu_id = Column(UUID(as_uuid=True), ForeignKey(
        'submenus.id', ondelete='CASCADE'), nullable=False)
    title = Column(String,  nullable=False)  
    description = Column(String,  nullable=False) 
    price = Column(String,  nullable=False)
    submenu = relationship("SubMenu", back_populates = "dishes")
