from redis.client import Redis
from abc import ABC, abstractmethod

from typing import Union


class AbstractCache(ABC):
    def __init__(self, cache_instance):
        self.cache: Union[dict, Redis] = cache_instance

    @abstractmethod
    def get(self, key: str):
        pass

    @abstractmethod
    def set(
        self,
        key: str,
        value: Union[bytes, str],
        expire: int = 30,
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
        value: Union[bytes, str],
        expire: int = 30,
    ):
        self.cache.set(name=key, value=value, ex=expire)

    async def remove(self, key: str):
        self.cache.delete(key)

    async def close(self):
        self.cache.close()


cache: Union[AbstractCache, None] = None


async def get_cache() -> AbstractCache:
    return RedisCache(cache)
