import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def select_and_announce_winner(self):
        if self.is_empty():
            print("No entries in the raffle.")
            return None

        winner_index = random.randrange(len(self.items))

        winner = None
        for _ in range(winner_index + 1):
            winner = self.dequeue()

        print(f"The winner is: {winner}")
        return winner