import pickle
import streamlit as st
import requests


def recommend(movie):
    index = movies_dataset[movies_dataset['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:6]:
        a = (movies_dataset.iloc[i[0]].title)
        print(a)



st.header('Movie Recommender System')
movies_dataset = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies_dataset['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    a = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:
        st.text(a[0])

    with col2:
        st.text(a[1])


    with col3:
        st.text(a[2])

    with col4:
        st.text(a[3])

    with col5:
        st.text(a[4])

