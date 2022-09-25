# FreshNews.AI - News Summarizer

FreshNews.AI uses newsapi.org to curate news and summarize them for the user. FreshNews.AI is based on Flask which is a micro web framework written in Python.  

## Installation (Server)

* Install Python 3 (https://www.python.org/downloads/release/python-3107/)

* Install XAMPP

* Clone this repository  

* Go to cloned project folder

    ```
    cd path\to\news_ai
    ```

* Create a new virtual environment in the project folder

    ```
    python -m venv venv
    ```

* Activate the virtual environment
    
    ```
    .\venv\Scripts\activate
    ```

* Install dependencies
    ```
    pip install -r requirements.txt
    ```

* Run XAMPP as administrator and start Apache and MySQL

* Create database "news_ai" using phpMyAdmin

* Run Flask App
    ```
    flask --debug run
    ```