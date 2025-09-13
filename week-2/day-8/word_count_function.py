# python function to count words in a sentence.

def count_words(sentence): # using len() function
    words = sentence.split()
    return len(words)

def count_words_2(sentence): # using loop
    words = sentence.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

sentence = input("Enter a sentence: ")
word_count = count_words(sentence)
word_count_2 = count_words_2(sentence)
print(f"The number of words in the sentence is: {word_count}")
print(f"The number of words in the sentence using loop is: {word_count_2}")