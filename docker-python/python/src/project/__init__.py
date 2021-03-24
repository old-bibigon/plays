#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import datetime
import psycopg2

psql_conn = psycopg2.connect(
    os.environ.get('PSQL_URI', 'postgresql://postgres/playdb')
)


from flask import Flask
app = Flask(__name__)
 

@app.route('/')
def hello_world():
    t = datetime.datetime.now()
    return f'Moe Flask приложение в контейнере Docker. {t}\n'


@app.route('/script')
def create_table():
    query = """
        CREATE TABLE IF NOT EXISTS tmp_play (
            id serial,
            name varchar(255)
        )
    """
    cursor = psql_conn.cursor()
    cursor.execute(query)
    psql_conn.commit()
    return f'таблица создана\n'


@app.route('/tables')
def list_tables():
    query = """
        SELECT table_name FROM information_schema.tables
        WHERE table_schema NOT IN ('information_schema', 'pg_catalog')
        AND table_schema IN('public');
    """
    cursor = psql_conn.cursor()
    cursor.execute(query)
    return '\n'.join([x[0] for x in cursor.fetchall()]) + '\n'


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
