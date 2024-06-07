# Real-Estate Application - Gurgaon
The app can be visited here : https://real-estate-gurgaon.streamlit.app/

Collected datasets from Kaggle and a few GitHub repositories - flats-flats.csv, apartments.csv

Perfomed proper Data Cleaning and Feature Engineering - cleaned.csv, next.csv files are improved versions of flats-flats.csv file

Perfomed Exploratory Data Analysis and drew valuable insights about the data, also got an idea about the important features affecting price - Notebook 1

For better understanding, perfomed Feature Selection techniques and kept only the relevant columns for final model training - Notebook2

Got best results after hyperparameter tuning using optuna for the algorithm XGBoost, made a pipeline for model tuning

With the model ready, I went on to built the 3 modules of my application-

1.Price Predictor -  using my pipeline.pkl file mainly

2. Analytics- Perfomed Data Analysis on the cleaned files and plotted relevant visualisations on the webpage
3. 
4. Recommender - Using Location, Price and Facilities as the base, created a recommender system which recommends top 5 related properties


