# Resultado - Desáfio CoorLab

### Documentação de Dependências do Projeto

#### Dependências do Vue3:
- **[@vuepic/vue-datepicker](https://www.npmjs.com/package/@vuepic/vue-datepicker)** (Versão: 8.3.1)
  - Descrição: Componente datepicker para Vue3, que fornece funcionalidade de seleção de datas.
  - Uso: Utilizado para selecionar datas no frontend do projeto.

- **[vue](https://v3.vuejs.org/)** (Versão: 3.4.21)
  - Descrição: Vue.js é um framework para construir interfaces de usuário, focando na camada de visualização.
  - Uso: A biblioteca principal para construir os componentes frontend e gerenciar o estado da aplicação.

- **[vue-material-design-icons](https://www.npmjs.com/package/vue-material-design-icons)** (Versão: 5.3.0)
  - Descrição: Coleção de ícones Material Design como componentes Vue em um único arquivo.
  - Uso: Fornece ícones para vários elementos de UI no frontend do projeto.

- **[vuetify](https://vuetifyjs.com/)** (Versão: 3.5.11)
  - Descrição: Vuetify é um framework de componentes Material Design para Vue.js.
  - Uso: Seletor de opções, com dropdown.

#### DevDependencies:
- **[@mdi/font](https://www.npmjs.com/package/@mdi/font)** (Versão: 7.4.47)
  - Descrição: Material Design Icons, uma biblioteca de ícones para projetos web.
  - Uso: Fornece ícones adicionais do Material Design para uso no projeto.

- **[@types/vue](https://www.npmjs.com/package/@types/vue)** (Versão: 2.0.0)
  - Descrição: Definições de tipos TypeScript para Vue.js.
  - Uso: Permite a verificação de tipos em componentes Vue ao usar TypeScript.

- **[@vitejs/plugin-vue](https://www.npmjs.com/package/@vitejs/plugin-vue)** (Versão: 5.0.4)
  - Descrição: Plugin Vue 3 para Vite, uma ferramenta de construção rápida.
  - Uso: Integra o Vue 3 com o Vite para desenvolvimento e empacotamento eficientes.

- **[typescript](https://www.typescriptlang.org/)** (Versão: 5.2.2)
  - Descrição: TypeScript é um superset fortemente tipado de JavaScript que compila para JavaScript puro.
  - Uso: Permite escrever código seguro em tipos nos componentes Vue.

- **[vite](https://vitejs.dev/)** (Versão: 5.1.6)
  - Descrição: Vite é uma ferramenta de construção de frontend de próxima geração que melhora significativamente a experiência de desenvolvimento frontend.
  - Uso: Usado como ferramenta de construção para o projeto Vue 3, fornecendo desenvolvimento rápido e substituição de módulos facilitado.

### Backend (Python 3.8) Dependências:
- **[Flask](https://flask.palletsprojects.com/)**: Flask é um framework de aplicação web WSGI leve em Python.
  - Uso: Usado para criar os endpoints da API backend e servir o backend do projeto.

- **[CORS](https://flask-cors.readthedocs.io/en/latest/)**: CORS (Cross-Origin Resource Sharing) é um mecanismo que permite que recursos restritos em uma página da web sejam solicitados de outro domínio fora do domínio de onde o recurso se originou.
  - Uso: Utilizado para lidar com o Cross-Origin Resource Sharing no backend do Flask, permitindo solicitações frontend para a API backend de diferentes origens.

Essas dependências foram utilizadas no projeto para o desenvolvimento frontend, incluindo componentes Vue.js, gerenciamento de estado, design de UI com Vuetify, e desenvolvimento backend com Flask para criação e gerenciamento de APIs.


## Estrutura do Projeto

O projeto foi organizado de maneira simples, com como a pasta principal `app` onde pode ser encontrado a pasta **backend** e **frontend**, no backend pode ser encontrado em python, onde terá o código em Flask que foi utilizado. Um arquivo `data.json` aonde foi armazenado os dados dos bilhetes de viagem. Este arquivo contém as informações sobre as viagens disponíveis, como nome da empresa, preço, tipo de assento, etc.

### Rotas da API

Foram definidas duas rotas principais para a API:

- **`/api/locals`** (método GET): Esta rota retorna a lista de cidades disponíveis para seleção de destino.
- **`/api/ticket`** (método POST): Esta rota é usada para buscar e retornar os bilhetes de viagem com base na cidade selecionada.

### Lógica de Busca e Seleção de Bilhetes

- A função `search_ticket_per_city` foi criada para filtrar os bilhetes com base na cidade selecionada.
- A função `find_cheapest_fastest_tickets` foi implementada para encontrar o bilhete mais barato e o mais rápido. Esta função compara os preços de bilhetes de conforto e econômico para determinar o tipo de assento mais barato.
- Os bilhetes são então retornados como objetos JSON contendo informações como nome da empresa, preço, duração, tipo de assento e código do assento.

### Gerenciamento de Requisições e Respostas

- O Flask foi configurado para lidar com solicitações POST e GET usando as bibliotecas Flask e request.
- As respostas da API são formatadas como JSON usando a função `jsonify` do Flask, tornando fácil para o frontend consumir os dados.

### Arquivo JSON de Dados

- O arquivo `data.json` foi utilizado como fonte de dados para os bilhetes de viagem. Este arquivo contém os detalhes dos bilhetes, como preço, duração, tipo de assento, etc.

### Integração com o Frontend

- A API Flask backend foi integrada ao frontend Vue.js para permitir que os usuários visualizem e selecionem as opções de viagem de forma interativa.

Este é um resumo geral do processo de desenvolvimento, destacando a utilização do Flask para criar o backend da aplicação, a implementação das rotas da API, a lógica de busca e seleção de bilhetes, e a integração com o frontend Vue.js para proporcionar uma experiência de usuário completa.

## Considerações Finais

Em resumo, o desenvolvimento da Calculadora de Viagens foi uma jornada interessante que me permitiu aprender uma nova stack, diversas tecnologias e novos conceitos. A integração entre o backend e o frontend, a lógica de busca de bilhetes e a estrutura do projeto foram aspectos fundamentais que, somados, representam o conhecimento adquirido durante o período de desenvolvimento deste projeto.