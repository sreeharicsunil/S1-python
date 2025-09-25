#sreehari c
#3)count the occurrence of each word in a line of text

text = "The cat and the dog and the cat"

text = text.lower()

words = text.split(" ")

word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

for word, count in word_counts.items():
    print(f"{word} : {count}")




