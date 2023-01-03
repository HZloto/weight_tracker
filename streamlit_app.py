import streamlit as st
import pandas as pd 
from weight_tracker import track_weight

df = pd.read_csv("weight_tracker.csv")

def main():
    
    st.title("Hugros's weight tracker")
    st.write("This app is a companion for a weight loss journey: track your daily weight, visualise progress and get insights regarding when the objectives will be met!")
    st.header("Add data for the day")
    user_input = st.text_input("Today's weight:")
    result = track_weight(user_input)
    

    st.write(result)
    
    
    st.header("Visualise previous data")
    st.line_chart(df, x="Date",y="Weight", )

if __name__ == '__main__':
    main()