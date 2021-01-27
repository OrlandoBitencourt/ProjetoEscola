# ProjetoEscola
 
**_Projeto de restAPI para backend de uma escola._**

- O projeto foi feito no seguindo o padrão MVC (model view controller).
- Linguagem Python.  
- Frameworks usados: Flask e Flask_restfull.
- Todos os modulos do python estão no arquivo `Requirements.txt` (estão instalados na virtualenv na pasta nomeada `venv`).

## **Documentação:**

Toda entrada e saída de dados é em no formato `JSON`.

Para validar os metodos POST utilizei o app Postman, dentro da pasta `postman-tests`.

Para executar o projeto basta executar o arquivo `main.py`.

No arquivo `endpoints.py` estão todas as rotas:
- `"/health-check"`
- `"/aluno"`
- `"/gabaritos"`
- `"/provas/<cpf>/<idProva>"`
- `"/aprovados"`

### Rota: `"/health-check"`:
- Responsável pelo teste dos endpoints.
- Metodo Get retorna '_ok_' caso esteja funcionando.

### Rota: `"/aluno"`:
- Cadastra o aluno no sistema através do metodo POST. 
- O sistema é limitado a 100 alunos cadastrados, caso o usuario tente criar mais que 100, haverá o retorno (_"Numero maximo de alunos cadastrados"_).

### Rota: `"/gabaritos"`:
- Cadastra todas as questões das provas e as respostas através do metodo POST.
- O sistema permite cadastrar 10 questões para cada prova e 10 respostas. 

### Rota: `"/provas/<cpf>/<idProva>"`:
- Rota resposavel por cadastrar as respostas do aluno para a prova com metodo POST.
- O calculo da nota acontece após as respostas serem salvas. 
- A media geral do aluno também é calculada cada vez que ele responde uma questão (a nota final é a média aritmética das notas de todas as provas).

### Rota: `"/aprovados"`:
- Responsavel por retornar lista de alunos aprovados em formato json com o metodo GET (Para um aluno ser aprovado sua media precisa ser acima de 7).

## **Utilização:**

Após executar o arquivo `main.py`, devem ser inseridos gabaritos e alunos, no diretorio `postman-tests` existem alguns exemplos que foram utilizados durante a produção da aplicação. 

Através do metodo POST podem ser inseridos alunos e gabaritos.

Cadastrar aluno alunos:

![cadastroAluno](https://user-images.githubusercontent.com/11688998/106030489-fff7bf80-60ac-11eb-8f2d-673576551581.png)

Cadastrar gabaritos: 

![cadastroGabarito](https://user-images.githubusercontent.com/11688998/106031067-8f9d6e00-60ad-11eb-8caf-0233dab16c88.png)

A resposta de provas também é feita pelo Metodo POST, da seguinte forma:

Resposta de provas (CPF e ID da prova são enviados junto no cabeçalho):

![cadastroRespostas](https://user-images.githubusercontent.com/11688998/106031425-06d30200-60ae-11eb-9cae-31a0123e6a0c.png)

A lista de alunos aprovados é retornada em modo json com metodo GET na rota /aprovados:
![listaAprovados](https://user-images.githubusercontent.com/11688998/106031737-5ca7aa00-60ae-11eb-86ad-6a6059d1a0da.png)

