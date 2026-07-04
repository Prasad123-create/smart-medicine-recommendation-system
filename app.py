from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['POST'])
def search():

    problem = request.form['problem'].lower()

    import sqlite3

    conn = sqlite3.connect('medicines.db')
    cursor = conn.cursor()

    cursor.execute(
    "SELECT DISTINCT medicine FROM medicines WHERE problem=?",
    (problem,)
)

    medicines = cursor.fetchall()

    conn.close()

    return render_template(
        'result.html',
        problem=problem,
        medicines=medicines
    )
@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/add_medicine', methods=['POST'])
def add_medicine():

    problem = request.form['problem'].lower()
    medicine = request.form['medicine']

    import sqlite3

    conn = sqlite3.connect('medicines.db')
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO medicines(problem, medicine) VALUES(?, ?)",
        (problem, medicine)
    )

    conn.commit()
    conn.close()

    return redirect('/view_medicines')

@app.route('/view_medicines')
def view_medicines():

    conn = sqlite3.connect("medicines.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, problem, medicine FROM medicines ORDER BY problem"
    )

    medicines = cursor.fetchall()

    conn.close()

    return render_template(
        "view_medicines.html",
        medicines=medicines
    )
@app.route('/delete/<int:id>')
def delete(id):

    conn = sqlite3.connect('medicines.db')
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM medicines WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect('/view_medicines')
    from flask import redirect

    return redirect('/view_medicines')

@app.route('/edit/<int:id>')
def edit(id):

    import sqlite3

    conn = sqlite3.connect("medicines.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, problem, medicine FROM medicines WHERE id=?",
        (id,)
    )

    medicine = cursor.fetchone()

    conn.close()

    return render_template(
        "edit.html",
        medicine=medicine
    )


@app.route('/update/<int:id>', methods=['POST'])
def update(id):

    problem = request.form['problem'].lower()
    medicine = request.form['medicine']

    import sqlite3

    conn = sqlite3.connect("medicines.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE medicines SET problem=?, medicine=? WHERE id=?",
        (problem, medicine, id)
    )

    conn.commit()
    conn.close()

    return redirect('/view_medicines')

@app.route('/get_symptoms')
def get_symptoms():

    import sqlite3

    conn = sqlite3.connect('medicines.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT DISTINCT problem FROM medicines ORDER BY problem"
    )

    symptoms = cursor.fetchall()

    conn.close()

    return {
        "symptoms": [item[0] for item in symptoms]
    }
@app.route('/search_suggestions')
def search_suggestions():

    from flask import request
    import sqlite3

    keyword = request.args.get('q', '').lower()

    conn = sqlite3.connect("medicines.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT DISTINCT problem FROM medicines WHERE problem LIKE ?",
        ('%' + keyword + '%',)
    )

    data = cursor.fetchall()

    conn.close()

    return {
        "results": [item[0] for item in data]
    }

if __name__ == '__main__':
    app.run(debug=True)