def sentences_word(sentences_list):
    #Using list comprehension and and split function i have make list of list.
    word_trees = [sentences.split(" ") for sentences in sentences_list]
    #Using list comprehension i have open all list of list into one list(means i have add all word into one list)
    word_list = [word for word_list in word_trees for word in word_list]
    #using dictionary comprehension i have count number of word appearance in list.
    word_count = {word: word_list.count(word) for word in word_list}
    print("word_trees: {}".format(word_trees), "\nNumber of time each word appears: {}".format(word_count))


if __name__ == "__main__":
    sentences = [
        "My name is Ram",
        "He is a good person",
        "You should be careful while coding",
        "He can do better",
        "The person is mysterious;",
        "Jay Shree Ram",
        "It is my pen.",
    ]
    sentences_word(sentences)