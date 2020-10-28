from flask import Flask, render_template, g
import sqlite3
PATH ="db/jobs.sqlite"
app= Flask(__name__)

def open_connection():
    connection = g.getattr()

    if connection== None:
        connection=sqlite3.connect("db/jobs.sqlite")

    row_factory = sqlite3.Row

    

    def execute_sql(sql, values=(), commit=False, single= False):
        connection=connection
        cursor=connection.execute_sql()






@app.route("/")
@app.route("/jobs")
 
def jobs():
    return render_template('index.html')


 
