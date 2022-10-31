from flask import Flask, json, request


# variavel da aplicação 
# __name__ é o nome do proprio arquivo .py
app = Flask(__name__)

# primeira rota
@app.route('/', methods = ['GET'])
def index():
    
    get_header = request.headers.get('Content-Type')

    # para utilizar o request.get_data(), é necessário converter de bytes para str
    # e depois converter para json
    # converte de bytes para str utilizando encode 'utf-8'
    data = request.get_data().decode('utf-8')
    # converte de str para json
    data_json = json.loads(data)
    
    # utilizando o request.get_json() já é um objeto do tipo json

    my_json = {}
    my_json['API'] = 'Primeira API Flask'
    my_json['header'] = get_header
    my_json['body_request.get_data()'] = data_json
    my_json['body_request.get_json()'] = request.get_json()
    
    return my_json

# verifica se a aplicação está sendo chamado via linha de comando e executa
# se o arquivo .py for importado, essa aplicação não executada
if __name__ == '__main__':
    app.run(debug=True)
