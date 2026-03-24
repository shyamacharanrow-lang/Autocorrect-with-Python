import difflib

def load_words():
    with open("dictionary.txt") as f:
        return f.read().splitlines()

def correct_sentence(sentence):
    words = sentence.split()
    word_list = load_words()
    
    corrected = []
    for word in words:
        match = difflib.get_close_matches(word, word_list, n=1, cutoff=0.6)
        corrected.append(match[0] if match else word)
    
    return " ".join(corrected)