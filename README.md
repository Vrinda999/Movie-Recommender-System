# Movie-Recommender-System
Made using Jupyter and PyCharm.

## Jupyter
### 1. Installing the necessary Libraries.
To install jupyter, you need to have Python installed in your device.
Then, type the following in your CLC or Terminal:
```
pip install jupyterlab
pip install jupyter-notebook
```
To open a Jupyter Notebook, type:
```
jupyter notebook
```
We require certain Libraries in our project. The Command to install those are:
```
pip install numpy
pip install pandas
pip install ast
pip install sklearn
pip install nltk
pip install pickle
```
### 2. Getting Dataset
The dataset for this Project is taken from [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).
It has TMDB movie Metadata.

### 3. Explanation of the Code
Firstly, we upload the downloaded dataset to our jupyter notebook.
We then make two variables called _movies_ and _credits_ and load the respective datasets into these variables using the Pandas library functions.
We then merge All our data into a single CSV (the _"movies"_ csv).

### 4. Pre-processing of Data
1. Remove unnecessary coloumns and keep only the ones which we require in our filtering process.
   We keep the folowwing coloumns:
   + Genres
   + ID
   + Keywords
   + Title
   + Overview
   + Cast
   + Crew

2. Remove rows which have some missing data (In our case, 3 Rows did not have _"Overview"_.
3. Remove Duplicates, if any.

### 5. Formatting Our Data
This is where we will format our data (a list of dictionaries) into a desired and readable format.
The function ```Convert()``` helps us achieve this task for the coloumns _Genres_ and _Keywords_.
The function ```ConvertforCast()``` returns a similar output for the _"Cast"_ coloumnm.

We then concatenate all these coloumns together into a single coloumn (called "Tags") and perform stemming on them to ensure that duplicate or similar words like "Dance", "Dancing", "Dances" are all converted to their root form i.e. "Danc" to avoid redundancy in tags.
To perform stemming, we use the [***nltk*** library](https://www.nltk.org/howto/stem.html).

We then use the **CountVectorizer** function from the [***sklearn*** library](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html). It converts a collection of text documents to a matrix of token counts. This implementation produces a sparse representation of the counts. 

We then use **Cosine Similarity** Function from the [***sklearn*** library](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html) to compute and store similarity as the normalized dot product of the two entities a into a variable called "Similarity", which is a 4806 x 4806 matrix which stores the similarity index of each movie with every other movie.

### 6. Final Function
After finally getting all our data ready, we create a function called ```Recommend(selected_movie)``` to find out the top 5 movies similar to the selected_movie on the basis of their Cosine Similarities as stores in the variable "Similarity".

### 7. Result
This is how the Results are Displayed:


https://github.com/Vrinda999/Movie-Recommender-System/assets/98251856/489a26a1-12df-4015-8d40-f21224a032c4

___________________________________________________________________________________________________________________________________________________________________________________________________________________

## Exporting the Processed data for the Website
in your jupyter notebook, use Pickle library to dump ```.pkl``` files of the data in our device.
```
pickle.dump(new_df.to_dict(), open('MovieDict.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))
```
___________________________________________________________________________________________________________________________________________________________________________________________________________________

## Setting up a Website in PyCharm
### 1. Downloading PyCharm
Download the .exe for Pycharm for [Windows](https://www.jetbrains.com/pycharm/download/?section=windows), [Linux](https://www.jetbrains.com/pycharm/download/?section=linux), [MacOS](https://www.jetbrains.com/pycharm/download/?section=mac).

From here, we can now Launch Pycharm and Start a New Project by setting up a New Virtual Environment in our Desired Folder. In this new Project, we will create a Python File. 

### 2. Installing Libraries
We require certain Libraries in our project. The Command to install those are:
```
pip install streamlit as st
pip install pandas as pd
pip install pickle
pip install requests
```
Also, we need to paste the ```.pkl``` files to our Folder where this Project is saved.
### 3. Functions.
1. Recommend(): Same as that in the Jupyter notebook, we have just changed the variable names since we have stored our data into different variables and formats.
2. FetchPoster(): This function uses [TMDb API to fetch Details of a Movie whose movie_id is given](https://developer.themoviedb.org/reference/movie-details). To access this, we need to Sign up on TMDb and [request for an API Key](https://www.themoviedb.org/settings/api).

   This API Key and the movie_id are then used as inputs in the TMDb Image Path to access the Poster of a given movie as follows:
   ```
   https://api.themoviedb.org/3/movie/{MOVIE_ID}?api_key={API Key}
   ```
This function returns the Poster_path for the Movie.

### 4. Setting up of the Streamlit Website
We use functions available in [Streamlit Library](https://docs.streamlit.io/library/api-reference) to set up basic entities like Text, Headers, Buttons, Drop-Down Menus etc.
To Run the app, we write the following code in PyCharm Terminal:
```
streamlit run {File Name}.py                                    # "App.py" in this case
```

### 5. Result
This is how the Streamlit app looks like:


https://github.com/Vrinda999/Movie-Recommender-System/assets/98251856/81643e9c-7150-40e0-be81-d11b2530ea14
