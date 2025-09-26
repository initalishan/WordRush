import random

with open("word.txt") as f:
        words = [w.strip().lower() for w in f.readlines() if w.strip().isalpha()]
        
def get_word(difficulty):
    ranges = {
        "easy": (3, 4),
        "medium": (5, 5),
        "hard": (6, 8),
        "extreme": (9, 12)
    }
    min_len, max_len = (ranges[difficulty])
    filtered = [w for w in words if min_len <= len(w) <= max_len]
    return random.choice(filtered)