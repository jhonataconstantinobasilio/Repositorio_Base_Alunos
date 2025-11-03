from flask import Flask , render_template, request

app = Flask(__name__)

pessoa={
'nome':'gabriel',
'idade':16,
'telefone':'115587-456'
}


@app.route('/')
def home():
    return render_template('home.html',pessoa=pessoa)

@app.route('/teste')
def test():
   return render_template('produto.html',pessoa=pessoa)

@app.route('/games')
def games():
   return render_template('styles.css')

alunos=[]
@app.route('/register',methods={'POST','GET'})
def register():
   nome=request.form.get('nome')
   idade=request.form.get('idade')
   email=request.form.get('email')
   rg=request.form.get('RG')
   alunos.append({'nome':nome,'idade':idade,'email':email,'RG':rg})
   return render_template('register.html',alunos=alunos)

if __name__ == '__main__':
 app.run(debug=True, host='127.0.0.1', port=5000)