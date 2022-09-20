# Criação de um portal de busca de vagas e headhunting com dinâmica similar apps como o Tinder

#### <u>Projeto de conclusão de curso do Grupo 2 do curso de Python Entra21 de 2022</u>

### Desenvolvedores:
- ### Diego Dalmolini
- ### Felipe Sartorato
- ### João Paulo Correa Santini
- ### José Goetten
- ### Luiza Bicalho Pollmann
- ### Mark Odebrecht
- ### Nicolas Felipe da Silva
- ### Raquel Schwartz

### Orientador: Adriano Machado

#### 18/08/2022

- Início dos trabalhos, onde foram finalizadas a História do Usuário e a descrição da idéia;
- Foi inciado também o esboço das entidades do banco de dados do projeto, onde cada participante trará sugestões de como será a estrutura de registro de anunciantes e candidatos;

#### 19/08/2022

- Foi iniciada a criação da matriz de relacionamentos do banco de dados. Todos participaram da análise;

#### 22/08/2022

- Continuação da avaliação da matriz de relacionamentos, com participação do professor/orientador, Adriano;

#### 23/08/2022

- Foi criado o ambiente Django no repositório;
- Foi também feita conexão do repositório ao Linear[^1] para acompanhamento das tasks durante o projeto;

#### 25/08/2022

- Mark Odebrecht foi definido como o Project Owner;
- Iniciada a criação da primeira entidade no Django (Empresas);
- Criado o repositório de teste do projeto;
- Entidade "Empresas" registrada e carregada no Django;
  
#### 26/08/2022

- Unificação das bases de dados para todos os usuários na nuvem;
- foi feita a criação de banco de dados para o projeto e testes de criação de tabelas;

- todos os integrantes do grupo possuem acesso ao DB na nuvem;

#### 29/08/2022

- Daily Scrum realizado;
- Apenas um dos integrantes não havia conectado ao DB e foi auxiliado pelos outros componentes do grupo;
- Com exceção desse ponto, não há pendências ou dificuldades por parte dos integrantes;
- Durante a manhã foi feta a revisão e atualização da matriz dem entidades do projeto;
- Foram inciados ajustes e construções de classes no arquivo models, para adequar os campos do banco de dados às necessidades do projeto;
  

#### De 30/08/2022 a 08/09/2022

- Foi revisado o planejamento de entidades e aplicativos do projeto para que fique mais organizado;
- Foi criado o template about;
- Adicionados o app accounts e login required;
- Criados Forms de candidatos;

#### 09/09/2022

- Criação em formulário para checklists;
- Também trabalhou-se para evoluir o login para a página, já que teremos dois tipos de login diferente.

#### 12/09/2022

- Foi finalizada a revisão da estrutura do projeto;
- Serão 6 aplicações diferentes:
  - Login;
  - Cadastro empresas;
  - Cadastro Vagas;
  - Formas de pagamento;
  - Cadastro Candidatos;
  - Cadastro de CV;
- Criadas as diferentes branches no GitHub para as diferentes aplicações do projeto;
- Criados os apps no projeto;

### 15/09/2022

- Definido o número de aplicativos a serem usados no projeto. São cinco ao todo:
  - Candidatos (Dados de cadastro do candidato);
  - CV's (Cadastro dos dados profissionais);
  - Empresas (Dados de cadastro de empresas contratantes);
  - Vagas (Cadastro de vagas);
  - Tabela de preços;

- foi também definido o template de front-end (Jobzilla)[^2][^3];

### 16/09/2022

- Criada a conta de email para o grupo de trabalho;
- Esse endereço será usado para cadastro no Heroku, onde o prjeto será publicado;
- Endereço: grupo2pythonentra21@gmail.com;
- Senha: Grupo2entra21;
- Aberta a conta no Heroku;
- O endereço de email é o informado acima;
- A senha é: Grupo2entra2122&


### 20/09/2022

- Ajustes foram feitos nos aplicativos;
- A criação de perfis fora do app accounts trouxe dificuldades que foram corrigidas trazendo todos os registros de canididatos e empresas para esse app;
- Dessa forma, a estrutura de apps ficou como segue:
  - accounts (receberá todos os dados de candidatos e empresas);
  - candidatos (será o registro dos currículos dos candidatos);
  - vagas (registro das vagas);
  - tabela de preços (registro das informações e entidades relativas ao preço)


  
  


Referências:
[^1]: https://linear.app/
[^2]: https://github.com/G2-5-Entra2122/Proj_Entra21_Gr2/blob/feature/pro-11-atualizar-readme/Entidades_Grupo2_E4H.pdf
[^3]: https://github.com/G2-5-Entra2122/Proj_Entra21_Gr2/blob/feature/pro-11-atualizar-readme/Entidades_Grupo2_E4H.png