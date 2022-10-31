from flask import Flask, json

# variavel da aplicação 
# __name__ é o nome do proprio arquivo .py
app = Flask(__name__)

# primeira rota
@app.route('/')
def index():
    result = 'Primeira API Flask'
    return result   

# verifica se a aplicação está sendo chamado via linha de comando e executa
# se o arquivo .py for importado, essa aplicação não executada
if __name__ == '__main__':
    app.run(debug=True)
