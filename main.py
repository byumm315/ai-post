#from dotenv import load_dotenv
#load_dotenv()
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

model = ChatOpenAI()
output_parser = StrOutputParser()

st.title('인공지능 시인')
content=st.text_input('시의 주제를 제시해주세요.')
if st.button('시 작성 요청하기'):
  with st.spinner('시 작성 중...'):
    prompt=ChatPromptTemplate.from_template("{foo}에 대한 시를 써줘.")
    chain = prompt | model | output_parser
    st.write(chain.invoke({'foo':content}))


