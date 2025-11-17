from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app=Flask(__name__)

def init_db():
    conn = sqlite3.connect('registro.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            nota INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()




@app.route ('/cadastro')
def index ():
   conn= sqlite3.connect
   cursor= conn.cursor
    
   cursor.execute( 'SELECT * from  registro') 
   aluno = cursor.fetchall ()
   conn.close ()
   return render_template ('index2.html')



app.run(debug=True)

aluno=[{ "id": 1,"nome":"Beatriz", "idade":16,"nota": "9" }]


#return render_template ('index2.html', resultado = aluno )


   
@app.route ('/adicionar',methods= ['POST'])
def adicionar():
 Nome= request.form ['nome']
 Idade = request.form ['idade']
 Nota = request.form ['nota']