# IPL Win Prediction App
### Preview 
#### Link to site: [click her👆🏻](https://ipl-win-prediction-by-jyotirmaya.streamlit.app/) 
![ipl](https://github.com/jyotirmaya16/IPL_Win_Prediction/assets/146333462/23e7eec2-2e8d-4feb-8c0c-74cea5e4b916)
## Overview
I have developed an end-to-end Python application that predicts which IPL team is likely to win the match. This app utilizes 2008-2023 IPL data and machine learning techniques to generate its predictions.

## Project Workflow

### Data Collection
1. **Data Source:** I downloaded IPL data spanning from 2008 to 2023 from Kaggle.
2. **Data Cleaning:** I removed outdated teams that no longer participate in the IPL.

### Feature Engineering
3. **New Features:** I derived new columns such as:
    - Current Run Rate (CRR)
    - Required Run Rate (RRR)
    - Wickets (wickets remaining at each ball)
   The data is divided into two parts:
    - All Matches Data
    - Ball-by-Ball Data

### Data Preparation
4. **Data Merging:** I merged the datasets using Pandas and separated the features (X - independent variables) from the target (y - dependent variable) necessary for building the machine learning model.
5. **Encoding:** Converted string columns to one-hot encoding to make them suitable for the model.

### Model Building
6. **Pipeline Creation:** Created a pipeline with the following steps:
    1. One-hot encoding of categorical variables
    2. Logistic Regression for prediction
7. **Model Serialization:** Saved the trained model to a pickle file, generating a `pipe.pickle` file.

### Application Development
8. **App Creation:** Developed a Streamlit application (`app.py`) which:
    - Accepts user inputs: Batting team, Bowling team, City, Target, Current Runs, Current Overs, and Wickets Gone.
    - Predicts the winning probability of the batting team.
    - Displays results with a stacked bar chart.
9. **Visual Enhancements:** Fetches and displays the logos of the selected batting and bowling teams dynamically.

### User Engagement
10. **Interactive Features:** Added fun comments to enhance user engagement. For example, messages appear when:
    - The same team is chosen for batting and bowling.
    - No target is provided (target box left at 0).
    - Unrealistic targets are set (e.g., 300+ runs).

### Deployment
11. **Hosting:** Deployed the app on a live server for public access.

## Conclusion
This project demonstrates the entire workflow of building a machine learning model from data collection and cleaning to model training and deployment in a user-friendly web application.

---
