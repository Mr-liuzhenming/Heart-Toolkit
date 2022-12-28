from .text_reader import read_text
from .keyword_extractor import extract_keywords
from .pattern_builder import build_patterns
from .pattern_matcher import match_patterns
from .summary_generator import generate_summary

def summarize(text):
    """生成文本摘要"""
    tokens = read_text(text)
    keywords = extract_keywords(tokens)
    patterns = build_patterns(keywords)
    matched_patterns = match_patterns(tokens, patterns)
    summary = generate_summary(tokens, matched_patterns)
    return summary 
