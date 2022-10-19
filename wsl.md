
# instalação do wsl e Ubuntu
wsl --install -d Ubuntu

# atualizar a versão do Ubuntu
sudo apt install update-manager
# atualize os pacotes do sistema
sudo apt-get update
sudo apt-get dist-upgrade
#  instale o update-manager-core
sudo apt-get install update-manager-core
# Visualize o arquivo /etc/update-manager/release-upgrades, antes de editá-lo
cat /etc/update-manager/release-upgrades (Promp=lts)
# Inicie o processo de atualização com o comando
sudo do-release-upgrade -d

# versão do Ubuntu
lsb_release -a


# listar e ver a versão do linux/wsl
wsl -l -v

# Pacotes de atualização e upgrade
sudo apt update
sudo apt upgrade


# listar e ver a versão e o status do linux/wsl
wsl -l -v

# iniciar wsl
wsl