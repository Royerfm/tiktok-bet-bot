from core import bet_manager
from core import user_points

async def handle(client, winning_option):
    await client.send_message(f"🏆 Resolviendo apuesta, opción ganadora: {winning_option}...")

    # Procesar apuestas
    total_winners = []
    total_losers = []
    
    active_bet = bet_manager.active_bet

    total_pool = sum(b["amount"] for b in active_bet["bets"].values())
    total_winning = sum(
        b["amount"] for b in active_bet["bets"].values() if b["option"] == winning_option
    )

    if total_winning == 0:
        await client.send_message("❌ Nadie apostó a la opción ganadora.")
        return

    for user, bet in active_bet["bets"].items():
        if bet["option"] == winning_option:
            reward = (bet["amount"] / total_winning) * total_pool
            user_points.update_user_points(user, int(reward))
            total_winners.append(f"{user} ganó {int(reward)} puntos 🤑")
        else:
            total_losers.append(f"{user} perdió {bet['amount']} puntos 😭")

    await client.send_message("🎉 Resultados:")
    for msg in total_winners + total_losers:
        await client.send_message(msg)

    bet_manager.active_bet["bets"] = {}
