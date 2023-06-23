import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Load the CSV file and read the column of rationales
csv_file_path = r'C:\Users\Karthik\OneDrive\Documents\GitHub\NLPStuff\output_1.csv'
column_of_rationales = 'OUTPUT:rationale_5_original'
data = pd.read_csv(csv_file_path)
data[column_of_rationales].fillna('', inplace=True)  # Replace NaN values with an empty string
rationales = data[column_of_rationales].tolist()

# Create an n-gram vectorizer
n = 2  # Change the value of n for different n-gram sizes
vectorizer = CountVectorizer(ngram_range=(n, n), stop_words='english')

# Generate n-gram matrix
ngram_matrix = vectorizer.fit_transform(rationales)

# Get the feature names (n-grams)
feature_names = vectorizer.get_feature_names_out()

# Calculate the total count of each n-gram
ngram_counts = ngram_matrix.sum(axis=0).A1

# Create a dictionary of n-grams and their counts
ngram_frequency = dict(zip(feature_names, ngram_counts))

# Sort the n-grams by their counts in descending order
sorted_ngrams = sorted(ngram_frequency.items(), key=lambda x: x[1], reverse=True)

# custom_stopwords = ['author zoe4123190', 'jan', 'kendall', 'output', 'rationale_5_original']  # Add your custom stop words here
# stopwords = set(STOPWORDS).union(set(custom_stopwords))
#
# # Generate the word cloud
# wordcloud = WordCloud(width=800, height=400, background_color='white', stopwords=stopwords).generate_from_frequencies(ngram_frequency)
#
#
# # Display the word cloud
# plt.figure(figsize=(10, 5))
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis('off')
#
# # Save the word cloud as an image file
# output_file_path = 'wordcloud_rat5_orig.png'
# wordcloud.to_file(output_file_path)
# print(f"Word cloud saved as {output_file_path}")
print(sorted_ngrams)
