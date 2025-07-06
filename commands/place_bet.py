from core import bet_manager, user_points

async def handle(client, user, option, amount):
    current_points = user_points.get_user_points(user)
    if amount > current_points:
        await client.send_message(f"❌ {user}, no tienes suficientes puntos.")
        return

    result = bet_manager.place_bet(user, option, amount)
    if result.startswith("✅"):
        user_points.update_user_points(user, -amount)
    await client.send_message(f"{user} {result}")
