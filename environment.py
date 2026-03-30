import random
from typing import Tuple

class EmailEnv:
    def __init__(self):
        self.tasks = {
            "easy": [
                ("Win money now!!!", 0),
                ("Meeting at 5pm today", 1),
                ("Flat 50% off sale", 2)
            ],
            "medium": [
                ("Update your bank details urgently", 0),
                ("Project submission tomorrow", 1),
                ("Exclusive shopping deals", 2)
            ],
            "hard": [
                ("Reminder: claim reward before expiry", 0),
                ("Client meeting rescheduled", 1),
                ("Limited time offer just for you", 2)
            ]
        }
        self.current_email = None
        self.current_label = None
        self.current_task = None

    def reset(self, task: str = "easy") -> str:
        if task not in self.tasks:
            raise ValueError("Invalid task")

        self.current_task = task
        email, label = random.choice(self.tasks[task])
        self.current_email = email
        self.current_label = label
        return email

    def step(self, action: int) -> Tuple[str, float, bool, dict]:
        if self.current_email is None:
            raise ValueError("Call reset() first")

        correct = self.current_label

        if action == correct:
            reward = 1.0
        elif abs(action - correct) == 1:
            reward = 0.5
        else:
            reward = -1.0

        done = True

        return self.current_email, reward, done, {
            "correct_label": correct,
            "task": self.current_task
        }

    def state(self) -> str:
        return self.current_email
        def reset(self):
            return self.state
