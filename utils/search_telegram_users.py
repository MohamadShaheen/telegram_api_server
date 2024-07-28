from telethon import TelegramClient
from dotenv import load_dotenv
import asyncio
import json
import os

load_dotenv()
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

if api_id is None or api_hash is None:
    print('API ID and hash are not set correctly. Refer to README.md for further information.')
    exit(1)

try:
    api_id = int(api_id)
except ValueError:
    print('API ID is not an integer. Refer to README.md for more information.')
    exit(1)

client = TelegramClient('session', api_id=api_id, api_hash=api_hash)

async def search_users():
    async with client:
        users = []
        try:
            async for user in client.iter_participants('@hamsters_news_chat'):
                # if keyword.lower() in (user.username or user.first_name or user.last_name or '').lower():
                users.append({
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'user_id': user.id,
                })
        except Exception as e:
            print(f'An error occurred: {e}')
        return users

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    users = loop.run_until_complete(search_users())
    with open('../data/users.json', 'w') as file:
        json.dump(users, file, indent=4)
