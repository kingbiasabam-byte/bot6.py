from telethon import TelegramClient, functions
import asyncio
import datetime
import os

api_id = 37985843
api_hash = "2c08388d6a70e5398eda0ff973ebc3cc"

client = TelegramClient("session", api_id, api_hash)

async def main():
    await client.start()
    print("✅ ربات فعال شد")

    while True:
        now = datetime.datetime.now()

        hour = now.hour

        if 5 <= hour < 12:
            greeting = "🌞 صبح بخیر"
        elif 12 <= hour < 18:
            greeting = "☀️ روز بخیر"
        elif 18 <= hour < 22:
            greeting = "🌆 عصر بخیر"
        else:
            greeting = "🌙 شب بخیر"

        bio_text = (
            f"🕒 {now.strftime('%H:%M:%S')}\n"
            f"📅 {now.strftime('%Y/%m/%d')}\n"
            f"📆 {now.strftime('%A')}\n"
            f"{greeting}"
        )

        await client(functions.account.UpdateProfileRequest(
            about=bio_text
        ))

        print("Updated")
        await asyncio.sleep(60)

with client:
    client.loop.run_until_complete(main())
