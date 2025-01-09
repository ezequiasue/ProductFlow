git config --global user.name "Ezequias S. Santos"
git config --global user.email "phd.esantos@gmail.com"

git remote add origin https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git


git remote add origin git@github.com:ezequiasue/ProductFlow-.git


Passo 1: Verifique se você já tem uma chave SSH
Primeiro, verifique se você já tem uma chave SSH no seu computador. No terminal, execute:

linux:
ls -al ~/.ssh

Microsoft
Get-ChildItem -Path $env:USERPROFILE\.ssh

ssh-keygen -t rsa -b 4096 -C "phd.esantos@gmail.com"

Renomeie a branch local de master para main:
git branch -m master main
