import requests_async as requests
import asyncio
import pause

class NameSniper:

    def __init__(self, dropTime, proxies= None):

        # Request info
        self.nameChangeEndpoint = 'https://api.minecraftservices.com/minecraft/profile/name/'
        self.createProfileEndpoint = 'https://api.minecraftservices.com/minecraft/profile/'
        self.authHeader = None
        self.drop_time = dropTime

        # Proxy information
        self.proxies = proxies

        # Timings
        self.adjustment = -2

    def __defAuthHeader(self, token):

        self.authHeader = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }

    async def __nameChangeRequest(self, username):

        if self.proxies is None:
            if self.gamepassAccount is not None:
                return await requests.post(self.createProfileEndpoint, headers= self.authHeader, json= {"profileName": username}, proxies= self.proxies)
            else:
                return await requests.put(self.nameChangeEndpoint + username, headers= self.authHeader, proxies= self.proxies, verify = False)

        else:
            if self.gamepassAccount is not None:
                print(self.createProfileEndpoint)
                print(self.authHeader)
                print(username)
                print(self.proxies)
                return await requests.post(self.createProfileEndpoint, headers= self.authHeader, json= {"profileName": username}, proxies= self.proxies)
            else:
                return await requests.put(self.nameChangeEndpoint + username, headers= self.authHeader, proxies= self.proxies, verify = False)

    async def __snipeLoop(self, username):
        while True:
            response = await self.__nameChangeRequest(username)
            if response.status_code == 200:
                print(f'Successfully sniped {username}')
            else:
                print(response.text)
                print(response.status_code)

    def snipe(self, username, token, gamepassAccount= None):
        self.gamepassAccount = gamepassAccount

        self.__defAuthHeader(token)

        pause.until(self.drop_time + self.adjustment)

        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.__snipeLoop(username))
        loop.close()