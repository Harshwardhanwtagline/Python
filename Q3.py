def sentences_word(sentences_list):
    word_trees = [i.split(" ") for i in sentences]
    word_list = [j for i in word_trees for j in i]
    dict_1 = {word: word_list.count(word) for word in word_list}
    print("word_trees: {}".format(word_trees))
    print("Number of time each word appears: {}".format(dict_1))


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