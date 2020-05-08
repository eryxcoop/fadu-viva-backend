from pymemcache import Client as MemcachedClient

from layers.interface.cache.serde import JSONSerde
from settings import app_config


class CacheClientFactory:
    def for_actual_environment(self):
        return app_config.get_cache_client(self)

    def null_client(self):
        return NullCacheClient()

    def memcached_client(self, server):
        five_seconds = 5
        return MemcachedClient(server=server, serde=JSONSerde(), timeout=five_seconds, connect_timeout=five_seconds)


class NullCacheClient:
    def get(self, key, default=None):
        pass

    def set(self, key, value, expire=None):
        pass
