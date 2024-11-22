
Versão do Python : 3.12.4

Instale as dependências : pip install -r requirements.txt

Crie o executável : pyinstaller --onefile pycommit.py

Adicione o executável ao PATH

Crie uma pattern de commit com pycommit.exe add_pattern --pattern "{variavel1} : {placeholder} / {versao}" --name "Nome da pattern"

No final basta utilizar para o commit com pycommit.exe --name ( o nome da pattern criada anteriormente )