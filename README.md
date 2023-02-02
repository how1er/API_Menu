## Задача

<p>Написать проект на FastAPI с использованием PostgreSQL в качестве БД</p>

## Описание
<ul>
В проекте следует реализовать REST API по работе с меню ресторана, все CRUD операции.<br />
Даны 3 сущности: Меню, Подменю, Блюдо.<br />
Зависимости:

<li>У меню есть подменю, которые к ней привязаны</li>
<li>У подменю есть блюда</li>
Условия:
<li>Блюдо не может быть привязано напрямую к меню, минуя подменю.</li>
<li>Блюдо не может находиться в 2-х подменю одновременно.</li>
<li>Подменю не может находиться в 2-х меню одновременно.</li>
<li>Если удалить меню, должны удалиться все подменю и блюда этого меню.</li>
<li>Если удалить подменю, должны удалиться все блюда этого подменю.</li>
<li>Цены блюд выводить с округлением до 2 знаков после запятой.</li>
<li>Во время выдачи списка меню, для каждого меню добавлять кол-во подменю и блюд в этом меню.</li>
<li>Во время выдачи списка подменю, для каждого подменю добавлять кол-во блюд в этом подменю.</li>
<li>Во время запуска тестового сценария БД должна быть пуста.</li>
</ul>




## Установка и запуск


## С помощью Docker

````
docker-compose build
docker compose up
````

## Запуск тестов

````
docker-compose -f docker-compose-test.yaml up --build
````
## Без Docker

1. Склонировать репозиторий с Github:

````
git clone https://github.com/how1er/API_Menu
````
2. Перейти в директорию проекта

3. Создать виртуальное окружение:

````
python -m venv venv
````

4. Активировать окружение:

````
source venv\scripts\activate
````
5. В файле .evn заполнить необходимые данные

6. Установка зависимостей:

```
pip install -r requirements.txt
```

7. Запустить миграции БД:
```
alembic upgrade head
```
8. Запустить API с помощью uvicorn
```
cd app
uvicorn main:app --reload
```

***


# API
----------
## Requests:
````
Get all menus          `/api/v1/menus/`    
Create menu            `/api/v1/menus/` 
Get menu by id         `/api/v1/menus/{menu_id}`
Delete menu by id      `/api/v1/menus/{menu_id}`  
Update menu by id      `/api/v1/menus/{menu_id}`                                         
Get all submenus       `/api/v1/menus/{menu_id}/submenus`                                   
Create submenu         `/api/v1/menus/{menu_id}/submenus`                                    
Get submenu by id      `/api/v1/menus/{menu_id}/submenus/{submenu_id}`        
Delete submenu by id   `/api/v1/menus/{menu_id}/submenus/{submenu_id}`                 
Update submenu by id   `/api/v1/menus/{menu_id}/submenus/{submenu_id}`                     
Get all dishes         `/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes` 
Create dish            `/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes`                 
Get dish by id         `/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}` 
Delete dish by id      `/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}`    
Update dish by id      `/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}`    
````
----------

Документация для API доступна по адресу:

```http://127.0.0.1:8000/docs```
