from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

def extract_keywords(tokens):
    """提取关键词"""
    # 去除停用词
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    # 词形还原
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    # 计算词频
    word_frequencies = {}
    for token in lemmatized_tokens:
        if token in word_frequencies:
            word_frequencies[token] += 1
        else:
            word_frequencies[token] = 1
    # 计算词的权重（可以使用 TextRank 算法或其他算法）
    # 这里我们简单地使用词频作为权重
    keywords = []
    for token, frequency in word_frequencies.items():
        keywords.append((token, frequency))
    # 根据权重排序
    keywords.sort(key=lambda x: x[1], reverse=True)
    # 提取前n个关键词
    n = 10
    top_keywords = keywords[:n]
    return top_keywords
