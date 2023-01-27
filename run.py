import mcsniper

    # Account tokens
bearerToken = 'eyJraWQiOiI0ZjZjOCIsImFsZyI6IkhTMjU2In0.eyJ4dWlkIjoiMjUzNTQyMzA5MTMxMTc2MiIsImFnZyI6IkFkdWx0Iiwic3ViIjoiOTM5M2ZkMDAtOTJiMC00MmFhLTgyOWEtZDY5MmExNDA2ZjA5IiwibmJmIjoxNjc0NjI5MTM0LCJhdXRoIjoiWEJPWCIsInJvbGVzIjpbXSwiaXNzIjoiYXV0aGVudGljYXRpb24iLCJleHAiOjE2NzQ3MTU1MzQsImlhdCI6MTY3NDYyOTEzNCwicGxhdGZvcm0iOiJVTktOT1dOIiwieXVpZCI6IjYyZTM2Y2RiMWY3MDMxNjllZWNkYjU0MWMyYzk5MDFlIn0.2r-8TJ_R91bc3LGiwQLx31YD95mTZSwjLVq0rKkcp5w'

    # Proxy credentials
proxy = {'http':'minecat:5d86f4-e1a8a9-a211fd-5f7e38-23741a@usa.rotating.proxyrack.net:9000'}

sniper = mcsniper.FoxSniper(1674454282, True, proxy)
sniper.snipe("Alex", bearerToken)
