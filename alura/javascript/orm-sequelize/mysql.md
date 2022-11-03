# iniciar serviço mysql
sudo service mysql start
# ver o status do banco de dados
sudo service mysql status
# reiniciar serviço mysql
sudo service mysql restart
# ver o serviço rodando
sudo service mysql status
sudo ss -tap | grep mysql
# acessar o mysql com o usuário fernando@localhost
sudo mysql -u fernando@localhost -p

# mostra as base de dados
show databases;
# seleciona uma base de dados: use <database>
use escola_ingles;
# mostra as tabelas da base de dados
show tables;

# Erro "Public Key Retrieval is not allowed" ao fazer Test Connection no Dbeaver. Como resolver?
# https://cursos.alura.com.br/forum/topico-erro-public-key-retrieval-is-not-allowed-ao-fazer-test-connection-no-dbeaver-como-resolver-137427

Na string de conexão você pode incluir a opção "allowPublicKeyRetrieval=true", exemplo:
  jdbc:mysql://localhost:3306/db?allowPublicKeyRetrieval=true&useSSL=false

Para usuários do DBeaver:
  Clique com o botão direito na sua conexão, escolha "Editar Conexão"
  Na tela "Configurações de conexão" (tela principal), clique em "Editar configurações do driver"
  Clique em "Propriedades da conexão"
  Clique com o botão direito na área "propriedades do usuário" e escolha "Adicionar nova propriedade"
  Adicione duas propriedades: "useSSL" e "allowPublicKeyRetrieval"
  Defina seus valores como "false" e "true" clicando duas vezes na coluna "value"


## Incluir 2 colunas na tabela Pessoas
  ALTER TABLE Pessoas ADD COLUMN  created_at DATETIME NOT NULL;
  ALTER TABLE Pessoas ADD COLUMN  updated_at DATETIME NOT NULL;

## Excluir 2 colunas na tabela Pessoas
  ALTER TABLE Pessoas DROP COLUMN created_at;
  ALTER TABLE Pessoas DROP COLUMN updated_at;