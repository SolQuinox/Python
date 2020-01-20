import random

with open("words.txt", "r") as f:
    words = [line.strip() for line in f]

word1 = random.choice(words)
word2 = random.choice(words)
word3 = random.choice(words)

print(word1 + word2 + word3)

consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']

print(random.choice(consonants) + random.choice(vowels) + random.choice(consonants))