import streamlit as st
import pickle
import pandas as pd
import plotly.graph_objects as go

# List of teams and cities
teams = ['Rajasthan Royals', 'Sunrisers Hyderabad', 'Mumbai Indians',
         'Kolkata Knight Riders', 'Chennai Super Kings',
         'Royal Challengers Bangalore', 'Punjab Kings', 'Delhi Capitals',
         'Lucknow Super Giants', 'Gujarat Titans']

cities = ['Jaipur', 'Chennai', 'Chandigarh', 'Bangalore', 'Mumbai', 'Delhi',
          'Hyderabad', 'Durban', 'Cape Town', 'Dubai', 'Pune', 'Cuttack',
          'Lucknow', 'Kolkata', 'Dharamsala', 'Ranchi', 'Centurion',
          'Abu Dhabi', 'Ahmedabad', 'Nagpur', 'Visakhapatnam',
          'Port Elizabeth', 'East London', 'Sharjah', 'Johannesburg',
          'Guwahati', 'Kimberley', 'Indore', 'Bloemfontein', 'Raipur']

# Load the model
pipe = pickle.load(open('pipe.pkl', 'rb'))

# App title
st.markdown(
    """
    <div style="background: linear-gradient(to right, #C33764, #1D2671);padding:10px;border-radius:10px;display:flex;align-items:center;">
        <img src="https://www.vhv.rs/file/max/29/294049_ipl-logo-png.png" alt="IPL Logo" style="width:auto;height:90px;transform: translateX(85px);
;">
        <h1 style="color:white;text-align:center;margin-left:100px;">IPL Win Predictor</h1>
    </div>
    """, unsafe_allow_html=True
)

# Team and city selection
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select the bowling team', sorted(teams))
    
#_______________________________dinamic logo____________________________________
team_logos = {
    'Rajasthan Royals': 'https://upload.wikimedia.org/wikipedia/hi/thumb/6/60/Rajasthan_Royals_Logo.svg/640px-Rajasthan_Royals_Logo.svg.png',
    'Sunrisers Hyderabad': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSIcY1qYfs9AvTK_DootPjsAXT4RgtsAwElaQ&s',
    'Mumbai Indians': 'https://upload.wikimedia.org/wikipedia/en/thumb/c/cd/Mumbai_Indians_Logo.svg/1200px-Mumbai_Indians_Logo.svg.png',
    'Kolkata Knight Riders':'https://upload.wikimedia.org/wikipedia/en/thumb/4/4c/Kolkata_Knight_Riders_Logo.svg/1200px-Kolkata_Knight_Riders_Logo.svg.png',
    'Chennai Super Kings':'https://upload.wikimedia.org/wikipedia/en/thumb/2/2b/Chennai_Super_Kings_Logo.svg/1200px-Chennai_Super_Kings_Logo.svg.png',
    'Royal Challengers Bangalore':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTY2us7wrfWxPr0yp0iVNgx3ihYpm2-qUe5A&s',
    'Punjab Kings':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDo_H7vOrQ-9ueb6BbjhXRVb2-g3946Nm36Q&s', 
    'Delhi Capitals':'https://upload.wikimedia.org/wikipedia/en/thumb/2/2f/Delhi_Capitals.svg/1200px-Delhi_Capitals.svg.png',
    'Lucknow Super Giants':'https://upload.wikimedia.org/wikipedia/en/thumb/a/a9/Lucknow_Super_Giants_IPL_Logo.svg/290px-Lucknow_Super_Giants_IPL_Logo.svg.png', 
    'Gujarat Titans':'https://upload.wikimedia.org/wikipedia/en/thumb/0/09/Gujarat_Titans_Logo.svg/1200px-Gujarat_Titans_Logo.svg.png'
}

# App title with dynamic logos
st.markdown(
    """
    <div style="display: flex; align-items: center; justify-content: center;">
        <div style="margin-right: 10px;">
            <img src="{}" alt="Batting Team Logo" style="width: auto; height: 65px;">
        </div>
        <h1 style="color: royalblue; text-align: center;">- - - -𝕧𝕤- - - -</h1>
        <div style="margin-left: -18px;">
            <img src="{}" alt="Bowling Team Logo" style="width: auto; height: 65px;">
        </div>
    </div>
    """.format(
        team_logos.get(batting_team, ''),
        team_logos.get(bowling_team, '')
    ),
    unsafe_allow_html=True
)
#_______________________________________________________________________________

selected_city = st.selectbox('Select host city', sorted(cities))

# Target and match status input
target = st.number_input('Target', min_value=0, format="%d")

col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input('Score', min_value=0, format="%d")
with col4:
    overs = st.number_input('Overs completed', min_value=0, step=1, format="%d")
with col5:
    wickets = st.number_input('Wickets out', min_value=0, max_value=10, step=1, format="%d")

# Prediction button and result display
if st.button('Predict Probability'):
    if batting_team == bowling_team:
        st.markdown(
            """
            <div style="background-color:#FF5722;padding:10px;border-radius:10px;text-align:center;">
                <h2 style="color:white;">Are you serious?</h2>
            </div>
            """, unsafe_allow_html=True
        )
    elif target == 0:
        st.markdown(
            """
            <div style="background-color:#FF5722;padding:10px;border-radius:10px;text-align:center;">
                <h2 style="color:white;">Come on, try putting some target, dude</h2>
            </div>
            """, unsafe_allow_html=True
        )
    elif target >299:
         st.markdown(
             """
            <div style="background-color:#FF5722;padding:10px;border-radius:10px;text-align:center;">
                <h2 style="color:white;">⚠️ Hold on! That's a massive target bruhh !</h2>
            </div>
            """, unsafe_allow_html=True
         )
    else:
        runs_left = target - score
        balls_left = 120 - (overs * 6)
        wickets_left = 10 - wickets
        crr = score / overs if overs > 0 else 0
        rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [selected_city],
            'runs_left': [runs_left],
            'balls_left': [balls_left],
            'wickets': [wickets_left],
            'total_runs_x': [target],
            'crr': [crr],
            'rrr': [rrr]
        })

        result = pipe.predict_proba(input_df)
        loss = result[0][0]
        win = result[0][1]

        # Display probabilities as headers
        st.header(batting_team + " - " + str(round(win * 100)) + "%")
        st.header(bowling_team + " - " + str(round(loss * 100)) + "%")

        # Create horizontal bar with Plotly
        fig = go.Figure()

        fig.add_trace(go.Bar(
            y=['Win Probability'],
            x=[win * 100],
            name=batting_team,
            orientation='h',
            marker=dict(color='royalblue'),
            text=str(round(win * 100)) + '%',
            textposition='inside',
            insidetextanchor='end'
        ))

        fig.add_trace(go.Bar(
            y=['Win Probability'],
            x=[loss * 100],
            name=bowling_team,
            orientation='h',
            marker=dict(color='red'),
            text=str(round(loss * 100)) + '%',
            textposition='inside',
            insidetextanchor='start'
        ))

        fig.update_layout(
            barmode='stack',
            title='',
            xaxis=dict(
                title='',
                range=[0, 100],
                showticklabels=False 
            ),
            yaxis=dict(
                showticklabels=False
            ),
            showlegend=False,
            height=200
        )

        st.plotly_chart(fig)
#footer

st.markdown(
    """
    <div style="background:linear-gradient(to right, #355C7D, #6C5B7B,#C06C84) ; padding: 10px; border-radius: 10px; text-align: center; margin-top: 20px;">
        <p style="margin: 0;">Developed by Jyotirmaya Maharana</p>
        <p style="margin: 0;">jyotirmayamahara16@gmail.com</p>
    </div>
    """, unsafe_allow_html=True
)
        


