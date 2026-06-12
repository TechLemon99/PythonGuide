scores = [3, 5, 5, 2, 1, 4, 0, 1, 4, 5]
total_points = 0

for index, score in enumerate(scores):
    # Default points is just the score
    points = score

    # If score is 5 and it's not the last round, add next round's score as bonus
    if score == 5 and index < 9:
        points += scores[index + 1]

    # If it's the last round and score is 5, assign 10 points
    if score == 5 and index == 9:
        points = 10

    total_points += points
    print(f"Round {index + 1} - Score {score} - Points {points}")

print(f"\nTotal Points: {total_points}")