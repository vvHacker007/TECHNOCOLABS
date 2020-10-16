import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


st.markdown("<h1 style='text-align: center; color: #FF3342;'><strong><u>Predict Blood Donation for Future Expectancy</u></strong></h1>", unsafe_allow_html=True)

st.sidebar.markdown("<h1 style='text-align: center; color:#FF3342 ;'><strong><u>Specify Input Parameters</u></strong></h1>", unsafe_allow_html=True)
    
st.markdown("Forecasting blood supply is a serious and recurrent problem for blood collection managers: in January 2019, Nationwide, the Red Cross saw 27,000 fewer blood donations over the holidays than they see at other times of the year. Machine learning can be used to learn the patterns in the data to help to predict future blood donations and therefore save more lives.")
st.markdown("Understanding the Parameters -")
st.markdown("(Recency - months since the last donation)")
st.markdown("(Frequency - total number of donation)")
st.markdown("(Monetary - total blood donated in c.c.)")
st.markdown("(Time - months since the first donation)")
st.markdown("Target - (1 stands for donating blood, 0 stands for not donating blood)")




def user_input_features():
     Recency  = st.sidebar.slider('Recency', 0, 74)
     Frequency= st.sidebar.slider('Frequency', 1,43)
     Monetary = st.sidebar.slider('Monetary', 250,12500)
     Time = st.sidebar.slider('Time', 2,98)
     
     data = {'Recency (months)': Recency  ,
           'Frequency (times)': Frequency,
           'Monetary (c.c. blood)': Monetary,
           'Time (months)':Time}
           
           
     features = pd.DataFrame(data, index=[0])
     return features

df = user_input_features()

st.write(df)

trans = pd.read_csv('transfusion.csv')

X_train,X_test,y_train,y_test = train_test_split(trans.drop(columns=['target']), trans['target'].values,test_size=0.2, random_state=24)

clf = LogisticRegression()
clf.fit(X_train, y_train)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)



st.subheader('Prediction')
st.write(trans.target[prediction])

st.subheader('Prediction Probability')
st.write(prediction_proba)


st.markdown("For issues Contact - im.vedanshvijay2002@gmail.com")