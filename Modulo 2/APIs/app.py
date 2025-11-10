from flask import Flask , render_template, request,redirect,url_for,g
import sqlite3
from pathlib import Path

app = Flask(__name__)
Db_path= Path(__file__).parent / 'alunos.db'
def get_db():
  if 'db' not in g:
    conn = sqlite3.connect(Db_path)
    conn.row_factory= sqlite3.Row
    g.db = conn
  return g.db

@app.teardown_appcontext
def close_db(exc):
   db = g.pop('db',None)
   if db is not None:
     db.close()

@app.route('/teste')
def init_db():
    db = sqlite3.connect(Db_path)
    with db:
        # Tente criar a tabela
        db.execute("""
            CREATE TABLE  aluno (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                rg TEXT NOT NULL,
                idade TEXT NOT NULL,
                email TEXT NOT NULL
            );
        """)
    db.close()


@app.route('/init_db')
def route_init_db():
  return 'banco de dados criado com sucesso'    

@app.route('/tabelas')
def listar_tabelas():
    db = get_db()
    cur = db.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [r[0] for r in cur.fetchall()]
    return "<br>".join(tables)

@app.route('/')
def index():
   return render_template('register.html')



@app.route('/adicionar',methods=['POST'])

def adicionar():
   nome=request.form.get('nome')
   idade=request.form.get('idade')
   email=request.form.get('email')
   rg=request.form.get('rg')
   db = get_db()
   cur = db.execute("INSERT INTO aluno (nome, idade, email, rg) VALUES (?, ?, ?, ?)", (nome, idade, email, rg))
   db.commit()
   return redirect(url_for('index'))

if __name__ == '__main__':
 app.run(debug=True, host='127.0.0.1', port=5000)

