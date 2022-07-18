import streamlit as st
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

#quando for subir colocar as variaveis cadastradas no HEROKU

host = os.getenv("HOST")
dbname = os.getenv("DBNAME")
user = os.getenv("USER")
password = os.getenv("PASSWORD")

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton


def init_connection(): 
    return psycopg2.connect(host=host,dbname=dbname, user=user,password=password)

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
#@st.experimental_memo(ttl=600)

def run_query(query):
     with conn.cursor() as cur:
         cur.execute(query)
         return cur.fetchall()
     
     
rows = run_query("SELECT * from clie;")
    # Print results.
for row in rows:
        st.write(f"{row[0]} has a :{row[1]}:")
