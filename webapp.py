
import streamlit as st
import pandas as pd
import joblib

# city                                     city_149
# city_development_index                      0.689
# gender                                       Male
# relevent_experience       Has relevent experience
# enrolled_university                 no_enrollment
# education_level                          Graduate
# major_discipline                             STEM
# experience                                      3
# company_size                              100-500
# company_type                              Pvt Ltd
# last_new_job                                    1
# training_hours                                106


st.title('Job change prediction')

#read the dataset to fill the values in the drop down list
df = pd.read_csv('train_jqd04QH.csv')

#create the input fields
city = st.selectbox("city", pd.unique(df['city']))
city_development_index = st.number_input("city_development_index")
gender = st.selectbox("gender", pd.unique(df['gender']))
relevent_experience = st.selectbox("relevent_experience", pd.unique(df['relevent_experience']))
enrolled_university = st.selectbox("enrolled_university", pd.unique(df['enrolled_university']))
education_level = st.selectbox("education_level", pd.unique(df['education_level']))
major_discipline = st.selectbox("major_discipline", pd.unique(df['major_discipline']))
experience = st.selectbox("experience", pd.unique(df['experience']))
company_size = st.selectbox("company_size", pd.unique(df['company_size']))
company_type = st.selectbox("company_type", pd.unique(df['company_type']))
last_new_job = st.selectbox("last_new_job", pd.unique(df['last_new_job']))
training_hours = st.number_input("training_hours")


#convert the input values into a dictionary
inputs = {
"city": city,
"city_development_index": city_development_index,
"gender": gender,
"relevent_experience": relevent_experience,
"enrolled_university": enrolled_university,
"education_level": education_level,
"major_discipline": major_discipline,
"experience": experience,
"company_size": company_size,
"company_type": company_type,
"last_new_job": last_new_job,
"training_hours": training_hours
}


#Click for prediction (prediction button)

if st.button("Predict"):
    model = joblib.load("jobchg_pipeline_model.pkl")
    #input to the fields
    X_input = pd.DataFrame(inputs, index=[0])
    #model prediction
    prediction = model.predict(X_input)
    #display the prediction
    st.write(prediction)
