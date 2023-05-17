import streamlit as st
import pickle
import pandas as pd
import requests

#import the dictionary and make dataframe here
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=3d700b3a5362f3fedc9be1bca7abfd9f&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+ data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    recommend_posters = []
    for i in movies_list:
       #movies_list has two keys, index and match point. index will be our movie id
        movie_id = movies.iloc[i[0]].movie_id
        #fetch poster from api
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_posters.append(fetch_poster(movie_id))
    return recommend_movies, recommend_posters

st.set_page_config(page_title="Zul's Movie Recommender", page_icon='🎦', layout="wide", initial_sidebar_state="auto", menu_items=None)
st.title('Movie Recommending System')

selected_movie = st.selectbox(
    'Please type your desired movie name',
    movies['title'].values)

st.write('We are looking for recommendations based on your movie: ', selected_movie)

if st.button('Ask for recommendations'):
    names, posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5, gap='small')

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])


