<p align="center">
  <img src="nova-logo.jpg" />
</p>

<h1 align="center">Experts 4 Hire</h1>

<h3 align="center">Criação de um portal de busca de vagas e headhunting com dinâmica similar apps como o Tinder</h3>

<p></p>

<h4 align="center"><u>Projeto de conclusão de curso do Grupo 2 do curso de Python Entra21 de 2022</u></h4>
<p></p>

### Desenvolvedores:
- ### Diego Dalmolini
- ### Felipe Sartorato
- ### João Paulo Correa Santini
- ### José Orli Goetten
- ### Luiza Bicalho Pollmann
- ### Mark Odebrecht
- ### Nicolas Felipe da Silva
- ### Raquel Schwartz

<p></p>

### Orientador: Adriano Machado


# Descrição da Idéia

## História do Usuário

Programação de sistema que conectará profissionais às vagas em empresas de tecnologia. 

Haverá o portal do profissional e o portal das oportunidades. A plataforma conectará as capacidades de forma prática e transparente, usando sistema de *match* para a escolha dos candidatos.

A aplicação será desenvolvida com Python, Django e MySQL.

## Inspiração

Experts 4 Hire é um ambiente resultante da busca por um sistema buscador de candidatos (por parte das empresas) e de vagas (por parte dos candidatos) mais transparente e direto.

Um portal que busca a simplificação e maior agilidade na visualização tanto de perfis, quanto de vagas, levando a maior assertividade no processo de contratação.

Nesse portal, é possível que as empresas anunciem suas vagas, identificando especificamente as tecnologias, e seus respectivos níveis de conhecimento desejados.

Estas informações servirão como filtros automáticos na apresentação dessas vagas a candidatos que tenham o perfil desejado. 

Isso traz leads mais diretos e efetivos para o contratante que pode escolher, entre os mini-currículos recebidos dos candidatos interessados, os perfis que mais se encaixam em sua busca por profissionais.

Para candidatos, a concentração de vagas de tecnologia em um único portal, economiza trabalho em filtros excessivos na busca por oportunidades, além de receberem acesso a vagas que estão em *match* com seus conhecimentos e aspirações financeiras.

## Como funciona o ambiente

### Cadastros de candidatos e empresas 

A dinâmica do portal consiste nos seguintes passos:

- Para candidatos:
  - Cadastro no sistema, composto por:
    - dados pessoais,
    - tecnologias de proficiência,
    - tecnologia de maior conhecimento;
    - tempo trabalhando com cada tecnologia,
    - tempo de carreira total em tecnologia,
    - montagem de mini-currículo,
    - carregamento de currículo completo em formato pdf (preferencialmente formatado de acordo com o sugerido pelo portal),
    - preenchimento de pretensão salarial (*range*),
    - lista de empresas para as quais não deseja que seu perfil seja apresentado, 
  - busca por vagas que combinem com suas aptidões, conhecimentos e pretensão salarial (somente após preenchimento completo do cadastro);

- Para empresas:
  - Cadastro no sistema Experts 4 Hire, composto por:
    - nome da empresa/contratante,
    - CNPJ, IE etc.,
    - endereço;
    - nome da pessoa responsável pelo perfil da empresa;
    - telefone para contato;
  - Cadastro das vagas:
    - título (nome da posição em aberto),
    - descrição da vaga,
    - preenchimento dos requisitos desejados em relação aos candidatos:
      - tecnologias que satisfazem o preenchimento da vaga,
      - tempo de carreira total,
      - tempo de carreira na tecnologia principal,
    - desafios da posição, ou em que o contratado irá atuar,
    - descrição da empresa (sem citar o nome),
    - evantuais benefícios oferecidos pela empresa,
    - tipo de contrato (CLT, CNPJ, temporário, estagiário etc.),
    - salário oferecido (range para que seja comparado com as pretensões dos candidatos);

### A dinâmica do ambiente

Candidatos preenchem seus cadastros e após o preenchimento completo têm acesso exclusivamente às vagas que se relacionam com seu perfil.

As empresas preenchem seus cadastros e também o cadastro da vaga. Somente após o cadastro da vaga, passarão a receber os mini-currículos de candidatos que se relacionam às vagas.

Pelos candidatos, as vagas são visualizadas somente com as descrições constantes no cadasatro da vaga, sem citar o nome da empresa.

O que o candidato verá são oportunidades para que exerça suas qualidades em uma empresa (independentemente de qual) sabendo que sua pretensão salarial será atendida e se canditará às que possuam as descrições que mais lhe agradarem.

Nos mini-currículos recebidos pela empresa, constarão apenas as tecnologias usuais aos candidatos, bem como outras informações que os mesmos considerem válidas (serão direcionados sobre o que podem informar, no momento da montagem do cadastro). Não constarão o nome ou qualquer outra informação pessoal do candidato.

Isso é feito, para que as competências técnicas sejam a primeira vitrine apresentada ao contratante, trazendo transparência ao processo para que nenhum tipo de viés prejudique a escolha inicial, seja ele por sexo, cor, idade etc.

A intenção é que, com os mini-currículos em mãos, o profissional responsável pelo anúncio possa tomar a decisão de quais perfis completos deseja visualizar, seja por decisão própria ou por intermédio da análise dos mesmos que podem ser impressos e apresentados ao superior responsável pela posição.


### Bugs conhecidos em 21/10/2022

- Sistema de match não rodando;
- Sistema de alteração de senhas;
- Página de vaga individual contendo quadros do template que devem ser deletados;
- Menu suspenso não aparece em aparelhos mobile em visualização vertical. Em visualização horizontal, o menu suspenso aparece e não recolhe;
- Logos de empresas (página inicial) aparecem comprimidos na visualização vertical;
- Adicionar vagas não funcionando;



## Histórico das principais ações durante o projeto

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
  - app (terá todos os templates e arquivos estáticos do projeto);
  - candidatos (será o registro dos currículos dos candidatos);
  - tabela de preços (registro das informações e entidades relativas ao preço);
  - vagas (registro das vagas);


### 22/09/2022

- Foram criados nomes de empresas e candidatos fictícios para popular o banco de dados;
- Montado o Forms e Views do app Vagas;
- Feita uma função de mudança de senha no app accounts;
- No front-end já foi criado um repositório e um novo projeto Django para ajustes;
- Trabalhando no momento na página inicial (index) e na página Vagas;
- No back-end o trabalho está concentrado no form Habilidades, buscando um loop para especificar as habilidades por candidato;
- Será criada uma branch "Developer" de onde serão criadas todas as próximas branches;
- A branch Developer será administrada unicamente pelo PO, que também será responsável pelos merges com a Main;
- O arquivo README será atualizado diretamente nessa branch;
- Continuando o trabalho do form Candidatos;


### 26/09/2022
- Front-end finalizará a página inicial da página web e revisará as cores de acordo com nova logo desenvolvida;
- Também será analisada uma drop-window que não tem funcionado corretamente;
- Será montada a seção sobre, referente aos criadores do projeto;
- No back-end será buscada a validação de e-mails pelos usuários;


### 27/09/2022

- Demandas:
  - Criação de listagem de todas as vagas criadas no DB para apresentar na página inicial;
  - List view que apresente as vagas próprias de cada empresa;
  - Limpar a árvore git do projeto;
  - Delete view, para deletar as vagas que devem ser descartadas;
  - Desenvolvimento da página de vagas com filtro;


### 29/09/2022

- Continuação do desenvolvimento da view da lista de vagas;
- Continuação do desenvolvimento da view "minhas vagas" (vagas exclusivas de cada anunciante);
- Front-end trabalhando na logo e figuras/imagens. Também foi resolvido problema com posicionamento de botões.
- Serão revisados os textos de rodapé e será iniciada a integração do front com o back;
- Também foram revisadas as cores de alguns temas;
- Serão montados header e footer para integração à base;
- Será iniciada a integração para a ocorrência de matches entre vagas e curriculos;
- Finalizado desenvolvimento da view vagas;


### 30/09/2022

- Demandas:
  - contador de vagas (front: colocar um count do id de vagas - nicolas);
  - ordenar: ficar só salario (mais alto para mais baixo e vice versa); vagas mais recentes para mais antigas; mais antigas para mais recentes: felipe e mark vao adicionar as variaveis de salario e data; 
  - mostrar 10...20... (front - nicolas)
  - demanda para back: colocar a variavel de data na publicação da vaga e a de salario (para fazer o ranqueamento);
  - verificarem se tem variavel categoria (full, back, front) - adicionar models (felipe);
  - nicolas: tirar palavra chave;
  - modalidade: presencial, hibrido, remoto (nicolas);
  - demanda posterior: depois que concluir essas demandas anteriores (principalmente a da data); ver se consegue implementar a parte do "tempo de postagem" para conseguir filtrar vagas mais recentes( mark, felipe e nicolas)
  - criar filtro de cidade (mark e felipe);
  - nicolas: tirar quadradinho de logos das empresas;
  - adicionar no models choices tipo de vaga: freelance; tempo integral; estagio; meio período; temporário; voluntário (felipe e mark);
  - mudar de "tipo de empresa" para "tamanho" e verificar os portes q estão definidos no models (nicolas)
  - ajustes no html de vagas;
  - mostrando xxx candidatos (nicolas, arrumar);
  - duvida tirada: os ordenar por da pagina de vagas, tem q ser na views e nao no front;
  - sobre candidatos: nao terá nome nem foto; tera: categoria (full, back etc etc); linguagens (perfil); nivel (jr; pleno, senior); contrato (estagio, pj, clt...); habilidades, resumo e local; 
  - alteração no models: local ser cidade e modalidade ser: hibrido, remoto ou presencial;
  - renomear no models perfil por categoria (diego);
  -  renomear no models perfil por categoria (no models vagas - felipe);
  - tirar palavra-chave (nicolas);
  - verificar a possibilidade de autopreencher localização a partir do cep ou usuario conseguir escrever cidade tendo opções previas pq o usuario é uma capivara;
  - candidatos seremos só nós - fazer essa alteração no banco de dados;
  - nicolas: remover tempo de postagem da pagina de candidatos;
  - nicolas: remover tipo de empresa  
  - inserção de busca de endereço por CEP
  - verificar



### 04/10/2022

- Foi revisado o model "contrato" no arquivo models.py do app vagas. Adicionados diferentes tipos de contratos;
- também, no mesmo app, foi criado o model/choices "jornada" para seleção da jornada da vaga;
- Revisão do progresso do projeto para fazer as migrações do DB;


### 07/10/2022

- Foram equalizados os nomes das choices entre os apps candidatos e vagas;

### 13/10/2022

- Construção de filtros para vagas;
- Será feito migrate para disponibilizar base de dados aos usuários no repositório local;


### 14/10/2022

- Ajustes na paginação da lista de vagas;
- continuação da construção de filtros de vagas;
- cadastramento de vagas no DB;
- finalizada a inserção do DB;
- lógica do match entre contratantes e candidatos em andamento;
- Nova demanda: criar o html de visualização de uma vaga selecionada;

### 17/10/2022

- Filtros para a página de vagas construídos e funcionando parcialmente. Apenas filtra corretamente, se todos os campos estiverem selecionados.
- Se alguma janela suspensa não sofre modificação, retorna a mensagem de que não há vagas disponíveis;
- Também foi trabalhado na enumeração, contagem e compressão de objetos;

### 18/10/2022

- Finalizado o filtro de vagas;
- Novas demandas:
  - incorporar a parte do filtro da página de lista de vagas e dar pull request;
  - incorporar a pagina de lista de candidatos + pagina de detalhe de candidato;
  - arrumar about (botão do linktree); e fazer o pull request;
  - dar o pull request na pagina de preços;
  - arrumar o "mostrando 2150 vagas" na pagina de lista de vagas;


 
Referências:
[^1]: https://linear.app/
[^2]: https://github.com/G2-5-Entra2122/Proj_Entra21_Gr2/blob/feature/pro-11-atualizar-readme/Entidades_Grupo2_E4H.pdf
[^3]: https://github.com/G2-5-Entra2122/Proj_Entra21_Gr2/blob/feature/pro-11-atualizar-readme/Entidades_Grupo2_E4H.png