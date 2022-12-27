import nltk

def generate_summary(tokens, matched_patterns):
    """根据匹配的摘要模式生成摘要"""
    pos_tags = nltk.pos_tag(tokens)  # 词性标注
    summary = []
    for pattern in matched_patterns:
        keyword, pos = pattern
        for i, (token, tag) in enumerate(pos_tags):
            if token == keyword and tag == pos:
                summary.append(token)
                break
    return summary
