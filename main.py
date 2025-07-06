from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent

from commands import start_bet, place_bet, close_bet, resolve_bet

client = TikTokLiveClient(unique_id=".royerfm")  # SIN el @

@client.on("comment")
async def on_comment(event: CommentEvent):
    user = event.user.unique_id
    message = event.comment.strip()
    print(f"[{user}]: {message}")

    if message == "!startbet":
        await start_bet.handle(client)
    elif message.startswith("!apuesta"):
        try:
            _, option, amount = message.split()
            await place_bet.handle(client, user, option.upper(), int(amount))
        except:
            await client.send_message("❌ Formato incorrecto. Usa !apuesta A 100")
    elif message == "!closebet":
        await close_bet.handle(client)
    elif message.startswith("!resolvebet"):
        try:
            _, winner = message.split()
            await resolve_bet.handle(client, winner.upper())
        except:
            await client.send_message("❌ Usa !resolvebet A o !resolvebet B")

if __name__ == "__main__":
    client.run()
