import streamlit as st
from math import floor

st.title("ススムタスク（仮）")

task = st.text_input("タスク名を入力")
minutes = st.number_input("想定所要時間（分）",min_value=1,step=5)

def split_task(total_minutes):
    if total_minutes <= 60:
        return [total_minutes]
    chunks = []
    while total_minutes > 60:
        chunks.append(25)
        total_minutes -= 25
    chunks.append(total_minutes)
    return chunks

if task and minutes:
    chunks = split_task(minutes)

    st.subheader("今やるのはこれ")
    st.write(f"{task} 1/{len(chunks)}")
    st.write(f"残り{chunks[0]}分")

    st.divider()

    total_time = sum(chunks)
    st.write(f"今日の合計：{total_time}分")