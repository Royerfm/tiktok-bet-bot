from core import bet_manager

async def handle(client):
    bet_manager.close_bet()
    await client.send_message("🔒 ¡Apuestas cerradas!")
