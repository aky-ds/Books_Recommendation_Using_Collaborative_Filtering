import streamlit as st
import pickle
import numpy as np
# Loading the model

with open('Similarity_score.pkl','rb') as x:
    similarity=pickle.load(x)
    x.close()

# Loading the pivot

with open('pivot.pkl','rb') as x:
    pt=pickle.load(x)
    x.close()

# Creating a title

st.title('Book Recommendation using Collaborative Filtering')


# Creating an input

book_name=st.text_input('Enter the book name')


if st.button('Recommend'):
    index = np.where(pt.index == book_name)[0][0]

    # Find the most similar books to the given book
    similar_books = sorted(list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True)[1:6]
    st.write('The Recommended Books are:')
    # Print the recommended books
    for book_index, _ in similar_books:  # unpack the tuple (index, similarity)
        st.write(f'*{pt.index[book_index]}')