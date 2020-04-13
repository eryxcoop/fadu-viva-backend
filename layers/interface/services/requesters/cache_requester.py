from layers.interface.cache.clients import CacheClientFactory
from layers.interface.services.requesters.base import Requester


class CacheRequester:
    def __init__(self, expiration=0) -> None:
        self._requester = Requester()
        self._cache_client = CacheClientFactory().for_actual_environment()
        self._expiration = expiration

    def call(self, url, query_params=None):
        raise NotImplementedError

    def _cache_key(self, url, query_params):
        return f'{url}{query_params}'.replace(' ', '')


class RequesterUpdatingCachedResults(CacheRequester):
    def call(self, url, query_params=None):
        response = self._requester.call(url, query_params)
        self._cache_client.set(key=self._cache_key(url, query_params), value=response, expire=self._expiration)
        return response


class RequesterUsingCachedResults(CacheRequester):
    def call(self, url, query_params=None):
        response = self._cache_client.get(self._cache_key(url, query_params), default=None)
        if response is None:
            response = RequesterUpdatingCachedResults(expiration=self._expiration).call(url, query_params)
        return response
