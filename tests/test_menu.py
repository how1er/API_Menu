import json


from app.models import Menu


class TestMenu:
    def test_create_menu(self, client, menu):
        resp = client.post("/api/v1/menus/", data=json.dumps(menu))
        resp_data = resp.json()
        assert resp.status_code == 201
        assert resp_data["title"] == menu["title"]
        assert resp_data["description"] == menu["description"]
        assert resp_data["submenus_count"] == 0
        assert resp_data["dishes_count"] == 0

    def test_get_menu(self, client, create_menu_list):
        resp = client.get("/api/v1/menus/")
        assert len(resp.json()) == 3

    def test_get_menu_by_id(self, client, menu, create_menu, db):
        create_menu(db, menu)
        last_menu = db.query(Menu).first()
        menu_id = str(last_menu.id)
        resp = client.get(f"/api/v1/menus/{menu_id}")
        assert resp.status_code == 200
        resp_data = resp.json()
        assert resp_data["id"] == menu_id
        assert resp_data["title"] == menu["title"]
        assert resp_data["description"] == menu["description"]
        assert resp_data["submenus_count"] == 0
        assert resp_data["dishes_count"] == 0

    def test_update_menu(self, client, menu, create_menu, db):
        new_data = {"title": "Updated title",
                    "description": "Updated description"}
        create_menu(db, menu)
        last_menu = db.query(Menu).first()
        menu_id = str(last_menu.id)
        resp = client.patch(
            f"/api/v1/menus/{menu_id}", data=json.dumps(new_data))
        resp_data = resp.json()
        assert resp_data["id"] == menu_id
        assert resp_data["title"] == new_data["title"]
        assert resp_data["description"] == new_data["description"]
        assert resp_data["submenus_count"] == 0
        assert resp_data["dishes_count"] == 0

    def test_delete_menu(self, client, create_menu, menu, db):
        create_menu(db, menu)
        last_menu = db.query(Menu).first()
        menu_id = str(last_menu.id)
        resp = client.delete(f"/api/v1/menus/{menu_id}")
        assert resp.status_code == 200
        resp_data = resp.json()
        assert resp_data["success"] is True
