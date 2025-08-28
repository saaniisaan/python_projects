# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 13:53:21 2025

@author: saani
"""

# guess_number_advanced.py
import random

class GuessNumberGame:
    """بازی حدس عدد حرفه‌ای"""
    
    def __init__(self, low=1, high=100):
        self.low = low
        self.high = high
        self.number = random.randint(low, high)
        self.attempts = 0

    def guess(self, value):
        self.attempts += 1
        if value < self.number:
            return "عدد بزرگتر است!"
        elif value > self.number:
            return "عدد کوچکتر است!"
        else:
            return f"تبریک! عدد {self.number} بود. تعداد تلاش‌ها: {self.attempts}"

    def run(self):
        print(f"به بازی حدس عدد خوش آمدید! عدد بین {self.low} تا {self.high} است.")
        while True:
            try:
                guess = int(input("حدس شما: "))
                result = self.guess(guess)
                print(result)
                if "تبریک" in result:
                    break
            except ValueError:
                print("لطفاً عدد صحیح وارد کنید.")


if __name__ == "__main__":
    game = GuessNumberGame()
    game.run()