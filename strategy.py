import random

def play_game(strategy_threshold):
    """Simulates one round of the game."""
    balls = list(range(1, 101))
    winnings = 0
    while balls and winnings < strategy_threshold:
        draw = random.choice(balls)
        if draw + winnings > strategy_threshold:
            return draw + winnings
        else:
            winnings -= 1
            balls.remove(draw)
    return winnings
    


def simulate_games(num_games, strategy_threshold):
    """Simulates multiple games with a given strategy."""
    total_winnings = 0
    for _ in range(num_games):
        total_winnings += play_game(strategy_threshold)
    return total_winnings / num_games


# Simulate with optimal strategy (redraw if <= 49)
num_simulations = 100000
average_winnings = simulate_games(num_simulations, 50.5)
print(f"Average winnings with optimal strategy (redraw if <= 49): ${average_winnings:.2f}")


# Demonstration of expected value calculation within the code (similar to calculative part)
def calculate_expected_value_redraw(current_ball):
    remaining_balls_sum = sum(range(1,101)) - current_ball
    return (remaining_balls_sum / 99.0) - 1


# Example: If you draw a ball, should you redraw?
drawn_ball = 12
ev_redraw = calculate_expected_value_redraw(drawn_ball)
print(f"\nIf you draw {drawn_ball}, the expected value of redrawing is: ${ev_redraw:.2f}")
print("Redraw!" if ev_redraw > drawn_ball else "Keep!")