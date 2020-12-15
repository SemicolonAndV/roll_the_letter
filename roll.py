from random import randint

def load_names(file):
    with open(file, 'r') as data:
        return [x.strip() for x in data.readlines()]

def generate():
    while True:
        x = randint(1, 6)
        yield x

def roll(list_of_names):
    dice = generate()
    letter_stats = {}
    for letter in 'WesolychSwiat':
        letter_stats[letter] = {}
        for name in list_of_names:
            score = 0
            for _ in range(2137):
                score += next(dice)
            letter_stats[letter][name] = score
    return letter_stats
    
if name == "__main__":
    result = roll(load_names('names.txt'))
    for k, v in result.items():
        print(f"{k}: {sorted(v.items(), key=lambda x: x[1], reverse=True)}\n")
