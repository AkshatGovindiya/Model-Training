import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# Loading the saved model
diabetes_model = pickle.load(open(f'{working_dir}/diabetes_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    st.title("Health Assistant")
    selected = option_menu('Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Title of the selected page
st.title(selected)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    # Instructions
    st.markdown("""
        Please fill in the details below to predict diabetes risk. 
        All fields are required for accurate predictions.
    """)

    # Getting the input data from the user with improved layout
    form = st.form(key='diabetes_form')
    col1, col2, col3 = form.columns(3)

    with col1:
        Pregnancies = form.number_input('Number of Pregnancies', min_value=0, step=1)

    with col2:
        Glucose = form.number_input('Glucose Level', min_value=0.0, step=0.1)

    with col3:
        BloodPressure = form.number_input('Blood Pressure value', min_value=0.0, step=0.1)

    with col1:
        SkinThickness = form.number_input('Skin Thickness value', min_value=0.0, step=0.1)

    with col2:
        Insulin = form.number_input('Insulin Level', min_value=0.0, step=0.1)

    with col3:
        BMI = form.number_input('BMI value', min_value=0.0, step=0.1)

    with col1:
        DiabetesPedigreeFunction = form.number_input('Diabetes Pedigree Function value', min_value=0.0, step=0.01)

    with col2:
        Age = form.number_input('Age of the Person', min_value=0, step=1)

    # Creating a button for Prediction
    submit_button = form.form_submit_button(label='Get Diabetes Test Result')

    # Code for Prediction
    if submit_button:
        # Check if any input is missing
        if (Pregnancies is None or Glucose is None or BloodPressure is None or
                SkinThickness is None or Insulin is None or BMI is None or
                DiabetesPedigreeFunction is None or Age is None):
            st.error("Please fill in all fields.")
        else:
            user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                          BMI, DiabetesPedigreeFunction, Age]

            user_input = [float(x) for x in user_input]

            # Predicting using the loaded model
            diab_prediction = diabetes_model.predict([user_input])

            if diab_prediction[0] == 1:
                st.success('The person is diabetic.')
            else:
                st.success('The person is not diabetic.')

# Footer
st.markdown("<footer style='text-align: center; padding: 10px;'><strong>Created by Akshat Gajjar</strong></footer>", unsafe_allow_html=True)

# Add some custom CSS for better styling
st.markdown("""
    <style>
    footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)
