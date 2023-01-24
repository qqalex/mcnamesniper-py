import requests                                              # Needed for making requests in Python
import concurrent.futures                                    # Needed for making threaded requests
from requests.structures import CaseInsensitiveDict          # Needed for defining request header

import pause                                                 # Needed for running at specific unix times
                                                             # I should write my own pause, because it's really easy, and I won't have to rely on this package

class FoxSniper:

    def __init__(self, dropTime, threads, proxies= None):

        # Request info
        self.nameChangeEndpoint = "https://api.minecraftservices.com/minecraft/profile/name/"               # https://api.minecraftservices.com/minecraft/profile/name/{username}
        self.authHeader = None
        self.drop_time = dropTime                                                                           # Unix time when to start sending namechange requests

        # Proxy information
        self.proxies = proxies

        # Threads
        self.threadNum = threads

        # Timings
        self.adjustment = -3

    def __defAuthHeader(self, token):

        self.authHeader = CaseInsensitiveDict()
        self.authHeader["Authorization"] = f"Bearer {token}"

    def __nameChangeRequest(self, username):

        if self.proxies is None:
            request = requests.put(f'{self.nameChangeEndpoint}{username}', headers= self.authHeader)
            return request

        else:
            request = requests.put(f'{self.nameChangeEndpoint}{username}', headers= self.authHeader, proxies= self.proxies)
            return request

    def __run(self, username):

        nameChangeRequest = self.__nameChangeRequest(username)

        print(nameChangeRequest.status_code)
        if nameChangeRequest.status_code == 200:
            print(nameChangeRequest.content)

    def snipe(self, username, token):

        self.__defAuthHeader(token)                                         # Define the request Authorization header

        pause.until(self.drop_time + self.adjustment)                       # Pause until username droptime + adjustment

        with concurrent.futures.ProcessPoolExecutor(max_workers= self.threadNum) as executor:
            executor.submit(self.__run(username))