# Predia: A diabetes prediction website
This is a machine learning model developed to predict or diagnose diabetes based on patient's physiological data. 
## About
The model is a classification model that categorizes results generated after analysing the features into three cateories:
1. Y, Diabetic
2. P, Prediabetic
3. N, Not diabetic
## Dataset
The data was gotten from [kaggle](https://www.kaggle.com/datasets/marshalpatel3558/diabetes-prediction-dataset-legit-dataset)
## Methodology
### Data Preprocessing
1. Handling missing values
2. Removing outliers
3. Splitting data into train/test sets
### Feature Engineering
Label encoding
### Model Development
1. Applied machine learning models (Logistic regression and Catboost
2. Performance evaluation (accuracy, precision, recall, F1-score, ROC-AUC)
### Deployment
Interactive prediction app using [Streamlit](https://diabetes-prediction-st.streamlit.app/)

## How to Run Locally
1. Clone the repository
`git clone https://github.com/Olaoti/diabetes-prediction.git`
`cd diabetes-prediction`
2. Install dependencies
   `pip install -r requirements.txt`
3. Run the Streamlit app
   `streamlit run app.py`
## Key Features
1. Predicts diabetes with up to 99% accuracy
2. Easy-to-use web interface
3. Transparent methodology with reproducible results
