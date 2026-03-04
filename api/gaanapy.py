import aiohttp
from api.songs.songs import Songs
from api.albums.albums import Albums
from api.artists.artists import Artists
from api.trending.trending import Trending
from api.newreleases.newreleases import NewReleases
from api.charts.charts import Charts
from api.playlists.playlists import Playlists
from api import endpoints
from api.functions import Functions
from api.errors import Errors

class GaanaPy(Songs, Albums, Artists, Trending, NewReleases, Charts, Playlists):
    def __init__(self):
        # We set this to None initially so Vercel doesn't crash on startup!
        self._aiohttp = None 
        self.api_endpoints = endpoints
        self.functions = Functions()
        self.errors = Errors()
        self.info = False
        
    # This automatically creates the session ONLY when an endpoint is actually called
    @property
    def aiohttp(self):
        if self._aiohttp is None:
            self._aiohttp = aiohttp.ClientSession()
        return self._aiohttp

    def __await__(self):
        return self.async_init().__await__()
