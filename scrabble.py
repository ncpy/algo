import random
from itertools import permutations 

# given 1
letter_score = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4,
         "G": 2, "H": 4, "I": 1, "J": 8, "K": 5, "L": 1, 
         "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10,"R": 1, 
         "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8,
         "Y": 4, "Z": 10}

# given 2
bag = ["E"]*12 +  ["A", "I"]*9 + ["O"]*8 + ["N","R","T"]*6 + ["L","S","U","D"]*4 + ["G"]*3 + ["B","C","M","P","F","H","V","W","Y"]*2 + ["K","J","X","Q","Z"]*1

# given 3
words = []
with open("Q:/algo/dictionary.txt", "r") as file:
    dictionary = file.readlines()
for i in dictionary:
    words.append(i.strip())

# randomize
seven_tiles = ""
for i in range(7):
    seven_tiles = seven_tiles + random.choice(bag)
print(seven_tiles)  #random created 7-letter-word

# scoring
def scrabble_score(word):
    total = 0
    for letter in word:
        total = total+letter_score[letter.upper()]
    return total

#combination or permutation :)
comb_list = []
for i in range(7):
    comb_list.append(permutations(seven_tiles, i))

#valid words
n = 0
valid_words = []
for comb in comb_list:
    for i in comb: 
        i = "".join(i)
        if i.lower() in words:
            if i not in valid_words:
                valid_words.append(i)
        n += 1
        print(n)
print(valid_words)

# scoring of valid words
longest = 0
highest = 0
longest_word = ""
highest_score_word = ""
for i in valid_words:
    if len(i) >= longest:
        longest = len(i)
        longest_word = i
    if scrabble_score(i) >= highest:
        highest = scrabble_score(i)
        highest_score_word = i

print("long: ", longest, longest_word)
print("high_score: ", highest, highest_score_word)






# s = ["acd", "cda", "ert"]
# c = permutations("acd", 3)
# for i in c:
#     i = "".join(i)
#     if i in s:
#         print(i)