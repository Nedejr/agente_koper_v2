# 📚 Documentação: Passo a passo - Módulo de Engenharia


[video:https://youtu.be/BdLq4eBgfxQ?si=Sxmnm__Ai1ReGR0_]


**🎥 Vídeo Original:** https://youtu.be/BdLq4eBgfxQ?si=Sxmnm__Ai1ReGR0_

**📊 Total de Seções:** 22

---

---

## 1. Cadastro da Obra no Módulo de Engenharia

**📋 METADADOS:**
- **ID:** sec_1
- **⏱️ Minutagem:** 00:03 → 02:37
- **⏲️ Duração:** 154s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/BdLq4eBgfxQ?si=Sxmnm__Ai1ReGR0_&t=3)
- **📦 Módulo:** Engenharia
- **🏷️ Categorias:** Cadastro, Operacional, Configuração
- **🔑 Palavras-chave:** cadastro, obra, tipo de obra, campos obrigatórios, estrutura da obra

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de cadastro de uma obra no módulo de engenharia, incluindo a seleção do tipo de obra, preenchimento de campos obrigatórios e opções para adicionar informações complementares.

**Contexto:**
Estamos no módulo de engenharia de um sistema de gestão, onde o objetivo é cadastrar uma nova obra, definindo suas características e estrutura.

**Localização no Sistema:**
- Caminho de navegação: Menu Principal > Módulo Engenharia > Cadastro de Obra
- Tela/interface específica: Tela de Cadastro de Obra

**Funcionalidade Detalhada:**
O cadastro da obra permite que os usuários insiram informações essenciais sobre um projeto de construção. É crucial para a gestão de obras, pois possibilita o acompanhamento e a organização de dados relevantes. O sistema oferece uma versão tradicional para facilitar o preenchimento.

### 🔹 Passo a Passo Detalhado:

1. **Selecionar a Versão Tradicional**
   - Localização: Tela de Cadastro de Obra
   - Como fazer: Clique na opção **"Versão Tradicional"** para iniciar o cadastro.
   - Resultado esperado: A interface de cadastro se ajusta para permitir o preenchimento dos dados.

2. **Selecionar o Tipo da Obra**
   - Localização: Campo **"Tipo da Obra"**
   - Como fazer: Escolha entre as opções disponíveis: **"Obra Própria"** ou **"Obra para Terceiro"**.
   - Observações importantes: A seleção do tipo de obra abrirá novos campos para preenchimento.
   - Resultado esperado: Campos adicionais aparecem para coleta de informações específicas.

3. **Preencher Campos Obrigatórios**
   - Localização: Campos subsequentes após a seleção do tipo de obra
   - Como fazer: Preencha os campos obrigatórios, que possuem um asterisco (*) ao lado. Os campos incluem:
     * `Nome da Obra`: Nome que identifica a obra.
     * `Data de Início`: Data em que a obra começará.
   - Resultado esperado: Os campos obrigatórios são preenchidos corretamente.

4. **Adicionar Tipos de Obra Pré-Cadastrados**
   - Localização: Botão **"Mais Adicionar"**
   - Como fazer: Clique no botão para cadastrar um novo tipo de obra caso o desejado não esteja na lista pré-cadastrada.
   - Resultado esperado: Uma nova interface para cadastro de tipo de obra é exibida.

5. **Definir a Estrutura da Obra**
   - Localização: Seção **"Estrutura da Obra"**
   - Como fazer: Responda às perguntas sobre a estrutura da obra, como:
     * **Possui blocos?** Se sim, selecione **"Sim"** e insira a quantidade de blocos.
     * **Possui andares?** Se sim, selecione **"Sim"** e insira o número de andares.
     * **Unidades por andar:** Insira a quantidade de unidades por andar.
   - Resultado esperado: A estrutura da obra é definida com base nas respostas fornecidas.

6. **Inserir Endereço da Obra**
   - Localização: Campo **"Endereço da Obra"**
   - Como fazer: Preencha o endereço completo onde a obra será realizada.
   - Resultado esperado: O endereço da obra é salvo no sistema.

7. **Salvar o Cadastro da Obra**
   - Localização: Botão **"Salvar"**
   - Como fazer: Clique no botão **"Salvar"** para finalizar o cadastro.
   - Resultado esperado: A obra é cadastrada com sucesso no sistema.

8. **Adicionar Imagem e Organizar Documentos**
   - Localização: Seções específicas para imagem e documentos
   - Como fazer: Utilize as opções disponíveis para adicionar uma imagem da obra e organizar documentos relevantes.
   - Resultado esperado: A obra cadastrada possui uma imagem e documentos organizados.

**Campos e Parâmetros:**

| Campo                  | Tipo         | Obrigatório | Descrição                                         | Exemplo                   |
|------------------------|--------------|-------------|---------------------------------------------------|---------------------------|
| Nome da Obra           | Texto        | Sim         | Nome que identifica a obra.                       | "Construção do Prédio A"  |
| Data de Início         | Data         | Sim         | Data em que a obra começará.                      | "01/01/2024"              |
| Tipo da Obra           | Dropdown     | Sim         | Tipo de obra (própria ou para terceiro).         | "Obra Própria"            |
| Estrutura da Obra      | Texto        | Não         | Informações sobre blocos, andares e unidades.    | "3 blocos, 5 andares"     |
| Endereço da Obra       | Texto        | Sim         | Endereço completo da obra.                        | "Rua Exemplo, 123"        |

**Regras de Negócio:**
- Campos com asterisco (*) são obrigatórios.
- O tipo de obra selecionado determina quais campos adicionais serão exibidos.
- A estrutura da obra deve ser preenchida de acordo com a realidade do projeto.

**Observações Importantes:**
- Sempre preencha os campos obrigatórios para evitar erros de cadastro.
- Utilize a opção de adicionar novos tipos de obra se necessário.
- Verifique se a obra está finalizada antes de salvar.

**Conceitos-Chave:**
- **Obra Própria**: Projeto que a empresa realiza para si mesma.
- **Obra para Terceiro**: Projeto que a empresa realiza para um cliente.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                  | Solução                                      | Prevenção                                   |
|-----------------------------------|----------------------------------|----------------------------------------------|---------------------------------------------|
| Campo "Salvar" desabilitado       | Campos obrigatórios não preenchidos | Preencha todos os campos obrigatórios.      | Verifique sempre os campos antes de salvar. |
| Tipo de obra não aparece          | Não selecionou a versão correta | Selecione a **"Versão Tradicional"**.      | Sempre inicie pelo modo correto.           |

**💡 DICAS E BOAS PRÁTICAS:**
- Utilize a versão tradicional para um preenchimento mais ágil.
- Verifique se todos os campos obrigatórios estão preenchidos antes de salvar.
- Organize os documentos relacionados à obra logo após o cadastro.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Cadastro de uma Obra Própria**
```
Situação: A empresa está construindo um novo prédio.
Ação: 
  • Campo Nome da Obra: "Construção do Prédio A"
  • Campo Data de Início: "01/01/2024"
  • Tipo da Obra: "Obra Própria"
  • Estrutura: "2 blocos, 4 andares, 2 unidades por andar"
Resultado: A obra é cadastrada com sucesso e está pronta para acompanhamento.
```

**Exemplo 2: Cadastro de uma Obra para Terceiro**
```
Situação: A empresa está realizando uma reforma para um cliente.
Ação: 
  • Campo Nome da Obra: "Reforma do Escritório do Cliente X"
  • Campo Data de Início: "15/02/2024"
  • Tipo da Obra: "Obra para Terceiro"
  • Estrutura: "1 bloco, 1 andar, 5 unidades"
Resultado: A obra é cadastrada e os dados do cliente podem ser organizados.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** Acesso ao módulo de engenharia.
- **Habilita:** Geração de ordens de compra relacionadas à obra cadastrada.
- **Relacionado a:** Módulo de Compras, onde as ordens de compra são geradas.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como cadastrar uma obra?"
- **Com problema:** "Não consigo cadastrar uma obra, o que fazer?"
- **Informal:** "Como eu coloco uma obra no sistema?"
- **Por sintoma:** "O que fazer se o botão de salvar não está habilitado?"
- **Com dúvida:** "Quais campos são obrigatórios para cadastrar uma obra?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Criar obra", "Adicionar obra", "Cadastrar obra", "Novo projeto", "Registrar obra"
- "Obra própria", "Obra para cliente", "Projeto de construção"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como faço para cadastrar uma nova obra?
- Quais campos são obrigatórios no cadastro de uma obra?
- O que fazer se o tipo de obra que quero não está na lista?
- O que fazer se o botão de salvar não está habilitado?
- O que preciso ter feito antes de cadastrar uma obra?

---


---


---

## 2. Cadastro de Obras e Estruturas

**📋 METADADOS:**
- **ID:** sec_2
- **⏱️ Minutagem:** 02:34 → 05:08
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/BdLq4eBgfxQ?si=Sxmnm__Ai1ReGR0_&t=154)
- **📦 Módulo:** Cadastro de Obras
- **🏷️ Categorias:** Configuração, Cadastro, Estrutura, Administração
- **🔑 Palavras-chave:** cadastro, obra, unidades, blocos, andares, editar, anexar, financeiro

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de cadastro de obras e suas respectivas estruturas no sistema, incluindo a adição de blocos, unidades e andares, além de como editar informações e anexar documentos relevantes.

**Contexto:**
Estamos no módulo de Cadastro de Obras, onde o usuário pode organizar e estruturar informações sobre projetos de construção. O objetivo desta seção é guiar o usuário na criação e edição de obras, facilitando a gestão de informações essenciais.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Cadastro de Obras > Tela de Cadastro de Obras
- Tela/interface específica: Tela de Cadastro de Obras

**Funcionalidade Detalhada:**
Esta funcionalidade permite que os usuários cadastrem obras, organizando-as em pastas e adicionando informações sobre blocos, unidades e andares. É possível editar as áreas das unidades, alterar nomes e anexar documentos, além de registrar informações financeiras relacionadas à obra.

### 🔹 Passo a Passo Detalhado:

1. **Criar Pasta**
   - Localização: Tela de Cadastro de Obras
   - Como fazer: Clique no botão **Criar Pasta**, insira o nome desejado e clique em **Adicionar**.
   - Campos/Opções disponíveis:
     * `Nome da Pasta`: Campo de texto para inserir o nome da nova pasta.
   - Resultado esperado: A nova pasta é criada e aparece na lista de pastas disponíveis.

2. **Adicionar Documentos à Pasta**
   - Localização: Dentro da pasta recém-criada
   - Como fazer: Selecione a pasta e clique em **Adicionar Documentos**. Selecione os arquivos desejados e clique em **Confirmar**.
   - Resultado esperado: Os documentos são anexados à pasta selecionada.

3. **Adicionar Estruturas (Blocos, Unidades, Andares)**
   - Localização: Tela de Cadastro de Obras
   - Como fazer: Clique no botão **Mais Estrutura**. Selecione a opção desejada (Bloco, Nível ou Unidade) e preencha os campos necessários.
   - Observações importantes: Certifique-se de selecionar a opção correta para evitar confusões.
   - Resultado esperado: A estrutura selecionada é adicionada à obra.

4. **Editar Áreas das Unidades**
   - Localização: Tela de Cadastro de Obras
   - Como fazer: Selecione as unidades que deseja editar, insira a área privativa e a área comum nos campos correspondentes e clique em **Salvar**.
   - Campos/Opções disponíveis:
     * `Área Privativa`: Campo numérico para inserir a área privativa em m².
     * `Área Comum`: Campo numérico para inserir a área comum em m².
   - Resultado esperado: As áreas das unidades selecionadas são atualizadas.

5. **Editar Nomes das Unidades**
   - Localização: Tela de Cadastro de Obras
   - Como fazer: Clique em **Editar Nomes**, selecione a unidade e altere o nome conforme necessário. Clique em **Concluir Edição**.
   - Resultado esperado: O nome da unidade é atualizado.

6. **Anexar Arquivos às Unidades**
   - Localização: Dentro da unidade específica
   - Como fazer: Selecione a unidade e clique em **Anexar Arquivos**. Escolha os arquivos desejados e clique em **Confirmar**.
   - Resultado esperado: Os arquivos são anexados à unidade selecionada.

7. **Definir Valor da Unidade**
   - Localização: Dentro da unidade específica
   - Como fazer: Se a unidade for vendável, clique em **Definir Valor** e insira o valor da planta.
   - Campos/Opções disponíveis:
     * `Valor da Unidade`: Campo numérico para inserir o valor da planta.
   - Resultado esperado: O valor da unidade é registrado.

8. **Associar Vagas de Garagem e Subunidades**
   - Localização: Dentro da unidade específica
   - Como fazer: Clique em **Adicionar Vagas de Garagem** para associar vagas e em **Adicionar Subunidades** para incluir cômodos como quarto, sala e banheiro.
   - Campos/Opções disponíveis:
     * `Nome da Subunidade`: Campo de texto para inserir o nome do cômodo.
     * `Área da Subunidade`: Campo numérico para inserir a área do cômodo.
   - Resultado esperado: As vagas de garagem e subunidades são associadas à unidade.

9. **Lançar Receitas e Despesas**
   - Localização: Módulo Financeiro
   - Como fazer: Após o cadastro da obra, acesse o módulo financeiro e insira as receitas e despesas relacionadas à obra.
   - Resultado esperado: As informações financeiras são registradas e vinculadas à obra.

**Campos e Parâmetros:**

| Campo                   | Tipo       | Obrigatório | Descrição                                      | Exemplo                  |
|-------------------------|------------|-------------|------------------------------------------------|--------------------------|
| Nome da Pasta           | Texto      | Sim         | Nome da nova pasta a ser criada                | "Documentos da Obra"    |
| Área Privativa          | Numérico   | Sim         | Área privativa da unidade em m²                | 50                       |
| Área Comum              | Numérico   | Sim         | Área comum da unidade em m²                    | 20                       |
| Valor da Unidade        | Numérico   | Sim         | Valor da planta da unidade                      | 300000                   |
| Nome da Subunidade      | Texto      | Não         | Nome do cômodo a ser adicionado                | "Quarto Principal"       |
| Área da Subunidade      | Numérico   | Não         | Área do cômodo em m²                           | 15                       |

**Regras de Negócio:**
- É necessário criar uma pasta antes de adicionar documentos.
- As áreas das unidades podem ser editadas em lote.
- O valor da unidade deve ser inserido apenas se a unidade for vendável.
- Subunidades são opcionais e podem ser adicionadas a qualquer momento.

**Observações Importantes:**
- Verifique se todas as informações estão corretas antes de salvar.
- Evite duplicar nomes de unidades para facilitar a identificação.
- Os documentos anexados devem estar em formatos suportados pelo sistema.

**Conceitos-Chave:**
- **Bloco**: Estrutura física que compõe a obra.
- **Unidade**: Espaço vendável dentro da obra, como apartamentos ou salas.
- **Subunidade**: Cômodos que compõem uma unidade, como quartos e banheiros.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                | Solução                                         | Prevenção                                   |
|-----------------------------------|-------------------------------|------------------------------------------------|---------------------------------------------|
| Não consigo criar uma pasta       | Campo de nome vazio           | Preencha o campo "Nome da Pasta" e tente novamente | Sempre verifique os campos obrigatórios     |
| Erro ao adicionar documentos       | Formato de arquivo não suportado | Verifique se o arquivo está em um formato aceito | Consulte a lista de formatos suportados     |
| Não consigo editar a unidade      | Unidade não selecionada       | Selecione a unidade desejada antes de editar   | Sempre selecione a unidade correta          |
| Valor da unidade não é aceito     | Valor fora do intervalo permitido | Insira um valor válido e tente novamente       | Consulte as diretrizes de valores permitidos |

**💡 DICAS E BOAS PRÁTICAS:**
- Utilize nomes descritivos para pastas e unidades para facilitar a busca.
- Sempre revise as informações antes de concluir o cadastro.
- Utilize a funcionalidade de edição em lote para otimizar o processo.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Cadastro de uma nova obra**
```
Situação: Cadastro de uma nova obra chamada "Residencial Jardim".
Ação: 
  • Criar Pasta: "Residencial Jardim"
  • Adicionar Blocos: "Bloco A"
  • Adicionar Unidades: "Apartamento 101"
Resultado: A obra "Residencial Jardim" é criada com o Bloco A e o Apartamento 101.
```

**Exemplo 2: Edição de unidades existentes**
```
Situação: Alterar a área do Apartamento 101.
Ação: 
  • Selecionar Apartamento 101
  • Editar Área Privativa: 55 m²
  • Editar Área Comum: 25 m²
Resultado: As áreas do Apartamento 101 são atualizadas para 55 m² e 25 m², respectivamente.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** É necessário ter acesso ao módulo de Cadastro de Obras.
- **Habilita:** O cadastro de obras permite o lançamento de receitas e despesas no módulo financeiro.
- **Relacionado a:** Funcionalidades de relatórios financeiros e gestão de documentos.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como cadastrar uma obra?"
- **Com problema:** "Não consigo adicionar unidades, o que fazer?"
- **Informal:** "Como faço pra criar uma nova pasta?"
- **Por sintoma:** "O que fazer se não consigo editar a área da unidade?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Criar pasta", "adicionar pasta", "nova pasta", "cadastrar pasta"
- "Adicionar bloco", "inserir unidade", "editar unidade"
- "Anexar documento", "subir arquivo", "carregar documento"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como criar uma nova pasta para uma obra?
- O que fazer se não consigo adicionar documentos à pasta?
- Como editar as áreas das unidades cadastradas?
- O que fazer se o valor da unidade não é aceito?
- O que preciso ter feito antes de cadastrar uma obra?

---


---


---

## 3. Geração de Orçamentos no Sistema

**📋 METADADOS:**
- **ID:** sec_3
- **⏱️ Minutagem:** 05:05 → 07:39
- **⏲️ Duração:** 154s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/BdLq4eBgfxQ?si=Sxmnm__Ai1ReGR0_&t=305)
- **📦 Módulo:** Orçamentos
- **🏷️ Categorias:** Orçamentação, Cadastro, Relatórios
- **🔑 Palavras-chave:** orçamento, BDI, composições, serviços, etapas

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de geração de orçamentos no sistema, orientando sobre a escolha do tipo de orçamento, preenchimento de campos e opções disponíveis, além de esclarecer a importância de cada etapa.

**Contexto:**
Estamos na funcionalidade de geração de orçamentos dentro do módulo de Orçamentos do sistema. O objetivo é permitir que usuários que executam serviços possam criar orçamentos de forma eficiente e prática, utilizando as opções adequadas.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Orçamentos > Geração de Orçamentos
- Tela/interface específica: Tela de Geração de Orçamentos

**Funcionalidade Detalhada:**
A funcionalidade de geração de orçamentos permite que os usuários criem orçamentos para serviços prestados. É recomendável que aqueles que executam serviços selecionem a opção de "orçamentos por serviços", pois isso simplifica o processo, evitando a necessidade de vincular serviços a composições e insumos, que é mais adequado para orçamentistas.

### 🔹 Passo a Passo Detalhado:

1. **Clique em "Mais Orçamento"**
   - Localização: Botão **Mais Orçamento** na tela de Geração de Orçamentos.
   - Como fazer: Clique no botão **Mais Orçamento** para iniciar a criação de um novo orçamento.
   - Campos/Opções disponíveis:
     * `Tipo de Orçamento`: Selecione entre "Orçamento por Serviços" ou "Orçamento por Composições".
   - Resultado esperado: O sistema abre um formulário para preenchimento dos detalhes do orçamento.

2. **Selecionar o Tipo de Orçamento**
   - Localização: Dropdown **Tipo de Orçamento**.
   - Como fazer: Escolha a opção **Orçamento por Serviços** para facilitar a execução do serviço.
   - Observações importantes: A escolha do tipo de orçamento é crucial; orçamentos por composições são mais complexos e destinados a orçamentistas.
   - Resultado esperado: O sistema ajusta as opções disponíveis para o tipo de orçamento selecionado.

3. **Preencher Nome do Orçamento e BDI**
   - Localização: Campos **Nome do Orçamento** e **Valor do BDI**.
   - Como fazer: Insira o nome do orçamento desejado e o percentual do BDI que será aplicado.
   - Campos/Opções disponíveis:
     * `Nome do Orçamento`: Campo de texto para o nome do orçamento.
     * `Valor do BDI`: Campo numérico para inserir o percentual do BDI.
   - Resultado esperado: Os dados são salvos e utilizados no cálculo do orçamento.

4. **Associar Obra e Cliente (Opcional)**
   - Localização: Campos **Obra** e **Cliente**.
   - Como fazer: Preencha os campos se necessário, mas lembre-se que não são obrigatórios neste momento.
   - Observações importantes: A obra pode não ser necessária se o orçamento for para um possível cliente e não para uma obra já definida.
   - Resultado esperado: O orçamento é criado sem a necessidade de vinculação obrigatória a uma obra ou cliente.

5. **Escolher Opção de Arredondamento**
   - Localização: Opção de **Arredondamento**.
   - Como fazer: Selecione entre **Não Truncar Valores Unitários** ou **Truncar Valores Unitários**.
   - Observações importantes: "Não truncar" mantém as casas decimais originais, enquanto "truncar" desconsidera as casas decimais.
   - Resultado esperado: O sistema ajusta os valores do orçamento conforme a opção escolhida.

6. **Selecionar Base de Composições**
   - Localização: Dropdown **Base de Composições**.
   - Como fazer: Escolha entre a **Base da SINAP** ou a **Base Própria** da empresa.
   - Campos/Opções disponíveis:
     * `Base da SINAP`: Padrão do sistema.
     * `Base Própria`: Base personalizada da empresa.
   - Resultado esperado: O sistema ajusta as composições disponíveis para o orçamento.

7. **Selecionar Referência e Estado**
   - Localização: Campos **Referência** e **Estado**.
   - Como fazer: Preencha com a referência desejada e o estado correspondente.
   - Observações importantes: A referência é atualizada conforme a caixa atualiza, garantindo que as informações estejam sempre corretas.
   - Resultado esperado: As etapas e subetapas cadastradas são exibidas para seleção.

**Campos e Parâmetros:**

| Campo                     | Tipo         | Obrigatório | Descrição                                                                 | Exemplo               |
|---------------------------|--------------|-------------|---------------------------------------------------------------------------|-----------------------|
| Nome do Orçamento         | Texto        | Sim         | Nome que identifica o orçamento.                                         | "Orçamento João Silva"|
| Valor do BDI              | Numérico     | Não         | Percentual do BDI a ser aplicado ao orçamento.                          | 15%                   |
| Obra                      | Texto        | Não         | Nome da obra associada ao orçamento, se aplicável.                      | "Construção XYZ"      |
| Cliente                   | Texto        | Não         | Nome do cliente associado ao orçamento, se aplicável.                   | "Maria Oliveira"      |
| Arredondamento            | Opção        | Não         | Escolha entre truncar ou não os valores unitários.                      | "Não Truncar"        |
| Base de Composições       | Dropdown     | Sim         | Seleção entre a base da SINAP ou a base própria da empresa.             | "Base da SINAP"      |
| Referência                | Texto        | Sim         | Referência da composição a ser utilizada.                                | "Ref123"              |
| Estado                    | Dropdown     | Sim         | Estado relacionado à referência selecionada.                             | "SP"                  |

**Regras de Negócio:**
- O tipo de orçamento deve ser escolhido corretamente para evitar complicações na execução do serviço.
- A obra e o cliente não são obrigatórios, permitindo flexibilidade na criação de orçamentos.
- O sistema deve atualizar as composições conforme a referência e o estado selecionados.

**Observações Importantes:**
- É recomendado que usuários que executam serviços optem por "Orçamento por Serviços" para simplificar o processo.
- Evite associar um orçamento a uma obra se não houver certeza de que a obra será realizada.
- Verifique se as composições estão atualizadas antes de finalizar o orçamento.

**Conceitos-Chave:**
- **BDI (Benefício e Despesas Indiretas)**: Percentual aplicado sobre o custo do orçamento para cobrir despesas indiretas e lucro.
- **Base de Composições**: Conjunto de dados que contém as composições de serviços e insumos utilizados para orçamentação.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                             | Causa Provável                     | Solução                                          | Prevenção                                     |
|--------------------------------------|------------------------------------|--------------------------------------------------|-----------------------------------------------|
| Botão "Mais Orçamento" não aparece   | Permissões de usuário insuficientes| Verifique as permissões do usuário no sistema.   | Configure permissões adequadas para o usuário.|
| Erro ao salvar orçamento              | Campos obrigatórios não preenchidos| Preencha todos os campos obrigatórios corretamente.| Revise os campos antes de salvar.            |
| Valores do BDI não aplicados corretamente | Opção de arredondamento incorreta | Verifique a opção de arredondamento selecionada. | Escolha a opção correta antes de finalizar.  |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre verifique se a base de composições está atualizada antes de iniciar um novo orçamento.
- Utilize nomes claros e descritivos para os orçamentos para facilitar a identificação futura.
- Considere a possibilidade de criar orçamentos preliminares sem associar a uma obra ou cliente.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Orçamento para Serviço de Construção**
```
Situação: Um cliente solicita um orçamento para a construção de uma casa.
Ação: 
  • Clique em "Mais Orçamento".
  • Selecione "Orçamento por Serviços".
  • Nome do Orçamento: "Orçamento Casa João".
  • Valor do BDI: 20%.
  • Arredondamento: "Não Truncar".
Resultado: O orçamento é criado com os dados inseridos e está pronto para ser enviado ao cliente.
```

**Exemplo 2: Orçamento para Manutenção**
```
Situação: Um cliente solicita um orçamento para manutenção de um prédio.
Ação: 
  • Clique em "Mais Orçamento".
  • Selecione "Orçamento por Serviços".
  • Nome do Orçamento: "Orçamento Manutenção Prédio XYZ".
  • Valor do BDI: 10%.
  • Arredondamento: "Truncar".
Resultado: O orçamento é gerado com os valores arredondados conforme a opção escolhida.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O usuário deve ter permissões adequadas para acessar a funcionalidade de geração de orçamentos.
- **Habilita:** A criação de orçamentos permite a geração de relatórios financeiros e planejamento de obras.
- **Relacionado a:** Funcionalidades de cadastro de serviços e composições, que são utilizadas na criação de orçamentos.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como gerar um orçamento no sistema?"
- **Com problema:** "Não consigo criar um orçamento, o que fazer?"
- **Informal:** "Como faço um orçamento aqui?"
- **Por sintoma:** "Quando tento criar um orçamento, não aparece a opção."
- **Com dúvida:** "Qual a diferença entre orçamento por serviços e por composições?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Criar orçamento", "Adicionar orçamento", "Novo orçamento", "Cadastrar orçamento"
- "BDI", "Percentual de BDI", "Custo indireto"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como faço para gerar um orçamento no sistema?
- Quais campos são obrigatórios ao criar um orçamento?
- O que significa a opção de arredondamento no orçamento?
- O que fazer se o botão de gerar orçamento não estiver disponível?
- O que preciso ter configurado antes de criar um orçamento?

---


---


---

## 4. Cadastro de Etapas e Subetapas no Orçamento

**📋 METADADOS:**
- **ID:** sec_4
- **⏱️ Minutagem:** 07:36 → 10:12
- **⏲️ Duração:** 155s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/BdLq4eBgfxQ?si=Sxmnm__Ai1ReGR0_&t=456)
- **📦 Módulo:** Orçamento
- **🏷️ Categorias:** Configuração, Cadastro, Orçamento
- **🔑 Palavras-chave:** etapas, subetapas, cadastro, serviços, orçamento

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como cadastrar etapas e subetapas no sistema de orçamento, explicando a importância das etapas e como adicionar serviços a elas, além de esclarecer que as subetapas são opcionais e não impactam o valor final do orçamento.

**Contexto:**
Estamos na funcionalidade de cadastro de etapas e subetapas dentro do módulo de Orçamento. O objetivo é organizar a estrutura da obra, permitindo que o usuário crie um orçamento detalhado e bem estruturado.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Orçamento > Cadastro de Etapas
- Tela/interface específica: Tela de Cadastro de Etapas e Subetapas

**Funcionalidade Detalhada:**
A funcionalidade permite que o usuário cadastre etapas e subetapas para organizar a estrutura do orçamento. As etapas são obrigatórias e servem para categorizar os serviços, enquanto as subetapas são opcionais e servem apenas como uma especificação adicional. O usuário pode adicionar novos serviços a cada etapa e, caso não encontre um serviço desejado, pode cadastrá-lo diretamente.

### 🔹 Passo a Passo Detalhado:

1. **Selecionar uma Etapa**
   - Localização: Tela de Cadastro de Etapas
   - Como fazer: Clique na lista de etapas disponíveis e selecione uma etapa existente.
   - Resultado esperado: A etapa selecionada será destacada, permitindo que você adicione serviços a ela.

2. **Adicionar uma Subetapa (Opcional)**
   - Localização: Tela de Cadastro de Etapas
   - Como fazer: Caso deseje adicionar uma subetapa, clique no botão **+ Adicionar**.
   - Campos/Opções disponíveis:
     * `Nome da Subetapa`: Campo de texto para inserir o nome da subetapa.
   - Resultado esperado: A subetapa será cadastrada e associada à etapa selecionada.

3. **Cadastrar uma Nova Etapa**
   - Localização: Tela de Cadastro de Etapas
   - Como fazer: Clique no botão **+ Adicionar** ao lado da lista de etapas.
   - Campos/Opções disponíveis:
     * `Nome da Etapa`: Campo de texto para inserir o nome da nova etapa.
   - Resultado esperado: A nova etapa será cadastrada e aparecerá na lista de etapas disponíveis.

4. **Adicionar Serviços a uma Etapa**
   - Localização: Ao lado da etapa selecionada, clique nos três pontinhos (menu de opções).
   - Como fazer: Selecione a opção **Adicionar Serviço**.
   - Campos/Opções disponíveis:
     * `Nome do Serviço`: Campo de texto para inserir o nome do serviço.
     * `Unidade de Medida`: Dropdown para selecionar a unidade de medida (ex: metro quadrado, metro cúbico, diária).
     * `Categoria`: Dropdown para selecionar a categoria do serviço (ex: acabamento).
     * `Clima`: Checkbox para indicar se o clima pode afetar a execução do serviço.
     * `Descrição`: Campo de texto opcional para adicionar orientações sobre o serviço.
   - Resultado esperado: O serviço será adicionado à etapa selecionada.

5. **Cadastrar um Novo Serviço**
   - Localização: Tela de Adição de Serviços
   - Como fazer: Clique no botão **+ Adicionar** ao lado da lista de serviços.
   - Campos/Opções disponíveis:
     * `Nome do Serviço`: Campo de texto para inserir o nome do novo serviço.
     * `Unidade de Medida`: Dropdown para selecionar a unidade de medida.
     * `Categoria`: Dropdown para selecionar a categoria do serviço.
   - Resultado esperado: O novo serviço será cadastrado e aparecerá na lista de serviços disponíveis.

**Campos e Parâmetros:**

| Campo                | Tipo         | Obrigatório | Descrição                                                  | Exemplo                  |
|----------------------|--------------|-------------|-----------------------------------------------------------|--------------------------|
| Nome da Etapa       | Texto        | Sim         | Nome da etapa a ser cadastrada.                           | "Canteiro de Obras"     |
| Nome da Subetapa    | Texto        | Não         | Nome da subetapa a ser cadastrada.                        | "Preparação do Terreno" |
| Nome do Serviço      | Texto        | Sim         | Nome do serviço a ser cadastrado.                         | "Pintura"               |
| Unidade de Medida    | Dropdown     | Sim         | Unidade de medida do serviço (ex: m², m³, diária).       | "m²"                     |
| Categoria            | Dropdown     | Sim         | Categoria do serviço (ex: acabamento).                    | "Acabamento"            |
| Clima                | Checkbox     | Não         | Indica se o clima afeta a execução do serviço.            | [ ] Sim                 |
| Descrição            | Texto        | Não         | Orientações sobre a execução do serviço.                  | "Usar tinta acrílica."  |

**Regras de Negócio:**
- As etapas são obrigatórias para a criação do orçamento.
- As subetapas são opcionais e não impactam o valor final do orçamento.
- O usuário pode adicionar serviços a qualquer etapa selecionada.
- Caso um serviço não esteja disponível, o usuário pode cadastrá-lo diretamente.

**Observações Importantes:**
- É recomendado que as etapas sejam bem definidas para facilitar a organização do orçamento.
- Evite cadastrar serviços duplicados para manter a clareza na lista de serviços.
- Verifique se a unidade de medida está correta para evitar erros de cálculo.

**Conceitos-Chave:**
- **Etapa**: Categoria principal que organiza os serviços dentro do orçamento.
- **Subetapa**: Especificação adicional que pode ser utilizada para detalhar uma etapa.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                  | Solução                                         | Prevenção                          |
|-----------------------------------|----------------------------------|------------------------------------------------|------------------------------------|
| Não consigo adicionar uma etapa    | Campo de nome vazio              | Preencha o campo "Nome da Etapa" e tente novamente. | Sempre preencha todos os campos obrigatórios. |
| Serviço não aparece na lista       | Serviço não cadastrado           | Cadastre o serviço usando a opção **+ Adicionar**. | Verifique a lista antes de cadastrar. |
| Erro ao salvar a subetapa         | Nome da subetapa já existe      | Use um nome diferente para a subetapa.        | Verifique a lista de subetapas antes de cadastrar. |

**💡 DICAS E BOAS PRÁTICAS:**
- Utilize nomes descritivos para etapas e serviços para facilitar a identificação.
- Agrupe serviços semelhantes sob a mesma etapa para melhor organização.
- Revise as descrições dos serviços para garantir clareza nas orientações.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Cadastro de Etapa e Serviço**
```
Situação: Cadastro da etapa "Canteiro de Obras" e serviço "Pintura".
Ação: 
  • Campo Nome da Etapa: "Canteiro de Obras"
  • Campo Nome do Serviço: "Pintura"
  • Campo Unidade de Medida: "m²"
Resultado: A etapa "Canteiro de Obras" é criada e o serviço "Pintura" é adicionado a ela.
```

**Exemplo 2: Cadastro de Subetapa**
```
Situação: Cadastro da subetapa "Preparação do Terreno".
Ação: 
  • Campo Nome da Subetapa: "Preparação do Terreno"
Resultado: A subetapa "Preparação do Terreno" é cadastrada sob a etapa "Canteiro de Obras".
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O usuário deve ter acesso ao módulo de Orçamento.
- **Habilita:** A criação de um orçamento detalhado e organizado.
- **Relacionado a:** Funcionalidades de cadastro de serviços e relatórios de orçamento.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como cadastrar uma etapa no orçamento?"
- **Com problema:** "Não consigo adicionar uma subetapa, o que fazer?"
- **Informal:** "Como eu coloco uma nova etapa no orçamento?"
- **Por sintoma:** "O que fazer se a etapa não aparecer na lista?"
- **Com dúvida:** "Qual a diferença entre etapa e subetapa?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Adicionar etapa", "Cadastrar etapa", "Criar subetapa", "Inserir serviço"
- "Etapa de obra", "Subdivisão de etapa", "Serviço de obra"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como cadastrar uma nova etapa no orçamento?
- O que fazer se não consigo adicionar um serviço?
- Como adicionar uma subetapa a uma etapa existente?
- O que fazer se a etapa não aparece na lista?
- O que preciso ter antes de cadastrar serviços e etapas?

---


---


---

## 5. Checklists e Composições para Execução de Serviços

**📋 METADADOS:**
- **ID:** sec_5
- **⏱️ Minutagem:** 10:09 → 12:34
- **⏲️ Duração:** 145s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/BdLq4eBgfxQ?si=Sxmnm__Ai1ReGR0_&t=609)
- **📦 Módulo:** Execução de Serviços
- **🏷️ Categorias:** Configuração, Operacional, Checklist
- **🔑 Palavras-chave:** checklist, composição, insumos, EPI, equipamentos

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como utilizar checklists para garantir a conformidade na execução de serviços, além de associar composições necessárias para a realização das atividades. O objetivo é assegurar que todos os requisitos sejam atendidos antes e após a execução do serviço.

**Contexto:**
Estamos na interface de execução de serviços, onde o usuário pode iniciar e finalizar atividades, garantindo que todas as conformidades e insumos necessários sejam atendidos.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Execução de Serviços > Submenu Checklists e Composições
- Tela/interface específica: Tela de Execução de Serviços

**Funcionalidade Detalhada:**
A funcionalidade de checklists permite que o usuário verifique se todos os requisitos necessários para iniciar e finalizar um serviço estão atendidos. Os checklists são divididos em dois tipos: **Checklist Inicial** e **Checklist Final**. O primeiro é utilizado para garantir que todos os insumos e condições estão prontos para o início do serviço, enquanto o segundo assegura que todas as etapas foram concluídas corretamente antes da entrega final.

### 🔹 Passo a Passo Detalhado:

1. **Acessar o Checklist Inicial**
   - Localização: Tela de Execução de Serviços
   - Como fazer: Na tela de execução, localize a seção de **Checklist Inicial**. Aqui, você verá uma lista de itens que podem ser verificados.
   - Campos/Opções disponíveis:
     * `EPI`: Equipamentos de Proteção Individual necessários para a execução do serviço.
     * `Organização da Equipe`: Verificação da disposição e organização da equipe de trabalho.
     * `Local Limpo`: Confirmação de que o local de trabalho está limpo e organizado.
   - Resultado esperado: O usuário pode selecionar os itens que foram verificados, garantindo que todos os requisitos estão atendidos.

2. **Acessar o Checklist Final**
   - Localização: Tela de Execução de Serviços
   - Como fazer: Após a conclusão do serviço, vá até a seção de **Checklist Final**. Aqui, você deve verificar os itens necessários para finalizar o serviço.
   - Observações importantes: Embora o preenchimento dos checklists não seja obrigatório, é altamente recomendado para garantir a conformidade.
   - Resultado esperado: O usuário verifica e seleciona os itens que confirmam a entrega do EPI, equipamentos e a limpeza do local.

3. **Associar uma Composição ao Serviço**
   - Localização: Tela de Execução de Serviços
   - Como fazer: Na seção de **Composição**, clique no botão **Associar**. Se não houver composições associadas, você verá uma mensagem indicando que nenhuma composição está disponível.
   - Campos/Opções disponíveis:
     * `Pesquisar por Nomenclatura`: Campo para buscar composições pelo nome.
     * `Pesquisar por Código`: Campo para buscar composições pelo código.
   - Resultado esperado: O usuário pode selecionar uma composição existente ou, se necessário, cadastrar uma nova composição.

4. **Cadastrar uma Nova Composição**
   - Localização: Tela de Execução de Serviços
   - Como fazer: Clique no botão **Adicionar** para cadastrar uma nova composição. Preencha os campos necessários para registrar os insumos.
   - Campos/Opções disponíveis:
     * `Nome da Composição`: Nome que identifica a composição.
     * `Descrição`: Detalhes sobre os insumos que compõem o serviço.
   - Resultado esperado: A nova composição é cadastrada e pode ser associada ao serviço.

**Campos e Parâmetros:**

| Campo               | Tipo         | Obrigatório | Descrição                                           | Exemplo                   |
|---------------------|--------------|-------------|----------------------------------------------------|---------------------------|
| `EPI`               | Checkbox     | Não         | Equipamentos de Proteção Individual necessários     | "Capacete, Luvas"        |
| `Organização da Equipe` | Checkbox | Não         | Verificação da disposição da equipe                 | "Equipe organizada"       |
| `Local Limpo`       | Checkbox     | Não         | Confirmação de que o local está limpo              | "Local verificado"        |
| `Nome da Composição`| Texto        | Sim         | Nome da composição a ser cadastrada                 | "Composição de Pintura"   |
| `Descrição`         | Texto        | Sim         | Detalhes sobre os insumos da composição             | "Tinta, Pincéis, Rolo"   |

**Regras de Negócio:**
- O preenchimento dos checklists não é obrigatório, mas é altamente recomendado para garantir a conformidade.
- As composições devem ser associadas a cada serviço para garantir que todos os insumos necessários sejam considerados.
- Caso uma composição não esteja cadastrada, o usuário deve cadastrar uma nova antes de prosseguir.

**Observações Importantes:**
- É importante verificar todos os itens do checklist para evitar problemas durante a execução do serviço.
- Erros comuns incluem não verificar o local de trabalho, o que pode levar a atrasos na execução.
- As composições devem ser cadastradas antes da execução do serviço para evitar falta de insumos.

**Conceitos-Chave:**
- **Checklist Inicial**: Lista de verificação dos requisitos necessários antes de iniciar um serviço.
- **Checklist Final**: Lista de verificação dos requisitos necessários para finalizar um serviço.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                     | Solução                                         | Prevenção                                   |
|-----------------------------------|------------------------------------|------------------------------------------------|---------------------------------------------|
| Checklist não aparece             | Falta de permissões                | Verificar permissões do usuário em Admin > Usuários | Configurar permissões corretamente          |
| Não consigo associar composição    | Composição não cadastrada          | Cadastrar a composição antes de associar       | Cadastrar composições previamente           |
| Erro ao salvar checklist          | Campos obrigatórios não preenchidos| Preencher todos os campos obrigatórios          | Revisar checklist antes de salvar           |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre verifique os checklists antes de iniciar e finalizar um serviço.
- Utilize a pesquisa por nomenclatura ou código para encontrar composições mais rapidamente.
- Evite atrasos garantindo que todos os insumos estejam cadastrados antes da execução.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Início de um Serviço de Pintura**
```
Situação: Início do serviço de pintura em um escritório.
Ação: Preencher o checklist inicial.
  • Campo EPI: "Capacete, Luvas"
  • Campo Organização da Equipe: "Equipe organizada"
  • Campo Local Limpo: "Local verificado"
Resultado: Checklist inicial preenchido e serviço pode ser iniciado.
```

**Exemplo 2: Finalização de um Serviço de Limpeza**
```
Situação: Finalização do serviço de limpeza em um armazém.
Ação: Preencher o checklist final.
  • Campo EPI: "Luvas, Máscara"
  • Campo Organização da Equipe: "Todos os membros presentes"
  • Campo Local Limpo: "Local verificado"
Resultado: Checklist final preenchido e serviço finalizado com sucesso.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** As composições devem estar cadastradas antes da execução do serviço.
- **Habilita:** A associação de composições permite a execução de serviços com insumos adequados.
- **Relacionado a:** Funcionalidades de cadastro de composições e gerenciamento de serviços.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como usar checklists para serviços?"
- **Com problema:** "O que fazer se o checklist não aparece?"
- **Informal:** "Como checar se tudo está pronto para o serviço?"
- **Por sintoma:** "O que fazer se não consigo associar uma composição?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "verificação de requisitos", "lista de verificação", "itens de conformidade", "insumos necessários", "associar materiais"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como acessar e utilizar os checklists para serviços?
- O que fazer se não consigo associar uma composição ao serviço?
- Quais são os itens obrigatórios no checklist inicial?
- O que fazer se o checklist final não está salvando?
- O que preciso ter cadastrado antes de iniciar um serviço?

---


---


---

## 6. Cadastro de Composição de Insumos

**📋 METADADOS:**
- **ID:** sec_6
- **⏱️ Minutagem:** 12:40 → 15:09
- **⏲️ Duração:** 149s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/BdLq4eBgfxQ?si=Sxmnm__Ai1ReGR0_&t=760)
- **📦 Módulo:** Composição de Insumos
- **🏷️ Categorias:** Cadastro, Composição, Insumos, Orçamento
- **🔑 Palavras-chave:** composição, insumos, mão de obra, material, equipamento, valor unitário, cadastro

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como cadastrar uma composição de insumos no sistema, detalhando a inclusão de mão de obra, materiais e equipamentos, além de explicar a opção de criar composições globais.

**Contexto:**
Estamos na tela de cadastro de composições de insumos dentro do módulo de Composição de Insumos. O objetivo é permitir que o usuário crie uma nova composição, seja ela detalhada ou global, para facilitar a execução de serviços.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Composição de Insumos > Cadastro de Composição
- Tela/interface específica: Tela de Cadastro de Composição de Insumos

**Funcionalidade Detalhada:**
A funcionalidade de cadastro de composição de insumos permite ao usuário criar uma nova composição que pode incluir mão de obra, materiais e equipamentos necessários para a execução de um serviço. O sistema oferece a opção de adicionar insumos individualmente ou criar uma composição global, onde apenas os valores unitários são informados.

### 🔹 Passo a Passo Detalhado:

1. **Inserir Nome da Composição**
   - Localização: Campo de texto no topo da tela de cadastro
   - Como fazer: Clique no campo e digite o nome desejado para a composição. O nome pode ser o mesmo do serviço ou outro que você achar mais apropriado.
   - Resultado esperado: O nome da composição é salvo e exibido na tela.

2. **Adicionar Insumos**
   - Localização: Botão **Adicionar** na seção de insumos
   - Como fazer: Clique no botão **Adicionar** para incluir um novo insumo. 
   - Campos/Opções disponíveis:
     * `Tipo de Insumo`: Selecione entre **Mão de Obra**, **Material** ou **Equipamento**.
     * `Valor Unitário`: Insira o valor unitário do insumo.
     * `Quantidade Unitária`: Insira a quantidade que será utilizada.
   - Resultado esperado: O insumo é adicionado à composição e aparece na lista de insumos cadastrados.

3. **Cadastrar Insumo do Zero**
   - Localização: Botão **Mais Insumo**
   - Como fazer: Clique no botão **Mais Insumo** para cadastrar um insumo do zero, caso não tenha uma composição pré-existente.
   - Observações importantes: Certifique-se de que todos os campos obrigatórios estão preenchidos antes de salvar.
   - Resultado esperado: Um novo insumo é criado e adicionado à composição.

4. **Criar Composição Global**
   - Localização: Seção de criação de composição
   - Como fazer: Se você possui apenas o valor unitário da mão de obra e do material, clique em **Adicionar** e escolha a opção de composição global.
   - Resultado esperado: Uma composição global é criada, onde apenas os valores unitários são considerados.

5. **Finalizar Cadastro**
   - Localização: Botão **Salvar**
   - Como fazer: Após adicionar todos os insumos necessários, clique no botão **Salvar** para finalizar o cadastro da composição.
   - Resultado esperado: A composição é salva no sistema e pode ser utilizada em orçamentos futuros.

**Campos e Parâmetros:**

| Campo               | Tipo          | Obrigatório | Descrição                                                  | Exemplo                |
|---------------------|---------------|-------------|------------------------------------------------------------|------------------------|
| Nome da Composição   | Texto         | Sim         | Nome que identifica a composição no sistema.               | "Composição Serviço A" |
| Tipo de Insumo      | Dropdown      | Sim         | Tipo de insumo a ser adicionado (Mão de Obra, Material, Equipamento). | "Mão de Obra"         |
| Valor Unitário      | Numérico      | Sim         | Valor unitário do insumo.                                  | 150.00                 |
| Quantidade Unitária | Numérico      | Sim         | Quantidade do insumo que será utilizada.                   | 10                     |

**Regras de Negócio:**
- O nome da composição deve ser único para evitar duplicidade.
- O valor unitário deve ser um número positivo.
- A quantidade unitária deve ser um número inteiro e positivo.
- Composições globais podem ser criadas apenas quando não há insumos detalhados.

**Observações Importantes:**
- É recomendado que os usuários detalhem insumo por insumo para melhor controle.
- Erros comuns incluem não preencher campos obrigatórios, resultando em falha ao salvar.
- Verifique se você tem permissões adequadas para cadastrar composições.

**Conceitos-Chave:**
- **Composição de Insumos**: Conjunto de insumos necessários para a execução de um serviço.
- **Composição Global**: Composição que utiliza apenas valores unitários sem detalhamento de insumos.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                   | Solução                                           | Prevenção                                   |
|-----------------------------------|----------------------------------|--------------------------------------------------|---------------------------------------------|
| Não consigo salvar a composição    | Campos obrigatórios não preenchidos | Preencha todos os campos obrigatórios e tente novamente. | Verifique os campos antes de salvar.      |
| Valor unitário não aceito         | Valor inserido é negativo ou não numérico | Insira um valor positivo e numérico.            | Use apenas números positivos.              |
| Composição não aparece na lista    | Não foi salvo corretamente       | Verifique se o cadastro foi finalizado com sucesso. | Sempre clique em **Salvar** após adicionar insumos. |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre utilize nomes descritivos para composições para facilitar a identificação.
- Utilize a opção de composição global apenas quando não houver necessidade de detalhamento.
- Revise os insumos cadastrados antes de finalizar o cadastro.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Cadastro de Composição Detalhada**
```
Situação: Cadastro de uma composição para instalação de ar-condicionado.
Ação: 
  • Nome: "Instalação Ar-Condicionado"
  • Tipo de Insumo: "Mão de Obra"
  • Valor Unitário: 200.00
  • Quantidade Unitária: 1
Resultado: Composição detalhada é criada com mão de obra especificada.
```

**Exemplo 2: Cadastro de Composição Global**
```
Situação: Cadastro de uma composição para serviços de pintura.
Ação: 
  • Nome: "Serviço de Pintura"
  • Tipo de Insumo: "Material"
  • Valor Unitário: 500.00
  • Quantidade Unitária: 1
Resultado: Composição global é criada com valor unitário definido.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O usuário deve ter permissão para cadastrar composições.
- **Habilita:** A composição criada pode ser utilizada em orçamentos futuros.
- **Relacionado a:** Funcionalidades de orçamentos e relatórios de custos.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como cadastrar uma composição de insumos?"
- **Com problema:** "Não consigo adicionar insumos, o que fazer?"
- **Informal:** "Como eu faço pra colocar insumos no sistema?"
- **Por sintoma:** "O que fazer se não aparece a composição na lista?"
- **Com dúvida:** "Preciso detalhar todos os insumos ou posso fazer uma composição global?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Cadastrar composição", "Adicionar insumos", "Criar composição", "Composição de serviços"
- "Composição detalhada", "Composição simplificada", "Cadastro de insumos"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como faço para cadastrar uma nova composição de insumos?
- Quais campos são obrigatórios no cadastro de composição?
- O que é uma composição global e como posso criá-la?
- O que fazer se não consigo salvar a composição?
- Quais são os pré-requisitos para cadastrar uma composição de insumos?

---


---


---

## 7. Cadastro de Composição e Cálculo de Orçamento

**📋 METADADOS:**
- **ID:** sec_7
- **⏱️ Minutagem:** 15:23 → 17:55
- **⏲️ Duração:** 152s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/BdLq4eBgfxQ?si=Sxmnm__Ai1ReGR0_&t=923)
- **📦 Módulo:** Orçamento
- **🏷️ Categorias:** Cadastro, Orçamento, Composição, Serviços
- **🔑 Palavras-chave:** composição, orçamento, serviço, insumos, valor total

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como cadastrar uma composição associada a um serviço e calcular o valor total do orçamento com base na quantidade e no valor unitário dos insumos. O objetivo é facilitar a gestão de custos em projetos de construção.

**Contexto:**
Estamos no módulo de Orçamento do sistema, onde o usuário pode cadastrar composições de serviços e calcular os custos associados. Esta funcionalidade é essencial para a gestão financeira de projetos de construção.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Orçamento > Submenu Cadastro de Composição
- Tela/interface específica: Tela de Cadastro de Composição e Orçamento

**Funcionalidade Detalhada:**
A funcionalidade permite ao usuário cadastrar uma composição para um serviço específico, associando insumos e suas respectivas quantidades. O sistema calcula automaticamente o valor total do orçamento com base na quantidade informada e no valor unitário dos insumos cadastrados.

### 🔹 Passo a Passo Detalhado:

1. **Cadastrar Composição Associada ao Serviço**
   - Localização: Tela de Cadastro de Composição
   - Como fazer: 
     - Acesse a tela de Cadastro de Composição.
     - Selecione o serviço desejado no campo de seleção.
     - Clique em **Adicionar** para incluir a composição.
   - Campos/Opções disponíveis:
     * `Serviço`: Seleção do serviço (ex: Alvenaria e Assentamento)
     * `Composição`: Campo para associar a composição ao serviço
   - Resultado esperado: A composição é associada ao serviço selecionado.

2. **Inserir Quantidade no Orçamento**
   - Localização: Tela de Orçamento
   - Como fazer: 
     - No orçamento, localize o campo de **Quantidade**.
     - Insira a quantidade que será executada do serviço.
   - Observações importantes: O sistema multiplica automaticamente a quantidade pelo valor unitário da composição.
   - Resultado esperado: O valor total do serviço é calculado e exibido.

3. **Editar Quantidade**
   - Localização: Tela de Orçamento
   - Como fazer: 
     - Clique nos **três pontinhos** ao lado da quantidade.
     - Selecione a opção **Editar**.
     - Ajuste a quantidade conforme necessário e confirme.
   - Resultado esperado: A quantidade é atualizada e o valor total recalculado.

4. **Cadastrar Nova Etapa e Insumos**
   - Localização: Tela de Cadastro de Composição
   - Como fazer: 
     - Clique em **Cadastrar Nova Etapa**.
     - Selecione o serviço desejado (ex: Alvenaria e Assentamento).
     - Clique em **Criar Composição do Zero**.
   - Campos/Opções disponíveis:
     * `Insumos`: Adicione insumos necessários (ex: Pedreiro, Cimento, Argamassa)
     * `Valor Unitário`: O sistema puxa automaticamente os valores cadastrados.
   - Resultado esperado: Os insumos são cadastrados e associados à nova composição.

5. **Definir Quantidades dos Insumos**
   - Localização: Tela de Cadastro de Composição
   - Como fazer: 
     - Para cada insumo, insira a quantidade necessária.
     - Exemplo: Para o pedreiro, insira "0,5" horas para 1 m² de alvenaria.
     - Para o cimento, insira "6" kg para 1 m² de alvenaria.
   - Resultado esperado: As quantidades são salvas e utilizadas para o cálculo do orçamento.

**Campos e Parâmetros:**

| Campo                | Tipo        | Obrigatório | Descrição                                     | Exemplo          |
|----------------------|-------------|-------------|-----------------------------------------------|------------------|
| `Serviço`            | Dropdown    | Sim         | Seleção do serviço a ser orçado              | Alvenaria        |
| `Quantidade`         | Numérico    | Sim         | Quantidade do serviço a ser executado        | 10               |
| `Insumos`            | Multi-select| Sim         | Insumos necessários para o serviço            | Pedreiro, Cimento |
| `Valor Unitário`     | Numérico    | Sim         | Valor por unidade do insumo                   | 50,00            |
| `Horas do Pedreiro`  | Numérico    | Sim         | Tempo necessário do pedreiro por m²          | 0,5              |
| `Quilos de Cimento`  | Numérico    | Sim         | Quantidade de cimento necessária por m²      | 6                |

**Regras de Negócio:**
- O sistema deve calcular automaticamente o valor total multiplicando a quantidade pelo valor unitário.
- As quantidades de insumos devem ser informadas em unidades que façam sentido para o serviço (ex: horas, quilos).
- O valor unitário pode ser alterado pelo usuário, caso haja atualização nos preços.

**Observações Importantes:**
- Sempre verifique se a composição está corretamente associada ao serviço antes de finalizar o orçamento.
- Evite inserir valores negativos nas quantidades, pois isso pode gerar erros no cálculo.

**Conceitos-Chave:**
- **Composição**: Conjunto de insumos e suas quantidades necessárias para a execução de um serviço.
- **Orçamento**: Estimativa de custos associada à execução de serviços.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                         | Causa Provável                     | Solução                                       | Prevenção                                   |
|----------------------------------|------------------------------------|-----------------------------------------------|---------------------------------------------|
| Valor total não aparece          | Quantidade não informada           | Verifique se a quantidade foi preenchida     | Sempre preencher todos os campos obrigatórios|
| Insumo não encontrado             | Insumo não cadastrado              | Cadastre o insumo na base antes de usar     | Manter a base de insumos atualizada        |
| Erro ao editar quantidade        | Campo de edição não habilitado     | Verifique se a quantidade foi previamente salva| Salvar alterações antes de editar          |

**💡 DICAS E BOAS PRÁTICAS:**
- Utilize sempre insumos atualizados para evitar discrepâncias nos cálculos.
- Revise as composições cadastradas periodicamente para garantir precisão nos orçamentos.
- Use a funcionalidade de edição com cautela para evitar alterações indesejadas.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Cálculo de Orçamento para Alvenaria**
```
Situação: Um projeto de construção requer 10 m² de alvenaria.
Ação: 
  • Campo `Quantidade`: "10"
  • Campo `Insumos`: "Pedreiro, Cimento, Argamassa"
Resultado: O sistema calcula o valor total com base nas quantidades e valores unitários dos insumos.
```

**Exemplo 2: Atualização de Insumos**
```
Situação: O preço do cimento foi alterado para R$ 60,00.
Ação: 
  • Campo `Valor Unitário` do cimento: "60,00"
Resultado: O valor total do orçamento é recalculado automaticamente.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O serviço deve estar previamente cadastrado no sistema.
- **Habilita:** O cálculo de orçamento para outros serviços que utilizem a mesma composição.
- **Relacionado a:** Módulo de Cadastro de Insumos e Módulo de Relatórios de Orçamento.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como cadastrar uma composição?"
- **Com problema:** "Não consigo calcular o valor total do orçamento, o que fazer?"
- **Informal:** "Como eu faço pra colocar os insumos no orçamento?"
- **Por sintoma:** "Quando não aparece o valor total, o que está errado?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Cadastrar composição", "Adicionar insumos", "Criar orçamento", "Associar serviço"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como cadastrar uma nova composição para um serviço?
- O que fazer se o valor total não aparece no orçamento?
- Como editar a quantidade de um insumo no orçamento?
- O que fazer se não consigo encontrar um insumo?
- O que preciso ter cadastrado antes de criar um orçamento?

---


---


---

## 8. Gestão de Unidades de Medida e Execução de Serviços

**📋 METADADOS:**
- **ID:** sec_8
- **⏱️ Minutagem:** 17:54 → 20:29
- **⏲️ Duração:** 154s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/BdLq4eBgfxQ?si=Sxmnm__Ai1ReGR0_&t=1074)
- **📦 Módulo:** Orçamento
- **🏷️ Categorias:** Medidas, Orçamento, Execução de Serviços, Vendas
- **🔑 Palavras-chave:** unidade de medida, argamassa, orçamento, composição, proposta, venda direta, condições de pagamento

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como gerenciar unidades de medida no orçamento, incluindo a execução de serviços e a formalização de propostas de venda. O objetivo é garantir que os usuários compreendam como calcular e registrar as quantidades necessárias para a execução de serviços, além de editar valores unitários e formalizar vendas.

**Contexto:**
Estamos no módulo de Orçamento, onde o usuário pode gerenciar as unidades de medida dos produtos e serviços. A seção foca na relação entre a unidade de medida do produto e a unidade de medida da execução do serviço, além de como isso se reflete na composição do orçamento.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Orçamento > Submenu Gestão de Unidades de Medida
- Tela/interface específica: Tela de Orçamento

**Funcionalidade Detalhada:**

Esta funcionalidade permite ao usuário calcular a quantidade de insumos necessários para a execução de serviços, como a quantidade de metros cúbicos de argamassa necessária para 1 m² de alvenaria. O sistema também possibilita a edição de valores unitários de insumos, especialmente para aqueles que utilizam composições da SINAP. Além disso, o usuário pode formalizar propostas de venda ou realizar vendas diretas.

### 🔹 Passo a Passo Detalhado:

1. **Calcular Quantidade de Insumos**
   - Localização: Tela de Orçamento, seção de Cálculo de Insumos
   - Como fazer: Insira a unidade de medida do produto (ex: m³ para argamassa) e a unidade de medida da execução do serviço (ex: m² para alvenaria). O sistema calculará automaticamente a quantidade necessária.
   - Campos/Opções disponíveis:
     * `Unidade de Medida do Produto`: (ex: m³)
     * `Unidade de Medida da Execução`: (ex: m²)
   - Resultado esperado: O sistema exibe a quantidade de insumos necessária para a execução do serviço.

2. **Editar Valores Unitários de Insumos**
   - Localização: Tela de Orçamento, seção de Insumos
   - Como fazer: Selecione o insumo desejado da lista de composições. Clique no botão **Editar** ao lado do valor unitário.
   - Observações importantes: Alterações feitas aqui afetam apenas o orçamento atual, não impactando os valores padrão do sistema.
   - Resultado esperado: O valor unitário do insumo é atualizado no orçamento.

3. **Formalizar Proposta de Venda**
   - Localização: Tela de Orçamento, seção de Propostas
   - Como fazer: Clique no botão **Criar Proposta**. Selecione o cliente (ex: Karina) e insira a data da venda.
   - Campos/Opções disponíveis:
     * `Cliente`: (ex: Karina)
     * `Data da Venda`: (data atual ou outra)
   - Resultado esperado: Uma proposta de venda é gerada com as informações inseridas.

4. **Inserir Condições de Pagamento**
   - Localização: Tela de Propostas, seção de Condições de Pagamento
   - Como fazer: Insira o valor à vista (ex: 60.000) e clique em **Adicionar Condição Especial** para inserir parcelas.
   - Campos/Opções disponíveis:
     * `Valor à Vista`: (ex: 60.000)
     * `Quantidade de Parcelas`: (número de parcelas)
     * `Valor Total da Condição`: (valor total a ser pago)
     * `Data de Vencimento`: (data de cada parcela)
     * `Percentual de Juros`: (se aplicável)
   - Resultado esperado: As condições de pagamento são registradas e exibidas na proposta.

5. **Selecionar Recebimento por Medição**
   - Localização: Tela de Propostas, seção de Recebimento
   - Como fazer: Marque a opção **Recebimento por Medição** e insira o valor total.
   - Campos/Opções disponíveis:
     * `Valor Total`: (valor total a ser recebido)
   - Resultado esperado: O sistema registra que o recebimento será feito por medição.

**Campos e Parâmetros:**

| Campo                          | Tipo     | Obrigatório | Descrição                                               | Exemplo          |
|--------------------------------|----------|-------------|---------------------------------------------------------|------------------|
| Unidade de Medida do Produto   | Texto    | Sim         | Unidade de medida utilizada para o produto.            | m³               |
| Unidade de Medida da Execução  | Texto    | Sim         | Unidade de medida utilizada para a execução do serviço. | m²               |
| Cliente                        | Seleção  | Sim         | Nome do cliente para quem a proposta é feita.          | Karina           |
| Data da Venda                  | Data     | Sim         | Data em que a venda será formalizada.                  | 01/01/2024       |
| Valor à Vista                  | Numérico | Sim         | Valor total a ser pago à vista.                         | 60.000           |
| Quantidade de Parcelas         | Numérico | Não         | Número de parcelas acordadas.                            | 5                |
| Valor Total da Condição        | Numérico | Não         | Valor total a ser pago nas parcelas.                    | 120.000          |
| Data de Vencimento             | Data     | Não         | Data de vencimento de cada parcela.                     | 01/02/2024       |
| Percentual de Juros            | Numérico | Não         | Percentual de juros aplicado, se houver.                | 5%                |
| Valor Total                    | Numérico | Sim         | Valor total a ser recebido por medição.                 | 100.000          |

**Regras de Negócio:**
- A edição dos valores unitários de insumos afeta apenas o orçamento atual.
- As condições de pagamento devem ser inseridas de acordo com o que foi acordado com o cliente.
- O recebimento por medição deve ser selecionado se o pagamento for baseado em medições realizadas.

**Observações Importantes:**
- Sempre verifique se as unidades de medida estão corretas antes de calcular as quantidades.
- Evite alterar valores unitários sem a devida autorização, pois isso pode impactar o orçamento.
- Caso o cliente não tenha condições de pagamento definidas, a proposta não poderá ser formalizada.

**Conceitos-Chave:**
- **Unidade de Medida**: Refere-se à medida padrão utilizada para quantificar produtos e serviços, como metros cúbicos (m³) ou metros quadrados (m²).
- **Composição**: Conjunto de insumos e suas quantidades necessárias para a execução de um serviço.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                       | Solução                                           | Prevenção                                     |
|-----------------------------------|--------------------------------------|--------------------------------------------------|-----------------------------------------------|
| Cálculo incorreto de insumos      | Unidades de medida não correspondem  | Verifique se as unidades de medida estão corretas| Sempre confirme as unidades antes de calcular |
| Não consegue editar valores unitários | Permissões insuficientes            | Verifique as permissões do usuário               | Configure permissões adequadas para usuários   |
| Proposta não é gerada             | Campos obrigatórios não preenchidos | Preencha todos os campos obrigatórios            | Revise os campos antes de tentar gerar a proposta |

**💡 DICAS E BOAS PRÁTICAS:**
- Utilize sempre as unidades de medida corretas para evitar erros de cálculo.
- Mantenha um registro das condições de pagamento acordadas para facilitar a formalização.
- Revise as propostas antes de enviá-las ao cliente para garantir que todas as informações estão corretas.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Cálculo de Insumos para Alvenaria**
```
Situação: Um cliente solicita a execução de 100 m² de alvenaria.
Ação: O usuário insere 1 m² como unidade de medida da execução e 0.5 m³ como unidade de medida do produto (argamassa).
  • Unidade de Medida do Produto: "0.5 m³"
  • Unidade de Medida da Execução: "1 m²"
Resultado: O sistema calcula que são necessários 50 m³ de argamassa para a execução de 100 m² de alvenaria.
```

**Exemplo 2: Formalização de Proposta de Venda**
```
Situação: O usuário deseja formalizar uma proposta de venda para o cliente Karina.
Ação: O usuário seleciona Karina como cliente, insere a data de venda como 01/01/2024 e o valor à vista como 60.000.
Resultado: A proposta é gerada e pode ser enviada para o cliente.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O usuário deve ter acesso ao módulo de Orçamento e permissões para editar insumos.
- **Habilita:** A formalização de propostas de venda e a geração de relatórios financeiros.
- **Relacionado a:** Módulo de Vendas, onde as propostas podem ser convertidas em vendas diretas.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como calcular a quantidade de argamassa para alvenaria?"
- **Com problema:** "Não consigo editar os valores dos insumos, o que fazer?"
- **Informal:** "Como faço para vender direto para o cliente?"
- **Por sintoma:** "Quando o cliente não paga à vista, como registro isso?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "calcular insumos", "editar insumos", "formalizar proposta", "venda direta", "condições de pagamento"
- "orçamento", "proposta de venda", "execução de serviço"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como calcular a quantidade de insumos necessária para um serviço?
- Como editar os valores unitários dos insumos no orçamento?
- Como formalizar uma proposta de venda para um cliente?
- O que fazer se não consigo gerar uma proposta?
- O que preciso fazer antes de formalizar uma venda direta?

---


---


---

## 9. Geração de Planejamento de Obra

**📋 METADADOS:**
- **ID:** sec_9
- **⏱️ Minutagem:** 20:26 → 23:01
- **⏲️ Duração:** 155s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/BdLq4eBgfxQ?si=Sxmnm__Ai1ReGR0_&t=1226)
- **📦 Módulo:** Orçamento e Planejamento
- **🏷️ Categorias:** Planejamento, Orçamento, Gestão de Obras
- **🔑 Palavras-chave:** planejamento, orçamento, obra, geração, associar

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de geração do planejamento de uma obra a partir de um orçamento previamente realizado, incluindo a associação de obras e clientes, e as opções de edição disponíveis.

**Contexto:**
Estamos na fase de planejamento de uma obra, onde o usuário já completou o orçamento e agora precisa gerar o planejamento correspondente, associando-o a uma obra e a um cliente.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Orçamento e Planejamento > Submenu Planejamento
- Tela/interface específica: Tela de Geração de Planejamento

**Funcionalidade Detalhada:**
A funcionalidade de geração de planejamento de obra permite ao usuário criar um planejamento baseado em um orçamento previamente realizado. O planejamento deve ser associado a uma obra específica e a um cliente. O sistema garante que as informações orçadas e planejadas sejam consistentes, refletindo os mesmos valores inicialmente definidos.

### 🔹 Passo a Passo Detalhado:

1. **Inserir Data de Vencimento**
   - Localização: Campo de data na tela de planejamento
   - Como fazer: Clique no campo de data e selecione uma data futura, preferencialmente próxima ao final da obra.
   - Campos/Opções disponíveis:
     * `Data de Vencimento`: Campo de data (formato: DD/MM/AAAA)
   - Resultado esperado: A data de vencimento é salva e não contabilizada no financeiro até o seu vencimento.

2. **Salvar o Planejamento**
   - Localização: Botão **Salvar** na parte inferior da tela
   - Como fazer: Após inserir todos os dados necessários, clique no botão **Salvar**.
   - Resultado esperado: O planejamento é salvo no sistema, e uma confirmação de sucesso é exibida.

3. **Associar Obra ao Planejamento**
   - Localização: Campo de associação de obra na tela de planejamento
   - Como fazer: Selecione a obra correspondente no dropdown de obras disponíveis.
   - Observações importantes: É obrigatório associar uma obra ao planejamento; caso contrário, o sistema não permitirá a conclusão do processo.
   - Resultado esperado: A obra é associada ao planejamento, permitindo a continuidade do processo.

4. **Associar Cliente ao Planejamento**
   - Localização: Campo de associação de cliente na tela de planejamento
   - Como fazer: Selecione o cliente correspondente no dropdown de clientes disponíveis.
   - Resultado esperado: O cliente é associado ao planejamento, garantindo que todas as informações estejam vinculadas corretamente.

5. **Visualizar Informações do Planejamento**
   - Localização: Área de visualização na tela de planejamento
   - Como fazer: Após a geração do planejamento, as informações do orçamento e do planejamento serão exibidas na parte superior da tela.
   - Resultado esperado: Os valores orçados e planejados são iguais, refletindo a consistência dos dados.

**Campos e Parâmetros:**

| Campo                   | Tipo          | Obrigatório | Descrição                                         | Exemplo          |
|-------------------------|---------------|-------------|---------------------------------------------------|------------------|
| `Data de Vencimento`    | Data          | Sim         | Data em que o planejamento deve ser considerado.  | 30/12/2024       |
| `Obra`                  | Dropdown      | Sim         | Seleção da obra à qual o planejamento será associado. | Obra A           |
| `Cliente`               | Dropdown      | Sim         | Seleção do cliente associado ao planejamento.      | João Silva       |

**Regras de Negócio:**
- A data de vencimento deve ser sempre futura para evitar contabilizações indevidas.
- É obrigatório associar uma obra e um cliente ao planejamento antes de salvá-lo.
- Os valores orçados e planejados devem ser iguais no momento da geração do planejamento.

**Observações Importantes:**
- Ao editar o orçamento, o usuário pode alterar o nome, adicionar observações e modificar o percentual do BDI.
- Para replicar orçamentos, o usuário deve utilizar a funcionalidade de replicação disponível no sistema.
- O botão de exclusão permite remover orçamentos que não são mais necessários.

**Conceitos-Chave:**
- **BDI (Bonificação e Despesas Indiretas)**: Percentual aplicado sobre o custo direto de um serviço para cobrir despesas indiretas e lucro.
- **Planejamento**: Conjunto de ações e definições que visam organizar a execução de uma obra.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                   | Solução                                   | Prevenção                               |
|-----------------------------------|----------------------------------|-------------------------------------------|-----------------------------------------|
| Não consigo salvar o planejamento  | Obra ou cliente não associado    | Verifique se a obra e o cliente estão selecionados. | Sempre associe antes de salvar.        |
| Data de vencimento inválida       | Data passada selecionada         | Selecione uma data futura.               | Confirme a data antes de salvar.       |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre verifique se a data de vencimento está correta antes de salvar.
- Utilize a funcionalidade de replicação de orçamentos para economizar tempo em projetos semelhantes.
- Mantenha um registro dos orçamentos excluídos para referência futura.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Planejamento de Obra Residencial**
```
Situação: Planejamento de uma nova obra residencial.
Ação: 
  • Campo `Data de Vencimento`: "30/12/2024"
  • Campo `Obra`: "Construção Casa Silva"
  • Campo `Cliente`: "João Silva"
Resultado: O planejamento é salvo e associado corretamente à obra e ao cliente.
```

**Exemplo 2: Planejamento de Reforma Comercial**
```
Situação: Planejamento de uma reforma em um espaço comercial.
Ação: 
  • Campo `Data de Vencimento`: "15/11/2024"
  • Campo `Obra`: "Reforma Loja A"
  • Campo `Cliente`: "Maria Oliveira"
Resultado: O planejamento é salvo com sucesso, refletindo as informações do orçamento.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O orçamento deve ser gerado e salvo antes de iniciar o planejamento.
- **Habilita:** A geração de relatórios de planejamento e acompanhamento da obra.
- **Relacionado a:** Funcionalidades de edição de orçamento e relatórios financeiros.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como gerar o planejamento de uma obra?"
- **Com problema:** "Não consigo associar uma obra ao planejamento, o que fazer?"
- **Informal:** "Como faço o planejamento da obra?"
- **Por sintoma:** "O que fazer se o planejamento não está salvando?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Criar planejamento", "Adicionar planejamento", "Novo planejamento", "Cadastrar planejamento"
- "Associação de obra", "Vincular cliente"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como faço para gerar um planejamento de obra?
- O que devo fazer se não conseguir associar uma obra ao planejamento?
- Quais informações são necessárias para salvar um planejamento?
- O que fazer se a data de vencimento não for aceita?
- O que preciso ter feito antes de gerar um planejamento?

---


---


---

## 10. Alterações no Planejamento de Obras

**📋 METADADOS:**
- **ID:** sec_10
- **⏱️ Minutagem:** 22:58 → 25:32
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/BdLq4eBgfxQ?si=Sxmnm__Ai1ReGR0_&t=1378)
- **📦 Módulo:** Planejamento de Obras
- **🏷️ Categorias:** Planejamento, Orçamento, Controle, Execução
- **🔑 Palavras-chave:** alteração, serviço, orçamento, planejamento, medições, controle, execução

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como realizar alterações no planejamento de obras, incluindo adição de serviços e edição de valores, enfatizando a importância de realizar essas alterações na etapa correta para garantir a integridade dos dados entre orçado, planejado e executado.

**Contexto:**
Estamos na etapa de planejamento de uma obra, onde é possível realizar alterações diretamente no planejamento, sem a necessidade de voltar ao orçamento. O objetivo é garantir que as informações estejam sempre atualizadas e que os dados reflitam corretamente o que foi orçado, planejado e executado.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Planejamento de Obras > Submenu Planejamento
- Tela/interface específica: Tela de Planejamento de Obras

**Funcionalidade Detalhada:**
A funcionalidade permite que o usuário faça alterações no planejamento da obra, como adicionar novos serviços ou editar valores. Essas alterações devem ser feitas na etapa de planejamento, pois não se replicam automaticamente do orçamento. Isso é crucial para manter um comparativo entre o que foi orçado, o que foi planejado e o que foi realmente executado.

### 🔹 Passo a Passo Detalhado:

1. **Adicionar um Novo Serviço**
   - Localização: Tela de Planejamento de Obras, seção de serviços.
   - Como fazer: Clique no botão **Adicionar Serviço** localizado na parte superior da tela.
   - Campos/Opções disponíveis:
     * `Nome do Serviço`: Campo de texto para inserir o nome do serviço a ser adicionado.
     * `Valor Previsto`: Campo numérico para inserir o valor previsto para o serviço.
   - Resultado esperado: O novo serviço é adicionado à lista de serviços no planejamento.

2. **Editar um Valor de Serviço Existente**
   - Localização: Lista de serviços na tela de planejamento.
   - Como fazer: Clique no ícone de **Editar** ao lado do serviço desejado.
   - Campos/Opções disponíveis:
     * `Valor Previsto`: Campo numérico que pode ser alterado.
   - Observações importantes: As alterações feitas aqui não afetarão o orçamento anterior.
   - Resultado esperado: O valor do serviço é atualizado na lista de serviços.

3. **Preencher a Subaba de Orçamento**
   - Localização: Subaba de Orçamento dentro da tela de planejamento.
   - Como fazer: Clique na subaba **Orçamento** e preencha os campos conforme necessário.
   - Campos/Opções disponíveis:
     * `Valor a Receber`: Campo numérico para inserir o valor que se espera receber.
     * `Valor a Pagar`: Campo numérico para inserir o valor que se espera pagar.
   - Resultado esperado: Os valores são salvos e utilizados nas medições futuras.

4. **Preencher a Subaba de Controle**
   - Localização: Subaba de Controle dentro da tela de planejamento.
   - Como fazer: Clique na subaba **Controle** e selecione a forma de medição.
   - Campos/Opções disponíveis:
     * `Forma de Medição`: Dropdown com opções como "andar", "bloco", "unidade".
   - Observações importantes: A escolha da forma de medição deve refletir a estrutura da obra.
   - Resultado esperado: A forma de medição é salva e utilizada para o acompanhamento da execução.

**Campos e Parâmetros:**

| Campo               | Tipo    | Obrigatório | Descrição                                               | Exemplo         |
|---------------------|---------|-------------|---------------------------------------------------------|------------------|
| Nome do Serviço     | Texto   | Sim         | Nome do serviço a ser adicionado ao planejamento.      | "Pintura"        |
| Valor Previsto      | Numérico| Sim         | Valor estimado para o serviço.                          | 50.000           |
| Valor a Receber     | Numérico| Não         | Valor que se espera receber referente ao serviço.      | 50.000           |
| Valor a Pagar       | Numérico| Não         | Valor que se espera pagar referente ao serviço.        | 1.300            |
| Forma de Medição    | Dropdown| Sim         | Método de medição utilizado para o serviço.            | "Bloco"          |

**Regras de Negócio:**
- Alterações no planejamento devem ser feitas na etapa de planejamento e não no orçamento.
- O preenchimento da subaba de orçamento é opcional, apenas para quem trabalha com medições a pagar ou a receber.
- A forma de medição deve ser escolhida de acordo com a estrutura da obra (andar, bloco, unidade).

**Observações Importantes:**
- Sempre faça alterações na etapa de planejamento para garantir que os dados estejam corretos.
- Evite voltar ao orçamento para realizar alterações, pois isso não refletirá no planejamento.
- Verifique se a forma de medição escolhida é adequada para a estrutura da obra.

**Conceitos-Chave:**
- **Medição**: Processo de quantificação dos serviços executados em uma obra.
- **Orçamento**: Estimativa de custos e despesas para a realização de um projeto.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                        | Causa Provável                     | Solução                                         | Prevenção                                      |
|---------------------------------|------------------------------------|------------------------------------------------|------------------------------------------------|
| Alterações não aparecem no planejamento | Alterações feitas no orçamento | Realizar alterações diretamente na etapa de planejamento | Sempre editar na etapa correta                  |
| Campos obrigatórios não preenchidos | Campos não foram preenchidos corretamente | Preencher todos os campos obrigatórios antes de salvar | Revisar os campos obrigatórios antes de salvar  |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre revise os valores antes de salvar as alterações.
- Utilize a função de comparação entre orçado, planejado e executado para melhor controle.
- Mantenha uma documentação atualizada das alterações realizadas.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Adicionando um Novo Serviço**
```
Situação: Um novo serviço de "Pintura" precisa ser adicionado ao planejamento.
Ação: 
  • Campo Nome do Serviço: "Pintura"
  • Campo Valor Previsto: 50.000
Resultado: O serviço "Pintura" é adicionado ao planejamento com o valor previsto de 50.000.
```

**Exemplo 2: Editando um Valor de Serviço Existente**
```
Situação: O valor do serviço "Pintura" precisa ser atualizado.
Ação: 
  • Campo Valor Previsto: Alterar de 50.000 para 55.000
Resultado: O valor do serviço "Pintura" é atualizado para 55.000 no planejamento.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O orçamento deve estar previamente definido para que o planejamento seja realizado.
- **Habilita:** A funcionalidade de medições futuras e relatórios de execução.
- **Relacionado a:** Módulo de Orçamento e Módulo de Execução.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como adicionar um novo serviço no planejamento?"
- **Com problema:** "Não consigo editar o valor de um serviço, o que fazer?"
- **Informal:** "Como eu coloco um serviço novo no planejamento?"
- **Por sintoma:** "Quando tento alterar um serviço, nada muda, por que isso acontece?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Adicionar serviço", "incluir serviço", "editar serviço", "modificar planejamento"
- "Medição", "execução", "orçamento", "controle de obra"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como faço para adicionar um novo serviço no planejamento?
- O que acontece se eu editar um valor no orçamento?
- Como preencher a subaba de orçamento?
- O que fazer se as alterações não aparecem no planejamento?
- O que preciso ter feito antes de começar o planejamento?

---


---


---

## 11. Execução e Acompanhamento de Serviços

**📋 METADADOS:**
- **ID:** sec_11
- **⏱️ Minutagem:** 25:37 → 28:09
- **⏲️ Duração:** 152s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/BdLq4eBgfxQ?si=Sxmnm__Ai1ReGR0_&t=1537)
- **📦 Módulo:** Planejamento de Obras
- **🏷️ Categorias:** Execução, Acompanhamento, Planejamento, Gestão de Projetos
- **🔑 Palavras-chave:** execução, serviços, cronograma, planejamento, acompanhamento, predecessores, alvenaria

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como executar e acompanhar serviços em um sistema de planejamento de obras, abordando a definição de mão de obra, unidades de medida, cronograma e a relação entre serviços.

**Contexto:**
Estamos na fase de planejamento de um projeto de construção, onde é essencial definir como os serviços serão executados e como será feito o acompanhamento da obra. Esta seção orienta o usuário sobre como registrar essas informações no sistema.

**Localização no Sistema:**
- Caminho de navegação: Menu Principal > Planejamento de Obras > Execução de Serviços
- Tela/interface específica: Tela de Execução e Acompanhamento de Serviços

**Funcionalidade Detalhada:**
A funcionalidade permite ao usuário definir como os serviços serão executados, seja por mão de obra própria, terceirizada ou mista. Além disso, possibilita a definição da unidade de medida (por exemplo, m² ou m³) e a criação de um cronograma com datas de início e término para cada serviço. O sistema também permite a inclusão de predecessores, que são serviços que devem ser concluídos antes que outros possam ser iniciados.

### 🔹 Passo a Passo Detalhado:

1. **Definir Forma de Execução**
   - Localização: Tela de Execução de Serviços
   - Como fazer: Selecione a forma de execução desejada para o serviço. As opções disponíveis são:
     * **Mão de obra própria**
     * **Mão de obra terceirizada**
     * **Mista**
   - Resultado esperado: A forma de execução é registrada e refletida no planejamento.

2. **Selecionar Unidade de Medida**
   - Localização: Tela de Execução de Serviços
   - Como fazer: Escolha a unidade de medida que será utilizada para o serviço. As opções incluem:
     * **m²** (metros quadrados)
     * **m³** (metros cúbicos)
   - Resultado esperado: A unidade de medida é definida e utilizada para cálculos futuros.

3. **Definir Cronograma**
   - Localização: Tela de Execução de Serviços
   - Como fazer: Insira a data prevista para iniciar e finalizar cada serviço nos campos correspondentes.
   - Campos/Opções disponíveis:
     * `Data de Início`: [data prevista para o início do serviço]
     * `Data de Término`: [data prevista para a conclusão do serviço]
   - Resultado esperado: O cronograma é salvo e pode ser utilizado para comparativos entre o planejado e o executado.

4. **Adicionar Predecessores**
   - Localização: Tela de Execução de Serviços
   - Como fazer: Se desejar, adicione predecessores que vinculem a execução de um serviço a outro. Por exemplo, se o serviço de alvenaria não pode ser iniciado antes da limpeza geral do canteiro, registre essa relação.
   - Observações importantes: A inclusão de predecessores é opcional, e o sistema permite iniciar serviços mesmo que os predecessores não estejam concluídos.
   - Resultado esperado: A relação entre serviços é estabelecida, facilitando o planejamento.

5. **Salvar Planejamento**
   - Localização: Tela de Execução de Serviços
   - Como fazer: Após inserir todas as informações, clique no botão **Salvar**.
   - Resultado esperado: O planejamento é salvo com todas as definições feitas.

6. **Gerar Acompanhamento da Obra**
   - Localização: Tela de Execução de Serviços
   - Como fazer: Selecione a opção **Gerar Acompanhamento** e insira o nome do acompanhamento.
   - Resultado esperado: O acompanhamento é criado e pode ser utilizado para monitorar a execução dos serviços e os valores gastos.

**Campos e Parâmetros:**

| Campo                | Tipo         | Obrigatório | Descrição                                           | Exemplo               |
|----------------------|--------------|-------------|----------------------------------------------------|-----------------------|
| Forma de Execução    | Dropdown     | Sim         | Define como o serviço será executado               | Mão de obra própria    |
| Unidade de Medida    | Dropdown     | Sim         | Unidade utilizada para mensurar o serviço          | m²                    |
| Data de Início       | Data         | Sim         | Data prevista para o início do serviço             | 01/01/2024            |
| Data de Término      | Data         | Sim         | Data prevista para a conclusão do serviço          | 15/01/2024            |
| Predecessores        | Texto        | Não         | Serviços que devem ser concluídos antes de iniciar | Limpeza geral         |

**Regras de Negócio:**
- A forma de execução deve ser definida antes de salvar o planejamento.
- As datas de início e término devem ser válidas e coerentes.
- Predecessores são opcionais, mas se usados, devem referenciar serviços existentes.

**Observações Importantes:**
- Alterações nos insumos ou valores podem ser feitas diretamente na tela de planejamento.
- É importante revisar as datas do cronograma para evitar conflitos.

**Conceitos-Chave:**
- **Predecessores**: Serviços que precisam ser concluídos antes que outros possam ser iniciados.
- **Cronograma**: Planejamento temporal das atividades e serviços a serem realizados.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                 | Solução                                             | Prevenção                                       |
|-----------------------------------|--------------------------------|----------------------------------------------------|------------------------------------------------|
| Não consigo salvar o planejamento  | Campos obrigatórios não preenchidos | Verifique se todos os campos obrigatórios estão preenchidos | Sempre revisar os campos antes de salvar       |
| Data de término anterior à data de início | Datas inseridas incorretamente | Corrija as datas para que a data de término seja posterior à de início | Use um calendário para verificar as datas     |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre atualize os valores dos insumos antes de finalizar o planejamento.
- Utilize a funcionalidade de predecessores para evitar atrasos na execução dos serviços.
- Revise o cronograma periodicamente para garantir que os prazos estão sendo cumpridos.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Planejamento de Alvenaria**
```
Situação: Planejamento do serviço de alvenaria.
Ação: 
  • Forma de Execução: "Mão de obra própria"
  • Unidade de Medida: "m²"
  • Data de Início: "01/02/2024"
  • Data de Término: "15/02/2024"
Resultado: O serviço de alvenaria está planejado para ser executado com mão de obra própria, utilizando metros quadrados como unidade de medida.
```

**Exemplo 2: Planejamento de Limpeza Geral**
```
Situação: Planejamento do serviço de limpeza geral.
Ação: 
  • Forma de Execução: "Terceirizada"
  • Unidade de Medida: "m³"
  • Data de Início: "01/01/2024"
  • Data de Término: "05/01/2024"
Resultado: O serviço de limpeza geral está agendado para ser realizado por uma empresa terceirizada, com a unidade de medida em metros cúbicos.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** Os serviços devem ser cadastrados antes de serem vinculados como predecessores.
- **Habilita:** O acompanhamento da obra, que permite monitorar a execução e os gastos.
- **Relacionado a:** Funcionalidades de relatórios e análise de desempenho da obra.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como executar um serviço no planejamento?"
- **Com problema:** "Não consigo salvar o planejamento, o que fazer?"
- **Informal:** "Como faço para planejar a obra?"
- **Por sintoma:** "O que fazer se as datas não estão corretas?"
- **Com variação:** "Como adicionar predecessores no planejamento?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Executar serviço", "Planejar serviço", "Cronograma de serviços", "Acompanhamento de obra"
- "Serviço de alvenaria", "Limpeza do canteiro", "Planejamento de obra"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como definir a forma de execução de um serviço?
- Quais unidades de medida posso usar para os serviços?
- Como adicionar predecessores no planejamento?
- O que fazer se as datas de início e término não estão corretas?
- O que preciso fazer antes de gerar o acompanhamento da obra?

---


---


---

## 12. Liberação de Serviços para Execução

**📋 METADADOS:**
- **ID:** sec_12
- **⏱️ Minutagem:** 28:08 → 30:43
- **⏲️ Duração:** 155s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/BdLq4eBgfxQ?si=Sxmnm__Ai1ReGR0_&t=1688)
- **📦 Módulo:** Planejamento de Serviços
- **🏷️ Categorias:** Execução, Planejamento, Administração, Operacional
- **🔑 Palavras-chave:** liberação de serviços, execução, status, apontamentos, colaboradores

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de liberação de serviços para execução dentro do sistema, explicando como registrar a autorização para iniciar os serviços e como associar colaboradores a esses serviços.

**Contexto:**
Estamos na interface do módulo de Planejamento de Serviços, onde o usuário pode gerenciar o status dos serviços planejados e liberá-los para execução. O objetivo é garantir que os serviços sejam devidamente autorizados antes de sua execução.

**Localização no Sistema:**
- Caminho de navegação: Menu Principal > Módulo Planejamento de Serviços > Acompanhamento de Serviços
- Tela/interface específica: Acompanhamento de Serviços

**Funcionalidade Detalhada:**
A funcionalidade de liberação de serviços permite que o usuário autorize a execução de serviços previamente planejados. O sistema apresenta os serviços com status "planejado" e possibilita a alteração desse status para "liberado" ao preencher informações necessárias e selecionar os serviços a serem autorizados.

### 🔹 Passo a Passo Detalhado:

1. **Acessar Mais Ordens de Produção**
   - Localização: Na tela de Acompanhamento de Serviços, clique no botão **Mais Ordens de Produção**.
   - Como fazer: Clique no botão para abrir a interface de criação de novas ordens de produção.
   - Campos/Opções disponíveis:
     * `Título`: Campo de texto para inserir o nome da ordem de produção.
     * `Previsão para Início`: Campo de data para selecionar a data de início da execução.
     * `Previsão para Término`: Campo de data para selecionar a data de término da execução.
   - Resultado esperado: Uma nova ordem de produção é criada, permitindo a seleção de serviços para liberação.

2. **Selecionar Serviços para Liberação**
   - Localização: Na interface de criação de ordens de produção, localize a seção de seleção de serviços.
   - Como fazer: Marque os serviços que deseja liberar para execução. Por exemplo, selecione "Limpeza Geral do Canteiro".
   - Observações importantes: A unidade de medida deve ser escolhida corretamente; para serviços como "Alvenaria", a liberação pode ser parcial (ex: apenas bloco A ou bloco B).
   - Resultado esperado: Os serviços selecionados são marcados para liberação.

3. **Associar Colaboradores (Opcional)**
   - Localização: Na mesma interface de criação de ordens de produção, há uma seção para associar colaboradores.
   - Como fazer: Se o módulo de RH estiver habilitado, selecione os colaboradores que irão executar os serviços. O sistema sugere colaboradores com base em seus cargos.
   - Observações importantes: Não é obrigatório associar colaboradores; se não houver colaboradores com o cargo adequado, o sistema indicará aqueles que não estão alocados.
   - Resultado esperado: Colaboradores são associados aos serviços, facilitando o gerenciamento de execução.

4. **Salvar e Liberar o Serviço**
   - Localização: Após preencher todas as informações, clique no botão **Salvar**.
   - Como fazer: Clique no botão para confirmar a liberação dos serviços.
   - Resultado esperado: O status do serviço muda para "liberado", e os serviços aparecem na lista de serviços prontos para execução.

**Campos e Parâmetros:**

| Campo                     | Tipo          | Obrigatório | Descrição                                               | Exemplo                  |
|---------------------------|---------------|-------------|--------------------------------------------------------|--------------------------|
| Título                    | Texto         | Sim         | Nome da ordem de produção.                             | "Ordem de Produção 1"    |
| Previsão para Início      | Data          | Sim         | Data prevista para início da execução.                | "2023-10-01"             |
| Previsão para Término     | Data          | Sim         | Data prevista para término da execução.               | "2023-10-15"             |
| Serviços                  | Seleção múltipla | Sim         | Lista de serviços a serem liberados.                  | "Limpeza Geral", "Alvenaria" |
| Colaboradores             | Seleção múltipla | Não         | Colaboradores que executarão os serviços.             | "João Silva", "Maria Oliveira" |

**Regras de Negócio:**
- Os serviços devem estar com status "planejado" para serem liberados.
- A liberação de serviços pode ser parcial, dependendo da unidade de medida.
- A associação de colaboradores é opcional, mas facilita a gestão de execução.

**Observações Importantes:**
- Certifique-se de que todos os campos obrigatórios estejam preenchidos antes de salvar.
- Evite liberar serviços sem a devida associação de colaboradores, se aplicável.
- Verifique se os colaboradores têm os cargos adequados para os serviços que irão executar.

**Conceitos-Chave:**
- **Status do Serviço**: Indica a fase atual do serviço (planejado, liberado, executado).
- **Apontamentos**: Registro das atividades realizadas em cada serviço.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                     | Solução                                           | Prevenção                                      |
|-----------------------------------|------------------------------------|--------------------------------------------------|------------------------------------------------|
| Botão "Salvar" desabilitado       | Campos obrigatórios não preenchidos | Preencha todos os campos obrigatórios.           | Verifique os campos antes de tentar salvar.   |
| Serviço não aparece na lista      | Não foi liberado corretamente      | Revise o processo de liberação e salve novamente. | Siga todos os passos corretamente.             |
| Colaboradores não aparecem        | Cargo do colaborador não compatível| Verifique se o colaborador possui o cargo correto.| Mantenha os cargos atualizados no sistema.     |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre revise os serviços selecionados antes de liberar.
- Utilize a função de busca para encontrar colaboradores rapidamente.
- Mantenha um registro claro das ordens de produção para facilitar o acompanhamento.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Liberação de Serviços para um Projeto**
```
Situação: Um projeto de construção que requer a liberação de serviços de alvenaria e limpeza.
Ação: 
  • Campo Título: "Liberação Projeto A"
  • Campo Previsão para Início: "2023-10-01"
  • Campo Previsão para Término: "2023-10-15"
  • Selecionar Serviços: "Limpeza Geral", "Alvenaria do Bloco A"
Resultado: Os serviços são liberados e aparecem com status "liberado".
```

**Exemplo 2: Liberação Parcial de Serviços**
```
Situação: Necessidade de liberar apenas parte dos serviços de alvenaria.
Ação: 
  • Campo Título: "Liberação Parcial Bloco B"
  • Campo Previsão para Início: "2023-10-05"
  • Campo Previsão para Término: "2023-10-10"
  • Selecionar Serviços: "Alvenaria do Bloco B"
Resultado: Apenas o serviço do Bloco B é liberado, com status "liberado".
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O serviço deve estar previamente planejado e com status "planejado".
- **Habilita:** A execução dos serviços liberados.
- **Relacionado a:** Módulo de RH para associação de colaboradores.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como liberar um serviço para execução?"
- **Com problema:** "O que fazer se não consigo liberar um serviço?"
- **Informal:** "Como eu faço pra liberar um serviço?"
- **Por sintoma:** "Por que meu serviço não aparece para execução?"
- **Com dúvida:** "Preciso associar colaboradores ao liberar um serviço?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "autorizar serviço", "liberação de tarefa", "iniciar serviço", "aprovar execução"
- "serviço liberado", "status de serviço", "execução de serviços"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como faço para liberar um serviço para execução?
- O que fazer se o botão de salvar estiver desabilitado?
- Como associar colaboradores a um serviço liberado?
- O que fazer se o serviço não aparecer na lista de execução?
- Quais campos são obrigatórios para liberar um serviço?

---


---


---

## 13. Início e Controle de Serviços de Alvenaria

**📋 METADADOS:**
- **ID:** sec_13
- **⏱️ Minutagem:** 30:39 → 33:11
- **⏲️ Duração:** 152s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/BdLq4eBgfxQ?si=Sxmnm__Ai1ReGR0_&t=1839)
- **📦 Módulo:** Alvenaria
- **🏷️ Categorias:** Operacional, Controle de Serviços, Relatório
- **🔑 Palavras-chave:** alvenaria, iniciar serviço, controle de serviços, percentual executado, status do serviço

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de início e controle de serviços de alvenaria, incluindo como registrar a data e o horário de início, gerenciar colaboradores e monitorar o progresso do serviço.

**Contexto:**
Estamos na interface do módulo de alvenaria, onde o usuário pode iniciar e gerenciar serviços relacionados a obras. O objetivo é registrar o início de um serviço, controlar seu progresso e finalizar quando necessário.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Alvenaria > Início de Serviços
- Tela/interface específica: Tela de Controle de Serviços de Alvenaria

**Funcionalidade Detalhada:**

A funcionalidade permite ao usuário iniciar um serviço de alvenaria, registrar a data e o horário de início, associar colaboradores e monitorar o progresso do serviço. É importante seguir as regras de data para evitar conflitos com liberações anteriores.

### 🔹 Passo a Passo Detalhado:

1. **Iniciar Serviço de Alvenaria**
   - Localização: Tela de Controle de Serviços de Alvenaria
   - Como fazer: Clique no botão **Iniciar Serviço**.
   - Campos/Opções disponíveis:
     * `Data de Início`: Campo para inserir a data em que o serviço está sendo iniciado.
     * `Horário de Início`: Campo para inserir o horário em que o serviço está sendo iniciado.
   - Resultado esperado: O serviço é iniciado e registrado com a data e horário especificados.

2. **Associar Colaborador**
   - Localização: Na mesma tela, após iniciar o serviço.
   - Como fazer: O colaborador previamente associado aparecerá automaticamente. Para alterar, clique no campo de seleção e escolha outro colaborador da lista.
   - Observações importantes: Se a data de início for anterior à data de liberação do serviço, a alteração não será permitida.
   - Resultado esperado: O colaborador associado é atualizado conforme a seleção.

3. **Parar Serviço**
   - Localização: Na tela de Controle de Serviços de Alvenaria, após iniciar o serviço.
   - Como fazer: Clique no botão **Parar Serviço**.
   - Campos/Opções disponíveis:
     * `Horário de Parada`: Campo para inserir o horário em que o serviço foi parado.
     * `Observação`: Campo para inserir notas sobre a parada do serviço.
     * `Quantidade Executada`: Campo para registrar a quantidade de trabalho realizado até o momento.
   - Resultado esperado: O serviço é marcado como parado, e as informações são registradas.

4. **Registrar Percentual Executado**
   - Localização: Na tela de Controle de Serviços de Alvenaria, após parar o serviço.
   - Como fazer: No campo de percentual executado, insira o valor correspondente ao progresso do serviço.
   - Observações importantes: O percentual deve refletir a quantidade de trabalho realizado em relação ao total esperado.
   - Resultado esperado: O percentual executado é atualizado e refletido no acompanhamento da obra.

5. **Finalizar Serviço**
   - Localização: Na tela de Controle de Serviços de Alvenaria, após o serviço ser concluído.
   - Como fazer: Clique no botão **Finalizar Serviço**.
   - Resultado esperado: O status do serviço muda para **Finalizado**.

**Campos e Parâmetros:**

| Campo                  | Tipo     | Obrigatório | Descrição                                         | Exemplo             |
|------------------------|----------|-------------|---------------------------------------------------|---------------------|
| `Data de Início`      | Data     | Sim         | Data em que o serviço é iniciado.                 | 29/10/2023          |
| `Horário de Início`    | Hora     | Sim         | Hora em que o serviço é iniciado.                 | 08:00               |
| `Colaborador`          | Seleção  | Não         | Colaborador associado ao serviço.                  | João Silva          |
| `Horário de Parada`   | Hora     | Sim         | Hora em que o serviço é parado.                   | 10:30               |
| `Observação`          | Texto    | Não         | Notas sobre a parada do serviço.                   | "Parada para almoço"|
| `Quantidade Executada` | Numérico | Sim         | Quantidade de trabalho realizado até o momento.   | 30                  |
| `Percentual Executado` | Numérico | Sim         | Percentual de conclusão do serviço.                | 30%                 |

**Regras de Negócio:**
- A data de início não pode ser anterior à data de liberação do serviço.
- O percentual executado deve ser um valor entre 0 e 100.
- O status do serviço muda para **Parado** quando o serviço é interrompido e para **Finalizado** quando o serviço é concluído.

**Observações Importantes:**
- É recomendado que os apontamentos sejam feitos de acordo com a organização da equipe, podendo ser diários, semanais ou mensais.
- Evite iniciar um serviço antes da data de liberação para evitar conflitos.

**Conceitos-Chave:**
- **Alvenaria**: Processo de construção que utiliza blocos ou tijolos.
- **Percentual Executado**: Medida que indica a proporção do serviço concluído em relação ao total.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                       | Causa Provável                     | Solução                                               | Prevenção                                           |
|--------------------------------|------------------------------------|-------------------------------------------------------|----------------------------------------------------|
| Não consigo iniciar o serviço   | Data de início anterior à liberação| Verifique a data de liberação e ajuste a data de início. | Sempre verifique as datas antes de iniciar.       |
| Botão de finalizar desabilitado | Serviço ainda não concluído        | Certifique-se de que o percentual executado está correto e que o serviço foi parado. | Monitore o progresso regularmente.                 |

**💡 DICAS E BOAS PRÁTICAS:**
- Realize apontamentos regulares para manter o controle do progresso.
- Utilize observações para registrar informações importantes sobre o serviço.
- Sempre verifique as datas de liberação antes de iniciar um novo serviço.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Início de Serviço**
```
Situação: Iniciar um serviço de alvenaria no dia 29/10/2023.
Ação: 
  • Campo Data de Início: "29/10/2023"
  • Campo Horário de Início: "08:00"
Resultado: O serviço é iniciado com a data e horário registrados.
```

**Exemplo 2: Parar e Registrar Progresso**
```
Situação: Parar o serviço após 30% de conclusão.
Ação: 
  • Campo Horário de Parada: "10:30"
  • Campo Observação: "Parada para almoço"
  • Campo Quantidade Executada: "30"
Resultado: O serviço é marcado como parado e o progresso é registrado.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O serviço deve ser liberado antes de ser iniciado.
- **Habilita:** O acompanhamento da obra é atualizado automaticamente com o percentual executado.
- **Relacionado a:** Funcionalidades de relatórios de progresso e controle de serviços.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como iniciar um serviço de alvenaria?"
- **Com problema:** "Não consigo iniciar o serviço, o que fazer?"
- **Informal:** "Como começo a obra?"
- **Por sintoma:** "O que fazer se a data de início não está correta?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Iniciar obra", "começar serviço", "registrar alvenaria", "apontar serviço"
- "Controle de serviços", "gerenciar alvenaria", "monitorar progresso"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como iniciar um serviço de alvenaria?
- O que fazer se a data de início não for aceita?
- Como parar um serviço de alvenaria?
- O que fazer se o percentual executado não estiver correto?
- O que preciso fazer antes de iniciar um serviço?

---


---


---

## 14. Comparativo de Cronograma e Atualização de Execução

**📋 METADADOS:**
- **ID:** sec_14
- **⏱️ Minutagem:** 33:11 → 35:43
- **⏲️ Duração:** 151s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/BdLq4eBgfxQ?si=Sxmnm__Ai1ReGR0_&t=1991)
- **📦 Módulo:** Cronograma
- **🏷️ Categorias:** Planejamento, Execução, Relatórios
- **🔑 Palavras-chave:** cronograma, comparativo, execução, planejamento, atualização

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como utilizar a funcionalidade de comparativo no cronograma, permitindo que o usuário acompanhe a execução de atividades em relação ao planejamento inicial. A funcionalidade é crucial para garantir que as atividades estejam dentro do cronograma estabelecido.

**Contexto:**
Estamos na interface do módulo de cronograma, onde o usuário pode visualizar e gerenciar o progresso das atividades planejadas e executadas. O objetivo desta seção é ensinar como atualizar o cronograma e como o sistema reflete essas atualizações no gráfico comparativo.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Cronograma > Tela de Comparativo
- Tela/interface específica: Tela de Comparativo de Cronograma

**Funcionalidade Detalhada:**
A funcionalidade de comparativo de cronograma permite que o usuário compare as datas planejadas de início e término das atividades com as datas reais de execução. O sistema atualiza automaticamente o gráfico de progresso com base nas informações inseridas, permitindo uma visualização clara do andamento das atividades.

### 🔹 Passo a Passo Detalhado:

1. **Acessar o Cronograma**
   - Localização: Menu Principal > Módulo Cronograma
   - Como fazer: Clique no módulo "Cronograma" no menu principal para acessar a tela de comparativo.
   - Resultado esperado: A tela de comparativo do cronograma será exibida, mostrando as atividades planejadas e executadas.

2. **Editar Data de Execução**
   - Localização: Tela de Comparativo de Cronograma
   - Como fazer: Clique na atividade que deseja editar e selecione a opção "Editar".
   - Campos/Opções disponíveis:
     * `Data de Término Planejada`: Campo para inserir a data planejada de término (formato: DD/MM).
     * `Data de Término Real`: Campo para inserir a data real de término (formato: DD/MM).
   - Resultado esperado: A data de término real será atualizada na atividade selecionada.

3. **Atualizar o Gráfico**
   - Localização: Tela de Comparativo de Cronograma
   - Como fazer: Após editar a data de término, clique no botão "Atualizar Gráfico".
   - Observações importantes: O gráfico só será atualizado se a atividade estiver marcada como finalizada.
   - Resultado esperado: O gráfico de comparativo será atualizado para refletir as novas datas de execução.

4. **Finalizar Atividade**
   - Localização: Tela de Comparativo de Cronograma
   - Como fazer: Selecione a atividade e clique no botão "Finalizar".
   - Resultado esperado: A atividade será marcada como finalizada, permitindo que o gráfico seja atualizado com as novas informações.

5. **Acessar Cronograma Financeiro**
   - Localização: Subaba do Cronograma
   - Como fazer: Clique na subaba "Cronograma Financeiro" na tela de comparativo.
   - Resultado esperado: O sistema exibirá informações financeiras vinculadas às ordens de compra e ordens de serviço.

**Campos e Parâmetros:**

| Campo                     | Tipo     | Obrigatório | Descrição                                           | Exemplo         |
|---------------------------|----------|-------------|----------------------------------------------------|------------------|
| `Data de Término Planejada` | Data     | Sim         | Data planejada para o término da atividade         | 08/10            |
| `Data de Término Real`      | Data     | Sim         | Data real em que a atividade foi finalizada        | 17/10            |

**Regras de Negócio:**
- O gráfico de comparativo é atualizado somente após a finalização da atividade.
- As despesas lançadas nas ordens de serviço e medições são contabilizadas automaticamente no cronograma financeiro.

**Observações Importantes:**
- Certifique-se de que a atividade está marcada como finalizada antes de tentar atualizar o gráfico.
- Evite editar datas de atividades que já foram finalizadas sem necessidade, pois isso pode causar inconsistências nos relatórios.

**Conceitos-Chave:**
- **Cronograma:** Representação visual do planejamento e execução de atividades.
- **Comparativo:** Análise entre o que foi planejado e o que foi executado.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                     | Solução                                         | Prevenção                                   |
|-----------------------------------|------------------------------------|------------------------------------------------|---------------------------------------------|
| Gráfico não atualiza              | Atividade não finalizada           | Finalize a atividade antes de atualizar o gráfico. | Sempre finalize atividades antes de atualizar. |
| Erro ao editar data               | Formato de data incorreto          | Verifique se a data está no formato DD/MM.     | Utilize o formato correto ao inserir datas.  |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre revise as datas planejadas antes de iniciar a execução.
- Utilize a funcionalidade de comparativo regularmente para manter o cronograma atualizado.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Atualização de Atividade**
```
Situação: O planejamento inicial previa a finalização da atividade no dia 8 de outubro, mas a execução foi concluída no dia 17 de outubro.
Ação: 
  • Campo `Data de Término Planejada`: "08/10"
  • Campo `Data de Término Real`: "17/10"
Resultado: O gráfico de comparativo é atualizado para refletir a nova data de término.
```

**Exemplo 2: Finalização de Atividade**
```
Situação: Uma atividade foi concluída antes do previsto.
Ação: 
  • Selecione a atividade e clique em "Finalizar".
Resultado: A atividade é marcada como finalizada e o gráfico é atualizado automaticamente.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** A atividade deve estar criada e planejada no cronograma.
- **Habilita:** A visualização de relatórios financeiros relacionados às ordens de compra e serviços.
- **Relacionado a:** Funcionalidades de ordens de serviço e medições.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como atualizar o cronograma?"
- **Com problema:** "O gráfico não está atualizando, o que fazer?"
- **Informal:** "Como eu faço para ver se estou dentro do cronograma?"
- **Por sintoma:** "Quando finalizo uma atividade, o gráfico não muda, por quê?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Atualizar cronograma", "comparar cronograma", "ver progresso", "analisar execução".

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como eu atualizo as datas de execução no cronograma?
- O que fazer se o gráfico não atualizar após a finalização da atividade?
- Como posso acessar o cronograma financeiro?
- O que acontece se eu editar uma data de atividade já finalizada?
- O que preciso fazer antes de atualizar o gráfico de comparativo?

---


---


---

## 15. Lançamento de Insumos e Controle de Orçamento

**📋 METADADOS:**
- **ID:** sec_15
- **⏱️ Minutagem:** 35:43 → 38:16
- **⏲️ Duração:** 152s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/BdLq4eBgfxQ?si=Sxmnm__Ai1ReGR0_&t=2143)
- **📦 Módulo:** Gestão de Compras
- **🏷️ Categorias:** Compras, Orçamento, Relatórios
- **🔑 Palavras-chave:** insumos, ordem de compra, orçamento, lançamento de nota, cronograma financeiro

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de lançamento de insumos no sistema, incluindo a associação com ordens de compra e a visualização do impacto no orçamento. O objetivo é permitir que os usuários controlem suas despesas e comparem os valores planejados com os reais.

**Contexto:**
Estamos na interface do módulo de Gestão de Compras, onde o usuário pode registrar a compra de insumos e monitorar o impacto financeiro desses insumos no cronograma da obra.

**Localização no Sistema:**
- Caminho de navegação: Menu Principal > Gestão de Compras > Lançamento de Insumos
- Tela/interface específica: Tela de Lançamento de Insumos

**Funcionalidade Detalhada:**
Esta funcionalidade permite ao usuário registrar a compra de insumos, associá-los a uma ordem de compra e visualizar o impacto no orçamento da obra. O sistema calcula automaticamente o valor total da compra e atualiza o cronograma financeiro.

### 🔹 Passo a Passo Detalhado:

1. **Selecionar Serviço e Insumo**
   - Localização: Tela de Lançamento de Insumos
   - Como fazer: O usuário deve identificar o serviço ao qual o insumo está alocado. O sistema já exibe essa informação automaticamente.
   - Resultado esperado: O serviço correto é exibido, permitindo que o usuário prossiga com o lançamento.

2. **Inserir Quantidade de Insumo**
   - Localização: Campo de entrada de quantidade
   - Como fazer: O usuário deve inserir a quantidade desejada de insumo a ser comprada. Por exemplo, para 500 m³, o usuário deve digitar `100`.
   - Resultado esperado: A quantidade é registrada no sistema.

3. **Inserir Valor Unitário**
   - Localização: Campo de entrada de valor unitário
   - Como fazer: O usuário deve inserir o valor unitário do insumo. Por exemplo, se o valor unitário for R$ 41, o usuário deve digitar `41`.
   - Resultado esperado: O valor unitário é salvo e utilizado para calcular o valor total.

4. **Associar a um Parceiro**
   - Localização: Campo de seleção de parceiro
   - Como fazer: O usuário deve selecionar um parceiro associado à compra do insumo.
   - Resultado esperado: O parceiro é vinculado à compra.

5. **Calcular Valor Total**
   - Localização: Campo de exibição de valor total
   - Como fazer: O sistema calcula automaticamente o valor total da compra com base na quantidade e no valor unitário. Por exemplo, para 100 insumos a R$ 41, o valor total será R$ 4100.
   - Resultado esperado: O valor total é exibido corretamente.

6. **Lançar Nota e Associar com Ordem de Compra**
   - Localização: Botão "Lançar Nota"
   - Como fazer: O usuário deve clicar no botão **Lançar Nota** e associar a nota à ordem de compra correspondente.
   - Observações importantes: Se a compra for referente a uma ordem de serviço, o processo é semelhante.
   - Resultado esperado: A nota é lançada e associada à ordem de compra.

7. **Visualizar Cronograma Financeiro**
   - Localização: Tela de Cronograma Financeiro
   - Como fazer: O usuário deve acessar o cronograma financeiro da obra para visualizar o impacto da compra. O sistema já atualiza automaticamente o valor referente ao mês.
   - Resultado esperado: O usuário vê a comparação entre o planejado e o real executado.

8. **Verificar Recursos Alocados**
   - Localização: Aba de Recursos Alocados
   - Como fazer: O usuário deve acessar a aba para visualizar a quantidade de insumos comprados e a média de compras.
   - Resultado esperado: O sistema exibe se o usuário está extrapolando o orçamento, mostrando a média de compra e a porcentagem de extrapolação.

**Campos e Parâmetros:**

| Campo                     | Tipo      | Obrigatório | Descrição                                           | Exemplo        |
|---------------------------|-----------|-------------|----------------------------------------------------|----------------|
| `Quantidade`              | Numérico  | Sim         | Quantidade do insumo a ser comprada                | 100            |
| `Valor Unitário`          | Monetário | Sim         | Valor unitário do insumo                            | R$ 41          |
| `Parceiro`                | Seleção   | Sim         | Parceiro associado à compra                         | Fornecedor A   |
| `Valor Total`             | Monetário | Não         | Valor total calculado pela quantidade e valor unitário | R$ 4100        |

**Regras de Negócio:**
- O valor total é calculado multiplicando a quantidade pelo valor unitário.
- O sistema deve atualizar automaticamente o cronograma financeiro após o lançamento da nota.
- O usuário deve ser notificado se a média de compra extrapolar o orçamento planejado.

**Observações Importantes:**
- É importante verificar se o valor unitário está correto antes de lançar a nota.
- Evitar lançar notas sem associá-las a uma ordem de compra ou serviço.

**Conceitos-Chave:**
- **Ordem de Compra**: Documento que formaliza a compra de insumos.
- **Cronograma Financeiro**: Ferramenta que permite visualizar os gastos planejados e reais ao longo do tempo.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                     | Solução                                                  | Prevenção                          |
|-----------------------------------|------------------------------------|----------------------------------------------------------|------------------------------------|
| Valor total não aparece           | Campo de valor unitário vazio      | Verifique se o campo de valor unitário foi preenchido.  | Sempre preencher todos os campos.  |
| Nota não associada à ordem        | Ordem de compra não selecionada    | Certifique-se de selecionar a ordem de compra correta.   | Verificar a seleção antes de lançar. |
| Extrapolação de orçamento não aparece | Dados de compra não atualizados | Atualize a tela ou verifique a aba de recursos alocados. | Monitorar regularmente as compras. |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre revise os valores antes de finalizar o lançamento.
- Utilize filtros para visualizar o cronograma financeiro por mês, semana ou dia.
- Mantenha um registro das compras para facilitar a análise de orçamento.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Lançamento de Insumo para Obra**
```
Situação: O usuário precisa comprar 100 m³ de um insumo a R$ 41 cada.
Ação: 
  • Campo `Quantidade`: "100"
  • Campo `Valor Unitário`: "41"
Resultado: O valor total é calculado como R$ 4100 e a nota é lançada associada à ordem de compra.
```

**Exemplo 2: Verificação de Orçamento**
```
Situação: Após várias compras, o usuário verifica se está dentro do orçamento.
Ação: O usuário acessa a aba de recursos alocados e verifica a média de compras.
Resultado: O sistema indica que o usuário está extrapolando o orçamento em 13,89%.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O usuário deve ter permissões para lançar notas e acessar o módulo de Gestão de Compras.
- **Habilita:** A visualização do cronograma financeiro e o controle de orçamento.
- **Relacionado a:** Módulo de Gestão de Orçamento e Relatórios Financeiros.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como lançar um insumo?"
- **Com problema:** "Não consigo associar a nota à ordem de compra, o que fazer?"
- **Informal:** "Como eu compro insumos no sistema?"
- **Por sintoma:** "O que fazer se o valor total não aparece?"
- **Com variação:** "Como verificar se estou extrapolando o orçamento?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Registrar compra", "Adicionar insumo", "Lançar nota de compra", "Associar insumo a ordem".

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como lançar um insumo no sistema?
- O que fazer se o valor total não aparecer?
- Como verificar se estou dentro do orçamento?
- O que fazer se a nota não estiver associada à ordem de compra?
- O que preciso fazer antes de lançar um insumo?

---


---


---

## 16. Criação de Ordens de Serviço e Medições

**📋 METADADOS:**
- **ID:** sec_16
- **⏱️ Minutagem:** 38:13 → 40:46
- **⏲️ Duração:** 152s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/BdLq4eBgfxQ?si=Sxmnm__Ai1ReGR0_&t=2293)
- **📦 Módulo:** Acompanhamento de Obras
- **🏷️ Categorias:** Operacional, Cadastro, Relatório
- **🔑 Palavras-chave:** ordem de serviço, medições, prestador de serviço, cronograma, valores fixos

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como criar ordens de serviço e medições dentro do sistema, explicando as diferenças entre elas e orientando o usuário sobre como preencher os campos necessários.

**Contexto:**
Estamos no módulo de Acompanhamento de Obras, onde o usuário pode gerenciar serviços relacionados a uma obra específica. O objetivo desta seção é ensinar como registrar ordens de serviço e medições, fundamentais para o controle financeiro e operacional de serviços contratados.

**Localização no Sistema:**
- Caminho de navegação: Menu Principal > Acompanhamento de Obras > Subaba de Serviços
- Tela/interface específica: Tela de Criação de Ordens de Serviço e Medições

**Funcionalidade Detalhada:**
A funcionalidade permite ao usuário criar ordens de serviço e medições. As ordens de serviço são utilizadas quando o usuário já tem informações fixas sobre o pagamento a um prestador de serviço, enquanto as medições são usadas quando o pagamento depende da execução do serviço.

### 🔹 Passo a Passo Detalhado:

1. **Criar Ordem de Serviço**
   - Localização: Subaba de Serviços na tela de Acompanhamento de Obras
   - Como fazer: Clique no botão **"Criar Ordem de Serviço"**.
   - Campos/Opções disponíveis:
     * `Descrição`: Campo de texto onde o usuário pode inserir informações adicionais sobre o serviço.
     * `Data Inicial`: Campo de data que puxa automaticamente a data do cronograma.
     * `Data Final`: Campo de data que também puxa automaticamente do cronograma.
     * `Quantidade`: Campo numérico que indica a quantidade de serviço a ser executado.
     * `Valor Unitário`: Campo numérico que indica o valor por unidade do serviço.
   - Resultado esperado: Uma nova ordem de serviço é criada e registrada no sistema, refletindo as informações inseridas.

2. **Criar Medição**
   - Localização: Subaba de Serviços na tela de Acompanhamento de Obras
   - Como fazer: Clique no botão **"Criar Medição"**.
   - Observações importantes: O sistema não possui informações fixas sobre o pagamento, portanto, o usuário deve acompanhar a execução do serviço para determinar o valor a ser pago.
   - Resultado esperado: Uma nova medição é registrada, permitindo que o usuário acompanhe o progresso e os custos associados ao serviço.

**Campos e Parâmetros:**

| Campo            | Tipo       | Obrigatório | Descrição                                         | Exemplo           |
|------------------|------------|-------------|---------------------------------------------------|-------------------|
| Descrição        | Texto      | Não         | Informações adicionais sobre o serviço.           | "Serviço de Alvenaria" |
| Data Inicial     | Data       | Sim         | Data de início do serviço, puxada do cronograma.  | "01/01/2024"      |
| Data Final       | Data       | Sim         | Data de término do serviço, puxada do cronograma. | "31/01/2024"      |
| Quantidade       | Numérico   | Sim         | Quantidade de serviço a ser executado.            | "1000"            |
| Valor Unitário   | Numérico   | Sim         | Valor por unidade do serviço.                       | "50"              |

**Regras de Negócio:**
- Ordens de serviço devem ser criadas quando há valores fixos definidos para pagamento.
- Medições devem ser criadas quando o pagamento depende da execução do serviço.
- O sistema puxa automaticamente as datas do cronograma, mas o usuário pode alterá-las.

**Observações Importantes:**
- É importante verificar se os serviços estão alocados corretamente na obra antes de criar ordens de serviço ou medições.
- Erros comuns incluem a inserção de valores incorretos nos campos de quantidade e valor unitário.

**Conceitos-Chave:**
- **Ordem de Serviço**: Documento que formaliza a contratação de um prestador de serviço com valores e datas fixas.
- **Medição**: Registro que permite acompanhar a execução de um serviço sem valores fixos previamente definidos.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                     | Solução                                           | Prevenção                                      |
|-----------------------------------|------------------------------------|--------------------------------------------------|------------------------------------------------|
| Botão "Criar Ordem de Serviço" desabilitado | Falta de permissões de usuário     | Verificar permissões em Admin > Usuários         | Configurar permissões antes de tentar criar   |
| Dados não são salvos              | Campos obrigatórios não preenchidos | Preencher todos os campos obrigatórios            | Revisar campos antes de salvar                 |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre revise as informações inseridas antes de salvar.
- Utilize descrições claras para facilitar a identificação dos serviços.
- Mantenha um registro atualizado das medições para evitar surpresas no pagamento.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Criação de Ordem de Serviço**
```
Situação: Contratação de serviço de alvenaria para uma obra.
Ação: Criar uma ordem de serviço com os seguintes valores:
  • Descrição: "Serviço de Alvenaria"
  • Data Inicial: "01/01/2024"
  • Data Final: "31/01/2024"
  • Quantidade: "1000"
  • Valor Unitário: "50"
Resultado: A ordem de serviço é criada e registrada no sistema, permitindo o pagamento fixo ao prestador.
```

**Exemplo 2: Criação de Medição**
```
Situação: Acompanhamento de serviços de pintura onde o valor depende da execução.
Ação: Criar uma medição sem valores fixos.
Resultado: A medição é registrada, permitindo que o usuário acompanhe o progresso e determine o pagamento conforme o serviço é executado.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O serviço deve estar alocado na obra para que possa ser registrado.
- **Habilita:** A criação de relatórios financeiros e de progresso da obra.
- **Relacionado a:** Módulo de Compras, onde os materiais e serviços são cadastrados.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como criar uma ordem de serviço?"
- **Com problema:** "Não consigo registrar uma medição, o que fazer?"
- **Informal:** "Como faço pra adicionar um serviço?"
- **Por sintoma:** "O que fazer se o botão de criar ordem não aparece?"
- **Variações:** "Cadastrar ordem de serviço", "Adicionar medição", "Registrar serviço", "Criar serviço", "Inserir medição".

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Criar ordem", "Adicionar serviço", "Registrar medição", "Inserir ordem de serviço", "Cadastrar medição".

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como criar uma ordem de serviço?
- Qual a diferença entre ordem de serviço e medição?
- O que fazer se o sistema não salvar minha medição?
- Como posso alterar a data de uma ordem de serviço?
- O que preciso fazer antes de criar uma ordem de serviço?

---


---


---

## 17. Emissão e Gestão de Contratos e Medições

**📋 METADADOS:**
- **ID:** sec_17
- **⏱️ Minutagem:** 40:44 → 43:16
- **⏲️ Duração:** 151s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/BdLq4eBgfxQ?si=Sxmnm__Ai1ReGR0_&t=2444)
- **📦 Módulo:** Administração
- **🏷️ Categorias:** Contratos, Medições, Financeiro, Prestadores
- **🔑 Palavras-chave:** contrato, prestador, medição, valor total, quantidade, valor unitário

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de emissão de contratos e gestão de medições para serviços prestados, incluindo como calcular valores totais e associar contratos a medições, facilitando o controle financeiro e operacional.

**Contexto:**
Estamos no módulo de Administração do sistema, onde o usuário pode gerenciar contratos e medições relacionadas a serviços prestados por prestadores. O objetivo é garantir que todos os serviços sejam devidamente contratados e medidos, permitindo um controle financeiro eficiente.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Administração > Submenu Contratos
- Tela/interface específica: Tela de Emissão de Contratos e Medições

**Funcionalidade Detalhada:**
Esta funcionalidade permite ao usuário emitir contratos para prestadores de serviços, calcular valores totais com base na quantidade e valor unitário, e gerar medições associadas a esses contratos. O sistema facilita a gestão financeira ao permitir a edição de contratos antes de serem assinados e a geração de medições conforme o serviço é executado.

### 🔹 Passo a Passo Detalhado:

1. **Inserir Quantidade e Calcular Valor Total**
   - Localização: Tela de Emissão de Contratos
   - Como fazer: O usuário deve inserir a quantidade de serviços a serem contratados no campo designado.
   - Campos/Opções disponíveis:
     * `Quantidade`: Campo numérico onde o usuário insere a quantidade de serviços (ex: 100).
     * `Valor Unitário`: Campo que exibe o valor unitário do serviço.
   - Resultado esperado: O sistema multiplica a quantidade pelo valor unitário e exibe o valor total a ser pago ao prestador.

2. **Selecionar Prestador**
   - Localização: Tela de Emissão de Contratos
   - Como fazer: O usuário deve selecionar o prestador que irá executar o serviço a partir de um menu suspenso.
   - Observações importantes: O prestador deve estar previamente cadastrado no sistema.
   - Resultado esperado: O prestador selecionado é associado ao contrato.

3. **Definir Pagamento a Prazo**
   - Localização: Tela de Emissão de Contratos
   - Como fazer: Se o pagamento for a prazo, o usuário deve inserir a quantidade de parcelas no campo designado.
   - Campos/Opções disponíveis:
     * `Quantidade de Parcelas`: Campo numérico onde o usuário insere o número de vezes que pagará ao prestador.
   - Resultado esperado: O sistema registra a informação de pagamento a prazo.

4. **Emitir o Contrato**
   - Localização: Tela de Emissão de Contratos
   - Como fazer: Após preencher todas as informações, o usuário deve clicar no botão **Emitir Contrato**.
   - Resultado esperado: O contrato é gerado e aparece na lista de contratos emitidos.

5. **Assinar Contrato**
   - Localização: Tela de Contratos Emitidos
   - Como fazer: O usuário pode importar o contrato assinado pelo prestador e clicar no botão **Assinar Contrato**.
   - Observações importantes: O contrato só pode ser editado antes de ser assinado.
   - Resultado esperado: O status do contrato muda para "Assinado".

6. **Gerar Medição**
   - Localização: Tela de Medições
   - Como fazer: O usuário deve clicar em **Mais Medição** e associar a medição ao contrato emitido.
   - Campos/Opções disponíveis:
     * `Contrato`: Menu suspenso para selecionar o contrato associado.
   - Resultado esperado: A medição é criada e associada ao contrato.

7. **Inserir Quantidade Medida**
   - Localização: Tela de Medições
   - Como fazer: O usuário deve inserir a quantidade medida no campo designado.
   - Observações importantes: O sistema exibe a quantidade planejada conforme o contrato.
   - Resultado esperado: A quantidade medida é registrada e pode ser visualizada.

**Campos e Parâmetros:**

| Campo                   | Tipo       | Obrigatório | Descrição                                         | Exemplo            |
|-------------------------|------------|-------------|---------------------------------------------------|--------------------|
| `Quantidade`            | Numérico   | Sim         | Quantidade de serviços a serem contratados       | 100                |
| `Valor Unitário`        | Numérico   | Sim         | Valor unitário do serviço                          | 50,00              |
| `Quantidade de Parcelas`| Numérico   | Não         | Número de parcelas para pagamento a prazo         | 5                  |
| `Prestador`             | Dropdown   | Sim         | Prestador que executará o serviço                 | João Silva         |
| `Contrato`              | Dropdown   | Sim         | Contrato associado à medição                      | Contrato_2024      |
| `Quantidade Medida`     | Numérico   | Sim         | Quantidade de serviços efetivamente medidos       | 80                 |

**Regras de Negócio:**
- O valor total é calculado automaticamente multiplicando a `Quantidade` pelo `Valor Unitário`.
- O prestador deve ser selecionado de uma lista pré-cadastrada.
- O contrato pode ser editado antes de ser assinado, mas após a assinatura, apenas aditivos podem ser criados.
- A medição deve ser associada a um contrato previamente emitido.

**Observações Importantes:**
- É importante verificar se o prestador está cadastrado antes de emitir o contrato.
- Evitar editar contratos após a assinatura, pois isso pode gerar inconsistências.
- O sistema permite a importação de contratos assinados para facilitar a gestão.

**Conceitos-Chave:**
- **Contrato**: Documento que formaliza a prestação de serviços entre o contratante e o prestador.
- **Medição**: Registro da quantidade de serviços efetivamente prestados, que pode ser associado a um contrato.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                     | Solução                                         | Prevenção                                   |
|-----------------------------------|------------------------------------|------------------------------------------------|---------------------------------------------|
| Não consigo emitir o contrato     | Prestador não cadastrado           | Verificar se o prestador está cadastrado em Administração > Prestadores | Cadastrar prestadores antes de emitir contratos |
| Botão de assinar contrato desabilitado | Contrato já assinado               | Não é possível editar contratos assinados; crie um aditivo | Editar antes da assinatura                  |
| Erro ao gerar medição             | Contrato não associado             | Certifique-se de que a medição está associada a um contrato emitido | Associar medições corretamente               |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre revise os dados inseridos antes de emitir um contrato.
- Utilize a funcionalidade de edição para corrigir informações antes da assinatura.
- Mantenha um registro organizado dos contratos e medições para facilitar a auditoria.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Emissão de Contrato para Serviços de Limpeza**
```
Situação: Contratação de serviços de limpeza para um evento.
Ação: 
  • Campo `Quantidade`: 100
  • Campo `Valor Unitário`: 50,00
Resultado: O valor total a ser pago ao prestador será 5.000,00. O contrato é emitido e associado ao prestador "Limpeza Rápida".
```

**Exemplo 2: Geração de Medição para Serviços de Construção**
```
Situação: Medição de serviços de construção realizados.
Ação: 
  • Selecionar o contrato "Construção Edifício A"
  • Campo `Quantidade Medida`: 80
Resultado: A quantidade medida é registrada e associada ao contrato, permitindo o controle financeiro.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O prestador deve estar cadastrado no sistema antes da emissão do contrato.
- **Habilita:** A geração de medições e o controle financeiro de serviços prestados.
- **Relacionado a:** Módulo Financeiro para lançamento de notas e pagamentos.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como emitir um contrato para um prestador?"
- **Com problema:** "Não consigo emitir um contrato, o que fazer?"
- **Informal:** "Como faço para contratar alguém?"
- **Por sintoma:** "O que fazer se o botão de assinar contrato não está funcionando?"
- **Com foco em medições:** "Como registrar a medição de um serviço?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Emitir contrato", "criar contrato", "gerar contrato"
- "Registrar medição", "inserir medição", "adicionar medição"
- "Prestador de serviços", "fornecedor", "contratado"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como emitir um contrato para um prestador?
- O que fazer se o prestador não está na lista?
- Como registrar a medição de um serviço?
- O que fazer se o botão de assinar contrato não está habilitado?
- O que preciso ter cadastrado antes de emitir um contrato?

---


---


---

## 18. Registro e Liberação de Medições de Serviços

**📋 METADADOS:**
- **ID:** sec_18
- **⏱️ Minutagem:** 43:15 → 45:48
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/BdLq4eBgfxQ?si=Sxmnm__Ai1ReGR0_&t=2595)
- **📦 Módulo:** Medições e Liberações Financeiras
- **🏷️ Categorias:** Medições, Financeiro, Contratos
- **🔑 Palavras-chave:** medição, alvenaria, valor a pagar, valor a receber, liberação financeira

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de registro e liberação de medições de serviços, incluindo a inserção de quantidades, cálculo automático de valores e a finalização do processo de liberação financeira.

**Contexto:**
Estamos na etapa de registro de medições de serviços prestados, onde o usuário deve inserir as quantidades de serviços realizados e finalizar a medição para que os valores possam ser calculados e liberados financeiramente.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Medições e Liberações Financeiras > Submenu Registro de Medições
- Tela/interface específica: Tela de Registro de Medições

**Funcionalidade Detalhada:**
A funcionalidade permite ao usuário registrar medições de serviços, como alvenaria, e calcular automaticamente os valores a pagar e a receber com base nas informações do contrato e do planejamento da obra. O usuário pode finalizar a medição e proceder com a liberação financeira.

### 🔹 Passo a Passo Detalhado:

1. **Registro da Medição**
   - Localização: Tela de Registro de Medições
   - Como fazer: O usuário deve inserir a quantidade de serviços realizados. Por exemplo, para o serviço de alvenaria, o usuário deve especificar a quantidade de blocos executados.
   - Campos/Opções disponíveis:
     * `Quantidade Medida`: Campo numérico onde o usuário insere a quantidade de serviços realizados (ex: "2" para dois blocos).
     * `Forma de Medição`: Dropdown onde o usuário seleciona a forma de medição (ex: "por bloco").
   - Resultado esperado: O sistema calcula automaticamente o valor a pagar e o valor a receber com base nas informações do contrato e do planejamento da obra.

2. **Finalização da Medição**
   - Localização: Botão "Finalizar Medição" na parte inferior da tela
   - Como fazer: Após inserir as quantidades, o usuário deve clicar no botão **Finalizar Medição** para concluir o registro.
   - Observações importantes: O usuário pode optar por imprimir a medição com ou sem os valores.
   - Resultado esperado: A medição é finalizada e o sistema registra a informação.

3. **Aprovação da Medição**
   - Localização: Botão "Aprovar Medição" na tela de confirmação
   - Como fazer: Após finalizar a medição, o usuário deve clicar no botão **Aprovar Medição**.
   - Resultado esperado: A medição é aprovada, mas ainda não gera contas a pagar ou a receber até que a liberação financeira seja realizada.

4. **Liberação Financeira**
   - Localização: Menu "Liberações Financeiras"
   - Como fazer: O usuário deve acessar a seção de liberações financeiras e associar o contrato referente à medição.
   - Campos/Opções disponíveis:
     * `Contrato`: Dropdown com todos os contratos disponíveis.
     * `Data de Vencimento`: Campo de data onde o usuário insere a data limite para o pagamento.
     * `Retenção`, `Desconto`, `Adiantamento`, `Acréscimos`: Campos opcionais para ajustes financeiros.
   - Resultado esperado: O sistema gera uma conta a pagar associada à medição liberada.

**Campos e Parâmetros:**

| Campo                   | Tipo        | Obrigatório | Descrição                                            | Exemplo             |
|-------------------------|-------------|-------------|-----------------------------------------------------|---------------------|
| `Quantidade Medida`     | Numérico    | Sim         | Quantidade de serviços realizados                    | 2                   |
| `Forma de Medição`      | Dropdown    | Sim         | Método de medição utilizado                          | por bloco           |
| `Data de Vencimento`    | Data        | Sim         | Data limite para o pagamento                         | 30/11/2023          |
| `Retenção`              | Numérico    | Não         | Valor a ser retido do pagamento                      | 10%                 |
| `Desconto`              | Numérico    | Não         | Valor a ser descontado do pagamento                  | 50                   |
| `Adiantamento`          | Numérico    | Não         | Valor a ser adiantado no pagamento                   | 1000                |
| `Acréscimos`           | Numérico    | Não         | Valores adicionais a serem considerados               | 200                 |

**Regras de Negócio:**
- A medição deve ser aprovada antes de gerar contas a pagar ou a receber.
- Os valores a pagar e a receber são calculados automaticamente com base nas informações do contrato e do planejamento da obra.
- O usuário pode liberar todos os serviços de uma vez ou em partes.

**Observações Importantes:**
- É importante verificar se todos os campos obrigatórios estão preenchidos antes de finalizar a medição.
- Evitar inserir valores incorretos nas quantidades, pois isso afetará os cálculos financeiros.
- A liberação financeira deve ser feita após a aprovação da medição.

**Conceitos-Chave:**
- **Medição**: Registro da quantidade de serviços realizados para fins de pagamento.
- **Liberação Financeira**: Processo de autorização para efetuar pagamentos relacionados às medições aprovadas.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                      | Solução                                         | Prevenção                                   |
|-----------------------------------|-------------------------------------|------------------------------------------------|---------------------------------------------|
| Medição não aparece na lista      | Medição não foi finalizada          | Verifique se a medição foi finalizada corretamente. | Sempre finalize a medição após o registro. |
| Valores a pagar não calculam      | Campos obrigatórios não preenchidos | Preencha todos os campos obrigatórios corretamente. | Validar informações antes de finalizar.    |
| Botão de liberação desabilitado   | Medição não aprovada                | Certifique-se de que a medição foi aprovada.   | Aprovar a medição antes de liberar.        |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre revise as quantidades inseridas para evitar erros nos cálculos.
- Utilize a impressão da medição para conferência antes da liberação financeira.
- Mantenha um registro das datas de vencimento para evitar atrasos nos pagamentos.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Registro de Medição de Alvenaria**
```
Situação: O prestador realizou a construção de 2 blocos de alvenaria.
Ação: O usuário insere "2" no campo `Quantidade Medida` e seleciona "por bloco" na `Forma de Medição`.
Resultado: O sistema calcula automaticamente o valor a pagar e a receber com base no contrato.
```

**Exemplo 2: Liberação Financeira**
```
Situação: A medição foi aprovada e o usuário deseja liberar o pagamento.
Ação: O usuário acessa "Liberações Financeiras", associa o contrato e insere a data de vencimento como "30/11/2023".
Resultado: O sistema gera uma conta a pagar associada à medição liberada.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** A medição deve ser registrada e aprovada antes da liberação financeira.
- **Habilita:** A liberação financeira permite que o usuário efetue pagamentos relacionados às medições.
- **Relacionado a:** Módulo de Contratos, Módulo de Orçamento.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como registrar uma medição?"
- **Com problema:** "Não consigo finalizar a medição, o que fazer?"
- **Informal:** "Como faço para liberar o pagamento da medição?"
- **Por sintoma:** "Quando aprovo uma medição, o que acontece?"
- **Com variação:** "Qual o passo a passo para liberar uma medição?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Registrar medição", "Adicionar medição", "Finalizar medição", "Liberar pagamento"
- "Medição de serviços", "Registro de serviços", "Liberação de valores"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como registro uma medição de serviços?
- O que fazer se a medição não aparece na lista?
- Como aprovo uma medição?
- O que fazer se o botão de liberação está desabilitado?
- O que preciso fazer antes de liberar a medição financeiramente?

---


---


---

## 19. Liberação de Recebimentos Financeiros

**📋 METADADOS:**
- **ID:** sec_19
- **⏱️ Minutagem:** 45:45 → 48:14
- **⏲️ Duração:** 148s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/BdLq4eBgfxQ?si=Sxmnm__Ai1ReGR0_&t=2745)
- **📦 Módulo:** Financeiro
- **🏷️ Categorias:** Recebimentos, Gestão Financeira, Contas a Receber
- **🔑 Palavras-chave:** liberar financeiro, contas a receber, medição, saldo, valor total

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de liberação de recebimentos financeiros no sistema, permitindo que a empresa receba pagamentos de forma parcial ou total. O objetivo é garantir que os usuários entendam como gerenciar os valores a receber de forma eficaz.

**Contexto:**
Estamos na área financeira do sistema, especificamente na subaba de "A Receber", onde o usuário pode gerenciar os recebimentos de pagamentos de prestadores de serviços ou fornecedores.

**Localização no Sistema:**
- Caminho de navegação: Menu Principal > Módulo Financeiro > Submenu A Receber
- Tela/interface específica: Tela de Recebimentos Financeiros

**Funcionalidade Detalhada:**
A funcionalidade de liberação de recebimentos financeiros permite que o usuário visualize e gerencie os pagamentos que a empresa deve receber. O usuário pode liberar valores de forma total ou parcial, definir datas de vencimento e acompanhar o saldo de recebimentos.

### 🔹 Passo a Passo Detalhado:

1. **Visualizar Recebimentos**
   - Localização: Subaba "A Receber" dentro do módulo financeiro.
   - Como fazer: Clique na opção **Visualizar** para acessar a lista de recebimentos pendentes.
   - Resultado esperado: A tela exibirá todos os recebimentos que estão aguardando liberação.

2. **Liberar Financeiro**
   - Localização: Após visualizar os recebimentos, clique no botão **Liberar Financeiro**.
   - Como fazer: Selecione a opção de liberar todos os valores ou apenas uma parte deles. Para liberar parcialmente, escolha a quantia desejada.
   - Campos/Opções disponíveis:
     * `Data de Vencimento`: Campo para inserir a data limite até quando o pagamento deve ser recebido.
   - Resultado esperado: O sistema processará a liberação e atualizará o status dos recebimentos.

3. **Ver Conta de Origem**
   - Localização: Após a liberação, clique na opção **Ver Conta de Origem** para verificar detalhes do recebimento.
   - Como fazer: O sistema redirecionará para a tela de **Contas a Receber**, onde será possível visualizar o valor total acordado com o prestador e o valor atual que foi liberado.
   - Observações importantes: O valor liberado será subtraído do total acordado, atualizando o saldo a receber.
   - Resultado esperado: A tela mostrará o valor total acordado, o valor já liberado e o saldo restante.

4. **Gerar Parcelas**
   - Localização: Na tela de **Contas a Receber**, após a liberação dos valores.
   - Como fazer: O sistema automaticamente gerará parcelas com base nas medições realizadas.
   - Resultado esperado: O saldo a receber será atualizado conforme as medições forem sendo realizadas, refletindo o valor total acordado menos os valores já liberados.

**Campos e Parâmetros:**

| Campo               | Tipo     | Obrigatório | Descrição                                           | Exemplo                  |
|---------------------|----------|-------------|----------------------------------------------------|--------------------------|
| Data de Vencimento  | Data     | Sim         | Data limite para o recebimento do pagamento.       | 30/11/2023               |
| Valor Total         | Numérico | Sim         | Valor total acordado com o prestador.              | R$ 60.000,00             |
| Valor Liberado      | Numérico | Não         | Valor que foi liberado para recebimento.           | R$ 5.555,00              |
| Saldo a Receber     | Numérico | Não         | Valor restante a ser recebido após liberações.     | R$ 1.556.619,44          |

**Regras de Negócio:**
- O usuário pode liberar valores de forma total ou parcial.
- A data de vencimento deve ser preenchida para cada liberação.
- O saldo a receber é atualizado automaticamente conforme as medições são realizadas.

**Observações Importantes:**
- Certifique-se de que todos os valores estão corretos antes de liberar, pois isso afetará o fluxo financeiro.
- Evite liberar valores que não correspondem às medições realizadas, pois isso pode gerar discrepâncias.

**Conceitos-Chave:**
- **Medição**: Processo de avaliação do trabalho realizado que determina o valor a ser recebido.
- **Contas a Receber**: Registro financeiro que mostra os valores que a empresa tem a receber de clientes ou prestadores.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                    | Solução                                      | Prevenção                                   |
|-----------------------------------|-----------------------------------|----------------------------------------------|---------------------------------------------|
| Não consigo liberar o pagamento    | Campo de data não preenchido      | Preencha o campo **Data de Vencimento**    | Sempre verifique se todos os campos obrigatórios estão preenchidos. |
| Valor liberado não aparece no saldo| Falha na atualização do sistema    | Tente recarregar a página ou verificar as medições | Monitore as medições regularmente.         |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre revise os valores antes de confirmar a liberação.
- Utilize a funcionalidade de visualização para garantir que todos os recebimentos estão corretos.
- Mantenha um registro das medições realizadas para facilitar o acompanhamento dos saldos.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Liberação Total de Recebimento**
```
Situação: A empresa fechou um contrato de R$ 60.000,00 com um prestador.
Ação: O usuário acessa a subaba "A Receber", visualiza o recebimento e clica em "Liberar Financeiro", selecionando a opção de liberar o valor total.
  • Campo Data de Vencimento: "30/11/2023"
Resultado: O sistema atualiza o saldo a receber para R$ 0,00, indicando que o valor total foi liberado.
```

**Exemplo 2: Liberação Parcial de Recebimento**
```
Situação: A empresa precisa liberar apenas R$ 5.555,00 de um total de R$ 60.000,00.
Ação: O usuário acessa a subaba "A Receber", visualiza o recebimento e clica em "Liberar Financeiro", optando por liberar parcialmente.
  • Campo Data de Vencimento: "30/11/2023"
Resultado: O sistema atualiza o saldo a receber para R$ 54.445,00, refletindo a liberação parcial.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O usuário deve ter permissões adequadas para realizar liberações financeiras.
- **Habilita:** A liberação de recebimentos permite que o usuário acompanhe o fluxo de caixa e as medições.
- **Relacionado a:** Funcionalidades de medições e controle de contas a receber.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como liberar um recebimento financeiro?"
- **Com problema:** "Não consigo liberar o pagamento, o que fazer?"
- **Informal:** "Como faço pra receber o que me devem?"
- **Por sintoma:** "O que fazer se o saldo não atualizar após liberar um pagamento?"
- **Com dúvida:** "Qual o processo para liberar pagamentos parciais?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Liberar pagamento", "autorizar recebimento", "gerar recebimento", "receber valores".

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como faço para liberar um recebimento financeiro?
- O que fazer se não consigo liberar um pagamento?
- Como visualizar os recebimentos pendentes?
- O que acontece se o saldo não atualizar após a liberação?
- O que preciso ter feito antes de liberar um recebimento?

---


---


---

## 20. Diário de Obras

**📋 METADADOS:**
- **ID:** sec_20
- **⏱️ Minutagem:** 48:17 → 50:50
- **⏲️ Duração:** 152s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/BdLq4eBgfxQ?si=Sxmnm__Ai1ReGR0_&t=2897)
- **📦 Módulo:** Diário de Obras
- **🏷️ Categorias:** Registro, Monitoramento, Relatório
- **🔑 Palavras-chave:** diário, obra, interações, registro climático, ordem de serviço

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como utilizar o Diário de Obras, incluindo o registro de interações e informações climáticas, além de como visualizar as ações realizadas em relação à obra. O objetivo é fornecer um controle eficaz das atividades diárias da obra.

**Contexto:**
Estamos na interface do módulo Diário de Obras, onde o usuário pode visualizar e registrar informações relevantes sobre o andamento da obra, a partir da data de início cadastrada.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Diário de Obras
- Tela/interface específica: Tela do Diário de Obras

**Funcionalidade Detalhada:**

O Diário de Obras permite que o usuário visualize um resumo das atividades diárias da obra, que são preenchidas automaticamente com base nas ações realizadas em outros módulos do sistema. O diário é iniciado a partir da data de início da obra, que foi cadastrada previamente. O usuário pode registrar interações e informações climáticas, além de visualizar as ações realizadas, como ordens de serviço e medições.

### 🔹 Passo a Passo Detalhado:

1. **Visualizar o Diário de Obras**
   - Localização: Tela do Diário de Obras
   - Como fazer: Ao acessar o módulo, o diário será exibido automaticamente a partir da data de início da obra. Para ver mais detalhes, clique no botão **Ver mais detalhes**.
   - Resultado esperado: Um resumo das ações realizadas, como medições, ordens de serviço e serviços iniciados, será exibido.

2. **Registrar Interações**
   - Localização: Tela do Diário de Obras, seção de interações
   - Como fazer: Clique no botão **Alterar tipos de interação**. Em seguida, clique em **Mais tipo**, insira a nomenclatura desejada e clique em **Salvar**. Para registrar uma interação, clique na interação desejada e, em seguida, clique em **Mais registrar a interação**. Descreva a interação e clique em **Salvar**.
   - Observações importantes: As interações podem ser personalizadas conforme as necessidades do usuário.
   - Resultado esperado: As interações registradas aparecerão em ordem cronológica, com código, data, hora e usuário que registrou.

3. **Registrar Informações Climáticas**
   - Localização: Tela do Diário de Obras, seção de registro climático
   - Como fazer: Clique na opção correspondente para registrar as informações climáticas do dia.
   - Resultado esperado: As informações climáticas serão salvas e associadas ao diário da obra.

4. **Anexar Arquivos**
   - Localização: Tela do Diário de Obras, seção de interações
   - Como fazer: Durante o registro de uma interação, utilize a opção de anexar arquivos para incluir imagens ou vídeos relevantes.
   - Resultado esperado: Os arquivos anexados estarão disponíveis para consulta futura dentro da interação.

**Campos e Parâmetros:**

| Campo                     | Tipo       | Obrigatório | Descrição                                               | Exemplo                  |
|---------------------------|------------|-------------|--------------------------------------------------------|--------------------------|
| Data de Início            | Data       | Sim         | Data em que a obra foi iniciada                        | 29/09/2023               |
| Tipo de Interação         | Texto      | Sim         | Nome da interação a ser registrada                     | "Reunião com fornecedores"|
| Descrição da Interação    | Texto      | Sim         | Detalhes sobre a interação registrada                   | "Discussão sobre prazos" |
| Arquivo Anexado           | Arquivo    | Não         | Imagens ou vídeos relacionados à interação             | "foto_progresso.jpg"     |

**Regras de Negócio:**
- O diário é preenchido automaticamente com base nas ações realizadas em outros módulos.
- As interações devem ser registradas em ordem cronológica.
- É permitido anexar arquivos durante o registro de interações.

**Observações Importantes:**
- As informações do diário são atualizadas conforme as ações são realizadas em outros módulos.
- É importante registrar as interações de forma detalhada para facilitar o acompanhamento da obra.
- Verifique se você tem permissão para registrar interações e anexar arquivos.

**Conceitos-Chave:**
- **Diário de Obras**: Registro diário das atividades e interações relacionadas a uma obra.
- **Interação**: Registro de eventos ou atividades que ocorrem durante o andamento da obra.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                | Solução                                           | Prevenção                                      |
|-----------------------------------|-------------------------------|--------------------------------------------------|------------------------------------------------|
| Não consigo registrar uma interação| Permissões insuficientes      | Verifique suas permissões de usuário             | Solicite ao administrador as permissões necessárias |
| Arquivo não anexa                 | Formato de arquivo inválido   | Utilize formatos suportados (ex: .jpg, .png)    | Verifique os formatos aceitos antes de anexar  |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre registre as interações no mesmo dia em que ocorrem para manter a cronologia.
- Utilize descrições claras e detalhadas para facilitar a compreensão futura.
- Anexe arquivos relevantes para complementar as informações registradas.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Registro de Interação**
```
Situação: Reunião com fornecedores sobre materiais.
Ação: 
  • Tipo de Interação: "Reunião com fornecedores"
  • Descrição: "Discussão sobre prazos de entrega e qualidade dos materiais."
Resultado: A interação é registrada e aparece no diário com data e hora.
```

**Exemplo 2: Registro Climático**
```
Situação: Registro das condições climáticas do dia.
Ação: 
  • Data: "29/09/2023"
  • Condição: "Céu limpo, temperatura média de 25°C."
Resultado: As informações climáticas são salvas e associadas ao diário.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** A obra deve estar cadastrada e a data de início definida.
- **Habilita:** O registro de interações e informações climáticas que podem ser consultadas posteriormente.
- **Relacionado a:** Módulos de Ordens de Serviço e Medições, onde as ações são realizadas e impactam o diário.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como registrar uma interação no Diário de Obras?"
- **Com problema:** "Não consigo ver o diário da obra, o que fazer?"
- **Informal:** "Como faço para anotar o que aconteceu hoje na obra?"
- **Por sintoma:** "O que fazer se não consigo anexar arquivos no diário?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Diário de obra", "registro de obra", "anotações diárias", "relatório de atividades"
- "Interação", "registro de eventos", "anotações"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como visualizar o Diário de Obras?
- Como registrar uma interação?
- O que fazer se não consigo anexar arquivos?
- Como registrar informações climáticas?
- O que preciso fazer antes de registrar interações?

---


---


---

## 21. Exportação de Relatórios e Cadastro de Itens no Sistema de Obras

**📋 METADADOS:**
- **ID:** sec_21
- **⏱️ Minutagem:** 50:48 → 53:21
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/BdLq4eBgfxQ?si=Sxmnm__Ai1ReGR0_&t=3048)
- **📦 Módulo:** Gestão de Obras
- **🏷️ Categorias:** Relatório, Cadastro, Operacional
- **🔑 Palavras-chave:** exportar relatório, diário de obras, cadastro de composições, checklist, medições

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como exportar um relatório do diário de obras em formato PDF, incluindo imagens, e como cadastrar itens como composições, insumos e checklist no sistema de gestão de obras.

**Contexto:**
Estamos na interface do sistema de gestão de obras, onde o usuário pode gerenciar informações relacionadas a obras, incluindo a exportação de relatórios e o cadastro de diversos itens necessários para o acompanhamento e execução das obras.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Gestão de Obras > Submenu Relatórios e Cadastros
- Tela/interface específica: Tela de Relatórios e Cadastros de Itens

**Funcionalidade Detalhada:**
A funcionalidade permite ao usuário exportar um relatório do diário de obras em formato PDF, que inclui imagens associadas a cada registro. Além disso, o sistema oferece a opção de cadastrar composições, insumos, etapas, serviços e tipos de unidades, facilitando a organização e o acompanhamento das obras.

### 🔹 Passo a Passo Detalhado:

1. **Exportar Relatório do Diário de Obras**
   - Localização: Tela de Relatórios e Cadastros de Itens
   - Como fazer: Clique no botão **Exportar Relatório** localizado na parte superior da tela.
   - Campos/Opções disponíveis:
     * `Formato`: Selecione **PDF**.
     * `Incluir Imagens`: Marque a opção para incluir imagens no relatório.
   - Resultado esperado: Um arquivo PDF será gerado e baixado, contendo todas as informações do diário de obras, incluindo as imagens associadas.

2. **Gerar Medição e Emitir Contrato**
   - Localização: Tela de Medições e Contratos
   - Como fazer: Clique no botão **Emitir Contrato** ou **Gerar Medição**. Ambas as opções estão disponíveis na mesma interface.
   - Observações importantes: O processo de geração de medição funciona da mesma forma que no acompanhamento da obra.
   - Resultado esperado: O sistema irá gerar o contrato ou a medição conforme solicitado, permitindo o acompanhamento financeiro da obra.

3. **Cadastrar Composições e Insumos**
   - Localização: Tela de Cadastro de Composições
   - Como fazer: Clique no botão **Adicionar Composição** ou **Adicionar Insumo**.
   - Campos/Opções disponíveis:
     * `Nome da Composição`: Campo de texto para inserir o nome da composição.
     * `Descrição`: Campo de texto para descrever a composição.
   - Resultado esperado: A nova composição ou insumo será adicionada ao sistema e estará disponível para uso em orçamentos.

4. **Cadastrar Tipos de Unidade**
   - Localização: Tela de Cadastro de Tipos de Unidade
   - Como fazer: Clique no botão **Adicionar Tipo**.
   - Campos/Opções disponíveis:
     * `Nome do Tipo`: Campo de texto para inserir a nomenclatura do tipo de unidade (ex: apartamento, garagem, sala comercial).
   - Resultado esperado: O tipo de unidade será cadastrado e associado às obras conforme necessário.

5. **Criar Itens de Checklist**
   - Localização: Tela de Checklist
   - Como fazer: Clique no botão **Adicionar Item**.
   - Campos/Opções disponíveis:
     * `Nome do Item`: Campo de texto para inserir a nomenclatura do item do checklist.
   - Resultado esperado: O novo item de checklist será criado e poderá ser associado a serviços durante a execução.

**Campos e Parâmetros:**

| Campo                  | Tipo         | Obrigatório | Descrição                                          | Exemplo                |
|------------------------|--------------|-------------|----------------------------------------------------|------------------------|
| `Formato`              | Dropdown     | Sim         | Seleciona o formato do relatório a ser exportado. | PDF                    |
| `Incluir Imagens`      | Checkbox     | Não         | Opção para incluir imagens no relatório.           | [x] Incluir Imagens    |
| `Nome da Composição`   | Texto        | Sim         | Nome da composição a ser cadastrada.               | Composição A           |
| `Descrição`            | Texto        | Não         | Descrição detalhada da composição.                  | Composição para obra X |
| `Nome do Tipo`        | Texto        | Sim         | Nome do tipo de unidade a ser cadastrado.          | Apartamento            |
| `Nome do Item`        | Texto        | Sim         | Nome do item do checklist a ser criado.            | Verificar segurança     |

**Regras de Negócio:**
- O relatório do diário de obras só pode ser exportado em formato PDF.
- As composições e insumos devem ter um nome único para evitar duplicações.
- Os tipos de unidade devem ser associados corretamente às obras para garantir a categorização correta.

**Observações Importantes:**
- Sempre verifique se as imagens estão corretamente anexadas antes de exportar o relatório.
- Evite cadastrar composições com nomes muito semelhantes para não gerar confusão.
- O checklist deve ser revisado antes da execução do serviço para garantir a conformidade.

**Conceitos-Chave:**
- **Checklist**: Uma lista de verificação que deve ser completada antes da execução de um serviço.
- **Composição**: Conjunto de insumos e serviços que formam uma unidade de medida para orçamentos.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                       | Causa Provável                  | Solução                                           | Prevenção                                     |
|--------------------------------|----------------------------------|--------------------------------------------------|-----------------------------------------------|
| Relatório não é gerado        | Falta de permissões             | Verifique as permissões do usuário na configuração | Configure permissões adequadas antes          |
| Imagens não aparecem no PDF   | Imagens não anexadas corretamente| Revise os registros e anexe as imagens novamente  | Sempre verificar anexos antes da exportação   |
| Erro ao cadastrar composição   | Nome duplicado                  | Escolha um nome diferente para a composição       | Utilize nomes únicos e descritivos            |

**💡 DICAS E BOAS PRÁTICAS:**
- Utilize nomes descritivos para composições e insumos para facilitar a identificação.
- Revise o checklist antes de iniciar os serviços para garantir que todos os itens estão em conformidade.
- Use a opção de incluir imagens no relatório para melhor documentação visual.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Exportação de Relatório**
```
Situação: O usuário deseja exportar o relatório do diário de obras.
Ação: O usuário clica em **Exportar Relatório**, seleciona **PDF** e marca **Incluir Imagens**.
Resultado: Um arquivo PDF é gerado e baixado, contendo todas as informações e imagens do diário de obras.
```

**Exemplo 2: Cadastro de Composição**
```
Situação: O usuário precisa cadastrar uma nova composição para o orçamento.
Ação: O usuário clica em **Adicionar Composição**, insere "Piso Cerâmico" no campo **Nome da Composição** e "Piso cerâmico para áreas internas" no campo **Descrição**.
Resultado: A composição "Piso Cerâmico" é cadastrada e disponível para uso em orçamentos.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O usuário deve ter permissões adequadas para exportar relatórios e cadastrar itens.
- **Habilita:** A exportação de relatórios permite a documentação formal das obras.
- **Relacionado a:** Funcionalidades de acompanhamento de obras e gestão de contratos.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como exportar um relatório do diário de obras?"
- **Com problema:** "Não consigo gerar o relatório, o que fazer?"
- **Informal:** "Como faço para baixar o relatório da obra?"
- **Por sintoma:** "Por que as imagens não aparecem no relatório exportado?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "baixar relatório", "gerar PDF", "exportar dados", "cadastrar itens", "criar checklist"
- "documentação de obra", "relatório de progresso", "itens de verificação"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como exportar um relatório do diário de obras?
- O que fazer se o relatório não for gerado?
- Como cadastrar uma nova composição no sistema?
- O que fazer se as imagens não aparecerem no relatório?
- Quais são os pré-requisitos para cadastrar itens no sistema?

---


---


---

## 22. Registro de Treinamento do Módulo de Engenharia

**📋 METADADOS:**
- **ID:** sec_22
- **⏱️ Minutagem:** 53:19 → 53:32
- **⏲️ Duração:** 12s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/BdLq4eBgfxQ?si=Sxmnm__Ai1ReGR0_&t=3199)
- **📦 Módulo:** Engenharia
- **🏷️ Categorias:** Treinamento, Registro, Comunicação
- **🔑 Palavras-chave:** treinamento, módulo, engenharia, registro, COPER, dúvidas

> **🔍 RESUMO EXECUTIVO:** Esta seção aborda o processo de registro de informações relacionadas ao treinamento do módulo de engenharia e fornece um ponto de contato para esclarecimento de dúvidas.

**Contexto:**
Estamos no final do treinamento do módulo de engenharia, onde é importante garantir que todos os participantes tenham suas dúvidas esclarecidas e que o registro do treinamento seja feito de forma adequada.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Engenharia > Treinamento
- Tela/interface específica: Tela de Conclusão do Treinamento

**Funcionalidade Detalhada:**
O registro do treinamento do módulo de engenharia é uma funcionalidade que permite aos participantes documentar a conclusão do treinamento e garantir que qualquer dúvida possa ser direcionada ao COPER, que é o ponto de contato para suporte. Esta funcionalidade é crucial para manter a comunicação clara e para que os participantes saibam onde buscar ajuda.

### 🔹 Passo a Passo Detalhado:

1. **Finalizar o Treinamento**
   - Localização: Tela de Conclusão do Treinamento
   - Como fazer: Após assistir a todas as partes do treinamento, clique no botão **"Finalizar Treinamento"**.
   - Campos/Opções disponíveis:
     * `Botão "Finalizar Treinamento"`: Confirma a conclusão do módulo.
   - Resultado esperado: Uma mensagem de confirmação aparecerá, indicando que o treinamento foi registrado com sucesso.

2. **Registrar Dúvidas**
   - Localização: Tela de Conclusão do Treinamento
   - Como fazer: Após finalizar o treinamento, se houver dúvidas, clique no link **"Entrar em Contato com o COPER"**.
   - Observações importantes: Certifique-se de que suas dúvidas estejam claras e específicas para facilitar a resposta.
   - Resultado esperado: Uma nova janela ou formulário será aberto para que você possa enviar suas perguntas diretamente ao COPER.

**Campos e Parâmetros:**

| Campo | Tipo | Obrigatório | Descrição | Exemplo |
|-------|------|-------------|-----------|---------|
| Botão "Finalizar Treinamento" | Botão | Sim | Confirma a conclusão do treinamento do módulo de engenharia. | N/A |
| Link "Entrar em Contato com o COPER" | Link | Sim | Direciona o usuário para o formulário de contato do COPER. | N/A |

**Regras de Negócio:**
- O registro do treinamento só pode ser feito após a visualização completa do conteúdo do módulo.
- As dúvidas devem ser enviadas através do canal apropriado (COPER) para garantir que sejam tratadas adequadamente.

**Observações Importantes:**
- É importante registrar o treinamento para que haja um histórico de participação.
- Evite enviar dúvidas que já foram abordadas durante o treinamento para otimizar o tempo de resposta do COPER.

**Conceitos-Chave:**
- **COPER**: Centro de Operações e Respostas, responsável por atender dúvidas e solicitações dos usuários.
- **Treinamento**: Processo de aprendizado sobre o módulo de engenharia, que deve ser registrado para fins de controle.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema | Causa Provável | Solução | Prevenção |
|----------|---------------|---------|-----------|
| Não consigo finalizar o treinamento | O conteúdo não foi assistido completamente | Revise o conteúdo e tente novamente | Certifique-se de assistir a todas as partes do treinamento antes de finalizar |
| Link do COPER não abre | Problema de conexão ou link quebrado | Verifique sua conexão com a internet ou tente acessar o link em outro navegador | Mantenha seu navegador atualizado e verifique a conexão antes de acessar |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre anote suas dúvidas durante o treinamento para não esquecê-las ao entrar em contato com o COPER.
- Utilize um navegador compatível para evitar problemas de carregamento.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Registro de Conclusão de Treinamento**
```
Situação: Um usuário completou todas as partes do treinamento de engenharia.
Ação: O usuário clica no botão "Finalizar Treinamento".
Resultado: O sistema registra a conclusão e exibe uma mensagem de confirmação.
```

**Exemplo 2: Envio de Dúvidas ao COPER**
```
Situação: Um usuário tem dúvidas sobre um tópico específico abordado no treinamento.
Ação: O usuário clica no link "Entrar em Contato com o COPER" e preenche o formulário com suas perguntas.
Resultado: As dúvidas são enviadas para o COPER, que responderá em breve.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O usuário deve ter completado todas as partes do treinamento para registrar a conclusão.
- **Habilita:** O registro do treinamento permite que o usuário tenha acesso a suporte adicional.
- **Relacionado a:** Outros módulos de treinamento que podem ter um processo de registro semelhante.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como registrar a conclusão do treinamento do módulo de engenharia?"
- **Com problema:** "Não consigo finalizar o treinamento, o que fazer?"
- **Informal:** "Como eu marco que terminei o treinamento?"
- **Por sintoma:** "O que fazer se o botão de finalizar não funcionar?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Registrar treinamento", "finalizar módulo", "completar curso", "encerrar treinamento"
- "COPER" como sinônimo de suporte ou ajuda

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como faço para registrar que terminei o treinamento?
- O que fazer se não conseguir finalizar o treinamento?
- Como posso entrar em contato com o COPER?
- O que fazer se o link do COPER não abrir?
- O que preciso fazer antes de finalizar o treinamento?

---


---




---


## 🎬 DADOS DE TIMESTAMPS (Para Sistema RAG)


[VIDEO_TIMESTAMPS_DATA]

{
  "Passo a passo - Módulo de Engenharia": [
    {
      "start": "00:03",
      "end": "02:37",
      "line": "Nesse vídeo eu vou explicar as funcionalidades do módulo de engenharia. Primeiro, o cadastro da obra"
    },
    {
      "start": "02:34",
      "end": "05:08",
      "line": "da obra através das pastas, tá? Então é só criar aqui pasta, o nome e logo em seguida adicionar os d"
    },
    {
      "start": "05:05",
      "end": "07:39",
      "line": "Agora, a parte de orçamentos, como que vai gerar um orçamento aqui no sistema? Clique em mais orçame"
    },
    {
      "start": "07:36",
      "end": "10:12",
      "line": "organização de vocês. Mas lembrando, ah, não tem a etapa, a subetapa cadastrada aqui, não tem proble"
    },
    {
      "start": "10:09",
      "end": "12:34",
      "line": "eh executar esse serviço. Checklist inicial e checklist final. Não é obrigatório preencher, mas é eh"
    },
    {
      "start": "12:40",
      "end": "15:09",
      "line": "Então, coloca o nome, pode ser o mesmo nome do serviço, tá? caso vocês coloquem conforme vocês eh ac"
    },
    {
      "start": "15:23",
      "end": "17:55",
      "line": "OK, cadastrei a composição, já está associada ao serviço. Agora aqui no orçamento eu coloco a quanti"
    },
    {
      "start": "17:54",
      "end": "20:29",
      "line": "estamos lidando com duas unidades de medida. A unidade de medida do produto e a unidade de medida da"
    },
    {
      "start": "20:26",
      "end": "23:01",
      "line": "medindo aí lá no no financeiro, eu vou mostrar certinho como que vai ficar. Aí precisa colocar uma d"
    },
    {
      "start": "22:58",
      "end": "25:32",
      "line": "se eu precisar fazer alguma alteração, ah, adicionar um novo serviço, editar algum valor, eu vou sem"
    },
    {
      "start": "25:37",
      "end": "28:09",
      "line": "execução. Então, a forma de execução, como que e vai ser executada esse serviços? É por o por mão de"
    },
    {
      "start": "28:08",
      "end": "30:43",
      "line": "O acompanhamento vai trazer exatamente a mesma estrutura que estava lá no meu planejamento. Então el"
    },
    {
      "start": "30:39",
      "end": "33:11",
      "line": "Como eh a alvenaria era por bloco, então aparece aqui, ó, o mesmo serviço alvenaria, só que blocos d"
    },
    {
      "start": "33:11",
      "end": "35:43",
      "line": "Enquanto isso aqui no cronograma, ó, eu já consigo comparativo. Então, OK, meu planejado era iniciar"
    },
    {
      "start": "35:43",
      "end": "38:16",
      "line": "Então aqui o sistema ele já mostra, ó, em qual serviço essa esse insumo está alocado e o planejado, "
    },
    {
      "start": "38:13",
      "end": "40:46",
      "line": "material limpeza de terreno, né? Eu vou comprar os materiais de fato que eu preciso para executar aq"
    },
    {
      "start": "40:44",
      "end": "43:16",
      "line": "apenas 100. Então eu coloco aqui a quantidade, aí o sistema vai multiplicar, pegar a quantidade, mul"
    },
    {
      "start": "43:15",
      "end": "45:48",
      "line": "Então, essa é a primeira medição que eu estou realizando, mas se eu já tivesse feito medições para e"
    },
    {
      "start": "45:45",
      "end": "48:14",
      "line": "pagar, tá? Agora, para liberar a receber, ou seja, para minha empresa receber, aí eu venho nessa sub"
    },
    {
      "start": "48:17",
      "end": "50:50",
      "line": "Diário de obras. Então, o Diário de Obras, o nome já diz, eh por dia, né? Então, lembre que quando e"
    },
    {
      "start": "50:48",
      "end": "53:21",
      "line": "arquivos, vão ficar todos misturados, né? Agora, se vocês colocarem diretamente aqui dentro de cada "
    },
    {
      "start": "53:19",
      "end": "53:32",
      "line": "conseguirem deixar registrado, tá pessoal? E esse foi o treinamento do módulo de engenharia. Qualque"
    }
  ]
}

[/VIDEO_TIMESTAMPS_DATA]
