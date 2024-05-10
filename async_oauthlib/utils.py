import aiohttp


class BasicAuth(aiohttp.BasicAuth):

    def __new__(cls, login, client_secret, **kwargs):
        return super(BasicAuth, cls).__new__(cls, str(login), str(client_secret), **kwargs)
