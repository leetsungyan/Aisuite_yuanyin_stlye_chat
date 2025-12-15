# -*- coding: utf-8 -*-
"""
Lucky Vicky Positive Thinking Generator - Streamlit Version
"""

import streamlit as st
import aisuite as ai
import os

# Page config
st.set_page_config(
    page_title="Lucky Vicky 🌈",
    page_icon="✨",
    layout="centered"
)

# Title
st.title("꒰*ˊᵕˋ꒱ Lucky Vicky Positive Thinking Generator 🌈")
st.markdown("請輸入一件你覺得超小事，甚至有點倒楣的事，讓我幫你用員瑛式思考，超正向的方式重新詮釋！")

# System prompt
system = """
請用台灣習慣的中文來寫這段 po 文：
請用員瑛式思考, 也就是什麼都正向思維任何使用者寫的事情,
用我的第一人稱、社群媒體 po 文的口吻說一次,
說為什麼這是一件超幸運的事, 並且以「完全是 Lucky Vicky 呀!」結尾。
可以適度的加上 emoji。
"""

def reply(prompt, provider="groq", model="llama-3.3-70b-versatile"):
    """Generate AI response"""
    try:
        client = ai.Client()
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ]
        response = client.chat.completions.create(
            model=f"{provider}:{model}",
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"發生錯誤: {str(e)}"

# API Key setup
st.sidebar.header("API 設定")
api_key = st.sidebar.text_input("Groq API Key", type="password")
if api_key:
    os.environ['GROQ_API_KEY'] = api_key
    st.sidebar.success("API Key 已設定")
else:
    st.sidebar.warning("請輸入你的 Groq API Key")

# Provider selection
provider = st.sidebar.selectbox(
    "AI 供應商",
    ["groq"],
    help="目前只支援 Groq，其他供應商敬請期待"
)

model = st.sidebar.selectbox(
    "模型",
    ["llama-3.3-70b-versatile", "gemma2-9b-it"],
    help="選擇 AI 模型"
)

# Main interface
st.header("📝 輸入你遇到的小倒楣事")

user_input = st.text_area(
    "今天發生的事情是…",
    placeholder="例如：今天出門就下大雨, 可是忘了帶傘...",
    height=100
)

if st.button("Lucky Vicky 魔法! ✨", type="primary"):
    if not api_key:
        st.error("請先在側邊欄輸入 API Key")
    elif not user_input.strip():
        st.warning("請輸入一些內容")
    else:
        with st.spinner("Lucky Vicky 正在思考中..."):
            response = reply(user_input, provider, model)

        st.success("✨ 員瑛式貼文 ✨")
        st.write(response)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit and AI")
st.markdown("[GitHub Repository](https://github.com/yourusername/lucky-vicky) | [Streamlit App](https://your-app.streamlit.app)")