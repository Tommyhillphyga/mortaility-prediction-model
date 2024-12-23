import streamlit as st
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker

from PIL import Image
from utils import feature_list, feature_map

import pickle
import numpy as np
import base64

DATABASE_URL = 'sqlite:///database.db'
engine = create_engine( DATABASE_URL )

metadata = MetaData()
metadata.bind = engine

user_table = Table("users", metadata, autoload_with=engine)

#start local session
SessionLocal = sessionmaker(bind=engine)


# Load the model from the file
with open('mortality_prediction_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Function to make predictions
def predict(features):
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)
    return int(prediction[0])

def check_user (username, password):
    session = SessionLocal()
    user = session.query(user_table).filter_by(username=username, password=password).first()
    session.close()
    return user

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'username' not in st.session_state:
    st.session_state.username = ''

def login_page ():
    
    st.title('Login to the Mortality Prediction System')
    username = st.text_input('Username')
    password = st.text_input('Password', type= 'password')
   
    if st.button('Login'):
        user = check_user(username, password)

        if user:
            st.session_state.logged_in = True
            st.session_state.username  = username 
             # st.success('Logged in as {}'.format(user.username))
            st.experimental_rerun()
    
        else: 
            st.error('Incorrect username or password')

def prediction_page():             
    
    features = feature_list
    feat_map = feature_map
    st.title("Mortality Prediction System")
    st.write("This system predicts the mortality of patients based on their medical history.")
    st.write("Please enter the patient's information below:")
   
     # Input features
    feature_inputs = []
    for feat in features:
        col1, col2 = st.columns([0.1, 0.9]) 
        with col1:
            st.title(":notebook_with_decorative_cover:")
        with col2:
            feature_input = st.number_input(f"{feat}", min_value = 0.0, placeholder = f"{feat_map[feat]}")
            feature_inputs.append(feature_input)

    # Prediction button
    if st.button("Predict"):

        prediction = predict(feature_inputs)
        if prediction == 0:  # Assuming 0 represents 'alive' and 1 represents 'death'
            st.text_area("Prediction based on data provided","Based on the analysis, it appears that the patient is likely to have a positive outcome.")
        elif prediction == 1:
            st.text_area("Prediction based on data provided", "Based on the analysis, there are significant health risks that need to be addressed. \
                     We recommend discussing these findings with your healthcare provider to explore all possible options and next steps.")

        


def main():
    if st.session_state.logged_in:
        prediction_page()

    else:
        login_page()

if __name__ == "__main__" :
    main()
