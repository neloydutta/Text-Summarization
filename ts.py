import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize


def summarize(file_location):
    doc = open(file_location, "r")
    text = doc.read()
    words = word_tokenize(text, language='english')
    sentences = sent_tokenize(text, language='english')
    stop = " ".join(stopwords.words('english')).encode('ascii')
    stop = word_tokenize(stop, language='english')
    words = [w for w in words if w not in stop and w not in string.punctuation]
    graph = []
    for i in range(len(sentences)):
        graph.append([])
        sent_words_i = word_tokenize(sentences[i], language='english')
        for j in range(len(sentences)):
            graph[i].append(0)
            if i == j:
                continue
            for word in sent_words_i:
                if word in sentences[j] and word in words:
                    graph[i][j] += 1
    rank = []
    count = 0
    for i in range(len(sentences)):
        rank.append(0)
        for j in range(len(sentences)):
            if graph[i][j] != 0:
                rank[i] += graph[i][j]
        if rank[i] >= 2:
            count += 1
    if count >= 0.7 * len(sentences):
        for i in range(len(sentences)):
            if rank[i] >= 2:
                print sentences[i]
    else:
        for i in range(len(sentences)):
            print sentences[i]


if __name__ == "__main__":
    summarize('file.txt')
