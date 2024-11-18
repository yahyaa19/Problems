import random

def run_simulation() -> bool:
    """
    Simulates drawing 20 balls randomly from a deck of 100 balls (numbered 1 to 100).
    Returns True if the last drawn ball is greater than 39, otherwise False.

    Returns:
        bool: True if the last drawn ball is > 39, False otherwise.
    """
    # Create a balls of balls numbered from 1 to 100
    balls = list(range(1, 101))

    # Draw 20 balls randomly
    for _ in range(20):
        # Remove a random card from the deck
        draw = balls.pop(random.randint(0, len(balls) - 1))

    # Check if the last drawn ball is greater than 39
    return draw > 39

def calculate_probability(simulations = 100000):
    """
    Calculates the probability that the last drawn ball is greater than 39 
    over a specified number of simulations.

    Args:
        simulations (int): Number of simulations to run. Defaults to 100,000.

    Returns:
        float: The probability that the last drawn card is greater than 39.
    """
    # Run the simulation multiple times and calculate the success rate
    successful_simulations = sum(run_simulation() for i in range(simulations))
    return successful_simulations / simulations

if __name__ == "__main__":
    # Run the probability calculation with 100,000 simulations
    probability = calculate_probability(100000)
    print(f"Estimated Probability: {probability}")
