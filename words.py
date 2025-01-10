words = []
new_words = []
old_words = []
count = 1
def world_order(word_list):
    count = 1
    words = word_list.split(" ")
    print("prints words", words)
    print(len(words))
    for word in words:
        if word.startswith('*') and word.endswith('*'):
            new_words.append(word)
            print("new_words", new_words)
        else:
            old_words.append(word)
    print(words)
    print("new words", new_words)
    for item in old_words:
        new_words.append(item)
    return new_words

print(world_order("this is *a* *simple* test *case*"))
