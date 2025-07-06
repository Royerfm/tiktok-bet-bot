# core/bet_manager.py

active_bet = {
    "open": False,
    "bets": {},
    "options": ["A", "B"]
}

def start_bet():
    active_bet["open"] = True
    active_bet["bets"] = {}
    print("🟢 Apuesta iniciada: Opción A vs Opción B")

def place_bet(user, option, amount):
    if not active_bet["open"]:
        return "⛔ Las apuestas están cerradas."
    if option not in active_bet["options"]:
        return "❌ Opción inválida."
    
    active_bet["bets"][user] = {"option": option, "amount": amount}
    return f"✅ {user} apostó {amount} puntos a la opción {option}"

def close_bet():
    active_bet["open"] = False
    print("🔒 Apuestas cerradas.")

def resolve_bet(winning_option, get_user_points, update_user_points):
    total_pool = sum(b["amount"] for b in active_bet["bets"].values())
    total_winning = sum(
        b["amount"] for b in active_bet["bets"].values() if b["option"] == winning_option
    )

    print(f"🏆 Opción ganadora: {winning_option}")
    for user, bet in active_bet["bets"].items():
        if bet["option"] == winning_option:
            reward = (bet["amount"] / total_winning) * total_pool
            update_user_points(user, int(reward))
            print(f"🎉 {user} ganó {int(reward)} puntos")
        else:
            print(f"💸 {user} perdió {bet['amount']} puntos")

    active_bet["bets"] = {}
