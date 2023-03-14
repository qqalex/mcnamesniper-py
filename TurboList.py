from Sniper import listener, database
import asyncio

checker = listener()
db = database.manage()

watchdog_list = open('watchdog').readlines()

max_position = len(watchdog_list)

for i in range(len(watchdog_list)-1):
    watchdog_list[i] = watchdog_list[i].strip()
    db.addProfile(username=watchdog_list[i])


async def check_asyncio(user):
    try:
        status_code, response_uuid, status_time = await checker.check(user)

        if status_code is not None:

            if status_code == 204 and db.getStatus(username=user) == 200:
                info = f'{user}\n{db.getLastStatusUpdate(username=user)}\n{status_time}'
                file = open(f'{user}_droptime.txt','w')
                file.write(info)
                file.close()

            db.setStatus(username=user, status=status_code, time=status_time)
            db.setUUID(username=user, uuid=response_uuid)
    except Exception:
        pass

async def check_list():
    task_list = []
    current_position = 0
    while current_position < max_position:
        for i in range(current_position, current_position+90):
            current_position = i
            if i >= max_position:
                break
            task_list.append(asyncio.create_task(check_asyncio(watchdog_list[i])))

        await asyncio.gather(*task_list)

while True:
    print('Starting New List')
    asyncio.run(check_list())