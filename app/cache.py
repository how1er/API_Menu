from redis.client import Redis
from abc import ABC, abstractmethod


class AbstractCache(ABC):
    def __init__(self, cache_instance):
        self.cache: dict | Redis = cache_instance

    @abstractmethod
    def get(self, key: str):
        pass

    @abstractmethod
    def set(
        self,
        key: str,
        value: bytes | str,
        expire: int = 600,
    ):
        pass

    @abstractmethod
    def remove(self, key: str):
        pass

    @abstractmethod
    def close(self):
        pass


class RedisCache(AbstractCache):
    def get(self, key: str):
        item = self.cache.get(key)
        return item

    def set(
        self,
        key: str,
        value: bytes | str,
        expire: int = 600,
    ):
        self.cache.set(name=key, value=value, ex=expire)

    def remove(self, key: str):
        self.cache.delete(key)

    def close(self):
        self.cache.close()


cache: AbstractCache | None = None


def get_cache() -> AbstractCache:
    return RedisCache(cache)
