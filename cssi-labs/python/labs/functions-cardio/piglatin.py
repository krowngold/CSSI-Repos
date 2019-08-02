def get_words():
    """
        Return a list of words form the user.
    """
    words = raw_input("Enter a word or phrase: ")
    word_list = words.split(" ")
    return word_list

    #TODO: return something

def first_vowel(word):
    """
        Find the index of the first vowel
        Returns None if there were no vowels
    """
    vowels = ["a", "e", "i", "o", "u"]
    for i in range(len(word)):
        if word[i].lower() in vowels:
            return i

def rotate(word):
    """
        Return a version of word that is in pig latin
        Empty string is not accepted
    """
    new_word = ""
    letters = list(word)
    if first_vowel(word) != 0:
        letters.append(letters[0].lower())
        letters.remove(letters[0])
        letters.append("ay")
    else:
        letters.append("yay")
    for i in range(0,len(letters)):
        new_word += letters[i]

    new_word[0].upper()
    return new_word


def combineWords(word_list):
    """
        Combines a list of words into a phrase
        that is separated by spcaes
    """
    #TODO: return something
    phrase =  ""
    for i in word_list:
        phrase = phrase + str(i) + " "
    return phrase.strip()

# print combineWords(['test', 'word', 'list'])
# print combineWords([])
# print combineWords([24,3,54,98,420])
# print combineWords(["Hello"])


words = get_words();
pig_phrase = []

for word in words:
    pig_word = rotate(word)
    pig_phrase.append(pig_word)

print combineWords(pig_phrase)
