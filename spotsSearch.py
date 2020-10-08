from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import re

def spotSortByDocuments(chatDoc, spotsData) :
    corpus = makeCorpus(chatDoc, spotsData)
    vectorizer = TfidfVectorizer(token_pattern='\\b\\w+\\b')
    x = vectorizer.fit_transform(corpus)
    words = vectorizer.get_feature_names()
    tfids = x.toarray()
    points = [0 for _ in range(len(corpus))]
    for w in corpus[0].split(' '):
        for i, t in enumerate(corpus):
            points[i] += t.count(w) * tfids[0, words.index(w)]
    points = points[1:]
    sorted_points = sorted(enumerate(points), key=lambda x: x[1], reverse=True)
    sorted_index  = [*map(lambda x: x[0], sorted_points)]
    out = []
    for i in sorted_index:
        out.append( spotsData[i] )
    return out

def makeCorpus(chatDoc, spotsData) :
    baseText = parseDoc(chatDoc)
    texts    = [*map(lambda x: parseDoc(x['description']), spotsData)]
    texts.insert(0, baseText)
    return texts


def parseDoc(text):
    """
    # 文書の整形
    英語(大文字のみ)、数字、空白のみ通す
    """
    out = re.sub('[^A-Za-z\s0-9]', ' ', text)
    out = out.lower()
    out = ' '.join(out.split())
    return out
