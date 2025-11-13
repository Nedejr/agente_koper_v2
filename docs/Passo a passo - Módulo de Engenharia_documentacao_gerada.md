# 📚 Documentação: Passo a passo - Módulo de Engenharia

**🎥 Vídeo Original:** https://www.youtube.com/watch?v=BdLq4eBgfxQ&list=PLrsGJiMcdclnlo9exwzyqZC_e09rt5om8&index=4

**📊 Total de Seções:** 22

---

---

## 1. Cadastro da Obra no Módulo de Engenharia

**📋 METADADOS:**
- **ID:** sec_1
- **⏱️ Minutagem:** 00:03 → 02:37
- **⏲️ Duração:** 154s
- **🎬 Link:** [Assistir este trecho](https://www.youtube.com/watch?v=BdLq4eBgfxQ&list=PLrsGJiMcdclnlo9exwzyqZC_e09rt5om8&index=4&t=3)
- **📦 Módulo:** Engenharia
- **🏷️ Categorias:** Cadastro, Configuração, Operacional
- **🔑 Palavras-chave:** obra, cadastro, tipo, campos, dados

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como cadastrar uma nova obra no sistema, detalhando os campos obrigatórios e opcionais, além de fornecer orientações sobre a configuração e estrutura da obra.

**Contexto:**
Estamos no módulo de engenharia do sistema, onde o usuário pode cadastrar novas obras, definindo suas características e informações relevantes para o gerenciamento.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Engenharia > Cadastro de Obras
- Tela/interface específica: Tela de Cadastro de Obras

**Funcionalidade Detalhada:**

O cadastro da obra permite que os usuários registrem informações essenciais sobre uma nova obra, como o tipo de obra, dados da empresa ou do cliente, e a estrutura da obra. Essa funcionalidade é crucial para o gerenciamento eficaz de projetos de construção, permitindo que a empresa tenha um controle detalhado sobre cada obra em andamento.

### 🔹 Passo a Passo Detalhado:

1. **Selecionar a Versão de Cadastro**
   - Localização: Tela de Cadastro de Obras
   - Como fazer: Clique na opção **"Versão Tradicional"** para iniciar o cadastro.
   - Resultado esperado: A interface de cadastro se ajusta para permitir o preenchimento dos dados da obra.

2. **Definir o Tipo da Obra**
   - Localização: Campo **"Tipo da Obra"**
   - Como fazer: Selecione uma das opções disponíveis:
     * **Obra Própria**: obra da empresa
     * **Obra para Terceiro**: obra que a empresa está realizando para um cliente
   - Resultado esperado: Dependendo da seleção, novos campos para preenchimento são exibidos.

3. **Preencher Campos Obrigatórios**
   - Localização: Campos subsequentes que aparecem após a seleção do tipo de obra
   - Como fazer: Preencha os campos obrigatórios, que são identificados por um asterisco (*). Os campos incluem:
     * **Nome da Obra**: Nome que identifica a obra
     * **Data de Início**: Data em que a obra começará
   - Resultado esperado: Os campos obrigatórios são preenchidos corretamente.

4. **Adicionar Novo Tipo de Obra (se necessário)**
   - Localização: Botão **"Mais Adicionar"**
   - Como fazer: Clique no botão para cadastrar um novo tipo de obra, caso o desejado não esteja na lista pré-cadastrada.
   - Resultado esperado: Um novo campo é exibido para o cadastro do tipo de obra.

5. **Informar Status da Obra**
   - Localização: Campo **"Obra Finalizada"**
   - Como fazer: Selecione se a obra já está finalizada ou não.
   - Resultado esperado: O status da obra é atualizado conforme a seleção.

6. **Configurar Identificação das Etapas de Compra**
   - Localização: Campo **"Dados da Empresa ou Dados do Cliente"**
   - Como fazer: Escolha se as ordens de compra geradas para a obra devem conter os dados da empresa ou do cliente.
   - Resultado esperado: A configuração é salva conforme a seleção.

7. **Montar Estrutura da Obra**
   - Localização: Campos de estrutura da obra
   - Como fazer: Preencha as informações sobre a estrutura da obra, como:
     * **Possui Blocos?**: Se sim, selecione e informe a quantidade de blocos.
     * **Possui Andares?**: Se sim, selecione e informe o número de andares.
     * **Unidades por Andar**: Informe quantas unidades existem por andar (ex: 3 unidades por andar).
   - Resultado esperado: A estrutura da obra é configurada de acordo com as informações fornecidas.

8. **Preencher Endereço da Obra**
   - Localização: Campo **"Endereço da Obra"**
   - Como fazer: Insira o endereço completo onde a obra será realizada.
   - Resultado esperado: O endereço da obra é salvo corretamente.

9. **Salvar Cadastro da Obra**
   - Localização: Botão **"Salvar"**
   - Como fazer: Clique no botão para finalizar o cadastro da obra.
   - Resultado esperado: A obra é cadastrada no sistema e uma confirmação é exibida.

10. **Adicionar Imagem e Organizar Documentos**
    - Localização: Opções para adicionar imagem e documentos
    - Como fazer: Utilize as opções disponíveis para carregar uma imagem da obra e organizar documentos relevantes.
    - Resultado esperado: A imagem e os documentos são associados à obra cadastrada.

**Campos e Parâmetros:**

| Campo                       | Tipo        | Obrigatório | Descrição                                           | Exemplo                  |
|-----------------------------|-------------|-------------|----------------------------------------------------|--------------------------|
| Nome da Obra                | Texto       | Sim         | Nome que identifica a obra                          | "Construção do Prédio A" |
| Data de Início              | Data        | Sim         | Data em que a obra começará                        | "01/01/2024"             |
| Tipo da Obra                | Dropdown    | Sim         | Tipo de obra (Própria ou para Terceiro)           | "Obra Própria"           |
| Status da Obra              | Dropdown    | Não         | Indica se a obra está finalizada ou não            | "Não"                    |
| Dados da Empresa/Cliente     | Dropdown    | Sim         | Identificação para ordens de compra                | "Dados da Empresa"       |
| Possui Blocos               | Checkbox    | Não         | Indica se a obra possui blocos                      | "Sim"                    |
| Quantidade de Blocos        | Número      | Não         | Número de blocos na obra                            | "5"                      |
| Possui Andares              | Checkbox    | Não         | Indica se a obra possui andares                     | "Sim"                    |
| Número de Andares           | Número      | Não         | Total de andares na obra                            | "3"                      |
| Unidades por Andar          | Número      | Não         | Quantidade de unidades por andar                    | "3"                      |
| Endereço da Obra            | Texto       | Sim         | Endereço completo da obra                           | "Rua Exemplo, 123"       |

**Regras de Negócio:**
- Campos obrigatórios são identificados com um asterisco (*).
- O tipo da obra deve ser selecionado antes de preencher outros campos.
- A configuração de dados da empresa ou cliente deve ser definida para a geração de ordens de compra.

**Observações Importantes:**
- É recomendado utilizar a **versão tradicional** para um cadastro mais fácil e rápido.
- Erros comuns incluem não preencher campos obrigatórios, o que impede o salvamento do cadastro.
- Certifique-se de que todas as informações estão corretas antes de salvar.

**Conceitos-Chave:**
- **Cadastro de Obra**: Processo de registrar informações sobre uma nova obra no sistema.
- **Tipo de Obra**: Classificação que determina se a obra é própria ou para terceiros.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como cadastrar uma nova obra no sistema?
- Quais campos são obrigatórios no cadastro da obra?
- Como adicionar um novo tipo de obra se ele não estiver na lista?

---


---


---

## 2. Cadastro de Obras e Estruturas

**📋 METADADOS:**
- **ID:** sec_2
- **⏱️ Minutagem:** 02:34 → 05:08
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://www.youtube.com/watch?v=BdLq4eBgfxQ&list=PLrsGJiMcdclnlo9exwzyqZC_e09rt5om8&index=4&t=154)
- **📦 Módulo:** Cadastro de Obras
- **🏷️ Categorias:** Configuração, Cadastro, Administração
- **🔑 Palavras-chave:** obra, pasta, bloco, unidade, andar, editar, anexar, valor

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como cadastrar obras e suas respectivas estruturas no sistema, incluindo a criação de pastas, blocos, unidades e andares, além de como editar informações e anexar documentos relevantes.

**Contexto:**
Estamos no módulo de Cadastro de Obras, onde o usuário pode organizar e estruturar informações sobre projetos de construção. O objetivo desta seção é guiar o usuário no processo de cadastro e edição de obras, garantindo que todas as informações necessárias sejam registradas corretamente.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Cadastro de Obras > Tela de Cadastro de Obras
- Tela/interface específica: Tela de Cadastro de Obras

**Funcionalidade Detalhada:**
A funcionalidade de cadastro de obras permite que o usuário crie pastas para organizar documentos relacionados a cada obra. O sistema também possibilita a adição de blocos, unidades e andares, além da edição de informações como áreas e nomes das unidades. O usuário pode anexar arquivos a cada unidade e definir valores para unidades vendáveis.

### 🔹 Passo a Passo Detalhado:

1. **Criar Pasta**
   - Localização: Tela de Cadastro de Obras
   - Como fazer: Clique no botão **Criar Pasta**. Insira o nome da pasta no campo designado e clique em **Adicionar**.
   - Campos/Opções disponíveis:
     * `Nome da Pasta`: Campo de texto onde o usuário insere o nome desejado para a pasta.
   - Resultado esperado: A pasta é criada e aparece na lista de pastas disponíveis.

2. **Adicionar Estruturas**
   - Localização: Tela de Cadastro de Obras, seção de estruturas
   - Como fazer: Clique no botão **Mais Estrutura**. Uma janela de opções será exibida.
   - Observações importantes: Se você precisar adicionar mais blocos, andares ou unidades, selecione a opção correspondente:
     * **Bloco**: Para adicionar um novo bloco.
     * **Nível**: Para adicionar um novo andar.
     * **Unidade**: Para adicionar uma nova unidade.
   - Resultado esperado: A estrutura selecionada é adicionada à obra.

3. **Editar Áreas das Unidades**
   - Localização: Tela de Cadastro de Obras, seção de unidades
   - Como fazer: Selecione as unidades que deseja editar. Insira a área privativa e a área comum nos campos correspondentes.
   - Campos/Opções disponíveis:
     * `Área Privativa`: Campo numérico onde o usuário insere a área privativa em m².
     * `Área Comum`: Campo numérico onde o usuário insere a área comum em m².
   - Resultado esperado: As áreas das unidades selecionadas são atualizadas simultaneamente.

4. **Editar Nomes das Unidades**
   - Localização: Tela de Cadastro de Obras, seção de unidades
   - Como fazer: Clique no botão **Editar Nomes**. Insira o novo nome para a unidade no campo correspondente e clique em **Concluir**.
   - Resultado esperado: O nome da unidade é atualizado conforme o novo valor inserido.

5. **Anexar Arquivos a Unidades**
   - Localização: Dentro da tela de cada unidade
   - Como fazer: Acesse a unidade desejada e utilize a opção de **Anexar Arquivo** para selecionar e carregar documentos relevantes.
   - Resultado esperado: O arquivo é anexado à unidade e fica disponível para consulta.

6. **Definir Valor da Unidade**
   - Localização: Dentro da tela da unidade
   - Como fazer: Se a unidade for vendável, selecione a opção correspondente e insira o valor da planta no campo designado.
   - Campos/Opções disponíveis:
     * `Valor da Unidade`: Campo numérico onde o usuário insere o valor da unidade.
   - Resultado esperado: O valor da unidade é salvo e associado à unidade cadastrada.

7. **Adicionar Vagas de Garagem e Subunidades**
   - Localização: Dentro da tela da unidade
   - Como fazer: Utilize as opções para adicionar vagas de garagem e subunidades (cômodos) como quartos, salas e banheiros.
   - Campos/Opções disponíveis:
     * `Nome da Subunidade`: Campo de texto para o nome do cômodo.
     * `Área da Subunidade`: Campo numérico para a área do cômodo em m².
   - Resultado esperado: As vagas de garagem e subunidades são adicionadas à unidade.

8. **Lançar Receitas e Despesas**
   - Localização: Módulo Financeiro
   - Como fazer: Após o cadastro da obra, acesse o módulo financeiro para registrar receitas e despesas relacionadas à obra.
   - Resultado esperado: As receitas e despesas são registradas e associadas à obra cadastrada.

**Campos e Parâmetros:**

| Campo                  | Tipo         | Obrigatório | Descrição                                               | Exemplo         |
|------------------------|--------------|-------------|---------------------------------------------------------|------------------|
| Nome da Pasta          | Texto        | Sim         | Nome da pasta para organizar documentos da obra        | "Pasta da Obra"  |
| Área Privativa         | Numérico     | Sim         | Área privativa da unidade em m²                         | 50               |
| Área Comum             | Numérico     | Sim         | Área comum da unidade em m²                             | 20               |
| Valor da Unidade       | Numérico     | Sim         | Valor da planta da unidade                               | 200000           |
| Nome da Subunidade     | Texto        | Não         | Nome do cômodo (subunidade)                            | "Quarto"         |
| Área da Subunidade     | Numérico     | Não         | Área do cômodo em m²                                   | 15               |

**Regras de Negócio:**
- A criação de pastas é obrigatória para organizar documentos.
- As áreas das unidades podem ser editadas em massa.
- O valor da unidade deve ser inserido se a unidade for vendável.
- Subunidades são opcionais e podem ser adicionadas conforme necessidade.

**Observações Importantes:**
- Lembre-se de revisar as informações antes de concluir o cadastro.
- Evite duplicar nomes de unidades para manter a organização.
- Verifique se todos os campos obrigatórios estão preenchidos antes de salvar.

**Conceitos-Chave:**
- **Pasta**: Estrutura de organização para documentos relacionados a uma obra.
- **Unidade**: Parte da obra que pode ser vendida, como um apartamento ou sala.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como criar uma pasta para organizar documentos de uma obra?
- O que fazer se eu precisar adicionar mais blocos ou unidades?
- Como posso editar as áreas e nomes das unidades cadastradas?

---


---


---

## 3. Geração de Orçamentos no Sistema

**📋 METADADOS:**
- **ID:** sec_3
- **⏱️ Minutagem:** 05:05 → 07:39
- **⏲️ Duração:** 154s
- **🎬 Link:** [Assistir este trecho](https://www.youtube.com/watch?v=BdLq4eBgfxQ&list=PLrsGJiMcdclnlo9exwzyqZC_e09rt5om8&index=4&t=305)
- **📦 Módulo:** Orçamentos
- **🏷️ Categorias:** Orçamentação, Cadastro, Operacional
- **🔑 Palavras-chave:** orçamento, BDI, composições, serviços, obra, cliente

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como gerar um orçamento no sistema, orientando sobre a escolha do tipo de orçamento e detalhando os campos necessários para a criação do orçamento, incluindo opções de arredondamento e seleção de composições.

**Contexto:**
Estamos na funcionalidade de geração de orçamentos dentro do módulo de Orçamentos do sistema. O objetivo desta seção é guiar o usuário na criação de um orçamento, explicando cada passo e as opções disponíveis.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Orçamentos > Geração de Orçamento
- Tela/interface específica: Tela de Geração de Orçamento

**Funcionalidade Detalhada:**
A funcionalidade de geração de orçamentos permite que o usuário crie orçamentos para serviços a serem executados. O sistema oferece a opção de selecionar o tipo de orçamento, sendo recomendado que usuários que executam serviços optem por "orçamentos por serviços". Isso facilita a criação do orçamento, evitando a necessidade de vincular serviços a composições e insumos, que é mais adequado para orçamentistas.

### 🔹 Passo a Passo Detalhado:

1. **Clique em "Mais Orçamento"**
   - Localização: Botão "Mais Orçamento" na tela de Geração de Orçamento.
   - Como fazer: Clique no botão **"Mais Orçamento"** para iniciar o processo de criação de um novo orçamento.
   - Resultado esperado: O sistema abrirá um formulário para a inserção dos dados do novo orçamento.

2. **Selecione o Tipo de Orçamento**
   - Localização: Dropdown de seleção de tipo de orçamento.
   - Como fazer: No campo de seleção, escolha a opção **"Orçamentos por Serviços"**. Esta opção é recomendada para quem executa serviços.
   - Observações importantes: A escolha do tipo de orçamento é crucial, pois determina como o orçamento será estruturado.
   - Resultado esperado: O sistema ajustará os campos disponíveis para o tipo de orçamento selecionado.

3. **Preencha o Nome do Orçamento**
   - Localização: Campo de texto para o nome do orçamento.
   - Como fazer: Digite um nome descritivo para o orçamento no campo **"Nome do Orçamento"**.
   - Resultado esperado: O nome do orçamento será salvo e exibido na lista de orçamentos.

4. **Insira o Valor do BDI**
   - Localização: Campo de texto para o percentual do BDI.
   - Como fazer: No campo **"Valor do BDI"**, insira o percentual que a empresa aplica. Este campo é opcional, mas recomendado.
   - Resultado esperado: O percentual do BDI será associado ao orçamento.

5. **Preencha a Obra e o Cliente (Opcional)**
   - Localização: Campos de texto para obra e cliente.
   - Como fazer: Os campos **"Obra"** e **"Cliente"** podem ser preenchidos, mas não são obrigatórios neste momento.
   - Observações importantes: É comum que orçamentos sejam feitos para possíveis clientes, sem uma obra definida.
   - Resultado esperado: Caso preenchidos, as informações de obra e cliente serão salvas no orçamento.

6. **Escolha a Opção de Arredondamento**
   - Localização: Opções de arredondamento.
   - Como fazer: Selecione entre **"Não Truncar os Valores Unitários"** ou **"Truncar os Valores Unitários"**.
     - **Não Truncar**: Mantém as casas decimais originais.
     - **Truncar**: Desconsidera as casas decimais no valor total do orçamento.
   - Resultado esperado: O sistema aplicará a opção de arredondamento escolhida ao calcular o orçamento.

7. **Selecione a Base de Composições**
   - Localização: Dropdown para seleção da base de composições.
   - Como fazer: Escolha entre a **"Base da SINAP"** ou a **"Base Própria"** da empresa.
   - Observações importantes: A base da SINAP é padrão, mas a base própria pode ser utilizada conforme a necessidade.
   - Resultado esperado: O sistema ajustará as composições disponíveis com base na seleção feita.

8. **Escolha a Referência e o Estado**
   - Localização: Campos para referência e estado.
   - Como fazer: Preencha os campos **"Referência"** e **"Estado"** conforme necessário.
   - Resultado esperado: O sistema atualizará as composições disponíveis com base na referência e estado selecionados.

9. **Visualização das Etapas e Subetapas**
   - Localização: Área de visualização de etapas e subetapas.
   - Como fazer: O sistema mostrará todas as etapas e subetapas já cadastradas.
   - Resultado esperado: O usuário poderá visualizar e selecionar as etapas e subetapas para o orçamento.

**Campos e Parâmetros:**

| Campo                     | Tipo          | Obrigatório | Descrição                                                                 | Exemplo              |
|---------------------------|---------------|-------------|---------------------------------------------------------------------------|----------------------|
| Nome do Orçamento         | Texto         | Sim         | Nome descritivo do orçamento.                                            | "Orçamento 2023"     |
| Valor do BDI              | Percentual    | Não         | Percentual do BDI aplicado ao orçamento.                                 | "15%"                |
| Obra                      | Texto         | Não         | Nome da obra associada ao orçamento.                                     | "Construção A"       |
| Cliente                   | Texto         | Não         | Nome do cliente associado ao orçamento.                                   | "Cliente X"          |
| Arredondamento            | Opção         | Sim         | Opção de arredondamento dos valores unitários.                           | "Truncar" / "Não Truncar" |
| Base de Composições       | Dropdown      | Sim         | Seleção da base de composições a ser utilizada.                          | "SINAP" / "Própria"  |
| Referência                | Texto         | Sim         | Referência da composição selecionada.                                     | "Ref123"             |
| Estado                    | Texto         | Sim         | Estado relacionado à referência da composição.                            | "SP"                 |

**Regras de Negócio:**
- O campo **"Nome do Orçamento"** é obrigatório e deve ser preenchido para salvar o orçamento.
- O percentual do BDI é opcional, mas se fornecido, será aplicado ao cálculo do orçamento.
- A obra e o cliente não são obrigatórios, permitindo a criação de orçamentos para possíveis clientes.
- O sistema permite a escolha entre a base da SINAP e a base própria da empresa, com a SINAP como padrão.

**Observações Importantes:**
- É recomendado que usuários que executam serviços escolham a opção de **"Orçamentos por Serviços"** para facilitar a criação do orçamento.
- Evite deixar campos obrigatórios em branco, pois isso pode impedir a criação do orçamento.
- Verifique se a base de composições está atualizada antes de iniciar a geração do orçamento.

**Conceitos-Chave:**
- **BDI (Benefício e Despesas Indiretas)**: Percentual aplicado sobre o custo do orçamento para cobrir despesas indiretas e garantir lucro.
- **Base de Composições**: Conjunto de composições de custos que podem ser utilizadas para a elaboração de orçamentos.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso gerar um orçamento no sistema?
- Quais campos são obrigatórios para a criação de um orçamento?
- O que é BDI e como ele afeta meu orçamento?

---


---


---

## 4. Cadastro de Etapas e Subetapas no Orçamento

**📋 METADADOS:**
- **ID:** sec_4
- **⏱️ Minutagem:** 07:36 → 10:12
- **⏲️ Duração:** 155s
- **🎬 Link:** [Assistir este trecho](https://www.youtube.com/watch?v=BdLq4eBgfxQ&list=PLrsGJiMcdclnlo9exwzyqZC_e09rt5om8&index=4&t=456)
- **📦 Módulo:** Orçamento
- **🏷️ Categorias:** Configuração, Cadastro, Orçamento
- **🔑 Palavras-chave:** etapa, subetapa, cadastro, serviço, orçamento

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como cadastrar etapas e subetapas no sistema de orçamento, detalhando a importância das etapas e a flexibilidade no uso das subetapas, além de como adicionar serviços relacionados.

**Contexto:**
Estamos na interface de cadastro de orçamentos, onde o usuário pode organizar a estrutura da obra através de etapas e subetapas. O objetivo é permitir que o usuário crie uma estrutura clara e organizada para o orçamento, facilitando a gestão dos serviços.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Orçamento > Tela de Cadastro de Orçamento
- Tela/interface específica: Tela de Cadastro de Etapas e Subetapas

**Funcionalidade Detalhada:**
A funcionalidade permite que o usuário cadastre etapas e subetapas que compõem a estrutura do orçamento. As etapas são obrigatórias, enquanto as subetapas são opcionais e servem apenas como uma especificação adicional. O usuário pode adicionar novas etapas e subetapas conforme necessário, além de cadastrar serviços que pertencem a cada etapa.

### 🔹 Passo a Passo Detalhado:

1. **Selecionar uma Etapa**
   - Localização: Tela de Cadastro de Etapas e Subetapas
   - Como fazer: O usuário deve clicar na lista de etapas disponíveis e selecionar uma etapa existente. Caso a etapa desejada não esteja cadastrada, o usuário pode clicar no botão **"Mais"** para adicionar uma nova etapa.
   - Campos/Opções disponíveis:
     * `Etapa`: Nome da etapa selecionada.
   - Resultado esperado: A etapa selecionada é exibida na tela, permitindo que o usuário adicione subetapas ou serviços.

2. **Adicionar uma Subetapa (Opcional)**
   - Localização: Após selecionar uma etapa, o usuário deve procurar a opção para adicionar subetapas.
   - Como fazer: O usuário deve clicar no botão **"Mais"** ao lado da opção de subetapas e inserir a nomenclatura da subetapa desejada.
   - Observações importantes: As subetapas são opcionais e não são obrigatórias para o cadastro do orçamento.
   - Resultado esperado: A subetapa é cadastrada e associada à etapa selecionada.

3. **Adicionar um Serviço à Etapa**
   - Localização: Ao lado da etapa selecionada, há um ícone de três pontinhos (⋮).
   - Como fazer: O usuário deve clicar nos três pontinhos e selecionar a opção **"Adicionar Serviço"**. Em seguida, deve inserir o nome do serviço desejado.
   - Campos/Opções disponíveis:
     * `Nome do Serviço`: Nome que identifica o serviço.
     * `Unidade de Medida`: Como o serviço é medido (ex: metro quadrado, metro cúbico, diária).
     * `Categoria`: Categoria à qual o serviço pertence (ex: acabamento).
     * `Clima`: Se o clima afeta a execução do serviço (opção de seleção).
     * `Descrição`: Campo opcional para orientações sobre o serviço.
   - Resultado esperado: O serviço é adicionado à etapa selecionada.

4. **Cadastrar um Novo Serviço**
   - Localização: Na tela de cadastro de serviços, ao clicar em **"Mais"**.
   - Como fazer: O usuário deve clicar no botão **"Mais"** para abrir o formulário de cadastro de serviço e preencher os campos necessários.
   - Observações importantes: É necessário preencher todos os campos obrigatórios para que o serviço seja salvo corretamente.
   - Resultado esperado: O novo serviço é cadastrado e aparece na lista de serviços da etapa.

**Campos e Parâmetros:**

| Campo                | Tipo          | Obrigatório | Descrição                                               | Exemplo               |
|----------------------|---------------|-------------|---------------------------------------------------------|-----------------------|
| Etapa                | Texto         | Sim         | Nome da etapa cadastrada.                               | Canteiro de Obras     |
| Subetapa             | Texto         | Não         | Nome da subetapa cadastrada.                            | Preparação do Terreno |
| Nome do Serviço      | Texto         | Sim         | Nome que identifica o serviço.                          | Pintura               |
| Unidade de Medida    | Dropdown      | Sim         | Como o serviço é medido (ex: m², m³, diária).         | m²                    |
| Categoria            | Dropdown      | Sim         | Categoria à qual o serviço pertence.                    | Acabamento            |
| Clima                | Checkbox      | Não         | Indica se o clima afeta a execução do serviço.         | [ ] Sim               |
| Descrição            | Texto         | Não         | Orientações sobre a execução do serviço.                | Usar tinta acrílica   |

**Regras de Negócio:**
- As etapas são obrigatórias para o cadastro do orçamento.
- As subetapas são opcionais e não agregam valor ao orçamento.
- Os serviços devem ser cadastrados com nome, unidade de medida e categoria para serem válidos.

**Observações Importantes:**
- Caso não tenha a etapa ou subetapa cadastrada, o usuário pode clicar em **"Mais"** para adicionar.
- É possível trabalhar apenas com etapas e serviços, sem a necessidade de subetapas.
- Erros comuns incluem não preencher os campos obrigatórios ao cadastrar serviços.

**Conceitos-Chave:**
- **Etapa**: Uma fase ou parte do projeto que é obrigatória para a estrutura do orçamento.
- **Subetapa**: Uma especificação adicional de uma etapa, que é opcional.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso cadastrar uma nova etapa no orçamento?
- É necessário cadastrar subetapas para cada etapa?
- Como adicionar serviços a uma etapa existente no orçamento?

---


---


---

## 5. Checklists e Composição de Serviços

**📋 METADADOS:**
- **ID:** sec_5
- **⏱️ Minutagem:** 10:09 → 12:34
- **⏲️ Duração:** 145s
- **🎬 Link:** [Assistir este trecho](https://www.youtube.com/watch?v=BdLq4eBgfxQ&list=PLrsGJiMcdclnlo9exwzyqZC_e09rt5om8&index=4&t=609)
- **📦 Módulo:** Gestão de Serviços
- **🏷️ Categorias:** Checklist, Composição, Operacional
- **🔑 Palavras-chave:** checklist inicial, checklist final, composição, insumos, EPI, equipamentos

> **🔍 RESUMO EXECUTIVO:** Esta seção aborda a funcionalidade de checklists iniciais e finais, além da associação de composições a serviços, permitindo garantir a conformidade e a organização necessária para a execução de serviços.

**Contexto:**
Estamos na interface de gestão de serviços, onde o usuário pode iniciar e finalizar serviços, utilizando checklists para garantir que todas as conformidades sejam atendidas. A seção também permite associar composições que detalham os insumos necessários para a execução do serviço.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Gestão de Serviços > Tela de Execução de Serviços
- Tela/interface específica: Tela de Execução de Serviços

**Funcionalidade Detalhada:**

A funcionalidade de checklists permite que os usuários verifiquem se todos os requisitos estão atendidos antes e após a execução de um serviço. O checklist inicial é utilizado para garantir que todos os itens necessários para iniciar o serviço estão disponíveis, enquanto o checklist final assegura que todas as conformidades foram cumpridas ao término do serviço. Além disso, a funcionalidade de composição permite associar uma lista de insumos, que inclui materiais, mão de obra e equipamentos, a um serviço específico.

### 🔹 Passo a Passo Detalhado:

1. **Acessar o Checklist Inicial**
   - Localização: Tela de Execução de Serviços
   - Como fazer: Na tela, localize a seção de **Checklist Inicial**. Você verá uma lista de itens que podem ser verificados.
   - Campos/Opções disponíveis:
     * `EPI`: Equipamentos de Proteção Individual necessários para a execução do serviço.
     * `Organização da Equipe`: Verificação da disposição e organização da equipe que realizará o serviço.
     * `Local Limpo`: Confirmação de que o local está limpo e pronto para a execução.
   - Resultado esperado: Os itens selecionados no checklist inicial serão salvos e utilizados para garantir a conformidade durante a execução do serviço.

2. **Acessar o Checklist Final**
   - Localização: Tela de Execução de Serviços
   - Como fazer: Após a conclusão do serviço, localize a seção de **Checklist Final**. Aqui, você deve verificar os itens que precisam estar em conformidade.
   - Campos/Opções disponíveis:
     * `Entrega do EPI`: Confirmação de que todos os EPIs foram entregues.
     * `Entrega dos Equipamentos`: Verificação de que todos os equipamentos utilizados foram devolvidos.
     * `Limpeza do Local`: Confirmação de que o local foi limpo após a execução do serviço.
   - Resultado esperado: Os itens selecionados no checklist final serão salvos, indicando que todas as conformidades foram atendidas.

3. **Associar Composição ao Serviço**
   - Localização: Tela de Execução de Serviços, seção de **Composição**
   - Como fazer: Na seção de composição, clique no botão **Mais Associar** para adicionar uma composição ao serviço.
   - Observações importantes: Se não houver composições associadas, você verá uma mensagem indicando que nenhuma composição está disponível.
   - Resultado esperado: Uma lista de composições cadastradas será exibida, permitindo que você selecione a composição desejada.

4. **Pesquisar Composição**
   - Localização: Tela de Execução de Serviços, seção de **Composição**
   - Como fazer: Utilize a barra de pesquisa para buscar composições pelo nome ou código. Digite a nomenclatura ou o código da composição desejada.
   - Resultado esperado: A lista será filtrada para mostrar apenas as composições que correspondem à pesquisa.

5. **Adicionar Nova Composição**
   - Localização: Tela de Execução de Serviços, seção de **Composição**
   - Como fazer: Clique no botão **Mais Adicionar** para cadastrar uma nova composição.
   - Campos/Opções disponíveis:
     * `Nome da Composição`: Campo para inserir o nome da nova composição.
     * `Código da Composição`: Campo para inserir o código da nova composição.
   - Resultado esperado: A nova composição será cadastrada e estará disponível para associação ao serviço.

**Campos e Parâmetros:**

| Campo                   | Tipo         | Obrigatório | Descrição                                               | Exemplo               |
|-------------------------|--------------|-------------|---------------------------------------------------------|-----------------------|
| `EPI`                   | Checkbox     | Não         | Equipamentos de Proteção Individual necessários         | [ ] Capacete          |
| `Organização da Equipe` | Checkbox     | Não         | Verificação da disposição da equipe                     | [ ] Equipe organizada  |
| `Local Limpo`          | Checkbox     | Não         | Confirmação de que o local está limpo                  | [ ] Local limpo       |
| `Nome da Composição`    | Texto        | Sim         | Nome da nova composição a ser cadastrada                | "Composição A"        |
| `Código da Composição`   | Texto        | Sim         | Código da nova composição a ser cadastrada              | "COMP-A"              |

**Regras de Negócio:**
- O preenchimento dos checklists não é obrigatório, mas é altamente recomendado para garantir a conformidade.
- As composições devem ser cadastradas antes de serem associadas a um serviço.
- Se uma composição não estiver disponível, o usuário deve cadastrá-la antes de prosseguir.

**Observações Importantes:**
- É importante verificar todos os itens do checklist inicial antes de iniciar o serviço para evitar problemas futuros.
- Ao finalizar o serviço, todos os itens do checklist final devem ser verificados para garantir que todas as conformidades foram atendidas.
- Caso não utilize o SINAP, é necessário cadastrar manualmente as composições.

**Conceitos-Chave:**
- **Checklist Inicial**: Lista de verificação de itens necessários antes de iniciar um serviço.
- **Checklist Final**: Lista de verificação de conformidades a serem atendidas após a conclusão de um serviço.
- **Composição**: Conjunto de insumos necessários para a execução de um serviço, incluindo materiais, mão de obra e equipamentos.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- O que é o checklist inicial e como utilizá-lo?
- Como posso associar uma composição a um serviço?
- O que devo verificar no checklist final antes de finalizar um serviço?

---


---


---

## 6. Cadastro de Composição de Insumos

**📋 METADADOS:**
- **ID:** sec_6
- **⏱️ Minutagem:** 12:40 → 15:09
- **⏲️ Duração:** 149s
- **🎬 Link:** [Assistir este trecho](https://www.youtube.com/watch?v=BdLq4eBgfxQ&list=PLrsGJiMcdclnlo9exwzyqZC_e09rt5om8&index=4&t=760)
- **📦 Módulo:** Composição de Insumos
- **🏷️ Categorias:** Cadastro, Composição, Insumos, Orçamento
- **🔑 Palavras-chave:** composição, insumos, mão de obra, material, equipamento, valor unitário, cadastro

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como cadastrar uma composição de insumos no sistema, detalhando o processo de inclusão de mão de obra, materiais e equipamentos, além de explicar a diferença entre composições globais e detalhadas.

**Contexto:**
Estamos na funcionalidade de cadastro de composições de insumos dentro do módulo de Composição de Insumos. O objetivo é permitir que o usuário crie uma nova composição, seja ela detalhada ou global, para facilitar a execução de serviços.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Composição de Insumos > Cadastro de Composição
- Tela/interface específica: Tela de Cadastro de Composição

**Funcionalidade Detalhada:**

A funcionalidade de cadastro de composição de insumos permite ao usuário criar uma nova composição que pode incluir mão de obra, materiais e equipamentos necessários para a execução de um serviço. O sistema oferece a opção de criar uma composição a partir de insumos já existentes ou cadastrar novos insumos do zero. O usuário pode optar por uma composição global, que simplifica o processo ao permitir o cadastro de valores unitários sem detalhar cada insumo individualmente.

### 🔹 Passo a Passo Detalhado:

1. **Inserir Nome da Composição**
   - Localização: Campo de texto no topo da tela de cadastro.
   - Como fazer: Clique no campo de texto e digite o nome desejado para a composição. O nome pode ser o mesmo do serviço ou outro que você achar mais apropriado.
   - Resultado esperado: O nome da composição é salvo e exibido na tela.

2. **Adicionar Insumos**
   - Localização: Botão **"Mais Insumo"** na parte inferior da tela.
   - Como fazer: Clique no botão **"Mais Insumo"** para abrir a opção de cadastro de insumos.
   - Observações importantes: Se você já possui uma composição criada, pode usar a opção **"Mais Composição"** para complementar a composição atual.
   - Resultado esperado: Uma nova linha é adicionada para que você possa listar os insumos necessários.

3. **Cadastrar Mão de Obra**
   - Localização: Campo de seleção para tipo de insumo.
   - Como fazer: Selecione **"Mão de Obra"** na lista de tipos de insumos. Em seguida, preencha os campos obrigatórios.
   - Campos/Opções disponíveis:
     * `Cargo`: Campo de texto para inserir o cargo da mão de obra.
     * `Valor Unitário`: Campo numérico para inserir o valor unitário da mão de obra.
     * `Quantidade Unitária`: Campo numérico para inserir a quantidade de mão de obra necessária.
   - Resultado esperado: Os dados da mão de obra são salvos e podem ser utilizados no orçamento.

4. **Cadastrar Material**
   - Localização: Campo de seleção para tipo de insumo.
   - Como fazer: Selecione **"Material"** na lista de tipos de insumos. Em seguida, preencha os campos obrigatórios.
   - Campos/Opções disponíveis:
     * `Categoria`: Campo de seleção para escolher a categoria do material.
     * `Subcategoria`: Campo de seleção para escolher a subcategoria do material.
     * `Valor Unitário`: Campo numérico para inserir o valor unitário do material.
   - Resultado esperado: Os dados do material são salvos e podem ser utilizados no orçamento.

5. **Finalizar Cadastro**
   - Localização: Botão **"Adicionar"** na parte inferior da tela.
   - Como fazer: Após preencher todos os insumos necessários, clique no botão **"Adicionar"** para finalizar o cadastro da composição.
   - Resultado esperado: A composição é salva no sistema e pode ser acessada posteriormente para orçamentos.

**Campos e Parâmetros:**

| Campo               | Tipo         | Obrigatório | Descrição                                             | Exemplo                |
|---------------------|--------------|-------------|------------------------------------------------------|------------------------|
| Nome da Composição   | Texto        | Sim         | Nome que identifica a composição                      | "Composição de Serviço"|
| Tipo de Insumo      | Seleção      | Sim         | Tipo de insumo a ser cadastrado (Mão de Obra ou Material) | "Mão de Obra"         |
| Cargo               | Texto        | Sim         | Cargo da mão de obra                                  | "Eletricista"         |
| Valor Unitário      | Numérico     | Sim         | Valor unitário do insumo                              | "50.00"               |
| Quantidade Unitária | Numérico     | Sim         | Quantidade do insumo a ser utilizada                  | "10"                  |
| Categoria           | Seleção      | Sim         | Categoria do material                                 | "Elétrico"            |
| Subcategoria        | Seleção      | Sim         | Subcategoria do material                              | "Fios"                |

**Regras de Negócio:**
- O nome da composição deve ser único dentro do sistema.
- O valor unitário da mão de obra e do material deve ser preenchido para que a composição seja válida.
- A quantidade unitária deve ser um número positivo.
- As categorias e subcategorias devem ser selecionadas corretamente para o material.

**Observações Importantes:**
- É recomendado que os usuários detalhem insumo por insumo para melhor controle e visualização.
- Evite cadastrar composições sem especificar todos os insumos necessários, pois isso pode gerar inconsistências no orçamento.
- Verifique se todos os campos obrigatórios estão preenchidos antes de finalizar o cadastro.

**Conceitos-Chave:**
- **Composição Global**: Uma composição que permite o cadastro de valores unitários sem detalhar cada insumo individualmente.
- **Insumo**: Qualquer item necessário para a execução de um serviço, incluindo mão de obra, materiais e equipamentos.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como cadastrar uma nova composição de insumos no sistema?
- Quais são os campos obrigatórios para o cadastro de mão de obra e material?
- O que é uma composição global e como ela difere de uma composição detalhada?

---


---


---

## 7. Cadastro de Composição e Cálculo de Orçamento

**📋 METADADOS:**
- **ID:** sec_7
- **⏱️ Minutagem:** 15:23 → 17:55
- **⏲️ Duração:** 152s
- **🎬 Link:** [Assistir este trecho](https://www.youtube.com/watch?v=BdLq4eBgfxQ&list=PLrsGJiMcdclnlo9exwzyqZC_e09rt5om8&index=4&t=923)
- **📦 Módulo:** Orçamento
- **🏷️ Categorias:** Cadastro, Orçamento, Composição
- **🔑 Palavras-chave:** composição, orçamento, serviço, insumo, editar

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de cadastro de uma composição associada a um serviço no sistema, incluindo a inserção de insumos e o cálculo do valor total do orçamento com base na quantidade e no valor unitário.

**Contexto:**
Estamos na tela de orçamento do sistema, onde o usuário pode cadastrar composições de serviços e calcular os custos associados. O objetivo é permitir que o usuário insira informações detalhadas sobre os insumos necessários para a execução de um serviço e obtenha o valor total a ser gasto.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Orçamento > Tela de Cadastro de Composição
- Tela/interface específica: Tela de Orçamento

**Funcionalidade Detalhada:**
A funcionalidade permite ao usuário cadastrar uma composição associada a um serviço específico. O sistema calcula automaticamente o valor total com base na quantidade inserida e no valor unitário dos insumos. O usuário pode editar a quantidade de insumos conforme necessário.

### 🔹 Passo a Passo Detalhado:

1. **Cadastro da Composição**
   - Localização: Tela de Orçamento, seção de cadastro de composição.
   - Como fazer: O usuário deve inserir a quantidade do serviço que será executado no campo correspondente. O sistema automaticamente multiplica essa quantidade pelo valor unitário da composição cadastrada.
   - Campos/Opções disponíveis:
     * `Quantidade`: Campo numérico onde o usuário insere a quantidade do serviço a ser executado.
     * `Valor Unitário`: Campo que exibe o valor unitário da composição, que é puxado automaticamente do cadastro.
   - Resultado esperado: O sistema calcula e exibe o valor total que será gasto para o serviço.

2. **Edição da Quantidade**
   - Localização: Ao lado do campo de quantidade, há um ícone de três pontinhos.
   - Como fazer: O usuário deve clicar nos três pontinhos e selecionar a opção "Editar" para modificar a quantidade previamente inserida.
   - Observações importantes: É importante que o usuário revise a quantidade antes de confirmar a edição, pois isso afetará o cálculo do valor total.
   - Resultado esperado: O sistema atualiza a quantidade e recalcula o valor total automaticamente.

3. **Cadastro de Nova Etapa**
   - Localização: Tela de Orçamento, seção de cadastro de nova etapa.
   - Como fazer: O usuário deve clicar no botão "Adicionar Etapa" para iniciar o cadastro de um novo serviço.
   - Campos/Opções disponíveis:
     * `Serviço`: Campo onde o usuário insere o nome do serviço, por exemplo, "Alvenaria e Assentamento".
   - Resultado esperado: O sistema prepara a tela para o cadastro de uma nova composição associada ao serviço inserido.

4. **Inserção de Insumos**
   - Localização: Após cadastrar o serviço, o usuário deve inserir os insumos necessários.
   - Como fazer: O usuário deve clicar em "Adicionar Insumo" e selecionar os insumos necessários, como "Pedreiro", "Cimento" e "Argamassa".
   - Campos/Opções disponíveis:
     * `Insumo`: Dropdown onde o usuário seleciona os insumos a serem utilizados.
   - Resultado esperado: O sistema puxa automaticamente o valor unitário de cada insumo da base de dados.

5. **Definição de Quantidades de Insumos**
   - Localização: Após selecionar os insumos, o usuário deve inserir as quantidades necessárias.
   - Como fazer: O usuário deve preencher os campos correspondentes a cada insumo, como "Horas do Pedreiro" e "Quilos de Cimento".
   - Campos/Opções disponíveis:
     * `Horas do Pedreiro`: Campo numérico onde o usuário insere a quantidade de horas necessárias para executar 1 m² de alvenaria (exemplo: 0,5 horas).
     * `Quilos de Cimento`: Campo numérico onde o usuário insere a quantidade de cimento necessária para executar 1 m² de alvenaria (exemplo: 6 kg).
   - Resultado esperado: O sistema registra as quantidades e prepara para o cálculo do valor total.

**Campos e Parâmetros:**

| Campo                  | Tipo       | Obrigatório | Descrição                                      | Exemplo       |
|------------------------|------------|-------------|------------------------------------------------|---------------|
| `Quantidade`           | Numérico   | Sim         | Quantidade do serviço a ser executado         | 10            |
| `Valor Unitário`       | Moeda      | Sim         | Valor unitário da composição                   | R$ 50,00      |
| `Serviço`              | Texto      | Sim         | Nome do serviço a ser cadastrado               | Alvenaria     |
| `Insumo`               | Dropdown   | Sim         | Insumos necessários para o serviço             | Pedreiro      |
| `Horas do Pedreiro`    | Numérico   | Sim         | Horas necessárias para executar 1 m² de serviço| 0,5           |
| `Quilos de Cimento`    | Numérico   | Sim         | Quantidade de cimento necessária para 1 m²     | 6             |

**Regras de Negócio:**
- O sistema deve calcular automaticamente o valor total com base na quantidade e no valor unitário.
- O usuário pode editar a quantidade de insumos a qualquer momento, e o sistema deve recalcular o valor total.
- Os valores unitários dos insumos podem ser atualizados pelo usuário, caso haja mudanças.

**Observações Importantes:**
- É recomendável revisar todos os insumos e suas quantidades antes de finalizar o orçamento.
- Erros comuns incluem a inserção de quantidades incorretas, que podem levar a um cálculo de orçamento impreciso.
- Certifique-se de que todos os insumos necessários estão cadastrados na base de dados antes de iniciar o processo.

**Conceitos-Chave:**
- **Composição**: Conjunto de insumos e serviços necessários para a execução de uma tarefa específica.
- **Orçamento**: Estimativa de custos associados à execução de um serviço, calculada com base em quantidades e valores unitários.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como cadastrar uma nova composição associada a um serviço?
- Como editar a quantidade de insumos em um orçamento?
- Quais insumos são necessários para o serviço de alvenaria?

---


---


---

## 8. Configuração de Unidades de Medida e Execução de Serviços

**📋 METADADOS:**
- **ID:** sec_8
- **⏱️ Minutagem:** 17:54 → 20:29
- **⏲️ Duração:** 154s
- **🎬 Link:** [Assistir este trecho](https://www.youtube.com/watch?v=BdLq4eBgfxQ&list=PLrsGJiMcdclnlo9exwzyqZC_e09rt5om8&index=4&t=1074)
- **📦 Módulo:** Orçamento
- **🏷️ Categorias:** Configuração, Execução, Orçamento, Vendas
- **🔑 Palavras-chave:** unidade de medida, argamassa, orçamento, composição, proposta, venda, condições de pagamento, medição

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como configurar as unidades de medida para produtos e serviços no sistema, além de como formalizar propostas e vendas diretas, garantindo que os valores e condições de pagamento estejam corretos.

**Contexto:**
Estamos na seção de orçamento do sistema, onde o usuário pode definir as unidades de medida para produtos e serviços, além de formalizar propostas e vendas. O objetivo é garantir que todas as informações estejam corretas e que o usuário possa realizar transações de forma eficiente.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Orçamento > Submenu Configuração de Unidades e Vendas
- Tela/interface específica: Tela de Orçamento

**Funcionalidade Detalhada:**

Esta funcionalidade permite ao usuário configurar as unidades de medida do produto e da execução do serviço, como, por exemplo, quantos metros cúbicos de argamassa são necessários para executar 1 m² de alvenaria. O usuário pode editar os valores unitários dos insumos utilizados no orçamento, especialmente se estiver utilizando composições da SINAP. Além disso, é possível formalizar propostas para clientes ou realizar vendas diretas, definindo condições de pagamento e classificações financeiras.

### 🔹 Passo a Passo Detalhado:

1. **Configuração de Unidades de Medida**
   - Localização: Tela de Orçamento, seção de unidades de medida.
   - Como fazer: O usuário deve identificar as unidades de medida do produto e da execução do serviço. Por exemplo, ao calcular a quantidade de argamassa, deve-se determinar quantos m³ são necessários para 1 m² de alvenaria.
   - Campos/Opções disponíveis:
     * `Unidade de Medida do Produto`: Exemplo: m³ (metros cúbicos)
     * `Unidade de Medida da Execução`: Exemplo: m² (metros quadrados)
   - Resultado esperado: O sistema calcula automaticamente a quantidade necessária de insumos para a execução do serviço.

2. **Edição de Valores Unitários dos Insumos**
   - Localização: Subaba de composições dentro da tela de orçamento.
   - Como fazer: O usuário pode editar os valores unitários dos insumos utilizados no orçamento. Para isso, deve selecionar a composição desejada e clicar no campo de valor unitário.
   - Observações importantes: Alterações feitas aqui afetam apenas o orçamento atual e não as composições globais.
   - Resultado esperado: O valor unitário do insumo é atualizado para o orçamento em questão.

3. **Formalização de Propostas e Vendas**
   - Localização: Tela de Orçamento, seção de proposta/venda.
   - Como fazer: O usuário deve selecionar o cliente (por exemplo, "Karina"), inserir a data da venda e adicionar uma classificação financeira referente à receita gerada.
   - Campos/Opções disponíveis:
     * `Cliente`: Selecionar cliente (dropdown com lista de clientes)
     * `Data da Venda`: Campo de data
     * `Classificação Financeira`: Campo para inserir a classificação
   - Resultado esperado: A proposta ou venda é criada com as informações inseridas.

4. **Definição das Condições de Pagamento**
   - Localização: Tela de proposta/venda, seção de condições de pagamento.
   - Como fazer: O usuário deve inserir o valor à vista combinado com o cliente (por exemplo, R$ 60.000) e a primeira data de vencimento. Para parcelas, clicar em "Mais Condição Especial" e inserir a quantidade de parcelas, valor total da condição e data de vencimento.
   - Campos/Opções disponíveis:
     * `Valor à Vista`: Campo numérico
     * `Data de Vencimento`: Campo de data
     * `Quantidade de Parcelas`: Campo numérico
     * `Valor Total da Condição`: Campo numérico
     * `Percentual dos Juros`: Campo numérico (opcional)
   - Resultado esperado: As condições de pagamento são registradas e podem ser visualizadas na proposta ou venda.

5. **Recebimento por Medição**
   - Localização: Tela de proposta/venda, opção de recebimento.
   - Como fazer: O usuário deve selecionar a opção "Recebimento por Medição" e inserir o valor total a ser recebido.
   - Campos/Opções disponíveis:
     * `Recebimento por Medição`: Checkbox para seleção
     * `Valor Total`: Campo numérico
   - Resultado esperado: O sistema registra que o recebimento será feito por medição e o valor total é salvo.

**Campos e Parâmetros:**

| Campo                        | Tipo      | Obrigatório | Descrição                                           | Exemplo          |
|------------------------------|-----------|-------------|----------------------------------------------------|------------------|
| Unidade de Medida do Produto  | Texto     | Sim         | Unidade de medida utilizada para o produto         | m³               |
| Unidade de Medida da Execução | Texto     | Sim         | Unidade de medida utilizada para a execução         | m²               |
| Cliente                       | Dropdown  | Sim         | Seleção do cliente para a proposta ou venda        | Karina           |
| Data da Venda                 | Data      | Sim         | Data em que a venda será realizada                 | 01/01/2023       |
| Classificação Financeira      | Texto     | Não         | Classificação financeira da receita gerada          | Venda Direta     |
| Valor à Vista                 | Numérico  | Sim         | Valor total a ser pago à vista                     | 60.000           |
| Data de Vencimento            | Data      | Sim         | Data de vencimento da primeira parcela              | 01/02/2023       |
| Quantidade de Parcelas        | Numérico  | Não         | Número de parcelas acordadas                        | 5                |
| Valor Total da Condição       | Numérico  | Não         | Valor total a ser pago nas parcelas                 | 30.000           |
| Percentual dos Juros         | Numérico  | Não         | Percentual de juros aplicável nas parcelas         | 2%               |
| Recebimento por Medição       | Checkbox  | Não         | Indica se o recebimento será feito por medição     | [ ] Sim          |
| Valor Total                   | Numérico  | Sim         | Valor total a ser recebido por medição              | 100.000          |

**Regras de Negócio:**
- A edição dos valores unitários dos insumos afeta apenas o orçamento atual.
- As condições de pagamento devem ser registradas de acordo com o que foi acordado com o cliente.
- O recebimento por medição deve ser utilizado quando aplicável, e o valor total deve ser inserido corretamente.

**Observações Importantes:**
- É importante verificar se as unidades de medida estão corretas antes de finalizar o orçamento.
- Evitar alterar valores unitários sem a devida confirmação, pois isso pode impactar o resultado final do orçamento.
- As condições de pagamento devem ser claras e acordadas previamente com o cliente para evitar mal-entendidos.

**Conceitos-Chave:**
- **Unidade de Medida**: Refere-se à medida utilizada para quantificar produtos e serviços, como metros cúbicos (m³) e metros quadrados (m²).
- **Composição**: Conjunto de insumos e serviços que compõem um orçamento específico.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como configurar as unidades de medida para produtos e serviços no sistema?
- Como editar os valores unitários dos insumos em um orçamento?
- Como formalizar uma proposta ou venda direta para um cliente?

---


---


---

## 9. Geração de Planejamento de Obra

**📋 METADADOS:**
- **ID:** sec_9
- **⏱️ Minutagem:** 20:26 → 23:01
- **⏲️ Duração:** 155s
- **🎬 Link:** [Assistir este trecho](https://www.youtube.com/watch?v=BdLq4eBgfxQ&list=PLrsGJiMcdclnlo9exwzyqZC_e09rt5om8&index=4&t=1226)
- **📦 Módulo:** Orçamento
- **🏷️ Categorias:** Planejamento, Orçamento, Operacional
- **🔑 Palavras-chave:** planejamento, orçamento, obra, cliente, BDI

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como gerar o planejamento de uma obra após a realização do orçamento, detalhando os passos necessários para associar a obra e o cliente, além de explicar as opções de edição e replicação do orçamento.

**Contexto:**
Estamos na fase de planejamento de uma obra dentro do módulo de Orçamento do sistema. O objetivo desta seção é guiar o usuário na geração do planejamento, que é um passo crucial após a finalização do orçamento.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Orçamento > Planejamento de Obra
- Tela/interface específica: Tela de Geração de Planejamento

**Funcionalidade Detalhada:**
A funcionalidade de geração de planejamento de obra permite que o usuário associe um planejamento a uma obra específica, garantindo que as informações do orçamento sejam refletidas no planejamento. O planejamento deve ser gerado após a finalização do orçamento e é necessário associar a obra e o cliente a este planejamento.

### 🔹 Passo a Passo Detalhado:

1. **Inserir Data de Vencimento**
   - Localização: Campo de data na tela de orçamento
   - Como fazer: Clique no campo de data e selecione uma data futura, preferencialmente próxima ao final da obra.
   - Campos/Opções disponíveis:
     * `Data de Vencimento`: Campo de seleção de data (tipo data)
   - Resultado esperado: A data de vencimento é salva e não será contabilizada no financeiro até a data selecionada.

2. **Salvar Orçamento**
   - Localização: Botão **Salvar** na parte inferior da tela
   - Como fazer: Clique no botão **Salvar** para finalizar o orçamento.
   - Resultado esperado: O orçamento é salvo com sucesso, e uma mensagem de confirmação é exibida.

3. **Gerar Planejamento da Obra**
   - Localização: Botão ou opção **Gerar Planejamento** na tela de orçamento
   - Como fazer: Clique na opção **Gerar Planejamento** para iniciar o processo de planejamento.
   - Observações importantes: É obrigatório associar uma obra ao planejamento gerado.
   - Resultado esperado: O planejamento é criado e as informações do orçamento são replicadas.

4. **Associar Obra ao Planejamento**
   - Localização: Campo de associação de obra na tela de planejamento
   - Como fazer: Digite o nome da obra ou selecione a obra desejada na lista suspensa.
   - Campos/Opções disponíveis:
     * `Nome da Obra`: Campo de texto ou dropdown (tipo texto)
   - Resultado esperado: A obra é associada ao planejamento.

5. **Associar Cliente ao Planejamento**
   - Localização: Campo de associação de cliente na tela de planejamento
   - Como fazer: Digite o nome do cliente ou selecione o cliente desejado na lista suspensa.
   - Campos/Opções disponíveis:
     * `Nome do Cliente`: Campo de texto ou dropdown (tipo texto)
   - Resultado esperado: O cliente é associado ao planejamento.

6. **Finalizar Geração do Planejamento**
   - Localização: Botão **Finalizar** na tela de planejamento
   - Como fazer: Clique no botão **Finalizar** para concluir o processo de geração do planejamento.
   - Resultado esperado: O planejamento é salvo e as informações orçadas e planejadas são exibidas como iguais.

**Campos e Parâmetros:**

| Campo                | Tipo         | Obrigatório | Descrição                                          | Exemplo              |
|----------------------|--------------|-------------|---------------------------------------------------|----------------------|
| Data de Vencimento   | Data         | Sim         | Data em que o orçamento deve ser considerado.     | 30/12/2023           |
| Nome da Obra         | Texto        | Sim         | Nome da obra a ser associada ao planejamento.     | Construção Prédio A   |
| Nome do Cliente       | Texto        | Sim         | Nome do cliente a ser associado ao planejamento.   | João da Silva        |

**Regras de Negócio:**
- A data de vencimento deve ser sempre futura para evitar contabilização prematura no financeiro.
- É obrigatório associar uma obra e um cliente ao planejamento gerado.
- O planejamento traz as mesmas informações do orçamento, refletindo valores orçados e planejados iguais.

**Observações Importantes:**
- Recomenda-se que a data de vencimento seja escolhida próxima ao final da obra para facilitar o controle financeiro.
- Caso seja necessário editar o orçamento, o usuário pode alterar o nome, adicionar observações e ajustar o percentual do BDI através da opção de edição.
- Para replicar um orçamento, utilize a função de replicação disponível no sistema, permitindo ajustes em itens específicos.

**Conceitos-Chave:**
- **BDI (Bonificação e Despesas Indiretas)**: Percentual aplicado sobre o custo direto de um serviço para cobrir despesas indiretas e lucro.
- **Planejamento de Obra**: Documento que organiza e detalha as etapas e recursos necessários para a execução de uma obra.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso gerar o planejamento de uma obra após finalizar o orçamento?
- Quais informações são necessárias para associar uma obra e um cliente ao planejamento?
- O que devo fazer se precisar editar o orçamento antes de gerar o planejamento?

---


---


---

## 10. Alterações no Planejamento de Obras

**📋 METADADOS:**
- **ID:** sec_10
- **⏱️ Minutagem:** 22:58 → 25:32
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://www.youtube.com/watch?v=BdLq4eBgfxQ&list=PLrsGJiMcdclnlo9exwzyqZC_e09rt5om8&index=4&t=1378)
- **📦 Módulo:** Planejamento de Obras
- **🏷️ Categorias:** Planejamento, Controle, Execução
- **🔑 Palavras-chave:** alteração, serviço, orçamento, planejamento, medição, controle, execução, cronograma

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como realizar alterações no planejamento de obras, enfatizando a importância de fazer essas alterações na etapa correta para garantir a precisão entre o orçamento, planejamento e execução real.

**Contexto:**
Estamos na fase de planejamento de uma obra, onde é possível realizar alterações nos serviços e valores previamente definidos. É crucial que essas alterações sejam feitas na aba de planejamento, pois alterações feitas no orçamento não se replicam automaticamente para o planejamento.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Planejamento de Obras > Submenu Planejamento
- Tela/interface específica: Tela de Planejamento de Obras

**Funcionalidade Detalhada:**
A funcionalidade permite que o usuário faça alterações diretamente na etapa de planejamento, garantindo que as informações estejam atualizadas e que haja um comparativo entre o que foi orçado, o que está planejado e o que foi executado. É importante ressaltar que as alterações no orçamento não se refletem automaticamente no planejamento.

### 🔹 Passo a Passo Detalhado:

1. **Realizar Alterações no Planejamento**
   - Localização: Tela de Planejamento de Obras, na seção onde estão listados os serviços.
   - Como fazer: Navegue até a aba de planejamento e localize o serviço que deseja alterar. Clique no serviço para editar.
   - Campos/Opções disponíveis:
     * `Valor a Receber`: Campo onde você insere o valor que está previsto a receber referente ao serviço.
     * `Valor a Pagar`: Campo onde você insere o valor que está previsto a pagar referente ao serviço.
   - Resultado esperado: Os valores inseridos são atualizados no planejamento, permitindo um acompanhamento mais preciso das medições futuras.

2. **Preencher a Subaba de Orçamento (Opcional)**
   - Localização: Dentro da aba de planejamento, clique na subaba "Orçamento".
   - Como fazer: Caso você trabalhe com medições a pagar ou a receber, insira os valores correspondentes nos campos `Valor a Receber` e `Valor a Pagar`.
   - Observações importantes: Esta subaba não é obrigatória para todos os usuários; somente aqueles que trabalham com medições devem preenchê-la.
   - Resultado esperado: Os valores inseridos impactam nas medições quando estas forem realizadas.

3. **Preencher a Subaba de Controle**
   - Localização: Na mesma tela de planejamento, clique na subaba "Controle".
   - Como fazer: Selecione a forma de medição de execução e medição de recebimento. As opções disponíveis dependem da estrutura da obra (andar, bloco, unidades).
   - Campos/Opções disponíveis:
     * `Forma de Medição`: Opções como "andar", "bloco", "unidade de medida do serviço".
   - Resultado esperado: A forma de medição selecionada será utilizada para acompanhar a execução e a medição do serviço.

4. **Especificar Locais para Medição**
   - Localização: Após selecionar a forma de medição, um campo para especificar os locais aparecerá.
   - Como fazer: Escolha a forma de medição desejada (por exemplo, "bloco") e especifique os locais conforme solicitado pelo sistema.
   - Resultado esperado: Os locais especificados serão utilizados nas medições futuras.

**Campos e Parâmetros:**

| Campo                | Tipo   | Obrigatório | Descrição                                                       | Exemplo      |
|----------------------|--------|-------------|-----------------------------------------------------------------|--------------|
| Valor a Receber      | Numérico | Não         | Valor previsto a receber referente ao serviço.                 | 50.000       |
| Valor a Pagar        | Numérico | Não         | Valor previsto a pagar referente ao serviço.                   | 1.300        |
| Forma de Medição     | Dropdown | Sim         | Método de medição utilizado (andar, bloco, unidade).           | Bloco        |
| Local de Medição      | Texto  | Sim         | Local onde a medição será realizada.                           | Bloco A      |

**Regras de Negócio:**
- Alterações devem ser feitas na aba de planejamento para garantir a precisão dos dados.
- A subaba de orçamento não é obrigatória para todos os usuários, apenas para aqueles que trabalham com medições.
- A forma de medição deve ser escolhida de acordo com a estrutura da obra.

**Observações Importantes:**
- Sempre faça as alterações na etapa correta para evitar inconsistências.
- Evite preencher a subaba de orçamento se não estiver trabalhando com medições.
- Verifique se a forma de medição está correta antes de prosseguir.

**Conceitos-Chave:**
- **Medição**: Processo de quantificação dos serviços executados para controle financeiro.
- **Planejamento**: Etapa onde se define como os serviços serão executados e medidos.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso alterar um serviço no planejamento de obras?
- O que devo fazer se não trabalho com medições?
- Quais são as opções de medição disponíveis no sistema?

---


---


---

## 11. Execução e Acompanhamento de Serviços

**📋 METADADOS:**
- **ID:** sec_11
- **⏱️ Minutagem:** 25:37 → 28:09
- **⏲️ Duração:** 152s
- **🎬 Link:** [Assistir este trecho](https://www.youtube.com/watch?v=BdLq4eBgfxQ&list=PLrsGJiMcdclnlo9exwzyqZC_e09rt5om8&index=4&t=1537)
- **📦 Módulo:** Planejamento de Obras
- **🏷️ Categorias:** Execução, Acompanhamento, Planejamento, Serviços
- **🔑 Palavras-chave:** execução, serviços, cronograma, planejamento, acompanhamento, predecessores, insumos

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de execução de serviços em um projeto de obra, incluindo a definição de mão de obra, unidades de medida, cronograma e a geração de acompanhamento da obra.

**Contexto:**
Estamos na fase de execução de um projeto de obra, onde é necessário definir como os serviços serão realizados, incluindo a mão de obra e o cronograma. Esta seção orienta sobre como registrar essas informações e acompanhar a execução.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Planejamento de Obras > Execução de Serviços
- Tela/interface específica: Tela de Execução e Acompanhamento de Serviços

**Funcionalidade Detalhada:**
A funcionalidade permite ao usuário definir como os serviços serão executados, seja por mão de obra própria, terceirizada ou uma combinação de ambas. Além disso, é possível especificar a unidade de medida dos serviços (como m² ou m³) e estabelecer um cronograma com datas de início e término para cada serviço. O sistema também permite a inclusão de predecessores, que são serviços que precisam ser concluídos antes que outros possam ser iniciados.

### 🔹 Passo a Passo Detalhado:

1. **Definir Forma de Execução**
   - Localização: Tela de Execução de Serviços
   - Como fazer: Selecione a forma de execução desejada para o serviço. As opções disponíveis são:
     * **Mão de obra própria**
     * **Mão de obra terceirizada**
     * **Mista**
   - Resultado esperado: A forma de execução selecionada será registrada para o serviço.

2. **Especificar Unidade de Medida**
   - Localização: Tela de Execução de Serviços
   - Como fazer: Escolha a unidade de medida que será utilizada para o serviço. As opções incluem:
     * **m²** (metros quadrados)
     * **m³** (metros cúbicos)
   - Resultado esperado: A unidade de medida será associada ao serviço, facilitando o acompanhamento posterior.

3. **Definir Cronograma**
   - Localização: Tela de Execução de Serviços
   - Como fazer: Insira as datas previstas para iniciar e finalizar cada serviço. Utilize os campos:
     * `Data de Início`: [Campo para inserir a data de início]
     * `Data de Término`: [Campo para inserir a data de término]
   - Resultado esperado: As datas serão salvas, permitindo comparações entre o planejado e o executado.

4. **Adicionar Predecessores (Opcional)**
   - Localização: Tela de Execução de Serviços
   - Como fazer: Se desejar, adicione predecessores ao serviço. Isso indica que um serviço depende da conclusão de outro. Por exemplo, "não posso iniciar o serviço de alvenaria antes de finalizar a limpeza geral do canteiro".
   - Observações importantes: A inclusão de predecessores é informativa, mas não impede a execução de serviços fora da ordem.
   - Resultado esperado: A relação de precedência será registrada, ajudando no planejamento.

5. **Salvar Planejamento**
   - Localização: Tela de Execução de Serviços
   - Como fazer: Após definir todos os campos, clique no botão **Salvar** para registrar o planejamento.
   - Resultado esperado: O planejamento será salvo e estará disponível para futuras consultas e edições.

6. **Gerar Acompanhamento da Obra**
   - Localização: Tela de Execução de Serviços
   - Como fazer: Selecione a opção **Gerar Acompanhamento**. Insira o nome do acompanhamento no campo designado e clique em **Salvar**.
   - Resultado esperado: O acompanhamento da obra será criado, permitindo monitorar a execução dos serviços e os valores gastos.

**Campos e Parâmetros:**

| Campo                | Tipo       | Obrigatório | Descrição                                             | Exemplo               |
|----------------------|------------|-------------|-----------------------------------------------------|-----------------------|
| Forma de Execução    | Dropdown   | Sim         | Seleciona como o serviço será executado.            | Mão de obra própria    |
| Unidade de Medida    | Dropdown   | Sim         | Define a unidade de medida do serviço.               | m²                    |
| Data de Início       | Data       | Sim         | Data prevista para o início do serviço.              | 01/01/2024            |
| Data de Término      | Data       | Sim         | Data prevista para a conclusão do serviço.           | 15/01/2024            |
| Predecessores        | Texto      | Não         | Indica serviços que devem ser concluídos antes.     | Limpeza geral         |
| Nome do Acompanhamento| Texto     | Sim         | Nome para identificar o acompanhamento gerado.      | Acompanhamento 1      |

**Regras de Negócio:**
- A forma de execução deve ser escolhida antes de salvar o planejamento.
- As datas de início e término devem ser válidas e seguir a sequência lógica do cronograma.
- Predecessores são informativos e não bloqueiam a execução de serviços.

**Observações Importantes:**
- Alterações nos insumos podem ser feitas diretamente na tela de planejamento.
- É importante verificar se a forma de execução e a unidade de medida estão corretas antes de salvar.
- Evite adicionar muitos predecessores, pois isso pode complicar o planejamento.

**Conceitos-Chave:**
- **Predecessores**: Serviços que precisam ser concluídos antes que outros possam ser iniciados.
- **Cronograma**: Planejamento temporal que define quando cada serviço deve ser iniciado e concluído.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como defino a forma de execução de um serviço?
- Quais unidades de medida posso usar para os serviços?
- Como posso acompanhar a execução dos serviços após o planejamento?

---


---


---

## 12. Liberação de Serviços para Execução

**📋 METADADOS:**
- **ID:** sec_12
- **⏱️ Minutagem:** 28:08 → 30:43
- **⏲️ Duração:** 155s
- **🎬 Link:** [Assistir este trecho](https://www.youtube.com/watch?v=BdLq4eBgfxQ&list=PLrsGJiMcdclnlo9exwzyqZC_e09rt5om8&index=4&t=1688)
- **📦 Módulo:** Acompanhamento de Serviços
- **🏷️ Categorias:** Operacional, Gestão de Projetos, Execução de Serviços
- **🔑 Palavras-chave:** liberação, serviços, execução, apontamentos, colaboradores

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de liberação de serviços para execução dentro do sistema, explicando como registrar e acompanhar o status dos serviços planejados, além de associar colaboradores a esses serviços.

**Contexto:**
Estamos na interface do módulo de Acompanhamento de Serviços, onde o usuário pode gerenciar a execução de serviços planejados. O objetivo desta seção é guiar o usuário na liberação de serviços, permitindo que eles sejam iniciados e acompanhados adequadamente.

**Localização no Sistema:**
- Caminho de navegação: Menu Principal > Módulo Acompanhamento de Serviços > Submenu Liberação de Serviços
- Tela/interface específica: Tela de Liberação de Serviços

**Funcionalidade Detalhada:**
A funcionalidade de liberação de serviços permite que o usuário autorize a execução de serviços previamente planejados. O usuário pode selecionar serviços específicos, definir prazos e associar colaboradores que irão executar as tarefas. Essa liberação é essencial para o acompanhamento e controle do progresso dos serviços.

### 🔹 Passo a Passo Detalhado:

1. **Acessar a Tela de Liberação de Serviços**
   - Localização: Menu Principal > Módulo Acompanhamento de Serviços > Submenu Liberação de Serviços
   - Como fazer: Clique no submenu "Liberação de Serviços" para acessar a tela.
   - Resultado esperado: A tela de Liberação de Serviços será exibida, mostrando a estrutura de serviços planejados.

2. **Selecionar Ordem de Produção**
   - Localização: Tela de Liberação de Serviços
   - Como fazer: Clique no botão **Mais Ordens de Produção**.
   - Campos/Opções disponíveis:
     * `Título`: Campo para inserir um título descritivo da ordem de produção.
     * `Previsão para Início`: Campo para inserir a data prevista para o início da execução.
     * `Previsão para Término`: Campo para inserir a data prevista para o término da execução.
   - Resultado esperado: Um formulário para preenchimento das informações da ordem de produção será exibido.

3. **Preencher Informações da Ordem de Produção**
   - Localização: Formulário de Ordem de Produção
   - Como fazer: Preencha os campos `Título`, `Previsão para Início` e `Previsão para Término` com as informações desejadas. Note que esses preenchimentos são apenas informativos e não impactam no sistema neste primeiro momento.
   - Resultado esperado: As informações são salvas temporariamente, permitindo a seleção dos serviços.

4. **Selecionar Serviços para Liberação**
   - Localização: Formulário de Ordem de Produção
   - Como fazer: Marque os serviços que deseja liberar para execução. Por exemplo, selecione "Limpeza Geral do Canteiro" e escolha a unidade de medida correspondente.
   - Observações importantes: Para serviços como "Alvenaria", que são medidos por bloco, você pode optar por liberar parcialmente, selecionando apenas a alvenaria do bloco A ou bloco B, ou liberar todos de uma vez.
   - Resultado esperado: Os serviços selecionados são marcados para liberação.

5. **Associar Colaboradores (Opcional)**
   - Localização: Formulário de Ordem de Produção
   - Como fazer: Se o módulo de RH estiver disponível, você pode associar colaboradores que irão executar os serviços. O sistema identifica colaboradores baseando-se no cargo.
   - Observações importantes: Se um colaborador não possui o cargo necessário, ele será listado como não alocado e não poderá ser associado.
   - Resultado esperado: Colaboradores podem ser associados aos serviços, mas essa ação não é obrigatória.

6. **Salvar a Liberação do Serviço**
   - Localização: Formulário de Ordem de Produção
   - Como fazer: Clique no botão **Salvar** para finalizar a liberação do serviço.
   - Resultado esperado: O serviço é liberado para execução e seu status é atualizado para "Liberado".

7. **Executar o Serviço**
   - Localização: Tela de Acompanhamento de Serviços
   - Como fazer: Após a liberação, os serviços aparecerão na tela de apontamento, onde você poderá iniciar a execução.
   - Resultado esperado: Os serviços liberados estão disponíveis para execução, permitindo o registro de apontamentos.

**Campos e Parâmetros:**

| Campo                        | Tipo         | Obrigatório | Descrição                                                   | Exemplo                |
|------------------------------|--------------|-------------|-----------------------------------------------------------|------------------------|
| Título                       | Texto        | Sim         | Descrição da ordem de produção                             | "Liberação de Alvenaria"|
| Previsão para Início         | Data         | Sim         | Data prevista para o início da execução                   | "01/11/2023"           |
| Previsão para Término        | Data         | Sim         | Data prevista para o término da execução                   | "10/11/2023"           |
| Serviços                     | Seleção      | Sim         | Lista de serviços a serem liberados                       | "Limpeza Geral"        |
| Colaboradores                | Seleção      | Não         | Lista de colaboradores que podem ser associados ao serviço | "João Silva"           |

**Regras de Negócio:**
- Os serviços devem ser liberados antes de sua execução.
- A liberação pode ser parcial, dependendo da unidade de medida do serviço.
- A associação de colaboradores é opcional, mas facilita a gestão de execução.

**Observações Importantes:**
- Os campos de previsão são informativos e não impactam o sistema inicialmente.
- É importante verificar se os colaboradores têm os cargos adequados para serem alocados aos serviços.

**Conceitos-Chave:**
- **Liberação de Serviços**: Processo de autorizar a execução de serviços planejados.
- **Apontamento**: Registro da execução dos serviços liberados.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como eu libero um serviço para execução no sistema?
- Quais informações são necessárias para liberar um serviço?
- É possível associar colaboradores a um serviço liberado?

---


---


---

## 13. Início e Controle de Serviços de Alvenaria

**📋 METADADOS:**
- **ID:** sec_13
- **⏱️ Minutagem:** 30:39 → 33:11
- **⏲️ Duração:** 152s
- **🎬 Link:** [Assistir este trecho](https://www.youtube.com/watch?v=BdLq4eBgfxQ&list=PLrsGJiMcdclnlo9exwzyqZC_e09rt5om8&index=4&t=1839)
- **📦 Módulo:** Gestão de Serviços
- **🏷️ Categorias:** Operacional, Controle de Serviços, Alvenaria
- **🔑 Palavras-chave:** alvenaria, iniciar serviço, parar serviço, percentual executado, status do serviço

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como iniciar e controlar serviços de alvenaria no sistema, incluindo a definição de horários, a seleção de colaboradores e o registro do progresso do serviço.

**Contexto:**
Estamos na interface de gestão de serviços de alvenaria, onde o usuário pode iniciar, pausar e finalizar serviços, além de registrar o progresso e as observações pertinentes.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Gestão de Serviços > Submenu Alvenaria
- Tela/interface específica: Tela de Controle de Serviços de Alvenaria

**Funcionalidade Detalhada:**
Esta funcionalidade permite ao usuário iniciar um serviço de alvenaria, registrar o horário de início, associar colaboradores, pausar o serviço e registrar o percentual de execução. O sistema valida as datas de início e liberação, garantindo que não seja possível iniciar um serviço antes da data de liberação.

### 🔹 Passo a Passo Detalhado:

1. **Iniciar Serviço**
   - Localização: Tela de Controle de Serviços de Alvenaria
   - Como fazer: Clique no botão **Iniciar Serviço**. Em seguida, insira a data e o horário de início no campo correspondente.
   - Campos/Opções disponíveis:
     * `Data de Início`: Campo de data (formato: DD/MM/AAAA)
     * `Horário de Início`: Campo de horário (formato: HH:MM)
   - Resultado esperado: O serviço é iniciado e o horário de início é registrado. Se a data e o horário forem anteriores à data de liberação, uma mensagem de erro será exibida.

2. **Selecionar Colaborador**
   - Localização: Após iniciar o serviço, o colaborador associado aparecerá automaticamente.
   - Como fazer: Se desejar alterar o colaborador, clique no campo de seleção de colaboradores e escolha um novo colaborador na lista.
   - Observações importantes: O colaborador deve estar previamente cadastrado no sistema.
   - Resultado esperado: O colaborador selecionado é atualizado no registro do serviço.

3. **Parar Serviço**
   - Localização: Tela de Controle de Serviços de Alvenaria
   - Como fazer: Clique no botão **Parar Serviço**. Insira o horário em que o serviço foi parado e adicione uma observação no campo de comentários.
   - Campos/Opções disponíveis:
     * `Horário de Parada`: Campo de horário (formato: HH:MM)
     * `Observação`: Campo de texto livre
   - Resultado esperado: O serviço é pausado, o horário de parada é registrado e a observação é salva.

4. **Registrar Percentual Executado**
   - Localização: Tela de Controle de Serviços de Alvenaria
   - Como fazer: No campo de percentual executado, insira o valor correspondente ao progresso do serviço.
   - Campos/Opções disponíveis:
     * `Percentual Executado`: Campo numérico (0 a 100)
   - Resultado esperado: O percentual executado é atualizado e refletido no acompanhamento da obra.

5. **Finalizar Serviço**
   - Localização: Tela de Controle de Serviços de Alvenaria
   - Como fazer: Clique no botão **Finalizar Serviço** após a conclusão do trabalho.
   - Observações importantes: O status do serviço mudará para "Finalizado".
   - Resultado esperado: O serviço é marcado como finalizado e não pode ser editado posteriormente.

**Campos e Parâmetros:**

| Campo                   | Tipo         | Obrigatório | Descrição                                         | Exemplo        |
|-------------------------|--------------|-------------|---------------------------------------------------|----------------|
| `Data de Início`       | Data         | Sim         | Data em que o serviço é iniciado                  | 29/10/2023     |
| `Horário de Início`    | Horário      | Sim         | Horário em que o serviço é iniciado               | 08:00          |
| `Colaborador`           | Seleção      | Não         | Colaborador associado ao serviço                   | João da Silva  |
| `Horário de Parada`    | Horário      | Sim         | Horário em que o serviço é parado                 | 10:00          |
| `Observação`           | Texto livre   | Não         | Observações sobre o serviço pausado                | "Parada para almoço" |
| `Percentual Executado`  | Numérico     | Sim         | Percentual de conclusão do serviço                 | 30             |
| `Status do Serviço`     | Texto        | Não         | Indica se o serviço está "Iniciado", "Parado" ou "Finalizado" | "Parado"       |

**Regras de Negócio:**
- Não é permitido iniciar um serviço com uma data de início anterior à data de liberação.
- O percentual executado deve ser um valor entre 0 e 100.
- O status do serviço deve ser atualizado conforme as ações realizadas (Iniciado, Parado, Finalizado).

**Observações Importantes:**
- Os usuários podem optar por registrar o progresso do serviço de forma diária, semanal ou mensal, dependendo da organização de cada cliente.
- É importante que os usuários verifiquem as datas de liberação antes de iniciar um serviço para evitar erros.

**Conceitos-Chave:**
- **Alvenaria**: Estrutura de construção feita com blocos ou tijolos.
- **Percentual Executado**: Medida que indica a fração do serviço que foi completada.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como iniciar um serviço de alvenaria no sistema?
- O que fazer se a data de início for anterior à data de liberação?
- Como registrar o percentual de execução de um serviço de alvenaria?

---


---


---

## 14. Comparativo de Cronograma e Atualização de Execução

**📋 METADADOS:**
- **ID:** sec_14
- **⏱️ Minutagem:** 33:11 → 35:43
- **⏲️ Duração:** 151s
- **🎬 Link:** [Assistir este trecho](https://www.youtube.com/watch?v=BdLq4eBgfxQ&list=PLrsGJiMcdclnlo9exwzyqZC_e09rt5om8&index=4&t=1991)
- **📦 Módulo:** Cronograma
- **🏷️ Categorias:** Planejamento, Execução, Relatório
- **🔑 Palavras-chave:** cronograma, comparativo, execução, atualização, ordem de compra

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como utilizar a funcionalidade de comparativo no cronograma, permitindo que o usuário acompanhe a execução de tarefas em relação ao planejamento inicial, além de atualizar informações sobre a execução e suas implicações no gráfico do cronograma.

**Contexto:**
Estamos na interface do módulo de **Cronograma**, onde o usuário pode visualizar e comparar o planejamento das atividades com a execução real. O objetivo é garantir que as atividades estejam sendo realizadas conforme o cronograma estabelecido e fazer ajustes quando necessário.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Cronograma > Tela de Comparativo
- Tela/interface específica: Tela de Comparativo do Cronograma

**Funcionalidade Detalhada:**
A funcionalidade de comparativo no cronograma permite que o usuário visualize a diferença entre o planejamento e a execução das atividades. O gráfico do cronograma se atualiza automaticamente conforme o usuário insere dados sobre a execução, como datas de início e término das atividades. Essa funcionalidade é essencial para monitorar o progresso e ajustar o planejamento conforme necessário.

### 🔹 Passo a Passo Detalhado:

1. **Visualizar o Comparativo**
   - Localização: Tela de Comparativo do Cronograma
   - Como fazer: O usuário deve acessar a tela de comparativo e observar o gráfico que representa as datas planejadas e as datas de execução.
   - Resultado esperado: O gráfico exibirá as datas planejadas e as datas reais de execução, permitindo uma análise visual do progresso.

2. **Editar a Data de Execução**
   - Localização: Seção de apontamento na tela de comparativo
   - Como fazer: O usuário deve clicar no botão de **Editar** ao lado da data de execução. Em seguida, deve inserir a nova data no campo correspondente.
   - Campos/Opções disponíveis:
     * `Data de Término Planejada`: Campo onde se insere a data planejada para a finalização da atividade.
     * `Data de Término Real`: Campo onde se insere a data em que a atividade foi realmente finalizada.
   - Resultado esperado: Após a edição, o gráfico do cronograma deve atualizar automaticamente para refletir as novas datas.

3. **Finalizar a Atividade**
   - Localização: Seção de apontamento na tela de comparativo
   - Como fazer: Após editar a data, o usuário deve clicar no botão **Finalizar** para confirmar a conclusão da atividade.
   - Observações importantes: É necessário que todas as informações estejam corretas antes de finalizar, pois a atualização do gráfico depende da finalização da atividade.
   - Resultado esperado: O gráfico do cronograma será atualizado para refletir a nova data de término, permitindo uma visualização precisa do progresso.

4. **Acessar o Cronograma Financeiro**
   - Localização: Subaba do cronograma
   - Como fazer: O usuário deve navegar até a subaba **Cronograma Financeiro** dentro do módulo de cronograma.
   - Resultado esperado: O sistema exibirá informações financeiras vinculadas às ordens de compra e ordens de serviço, permitindo uma análise detalhada das despesas.

5. **Criar uma Ordem de Compra**
   - Localização: Tela de criação de ordem de compra
   - Como fazer: O usuário deve clicar no botão **Criar Ordem de Compra** e preencher os campos necessários.
   - Campos/Opções disponíveis:
     * `Descrição`: Campo onde se insere a descrição do item (ex: argamassa).
     * `Valor`: Campo onde se insere o valor da ordem de compra.
   - Resultado esperado: A nova ordem de compra será criada e vinculada ao cronograma, permitindo que as despesas sejam contabilizadas.

**Campos e Parâmetros:**

| Campo                       | Tipo      | Obrigatório | Descrição                                           | Exemplo             |
|-----------------------------|-----------|-------------|-----------------------------------------------------|---------------------|
| Data de Término Planejada   | Data      | Sim         | Data planejada para a finalização da atividade      | 08/10/2023          |
| Data de Término Real        | Data      | Sim         | Data em que a atividade foi realmente finalizada    | 17/10/2023          |
| Descrição                   | Texto     | Sim         | Descrição do item na ordem de compra                | Argamassa           |
| Valor                       | Moeda     | Sim         | Valor associado à ordem de compra                    | R$ 500,00           |

**Regras de Negócio:**
- O gráfico do cronograma só se atualiza após a finalização da atividade.
- As ordens de compra devem estar vinculadas às ordens de serviço para que as despesas sejam contabilizadas corretamente.
- As datas de execução devem ser inseridas corretamente para que o comparativo reflita a realidade.

**Observações Importantes:**
- É recomendável revisar todas as informações antes de finalizar uma atividade.
- Erros comuns incluem a inserção de datas incorretas ou a não finalização de atividades, o que impede a atualização do gráfico.
- As ordens de compra devem ser criadas de forma a garantir que todas as despesas sejam registradas no cronograma financeiro.

**Conceitos-Chave:**
- **Cronograma Financeiro**: Seção do sistema que vincula despesas às ordens de compra e ordens de serviço.
- **Comparativo**: Ferramenta que permite visualizar a diferença entre o planejamento e a execução das atividades.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso visualizar o comparativo entre o planejado e o executado no cronograma?
- O que acontece quando eu edito a data de execução de uma atividade?
- Como as ordens de compra afetam o cronograma financeiro?

---


---


---

## 15. Lançamento de Insumos e Associações de Notas Fiscais

**📋 METADADOS:**
- **ID:** sec_15
- **⏱️ Minutagem:** 35:43 → 38:16
- **⏲️ Duração:** 152s
- **🎬 Link:** [Assistir este trecho](https://www.youtube.com/watch?v=BdLq4eBgfxQ&list=PLrsGJiMcdclnlo9exwzyqZC_e09rt5om8&index=4&t=2143)
- **📦 Módulo:** Gestão de Compras
- **🏷️ Categorias:** Operacional, Relatório, Finanças
- **🔑 Palavras-chave:** insumo, nota fiscal, ordem de compra, planejamento, orçamento

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de lançamento de insumos no sistema, incluindo a associação de notas fiscais a ordens de compra. O objetivo é garantir que os usuários possam registrar corretamente as compras e monitorar o impacto financeiro em tempo real.

**Contexto:**
Estamos na interface do módulo de Gestão de Compras, onde o usuário pode registrar a compra de insumos e associá-los a ordens de compra. O foco é garantir que as informações financeiras sejam atualizadas e que o planejamento orçamentário seja monitorado.

**Localização no Sistema:**
- Caminho de navegação: Menu Principal > Gestão de Compras > Lançamento de Insumos
- Tela/interface específica: Tela de Lançamento de Insumos

**Funcionalidade Detalhada:**

A funcionalidade permite que o usuário registre a quantidade de insumos a serem comprados, insira o valor unitário, associe a compra a um parceiro e registre a nota fiscal correspondente. Isso é essencial para manter o controle financeiro e orçamentário da obra.

### 🔹 Passo a Passo Detalhado:

1. **Registro da Quantidade de Insumos**
   - Localização: Campo de entrada de quantidade na tela de Lançamento de Insumos.
   - Como fazer: Clique no campo de entrada e digite a quantidade desejada. Por exemplo, para a compra de 500 m³, digite `100`.
   - Campos/Opções disponíveis:
     * `Quantidade`: Campo numérico onde o usuário insere a quantidade de insumos a ser comprada.
   - Resultado esperado: A quantidade inserida é registrada no sistema.

2. **Inserção do Valor Unitário**
   - Localização: Campo de entrada de valor unitário na mesma tela.
   - Como fazer: Clique no campo de entrada e insira o valor unitário do insumo. Por exemplo, insira `R$ 41`.
   - Resultado esperado: O valor unitário é salvo e utilizado para calcular o valor total.

3. **Associação a um Parceiro**
   - Localização: Menu suspenso ou campo de seleção para parceiros.
   - Como fazer: Selecione o parceiro com o qual a compra será associada. Isso pode ser feito clicando no menu suspenso e escolhendo o parceiro desejado.
   - Resultado esperado: O parceiro selecionado é associado à compra.

4. **Cálculo do Valor Total**
   - Localização: Campo de exibição do valor total.
   - Como fazer: O sistema calcula automaticamente o valor total com base na quantidade e no valor unitário inseridos. Por exemplo, se a quantidade é `100` e o valor unitário é `R$ 41`, o valor total será `R$ 4100`.
   - Resultado esperado: O valor total é exibido corretamente.

5. **Lançamento da Nota Fiscal**
   - Localização: Botão de "Lançar Nota" na tela.
   - Como fazer: Clique no botão **Lançar Nota** para registrar a nota fiscal associada à ordem de compra.
   - Observações importantes: Certifique-se de que todos os campos obrigatórios estejam preenchidos antes de clicar no botão.
   - Resultado esperado: A nota fiscal é registrada e associada à ordem de compra.

6. **Visualização no Cronograma Financeiro**
   - Localização: Acesso ao cronograma financeiro na interface do sistema.
   - Como fazer: Navegue até a seção de cronograma financeiro e verifique se o valor referente ao mês foi atualizado.
   - Resultado esperado: O valor total de `R$ 4100` aparece no cronograma financeiro, permitindo a visualização do planejado versus o real executado.

7. **Análise de Recursos Alocados**
   - Localização: Aba de recursos alocados na tela de Lançamento de Insumos.
   - Como fazer: Verifique a aba para visualizar a quantidade de insumos comprados e a média de compras.
   - Resultado esperado: O sistema mostra se o orçamento está sendo extrapolado, com informações como o valor unitário planejado e o valor médio de compra.

**Campos e Parâmetros:**

| Campo                   | Tipo      | Obrigatório | Descrição                                           | Exemplo          |
|-------------------------|-----------|-------------|----------------------------------------------------|------------------|
| `Quantidade`            | Numérico  | Sim         | Quantidade de insumos a ser comprada               | `100`            |
| `Valor Unitário`        | Moeda     | Sim         | Valor unitário do insumo                            | `R$ 41`          |
| `Parceiro`              | Seleção   | Sim         | Parceiro associado à compra                         | `Fornecedor X`   |
| `Valor Total`           | Moeda     | Não         | Cálculo automático do valor total                   | `R$ 4100`        |
| `Nota Fiscal`           | Texto     | Sim         | Registro da nota fiscal associada à compra          | `NF 12345`       |

**Regras de Negócio:**
- O valor total é calculado multiplicando a `Quantidade` pelo `Valor Unitário`.
- A nota fiscal deve ser lançada para que a compra seja considerada válida.
- O sistema deve alertar se o valor médio de compra extrapolar o orçamento planejado.

**Observações Importantes:**
- Verifique sempre se todos os campos obrigatórios estão preenchidos antes de finalizar o lançamento.
- Erros comuns incluem a inserção de valores incorretos ou a não associação de um parceiro.
- É importante monitorar o cronograma financeiro para evitar surpresas no orçamento.

**Conceitos-Chave:**
- **Orçamento**: Limite financeiro estabelecido para a compra de insumos.
- **Nota Fiscal**: Documento que comprova a compra e deve ser registrado no sistema.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como registro a quantidade de insumos que quero comprar?
- O que devo fazer para associar uma nota fiscal a uma ordem de compra?
- Como posso verificar se estou extrapolando meu orçamento com os insumos comprados?

---


---


---

## 16. Criação de Ordens de Serviço e Medições

**📋 METADADOS:**
- **ID:** sec_16
- **⏱️ Minutagem:** 38:13 → 40:46
- **⏲️ Duração:** 152s
- **🎬 Link:** [Assistir este trecho](https://www.youtube.com/watch?v=BdLq4eBgfxQ&list=PLrsGJiMcdclnlo9exwzyqZC_e09rt5om8&index=4&t=2293)
- **📦 Módulo:** Acompanhamento de Obras
- **🏷️ Categorias:** Operacional, Gestão de Serviços, Controle de Obras
- **🔑 Palavras-chave:** ordem de serviço, medições, prestador de serviço, pagamento, cronograma

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de criação de ordens de serviço e medições no sistema, explicando as diferenças entre elas e como utilizá-las de forma eficaz para gerenciar serviços contratados.

**Contexto:**
Estamos no módulo de Acompanhamento de Obras, onde o usuário pode gerenciar serviços e materiais necessários para a execução de um projeto. O objetivo desta seção é ensinar como criar ordens de serviço e medições, destacando suas diferenças e aplicações.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Acompanhamento de Obras > Subaba de Serviços
- Tela/interface específica: Tela de Criação de Ordens de Serviço e Medições

**Funcionalidade Detalhada:**
A funcionalidade permite ao usuário criar ordens de serviço e medições para gerenciar serviços contratados. A **ordem de serviço** é utilizada quando o usuário já possui informações fixas sobre o pagamento ao prestador, enquanto as **medições** são usadas quando essas informações não estão definidas e dependem da execução do serviço.

### 🔹 Passo a Passo Detalhado:

1. **Acessar a Subaba de Serviços**
   - Localização: Menu Principal > Acompanhamento de Obras > Subaba de Serviços
   - Como fazer: Clique na subaba "Serviços" para acessar as opções de criação de ordens de serviço e medições.
   - Resultado esperado: A interface de serviços será exibida, permitindo a criação de novas ordens de serviço ou medições.

2. **Criar uma Ordem de Serviço**
   - Localização: Tela de Criação de Ordens de Serviço
   - Como fazer: Clique no botão "Criar Ordem de Serviço".
   - Campos/Opções disponíveis:
     * `Descrição`: Campo de texto para adicionar uma descrição ou orientação sobre o serviço.
     * `Data Inicial`: Campo de data que puxa automaticamente a data do cronograma.
     * `Data Final`: Campo de data que também puxa automaticamente a data do cronograma.
     * `Quantidade`: Campo numérico que indica a quantidade de serviço a ser executado.
     * `Valor Unitário`: Campo numérico que indica o valor por unidade do serviço.
   - Resultado esperado: Uma nova ordem de serviço é criada com as informações inseridas.

3. **Criar uma Medição**
   - Localização: Tela de Criação de Medições
   - Como fazer: Clique no botão "Criar Medição".
   - Observações importantes: As medições são utilizadas quando não se tem certeza do valor ou da data de pagamento ao prestador.
   - Resultado esperado: Uma nova medição é criada, permitindo o acompanhamento do serviço conforme a execução.

4. **Visualizar Recursos Disponíveis**
   - Localização: Tela de Criação de Ordens de Serviço e Medições
   - Como fazer: Ao criar uma ordem de serviço, o sistema automaticamente filtra e exibe apenas os serviços, recursos ou materiais que estão alocados à obra específica.
   - Resultado esperado: Apenas os serviços planejados e alocados para a obra atual são exibidos.

5. **Alterar Valores e Quantidades**
   - Localização: Tela de Criação de Ordens de Serviço
   - Como fazer: Após preencher os campos, o usuário pode alterar a `Quantidade` e o `Valor Unitário` conforme necessário.
   - Resultado esperado: As alterações são salvas e refletidas na ordem de serviço.

**Campos e Parâmetros:**

| Campo            | Tipo        | Obrigatório | Descrição                                               | Exemplo      |
|------------------|-------------|-------------|---------------------------------------------------------|--------------|
| `Descrição`      | Texto       | Sim         | Descrição ou orientação sobre o serviço.                | "Serviço de alvenaria" |
| `Data Inicial`   | Data        | Sim         | Data de início do serviço, puxada do cronograma.       | "01/01/2023" |
| `Data Final`     | Data        | Sim         | Data de término do serviço, puxada do cronograma.      | "10/01/2023" |
| `Quantidade`     | Numérico    | Sim         | Quantidade do serviço a ser executado.                 | "1000"       |
| `Valor Unitário` | Numérico    | Sim         | Valor por unidade do serviço.                            | "50"         |

**Regras de Negócio:**
- As ordens de serviço são criadas quando o usuário já possui condições fixas definidas para pagamento.
- As medições são criadas quando o pagamento depende da execução do serviço.
- Ao criar ordens de serviço, o sistema filtra apenas os serviços alocados à obra em questão.

**Observações Importantes:**
- É importante verificar se as informações de cronograma estão corretas antes de criar ordens de serviço.
- Evite criar medições desnecessárias, pois elas podem complicar o acompanhamento do serviço.

**Conceitos-Chave:**
- **Ordem de Serviço**: Documento que formaliza a contratação de um prestador de serviço com valores e datas fixas.
- **Medição**: Processo de acompanhamento de serviços onde os valores e datas de pagamento são definidos conforme a execução.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Qual a diferença entre uma ordem de serviço e uma medição?
- Como posso criar uma ordem de serviço no sistema?
- O que devo fazer se não souber o valor a ser pago ao prestador de serviço?

---


---


---

## 17. Emissão e Gestão de Contratos e Medições

**📋 METADADOS:**
- **ID:** sec_17
- **⏱️ Minutagem:** 40:44 → 43:16
- **⏲️ Duração:** 151s
- **🎬 Link:** [Assistir este trecho](https://www.youtube.com/watch?v=BdLq4eBgfxQ&list=PLrsGJiMcdclnlo9exwzyqZC_e09rt5om8&index=4&t=2444)
- **📦 Módulo:** Administração
- **🏷️ Categorias:** Contratos, Medições, Financeiro, Prestadores
- **🔑 Palavras-chave:** contrato, prestador, medição, valor total, quantidade, editar, assinar

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de emissão de contratos e a gestão de medições no sistema, permitindo que o usuário registre e controle os serviços prestados, além de associar pagamentos e gerenciar alterações contratuais.

**Contexto:**
Estamos na interface do sistema responsável pela gestão de contratos e medições, onde o usuário pode emitir contratos para prestadores de serviços e registrar medições de serviços realizados.

**Localização no Sistema:**
- Caminho de navegação: Menu Principal > Módulo Administração > Submenu Contratos e Medições
- Tela/interface específica: Tela de Emissão de Contratos e Registro de Medições

**Funcionalidade Detalhada:**
A funcionalidade permite ao usuário emitir contratos para prestadores de serviços, registrar medições de serviços executados e gerenciar informações contratuais. O sistema calcula automaticamente o valor total a ser pago com base na quantidade de serviços e no valor unitário. O usuário pode também editar informações do contrato antes de ser assinado e gerar aditivos após a assinatura.

### 🔹 Passo a Passo Detalhado:

1. **Inserir Quantidade e Calcular Valor Total**
   - Localização: Tela de Emissão de Contratos
   - Como fazer: O usuário deve inserir a quantidade de serviços a serem contratados no campo correspondente.
   - Campos/Opções disponíveis:
     * `Quantidade`: Campo numérico onde o usuário insere a quantidade de serviços (ex: 100).
     * `Valor Unitário`: Campo que exibe o valor unitário do serviço.
   - Resultado esperado: O sistema multiplica a `Quantidade` pelo `Valor Unitário` e exibe o `Valor Total` a ser pago pelo prestador.

2. **Selecionar Prestador**
   - Localização: Tela de Emissão de Contratos
   - Como fazer: O usuário deve selecionar o prestador que irá executar o serviço a partir de um dropdown.
   - Observações importantes: O prestador deve estar previamente cadastrado no sistema.
   - Resultado esperado: O prestador selecionado é associado ao contrato.

3. **Definir Pagamento a Prazo**
   - Localização: Tela de Emissão de Contratos
   - Como fazer: O usuário deve inserir a quantidade de vezes que irá pagar ao prestador, caso o pagamento seja a prazo.
   - Resultado esperado: O sistema registra a quantidade de parcelas para o pagamento.

4. **Emitir Contrato**
   - Localização: Tela de Emissão de Contratos
   - Como fazer: Após preencher todas as informações, o usuário deve clicar no botão **Emitir Contrato**.
   - Resultado esperado: O contrato é gerado e aparece na lista de contratos emitidos.

5. **Imprimir e Assinar Contrato**
   - Localização: Tela de Contratos Emitidos
   - Como fazer: O usuário pode clicar no botão **Imprimir** para gerar uma cópia do contrato para o prestador assinar.
   - Resultado esperado: O contrato impresso pode ser assinado pelo prestador.

6. **Importar Contrato Assinado**
   - Localização: Tela de Contratos Emitidos
   - Como fazer: Após o prestador assinar, o usuário deve clicar no botão **Assinar Contrato** para importar o contrato assinado.
   - Resultado esperado: O contrato agora está registrado como assinado no sistema.

7. **Editar Contrato**
   - Localização: Tela de Contratos Emitidos
   - Como fazer: O usuário pode selecionar o contrato e clicar na opção **Editar** para modificar informações como serviços, quantidade ou valor unitário.
   - Observações importantes: A edição só é permitida enquanto o contrato estiver com status "Emitido".
   - Resultado esperado: As informações do contrato são atualizadas conforme as alterações feitas.

8. **Gerar Medição**
   - Localização: Tela de Emissão de Contratos
   - Como fazer: O usuário deve clicar em **Mais Medição** e associar a medição ao contrato recém-emitido.
   - Resultado esperado: A medição é criada e associada ao contrato.

9. **Registrar Quantidade Medida**
   - Localização: Tela de Medições
   - Como fazer: O usuário deve inserir a quantidade medida no campo correspondente.
   - Observações importantes: O sistema exibirá a quantidade planejada conforme o contrato e a quantidade acumulada anteriormente.
   - Resultado esperado: A quantidade medida é registrada e salva no sistema.

**Campos e Parâmetros:**

| Campo                | Tipo       | Obrigatório | Descrição                                              | Exemplo     |
|----------------------|------------|-------------|-------------------------------------------------------|-------------|
| `Quantidade`         | Numérico   | Sim         | Número de serviços a serem contratados                | 100         |
| `Valor Unitário`     | Monetário  | Sim         | Valor individual de cada serviço                       | R$ 50,00    |
| `Prestador`          | Dropdown   | Sim         | Seleção do prestador que irá executar o serviço       | Prestador A |
| `Quantidade de Parcelas` | Numérico | Não         | Número de vezes que o pagamento será realizado         | 3           |
| `Modelo de Contrato` | Dropdown   | Sim         | Seleção do modelo de contrato a ser utilizado          | Modelo 1    |

**Regras de Negócio:**
- O valor total é calculado automaticamente ao inserir a quantidade e o valor unitário.
- O prestador deve estar cadastrado no sistema para ser selecionado.
- A edição do contrato é permitida apenas enquanto o status for "Emitido".
- Após a assinatura do contrato, somente aditivos podem ser criados.

**Observações Importantes:**
- É recomendável revisar todas as informações antes de emitir o contrato.
- Evitar editar contratos já assinados, pois isso pode gerar inconsistências.
- Certifique-se de que o prestador assine o contrato impresso antes de importar.

**Conceitos-Chave:**
- **Contrato**: Documento que formaliza a prestação de serviços entre o contratante e o prestador.
- **Medição**: Registro da quantidade de serviços efetivamente realizados, que será utilizado para o pagamento.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como emitir um contrato para um prestador de serviços?
- O que fazer se precisar editar um contrato já emitido?
- Como registrar a medição de serviços realizados?

---


---


---

## 18. Medição de Serviços e Liberação Financeira

**📋 METADADOS:**
- **ID:** sec_18
- **⏱️ Minutagem:** 43:15 → 45:48
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://www.youtube.com/watch?v=BdLq4eBgfxQ&list=PLrsGJiMcdclnlo9exwzyqZC_e09rt5om8&index=4&t=2595)
- **📦 Módulo:** Medições e Financeiro
- **🏷️ Categorias:** Medição, Liberação Financeira, Contratos, Serviços
- **🔑 Palavras-chave:** medição, alvenaria, valor a pagar, valor a receber, liberação financeira

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de medição de serviços prestados, especificamente para o serviço de alvenaria, e a subsequente liberação financeira, incluindo a aprovação e o registro de valores a pagar e a receber.

**Contexto:**
Estamos na etapa de registro de medições de serviços prestados por um prestador, onde o usuário insere a quantidade de serviços realizados e aprova a medição para gerar os valores financeiros correspondentes.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Medições e Financeiro > Submenu Medições
- Tela/interface específica: Tela de Registro de Medições

**Funcionalidade Detalhada:**
A funcionalidade permite ao usuário registrar a quantidade de serviços realizados, calcular automaticamente os valores a pagar e a receber, e aprovar a medição. O sistema também possibilita a liberação financeira, onde o usuário pode associar contratos e definir datas de vencimento para pagamentos.

### 🔹 Passo a Passo Detalhado:

1. **Registro da Medição**
   - Localização: Tela de Registro de Medições
   - Como fazer: O usuário deve inserir a quantidade de serviços realizados. Por exemplo, para o serviço de alvenaria, o usuário seleciona a forma de medição como "por bloco" e insere a quantidade de blocos executados.
   - Campos/Opções disponíveis:
     * `Quantidade Medida`: Campo numérico onde o usuário insere a quantidade de serviços realizados (ex: 2 blocos).
     * `Forma de Medição`: Dropdown onde o usuário seleciona a forma de medição (ex: "por bloco").
   - Resultado esperado: O sistema calcula automaticamente o valor a pagar e o valor a receber com base nas informações do contrato e no planejamento da obra.

2. **Finalização da Medição**
   - Localização: Tela de Registro de Medições
   - Como fazer: Após inserir os dados, o usuário clica no botão **Salvar** para finalizar a medição.
   - Observações importantes: O usuário pode optar por imprimir a medição, selecionando se deseja incluir apenas a quantidade ou também os valores.
   - Resultado esperado: A medição é salva e está pronta para ser aprovada.

3. **Aprovação da Medição**
   - Localização: Tela de Registro de Medições
   - Como fazer: O usuário clica no botão **Aprovar** para aprovar a medição registrada.
   - Resultado esperado: A medição é aprovada, mas ainda não gera contas a pagar ou a receber até que a liberação financeira seja realizada.

4. **Liberação Financeira**
   - Localização: Menu Principal > Módulo Medições e Financeiro > Submenu Liberações Financeiras
   - Como fazer: O usuário acessa a tela de liberações financeiras e associa o contrato referente à medição aprovada.
   - Campos/Opções disponíveis:
     * `Contrato`: Campo onde o usuário seleciona o contrato associado à medição.
     * `Serviços Medidos`: Lista de serviços que foram medidos, onde o usuário pode optar por liberar todos ou apenas alguns.
     * `Retenção`: Campo numérico para inserir valores de retenção, se necessário.
     * `Desconto`: Campo numérico para inserir valores de desconto, se necessário.
     * `Adiantamento`: Campo numérico para inserir valores de adiantamento, se necessário.
     * `Classificação Financeira`: Dropdown para selecionar a classificação financeira da liberação.
     * `Data de Vencimento`: Campo de data para definir até quando o pagamento deve ser realizado.
   - Resultado esperado: A liberação financeira é concluída, e o usuário é redirecionado para a tela de contas a pagar.

**Campos e Parâmetros:**

| Campo                     | Tipo       | Obrigatório | Descrição                                               | Exemplo          |
|---------------------------|------------|-------------|---------------------------------------------------------|------------------|
| Quantidade Medida         | Numérico   | Sim         | Quantidade de serviços realizados                        | 2 blocos         |
| Forma de Medição          | Dropdown   | Sim         | Método de medição utilizado (ex: por bloco)             | por bloco        |
| Contrato                  | Dropdown   | Sim         | Seleção do contrato associado à medição                  | Contrato 123     |
| Serviços Medidos           | Lista      | Sim         | Lista de serviços que foram medidos                     | Alvenaria        |
| Retenção                  | Numérico   | Não         | Valor de retenção a ser aplicado                        | 10%              |
| Desconto                  | Numérico   | Não         | Valor de desconto a ser aplicado                        | 5%               |
| Adiantamento              | Numérico   | Não         | Valor de adiantamento a ser aplicado                    | 1000             |
| Classificação Financeira   | Dropdown   | Não         | Classificação para controle financeiro                   | Pagamento Pendente|
| Data de Vencimento        | Data       | Sim         | Data limite para o pagamento                            | 30/11/2023       |

**Regras de Negócio:**
- A medição deve ser aprovada antes de gerar contas a pagar ou a receber.
- O valor a pagar é calculado com base no contrato emitido para o prestador.
- O valor a receber é baseado no planejamento da obra.
- A liberação financeira deve ser realizada para que as contas sejam geradas.

**Observações Importantes:**
- O usuário deve garantir que todas as informações estejam corretas antes de finalizar a medição.
- É possível imprimir a medição com diferentes opções de informações.
- A liberação financeira deve ser feita com atenção às datas de vencimento.

**Conceitos-Chave:**
- **Medição**: Processo de registrar a quantidade de serviços realizados para fins de pagamento.
- **Liberação Financeira**: Ato de autorizar o pagamento referente a uma medição aprovada.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como registro a medição de serviços realizados?
- O que acontece após aprovar uma medição?
- Como faço a liberação financeira para um serviço medido?

---


---


---

## 19. Liberação de Recebimentos Financeiros

**📋 METADADOS:**
- **ID:** sec_19
- **⏱️ Minutagem:** 45:45 → 48:14
- **⏲️ Duração:** 148s
- **🎬 Link:** [Assistir este trecho](https://www.youtube.com/watch?v=BdLq4eBgfxQ&list=PLrsGJiMcdclnlo9exwzyqZC_e09rt5om8&index=4&t=2745)
- **📦 Módulo:** Financeiro
- **🏷️ Categorias:** Recebimentos, Gestão Financeira, Operacional
- **🔑 Palavras-chave:** liberar, financeiro, contas a receber, medições, saldo

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como liberar recebimentos financeiros no sistema, permitindo que a empresa receba pagamentos de forma parcial ou total. O processo inclui a definição de datas de vencimento e a visualização dos valores acordados com prestadores.

**Contexto:**
Estamos na subaba **Financeira** do módulo de gestão financeira, onde o usuário pode gerenciar os recebimentos de valores de prestadores de serviços. O objetivo é liberar os pagamentos de forma adequada, garantindo que os valores sejam registrados corretamente no sistema.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Financeiro > Subaba a Receber
- Tela/interface específica: Tela de Recebimentos Financeiros

**Funcionalidade Detalhada:**
A funcionalidade de liberação de recebimentos financeiros permite ao usuário liberar valores a serem recebidos de prestadores. O usuário pode optar por liberar o pagamento total ou parcialmente, além de definir uma data de vencimento para o recebimento. O sistema também permite visualizar o saldo atual e os valores acordados com os prestadores.

### 🔹 Passo a Passo Detalhado:

1. **Acessar a Subaba a Receber**
   - Localização: Menu Principal > Módulo Financeiro > Subaba a Receber
   - Como fazer: Clique na subaba **a Receber** para acessar as informações financeiras relacionadas aos recebimentos.
   - Resultado esperado: A tela de recebimentos financeiros será exibida, mostrando as opções disponíveis.

2. **Visualizar Recebimentos**
   - Localização: Tela de Recebimentos Financeiros
   - Como fazer: Clique no botão **Visualizar** para ver os detalhes dos recebimentos pendentes.
   - Resultado esperado: Uma lista de recebimentos pendentes será exibida, permitindo a seleção do recebimento desejado.

3. **Liberar Recebimento Financeiro**
   - Localização: Após visualizar os recebimentos, clique no botão **Liberar Financeiro**.
   - Como fazer: Selecione a opção de liberar o pagamento total ou parcialmente. Para liberar parcialmente, insira o valor desejado.
   - Campos/Opções disponíveis:
     * `Data de Vencimento`: Campo para inserir a data limite para o recebimento.
   - Resultado esperado: O recebimento será liberado conforme a opção escolhida, e o sistema atualizará o status do recebimento.

4. **Verificar Contas a Receber**
   - Localização: Após a liberação, clique no link que redireciona para **Contas a Receber**.
   - Como fazer: Clique no link para acessar a tela de contas a receber.
   - Resultado esperado: A tela de contas a receber será exibida, mostrando o valor total acordado com o prestador e o valor atual após a liberação.

5. **Visualizar Saldo e Medições**
   - Localização: Tela de Contas a Receber
   - Como fazer: Observe o valor total acordado e o valor já liberado. O saldo restante será exibido.
   - Observações importantes: O saldo é atualizado conforme as medições são realizadas e os valores são liberados.
   - Resultado esperado: O saldo restante será exibido corretamente, refletindo as liberações feitas.

**Campos e Parâmetros:**

| Campo               | Tipo       | Obrigatório | Descrição                                         | Exemplo               |
|---------------------|------------|-------------|---------------------------------------------------|-----------------------|
| Data de Vencimento  | Data       | Sim         | Data limite para o recebimento do pagamento.      | 30/12/2023            |
| Valor Total         | Numérico   | Sim         | Valor total acordado com o prestador.             | R$ 60.000,00          |
| Valor Liberado      | Numérico   | Sim         | Valor que foi liberado para recebimento.          | R$ 5.555,00           |
| Saldo Restante      | Numérico   | Não         | Valor restante a ser recebido após liberações.    | R$ 1.556.619,44       |

**Regras de Negócio:**
- O usuário pode liberar o pagamento total ou parcialmente.
- A data de vencimento deve ser inserida para cada liberação.
- O saldo é atualizado automaticamente conforme as medições são realizadas e os valores são liberados.

**Observações Importantes:**
- É importante verificar o valor total acordado antes de realizar a liberação.
- Erros comuns incluem a inserção de datas de vencimento incorretas ou valores liberados que não correspondem ao acordado.
- Certifique-se de que todas as medições foram registradas corretamente antes de liberar os pagamentos.

**Conceitos-Chave:**
- **Contas a Receber**: Registro financeiro que mostra os valores que a empresa tem a receber de seus prestadores.
- **Medições**: Processo de verificar e registrar o progresso de serviços prestados, que impacta os valores a serem recebidos.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como liberar um recebimento financeiro no sistema?
- Quais informações são necessárias para liberar um pagamento?
- O que acontece com o saldo após a liberação de um recebimento?

---


---


---

## 20. Diário de Obras

**📋 METADADOS:**
- **ID:** sec_20
- **⏱️ Minutagem:** 48:17 → 50:50
- **⏲️ Duração:** 152s
- **🎬 Link:** [Assistir este trecho](https://www.youtube.com/watch?v=BdLq4eBgfxQ&list=PLrsGJiMcdclnlo9exwzyqZC_e09rt5om8&index=4&t=2897)
- **📦 Módulo:** Diário de Obras
- **🏷️ Categorias:** Operacional, Registro, Relatório
- **🔑 Palavras-chave:** diário, obras, interações, registro, clima, serviços

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como utilizar o Diário de Obras, incluindo o registro de interações e informações climáticas, além de como visualizar as ações realizadas em uma obra específica.

**Contexto:**
Estamos no módulo de Diário de Obras, que permite o acompanhamento diário das atividades de uma obra, registrando informações relevantes e interações que ocorrem ao longo do dia.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Diário de Obras
- Tela/interface específica: Tela do Diário de Obras

**Funcionalidade Detalhada:**

O Diário de Obras é uma funcionalidade que permite o registro e acompanhamento das atividades diárias de uma obra. As informações são preenchidas automaticamente com base nas ações realizadas em outros módulos do sistema. Por exemplo, ao cadastrar uma obra, a data de início é registrada e o diário começa a ser preenchido a partir dessa data. Os usuários podem registrar interações e informações climáticas, além de visualizar um resumo das ações realizadas, como ordens de serviço e medições.

### 🔹 Passo a Passo Detalhado:

1. **Visualizar Detalhes do Diário**
   - Localização: Tela do Diário de Obras, botão **Ver mais detalhes**
   - Como fazer: Clique no botão **Ver mais detalhes** para acessar informações gerais sobre a obra.
   - Resultado esperado: As informações gerais são exibidas automaticamente, sem possibilidade de edição diretamente nesta tela.

2. **Registrar Interações**
   - Localização: Tela do Diário de Obras, seção de interações.
   - Como fazer: Clique em **Alterar tipos de interação**, depois clique em **Mais tipo**. Insira a nomenclatura desejada e clique em **Salvar**.
   - Resultado esperado: Um novo tipo de interação é criado e pode ser utilizado para registrar informações pertinentes ao longo do dia.

3. **Registrar uma Interação**
   - Localização: Tela do Diário de Obras, seção de interações, botão **Mais registrar a interação**.
   - Como fazer: Clique na interação desejada e, em seguida, clique em **Mais registrar a interação**. Descreva a interação no campo de texto e clique em **Salvar**.
   - Resultado esperado: A interação é registrada e aparece em ordem cronológica na lista de interações.

4. **Anexar Arquivos**
   - Localização: Tela do Diário de Obras, seção de interações.
   - Como fazer: Durante o registro de uma interação, utilize a opção de anexar imagens ou vídeos diretamente na interação ou na seção de arquivos.
   - Resultado esperado: Os arquivos anexados ficam disponíveis para visualização junto à interação registrada.

**Campos e Parâmetros:**

| Campo                   | Tipo       | Obrigatório | Descrição                                           | Exemplo                |
|-------------------------|------------|-------------|----------------------------------------------------|------------------------|
| Data de Início          | Data       | Sim         | Data em que a obra foi iniciada                    | 29/09/2023             |
| Tipo de Interação       | Texto      | Sim         | Nome da interação que será registrada               | "Reunião de equipe"    |
| Descrição da Interação  | Texto      | Sim         | Detalhes sobre a interação realizada                | "Discussão sobre prazos" |
| Anexos                  | Arquivo    | Não         | Imagens ou vídeos relacionados à interação         | "foto1.jpg"           |

**Regras de Negócio:**
- As informações do diário são preenchidas automaticamente com base nas ações realizadas em outros módulos.
- As interações devem ser registradas em ordem cronológica.
- Cada interação registrada deve ter um código único, data e hora de criação, e o usuário que a registrou.

**Observações Importantes:**
- É importante registrar as interações de forma detalhada para garantir um bom acompanhamento da obra.
- Evite deixar interações sem descrição, pois isso pode dificultar a compreensão futura das atividades realizadas.
- Os arquivos anexados devem ser relevantes e diretamente relacionados à interação registrada.

**Conceitos-Chave:**
- **Diário de Obras**: Registro diário das atividades e interações de uma obra, permitindo acompanhamento e controle.
- **Interação**: Registro de eventos ou ações realizadas durante o dia, que podem incluir reuniões, medições, ou outras atividades relevantes.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso visualizar o diário de uma obra específica?
- O que devo fazer para registrar uma nova interação no diário?
- Como anexo arquivos a uma interação registrada no diário de obras?

---


---


---

## 21. Exportação de Relatórios e Cadastro de Itens

**📋 METADADOS:**
- **ID:** sec_21
- **⏱️ Minutagem:** 50:48 → 53:21
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://www.youtube.com/watch?v=BdLq4eBgfxQ&list=PLrsGJiMcdclnlo9exwzyqZC_e09rt5om8&index=4&t=3048)
- **📦 Módulo:** Acompanhamento de Obras
- **🏷️ Categorias:** Relatório, Cadastro, Operacional
- **🔑 Palavras-chave:** exportar, relatório, diário de obras, cadastro, checklist, composições, insumos, tipos de unidade

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como exportar relatórios do diário de obras em formato PDF e como cadastrar itens como composições, insumos e tipos de unidade no sistema. O objetivo é facilitar a organização e visualização das informações relacionadas às obras.

**Contexto:**
Estamos na interface do módulo de Acompanhamento de Obras, onde o usuário pode gerenciar informações sobre as obras em andamento, incluindo a exportação de relatórios e o cadastro de diferentes itens que compõem o orçamento e a execução dos serviços.

**Localização no Sistema:**
- Caminho de navegação: Menu Principal > Acompanhamento de Obras > Relatórios e Cadastros
- Tela/interface específica: Tela de Acompanhamento de Obras

**Funcionalidade Detalhada:**

A funcionalidade permite ao usuário exportar um relatório do diário de obras em formato PDF, incluindo imagens associadas a cada registro. Além disso, o usuário pode cadastrar composições, insumos, tipos de unidade e itens de checklist, facilitando a organização e a execução das atividades relacionadas à obra.

### 🔹 Passo a Passo Detalhado:

1. **Exportar Relatório do Diário de Obras**
   - Localização: Tela de Acompanhamento de Obras
   - Como fazer: Clique no botão **Exportar Relatório** localizado na parte superior da tela.
   - Campos/Opções disponíveis:
     * `Formato`: PDF (opção única)
   - Resultado esperado: Um relatório em PDF é gerado, contendo todas as informações do diário de obras, incluindo imagens associadas a cada registro.

2. **Gerar Medição e Emitir Contrato**
   - Localização: Tela de Acompanhamento de Obras
   - Como fazer: Clique no botão **Emitir Contrato** ou **Gerar Medição**, que estão disponíveis na seção de contratos e medições.
   - Observações importantes: O processo de emissão de contrato e geração de medição é semelhante ao realizado diretamente no acompanhamento da obra.
   - Resultado esperado: O contrato ou medição é gerado com sucesso, permitindo o acompanhamento das etapas da obra.

3. **Cadastrar Composições e Insumos**
   - Localização: Tela de Cadastro de Composições
   - Como fazer: Clique no botão **Cadastrar Composição** ou **Cadastrar Insumo**.
   - Campos/Opções disponíveis:
     * `Nome da Composição`: Campo de texto para inserir o nome da composição.
     * `Descrição`: Campo de texto para descrever a composição.
   - Resultado esperado: A composição ou insumo é cadastrado com sucesso e fica disponível para uso no orçamento.

4. **Cadastrar Tipos de Unidade**
   - Localização: Tela de Cadastro de Tipos de Unidade
   - Como fazer: Clique no botão **Adicionar Tipo** e insira a nomenclatura desejada.
   - Observações importantes: É possível associar um tipo de unidade, como apartamento, garagem ou sala comercial.
   - Resultado esperado: O tipo de unidade é cadastrado e pode ser utilizado no cadastro da obra.

5. **Criar Itens de Checklist**
   - Localização: Tela de Checklist
   - Como fazer: Clique no botão **Adicionar Item** e insira a nomenclatura do item.
   - Campos/Opções disponíveis:
     * `Nome do Item`: Campo de texto para inserir o nome do checklist.
   - Resultado esperado: O item de checklist é criado e pode ser associado à execução de serviços.

6. **Realizar Checklist Antes da Execução do Serviço**
   - Localização: Tela de Execução de Serviços
   - Como fazer: Antes de iniciar o serviço, selecione a opção **Realizar Checklist**.
   - Observações importantes: É possível indicar se está tudo em conformidade, se foi aprovado ou reprovado, e anexar um arquivo, mas isso não impede a execução do serviço.
   - Resultado esperado: O checklist é registrado, permitindo um controle de conformidade antes da execução do serviço.

**Campos e Parâmetros:**

| Campo                   | Tipo       | Obrigatório | Descrição                                           | Exemplo                |
|-------------------------|------------|-------------|----------------------------------------------------|------------------------|
| Nome da Composição      | Texto      | Sim         | Nome da composição a ser cadastrada                 | "Composição A"         |
| Descrição               | Texto      | Não         | Descrição detalhada da composição                   | "Descrição da Composição A" |
| Nome do Item de Checklist| Texto     | Sim         | Nome do item a ser adicionado ao checklist         | "Verificação de Segurança" |
| Tipo de Unidade         | Texto      | Sim         | Nome do tipo de unidade a ser cadastrado           | "Apartamento"          |

**Regras de Negócio:**
- O relatório do diário de obras é gerado em formato PDF e inclui imagens.
- A geração de medições e contratos pode ser feita diretamente na tela de acompanhamento.
- Os itens de checklist podem ser criados e associados a serviços, mas não impedem a execução do serviço.

**Observações Importantes:**
- É recomendável revisar os dados antes de exportar o relatório para garantir que todas as informações estejam corretas.
- Ao cadastrar composições e insumos, certifique-se de que os nomes sejam descritivos para facilitar a identificação futura.
- Erros comuns incluem não preencher campos obrigatórios ao cadastrar novos itens.

**Conceitos-Chave:**
- **Checklist**: Um conjunto de itens que devem ser verificados antes da execução de um serviço.
- **Composição**: Conjunto de insumos e serviços que compõem uma parte do orçamento de uma obra.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como exportar um relatório do diário de obras?
- Quais são os passos para cadastrar composições e insumos?
- Como criar e utilizar itens de checklist no sistema?

---


---


---

## 22. Registro de Treinamento do Módulo de Engenharia

**📋 METADADOS:**
- **ID:** sec_22
- **⏱️ Minutagem:** 53:19 → 53:32
- **⏲️ Duração:** 12s
- **🎬 Link:** [Assistir este trecho](https://www.youtube.com/watch?v=BdLq4eBgfxQ&list=PLrsGJiMcdclnlo9exwzyqZC_e09rt5om8&index=4&t=3199)
- **📦 Módulo:** Engenharia
- **🏷️ Categorias:** Treinamento, Documentação, Suporte
- **🔑 Palavras-chave:** registro, treinamento, módulo, engenharia, COPER

> **🔍 RESUMO EXECUTIVO:** Esta seção aborda a finalização do treinamento do módulo de engenharia, destacando a importância de registrar as informações discutidas e a disponibilidade de suporte através do COPER.

**Contexto:**
Estamos na fase final do treinamento do módulo de engenharia, onde é enfatizada a importância de documentar o que foi aprendido. O objetivo é garantir que todos os participantes tenham acesso às informações e possam esclarecer dúvidas posteriormente.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Engenharia > Treinamento
- Tela/interface específica: Tela de Conclusão do Treinamento

**Funcionalidade Detalhada:**
Esta funcionalidade serve para registrar as informações discutidas durante o treinamento do módulo de engenharia. É crucial para que os participantes possam consultar o conteúdo posteriormente e esclarecer quaisquer dúvidas que possam surgir. O COPER é mencionado como um canal de suporte para resolver questões que não foram abordadas durante o treinamento.

### 🔹 Passo a Passo Detalhado:

1. **Finalização do Treinamento**
   - Localização: Tela de Conclusão do Treinamento
   - Como fazer: Ao final do treinamento, os participantes devem garantir que todas as informações relevantes foram registradas. Isso pode incluir anotações pessoais ou a utilização de um sistema de documentação.
   - Resultado esperado: Os participantes devem sair do treinamento com um entendimento claro do conteúdo e saber como acessar informações adicionais se necessário.

2. **Contato com o COPER**
   - Localização: Informações de contato disponíveis na tela de conclusão ou na documentação do treinamento.
   - Como fazer: Caso surjam dúvidas após o treinamento, os participantes devem entrar em contato com o COPER. Isso pode ser feito através de e-mail, telefone ou sistema de tickets, conforme as instruções fornecidas.
   - Observações importantes: É recomendável que os participantes anotem suas dúvidas durante o treinamento para que possam ser discutidas com o COPER posteriormente.
   - Resultado esperado: Os participantes devem ter um canal claro para resolver suas dúvidas e obter suporte adicional.

**Campos e Parâmetros:**

| Campo          | Tipo   | Obrigatório | Descrição                                   | Exemplo               |
|----------------|--------|-------------|---------------------------------------------|-----------------------|
| Nome do Treinamento | Texto  | Sim         | Nome do módulo de treinamento realizado     | Engenharia             |
| Dúvida         | Texto  | Não         | Questões que o participante deseja esclarecer | "Como acessar o sistema?" |

**Regras de Negócio:**
- Os participantes devem registrar as informações discutidas durante o treinamento.
- O COPER deve ser contatado para quaisquer dúvidas que não foram resolvidas durante o treinamento.
- É importante que os participantes anotem suas dúvidas para facilitar a comunicação com o COPER.

**Observações Importantes:**
- É aconselhável que os participantes revisem suas anotações após o treinamento para consolidar o aprendizado.
- Erros comuns a evitar incluem não registrar informações importantes ou não anotar dúvidas que possam surgir.
- Certifique-se de ter as informações de contato do COPER à mão para facilitar o suporte.

**Conceitos-Chave:**
- **COPER**: Central de Operações e Suporte, responsável por fornecer assistência e esclarecer dúvidas dos usuários.
- **Treinamento**: Processo de aprendizado sobre o módulo de engenharia, onde informações cruciais são discutidas.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso registrar as informações discutidas durante o treinamento?
- O que devo fazer se tiver dúvidas após o treinamento?
- Quem é o COPER e como posso entrar em contato com eles?

---


---

