import json
from app.cache import AbstractCache


def set_item(cache: AbstractCache, type_: str, item: dict) -> None:
    item_id = item["id"]
    key = f"{type_}:{item_id}"
    cache.set(key, json.dumps(item))


def get_item(cache: AbstractCache, type_: str, id_: str) -> dict | None:
    key = f"{type_}:{id_}"
    item = cache.get(key)
    return json.loads(item) if item else None


def set_list(cache: AbstractCache, key: str, items: list):
    cache.set(key, json.dumps(items))


def get_list(cache: AbstractCache, key: str) -> list | None:
    items = cache.get(key)
    return json.loads(items) if items else None


def delete(cache: AbstractCache, type_: str, id_: str):
    cache.remove(f"{type_}:{id_}")


def delete_list(cache: AbstractCache, key: str):
    cache.remove(key)
