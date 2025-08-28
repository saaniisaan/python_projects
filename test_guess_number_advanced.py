# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 13:53:42 2025

@author: saani
"""

# test_guess_number_advanced.py
from guess_number_advanced import GuessNumberGame

def test_guess_game():
    game = GuessNumberGame(low=1, high=10)
    game.number = 5  # ثابت کردن عدد برای تست
    
    assert game.guess(3) == "عدد بزرگتر است!"
    assert game.guess(7) == "عدد کوچکتر است!"
    assert game.guess(5) == "تبریک! عدد 5 بود. تعداد تلاش‌ها: 3"
