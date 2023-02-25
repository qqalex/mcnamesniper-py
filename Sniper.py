# Standard Library Packages
import os
import time
import asyncio

# Independent Packages
import aiohttp
import pause                        

#####################################################################################
#                                                                                   #
#                       ROADMAP (in order of importance)                            #
#                                                                                   #
#   - Write a DataBase for managing profiles.                                       #
#   - Sniper needs a rewrite to work asynchronously.. with proxies.                 #
#   - Remove worthless / shit names from watchdog list.                             #
#   - Proper database for dropping usernames.                                       #
#   - - - Integrate DogBot with such drop name database.                            #
#   - Write my own pause instead of using an import.                                #
#   - Fix hardcoded credentials, basically rewrite credentials class entirely.      #
#                                                                                   #
#####################################################################################

class bcolors:
	ResetAll = "\033[0m"

	Bold       = "\033[1m"
	Dim        = "\033[2m"
	Underlined = "\033[4m"
	Blink      = "\033[5m"
	Reverse    = "\033[7m"
	Hidden     = "\033[8m"

	ResetBold       = "\033[21m"
	ResetDim        = "\033[22m"
	ResetUnderlined = "\033[24m"
	ResetBlink      = "\033[25m"
	ResetReverse    = "\033[27m"
	ResetHidden     = "\033[28m"

	Default      = "\033[39m"
	Black        = "\033[30m"
	Red          = "\033[31m"
	Green        = "\033[32m"
	Yellow       = "\033[33m"
	Blue         = "\033[34m"
	Magenta      = "\033[35m"
	Cyan         = "\033[36m"
	LightGray    = "\033[37m"
	DarkGray     = "\033[90m"
	LightRed     = "\033[91m"
	LightGreen   = "\033[92m"
	LightYellow  = "\033[93m"
	LightBlue    = "\033[94m"
	LightMagenta = "\033[95m"
	LightCyan    = "\033[96m"
	White        = "\033[97m"

	BackgroundDefault      = "\033[49m"
	BackgroundBlack        = "\033[40m"
	BackgroundRed          = "\033[41m"
	BackgroundGreen        = "\033[42m"
	BackgroundYellow       = "\033[43m"
	BackgroundBlue         = "\033[44m"
	BackgroundMagenta      = "\033[45m"
	BackgroundCyan         = "\033[46m"
	BackgroundLightGray    = "\033[47m"
	BackgroundDarkGray     = "\033[100m"
	BackgroundLightRed     = "\033[101m"
	BackgroundLightGreen   = "\033[102m"
	BackgroundLightYellow  = "\033[103m"
	BackgroundLightBlue    = "\033[104m"
	BackgroundLightMagenta = "\033[105m"
	BackgroundLightCyan    = "\033[106m"
	BackgroundWhite        = "\033[107m"

class database:

    class linkedList:

        def __init__(self, profile):
            self.profileObject = profile
            self.next = None

    class profile:

        # If last status was 200 & new status is 203 or 404
        def __init__(self, username):
            # Minecraft Profile Info
            self.username = username
            self.uuid = None

            # Boolean Of Whether To Skip Object
            self.ignore = False

            # Last API Request Status
            self.status = None

            # Time Of Last Status Update
            self.lastStatusTime = None

    class manage:

        def __init__(self):
            self.__head = None

        def addProfile(self, username):
            index = self.__head

            if index is None:
                self.__head.profileObject = database.linkedList(database.profile(username))
                return 0

            while index.next is not None:
                index = index.next
            index.next = database.linkedList(database.profile(username))
            return 0

        def getProfile(self, username):
            index = self.__head

            while True:
                if index.profileObject.username == username:
                    return index.profileObject
                elif index.next == None:
                    return None
                else:
                    index = index.next

        def setUUID(self, username, uuid): # Set the UUID of a profile in a LL; find the profile with a given username
            profile = self.getProfile(username)
            if profile is not None:
                profile.uuid = uuid

        def getUUID(self, username): # Get the UUID of a profile in a LL; find the profile with a given username
            profile = self.getProfile(username)
            if profile is not None:
                return profile.uuid

        def setStatus(self, username, status, time): # Set the most recent API status of profile in LL
            profile = self.getProfile(username)
            if profile is not None:
                profile.status = status
                profile.lastStatusTime = time

        def getStatus(self, username): # Get the most recent API status of profile in LL
            profile = self.getProfile(username)
            if profile is not None:
                return profile.status

        def toggleIgnore(self, username): # Set the boolean of whether to ignore a profile in LL
            profile = self.getProfile(username)
            if profile is not None:
                profile.ignore = not profile.ignore

        def getIgnore(self, username): # Get the boolean of whether to ignore a profile in LL
            profile = self.getProfile(username)
            if profile is not None:
                return profile.ignore

class credentials:

    # At some point, these credentials need to be stored in a better manner; ie. not hardcoded.

    def __init__(self):
        # Discord verification tokens
        self.verification_bot_token = "MTA2OTE2ODA2OTAyNjUyNTIwNA.Gmj87y.wrLxx0Gm_eZa0BJZ4En55YMC4Q6njGbGqnkamc"
        self.dog_bot_token = "MTA2OTE2ODA2OTAyNjUyNTIwNA.Gmj87y.wrLxx0Gm_eZa0BJZ4En55YMC4Q6njGbGqnkamc"
        
        # Proxy authentication credentials     username:creds@rotating-address
        self.proxy = 'http://minecat:5d86f4-e1a8a9-a211fd-5f7e38-23741a@usa.rotating.proxyrack.net:9000'

class watchdog:

    def __init__(self):
        self.watchdog_file_name = 'wd/watchdog'

        if os.path.isfile(self.watchdog_file_name):
            pass
        else:
            open(self.watchdog_file_name, 'w')

        self.watchdog_file_read = open(self.watchdog_file_name, 'r')
        self.watchdog_list = self.__loadList()

    def __loadList(self):
        list = self.watchdog_file_read.readlines()
        for i in range(len(list)-1):
            list[i] = list[i].strip()
        
        return list

    def __checkDuplicates(self, name):
        list = self.watchdog_list

        if name in list:
            return 1
        else:
            return 0

    def __listWrite(self):
        list_string = ''

        file = open(self.watchdog_file_name, 'w')
        list = self.watchdog_list

        last_index = len(list)-1
        for i in list:
            if i == list[last_index]:
                list_string += f'{i}'
            else:
                list_string += f'{i}\n'

        file.write(list_string)

    def Watch(self, name):
        name = name.lower()
        if self.__checkDuplicates(name):
            return 1
        else:
            pass

        self.watchdog_list.append(name)
        self.__listWrite()
        
        return 0

    def Ignore(self, name):
        name = name.lower()
        if self.__checkDuplicates(name):
            pass
        else:
            return 0

        self.watchdog_list.remove(name)
        self.__listWrite()

class namesniper:

    def __init__(self, dropTime):

        # Request info
        self.nameChangeEndpoint = 'https://api.minecraftservices.com/minecraft/profile/name/'
        self.createProfileEndpoint = 'https://api.minecraftservices.com/minecraft/profile/'
        self.authHeader = None
        self.drop_time = dropTime

        # Proxy information
        self.proxies = credentials().proxy

        # Timings
        self.adjustment = -2

    def __defAuthHeader(self, token):

        self.authHeader = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }

    async def __nameChangeRequest(self, username):
        # "Gamepass" Create profile namechange request
        if self.gamepassAccount:
            async with aiohttp.ClientSession() as session:
                async with session.post(self.createProfileEndpoint, headers= self.authHeader, json= {"profileName": username}, proxy= self.proxies) as response:
                    return response

        # Existing account namechange request
        else:
            async with aiohttp.ClientSession() as session:
                async with session.put(self.nameChangeEndpoint + username, headers= self.authHeader, proxy= self.proxies) as response:
                    return response

    async def __snipeLoop(self, username):
        while True:
            response = await self.__nameChangeRequest(username)
            if response.status == 200:
                print(f'Successfully sniped {username}')
                return 1
            else:
                print(response.status)

    async def snipe(self, username, token, gamepassAccount= None):
        self.gamepassAccount = gamepassAccount

        self.__defAuthHeader(token)

        pause.until(self.drop_time + self.adjustment)

        loop = asyncio.get_event_loop()
        loop.run_until_complete(await self.__snipeLoop(username))
        loop.close()

class listener:

    def __init__(self):
        self.uuidEndpoint = 'https://api.mojang.com/users/profiles/minecraft/' #<username>
        self.proxies = credentials().proxy
        self.nameChangeStartRange = None
        self.nameChangeEndRange = None

    async def __requestCurrentUUID(self, username):
        async with aiohttp.ClientSession(timeout= aiohttp.ClientTimeout(total=1)) as session:
            async with session.get(f'{self.uuidEndpoint}{username}', proxy=self.proxies) as response:
                return response

    
    async def check(self, username):

        response = await self.__requestCurrentUUID(username)

        self.nameChangeEndRange = time.time()

        if response.status == 200: # Success
            print(f'{bcolors.Green}{response.status} {username}{bcolors.ResetAll}', end='')
        elif response.status == 404: # Name is in uncache limbo
            print(f'{bcolors.Green}{bcolors.Blink}{bcolors.BackgroundLightMagenta}{response.status} {username}{bcolors.ResetAll}', end='')
            info = f'{username}\n{self.nameChangeEndRange}'
            open(f'{username}_droptime.txt','w').write(info)
        elif response.status == 204: # Name is in limbo
            print(f'{bcolors.Magenta}{response.status} {username}{bcolors.ResetAll}', end='')
        elif response.status == 403: # Error
            print(f'{bcolors.Red}{response.status} {username}{bcolors.ResetAll}', end='')
        else: # Blanket else case, incase there is any I missed.
            print(f'{bcolors.Red}{bcolors.Blink}{bcolors.BackgroundLightRed}{response.status} {username}{bcolors.ResetAll}', end='')