from environment import EmailEnv
import random

env = EmailEnv()

tasks = ["easy", "medium", "hard"]

results = {}

for task in tasks:
    total_reward = 0

    for _ in range(10):
        state = env.reset(task)
        action = random.randint(0, 2)
        _, reward, _, _ = env.step(action)
        total_reward += reward

    avg_score = total_reward / 10
    results[task] = avg_score
    print(f"{task} average score: {avg_score}")

final_score = sum(results.values()) / len(results)
print("Final Score:", final_score)