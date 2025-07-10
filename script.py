
import os
from pyrogram import Client, filters
from pyrogram.types import Message

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "@raj_dev_01")

app = Client("raj_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start_handler(client, message: Message):
    await message.reply_text(f"👋 Hello {message.from_user.first_name}!

"
                              f"Welcome to the bot.

"
                              f"Use /help to know more.

🤖 Credit: {OWNER_USERNAME}")

@app.on_message(filters.command("help"))
async def help_handler(client, message: Message):
    await message.reply_text("🛠 Available Commands:
"
                              "/start - Start the bot
"
                              "/help - Help info
"
                              "/about - About this bot
"
                              "/rules - Channel rules
"
                              "/check - Status
"
                              "/filter - Set filters
"
                              "/delfilters - Delete filters
"
                              "/broadcast - Send to all
"
                              "/groupbroadcast - Group broadcast
"
                              "/clone - Clone a message")

@app.on_message(filters.command("about"))
async def about_handler(client, message: Message):
    await message.reply_text("ℹ️ This is a custom Telegram bot.
Developed and maintained by Rajdev.
"
                              f"Username: {OWNER_USERNAME}")

@app.on_message(filters.command("rules"))
async def rules_handler(client, message: Message):
    await message.reply_text("📜 Rules:
1. Be respectful
2. No spam
3. Follow admin instructions")

@app.on_message(filters.command("check"))
async def check_handler(client, message: Message):
    await message.reply_text("✅ Bot is up and running.")

@app.on_message(filters.command("filter"))
async def filter_handler(client, message: Message):
    await message.reply_text("🔎 Filter set successfully. (Placeholder)")

@app.on_message(filters.command("delfilters"))
async def delfilters_handler(client, message: Message):
    await message.reply_text("🗑 All filters deleted. (Placeholder)")

@app.on_message(filters.command("broadcast"))
async def broadcast_handler(client, message: Message):
    await message.reply_text("📢 Broadcast sent. (Placeholder)")

@app.on_message(filters.command("groupbroadcast"))
async def groupbroadcast_handler(client, message: Message):
    await message.reply_text("📢 Group broadcast sent. (Placeholder)")

@app.on_message(filters.command("clone"))
async def clone_handler(client, message: Message):
    await message.reply_text("📋 Clone operation completed. (Placeholder)")

app.run()
