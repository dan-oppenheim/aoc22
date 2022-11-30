import requests

with open("utils/session.txt") as session_file:
    session_cookie = session_file.readline()

day = input("Which day? ")
try:
    day = int(day.strip())
    if day < 0 or day > 24:
        raise ValueError()

    request = requests.get(f"https://adventofcode.com/2022/day/{day}/input", 
        headers={
            'cookie':f"session={session_cookie}"
        }
    )

    with open(f"input/day{day}.txt", 'w') as out_file:
        print(request.text, file=out_file)

except Exception as e:
    print(e)
    print("Please enter a number between 1 and 24")