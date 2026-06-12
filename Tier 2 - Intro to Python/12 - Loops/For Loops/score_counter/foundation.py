scores = [3,5,5,2,1,4,0,1,4,5]

for index, i in enumerate(scores):
    score = i
    round = index + 1

    if round == 10:
        if score >= 5:
            points == 10

    if score >= 5:
        points = score + scores[i+1]
    else:
        points = score
    
    print(f"Round {index + 1} - Score {score} - Points {points}")