# app.py

from flask import Flask, render_template, request, g
import sqlite3

app = Flask(__name__)

DATABASE = 'mega.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_date = request.form['selected_date']
        predictions = get_predictions_for_date(selected_date)
        print(predictions)
        print(selected_date)
        if predictions:
            return render_template('result.html', predictions=predictions, selected_date=selected_date)
        else:
            error_message = "No predictions found for the selected date."
            return render_template('result.html', error_message=error_message, selected_date=selected_date)
    else:
        return render_template('index.html')

def get_predictions_for_date(selected_date):
    db = get_db()
    cursor = db.cursor()
    # Assuming the selected date format is 'YYYY-MM-DD'
    year, month, day = map(int, selected_date.split('-'))
   
    cursor.execute("SELECT * FROM haryana_final WHERE day=? AND month=? AND year=?", (day, month, year))
    predictions = cursor.fetchall()
    return predictions

if __name__ == '__main__':
    app.run(debug=True)