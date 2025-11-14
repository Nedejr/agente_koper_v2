# 📚 Documentação: Passo a passo - Módulo de Qualidade

**🎥 Vídeo Original:** https://youtu.be/lefybyzpmgY?si=YfjXcK_ZY3ZoekrC

**📊 Total de Seções:** 5

**ℹ️ Nota:** Cada seção abaixo contém um link direto para o trecho específico do vídeo tutorial.

---

---

## 1. Cadastro de Categorias e Itens de Assistência no Módulo Qualidade

**📋 METADADOS:**
- **ID:** sec_1
- **⏱️ Minutagem:** 00:01 → 02:33
- **⏲️ Duração:** 152s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/lefybyzpmgY?si=YfjXcK_ZY3ZoekrC&t=1)
- **📦 Módulo:** Qualidade
- **🏷️ Categorias:** Cadastro, Assistência, Garantia, Pós-vendas
- **🔑 Palavras-chave:** Cadastro de categorias, Itens de assistência, Garantia, Subcategorias, Pós-vendas

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como cadastrar categorias e itens de assistência no módulo qualidade, essencial para gerenciar o fluxo do pós-vendas e garantir que os itens estejam devidamente organizados e categorizados.

**Contexto:**
Estamos no módulo qualidade do sistema, que tem como objetivo gerenciar o fluxo do pós-vendas. O foco desta seção é o cadastro inicial de categorias e itens de assistência, que são fundamentais para a organização e gestão de garantias.

**Localização no Sistema:**
- Caminho de navegação: Menu Principal > Módulo Qualidade > Cadastros > Categorias de Assistências
- Tela/interface específica: Tela de Cadastro de Categorias e Itens de Assistência

**Funcionalidade Detalhada:**
O módulo qualidade permite o gerenciamento de categorias e itens de assistência, que são utilizados para definir garantias e organizar o suporte pós-venda. O cadastro de categorias é o primeiro passo para estruturar os itens que serão oferecidos aos clientes.

### 🔹 Passo a Passo Detalhado:

1. **Acessar o Módulo Qualidade**
   - Localização: Menu Principal
   - Como fazer: Clique no ícone do módulo **Qualidade**.
   - Resultado esperado: A tela do módulo qualidade será exibida.

2. **Cadastrar Categorias de Assistência**
   - Localização: Menu lateral > **Cadastros** > Aba **Categorias de Assistências**
   - Como fazer: Clique na aba **Categorias de Assistências**.
   - Resultado esperado: A lista de categorias pré-cadastradas será exibida.

3. **Adicionar Nova Categoria**
   - Localização: Tela de Categorias de Assistências
   - Como fazer: Clique no botão **Mais Categoria**.
   - Campos/Opções disponíveis:
     * `Nome da Categoria`: Campo de texto para inserir o nome da nova categoria.
   - Resultado esperado: Um novo campo para inserir o nome da categoria será exibido.

4. **Salvar Categoria**
   - Localização: Após inserir o nome da categoria
   - Como fazer: Clique no botão **Salvar**.
   - Resultado esperado: A nova categoria será adicionada à lista de categorias.

5. **Adicionar Subcategoria**
   - Localização: Ao lado da categoria recém-cadastrada
   - Como fazer: Clique no botão **Mais** ao lado da categoria.
   - Campos/Opções disponíveis:
     * `Nome da Subcategoria`: Campo de texto para inserir o nome da subcategoria.
   - Resultado esperado: Um novo campo para inserir o nome da subcategoria será exibido.

6. **Salvar Subcategoria**
   - Localização: Após inserir o nome da subcategoria
   - Como fazer: Clique no botão **Salvar**.
   - Resultado esperado: A nova subcategoria será adicionada à lista de subcategorias da categoria correspondente.

7. **Editar ou Excluir Categorias/Subcategorias**
   - Localização: Lista de categorias/subcategorias
   - Como fazer: Selecione a categoria ou subcategoria desejada e clique nos botões **Editar** ou **Excluir**.
   - Resultado esperado: A categoria ou subcategoria será editada ou removida conforme a ação escolhida.

8. **Cadastrar Itens de Assistência**
   - Localização: Menu lateral > **Itens de Assistência**
   - Como fazer: Clique na aba **Itens de Assistência**.
   - Resultado esperado: A tela para cadastro de itens de assistência será exibida.

9. **Adicionar Novo Item**
   - Localização: Tela de Itens de Assistência
   - Como fazer: Clique no botão **Mais Item**.
   - Campos/Opções disponíveis:
     * `Categoria`: Selecionar a categoria correspondente.
     * `Subcategoria`: Selecionar a subcategoria correspondente.
     * `Nome do Item`: Campo de texto para inserir o nome do item.
   - Resultado esperado: Campos para selecionar categoria, subcategoria e inserir o nome do item serão exibidos.

10. **Selecionar Empreendimentos**
    - Localização: Abaixo do campo de nome do item
    - Como fazer: Arraste para o lado ou clique na mãozinha para selecionar os empreendimentos que oferecem garantia para o item.
    - Resultado esperado: Os empreendimentos selecionados serão associados ao item.

11. **Definir Garantia**
    - Localização: Após selecionar os empreendimentos
    - Como fazer: Escolha entre as opções de garantia disponíveis (ex: "Garantia até o ato da entrega" ou "Garantia fornecida pela construtora").
    - Resultado esperado: A garantia será definida para o item cadastrado.

**Campos e Parâmetros:**

| Campo                  | Tipo         | Obrigatório | Descrição                                           | Exemplo                  |
|------------------------|--------------|-------------|----------------------------------------------------|--------------------------|
| Nome da Categoria       | Texto        | Sim         | Nome da nova categoria a ser cadastrada.           | "Eletrodomésticos"       |
| Nome da Subcategoria    | Texto        | Sim         | Nome da nova subcategoria a ser cadastrada.        | "Geladeiras"             |
| Categoria               | Dropdown     | Sim         | Seleção da categoria à qual o item pertence.       | "Eletrodomésticos"       |
| Subcategoria            | Dropdown     | Sim         | Seleção da subcategoria à qual o item pertence.    | "Geladeiras"             |
| Nome do Item            | Texto        | Sim         | Nome do item a ser cadastrado.                     | "Geladeira Branca"       |
| Empreendimentos         | Checkbox     | Sim         | Seleção dos empreendimentos que oferecem garantia.  | "Empreendimento A"       |
| Garantia                | Dropdown     | Sim         | Tipo de garantia oferecida para o item.            | "Garantia até a entrega" |

**Regras de Negócio:**
- Cada categoria deve ter um nome único.
- Subcategorias devem ser associadas a uma categoria existente.
- Itens de assistência devem ter uma categoria e subcategoria definidas.
- Empreendimentos devem ser selecionados para cada item que oferece garantia.

**Observações Importantes:**
- Ao cadastrar uma nova categoria, verifique se o nome não está duplicado.
- As subcategorias devem ser relevantes e específicas para facilitar a busca.
- Sempre salve as alterações após cada cadastro para evitar perda de dados.

**Conceitos-Chave:**
- **Categoria**: Classificação principal para agrupar itens de assistência.
- **Subcategoria**: Classificação secundária que fornece mais detalhes sobre a categoria.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                     | Solução                                           | Prevenção                                      |
|-----------------------------------|------------------------------------|--------------------------------------------------|------------------------------------------------|
| Não consigo salvar a categoria     | Nome da categoria já existe        | Verifique se o nome é único e tente novamente.   | Sempre verifique a lista antes de cadastrar.  |
| Subcategoria não aparece na lista  | Categoria não cadastrada           | Cadastre a categoria antes de adicionar subcategorias. | Cadastre categorias primeiro.                  |
| Item não aparece na lista de itens | Não foi selecionada a categoria    | Certifique-se de que a categoria e subcategoria estão selecionadas. | Revise as seleções antes de salvar.            |

**💡 DICAS E BOAS PRÁTICAS:**
- Utilize nomes descritivos para categorias e subcategorias para facilitar a identificação.
- Revise as garantias oferecidas periodicamente para garantir que estão atualizadas.
- Use a funcionalidade de edição para corrigir informações em vez de excluir e cadastrar novamente.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Cadastro de Categoria e Subcategoria**
```
Situação: Cadastro de uma nova categoria de assistência.
Ação: 
  • Campo Nome da Categoria: "Eletrodomésticos"
  • Campo Nome da Subcategoria: "Geladeiras"
Resultado: A categoria "Eletrodomésticos" e a subcategoria "Geladeiras" são cadastradas com sucesso.
```

**Exemplo 2: Cadastro de Item de Assistência**
```
Situação: Cadastro de um item de assistência.
Ação: 
  • Campo Categoria: "Eletrodomésticos"
  • Campo Subcategoria: "Geladeiras"
  • Campo Nome do Item: "Geladeira Branca"
Resultado: O item "Geladeira Branca" é cadastrado com a garantia selecionada para os empreendimentos escolhidos.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** As categorias devem ser cadastradas antes de adicionar itens de assistência.
- **Habilita:** O cadastro de itens de assistência permite a gestão de garantias e suporte pós-venda.
- **Relacionado a:** Funcionalidades de relatórios de assistência e gestão de garantias.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como cadastrar uma nova categoria de assistência?"
- **Com problema:** "Não consigo adicionar uma subcategoria, o que fazer?"
- **Informal:** "Como eu coloco uma nova categoria no sistema?"
- **Por sintoma:** "O que fazer se a categoria não aparece na lista?"
- **Alternativa:** "Como faço para editar uma categoria existente?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Adicionar categoria", "Criar categoria", "Cadastrar subcategoria", "Inserir item de assistência"
- "Gerenciar assistência", "Configurar garantias"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como cadastrar uma nova categoria de assistência?
- O que fazer se não consigo salvar uma subcategoria?
- Como adicionar um item de assistência ao sistema?
- O que fazer se a categoria não aparece na lista de opções?
- O que preciso ter feito antes de cadastrar itens de assistência?

---


---


---

## 2. Configuração de Assistências Técnicas

**📋 METADADOS:**
- **ID:** sec_2
- **⏱️ Minutagem:** 02:31 → 05:05
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/lefybyzpmgY?si=YfjXcK_ZY3ZoekrC&t=151)
- **📦 Módulo:** Assistências Técnicas
- **🏷️ Categorias:** Configuração, Cadastro, Operacional
- **🔑 Palavras-chave:** assistência técnica, solicitação, garantia, edição, exclusão

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de configuração de assistências técnicas no sistema, desde a definição de prazos de garantia até a execução do serviço, permitindo que os usuários gerenciem solicitações de assistência de forma eficiente.

**Contexto:**
Estamos no módulo de Assistências Técnicas do sistema, onde os usuários podem registrar e gerenciar solicitações de assistência para itens que estão sob garantia. O objetivo desta seção é guiar o usuário através do processo de configuração e gerenciamento dessas assistências.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Assistências Técnicas > Submenu Solicitar Assistência
- Tela/interface específica: Tela de Solicitação de Assistência

**Funcionalidade Detalhada:**
A funcionalidade de configuração de assistências técnicas permite que os usuários registrem solicitações de assistência para itens que estão sob garantia. O sistema exige que o usuário defina o prazo de garantia e selecione o empreendimento e a unidade antes de iniciar o fluxo de assistência. O usuário pode também editar ou excluir itens previamente cadastrados e visualizar informações sobre o status da assistência.

### 🔹 Passo a Passo Detalhado:

1. **Definir Prazo de Garantia**
   - Localização: Tela de Configuração de Itens
   - Como fazer: Na seção de configuração, o usuário deve inserir o prazo de garantia em meses ou dias para o item relacionado ao empreendimento.
   - Campos/Opções disponíveis:
     * `Prazo de Garantia`: Campo numérico, obrigatório, onde o usuário insere o valor em meses ou dias.
   - Resultado esperado: O prazo de garantia é salvo e o item é configurado na base de dados.

2. **Salvar Configuração**
   - Localização: Botão **Salvar** na parte inferior da tela de configuração.
   - Como fazer: Após definir o prazo de garantia, clique no botão **Salvar** para confirmar as alterações.
   - Resultado esperado: A configuração do item é salva e o sistema confirma a operação.

3. **Iniciar Novo Fluxo de Assistência**
   - Localização: Tela de Solicitação de Assistência, botão **Mais Assistência**.
   - Como fazer: Clique no botão **Mais Assistência** para iniciar um novo fluxo de assistência técnica.
   - Resultado esperado: O sistema abre um novo formulário para preenchimento da solicitação.

4. **Selecionar Empreendimento e Unidade**
   - Localização: Campo de seleção de **Empreendimento** e **Unidade** na tela de solicitação.
   - Como fazer: Escolha o empreendimento relacionado e, em seguida, selecione a unidade. O sistema só permitirá selecionar unidades cuja entrega das chaves já foi realizada.
   - Observações importantes: Certifique-se de que a entrega das chaves foi registrada para a unidade selecionada.
   - Resultado esperado: A unidade é vinculada à solicitação de assistência.

5. **Definir Data da Solicitação**
   - Localização: Campo de **Data da Solicitação**.
   - Como fazer: Insira a data em que a solicitação está sendo feita.
   - Resultado esperado: A data é registrada na solicitação.

6. **Sinalizar Urgência**
   - Localização: Opção de seleção **Urgente** na tela de solicitação.
   - Como fazer: Marque a opção se a assistência for urgente.
   - Resultado esperado: A solicitação é marcada como urgente, alterando seu status.

7. **Descrição do Problema**
   - Localização: Campo de **Descrição do Problema**.
   - Como fazer: Insira uma descrição detalhada do problema que requer assistência.
   - Resultado esperado: A descrição é salva e associada à solicitação.

8. **Selecionar Itens Relacionados**
   - Localização: Tela de seleção de itens, após clicar em **Próximo**.
   - Como fazer: Filtre os itens pela categoria e subcategoria para encontrar os itens relacionados à assistência. Selecione os itens arrastando-os ou clicando na mãozinha.
   - Observações importantes: A seleção de itens é obrigatória e deve ser feita com base na categoria.
   - Resultado esperado: Os itens são adicionados à solicitação de assistência.

9. **Salvar Solicitação de Assistência**
   - Localização: Botão **Salvar** na tela de solicitação.
   - Como fazer: Após preencher todos os campos e selecionar os itens, clique em **Salvar**.
   - Resultado esperado: A assistência é iniciada e aparece na lista de assistências com status e informações gerais.

10. **Importar Arquivos**
    - Localização: Tela de detalhes da assistência, opção **Importar Arquivos**.
    - Como fazer: Clique na opção para anexar documentos relevantes à solicitação.
    - Resultado esperado: Os arquivos são anexados à assistência para referência futura.

**Campos e Parâmetros:**

| Campo                     | Tipo       | Obrigatório | Descrição                                               | Exemplo                |
|---------------------------|------------|-------------|---------------------------------------------------------|------------------------|
| `Prazo de Garantia`       | Numérico   | Sim         | Tempo de garantia do item em meses ou dias.            | 12 (meses)             |
| `Empreendimento`          | Dropdown   | Sim         | Seleção do empreendimento relacionado à assistência.    | "Empreendimento A"     |
| `Unidade`                 | Dropdown   | Sim         | Seleção da unidade que já teve entrega de chaves.      | "Unidade 101"         |
| `Data da Solicitação`     | Data       | Sim         | Data em que a solicitação está sendo feita.            | "2023-10-01"           |
| `Urgente`                 | Checkbox   | Não         | Indica se a assistência é urgente.                      | [ ] Urgente            |
| `Descrição do Problema`    | Texto      | Sim         | Descrição detalhada do problema a ser assistido.      | "Fuga de água"         |
| `Itens Relacionados`      | Lista      | Sim         | Itens que fazem parte da assistência e estão sob garantia. | "Item 1, Item 2"      |

**Regras de Negócio:**
- O prazo de garantia deve ser definido antes de salvar a configuração do item.
- Apenas unidades com entrega de chaves registrada podem ser selecionadas para assistência.
- A descrição do problema é obrigatória para a criação da solicitação de assistência.
- A seleção de itens relacionados deve ser feita filtrando por categoria e subcategoria.

**Observações Importantes:**
- Verifique se todos os campos obrigatórios estão preenchidos antes de salvar.
- Evite selecionar unidades sem entrega de chaves, pois isso causará erro na solicitação.
- A descrição do problema deve ser clara e detalhada para facilitar a assistência.

**Conceitos-Chave:**
- **Assistência Técnica**: Processo de solicitação de suporte para itens que estão sob garantia.
- **Prazo de Garantia**: Tempo estipulado para a cobertura de assistência de um item.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                   | Solução                                           | Prevenção                                   |
|-----------------------------------|----------------------------------|--------------------------------------------------|---------------------------------------------|
| Não consigo salvar a assistência   | Campos obrigatórios não preenchidos | Verifique se todos os campos obrigatórios estão preenchidos. | Sempre revisar os campos antes de salvar.  |
| Unidade não aparece na lista       | Chaves não entregues             | Confirme se a entrega das chaves foi registrada. | Registrar a entrega de chaves previamente.  |
| Erro ao selecionar itens           | Filtros de categoria não aplicados | Aplique filtros corretos para visualizar itens.  | Usar sempre a categoria correta ao filtrar. |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre defina o prazo de garantia antes de iniciar a assistência.
- Utilize descrições detalhadas para facilitar o entendimento do problema.
- Revise as informações antes de salvar para evitar retrabalho.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Solicitação de Assistência Urgente**
```
Situação: Um cliente reporta uma fuga de água em um apartamento.
Ação: 
  • Campo Empreendimento: "Empreendimento A"
  • Campo Unidade: "Unidade 101"
  • Campo Data da Solicitação: "2023-10-01"
  • Campo Urgente: [x] Urgente
  • Campo Descrição do Problema: "Fuga de água na cozinha."
Resultado: A assistência é registrada como urgente e aparece na lista de assistências.
```

**Exemplo 2: Solicitação de Assistência Não Urgente**
```
Situação: Um cliente solicita assistência para um problema no aquecedor.
Ação: 
  • Campo Empreendimento: "Empreendimento B"
  • Campo Unidade: "Unidade 202"
  • Campo Data da Solicitação: "2023-10-02"
  • Campo Urgente: [ ] Urgente
  • Campo Descrição do Problema: "Aquecedor não está funcionando."
Resultado: A assistência é registrada e aparece na lista de assistências com status normal.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O item deve estar cadastrado com o prazo de garantia definido.
- **Habilita:** A possibilidade de gerenciar assistências técnicas e acompanhar o status.
- **Relacionado a:** Módulo de Itens e Módulo de Empreendimentos.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como configurar uma assistência técnica?"
- **Com problema:** "Não consigo registrar uma assistência, o que fazer?"
- **Informal:** "Como faço pra pedir assistência?"
- **Por sintoma:** "O que fazer se a unidade não aparece na lista de assistência?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Registrar assistência", "solicitar assistência", "abrir chamado", "pedir ajuda"
- "Assistência técnica", "suporte técnico", "ajuda técnica"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como definir o prazo de garantia para um item?
- O que fazer se a unidade não aparece na lista de seleção?
- Como sinalizar uma assistência como urgente?
- O que fazer se não consigo salvar a solicitação de assistência?
- O que preciso ter feito antes de solicitar uma assistência técnica?

---


---


---

## 3. Análise de Garantia e Vistoria

**📋 METADADOS:**
- **ID:** sec_3
- **⏱️ Minutagem:** 05:02 → 07:37
- **⏲️ Duração:** 154s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/lefybyzpmgY?si=YfjXcK_ZY3ZoekrC&t=302)
- **📦 Módulo:** Análise e Vistoria
- **🏷️ Categorias:** Análise, Vistoria, Aprovação, Materiais
- **🔑 Palavras-chave:** análise de garantia, vistoria, pré-vistoria, aprovação, reprovação, materiais

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de análise de garantia e vistoria em um sistema de assistência técnica, abordando desde a verificação da garantia até a aprovação ou reprovação do serviço, incluindo a gestão de materiais.

**Contexto:**
Estamos na etapa de análise de um sistema de assistência técnica, onde o usuário deve verificar a garantia do produto, realizar uma vistoria e aprovar ou reprovar o serviço solicitado.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Análise e Vistoria > Submenu Análise de Garantia
- Tela/interface específica: Tela de Análise de Garantia e Vistoria

**Funcionalidade Detalhada:**
Esta funcionalidade permite ao usuário verificar a garantia de um produto, realizar uma vistoria e aprovar ou reprovar a assistência técnica. É essencial para garantir que o serviço prestado esteja de acordo com as políticas da empresa e que os materiais necessários sejam geridos adequadamente.

### 🔹 Passo a Passo Detalhado:

1. **Iniciar a Análise**
   - Localização: Tela de Análise de Garantia
   - Como fazer: Clique no botão **Iniciar Análise** para começar o processo.
   - Resultado esperado: O sistema abre a seção de verificação de garantia.

2. **Verificar Garantia**
   - Localização: Seção de Verificação de Garantia
   - Como fazer: Clique em **Analisar Garantia**.
   - Campos/Opções disponíveis:
     * `Possui Garantia`: Selecione **Sim** ou **Não**.
     * `Comentários`: Campo de texto para adicionar observações sobre a análise.
   - Resultado esperado: O sistema registra a verificação da garantia.

3. **Salvar Análise de Garantia**
   - Localização: Botão **Salvar** na parte inferior da tela
   - Como fazer: Após preencher os campos, clique em **Salvar**.
   - Resultado esperado: As informações sobre a garantia são salvas no sistema.

4. **Vistoria**
   - Localização: Seção de Vistoria
   - Como fazer: Escolha entre as opções:
     * **Pular esta etapa**: Clique em **Pular** e forneça uma justificativa.
     * **Realizar Pré-Vistoria**: Clique em **Pré-Vistoria**.
   - Observações importantes: Se optar por pular, é necessário justificar a decisão.
   - Resultado esperado: Se a pré-vistoria for realizada, o sistema solicitará a data e comentários.

5. **Registrar Pré-Vistoria**
   - Localização: Tela de Registro de Pré-Vistoria
   - Como fazer: Preencha a data da vistoria e adicione comentários sobre o processo.
   - Campos/Opções disponíveis:
     * `Data da Vistoria`: Campo de data.
     * `Comentários`: Campo de texto para observações.
   - Resultado esperado: As informações da pré-vistoria são salvas.

6. **Aprovação ou Reprovação**
   - Localização: Seção de Aprovação
   - Como fazer: Escolha entre **Aprovar** ou **Reprovar** a assistência.
   - Observações importantes: Se a assistência for reprovada, o fluxo é encerrado.
   - Resultado esperado: O sistema registra a decisão e permite adicionar um parecer.

7. **Salvar Aprovação**
   - Localização: Botão **Salvar** na parte inferior da tela
   - Como fazer: Após a decisão, clique em **Salvar**.
   - Resultado esperado: A decisão de aprovação ou reprovação é registrada.

8. **Gerenciamento de Materiais**
   - Localização: Seção de Materiais
   - Como fazer: Escolha entre as opções:
     * **Pular esta etapa**: Clique em **Pular** e forneça uma justificativa.
     * **Solicitar Material**: Inicie o fluxo de compras.
     * **Compra Direta**: Formalize a compra já realizada.
   - Observações importantes: Se optar por pular, justifique a decisão.
   - Resultado esperado: O sistema registra a escolha feita em relação aos materiais.

9. **Salvar Etapa de Materiais**
   - Localização: Botão **Salvar** na parte inferior da tela
   - Como fazer: Após a decisão sobre os materiais, clique em **Salvar**.
   - Resultado esperado: As informações sobre a etapa de materiais são salvas.

**Campos e Parâmetros:**

| Campo                  | Tipo         | Obrigatório | Descrição                                         | Exemplo                  |
|------------------------|--------------|-------------|---------------------------------------------------|--------------------------|
| `Possui Garantia`      | Dropdown     | Sim         | Indica se o produto possui garantia.              | Sim / Não                |
| `Comentários`          | Texto livre  | Não         | Observações sobre a análise de garantia.          | "Produto em bom estado." |
| `Data da Vistoria`     | Data         | Sim         | Data em que a pré-vistoria foi realizada.        | 2023-10-01               |
| `Comentários Vistoria` | Texto livre  | Não         | Observações sobre a pré-vistoria.                | "Vistoria realizada."     |

**Regras de Negócio:**
- A análise de garantia deve ser feita antes da vistoria.
- Se a assistência for reprovada, o fluxo de serviço é interrompido.
- Justificativas são obrigatórias ao pular etapas.

**Observações Importantes:**
- Sempre salve as informações após cada etapa para evitar perda de dados.
- Verifique se todos os campos obrigatórios estão preenchidos antes de salvar.
- A documentação do processo é essencial para futuras referências.

**Conceitos-Chave:**
- **Análise de Garantia**: Processo de verificação se o produto está coberto pela garantia.
- **Pré-Vistoria**: Avaliação inicial do produto antes da execução do serviço.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável               | Solução                                           | Prevenção                                   |
|-----------------------------------|------------------------------|--------------------------------------------------|---------------------------------------------|
| Botão **Salvar** desabilitado     | Campos obrigatórios não preenchidos | Preencha todos os campos obrigatórios.          | Verifique os campos antes de tentar salvar. |
| Não consegue realizar a vistoria  | Etapa anterior não concluída | Complete a análise de garantia antes da vistoria. | Siga a ordem correta das etapas.            |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre adicione comentários para documentar o processo.
- Utilize a opção de pular etapas apenas quando necessário.
- Revise as informações antes de salvar para evitar retrabalho.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Aprovação de Assistência**
```
Situação: Um cliente solicita assistência para um produto com garantia.
Ação: 
  • Campo `Possui Garantia`: "Sim"
  • Campo `Comentários`: "Produto em bom estado."
Resultado: A assistência é aprovada e registrada no sistema.
```

**Exemplo 2: Reprovação de Assistência**
```
Situação: Um cliente solicita assistência, mas o produto não está coberto pela garantia.
Ação: 
  • Campo `Possui Garantia`: "Não"
  • Campo `Comentários`: "Produto fora da garantia."
Resultado: A assistência é reprovada e o fluxo é encerrado.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O produto deve ser registrado no sistema antes da análise de garantia.
- **Habilita:** A aprovação da assistência permite iniciar o fluxo de compras para materiais.
- **Relacionado a:** Funcionalidades de gestão de materiais e relatórios de assistência técnica.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como verificar a garantia de um produto?"
- **Com problema:** "O que fazer se não consigo aprovar a assistência?"
- **Informal:** "Como faço pra ver se o produto ainda tem garantia?"
- **Por sintoma:** "Quando a assistência é reprovada, o que acontece?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Verificar garantia", "analisar garantia", "vistoria de assistência", "aprovação de serviço", "reprovação de assistência".

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como iniciar a análise de garantia?
- O que fazer se a assistência for reprovada?
- Como registrar uma pré-vistoria?
- O que fazer se o botão de salvar estiver desabilitado?
- O que preciso fazer antes de iniciar a análise de garantia?

---


---


---

## 4. Agendamento e Execução de Serviços

**📋 METADADOS:**
- **ID:** sec_4
- **⏱️ Minutagem:** 07:32 → 10:09
- **⏲️ Duração:** 156s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/lefybyzpmgY?si=YfjXcK_ZY3ZoekrC&t=452)
- **📦 Módulo:** Gestão de Assistências Técnicas
- **🏷️ Categorias:** Operacional, Agendamento, Execução, Relatório
- **🔑 Palavras-chave:** agendamento, execução, assistência técnica, pós-vistoria, finalização

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de agendamento e execução de serviços de assistência técnica, incluindo a finalização do serviço e a realização de vistorias. O objetivo é garantir que todos os passos sejam seguidos corretamente para uma gestão eficiente das assistências.

**Contexto:**
Estamos na interface do módulo de Gestão de Assistências Técnicas, onde o usuário pode gerenciar o fluxo de serviços, desde o agendamento até a finalização e vistoria.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Gestão de Assistências Técnicas > Submenu Agendamento e Execução
- Tela/interface específica: Tela de Gestão de Assistências

**Funcionalidade Detalhada:**
A funcionalidade permite ao usuário agendar a execução de serviços de assistência técnica, registrar a finalização do serviço e realizar vistorias. É essencial para manter um registro organizado e atualizado das assistências prestadas.

### 🔹 Passo a Passo Detalhado:

1. **Agendar Execução do Serviço**
   - Localização: Botão **Mais Agendamento** na tela de Gestão de Assistências.
   - Como fazer: Clique no botão **Mais Agendamento**. Uma nova janela será aberta onde você deve inserir as informações necessárias.
   - Campos/Opções disponíveis:
     * `Data`: Seletor de data para escolher o dia do agendamento.
     * `Horário`: Campo para inserir o horário do agendamento.
     * `Comentários`: Campo de texto para adicionar observações sobre o que foi alinhado com o cliente.
   - Resultado esperado: O agendamento é salvo e aparece na lista de agendamentos.

2. **Finalizar Serviço**
   - Localização: Botão **Finalizar Serviço** na tela de Gestão de Assistências.
   - Como fazer: Após a execução do serviço, clique em **Finalizar Serviço**. Uma janela aparecerá para você confirmar a finalização.
   - Observações importantes: É necessário verificar se o serviço foi realmente finalizado antes de clicar em salvar.
   - Resultado esperado: O status do serviço é atualizado para "Finalizado" e você pode adicionar comentários sobre o processo.

3. **Adicionar Informativos e Documentação**
   - Localização: Área de informativos na tela de finalização do serviço.
   - Como fazer: Após finalizar o serviço, você pode anexar arquivos, como fotos ou documentos relacionados à execução.
   - Resultado esperado: Os arquivos são salvos junto ao registro do serviço.

4. **Realizar Pós-Vistoria**
   - Localização: Botão **Realizar Pós-Vistoria** na tela de Gestão de Assistências.
   - Como fazer: Clique em **Realizar Pós-Vistoria**. Uma nova janela será aberta para você inserir os dados da vistoria.
   - Campos/Opções disponíveis:
     * `Data da Vistoria`: Seletor de data para registrar quando a vistoria foi realizada.
     * `Aprovada`: Opção para marcar se a vistoria foi aprovada ou não.
     * `Comentários`: Campo de texto para adicionar observações sobre a vistoria.
   - Resultado esperado: Os dados da pós-vistoria são salvos e o status da assistência é atualizado.

5. **Reabrir Assistência (se necessário)**
   - Localização: Opção disponível na tela de Gestão de Assistências.
   - Como fazer: Se a assistência precisar ser reaberta, clique na opção **Reabrir Assistência**.
   - Resultado esperado: A assistência é reaberta para novos agendamentos ou execuções.

**Campos e Parâmetros:**

| Campo                | Tipo         | Obrigatório | Descrição                                               | Exemplo               |
|----------------------|--------------|-------------|---------------------------------------------------------|-----------------------|
| `Data`               | Data         | Sim         | Data do agendamento da execução do serviço.            | 15/10/2023            |
| `Horário`            | Hora         | Sim         | Horário do agendamento da execução do serviço.         | 14:00                 |
| `Comentários`        | Texto        | Não         | Observações sobre o que foi alinhado com o cliente.    | "Cliente prefere manhã"|
| `Aprovada`           | Checkbox     | Sim         | Indica se a pós-vistoria foi aprovada.                 | [ ] Aprovada          |

**Regras de Negócio:**
- O agendamento deve ser realizado após a aprovação da assistência técnica.
- A finalização do serviço deve ser registrada com comentários que justifiquem o status.
- A pós-vistoria deve ser realizada após a execução do serviço e deve incluir uma avaliação de aprovação.

**Observações Importantes:**
- Sempre verifique a data e o horário antes de salvar o agendamento.
- Comentários são importantes para manter um histórico claro das interações com o cliente.
- Caso a assistência precise ser reaberta, todos os dados anteriores serão mantidos.

**Conceitos-Chave:**
- **Agendamento**: Processo de marcar uma data e horário para a execução do serviço.
- **Pós-Vistoria**: Avaliação realizada após a execução do serviço para verificar a qualidade e a satisfação do cliente.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                     | Causa Provável                     | Solução                                   | Prevenção                               |
|------------------------------|------------------------------------|-------------------------------------------|-----------------------------------------|
| Não consigo salvar o agendamento | Campos obrigatórios não preenchidos | Verifique se todos os campos obrigatórios estão preenchidos. | Sempre revise os campos antes de salvar. |
| O botão de finalizar serviço está desabilitado | Serviço não foi executado corretamente | Certifique-se de que a execução foi registrada antes de finalizar. | Registre a execução imediatamente após a conclusão. |
| Não consigo anexar arquivos | Formato de arquivo não suportado  | Verifique se o arquivo está em um formato aceito (ex: .jpg, .pdf). | Utilize formatos de arquivo comuns. |

**💡 DICAS E BOAS PRÁTICAS:**
- Utilize o campo de comentários para registrar informações relevantes que possam ser úteis no futuro.
- Sempre revise as informações antes de finalizar um serviço para evitar erros.
- Mantenha um histórico de vistorias para facilitar a gestão de qualidade.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Agendamento de Serviço**
```
Situação: Cliente solicita assistência técnica para instalação.
Ação: 
  • Campo Data: "15/10/2023"
  • Campo Horário: "10:00"
  • Campo Comentários: "Cliente prefere pela manhã"
Resultado: Agendamento salvo com sucesso.
```

**Exemplo 2: Realização de Pós-Vistoria**
```
Situação: Após a execução do serviço, é realizada a vistoria.
Ação: 
  • Campo Data da Vistoria: "15/10/2023"
  • Campo Aprovada: [X] Aprovada
  • Campo Comentários: "Serviço executado conforme solicitado."
Resultado: Vistoria registrada e status atualizado para "Aprovada".
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** A assistência técnica deve estar aprovada antes de realizar o agendamento.
- **Habilita:** A finalização do serviço permite que o usuário realize a pós-vistoria.
- **Relacionado a:** Módulo de Gestão de Assistências Técnicas, onde todas as assistências são listadas.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como agendar um serviço?"
- **Com problema:** "Não consigo finalizar um serviço, o que fazer?"
- **Informal:** "Como eu marco um serviço?"
- **Por sintoma:** "O que fazer se o botão de finalizar não está funcionando?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Agendar assistência", "Registrar agendamento", "Finalizar serviço", "Realizar vistoria", "Registrar pós-vistoria".

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como agendar um serviço de assistência técnica?
- O que fazer se não consigo finalizar um serviço?
- Como realizar uma pós-vistoria?
- O que fazer se o agendamento não está sendo salvo?
- O que preciso fazer antes de agendar um serviço?

---


---


---

## 5. Assistência Técnica Após as Vendas

**📋 METADADOS:**
- **ID:** sec_5
- **⏱️ Minutagem:** 10:04 → 10:09
- **⏲️ Duração:** 5s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/lefybyzpmgY?si=YfjXcK_ZY3ZoekrC&t=604)
- **📦 Módulo:** Assistência Técnica
- **🏷️ Categorias:** Suporte, Pós-Venda, Atendimento ao Cliente
- **🔑 Palavras-chave:** assistência técnica, suporte, pós-venda, atendimento, cliente

> **🔍 RESUMO EXECUTIVO:** Esta seção aborda a funcionalidade de assistência técnica após as vendas, detalhando como os usuários podem acessar e utilizar os recursos de suporte disponíveis para resolver problemas pós-venda.

**Contexto:**
Estamos na interface do módulo de assistência técnica, onde os usuários podem acessar serviços de suporte após a finalização de uma venda. O objetivo é garantir que os clientes tenham acesso a ajuda e soluções para quaisquer problemas que possam surgir após a compra.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Assistência Técnica > Submenu Suporte ao Cliente
- Tela/interface específica: Tela de Suporte ao Cliente

**Funcionalidade Detalhada:**

A funcionalidade de assistência técnica após as vendas permite que os usuários solicitem suporte para resolver problemas relacionados a produtos adquiridos. Esta funcionalidade é essencial para garantir a satisfação do cliente e a resolução eficaz de problemas.

### 🔹 Passo a Passo Detalhado:

1. **Acessar o Módulo de Assistência Técnica**
   - Localização: Menu Principal na barra lateral esquerda
   - Como fazer: Clique no menu **Assistência Técnica** para expandir as opções disponíveis.
   - Resultado esperado: O submenu **Suporte ao Cliente** será exibido.

2. **Selecionar Suporte ao Cliente**
   - Localização: Submenu Assistência Técnica
   - Como fazer: Clique na opção **Suporte ao Cliente**.
   - Resultado esperado: A tela de suporte ao cliente será carregada, exibindo opções de contato e recursos de ajuda.

3. **Preencher o Formulário de Solicitação de Suporte**
   - Localização: Tela de Suporte ao Cliente
   - Como fazer: Preencha os campos do formulário de solicitação de suporte.
   - Campos/Opções disponíveis:
     * `Nome do Cliente`: Campo de texto (obrigatório) - Insira o nome completo do cliente.
     * `Descrição do Problema`: Campo de texto longo (obrigatório) - Descreva detalhadamente o problema enfrentado.
   - Resultado esperado: O formulário deve ser enviado com sucesso, e uma confirmação de recebimento será exibida.

4. **Acompanhar o Status da Solicitação**
   - Localização: Tela de Suporte ao Cliente
   - Como fazer: Clique na aba **Minhas Solicitações** para visualizar o status das solicitações anteriores.
   - Resultado esperado: Uma lista de solicitações com seus respectivos status (Pendente, Em Andamento, Resolvido) será exibida.

**Campos e Parâmetros:**

| Campo                   | Tipo            | Obrigatório | Descrição                                      | Exemplo               |
|-------------------------|-----------------|-------------|------------------------------------------------|-----------------------|
| Nome do Cliente         | Texto           | Sim         | Nome completo do cliente que solicita suporte. | João Silva            |
| Descrição do Problema   | Texto longo     | Sim         | Detalhes sobre o problema enfrentado.          | O produto não liga.   |

**Regras de Negócio:**
- O campo `Nome do Cliente` deve ser preenchido com um nome válido.
- O campo `Descrição do Problema` deve conter pelo menos 10 caracteres.
- Solicitações sem informações completas não serão processadas.

**Observações Importantes:**
- É recomendável que o cliente tenha em mãos o número do pedido ao solicitar suporte.
- Evite usar jargões técnicos na descrição do problema para facilitar a compreensão.

**Conceitos-Chave:**
- **Assistência Técnica**: Serviço oferecido para resolver problemas relacionados a produtos após a venda.
- **Solicitação de Suporte**: Processo pelo qual um cliente pede ajuda para resolver um problema.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                       | Solução                                       | Prevenção                                    |
|-----------------------------------|--------------------------------------|-----------------------------------------------|----------------------------------------------|
| Formulário não é enviado          | Campos obrigatórios não preenchidos  | Verifique se todos os campos obrigatórios estão preenchidos. | Sempre revise o formulário antes de enviar. |
| Solicitação não aparece na lista  | Problema de conexão ou erro no sistema | Tente recarregar a página ou verificar a conexão com a internet. | Mantenha uma conexão estável ao usar o sistema. |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre forneça detalhes suficientes na descrição do problema para agilizar o atendimento.
- Utilize a aba **Minhas Solicitações** para acompanhar o progresso do seu pedido de suporte.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Solicitação de Suporte para Produto com Defeito**
```
Situação: O cliente comprou um aparelho de som que não liga.
Ação: O cliente acessa o módulo de assistência técnica, preenche o formulário com:
  • Nome do Cliente: "Maria Oliveira"
  • Descrição do Problema: "O aparelho de som não liga, mesmo após tentar trocar a tomada."
Resultado: A solicitação é enviada e o cliente recebe uma confirmação.
```

**Exemplo 2: Solicitação de Suporte para Dúvida sobre Funcionamento**
```
Situação: O cliente tem dúvidas sobre como usar uma funcionalidade do software adquirido.
Ação: O cliente acessa o módulo de assistência técnica, preenche o formulário com:
  • Nome do Cliente: "Carlos Almeida"
  • Descrição do Problema: "Não consigo entender como configurar as opções de áudio no software."
Resultado: A solicitação é enviada e o cliente recebe uma confirmação.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O cliente deve ter um produto registrado no sistema para solicitar suporte.
- **Habilita:** A funcionalidade de acompanhamento de solicitações permite que o cliente veja o status de suas interações com o suporte.
- **Relacionado a:** Módulo de Vendas, onde os produtos são registrados e geridos.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como solicitar assistência técnica?"
- **Com problema:** "Não consigo enviar uma solicitação de suporte, o que fazer?"
- **Informal:** "Como eu peço ajuda depois de comprar algo?"
- **Por sintoma:** "Meu produto não está funcionando, como posso resolver isso?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "suporte pós-venda", "ajuda ao cliente", "assistência ao consumidor", "suporte técnico".

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como faço para solicitar assistência técnica?
- O que fazer se o formulário de suporte não enviar?
- Como posso acompanhar o status da minha solicitação de suporte?
- O que fazer se não recebi confirmação da minha solicitação?
- O que preciso ter antes de solicitar assistência técnica?

---


---




---


## 🎬 DADOS DE TIMESTAMPS (Para Sistema RAG)


[VIDEO_TIMESTAMPS_DATA]

{
  "Passo a passo - Módulo de Qualidade": [
    {
      "start": "00:01",
      "end": "02:33",
      "line": "Olá, neste vídeo irei realizar uma apresentação completa quanto ao funcionamento do módulo qualidade"
    },
    {
      "start": "02:31",
      "end": "05:05",
      "line": "Para esses períodos, temos as definições entre meses e dias. Então aqui basta definir o seu prazo qu"
    },
    {
      "start": "05:02",
      "end": "07:37",
      "line": "a análise, que nesse momento vamos percorrer pela linha do tempo em relação à análise, materiais e s"
    },
    {
      "start": "07:32",
      "end": "10:09",
      "line": "e iniciamos a dinâmica de serviços. Aqui dentro do serviço, o primeiro passo após aprovar uma assist"
    },
    {
      "start": "10:04",
      "end": "10:09",
      "line": "assistência técnica após as vendas."
    }
  ]
}

[/VIDEO_TIMESTAMPS_DATA]
