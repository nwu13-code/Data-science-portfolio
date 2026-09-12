
from datetime import datetime

def greet_user():
    name = input("Enter your name: ")

    hour = datetime.now().hour
    if hour < 12:
        time_hello = "Good morning"
    elif hour < 18:
        time_hello = "Good afternoon"
    else:
        time_hello = "Good evening"

    print(f"{time_hello}, {name}! Welcome to Data Science.")

if __name__ == "__main__":
    greet_user()
