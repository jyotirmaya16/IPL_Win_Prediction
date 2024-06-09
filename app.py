import streamlit as st
import pickle
import pandas as pd

teams = ['Royal Challengers Bangalore',
 'Punjab Kings',
 'Mumbai Indians',
 'Kolkata Knight Riders',
 'Rajasthan Royals',
 'Chennai Super Kings',
 'Sunrisers Hyderabad',
 'Delhi Capitals',
 'Lucknow Super Giants',
 'Gujarat Titans']

cities = ['Ahmedabad', 'Delhi', 'Bangalore', 'Kolkata', 'Mumbai', 'Chennai',
       'Hyderabad', 'Chandigarh', 'Lucknow', 'Cuttack', 'Visakhapatnam',
       'Abu Dhabi', 'Jaipur', 'Cape Town', 'Raipur', 'Johannesburg',
       'Centurion', 'Durban', 'Dubai', 'Sharjah', 'East London',
       'Dharamsala', 'Port Elizabeth', 'Pune', 'Ranchi', 'Indore',
       'Kimberley', 'Nagpur', 'Guwahati', 'Bloemfontein']

pipe = pickle.load(open('pipe.pkl','rb'))
st.title('IPL Win Predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Select the bowling team',sorted(teams))

selected_city = st.selectbox('Select host city',sorted(cities))

target = st.number_input('Target')

col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input('Score')
with col4: 
    overs = st.number_input('Overs completed')
with col5:
    wickets = st.number_input('Wickets out')

if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 - (overs*6) 
    wicket = 10 - wickets 
    crr = score/overs 
    rrr = (runs_left*6)/balls_left

    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'wicket':[wicket],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})


    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + "- " + str(round(win*100)) + "%")
    st.header(bowling_team + "- " + str(round(loss*100)) + "%") 