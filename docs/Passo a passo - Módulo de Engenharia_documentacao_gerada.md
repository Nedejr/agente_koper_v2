## 1. Cadastro da Obra

**Minutagem:** 00:00 → 02:30

**Contexto:**
Nesta seção, vamos aprender como cadastrar uma obra no módulo de engenharia do sistema. O objetivo é registrar todas as informações necessárias para o gerenciamento da obra.

**Localização no Sistema:**
- Menu Principal > Módulo de Engenharia > Cadastro de Obras

**Funcionalidade Detalhada:**
O cadastro da obra permite que os usuários insiram informações essenciais sobre a obra, como nome, tipo, data de início e estrutura. É importante seguir as orientações para garantir que todos os campos obrigatórios sejam preenchidos corretamente.

### 🔹 Passo a Passo Detalhado:

1. **Selecionar a Versão Tradicional**
   - Localização: Tela de Cadastro de Obras
   - Como fazer: Clique na opção **"Versão Tradicional"** para facilitar o preenchimento.
   - Resultado esperado: O sistema ajusta a interface para o modo tradicional, permitindo um preenchimento mais simples.

2. **Selecionar o Tipo da Obra**
   - Localização: Campo **"Tipo da Obra"**
   - Como fazer: Clique no dropdown e selecione entre as opções **"Obra Própria"** ou **"Obra para Terceiro"**.
   - Observações importantes: Ao selecionar o tipo, novos campos serão exibidos para preenchimento.
   - Resultado esperado: Campos adicionais aparecem para que você possa inserir informações específicas da obra.

3. **Preencher Campos Obrigatórios**
   - Localização: Campos de entrada
   - Campos/Opções disponíveis:
     * `Nome da Obra`: Campo de texto (obrigatório)
     * `Data de Início`: Campo de data (obrigatório)
     * `Tipo da Obra`: Dropdown (obrigatório)
   - Como fazer: Preencha todos os campos obrigatórios, que possuem um asterisco (*) ao lado.
   - Resultado esperado: Os campos obrigatórios são preenchidos corretamente, permitindo prosseguir.

4. **Adicionar Novo Tipo de Obra**
   - Localização: Botão **"Mais Adicionar"**
   - Como fazer: Se o tipo de obra desejado não estiver listado, clique em **"Mais Adicionar"** para cadastrar um novo tipo.
   - Resultado esperado: Uma nova interface se abre para o cadastro do tipo de obra.

5. **Preencher Estrutura da Obra**
   - Localização: Seção **"Estrutura da Obra"**
   - Como fazer: Responda às perguntas sobre a estrutura da obra, como:
     * **Possui blocos?** Se sim, selecione **"Sim"** e insira a quantidade.
     * **Possui andares?** Se sim, selecione **"Sim"** e insira o número de andares.
     * **Possui unidades por andar?** Insira a quantidade de unidades.
   - Resultado esperado: As informações sobre a estrutura da obra são registradas corretamente.

6. **Inserir Endereço da Obra**
   - Localização: Campo **"Endereço da Obra"**
   - Como fazer: Preencha o campo com o endereço completo da obra.
   - Resultado esperado: O endereço da obra é salvo no sistema.

7. **Salvar Cadastro da Obra**
   - Localização: Botão **"Salvar"**
   - Como fazer: Clique no botão **"Salvar"** para concluir o cadastro da obra.
   - Resultado esperado: A obra é cadastrada no sistema, e uma mensagem de confirmação é exibida.

**Campos e Parâmetros:**

| Campo               | Tipo         | Obrigatório | Descrição                               | Exemplo                 |
|---------------------|--------------|-------------|-----------------------------------------|-------------------------|
| Nome da Obra        | Texto        | Sim         | Nome que identifica a obra              | "Construção Edifício A" |
| Data de Início      | Data         | Sim         | Data em que a obra começa               | "01/10/2023"            |
| Tipo da Obra        | Dropdown     | Sim         | Tipo de obra (própria ou para terceiro) | "Obra Própria"          |
| Estrutura da Obra   | Checkbox     | Não         | Informações sobre blocos, andares, etc. | "Sim" ou "Não"          |
| Endereço da Obra    | Texto        | Sim         | Localização da obra                     | "Rua Exemplo, 123"      |

**Regras de Negócio:**
- Todos os campos marcados com asterisco (*) são obrigatórios.
- O tipo da obra deve ser selecionado antes de preencher os campos adicionais.
- O sistema permite adicionar novos tipos de obra caso não estejam cadastrados.

**Observações Importantes:**
- Utilize a versão tradicional para um preenchimento mais rápido.
- Verifique se todos os campos obrigatórios estão preenchidos antes de salvar.
- Caso precise adicionar mais blocos ou unidades, utilize a opção **"Mais Estrutura"**.

**Conceitos-Chave:**
- **Cadastro de Obra**: Processo de registrar informações essenciais sobre uma obra no sistema.
- **Estrutura da Obra**: Informações sobre a configuração física da obra, como blocos e andares.

---

## 2. Organização de Documentos da Obra

**Minutagem:** 02:30 → 05:00

**Contexto:**
Após cadastrar a obra, é importante organizar os documentos relacionados a ela. Nesta seção, vamos aprender como criar pastas e adicionar documentos.

**Localização no Sistema:**
- Menu Principal > Módulo de Engenharia > Cadastro de Obras > Seção de Documentos

**Funcionalidade Detalhada:**
A funcionalidade de organização de documentos permite que os usuários criem pastas para armazenar documentos relevantes da obra, facilitando o acesso e a gestão de informações.

### 🔹 Passo a Passo Detalhado:

1. **Criar Pasta para Documentos**
   - Localização: Seção **"Documentos da Obra"**
   - Como fazer: Clique no botão **"Criar Pasta"**.
   - Resultado esperado: Um campo para nomear a nova pasta aparece.

2. **Nomear a Pasta**
   - Localização: Campo de texto para nome da pasta
   - Como fazer: Digite um nome descritivo para a pasta, como **"Contratos"** ou **"Projetos"**.
   - Resultado esperado: O nome da pasta é salvo e a pasta é criada.

3. **Adicionar Documentos à Pasta**
   - Localização: Pasta recém-criada
   - Como fazer: Clique na pasta e, em seguida, clique em **"Adicionar Documento"**.
   - Resultado esperado: Um campo para upload de documentos aparece.

4. **Selecionar Documento para Upload**
   - Localização: Campo de upload
   - Como fazer: Clique em **"Selecionar Arquivo"** e escolha o documento desejado no seu computador.
   - Resultado esperado: O documento é selecionado para upload.

5. **Salvar Documento**
   - Localização: Botão **"Salvar"**
   - Como fazer: Clique em **"Salvar"** para concluir o upload do documento.
   - Resultado esperado: O documento é adicionado à pasta e aparece na lista de documentos.

**Campos e Parâmetros:**

| Campo               | Tipo         | Obrigatório | Descrição                               | Exemplo                 |
|---------------------|--------------|-------------|-----------------------------------------|-------------------------|
| Nome da Pasta        | Texto        | Sim         | Nome que identifica a pasta             | "Contratos"             |
| Documento            | Arquivo      | Sim         | Arquivo a ser anexado                   | "contrato.pdf"          |

**Regras de Negócio:**
- É necessário criar uma pasta antes de adicionar documentos.
- Os documentos devem ser salvos em formatos aceitos pelo sistema.

**Observações Importantes:**
- Organize os documentos em pastas para facilitar a localização.
- Verifique se o documento está no formato correto antes de tentar fazer o upload.

**Conceitos-Chave:**
- **Pasta de Documentos**: Estrutura que permite organizar arquivos relacionados a uma obra.
- **Upload de Documentos**: Processo de anexar arquivos ao sistema para armazenamento e gestão.

---

## 3. Estrutura da Obra

**Minutagem:** 05:00 → 07:30

**Contexto:**
Nesta seção, vamos detalhar como preencher a estrutura da obra, incluindo informações sobre blocos, andares e unidades.

**Localização no Sistema:**
- Menu Principal > Módulo de Engenharia > Cadastro de Obras > Seção de Estrutura da Obra

**Funcionalidade Detalhada:**
A estrutura da obra é uma parte crucial do cadastro, pois define como a obra será organizada fisicamente. Isso inclui a quantidade de blocos, andares e unidades.

### 🔹 Passo a Passo Detalhado:

1. **Indicar se a Obra Possui Blocos**
   - Localização: Campo **"A obra possui blocos?"**
   - Como fazer: Selecione **"Sim"** ou **"Não"**.
   - Resultado esperado: Se **"Sim"** for selecionado, um campo para inserir a quantidade de blocos aparece.

2. **Inserir Quantidade de Blocos**
   - Localização: Campo de texto para quantidade de blocos
   - Como fazer: Digite o número de blocos que a obra possui.
   - Resultado esperado: A quantidade de blocos é registrada no sistema.

3. **Indicar se a Obra Possui Andares**
   - Localização: Campo **"A obra possui andares?"**
   - Como fazer: Selecione **"Sim"** ou **"Não"**.
   - Resultado esperado: Se **"Sim"** for selecionado, um campo para inserir o número de andares aparece.

4. **Inserir Número de Andares**
   - Localização: Campo de texto para número de andares
   - Como fazer: Digite o número de andares que a obra possui.
   - Resultado esperado: O número de andares é registrado no sistema.

5. **Indicar Unidades por Andar**
   - Localização: Campo **"Quantas unidades por andar?"**
   - Como fazer: Insira a quantidade de unidades que existem em cada andar.
   - Resultado esperado: A quantidade de unidades por andar é registrada.

6. **Salvar Estrutura da Obra**
   - Localização: Botão **"Salvar"**
   - Como fazer: Clique em **"Salvar"** para registrar todas as informações da estrutura.
   - Resultado esperado: A estrutura da obra é salva no sistema.

**Campos e Parâmetros:**

| Campo                     | Tipo         | Obrigatório | Descrição                               | Exemplo                 |
|---------------------------|--------------|-------------|-----------------------------------------|-------------------------|
| A obra possui blocos?     | Checkbox     | Sim         | Indica se a obra possui blocos          | "Sim"                   |
| Quantidade de Blocos      | Número       | Sim         | Número total de blocos na obra          | "5"                     |
| A obra possui andares?     | Checkbox     | Sim         | Indica se a obra possui andares         | "Sim"                   |
| Número de Andares         | Número       | Sim         | Total de andares na obra                | "3"                     |
| Quantidade de Unidades    | Número       | Sim         | Número de unidades por andar            | "4"                     |

**Regras de Negócio:**
- As informações sobre blocos, andares e unidades devem ser preenchidas corretamente para garantir a integridade do cadastro da obra.
- A quantidade de blocos e andares deve ser um número inteiro.

**Observações Importantes:**
- Certifique-se de que as informações estão corretas antes de salvar, pois elas impactam outras funcionalidades do sistema.
- Utilize a opção de edição caso precise alterar alguma informação após o cadastro.

**Conceitos-Chave:**
- **Estrutura da Obra**: Conjunto de informações que define a configuração física da obra.
- **Unidades**: Divisões dentro da obra, como apartamentos ou salas comerciais.

---

## 4. Cadastro de Unidades e Andares

**Minutagem:** 07:30 → 10:00

**Contexto:**
Após definir a estrutura da obra, é necessário cadastrar as unidades e andares. Nesta seção, vamos aprender como fazer isso de forma detalhada.

**Localização no Sistema:**
- Menu Principal > Módulo de Engenharia > Cadastro de Obras > Seção de Unidades e Andares

**Funcionalidade Detalhada:**
O cadastro de unidades e andares permite que os usuários registrem informações específicas sobre cada unidade, como área, valor e características adicionais.

### 🔹 Passo a Passo Detalhado:

1. **Adicionar Unidades**
   - Localização: Botão **"Adicionar Unidade"**
   - Como fazer: Clique em **"Adicionar Unidade"** para começar o cadastro de uma nova unidade.
   - Resultado esperado: Um formulário para preencher as informações da unidade aparece.

2. **Preencher Informações da Unidade**
   - Localização: Campos de entrada
   - Campos/Opções disponíveis:
     * `Nome da Unidade`: Campo de texto (obrigatório)
     * `Área Privativa`: Campo numérico (obrigatório)
     * `Área Comum`: Campo numérico (opcional)
   - Como fazer: Preencha todos os campos obrigatórios.
   - Resultado esperado: As informações da unidade são registradas no sistema.

3. **Definir se a Unidade é Vendável**
   - Localização: Checkbox **"Unidade Vendável?"**
   - Como fazer: Selecione **"Sim"** se a unidade estiver disponível para venda.
   - Resultado esperado: O sistema registra que a unidade é vendável.

4. **Associar Vagas de Garagem**
   - Localização: Campo **"Vagas de Garagem"**
   - Como fazer: Insira o número de vagas de garagem associadas à unidade.
   - Resultado esperado: O número de vagas é registrado.

5. **Adicionar Subunidades**
   - Localização: Botão **"Adicionar Subunidade"**
   - Como fazer: Clique em **"Adicionar Subunidade"** para cadastrar cômodos, como quartos e salas.
   - Resultado esperado: Um formulário para preencher as informações da subunidade aparece.

6. **Preencher Informações da Subunidade**
   - Localização: Campos de entrada
   - Campos/Opções disponíveis:
     * `Nome da Subunidade`: Campo de texto (obrigatório)
     * `Área`: Campo numérico (opcional)
   - Como fazer: Preencha os campos conforme necessário.
   - Resultado esperado: As informações da subunidade são registradas no sistema.

7. **Salvar Cadastro da Unidade**
   - Localização: Botão **"Salvar"**
   - Como fazer: Clique em **"Salvar"** para concluir o cadastro da unidade.
   - Resultado esperado: A unidade é cadastrada no sistema, e uma mensagem de confirmação é exibida.

**Campos e Parâmetros:**

| Campo                     | Tipo         | Obrigatório | Descrição                               | Exemplo                 |
|---------------------------|--------------|-------------|-----------------------------------------|-------------------------|
| Nome da Unidade            | Texto        | Sim         | Nome que identifica a unidade           | "Apartamento 101"       |
| Área Privativa            | Número       | Sim         | Área privativa da unidade               | "50"                    |
| Área Comum                | Número       | Não         | Área comum da unidade                   | "10"                    |
| Unidade Vendável?         | Checkbox     | Sim         | Indica se a unidade está à venda        | "Sim"                   |
| Vagas de Garagem          | Número       | Não         | Número de vagas de garagem              | "1"                     |
| Nome da Subunidade        | Texto        | Sim         | Nome que identifica a subunidade        | "Quarto"                |
| Área da Subunidade        | Número       | Não         | Área da subunidade                      | "20"                    |

**Regras de Negócio:**
- As informações sobre a unidade devem ser preenchidas corretamente para garantir a integridade do cadastro.
- O campo **"Área Privativa"** é obrigatório e deve ser um número positivo.

**Observações Importantes:**
- Utilize a opção de adicionar subunidades para detalhar a configuração interna da unidade.
- Verifique se a unidade é realmente vendável antes de marcar a opção.

**Conceitos-Chave:**
- **Unidade**: Divisão da obra que pode ser vendida ou alugada.
- **Subunidade**: Cômodos ou partes que compõem uma unidade, como quartos e salas.

---

## 5. Lançamento de Receitas e Despesas

**Minutagem:** 10:00 → 12:30

**Contexto:**
Após cadastrar a obra e suas unidades, é possível lançar receitas e despesas relacionadas a ela. Nesta seção, vamos aprender como realizar esses lançamentos.

**Localização no Sistema:**
- Menu Principal > Módulo Financeiro > Lançamento de Receitas e Despesas

**Funcionalidade Detalhada:**
O lançamento de receitas e despesas permite que os usuários registrem todas as transações financeiras relacionadas à obra, facilitando o controle financeiro.

### 🔹 Passo a Passo Detalhado:

1. **Selecionar Tipo de Lançamento**
   - Localização: Dropdown **"Tipo de Lançamento"**
   - Como fazer: Selecione entre **"Receita"** ou **"Despesa"**.
   - Resultado esperado: O sistema ajusta os campos disponíveis conforme o tipo selecionado.

2. **Preencher Informações do Lançamento**
   - Localização: Campos de entrada
   - Campos/Opções disponíveis:
     * `Descrição`: Campo de texto (obrigatório)
     * `Valor`: Campo numérico (obrigatório)
     * `Data`: Campo de data (obrigatório)
   - Como fazer: Preencha todos os campos obrigatórios com as informações da transação.
   - Resultado esperado: As informações do lançamento são registradas no sistema.

3. **Associar Lançamento à Obra**
   - Localização: Campo **"Associar à Obra"**
   - Como fazer: Selecione a obra relacionada ao lançamento.
   - Resultado esperado: O lançamento é vinculado à obra selecionada.

4. **Salvar Lançamento**
   - Localização: Botão **"Salvar"**
   - Como fazer: Clique em **"Salvar"** para concluir o lançamento.
   - Resultado esperado: O lançamento é registrado no sistema, e uma mensagem de confirmação é exibida.

**Campos e Parâmetros:**

| Campo                     | Tipo         | Obrigatório | Descrição                               | Exemplo                 |
|---------------------------|--------------|-------------|-----------------------------------------|-------------------------|
| Tipo de Lançamento        | Dropdown     | Sim         | Tipo de lançamento (receita ou despesa) | "Receita"               |
| Descrição                 | Texto        | Sim         | Descrição do lançamento                  | "Venda de Unidade"      |
| Valor                     | Número       | Sim         | Valor da receita ou despesa             | "50000"                 |
| Data                      | Data         | Sim         | Data do lançamento                       | "01/10/2023"            |
| Associar à Obra          | Dropdown     | Sim         | Seleção da obra relacionada              | "Construção Edifício A" |

**Regras de Negócio:**
- Todos os campos obrigatórios devem ser preenchidos antes de salvar o lançamento.
- O valor deve ser um número positivo.

**Observações Importantes:**
- Verifique se a obra está corretamente associada ao lançamento.
- Utilize descrições claras para facilitar a identificação futura dos lançamentos.

**Conceitos-Chave:**
- **Lançamento Financeiro**: Registro de uma transação financeira, seja receita ou despesa, relacionada a uma obra.
- **Controle Financeiro**: Processo de monitoramento das entradas e saídas financeiras de uma obra.

---

## 6. Geração de Orçamentos

**Minutagem:** 12:30 → 15:00

**Contexto:**
Após o cadastro da obra e o lançamento de receitas e despesas, é possível gerar orçamentos. Nesta seção, vamos aprender como criar um orçamento no sistema.

**Localização no Sistema:**
- Menu Principal > Módulo de Engenharia > Orçamentos

**Funcionalidade Detalhada:**
A geração de orçamentos permite que os usuários estimem os custos de uma obra, considerando serviços, insumos e composições. É uma etapa crucial para o planejamento financeiro.

### 🔹 Passo a Passo Detalhado:

1. **Iniciar Geração de Orçamento**
   - Localização: Botão **"Mais Orçamento"**
   - Como fazer: Clique em **"Mais Orçamento"** para iniciar o processo de criação.
   - Resultado esperado: Um formulário para preenchimento do orçamento aparece.

2. **Selecionar Tipo de Orçamento**
   - Localização: Dropdown **"Tipo de Orçamento"**
   - Como fazer: Selecione a opção **"Orçamentos por Serviços"**.
   - Resultado esperado: O sistema ajusta os campos disponíveis conforme o tipo selecionado.

3. **Preencher Informações do Orçamento**
   - Localização: Campos de entrada
   - Campos/Opções disponíveis:
     * `Nome do Orçamento`: Campo de texto (obrigatório)
     * `Valor do BDI`: Campo numérico (opcional)
     * `Percentual`: Campo numérico (opcional)
   - Como fazer: Preencha todos os campos obrigatórios e opcionais conforme necessário.
   - Resultado esperado: As informações do orçamento são registradas no sistema.

4. **Associar Orçamento à Obra**
   - Localização: Campo **"Associar à Obra"**
   - Como fazer: Selecione a obra relacionada ao orçamento.
   - Resultado esperado: O orçamento é vinculado à obra selecionada.

5. **Salvar Orçamento**
   - Localização: Botão **"Salvar"**
   - Como fazer: Clique em **"Salvar"** para concluir a geração do orçamento.
   - Resultado esperado: O orçamento é registrado no sistema, e uma mensagem de confirmação é exibida.

**Campos e Parâmetros:**

| Campo                     | Tipo         | Obrigatório | Descrição                               | Exemplo                 |
|---------------------------|--------------|-------------|-----------------------------------------|-------------------------|
| Nome do Orçamento         | Texto        | Sim         | Nome que identifica o orçamento         | "Orçamento Edifício A"  |
| Valor do BDI              | Número       | Não         | Percentual de BDI aplicado              | "10"                    |
| Percentual                | Número       | Não         | Percentual adicional, se necessário     | "5"                     |
| Associar à Obra          | Dropdown     | Sim         | Seleção da obra relacionada              | "Construção Edifício A" |

**Regras de Negócio:**
- O nome do orçamento é um campo obrigatório.
- O orçamento deve ser associado a uma obra para ser válido.

**Observações Importantes:**
- Utilize descrições claras para facilitar a identificação futura dos orçamentos.
- O BDI pode ser ajustado conforme as políticas da empresa.

**Conceitos-Chave:**
- **Orçamento**: Estimativa de custos para a execução de uma obra, considerando serviços e insumos.
- **BDI (Benefícios e Despesas Indiretas)**: Percentual aplicado sobre o custo direto para cobrir despesas indiretas.

---

## 7. Estrutura do Orçamento

**Minutagem:** 15:00 → 17:30

**Contexto:**
Após gerar o orçamento, é necessário estruturar os serviços e composições que farão parte dele. Nesta seção, vamos aprender como adicionar etapas e serviços ao orçamento.

**Localização no Sistema:**
- Menu Principal > Módulo de Engenharia > Orçamentos > Estrutura do Orçamento

**Funcionalidade Detalhada:**
A estrutura do orçamento permite que os usuários organizem os serviços e composições que serão utilizados na obra, facilitando o controle e a execução.

### 🔹 Passo a Passo Detalhado:

1. **Adicionar Etapa ao Orçamento**
   - Localização: Botão **"Adicionar Etapa"**
   - Como fazer: Clique em **"Adicionar Etapa"** para incluir uma nova etapa no orçamento.
   - Resultado esperado: Um formulário para preencher as informações da etapa aparece.

2. **Preencher Informações da Etapa**
   - Localização: Campos de entrada
   - Campos/Opções disponíveis:
     * `Nome da Etapa`: Campo de texto (obrigatório)
   - Como fazer: Preencha o campo com o nome da etapa, como **"Preparação do Terreno"**.
   - Resultado esperado: A etapa é registrada no sistema.

3. **Adicionar Subetapa (Opcional)**
   - Localização: Botão **"Adicionar Subetapa"**
   - Como fazer: Clique em **"Adicionar Subetapa"** para incluir uma subetapa na etapa criada.
   - Resultado esperado: Um formulário para preencher as informações da subetapa aparece.

4. **Preencher Informações da Subetapa**
   - Localização: Campos de entrada
   - Campos/Opções disponíveis:
     * `Nome da Subetapa`: Campo de texto (opcional)
   - Como fazer: Preencha o campo com o nome da subetapa, se necessário.
   - Resultado esperado: A subetapa é registrada no sistema.

5. **Adicionar Serviço à Etapa**
   - Localização: Botão **"Adicionar Serviço"**
   - Como fazer: Clique em **"Adicionar Serviço"** para incluir um serviço na etapa.
   - Resultado esperado: Um formulário para preencher as informações do serviço aparece.

6. **Preencher Informações do Serviço**
   - Localização: Campos de entrada
   - Campos/Opções disponíveis:
     * `Nome do Serviço`: Campo de texto (obrigatório)
     * `Unidade de Medida`: Campo de texto (obrigatório)
     * `Categoria`: Dropdown (opcional)
   - Como fazer: Preencha todos os campos obrigatórios e opcionais conforme necessário.
   - Resultado esperado: O serviço é registrado no sistema.

7. **Salvar Estrutura do Orçamento**
   - Localização: Botão **"Salvar"**
   - Como fazer: Clique em **"Salvar"** para concluir a estrutura do orçamento.
   - Resultado esperado: A estrutura do orçamento é salva no sistema, e uma mensagem de confirmação é exibida.

**Campos e Parâmetros:**

| Campo                     | Tipo         | Obrigatório | Descrição                               | Exemplo                 |
|---------------------------|--------------|-------------|-----------------------------------------|-------------------------|
| Nome da Etapa             | Texto        | Sim         | Nome que identifica a etapa             | "Preparação do Terreno" |
| Nome da Subetapa          | Texto        | Não         | Nome que identifica a subetapa          | "Limpeza do Terreno"    |
| Nome do Serviço            | Texto        | Sim         | Nome que identifica o serviço           | "Terraplanagem"         |
| Unidade de Medida         | Texto        | Sim         | Unidade de medida do serviço            | "m²"                    |
| Categoria                 | Dropdown     | Não         | Categoria do serviço                    | "Serviços Gerais"       |

**Regras de Negócio:**
- O nome da etapa e do serviço são campos obrigatórios.
- A subetapa é opcional e pode ser adicionada conforme a necessidade.

**Observações Importantes:**
- Utilize descrições claras para facilitar a identificação futura das etapas e serviços.
- A estrutura do orçamento deve ser organizada para refletir a execução da obra.

**Conceitos-Chave:**
- **Etapa**: Fase do orçamento que agrupa serviços relacionados.
- **Subetapa**: Divisão adicional dentro de uma etapa, permitindo maior detalhamento.

---

## 8. Composições e Insumos no Orçamento

**Minutagem:** 17:30 → 20:00

**Contexto:**
Nesta seção, vamos aprender como associar composições e insumos aos serviços dentro do orçamento, detalhando os materiais e mão de obra necessários.

**Localização no Sistema:**
- Menu Principal > Módulo de Engenharia > Orçamentos > Composições

**Funcionalidade Detalhada:**
As composições e insumos permitem que os usuários detalhem os materiais e a mão de obra necessários para a execução dos serviços, facilitando o controle de custos.

### 🔹 Passo a Passo Detalhado:

1. **Adicionar Composição ao Serviço**
   - Localização: Botão **"Adicionar Composição"**
   - Como fazer: Clique em **"Adicionar Composição"** para incluir uma nova composição ao serviço.
   - Resultado esperado: Um formulário para preencher as informações da composição aparece.

2. **Preencher Informações da Composição**
   - Localização: Campos de entrada
   - Campos/Opções disponíveis:
     * `Nome da Composição`: Campo de texto (obrigatório)
     * `Descrição`: Campo de texto (opcional)
   - Como fazer: Preencha todos os campos obrigatórios e opcionais conforme necessário.
   - Resultado esperado: A composição é registrada no sistema.

3. **Adicionar Insumos à Composição**
   - Localização: Botão **"Adicionar Insumo"**
   - Como fazer: Clique em **"Adicionar Insumo"** para incluir insumos à composição.
   - Resultado esperado: Um formulário para preencher as informações do insumo aparece.

4. **Preencher Informações do Insumo**
   - Localização: Campos de entrada
   - Campos/Opções disponíveis:
     * `Nome do Insumo`: Campo de texto (obrigatório)
     * `Quantidade`: Campo numérico (obrigatório)
     * `Valor Unitário`: Campo numérico (obrigatório)
   - Como fazer: Preencha todos os campos obrigatórios e opcionais conforme necessário.
   - Resultado esperado: O insumo é registrado na composição.

5. **Salvar Composição**
   - Localização: Botão **"Salvar"**
   - Como fazer: Clique em **"Salvar"** para concluir a adição da composição ao serviço.
   - Resultado esperado: A composição é registrada no sistema, e uma mensagem de confirmação é exibida.

**Campos e Parâmetros:**

| Campo                     | Tipo         | Obrigatório | Descrição                               | Exemplo                 |
|---------------------------|--------------|-------------|-----------------------------------------|-------------------------|
| Nome da Composição        | Texto        | Sim         | Nome que identifica a composição        | "Alvenaria"             |
| Descrição                 | Texto        | Não         | Descrição da composição                 | "Execução de alvenaria" |
| Nome do Insumo            | Texto        | Sim         | Nome do insumo necessário               | "Cimento"               |
| Quantidade                | Número       | Sim         | Quantidade do insumo                    | "100"                   |
| Valor Unitário            | Número       | Sim         | Valor unitário do insumo                | "20"                    |

**Regras de Negócio:**
- O nome da composição e do insumo são campos obrigatórios.
- A quantidade e o valor unitário devem ser números positivos.

**Observações Importantes:**
- Utilize descrições claras para facilitar a identificação futura das composições e insumos.
- A composição deve refletir com precisão os materiais e mão de obra necessários para o serviço.

**Conceitos-Chave:**
- **Composição**: Conjunto de insumos e mão de obra necessários para a execução de um serviço.
- **Insumo**: Material ou recurso utilizado na execução de um serviço.

---

## 9. Edição e Replicação de Orçamentos

**Minutagem:** 20:00 → 22:30

**Contexto:**
Após criar um orçamento, é possível editá-lo ou replicá-lo para facilitar a criação de novos orçamentos semelhantes. Nesta seção, vamos aprender como realizar essas ações.

**Localização no Sistema:**
- Menu Principal > Módulo de Engenharia > Orçamentos > Lista de Orçamentos

**Funcionalidade Detalhada:**
A edição e replicação de orçamentos permitem que os usuários ajustem informações ou criem novos orçamentos baseados em orçamentos existentes, economizando tempo e esforço.

### 🔹 Passo a Passo Detalhado:

1. **Selecionar Orçamento para Edição**
   - Localização: Lista de Orçamentos
   - Como fazer: Clique no orçamento que deseja editar.
   - Resultado esperado: O sistema abre a tela de edição do orçamento selecionado.

2. **Editar Informações do Orçamento**
   - Localização: Campos de entrada
   - Campos/Opções disponíveis:
     * `Nome do Orçamento`: Campo de texto (opcional)
     * `Valor do BDI`: Campo numérico (opcional)
     * `Percentual`: Campo numérico (opcional)
   - Como fazer: Altere as informações conforme necessário.
   - Resultado esperado: As informações do orçamento são atualizadas.

3. **Salvar Edição do Orçamento**
   - Localização: Botão **"Salvar"**
   - Como fazer: Clique em **"Salvar"** para concluir a edição.
   - Resultado esperado: As alterações são registradas no sistema, e uma mensagem de confirmação é exibida.

4. **Replicar Orçamento**
   - Localização: Botão **"Replicar Orçamento"**
   - Como fazer: Clique em **"Replicar Orçamento"** para criar uma cópia do orçamento.
   - Resultado esperado: O sistema cria uma nova entrada de orçamento com as mesmas informações do original.

5. **Alterar Informações na Cópia do Orçamento**
   - Localização: Campos de entrada da cópia
   - Como fazer: Altere as informações conforme necessário na nova cópia.
   - Resultado esperado: A nova cópia do orçamento é ajustada conforme as necessidades.

6. **Salvar Cópia do Orçamento**
   - Localização: Botão **"Salvar"**
   - Como fazer: Clique em **"Salvar"** para concluir a replicação do orçamento.
   - Resultado esperado: A nova cópia do orçamento é registrada no sistema, e uma mensagem de confirmação é exibida.

**Campos e Parâmetros:**

| Campo                     | Tipo         | Obrigatório | Descrição                               | Exemplo                 |
|---------------------------|--------------|-------------|-----------------------------------------|-------------------------|
| Nome do Orçamento         | Texto        | Não         | Nome que identifica o orçamento         | "Orçamento Edifício A"  |
| Valor do BDI              | Número       | Não         | Percentual de BDI aplicado              | "10"                    |
| Percentual                | Número       | Não         | Percentual adicional, se necessário     | "5"                     |

**Regras de Negócio:**
- O nome do orçamento pode ser editado, mas não é obrigatório.
- A replicação cria uma cópia exata do orçamento, que pode ser editada posteriormente.

**Observações Importantes:**
- Utilize a replicação para orçamentos semelhantes para economizar tempo.
- Verifique se as informações estão corretas após a edição ou replicação.

**Conceitos-Chave:**
- **Edição de Orçamento**: Processo de alterar informações em um orçamento existente.
- **Replicação de Orçamento**: Criação de uma cópia de um orçamento para facilitar a criação de novos orçamentos.

---

## 10. Geração de Relatórios de Orçamento

**Minutagem:** 22:30 → 25:00

**Contexto:**
Após a criação e edição de orçamentos, é possível gerar relatórios para análise. Nesta seção, vamos aprender como acessar e gerar relatórios de orçamento.

**Localização no Sistema:**
- Menu Principal > Módulo de Engenharia > Orçamentos > Relatórios

**Funcionalidade Detalhada:**
A geração de relatórios de orçamento permite que os usuários visualizem e analisem as informações financeiras relacionadas aos orçamentos, facilitando a tomada de decisões.

### 🔹 Passo a Passo Detalhado:

1. **Acessar Relatórios de Orçamento**
   - Localização: Seção **"Relatórios"**
   - Como fazer: Clique na aba **"Relatórios"** dentro do módulo de orçamentos.
   - Resultado esperado: O sistema exibe uma lista de relatórios disponíveis.

2. **Selecionar Tipo de Relatório**
   - Localização: Dropdown **"Tipo de Relatório"**
   - Como fazer: Selecione o tipo de relatório desejado, como **"Relatório de Orçamento Geral"**.
   - Resultado esperado: O sistema ajusta os campos disponíveis conforme o tipo selecionado.

3. **Gerar Relatório**
   - Localização: Botão **"Gerar Relatório"**
   - Como fazer: Clique em **"Gerar Relatório"** para criar o relatório com as informações selecionadas.
   - Resultado esperado: O sistema gera o relatório e o exibe na tela ou permite download.

4. **Visualizar Relatório**
   - Localização: Tela de visualização do relatório
   - Como fazer: Revise as informações apresentadas no relatório.
   - Resultado esperado: O relatório é exibido com todas as informações relevantes.

5. **Exportar Relatório**
   - Localização: Botão **"Exportar"**
   - Como fazer: Clique em **"Exportar"** para salvar o relatório em formato PDF ou Excel.
   - Resultado esperado: O relatório é baixado no formato selecionado.

**Campos e Parâmetros:**

| Campo                     | Tipo         | Obrigatório | Descrição                               | Exemplo                 |
|---------------------------|--------------|-------------|-----------------------------------------|-------------------------|
| Tipo de Relatório         | Dropdown     | Sim         | Seleção do tipo de relatório            | "Relatório de Orçamento" |
| Gerar Relatório           | Botão        | Sim         | Gera o relatório com as informações     | "Gerar Relatório"       |

**Regras de Negócio:**
- O tipo de relatório deve ser selecionado antes de gerar o relatório.
- Os relatórios podem ser exportados em diferentes formatos.

**Observações Importantes:**
- Utilize os relatórios para análise detalhada dos orçamentos.
- Verifique se todas as informações estão corretas antes de gerar o relatório.

**Conceitos-Chave:**
- **Relatório de Orçamento**: Documento que apresenta informações financeiras sobre os orçamentos cadastrados.
- **Exportação de Relatório**: Processo de salvar o relatório em um formato específico para compartilhamento ou análise.

---

## 11. Geração de Planejamento da Obra

**Minutagem:** 25:00 → 27:30

**Contexto:**
Após a criação do orçamento, o próximo passo é gerar o planejamento da obra. Nesta seção, vamos aprender como criar um planejamento baseado no orçamento.

**Localização no Sistema:**
- Menu Principal > Módulo de Engenharia > Planejamento

**Funcionalidade Detalhada:**
A geração de planejamento permite que os usuários organizem as etapas e serviços da obra, definindo prazos e recursos necessários para a execução.

### 🔹 Passo a Passo Detalhado:

1. **Iniciar Geração de Planejamento**
   - Localização: Botão **"Gerar Planejamento"**
   - Como fazer: Clique em **"Gerar Planejamento"** para iniciar o processo de criação.
   - Resultado esperado: Um formulário para preenchimento do planejamento aparece.

2. **Associar Planejamento à Obra**
   - Localização: Campo **"Associar à Obra"**
   - Como fazer: Selecione a obra relacionada ao planejamento.
   - Resultado esperado: O planejamento é vinculado à obra selecionada.

3. **Preencher Informações do Planejamento**
   - Localização: Campos de entrada
   - Campos/Opções disponíveis:
     * `Nome do Planejamento`: Campo de texto (obrigatório)
     * `Data de Início`: Campo de data (obrigatório)
     * `Data de Término`: Campo de data (obrigatório)
   - Como fazer: Preencha todos os campos obrigatórios com as informações do planejamento.
   - Resultado esperado: As informações do planejamento são registradas no sistema.

4. **Salvar Planejamento**
   - Localização: Botão **"Salvar"**
   - Como fazer: Clique em **"Salvar"** para concluir a geração do planejamento.
   - Resultado esperado: O planejamento é registrado no sistema, e uma mensagem de confirmação é exibida.

**Campos e Parâmetros:**

| Campo                     | Tipo         | Obrigatório | Descrição                               | Exemplo                 |
|---------------------------|--------------|-------------|-----------------------------------------|-------------------------|
| Nome do Planejamento      | Texto        | Sim         | Nome que identifica o planejamento      | "Planejamento Edifício A" |
| Data de Início            | Data         | Sim         | Data prevista para início do planejamento | "01/10/2023"            |
| Data de Término           | Data         | Sim         | Data prevista para término do planejamento | "30/12/2023"            |

**Regras de Negócio:**
- O planejamento deve ser associado a uma obra para ser válido.
- As datas de início e término devem ser preenchidas corretamente.

**Observações Importantes:**
- Utilize descrições claras para facilitar a identificação futura do planejamento.
- Verifique se as datas estão corretas antes de salvar.

**Conceitos-Chave:**
- **Planejamento da Obra**: Documento que organiza as etapas e serviços necessários para a execução da obra.
- **Cronograma**: Representação visual do planejamento, mostrando prazos e recursos.

---

## 12. Controle e Execução do Planejamento

**Minutagem:** 27:30 → 30:00

**Contexto:**
Após gerar o planejamento, é importante controlar e executar as etapas da obra. Nesta seção, vamos aprender como gerenciar o controle e a execução do planejamento.

**Localização no Sistema:**
- Menu Principal > Módulo de Engenharia > Planejamento > Controle

**Funcionalidade Detalhada:**
O controle e execução do planejamento permitem que os usuários monitorem o progresso da obra, registrando as etapas concluídas e as pendências.

### 🔹 Passo a Passo Detalhado:

1. **Acessar Controle do Planejamento**
   - Localização: Seção **"Controle"**
   - Como fazer: Clique na aba **"Controle"** dentro do módulo de planejamento.
   - Resultado esperado: O sistema exibe uma lista das etapas do planejamento.

2. **Registrar Progresso da Etapa**
   - Localização: Etapa desejada na lista
   - Como fazer: Clique na etapa que deseja atualizar.
   - Resultado esperado: O sistema abre a tela de edição da etapa.

3. **Atualizar Status da Etapa**
   - Localização: Campo **"Status"**
   - Como fazer: Selecione o novo status da etapa, como **"Concluída"** ou **"Em Andamento"**.
   - Resultado esperado: O status da etapa é atualizado no sistema.

4. **Registrar Data de Conclusão**
   - Localização: Campo **"Data de Conclusão"**
   - Como fazer: Preencha a data em que a etapa foi concluída.
   - Resultado esperado: A data de conclusão é registrada.

5. **Salvar Atualizações**
   - Localização: Botão **"Salvar"**
   - Como fazer: Clique em **"Salvar"** para concluir as atualizações.
   - Resultado esperado: As informações da etapa são atualizadas no sistema, e uma mensagem de confirmação é exibida.

**Campos e Parâmetros:**

| Campo                     | Tipo         | Obrigatório | Descrição                               | Exemplo                 |
|---------------------------|--------------|-------------|-----------------------------------------|-------------------------|
| Status                    | Dropdown     | Sim         | Status atual da etapa                   | "Concluída"             |
| Data de Conclusão         | Data         | Não         | Data em que a etapa foi concluída       | "15/10/2023"            |

**Regras de Negócio:**
- O status da etapa deve ser atualizado conforme o progresso real da obra.
- A data de conclusão deve ser preenchida corretamente se a etapa for marcada como concluída.

**Observações Importantes:**
- Utilize o controle para monitorar o progresso da obra e identificar pendências.
- Verifique se as informações estão corretas antes de salvar.

**Conceitos-Chave:**
- **Controle do Planejamento**: Processo de monitoramento do progresso das etapas da obra.
- **Status da Etapa**: Indicação do progresso de uma etapa, como "Concluída" ou "Em Andamento".

---

## 13. Acompanhamento da Obra

**Minutagem:** 30:00 → 32:30

**Contexto:**
Após o controle do planejamento, é importante acompanhar a execução da obra. Nesta seção, vamos aprender como registrar o acompanhamento da obra.

**Localização no Sistema:**
- Menu Principal > Módulo de Engenharia > Acompanhamento

**Funcionalidade Detalhada:**
O acompanhamento da obra permite que os usuários registrem as atividades diárias, monitorando o progresso e as ocorrências durante a execução.

### 🔹 Passo a Passo Detalhado:

1. **Iniciar Acompanhamento da Obra**
   - Localização: Botão **"Iniciar Acompanhamento"**
   - Como fazer: Clique em **"Iniciar Acompanhamento"** para começar a registrar as atividades.
   - Resultado esperado: Um formulário para preenchimento do acompanhamento aparece.

2. **Registrar Data e Hora do Acompanhamento**
   - Localização: Campos de entrada
   - Campos/Opções disponíveis:
     * `Data`: Campo de data (obrigatório)
     * `Hora`: Campo de hora (obrigatório)
   - Como fazer: Preencha a data e a hora em que o acompanhamento está sendo registrado.
   - Resultado esperado: As informações de data e hora são registradas.

3. **Registrar Atividades Realizadas**
   - Localização: Campo **"Atividades Realizadas"**
   - Como fazer: Descreva as atividades realizadas no dia, como **"Início da alvenaria"**.
   - Resultado esperado: As atividades são registradas no sistema.

4. **Salvar Acompanhamento**
   - Localização: Botão **"Salvar"**
   - Como fazer: Clique em **"Salvar"** para concluir o registro do acompanhamento.
   - Resultado esperado: O acompanhamento é registrado no sistema, e uma mensagem de confirmação é exibida.

**Campos e Parâmetros:**

| Campo                     | Tipo         | Obrigatório | Descrição                               | Exemplo                 |
|---------------------------|--------------|-------------|-----------------------------------------|-------------------------|
| Data                      | Data         | Sim         | Data do acompanhamento                   | "01/10/2023"            |
| Hora                      | Hora         | Sim         | Hora do acompanhamento                   | "08:00"                 |
| Atividades Realizadas     | Texto        | Sim         | Descrição das atividades do dia         | "Início da alvenaria"   |

**Regras de Negócio:**
- A data e a hora devem ser preenchidas corretamente.
- As atividades devem ser descritas de forma clara para facilitar o acompanhamento.

**Observações Importantes:**
- Utilize o acompanhamento para registrar ocorrências e progresso diário da obra.
- Verifique se as informações estão corretas antes de salvar.

**Conceitos-Chave:**
- **Acompanhamento da Obra**: Registro das atividades diárias e progresso da obra.
- **Atividades Realizadas**: Descrição das ações executadas durante o dia.

---

## 14. Diário de Obras

**Minutagem:** 32:30 → 35:00

**Contexto:**
O diário de obras é uma ferramenta importante para registrar informações diárias sobre a obra. Nesta seção, vamos aprender como utilizar o diário de obras.

**Localização no Sistema:**
- Menu Principal > Módulo de Engenharia > Diário de Obras

**Funcionalidade Detalhada:**
O diário de obras permite que os usuários registrem informações relevantes sobre o andamento da obra, como clima, ocorrências e interações.

### 🔹 Passo a Passo Detalhado:

1. **Acessar Diário de Obras**
   - Localização: Seção **"Diário de Obras"**
   - Como fazer: Clique na aba **"Diário de Obras"** dentro do módulo de engenharia.
   - Resultado esperado: O sistema exibe a interface do diário de obras.

2. **Registrar Informações do Dia**
   - Localização: Campos de entrada
   - Campos/Opções disponíveis:
     * `Clima`: Campo de texto (opcional)
     * `Ocorrências`: Campo de texto (opcional)
   - Como fazer: Preencha as informações relevantes do dia, como **"Céu limpo"** e **"Início da alvenaria"**.
   - Resultado esperado: As informações do dia são registradas no sistema.

3. **Registrar Interações**
   - Localização: Botão **"Registrar Interação"**
   - Como fazer: Clique em **"Registrar Interação"** para adicionar uma nova interação.
   - Resultado esperado: Um formulário para preencher as informações da interação aparece.

4. **Preencher Informações da Interação**
   - Localização: Campos de entrada
   - Campos/Opções disponíveis:
     * `Tipo de Interação`: Dropdown (obrigatório)
     * `Descrição`: Campo de texto (obrigatório)
   - Como fazer: Selecione o tipo de interação e descreva a interação realizada.
   - Resultado esperado: A interação é registrada no sistema.

5. **Salvar Diário de Obras**
   - Localização: Botão **"Salvar"**
   - Como fazer: Clique em **"Salvar"** para concluir o registro do diário de obras.
   - Resultado esperado: O diário de obras é atualizado no sistema, e uma mensagem de confirmação é exibida.

**Campos e Parâmetros:**

| Campo                     | Tipo         | Obrigatório | Descrição                               | Exemplo                 |
|---------------------------|--------------|-------------|-----------------------------------------|-------------------------|
| Clima                     | Texto        | Não         | Condições climáticas do dia            | "Céu limpo"             |
| Ocorrências               | Texto        | Não         | Eventos ou ocorrências do dia          | "Início da alvenaria"   |
| Tipo de Interação         | Dropdown     | Sim         | Tipo de interação registrada            | "Reunião"               |
| Descrição                 | Texto        | Sim         | Descrição da interação                  | "Reunião com o cliente" |

**Regras de Negócio:**
- As informações do diário devem ser registradas diariamente para manter um histórico preciso.
- O tipo de interação deve ser selecionado antes de registrar.

**Observações Importantes:**
- Utilize o diário de obras para documentar ocorrências e condições diárias.
- Verifique se as informações estão corretas antes de salvar.

**Conceitos-Chave:**
- **Diário de Obras**: Registro diário das atividades, ocorrências e condições da obra.
- **Interação**: Registro de eventos ou reuniões relevantes durante a execução da obra.

---

## 15. Contratos e Medições

**Minutagem:** 35:00 → 37:30

**Contexto:**
Após o acompanhamento da obra, é importante gerenciar contratos e medições. Nesta seção, vamos aprender como emitir contratos e gerar medições.

**Localização no Sistema:**
- Menu Principal > Módulo de Engenharia > Contratos e Medições

**Funcionalidade Detalhada:**
A gestão de contratos e medições permite que os usuários formalizem acordos com prestadores de serviços e monitorem o progresso das medições realizadas.

### 🔹 Passo a Passo Detalhado:

1. **Emitir Contrato**
   - Localização: Botão **"Emitir Contrato"**
   - Como fazer: Clique em **"Emitir Contrato"** para iniciar o processo de criação.
   - Resultado esperado: Um formulário para preenchimento do contrato aparece.

2. **Preencher Informações do Contrato**
   - Localização: Campos de entrada
   - Campos/Opções disponíveis:
     * `Prestador`: Dropdown (obrigatório)
     * `Modelo de Contrato`: Dropdown (obrigatório)
   - Como fazer: Selecione o prestador e o modelo de contrato desejado.
   - Resultado esperado: As informações do contrato são registradas no sistema.

3. **Salvar Contrato**
   - Localização: Botão **"Salvar"**
   - Como fazer: Clique em **"Salvar"** para concluir a emissão do contrato.
   - Resultado esperado: O contrato é registrado no sistema, e uma mensagem de confirmação é exibida.

4. **Gerar Medição**
   - Localização: Botão **"Gerar Medição"**
   - Como fazer: Clique em **"Gerar Medição"** para iniciar o processo de medição.
   - Resultado esperado: Um formulário para preenchimento da medição aparece.

5. **Preencher Informações da Medição**
   - Localização: Campos de entrada
   - Campos/Opções disponíveis:
     * `Contrato`: Dropdown (obrigatório)
     * `Quantidade Medida`: Campo numérico (obrigatório)
   - Como fazer: Selecione o contrato e preencha a quantidade medida.
   - Resultado esperado: As informações da medição são registradas no sistema.

6. **Salvar Medição**
   - Localização: Botão **"Salvar"**
   - Como fazer: Clique em **"Salvar"** para concluir a geração da medição.
   - Resultado esperado: A medição é registrada no sistema, e uma mensagem de confirmação é exibida.

**Campos e Parâmetros:**

| Campo                     | Tipo         | Obrigatório | Descrição                               | Exemplo                 |
|---------------------------|--------------|-------------|-----------------------------------------|-------------------------|
| Prestador                 | Dropdown     | Sim         | Seleção do prestador de serviços        | "Prestadora XYZ"        |
| Modelo de Contrato        | Dropdown     | Sim         | Seleção do modelo de contrato           | "Modelo Padrão"         |
| Quantidade Medida         | Número       | Sim         | Quantidade medida durante a execução    | "100"                   |

**Regras de Negócio:**
- O contrato deve ser associado a um prestador para ser válido.
- A quantidade medida deve ser um número positivo.

**Observações Importantes:**
- Utilize contratos para formalizar acordos com prestadores de serviços.
- Verifique se as informações estão corretas antes de salvar.

**Conceitos-Chave:**
- **Contrato**: Acordo formal entre a empresa e o prestador de serviços.
- **Medição**: Registro da quantidade de serviços executados para pagamento.

---

## 16. Liberação Financeira

**Minutagem:** 37:30 → 40:00

**Contexto:**
Após a geração de medições, é importante realizar a liberação financeira. Nesta seção, vamos aprender como liberar pagamentos e recebimentos relacionados às medições.

**Localização no Sistema:**
- Menu Principal > Módulo Financeiro > Liberação Financeira

**Funcionalidade Detalhada:**
A liberação financeira permite que os usuários processem pagamentos a prestadores de serviços e recebimentos de clientes, garantindo o fluxo de caixa da obra.

### 🔹 Passo a Passo Detalhado:

1. **Selecionar Medição para Liberação**
   - Localização: Lista de Medições
   - Como fazer: Clique na medição que deseja liberar.
   - Resultado esperado: O sistema abre a tela de liberação da medição selecionada.

2. **Liberar Pagamento**
   - Localização: Campo **"Liberar Pagamento"**
   - Como fazer: Clique em **"Liberar Pagamento"** para iniciar o processo de liberação.
   - Resultado esperado: O sistema processa a liberação do pagamento.

3. **Registrar Data de Vencimento**
   - Localização: Campo **"Data de Vencimento"**
   - Como fazer: Preencha a data em que o pagamento deve ser realizado.
   - Resultado esperado: A data de vencimento é registrada.

4. **Salvar Liberação Financeira**
   - Localização: Botão **"Salvar"**
   - Como fazer: Clique em **"Salvar"** para concluir a liberação financeira.
   - Resultado esperado: A liberação é registrada no sistema, e uma mensagem de confirmação é exibida.

5. **Liberar Recebimento**
   - Localização: Campo **"Liberar Recebimento"**
   - Como fazer: Clique em **"Liberar Recebimento"** para iniciar o processo de liberação.
   - Resultado esperado: O sistema processa a liberação do recebimento.

6. **Registrar Data de Vencimento do Recebimento**
   - Localização: Campo **"Data de Vencimento"**
   - Como fazer: Preencha a data em que o recebimento deve ser realizado.
   - Resultado esperado: A data de vencimento do recebimento é registrada.

7. **Salvar Liberação de Recebimento**
   - Localização: Botão **"Salvar"**
   - Como fazer: Clique em **"Salvar"** para concluir a liberação do recebimento.
   - Resultado esperado: A liberação do recebimento é registrada no sistema, e uma mensagem de confirmação é exibida.

**Campos e Parâmetros:**

| Campo                     | Tipo         | Obrigatório | Descrição                               | Exemplo                 |
|---------------------------|--------------|-------------|-----------------------------------------|-------------------------|
| Data de Vencimento        | Data         | Sim         | Data em que o pagamento deve ser realizado | "15/10/2023"            |

**Regras de Negócio:**
- A data de vencimento deve ser preenchida corretamente para garantir o controle financeiro.
- As liberações devem ser registradas para manter um histórico financeiro preciso.

**Observações Importantes:**
- Utilize a liberação financeira para gerenciar pagamentos e recebimentos de forma eficiente.
- Verifique se as informações estão corretas antes de salvar.

**Conceitos-Chave:**
- **Liberação Financeira**: Processo de autorização de pagamentos e recebimentos relacionados às medições.
- **Fluxo de Caixa**: Monitoramento das entradas e saídas financeiras da obra.

---

## 17. Controle de Compras

**Minutagem:** 40:00 → 42:30

**Contexto:**
Após a liberação financeira, é importante gerenciar as compras relacionadas à obra. Nesta seção, vamos aprender como realizar solicitações de compras e emitir ordens de compra.

**Localização no Sistema:**
- Menu Principal > Módulo de Compras > Controle de Compras

**Funcionalidade Detalhada:**
O controle de compras permite que os usuários solicitem materiais e emitam ordens de compra, garantindo que os insumos necessários estejam disponíveis para a execução da obra.

### 🔹 Passo a Passo Detalhado:

1. **Iniciar Solicitação de Compra**
   - Localização: Botão **"Solicitar Compra"**
   - Como fazer: Clique em **"Solicitar Compra"** para iniciar o processo de solicitação.
   - Resultado esperado: Um formulário para preenchimento da solicitação aparece.

2. **Preencher Informações da Solicitação**
   - Localização: Campos de entrada
   - Campos/Opções disponíveis:
     * `Material`: Dropdown (obrigatório)
     * `Quantidade`: Campo numérico (obrigatório)
   - Como fazer: Selecione o material e preencha a quantidade desejada.
   - Resultado esperado: As informações da solicitação são registradas no sistema.

3. **Salvar Solicitação de Compra**
   - Localização: Botão **"Salvar"**
   - Como fazer: Clique em **"Salvar"** para concluir a solicitação de compra.
   - Resultado esperado: A solicitação é registrada no sistema, e uma mensagem de confirmação é exibida.

4. **Emitir Ordem de Compra**
   - Localização: Botão **"Emitir Ordem de Compra"**
   - Como fazer: Clique em **"Emitir Ordem de Compra"** para iniciar o processo de emissão.
   - Resultado esperado: Um formulário para preenchimento da ordem de compra aparece.

5. **Preencher Informações da Ordem de Compra**
   - Localização: Campos de entrada
   - Campos/Opções disponíveis:
     * `Fornecedor`: Dropdown (obrigatório)
     * `Data de Entrega`: Campo de data (obrigatório)
   - Como fazer: Selecione o fornecedor e preencha a data de entrega desejada.
   - Resultado esperado: As informações da ordem de compra são registradas no sistema.

6. **Salvar Ordem de Compra**
   - Localização: Botão **"Salvar"**
   - Como fazer: Clique em **"Salvar"** para concluir a emissão da ordem de compra.
   - Resultado esperado: A ordem de compra é registrada no sistema, e uma mensagem de confirmação é exibida.

**Campos e Parâmetros:**

| Campo                     | Tipo         | Obrigatório | Descrição                               | Exemplo                 |
|---------------------------|--------------|-------------|-----------------------------------------|-------------------------|
| Material                  | Dropdown     | Sim         | Seleção do material a ser comprado     | "Cimento"               |
| Quantidade                | Número       | Sim         | Quantidade do material solicitado       | "100"                   |
| Fornecedor                | Dropdown     | Sim         | Seleção do fornecedor                   | "Fornecedor XYZ"        |
| Data de Entrega           | Data         | Sim         | Data prevista para entrega do material  | "15/10/2023"            |

**Regras de Negócio:**
- A solicitação de compra deve ser registrada antes de emitir a ordem de compra.
- As informações devem ser preenchidas corretamente para garantir a efetividade das compras.

**Observações Importantes:**
- Utilize o controle de compras para garantir que os insumos estejam disponíveis para a execução da obra.
- Verifique se as informações estão corretas antes de salvar.

**Conceitos-Chave:**
- **Solicitação de Compra**: Pedido formal para aquisição de materiais necessários para a obra.
- **Ordem de Compra**: Documento que formaliza a compra de materiais junto ao fornecedor.

---

## 18. Registro de Interações

**Minutagem:** 42:30 → 45:00

**Contexto:**
O registro de interações é uma parte importante do gerenciamento da obra. Nesta seção, vamos aprender como registrar interações relevantes durante a execução da obra.

**Localização no Sistema:**
- Menu Principal > Módulo de Engenharia > Interações

**Funcionalidade Detalhada:**
O registro de interações permite que os usuários documentem reuniões, conversas e ocorrências importantes que impactam a obra.

### 🔹 Passo a Passo Detalhado:

1. **Iniciar Registro de Interação**
   - Localização: Botão **"Registrar Interação"**
   - Como fazer: Clique em **"Registrar Interação"** para iniciar o processo de registro.
   - Resultado esperado: Um formulário para preenchimento da interação aparece.

2. **Preencher Informações da Interação**
   - Localização: Campos de entrada
   - Campos/Opções disponíveis:
     * `Tipo de Interação`: Dropdown (obrigatório)
     * `Descrição`: Campo de texto (obrigatório)
   - Como fazer: Selecione o tipo de interação e descreva a interação realizada.
   - Resultado esperado: As informações da interação são registradas no sistema.

3. **Salvar Registro de Interação**
   - Localização: Botão **"Salvar"**
   - Como fazer: Clique em **"Salvar"** para concluir o registro da interação.
   - Resultado esperado: A interação é registrada no sistema, e uma mensagem de confirmação é exibida.

**Campos e Parâmetros:**

| Campo                     | Tipo         | Obrigatório | Descrição                               | Exemplo                 |
|---------------------------|--------------|-------------|-----------------------------------------|-------------------------|
| Tipo de Interação         | Dropdown     | Sim         | Seleção do tipo de interação            | "Reunião"               |
| Descrição                 | Texto        | Sim         | Descrição da interação                  | "Reunião com o cliente" |

**Regras de Negócio:**
- O tipo de interação deve ser selecionado antes de registrar.
- As informações devem ser preenchidas corretamente para garantir um histórico preciso.

**Observações Importantes:**
- Utilize o registro de interações para documentar eventos importantes que impactam a obra.
- Verifique se as informações estão corretas antes de salvar.

**Conceitos-Chave:**
- **Interação**: Registro de eventos ou reuniões relevantes durante a execução da obra.
- **Registro de Interações**: Processo de documentar ocorrências e comunicações importantes.

---

## 19. Checklist de Execução

**Minutagem:** 45:00 → 47:30

**Contexto:**
O checklist de execução é uma ferramenta importante para garantir que todas as etapas e requisitos sejam cumpridos durante a execução da obra. Nesta seção, vamos aprender como utilizar o checklist.

**Localização no Sistema:**
- Menu Principal > Módulo de Engenharia > Checklist

**Funcionalidade Detalhada:**
O checklist permite que os usuários verifiquem se todas as condições necessárias para a execução de um serviço estão atendidas, garantindo a conformidade.

### 🔹 Passo a Passo Detalhado:

1. **Acessar Checklist**
   - Localização: Seção **"Checklist"**
   - Como fazer: Clique na aba **"Checklist"** dentro do módulo de engenharia.
   - Resultado esperado: O sistema exibe a lista de checklists disponíveis.

2. **Selecionar Checklist para Execução**
   - Localização: Lista de Checklists
   - Como fazer: Clique no checklist que deseja utilizar.
   - Resultado esperado: O sistema abre a tela de execução do checklist selecionado.

3. **Marcar Itens do Checklist**
   - Localização: Itens do Checklist
   - Como fazer: Marque os itens que foram cumpridos e preencha observações, se necessário.
   - Resultado esperado: Os itens marcados são registrados como cumpridos.

4. **Salvar Checklist**
   - Localização: Botão **"Salvar"**
   - Como fazer: Clique em **"Salvar"** para concluir o registro do checklist.
   - Resultado esperado: O checklist é atualizado no sistema, e uma mensagem de confirmação é exibida.

**Campos e Parâmetros:**

| Campo                     | Tipo         | Obrigatório | Descrição                               | Exemplo                 |
|---------------------------|--------------|-------------|-----------------------------------------|-------------------------|
| Itens do Checklist        | Checkbox     | Sim         | Itens a serem verificados               | "EPI disponível"        |
| Observações               | Texto        | Não         | Observações adicionais sobre o checklist | "Tudo em conformidade"  |

**Regras de Negócio:**
- Todos os itens do checklist devem ser verificados antes de iniciar a execução do serviço.
- As observações são opcionais, mas podem ser úteis para documentar situações específicas.

**Observações Importantes:**
- Utilize o checklist para garantir que todas as condições necessárias para a execução sejam atendidas.
- Verifique se as informações estão corretas antes de salvar.

**Conceitos-Chave:**
- **Checklist de Execução**: Lista de verificação que garante que todas as condições necessárias para a execução de um serviço sejam atendidas.
- **Conformidade**: Garantia de que todas as etapas e requisitos estão sendo cumpridos.

---

## 20. Encerramento da Obra

**Minutagem:** 47:30 → 50:00

**Contexto:**
Após a conclusão da obra, é importante realizar o encerramento formal. Nesta seção, vamos aprender como encerrar a obra no sistema.

**Localização no Sistema:**
- Menu Principal > Módulo de Engenharia > Encerramento da Obra

**Funcionalidade Detalhada:**
O encerramento da obra permite que os usuários finalizem todas as atividades relacionadas à obra, garantindo que todas as informações estejam registradas e que a obra seja oficialmente concluída.

### 🔹 Passo a Passo Detalhado:

1. **Iniciar Encerramento da Obra**
   - Localização: Botão **"Encerrar Obra"**
   - Como fazer: Clique em **"Encerrar Obra"** para iniciar o processo de encerramento.
   - Resultado esperado: Um formulário para preenchimento do encerramento aparece.

2. **Preencher Informações do Encerramento**
   - Localização: Campos de entrada
   - Campos/Opções disponíveis:
     * `Data de Encerramento`: Campo de data (obrigatório)
     * `Observações`: Campo de texto (opcional)
   - Como fazer: Preencha a data de encerramento e adicione observações, se necessário.
   - Resultado esperado: As informações do encerramento são registradas no sistema.

3. **Salvar Encerramento**
   - Localização: Botão **"Salvar"**
   - Como fazer: Clique em **"Salvar"** para concluir o encerramento da obra.
   - Resultado esperado: A obra é oficialmente encerrada no sistema, e uma mensagem de confirmação é exibida.

**Campos e Parâmetros:**

| Campo                     | Tipo         | Obrigatório | Descrição                               | Exemplo                 |
|---------------------------|--------------|-------------|-----------------------------------------|-------------------------|
| Data de Encerramento      | Data         | Sim         | Data em que a obra foi encerrada       | "30/12/2023"            |
| Observações               | Texto        | Não         | Observações adicionais sobre o encerramento | "Obra concluída com sucesso" |

**Regras de Negócio:**
- A data de encerramento deve ser preenchida corretamente para garantir o registro formal.
- As observações são opcionais, mas podem ser úteis para documentar a conclusão da obra.

**Observações Importantes:**
- Utilize o encerramento para formalizar a conclusão de todas as atividades da obra.
- Verifique se as informações estão corretas antes de salvar.

**Conceitos-Chave:**
- **Encerramento da Obra**: Processo de finalização formal de todas as atividades relacionadas à obra.
- **Registro Formal**: Documentação que garante que a obra foi oficialmente concluída.

---

Esta documentação detalha as funcionalidades do módulo de engenharia, seguindo a transcrição do vídeo tutorial. Cada seção foi estruturada para fornecer informações claras e precisas sobre as ações a serem realizadas no sistema.