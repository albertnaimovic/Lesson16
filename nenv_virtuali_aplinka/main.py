# Use any of virtual environment option , install random-word package and create shot python script which would print out 5 random word
# (names must be all capital letter and sorted.)

from random_word import RandomWords

random_words: list = lambda: sorted([RandomWords().get_random_word().capitalize() for x in range(5)])

print(random_words())
