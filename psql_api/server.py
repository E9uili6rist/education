from flask import Flask, jsonify, request
import psycopg2

# Flask-приложение для REST API
app = Flask(__name__)

# Подключение к базе данных PostgreSQL
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="whatislove",
    host="postgres",
    port="5432"
)
cur = conn.cursor()

# Создание таблицы, если она не существует
cur.execute("""
    CREATE TABLE IF NOT EXISTS public.data_study (
        id SERIAL PRIMARY KEY,
        text TEXT,
        time TIMESTAMP WITH TIME ZONE
    )
""")
conn.commit()

@app.route('/data', methods=['GET'])
def get_data():
    cur.execute("SELECT id, text, time FROM public.data_study")
    conn.commit()
    rows = cur.fetchall()
    data = [{'id': row[0], 'text': row[1], 'time': row[2]} for row in rows]
    return jsonify(data)

@app.route('/data', methods=['POST'])
def add_data():
    text = request.json.get('text')
    if text:
        cur.execute("INSERT INTO public.data_study (text, time) VALUES (%s, CURRENT_TIMESTAMP)", (text,))
        conn.commit()
        return 'Data added successfully.'
    else:
        return 'No text provided.', 400

@app.route('/data', methods=['DELETE'])
def delete_data():
    cur.execute("TRUNCATE TABLE public.data_study CASCADE")
    conn.commit()
    # Сбросить значение счетчика идентификаторов до 1
    cur.execute("ALTER SEQUENCE public.data_study_id_seq RESTART WITH 1")
    conn.commit()
    return 'Table cleared and sequence reset.'

@app.route('/data/<int:id>', methods=['GET'])
def get_data_by_id(id):
    cur.execute("SELECT id, text, time FROM public.data_study WHERE id = %s", (id,))
    conn.commit()
    row = cur.fetchone()
    if row:
        data = {'id': row[0], 'text': row[1], 'time': row[2]}
        return jsonify(data)
    else:
        return 'Data not found.', 404

@app.route('/data/<int:id>', methods=['PUT'])
def update_data(id):
    text = request.json.get('text')
    if text:
        cur.execute("UPDATE public.data_study SET text = %s WHERE id = %s", (text, id))
        conn.commit()
        return 'Data updated successfully.'
    else:
        return 'No text provided.', 400

@app.route('/data/<int:id>', methods=['DELETE'])
def delete_data_by_id(id):
    cur.execute("DELETE FROM public.data_study WHERE id = %s", (id,))
    conn.commit()
    return 'Data deleted successfully.'

app.run(host='0.0.0.0', port=5000)
