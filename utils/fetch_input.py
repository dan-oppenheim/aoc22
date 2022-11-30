import requests

with open("session.txt") as session_file:
    session_cookie = session_file.readline()

day = input("Which day? ")
try:
    day = int(day.strip())
    if day < 0 or day > 24:
        raise ValueError()

    request = requests.get(f"https://adventofcode.com/2021/day/{day}/input", 
        headers={
            'cookie':f"session={session_cookie}"
        }
    )
    print(request.text)
except Exception as e:
    print(e)
    print("Please enter a number between 1 and 24")