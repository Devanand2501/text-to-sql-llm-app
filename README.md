# SQL Query Generator and Executor

## Overview

This Streamlit application allows users to convert English questions into SQL queries and execute them on a MySQL database. It leverages Google's Generative AI for natural language understanding and generation.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)


## Features

- Convert English questions into SQL queries using Generative AI.
- Execute SQL queries on a MySQL database.
- Visualize the results in a tabular format using Streamlit.

## Installation

1. Clone the repository:

    git clone https://github.com/Devanand2501/text-to-sql-llm-app.git

2. Create and activate a virtual environment:

    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install dependencies:

    pip install -r requirements.txt

4. Set up your environment variables:

   Edit the `.env` file and add your API key and database credentials.

## Usage

Run the Streamlit app:


streamlit run app.py
