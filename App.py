import streamlit as st
import pickle
import pandas as pd
import requests
st.set_page_config(layout="wide")
movie_dict = pickle.load(open('MovieDict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

def fetch_poster(movie_id):
    # TMDB API for Movie Details to get the poster Path.
    # https: // api.themoviedb.org / 3 / movie / 550?api_key = db0bb8f8930e1530880e5a83b965d28d
    response = requests.get("https://api.themoviedb.org/3/movie/" + str(movie_id) + "?api_key=db0bb8f8930e1530880e5a83b965d28d")
    data = response.json()

    # print(data)
    # TMDB Image Path
    return "https://image.tmdb.org/t/p/w500" + data["poster_path"]
def recommend(movie_name):
    # To Find out the Index of the Movie so that we can find the Similarity index
    # from Vectors and proceed to recommend movies.
    movie_index = movies[movies['title'] == movie_name].index[0]
    dists = similarity[movie_index]

    # Recommending 5 Movies
    movies_list = sorted(list(enumerate(dists)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


st.title("Movie Recommender System")
option = st.selectbox("Select a Movie: ", movies['title'].values)

if st.button("Recommend"):
    names, posters = recommend(option)
    st.write("Top 5 Recommendations are: ")

    col1, col2, col3, col4, col5 = st.columns(5)

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