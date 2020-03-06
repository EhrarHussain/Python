from spacy.lang.en import English


def List2Str(list1):
    listToStr = ' '.join([str(elem) for elem in list1])
    return listToStr


nlp = English()


def stopwards(text):

    my_doc = nlp(text)
    # Create list of word tokens
    token_list = []
    for token in my_doc:
        token_list.append(token.text)

    filtered_sentence =[]

    for word in token_list:
        lexeme = nlp.vocab[word]
        if not lexeme.is_stop:
            filtered_sentence.append(word)

    return List2Str(filtered_sentence)


print(stopwards("i am going to play football"))
