from Sniper import listener, data
import asyncio

checker = listener()
profile_object = data()

watchdog_list = open('watchdog').readlines()

max_position = len(watchdog_list)

for username in watchdog_list:
    username = username.strip()


async def check_asyncio(username):
    try:
        await checker.check(username)
    except Exception:
        pass

async def check_list():
    task_list = []
    current_position = 0
    while current_position < max_position:
        for i in range(current_position, current_position+100):
            current_position = i
            if i >= max_position:
                break
            task_list.append(asyncio.create_task(check_asyncio(watchdog_list[i])))

        await asyncio.gather(*task_list)

while True:
    print('Starting New List')
    asyncio.run(check_list())
    