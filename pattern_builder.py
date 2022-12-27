def build_patterns(keywords):
    """根据关键词构建摘要模式"""
    patterns = []
    for keyword in keywords:
        patterns.append((keyword, 'NN'))
    return patterns
