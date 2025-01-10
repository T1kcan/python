# words = []
new_words = []
old_words = []
def world_order(word_list):
    words = word_list.split(" ")
    for index, word in enumerate(words):
        # print(index, word)
        if word.startswith('*') and word.endswith('*'):
            # print(index, word)
            new_words.append(word)
        else:
            old_words.append(word)
            # print(f"original list {index} - {old_words}")
    
    #print(words)
    print("new words", new_words)
    print("old words", old_words)
    for item in old_words:
        new_words.append(item)
        string = ' '.join(new_words)
    return string

print(world_order("this is *a* *simple* test *case* hala saimpel alus *1* kedi *ali*"))