import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = {
    'Title': ['Book A', 'Book B', 'Book C', 'Book D', 'Book E'],
    'Author': ['Author 1', 'Author 2', 'Author 3', 'Author 1', 'Author 2'],
    'Genre': ['Fiction', 'Mystery', 'Fiction', 'Sci-Fi', 'Mystery'],
    'Description': [
        'A great fictional story with adventure',
        'A mystery book full of suspense',
        'An amazing fictional drama',
        'A science fiction book with space adventure',
        'A detective solving a thrilling case'
    ]
}
df = pd.DataFrame(data)

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['Genre'] + ' ' + df['Description'])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommend_book(title, df, cosine_sim):
    idx = df.index[df['Title'] == title][0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]  # Get top 3 recommendations
    book_indices = [i[0] for i in sim_scores]
    return df['Title'].iloc[book_indices]

# Example Usage
print(recommend_book('Book A', df, cosine_sim))
