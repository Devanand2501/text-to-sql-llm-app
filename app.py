# Run below command to create virtual environment
# import venv
# venv.create('venv')

from dotenv import load_dotenv
load_dotenv() 


import os 
import streamlit as st 
import psycopg
import google.generativeai as genai

# Api key configuration
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) --> If you are running on local host
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"]) 

# Function to return sql queries
def get_sql_queries(prompt,question):
    model= genai.GenerativeModel(model_name="gemini-pro")
    response = model.generate_content([prompt[0],question])
    return response.text

def read_queries(query, cur):
    try:
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    except psycopg.Error as err:
        st.error(f"MySQL Error: {err}")
        return None

prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - RollNo, Name, Email, Division,
    Domain and Marks \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science Domain?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where Domain="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]

# Streamlit UI App
def main():
    st.set_page_config(page_title="SQL query retrieval")
    st.header("Prompt To SQL Query Converter :male-technologist:")

    conn = psycopg.connect(
        database=st.secrets["DB_NAME"],
        host = st.secrets["DB_HOST_NAME"],
        user = st.secrets["DB_USER_NAME"],
        port = st.secrets['DB_PORT'],
        password = st.secrets["DB_PASSWORD"]
    )
    cursor = conn.cursor()
    table = read_queries("SELECT * FROM student",cur=cursor)

    st.markdown('''
    ---
    ### Sample Data
    ''')
    st.dataframe(data=table)

    if 'question' not in st.session_state:
        st.session_state.question = 'SELECT * FROM student'

    st.session_state.question = st.text_input("Input : ",key="input")
    submit = st.button("Ask the question")

    if submit:
        query = get_sql_queries(prompt=prompt,question=st.session_state.question)

        with st.expander("Click to see the generated SQL Query"):
            st.write(f"{query}")
        data = read_queries(query=query,cur=cursor)
        st.subheader("Response is :")
        if len(data) > 0:
            st.table(data)
        else:
            st.warning("No data found.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
