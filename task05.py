def word_count(text):
    words = text.split()
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count

print(word_count("salom salom dunyo"))