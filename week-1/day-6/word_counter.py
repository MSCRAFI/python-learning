# python program to count the occurrences of each word in a given sentence.

text = input("Enter a sentence: ")
words = text.split()
word_count = {"word": 0}
for word in words:
    word_count["word"] += 1

print(f"Word occurrences with loop: {word_count["word"]} or with len: {len(words)}")