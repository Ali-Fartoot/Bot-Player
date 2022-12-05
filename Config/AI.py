import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
import pandas as pd
import numpy as np


class AI:
    def __init__(self, address):
        self.address = address
        self.data = pd.read_csv(self.address)

    # Get ID By Name
    def GetIDByName(self, name):
        temp = self.data.loc[self.data['title'] == name]
        return temp.iloc[0, 13]

    def RecommenderOne(self, ):
        temp = self.data.sort_values(by=['score'], ascending=False)
        rands = random.sample(range(50), 5)
        return {temp.iloc[rands[i], 3]: "https://www.imdb.com/title/" + str(
            self.GetIDByName(name=temp.iloc[rands[i], 3]) + "/") for i in range(5)}

    def RecommenderTwo(self, title):
        # Define a TF-IDF Vectorizer Object. Remove all english stopwords
        tfidf = TfidfVectorizer(stop_words='english')

        # Replace NaN with an empty string
        self.data['overview'] = self.data['overview'].fillna('')

        # Construct the required TF-IDF matrix by applying the fit_transform method on the overview feature
        tfidf_matrix = tfidf.fit_transform(self.data['overview'])
        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

        indices = pd.Series(self.data.index, index=self.data['title']).drop_duplicates()

        # Obtain the index of the movie that matches the title
        idx = indices[title]

        # Get the pairwsie similarity scores of all movies with that movie
        # And convert it into a list of tuples as described above
        sim_scores = list(enumerate(cosine_sim[idx]))

        # Sort the movies based on the cosine similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the 10 most similar movies. Ignore the first movie.
        sim_scores = sim_scores[1:11]

        # Get the movie indices
        movie_indices = [i[0] for i in sim_scores]

        # Return the top 10 most similar movies
        temp = list(set(self.data['title'].iloc[movie_indices]))

        return {temp[i]: "https://www.imdb.com/title/" + str(self.GetIDByName(name=temp[i]) + "/") for i in range(5)}

    def RecommenderThree(self, title):
        count = CountVectorizer(stop_words='english')
        count_matrix = count.fit_transform(self.data['soup'])
        cosine_sim = cosine_similarity(count_matrix, count_matrix)

        indices = pd.Series(self.data.index, index=self.data['title'])

        # Obtain the index of the movie that matches the title
        idx = indices[title]

        # Get the pairwsie similarity scores of all movies with that movie
        # And convert it into a list of tuples as described above
        sim_scores = list(enumerate(cosine_sim[idx]))

        # Sort the movies based on the cosine similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the 10 most similar movies. Ignore the first movie.
        sim_scores = sim_scores[1:11]

        # Get the movie indices
        movie_indices = [i[0] for i in sim_scores]

        # Return the top 10 most similar movies
        temp = list(set(self.data['title'].iloc[movie_indices]))

        return {temp[i]: "https://www.imdb.com/title/" + str(self.GetIDByName(name=temp[i]) + "/") for i in range(5)}
