import nltk

def match_patterns(tokens, patterns):
    """在文本中匹配摘要模式"""
    pos_tags = nltk.pos_tag(tokens)  # 词性标注
    matched_patterns = []
    for pattern in patterns:
        keyword, pos = pattern
        for i, (token, tag) in enumerate(pos_tags):
            if token == keyword and tag == pos:
                matched_patterns.append(pattern)
                break
    return matched_patterns
