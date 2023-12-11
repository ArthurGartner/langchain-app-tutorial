# Bring in deps
import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

os.environ['OPENAI_API_KEY'] = apikey

# App framework
st.title("YouTube GPT Creator")
prompt = st.text_input('Plug in your prompt here')

# Prompt templates
title_template = PromptTemplate(
    input_variables = ['topic'],
    template = 'Write me a youtube video title about {input_variables}'
)

# LLMS
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt = title_template, verbose = True)

# Show stuff to screen if prompt is found
if prompt:
    response = title_chain.run(prompt)
    st.write(response)