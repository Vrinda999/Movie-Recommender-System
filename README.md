# Movie-Recommender-System
Made using Jupyter and PyCharm.


## Jupyter
### Installing the necessary Libraries.
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
## Getting Dataset
The dataset for this Project is taken from [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).
It has TMDB movie Metadata.

## Explanation of the Code
Firstly, we upload the downloaded dataset to our jupyter notebook.
We then make two variables called _movies_ and _credits_ and load the respective datasets into these variables using the Pandas library functions.
We then merge All our data into a single CSV (the _"movies"_ csv).

### Pre-processing of Data
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

### Formatting Our Data
This is where we will format our data (a list of dictionaries) into a desired and readable format.
The function ```Convert()``` helps us achieve this task for the coloumns _Genres_ and _Keywords_.
The function ```ConvertforCast()``` returns a similar output for the _"Cast"_ coloumnm.

We then concatenate all these coloumns together into a single coloumn (called "Tags") and perform stemming on them to ensure that duplicate or similar words like "Dance", "Dancing", "Dances" are all converted to their root form i.e. "Danc" to avoid redundancy in tags.
To perform stemming, we use the [***nltk*** library](https://www.nltk.org/howto/stem.html).

We then use the **CountVectorizer** function from the [***sklearn*** library](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html). It converts a collection of text documents to a matrix of token counts. This implementation produces a sparse representation of the counts. 

We then use **Cosine Similarity** Function from the [***sklearn*** library](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html) to compute and store similarity as the normalized dot product of the two entities a into a variable called "Similarity", which is a 4806 x 4806 matrix which stores the similarity index of each movie with every other movie.

### Final Function
After finally getting all our data ready, we create a function called ```Recommend(selected_movie)``` to find out the top 5 movies similar to the selected_movie on the basis of their Cosine Similarities as stores in the variable "Similarity".

This is how the Results are Displayed:


https://github.com/Vrinda999/Movie-Recommender-System/assets/98251856/489a26a1-12df-4015-8d40-f21224a032c4


Inspiration taken from: CampusX (youtube).
