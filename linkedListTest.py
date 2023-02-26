import Sniper
import time

db = Sniper.database.manage()

username0 = 'Alex'
username1 = 'Steve'
username2 = 'Notch'
username3 = 'Jeb'

# Set
db.addProfile(username=username0)
db.addProfile(username=username1)
db.addProfile(username=username2)
db.addProfile(username=username3)

# Set Variables
db.setStatus(username=username0, status='203', time=time.time())
db.setUUID(username=username0, uuid='ec561538f3fd461daff5086b22154bce')
db.toggleIgnore(username0)

db.setStatus(username=username1, status='203', time=time.time())
db.setUUID(username=username1, uuid='ec561538f3fd461daff5086b22154bce')
db.toggleIgnore(username1)

db.setStatus(username=username2, status='403', time=time.time())
db.setUUID(username=username2, uuid='ec561538f3fd461daff5086b22154bce')

db.setStatus(username=username3, status='203', time=time.time())
db.setUUID(username=username3, uuid='ec561538f3fd461daff5086b22154bce')

# Get
print(f"\n{db.getUsername(username0)}\n{db.getUUID(username0)}\n{db.getStatus(username0)}\n{db.getLastStatusUpdate(username0)}\n{db.getIgnore(username0)}\n\n")
print(f"\n{db.getUsername(username1)}\n{db.getUUID(username1)}\n{db.getStatus(username1)}\n{db.getLastStatusUpdate(username1)}\n{db.getIgnore(username1)}\n\n")
print(f"\n{db.getUsername(username2)}\n{db.getUUID(username2)}\n{db.getStatus(username2)}\n{db.getLastStatusUpdate(username2)}\n{db.getIgnore(username2)}\n\n")
print(f"\n{db.getUsername(username3)}\n{db.getUUID(username3)}\n{db.getStatus(username3)}\n{db.getLastStatusUpdate(username3)}\n{db.getIgnore(username3)}\n\n")