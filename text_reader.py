import nltk

def read_and_tokenize(text_file):
    """读入文本并将文本分词"""
    with open(text_file, 'r') as f:
        text = f.read()
    tokens = nltk.word_tokenize(text)
    return tokens
