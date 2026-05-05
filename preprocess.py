import re

def extract_features(text):
    features = {}

    features['url_count'] = len(re.findall(r'http[s]?://', text))
    features['urgent_words'] = len(re.findall(r'urgent|immediately|verify|suspended|click', text.lower()))
    features['special_chars'] = len(re.findall(r'[!$]', text))

    return list(features.values())
