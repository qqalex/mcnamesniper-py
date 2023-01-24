import mcsniper

    # Account tokens
bearerToken = 'eyJhbGciOiJIUzI1NiJ9.eyJ4dWlkIjoiMjUzNTQ0NDcyMzM4MDY0MCIsImFnZyI6IkFkdWx0Iiwic3ViIjoiMTc4Nzk4MzAtMzE5MS00NTA2LTgwYjAtOTllNDVmNDhmNjVkIiwibmJmIjoxNjc0NTM3MDQ4LCJhdXRoIjoiWEJPWCIsInJvbGVzIjpbXSwiaXNzIjoiYXV0aGVudGljYXRpb24iLCJleHAiOjE2NzQ2MjM0NDgsImlhdCI6MTY3NDUzNzA0OCwicGxhdGZvcm0iOiJVTktOT1dOIiwieXVpZCI6ImE4YTIxZGQzZmQ3N2RjNDQ3MTI3ODliNjg1NTdjMTA4In0.M3PK8sXN45S4CWncqlatHvSSNCY45eR96v6JtumQuFQ'

    # Proxy credentials
proxy = {'http':'minecat:5d86f4-e1a8a9-a211fd-5f7e38-23741a@usa.rotating.proxyrack.net:9000'}
threads = 10    # Current proxy limits are 100 concurrent threads

    # Commands
sniper = mcsniper.FoxSniper(1674454282, threads, proxy)
sniper.snipe("Alex", bearerToken)