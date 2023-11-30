# Count the occurrences of each word in a sentence
sentence = "This is a simple sentence. This sentence is for testing."
word_count = {}
words = sentence.split()
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word count:", word_count)