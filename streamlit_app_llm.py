import streamlit as st
from langchain_openai.chat_models import ChatOpenAI

st.title('Chat with GPT-3')

open_api_key = st.sidebar.text_input('OpenAI API Key', type='password')


def generate_response(input_text):
    model = ChatOpenAI(temperatture=0.5, api_key=openai_api_key)
    st.info(model.invoke(input_text))


with st.form('my_form'):
    text = st.text_area('Enter text:',
                        'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if not open_api_key.startswith('sk-'):
        st.warning('Please enter a valid API key')
    elif submitted and open_api_key.startswith('sk-'):
        generate_response(text)
