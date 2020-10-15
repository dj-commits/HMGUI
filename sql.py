import psycopg2
from conn_param import conn_string

class Backend:
    
    def __init__(self):
        self.conn = psycopg2.connect(conn_string)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS movies (movie_name TEXT, director TEXT, fx_artist TEXT, year TEXT, rating TEXT, date_watched TEXT, entryID SERIAL )")
        self.conn.commit()

    def insert(self, movie_name, director, fx_artist, year, rating, date_watched):
        self.conn = psycopg2.connect(conn_string)
        self.cur = self.conn.cursor()
        self.cur.execute("INSERT INTO movies VALUES (%s, %s, %s, %s, %s, %s)", (movie_name, director, fx_artist, year, rating, date_watched))
        self.conn.commit()

    def view(self):
        self.conn = psycopg2.connect(conn_string)
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM movies")
        rows = self.cur.fetchall()
        return rows

    def delete(self, movie_name):
        self.conn = psycopg2.connect(conn_string)
        self.cur = self.conn.cursor()
        self.cur.execute("DELETE FROM movies WHERE movie_name=%s", (movie_name, ))
        self.conn.commit()

    def search(self, movie_name="", director="", fx_artist="", year="", rating="", date_watched=""):
        self.conn = psycopg2.connect(conn_string)
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM movies WHERE movie_name=%s OR director=%s OR fx_artist=%s OR year=%s OR rating=%s OR date_watched=%s", (movie_name, director, fx_artist, year, rating, date_watched))
        rows = self.cur.fetchall()
        return rows

    def update(self, movie_name, director, fx_artist, year, rating, date_watched, correct_row):
        self.conn = psycopg2.connect(conn_string)
        self.cur = self.conn.cursor()
        self.cur.execute("UPDATE movies SET movie_name=%s, director=%s, fx_artist=%s, year=%s, rating=%s, date_watched=%s WHERE entryID=%s", (movie_name, director, fx_artist, year, rating, date_watched, correct_row))
        self.conn.commit()
    
    def __del__(self):
        self.conn.close()
