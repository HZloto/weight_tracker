import streamlit as st
import pandas as pd 
import time
from weight_tracker import track_weight
from weight_tracker import check_decimal



def main():
    
    st.title("Hugros' weight tracker")
    st.write("This app is a companion for a weight loss journey: track your daily weight, visualise progress and get insights regarding when the objectives will be met!")
    
    df = pd.read_csv("weight_tracker.csv")

    df = pd.read_csv("weight_tracker.csv")
    st.header("Visualise previous data")
    
    st.subheader("Weight evolution")
    st.line_chart(df, x="Date",y="Weight", )
    
    st.subheader("Fat percentage evolution")
    st.line_chart(df, x="Date",y="Body Fat", )
    
    st.subheader("Muscle mass evolution")
    st.line_chart(df, x="Date",y="Muscle Mass", )
    
    st.header("Add data for the day")
    weight_input = st.text_input("Today's weight:")
    fat_input = st.text_input("Today's fat percentage:")
    muscle_input = st.text_input("Today's muscle %:")
    
    if muscle_input:
        result = track_weight(weight_input,fat_input,muscle_input)
        st.write(result)


if __name__ == '__main__':
    main()