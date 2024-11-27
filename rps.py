import random

def player(prev_play, opponent_history=[]):
    """
    Rock-Paper-Scissors player function.

    This function predicts the opponent's moves and counters them strategically.
    """
    # Append the previous play to opponent history
    if prev_play:
        opponent_history.append(prev_play)

    # Limit the opponent history size for efficiency
    history_limit = 100
    if len(opponent_history) > history_limit:
        opponent_history = opponent_history[-history_limit:]

    # If no previous play, start with Rock
    if not prev_play:
        return "R"

    # Strategy 1: Counter the most common move
    move_counts = {move: opponent_history.count(move) for move in "RPS"}
    most_common_move = max(move_counts, key=move_counts.get)
    counter = {"R": "P", "P": "S", "S": "R"}  # Counter rules
    move1 = counter[most_common_move]

    # Strategy 2: Detect repeated sequences
    sequence_length = 5
    if len(opponent_history) >= sequence_length:
        recent_sequence = "".join(opponent_history[-sequence_length:])
        for i in range(len(opponent_history) - sequence_length - 1, -1, -1):
            if "".join(opponent_history[i:i + sequence_length]) == recent_sequence:
                if i + sequence_length < len(opponent_history):
                    predicted_move = opponent_history[i + sequence_length]
                    return counter[predicted_move]

    # Fallback: Play the counter to the most common move
    return move1
