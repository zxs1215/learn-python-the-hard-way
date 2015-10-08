def break_words(suff):
    words = suff.split(' ')
    return words

def sort_words(words):
    return sorted(words)

def print_first_word(words):
    word = words.pop(0)
    print word

def print_last_word(words):
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


sentence = "All good things come to those who wait."
words = break_words(sentence)
words
sorted_words = sort_words(words)
sorted_words
print_first_word(words)
print_last_word(words)
words
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words
sorted_words = sort_sentence(sentence)
sorted_words
print_first_and_last(sentence)
print_first_and_last_sorted(sentence)