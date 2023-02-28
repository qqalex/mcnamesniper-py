from Sniper import listener, database
import asyncio

checker = listener()
db = database.manage()

watchdog_list = open('watchdog').readlines()

max_position = len(watchdog_list)

for username in watchdog_list:
    username = username.strip()
    db.addProfile(username=username)


async def check_asyncio(username):
    try:
        status_code, response_uuid, status_time = await checker.check(username)

        if status_code is not None:

            print('check')
            if status_code == 204 and db.getStatus() == 200:
                info = f'{username}\n{db.getLastStatusUpdate}\n{status_time}'
                open(f'{username}_droptime.txt','w').write(info)
            else:
                db.setStatus(username=username, status=status_code, time=status_time)
                db.setUUID(username=username, uuid=response_uuid)
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
    