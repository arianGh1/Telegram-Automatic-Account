from telethon import TelegramClient, events

api_id = '27420773'
api_hash = '2cbf51015f3539a2b370cda8f24a2ed3'
bot_token = '6227804126:AAFIrqf9Oe9hkN7e1J7oFx3QR-LTBD7oZEs'

bot = TelegramClient('anon', api_id, api_hash).start(bot_token=bot_token)

@bot.on(events.NewMessage)
async def my_event_handler(event):
    sticker = event.message.sticker
    if sticker:
        print("Sticker ID:", sticker.id)
        print("Access Hash:", sticker.access_hash)
        print("File Reference:", sticker.file_reference)

with bot:
    bot.run_until_disconnected()