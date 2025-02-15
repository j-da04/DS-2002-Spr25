#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3

import os

import os

# Prompt user for input and store in variables
favorite_color = input('What is your favorite color? ')
hobby = input('What is your favorite hobby? ')
city = input('Which city do you live in? ')

# Set the values as environment variables
os.environ["FAVORITE_COLOR"] = favorite_color
os.environ["HOBBY"] = hobby
os.environ["CITY"] = city

# Fetch and print the environment variables
print(os.getenv("FAVORITE_COLOR"))
print(os.getenv("HOBBY"))
print(os.getenv("CITY"))

