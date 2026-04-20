from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'magic'

card_bucket_list = [
    {"id": 1, "name": "Black Lotus", "cost": 15000, "date": "2026-05-01"},
    {"id": 2, "name": "Mox Sapphire", "cost": 8000, "date": "2026-06-10"},
    {"id": 3, "name": "Time Walk", "cost": 7000, "date": "2026-07-15"},
]

next_id = 4

def validate_input(name, cost, date):
    errors = []

    if not name or len(name) > 100:
        errors.append("Card name must be between 1 and 100 characters.")

    try:
        cost_int = int(cost)
        if cost_int < 0:
            errors.append("Cost must be a positive integer.")
    except ValueError:
        errors.append("Cost must be a valid integer.")

    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        errors.append("Date must be in YYYY-MM-DD format.")

    return errors


@app.route('/')
def index():
    return render_template('index.html', cards=card_bucket_list)


@app.route('/add', methods=['POST'])
def add_card():
    global next_id

    name = request.form.get('name', '').strip()
    cost = request.form.get('cost', '').strip()
    date = request.form.get('date', '').strip()

    errors = validate_input(name, cost, date)

    if errors:
        for error in errors:
            flash(error, 'danger')
        return redirect(url_for('index'))

    card_bucket_list.append({
        'id': next_id,
        'name': name,
        'cost': int(cost),
        'date': date
    })

    next_id += 1

    flash('Card added successfully!', 'success')
    return redirect(url_for('index'))


@app.route('/delete/<int:card_id>', methods=['POST'])
def delete_card(card_id):
    global card_bucket_list

    card_bucket_list = [c for c in card_bucket_list if c['id'] != card_id]

    flash('Card deleted.', 'info')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)