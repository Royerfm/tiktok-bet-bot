from core import bet_manager

async def handle(client):
    bet_manager.start_bet()
    await client.send_message("🟢 ¡Nueva apuesta abierta! Elige A o B con '!apuesta A 100'")
