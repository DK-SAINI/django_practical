# Python Django Practical 1.0.1

- Plase use Python 3.xx
- Make sure to use proper git-ignore for the commit.

## Problem Statement
- Please write an API that validates the DDOS attacks 
- Write a normal API that authenticates using the Bearer Key "mf8nrqICaHYD1y8wRMBksWm7U7gLgXy1mSWjhI0q" in the header.
- The API should be blocked for 20 minutes if same bearer is tried for over 10 times in 20 seconds.
- Once the 20 minutes are passed, the IP Should be allowed to access again.
- If the threshold breaking is crossed over 100 times in a minute's time the IP shuould be blocked parmenentaly. 
- The error should return a 400 Error response.
- Otherwise should return a JSON - with random data- You can generate the data from https://www.mockaroo.com/

## Project Setup Step
- Download zip and extract it.(Also other options, you can find online.)
- create virtual enviroment.
``` python -m venv venv ```
- Activate enivroment.
MacOS/Linux: ``` source venv/bin/activate```
-Install requirement.txt file.
``` pip install -r requirements.txt```
- Creat database and tables.
``` python manage.py makemigrations```
``` python manage.py migrate```
- run development server.
``` python manage.py runserver```