import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download("punkt")
nltk.download("stopwords")

def preprocess_text(text):
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words("english"))

    words = []
    for sentence in sentences:
        words.extend(word_tokenize(sentence.lower()))

    words = [word for word in words if word.isalnum() and word not in stop_words]
    words=" ".join(words)
    return sentences, words


text = """There are many techniques available to generate extractive summarization to keep it simple, I will be using an unsupervised learning approach to find the sentences similarity and rank them. Summarization can be defined as a task of producing a concise and fluent summary while preserving key information and overall meaning. One benefit of this will be, you don’t need to train and build a model prior start using it for your project. It’s good to understand Cosine similarity to make the best use of the code you are going to see. Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space that measures the cosine of the angle between them. Its measures cosine of the angle between vectors. The angle will be 0 if sentences are similar.
"""

sentences, words = preprocess_text(text)

print("Original Sentences:")
for sentence in sentences:
    print(sentence)

print("\nPreprocessed Words:")
print(words)
print(f"\n\n{len(words.split(' '))/len(text.split(' '))*100}")
