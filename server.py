import random

from fastapi import FastAPI, HTTPException
import json
import os

app = FastAPI()

@app.get('/')
async def root():
    return 'Hello from FastAPI!'

@app.get('/search/', description='Returns all users whose username, first name, or last name contains the provided keyword')
async def search(keyword: str):
    if not os.path.exists('data/users.json'):
        raise HTTPException(status_code=404, detail='Users data file not found')
    with open('data/users.json') as file:
        users = json.load(file)

    matching_users = []

    for user in users:
        username = user['username']
        user_first_name = user['first_name']
        user_last_name = user['last_name']
        if keyword.lower() in (username or user_first_name or user_last_name or '').lower():
            matching_users.append(user)

    return matching_users[0:10]

