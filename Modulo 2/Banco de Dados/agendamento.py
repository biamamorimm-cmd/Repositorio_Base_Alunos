from flask import Flask, render_template, request,redirect,url_for
import sqlite3

app = Flask(__name__)

def init_db():
     conn= sqlite3.connect ('agenda.db')
     cursor = conn.cursor ()
     cursor.execute ('''
                     CREATE TABLE IF NOT EXISTS agendamento(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     nome TEXT NOT NULL,
                     idade INTEGER NOT NULL,
                     peso REAL NOT NULL,
                     horarioaula TEXT NOT NULL                    
        )
     ''')

     conn.commit ()
     conn.close ()

init_db ()


@app.route ('/')
def index ():
   return render_template ('agendamento.html')

app.run (debug=True)

agenda = [{ "id": 1,"nome":"Beatriz Moraes Amorim", "idade":16,"peso": 70, "horarioaula": "15:00" }]



@app.route ('/agendar',methods= ['POST'])
def adicionar():

 Nome= request.form ['nome']
 Idade = request.form ['idade']
 Peso = request.form ['peso']
 Horario = request.form ['horario']

 conn= sqlite3.connect ('agenda.db')
 cursor= conn.cursor ()

 cursor.execute ('INSERT INTO  (nome,idade,peso,horario) VALUES (?,?,?,?), (nome,idade,peso,horario) ')

 conn.commit ()
 conn.close ()
 return render_template ('agendamento.html')

app.run ()


@app.route('/agendar')
def index():
    return render_template('agendamento.html')
