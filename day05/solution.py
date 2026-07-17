def word_count(text):
    words = text.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


if __name__ == "__main__":
    print(word_count("the cat sat on the mat"))
    print(word_count("hello world hello"))
    
