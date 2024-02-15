from telethon import TelegramClient, events

api_id = 'API_ID'
api_hash = "API_HASH"
bot_token = 'BOT_TOKEN'

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
