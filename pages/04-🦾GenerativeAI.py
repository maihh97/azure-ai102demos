from openai import AzureOpenAI
import streamlit as st
import dotenv
import json

# Load environment variables
ENV = dotenv.dotenv_values(".env")

# Intiate Azure OpenAI client
client = AzureOpenAI(
  azure_endpoint = ENV["AZURE_OPENAI_ENDPOINT"], 
  api_key=ENV["AZURE_OPENAI_KEY"],  
  api_version=ENV["AZURE_OPENAI_API_VERSION"]
)

st.title("💰Woodgrove Advisor")

# Prompt setup

default_prompt = """
You are an AI assistant that helps financial advisors to review information about the company finance product. 
"""

# Select model

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": default_prompt},
        {"role": "assistant", "content": "Hello, can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    # Generate completion
    response = client.chat.completions.create(
        model=ENV["AZURE_OPENAI_CHATGPT_DEPLOYMENT"], 
        messages=st.session_state.messages,
        temperature=0.7,
        top_p=0.95,
        max_tokens=500,
        # extra_body={
        #     "data_sources": [
        #         {
        #             "type": "azure_search",
        #             "parameters": {
        #                 "endpoint": ENV["AZURE_SEARCH_ENDPOINT"],
        #                 # "index_name": "sanfra",
        #                 "semantic_configuration": "default",
        #                 "query_type": "semantic",
        #                 "fields_mapping": {},
        #                 "in_scope": True,
        #                 "role_information": "You are an AI assistant that helps people find information.",
        #                 "filter": None,
        #                 "strictness": 3,
        #                 "top_n_documents": 5,
        #                 "authentication": {
        #                     "type": "system_assigned_managed_identity"
        #                 }
        #             }
        #         }
        #     ]
        # }
    )
    msg = response.choices[0].message.content
    context = response.choices[0].message.context
    st.write(context)
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
    
st.download_button(
    "Download Conversation",
    data=json.dumps(st.session_state["messages"]),
    file_name=f"conversation.json",
    mime="text/json",
)