from telethon import TelegramClient, events
from telethon import types
import asyncio
from random import randint

api_id = 'API_ID'
api_hash = 'API_HASH'
phone = 'PHONE_NUMBER'

client = TelegramClient('anon', api_id, api_hash)

sleep_time_min = 0.1 
sleep_time_max = 0.2

# Dictionary to keep track of user's last interaction time
user_last_interaction_time = {}

async def check_for_done_message():
    while True:
        await asyncio.sleep(1)  # Check every second for testing (you might want to change this back to 60 for production)
        current_time = client.loop.time()
        for chat_id, last_time in list(user_last_interaction_time.items()):
            if (current_time - last_time) >= randint(sleep_time_min * 60, sleep_time_max * 60):
                await client.send_message(chat_id, "We haven't received a 'done' from you yet. Is there anything else we can assist you with?")
                del user_last_interaction_time[chat_id]


async def my_event_handler(event):
    chat_id = event.chat_id

    if "new" in event.text.lower():
        await client.send_message(
            chat_id,
            file=types.InputDocument(
                id=1137162165791228056,
                access_hash=4295297447653710446,
                file_reference=b'\x01\x00\x00\x00\x02d\xd3c\xf1\xf5\xa7\xdf\x9f\xff,\x1aS\xb5\xb1Nb\xd9\xf7\xf7\xbd'
            )
        )
        user_last_interaction_time[chat_id] = client.loop.time()
        
    elif "order" in event.text.lower():
        welcome_message = "test"
        await event.reply(welcome_message)
        user_last_interaction_time[chat_id] = client.loop.time()
        
    elif "done" in event.text.lower():
        if chat_id in user_last_interaction_time:
            del user_last_interaction_time[chat_id]

async def main():
    await client.connect()

    if not await client.is_user_authorized():
        await client.send_code_request(phone)
        code = input('Enter the code: ')
        await client.sign_in(phone, code)

    client.add_event_handler(my_event_handler, events.NewMessage)
    client.loop.create_task(check_for_done_message())  # Start the "done" message check task
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
