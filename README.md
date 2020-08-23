# Dashboard Clínico
Simples dashboard clínico.
Projeto criado para aprendizagem de Flask e SQLAlchemy.
Ainda precisa de ajustes e melhorias, e não chega aos pés do projeto demonstrado pelo professor. Mas quando eu tiver maior domínio destas tecnologias estas pendências serão resolvidas.

🚧 **Em construção...** 🚧 

![Tela](https://github.com/alberto-minoru/flask_dashboard/tree/master/static/imgs/Tela.png)

Tabela de conteudos
=================
<!--ts-->
   * [Tabela de Conteudos](#tabela-de-conteudos)
   * [Tecnologias](#tecnologias)
   * [Requisitos](#requisitos)
   * [Executar](#executar)
   * [Licença](#licença)
   * [Agradecimentos](#agradecimentos)
<!--te-->

## Tecnologias

As seguintes ferramentas foram usadas na construção deste projeto:

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)

## Requisitos

Use o gerênciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar todas as dependências necessárias que estão no arquivo requirements.txt.

```bash
pip install -r requirements.txt.
```

## Executar
Será necessário ajustar as seguintes variáveis no seu sistema:
- SECRET (com a sua secret para o Flask)
- FLASK_ENV (descrevendo o seu ambiente, caso seja de produção ou desenvolvimento)
- SQLALCHEMY_DATABASE_URI (com as configurações do seu banco de dados)

Por exemplo, basta digitar os seguintes comandos em um terminal de um sistema Linux:
```bash
export SECRET='f0aa2c733b03dabf68135fae89273149'
export FLASK_ENV='production'
export SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://usuario:senha@127.0.0.1:3306/database'
```

Ou você poderá ajustar tudo diretamente no arquivo config.py
Depois execute os comandos abaixo:

```python
python model.py db upgrade
python run.py
```
## Licença
[MIT](https://choosealicense.com/licenses/mit/)

## Agradecimentos
Sempre serei grato a Deus e a minha família (sem o apoio dela eu seria ninguém).
Agradeço a [Digital Innovation One](https://digitalinnovation.one/) por disponibilizar excelentes cursos, onde fui capaz de aprender o necessário para desenvolver este projeto. E agradeço ao professor [Tiago Luiz](https://canaldoprof.com.br/) por disponibilizar parte de seu tempo para compartilhar seus conhecimentos sobre Flask e SQLAlchemy.