# 📚 Documentação: Passo a passo - Módulo de Qualidade

**🎥 Vídeo Original:** https://youtu.be/lefybyzpmgY?si=YfjXcK_ZY3ZoekrC

**📊 Total de Seções:** 5

---

---

## 1. Cadastro de Categorias e Itens de Assistência no Módulo Qualidade

**📋 METADADOS:**
- **ID:** sec_1
- **⏱️ Minutagem:** 00:01 → 02:33
- **⏲️ Duração:** 152s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/lefybyzpmgY?si=YfjXcK_ZY3ZoekrC&t=1)
- **📦 Módulo:** Módulo Qualidade
- **🏷️ Categorias:** Cadastro, Configuração, Assistência, Garantia
- **🔑 Palavras-chave:** categoria, subcategoria, item de assistência, cadastro, garantia, editar, excluir

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como cadastrar categorias e itens de assistência no Módulo Qualidade, permitindo que os usuários gerenciem o fluxo do pós-vendas de forma eficiente.

**Contexto:**
Estamos no Módulo Qualidade, que tem como objetivo gerenciar o fluxo do pós-vendas. Esta seção se concentra nos cadastros iniciais necessários para a configuração do sistema, começando pelas categorias de assistência.

**Localização no Sistema:**
- Caminho de navegação: Menu Principal > Módulo Qualidade > Cadastros > Categorias de Assistências
- Tela/interface específica: Tela de Cadastro de Categorias de Assistências

**Funcionalidade Detalhada:**
O Módulo Qualidade permite o cadastro de categorias e subcategorias de assistência, que são essenciais para a definição dos itens que terão garantia. Os usuários podem visualizar categorias pré-cadastradas e adicionar novas, além de editar ou excluir categorias existentes.

### 🔹 Passo a Passo Detalhado:

1. **Acessar o Módulo Qualidade**
   - Localização: Menu Principal
   - Como fazer: Clique no ícone do **Módulo Qualidade** para acessá-lo.
   - Resultado esperado: O sistema exibe a interface do Módulo Qualidade.

2. **Navegar até Cadastros**
   - Localização: Menu lateral do Módulo Qualidade
   - Como fazer: Clique na opção **Cadastros**.
   - Resultado esperado: O sistema apresenta as opções de cadastro disponíveis.

3. **Selecionar Categorias de Assistências**
   - Localização: Aba de **Categorias de Assistências**
   - Como fazer: Clique na aba **Categorias de Assistências**.
   - Resultado esperado: A tela exibe as categorias de assistência já cadastradas e a opção de adicionar novas.

4. **Cadastrar uma Nova Categoria**
   - Localização: Tela de Categorias de Assistências
   - Como fazer: Clique no botão **Mais Categoria**.
   - Campos/Opções disponíveis:
     * `Nome da Categoria`: Campo de texto onde você deve inserir o nome da nova categoria.
   - Resultado esperado: Uma nova categoria é criada após clicar em **Salvar**.

5. **Adicionar Subcategoria**
   - Localização: Lateral da categoria recém-cadastrada
   - Como fazer: Clique no botão **Mais** ao lado da categoria desejada.
   - Campos/Opções disponíveis:
     * `Nome da Subcategoria`: Campo de texto onde você deve inserir o nome da subcategoria.
   - Resultado esperado: A subcategoria é adicionada à categoria selecionada após clicar em **Salvar**.

6. **Editar ou Excluir Categorias/Subcategorias**
   - Localização: Lista de categorias/subcategorias
   - Como fazer: Clique no ícone de **Editar** ou **Excluir** ao lado da categoria/subcategoria desejada.
   - Resultado esperado: O sistema permite modificar ou remover a categoria/subcategoria selecionada.

7. **Acessar Itens de Assistência**
   - Localização: Aba de **Itens de Assistência**
   - Como fazer: Clique na aba **Itens de Assistência**.
   - Resultado esperado: A tela exibe a opção de cadastrar novos itens de assistência.

8. **Cadastrar um Novo Item de Assistência**
   - Localização: Tela de Itens de Assistência
   - Como fazer: Clique no botão **Mais Item**.
   - Campos/Opções disponíveis:
     * `Categoria`: Seletor onde você deve escolher a categoria correspondente.
     * `Subcategoria`: Seletor onde você deve escolher a subcategoria correspondente.
     * `Nome do Item`: Campo de texto onde você deve inserir o nome do novo item.
   - Resultado esperado: O novo item de assistência é cadastrado após selecionar as opções e clicar em **Salvar**.

9. **Selecionar Empreendimentos**
   - Localização: Tela de cadastro do item de assistência
   - Como fazer: Arraste para o lado ou clique na mãozinha para selecionar os empreendimentos que oferecem garantia para o item.
   - Resultado esperado: Os empreendimentos selecionados são associados ao item de assistência.

10. **Definir Garantia**
    - Localização: Tela de cadastro do item de assistência
    - Como fazer: Escolha entre as opções de garantia, que podem ser até o ato da entrega pelo fabricante ou durante um período fornecido pela construtora.
    - Resultado esperado: A garantia é definida para o item de assistência cadastrado.

**Campos e Parâmetros:**

| Campo                   | Tipo         | Obrigatório | Descrição                                                       | Exemplo                |
|-------------------------|--------------|-------------|-----------------------------------------------------------------|------------------------|
| Nome da Categoria       | Texto        | Sim         | Nome da nova categoria de assistência.                          | "Assistência Técnica"  |
| Nome da Subcategoria    | Texto        | Sim         | Nome da nova subcategoria de assistência.                       | "Reparo Elétrico"      |
| Categoria               | Dropdown     | Sim         | Seletor para escolher a categoria do item de assistência.      | "Assistência Técnica"  |
| Subcategoria            | Dropdown     | Sim         | Seletor para escolher a subcategoria do item de assistência.   | "Reparo Elétrico"      |
| Nome do Item            | Texto        | Sim         | Nome do novo item de assistência a ser cadastrado.            | "Ferro de Passar"      |
| Empreendimentos         | Checkbox      | Não         | Seleção dos empreendimentos que oferecem garantia para o item. | "Empreendimento A"     |
| Garantia                | Radio Button | Sim         | Opção para definir o tipo de garantia do item.                 | "Até entrega do fabricante" |

**Regras de Negócio:**
- As categorias e subcategorias devem ser cadastradas antes de cadastrar itens de assistência.
- É possível editar ou excluir categorias e subcategorias já cadastradas.
- Cada item de assistência deve estar associado a pelo menos uma categoria e subcategoria.
- A garantia deve ser definida no momento do cadastro do item de assistência.

**Observações Importantes:**
- Sempre verifique se a categoria e subcategoria estão corretas antes de salvar.
- Evite cadastrar categorias ou subcategorias duplicadas.
- Utilize os ícones de editar e excluir com cautela, pois a exclusão é permanente.

**Conceitos-Chave:**
- **Categoria**: Classificação principal para agrupar itens de assistência.
- **Subcategoria**: Classificação secundária que fornece mais detalhes sobre a categoria.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como cadastrar uma nova categoria de assistência?
- Quais são os passos para adicionar uma subcategoria?
- Como posso cadastrar um item de assistência e definir sua garantia?

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
- **🏷️ Categorias:** Configuração, Operacional, Cadastro
- **🔑 Palavras-chave:** assistência técnica, solicitação, garantia, editar, excluir

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de configuração e gerenciamento de assistências técnicas no sistema, desde a solicitação até a execução do serviço, permitindo que os usuários registrem e acompanhem as assistências de forma eficiente.

**Contexto:**
Estamos no módulo de Assistências Técnicas, onde os usuários podem gerenciar solicitações de assistência relacionadas a itens garantidos. O objetivo desta seção é guiar o usuário através do processo de criação e acompanhamento de assistências técnicas.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Assistências Técnicas > Submenu Criar Assistência
- Tela/interface específica: Tela de Criação de Assistência Técnica

**Funcionalidade Detalhada:**
A funcionalidade de Assistências Técnicas permite que os usuários registrem solicitações de assistência para itens garantidos. O fluxo inclui a definição do empreendimento, a unidade relacionada, a descrição do problema e a seleção dos itens que fazem parte da assistência. É possível marcar a assistência como urgente e acompanhar o status da solicitação.

### 🔹 Passo a Passo Detalhado:

1. **Iniciar um Novo Fluxo de Assistência**
   - Localização: Tela de Criação de Assistência Técnica
   - Como fazer: Clique no botão **"Mais Assistência"** para iniciar um novo fluxo de assistência técnica.
   - Resultado esperado: O sistema abrirá um formulário para preenchimento das informações da assistência.

2. **Definir o Empreendimento e Unidade**
   - Localização: Campo de seleção na tela de criação de assistência
   - Como fazer: Selecione o empreendimento relacionado à assistência. Em seguida, escolha a unidade que foi entregue.
   - Observações importantes: Apenas as unidades para as quais as chaves já foram entregues estarão disponíveis para seleção.
   - Resultado esperado: A unidade selecionada será exibida no formulário.

3. **Informar o Cliente Relacionado**
   - Localização: Informativo na tela de criação de assistência
   - Como fazer: O sistema automaticamente exibirá o cliente relacionado à unidade selecionada.
   - Resultado esperado: O cliente associado à unidade será visível no formulário.

4. **Definir a Data da Solicitação**
   - Localização: Campo de data na tela de criação de assistência
   - Como fazer: Insira a data em que a solicitação de assistência está sendo feita.
   - Resultado esperado: A data da solicitação será registrada no sistema.

5. **Marcar a Assistência como Urgente**
   - Localização: Opção de seleção na tela de criação de assistência
   - Como fazer: Marque a opção **"Urgente"** se a assistência requerer atenção imediata.
   - Resultado esperado: A assistência será identificada como urgente no sistema.

6. **Descrever o Problema**
   - Localização: Campo de descrição na tela de criação de assistência
   - Como fazer: Insira uma descrição detalhada do problema que requer assistência.
   - Resultado esperado: A descrição do problema será registrada e associada à solicitação.

7. **Selecionar Itens Relacionados à Assistência**
   - Localização: Tela de seleção de itens
   - Como fazer: Clique em **"Próximo"** para acessar a tela de seleção de itens. Filtre os itens pela categoria e subcategoria para localizar os itens garantidos relacionados à assistência.
   - Campos/Opções disponíveis:
     * `Categoria`: Selecione a categoria do item (ex: Eletrodomésticos, Móveis).
     * `Subcategoria`: Selecione a subcategoria do item (ex: Refrigeradores, Sofás).
   - Observações importantes: A seleção de itens é obrigatória e deve ser feita através do filtro.
   - Resultado esperado: Os itens relacionados à categoria e subcategoria selecionadas serão exibidos.

8. **Selecionar o Item para Assistência**
   - Localização: Lista de itens filtrados
   - Como fazer: Arraste o item desejado para o lado ou clique no ícone da mãozinha para selecioná-lo.
   - Resultado esperado: O item será adicionado à solicitação de assistência.

9. **Visualizar Informações do Item**
   - Localização: Tela de seleção de itens
   - Como fazer: Ao visualizar o item, verifique o tempo de garantia e o tempo restante de garantia para o empreendimento.
   - Resultado esperado: As informações de garantia do item serão exibidas.

10. **Salvar a Assistência**
    - Localização: Botão **"Salvar"** na tela de criação de assistência
    - Como fazer: Clique no botão **"Salvar"** para registrar a assistência técnica.
    - Resultado esperado: A assistência será iniciada e aparecerá na lista de assistências com o status atualizado.

11. **Visualizar Assistência Criada**
    - Localização: Lista de assistências
    - Como fazer: Clique na assistência recém-criada para visualizar detalhes adicionais.
    - Resultado esperado: Detalhes da assistência, incluindo status, urgência e informativos gerais, serão exibidos.

12. **Importar Arquivos Relacionados**
    - Localização: Opção de importação na tela de detalhes da assistência
    - Como fazer: Utilize a opção para importar arquivos relevantes à assistência.
    - Resultado esperado: Os arquivos importados serão associados à assistência técnica.

**Campos e Parâmetros:**

| Campo                       | Tipo         | Obrigatório | Descrição                                               | Exemplo                |
|-----------------------------|--------------|-------------|---------------------------------------------------------|------------------------|
| Empreendimento               | Dropdown     | Sim         | Seleção do empreendimento relacionado à assistência      | Empreendimento A       |
| Unidade                      | Dropdown     | Sim         | Seleção da unidade que foi entregue                     | Unidade 101            |
| Data da Solicitação          | Data         | Sim         | Data em que a solicitação de assistência é feita        | 2023-10-01             |
| Urgente                     | Checkbox     | Não         | Indica se a assistência é urgente                        | [X] Urgente            |
| Descrição do Problema        | Texto livre  | Sim         | Descrição detalhada do problema a ser assistido        | "O refrigerador não liga." |
| Categoria                    | Dropdown     | Sim         | Categoria do item relacionado à assistência             | Eletrodomésticos       |
| Subcategoria                 | Dropdown     | Sim         | Subcategoria do item relacionado à assistência          | Refrigeradores         |
| Item                         | Seleção      | Sim         | Item selecionado para a assistência                     | Refrigerador XYZ       |

**Regras de Negócio:**
- A unidade só pode ser selecionada se as chaves já tiverem sido entregues.
- A descrição do problema é um campo obrigatório.
- A seleção de itens deve ser feita através de filtros por categoria e subcategoria.

**Observações Importantes:**
- Certifique-se de que a descrição do problema seja clara e detalhada para facilitar a assistência.
- Evite selecionar unidades que não tenham as chaves entregues, pois não aparecerão na lista.
- Verifique sempre o tempo de garantia antes de registrar a assistência.

**Conceitos-Chave:**
- **Assistência Técnica**: Processo de solicitação e execução de serviços relacionados a itens garantidos.
- **Urgente**: Classificação que indica que a assistência requer atenção imediata.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como iniciar uma nova solicitação de assistência técnica?
- Quais informações são necessárias para registrar uma assistência?
- Como posso visualizar e acompanhar o status da assistência criada?

---


---


---

## 3. Análise de Garantia e Vistoria

**📋 METADADOS:**
- **ID:** sec_3
- **⏱️ Minutagem:** 05:02 → 07:37
- **⏲️ Duração:** 154s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/lefybyzpmgY?si=YfjXcK_ZY3ZoekrC&t=302)
- **📦 Módulo:** Análise de Assistência Técnica
- **🏷️ Categorias:** Análise, Vistoria, Aprovação, Materiais
- **🔑 Palavras-chave:** análise, garantia, vistoria, aprovação, reprovação, materiais, assistência técnica, pré-vistoria

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de análise de garantia e vistoria em um sistema de assistência técnica, abordando desde a verificação da garantia até a aprovação ou reprovação do serviço, além da gestão de materiais necessários.

**Contexto:**
Estamos na etapa de análise dentro do módulo de assistência técnica, onde o usuário deve verificar a garantia do produto, realizar uma vistoria e, em seguida, aprovar ou reprovar a assistência técnica solicitada.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Análise de Assistência Técnica > Submenu Análise de Garantia e Vistoria
- Tela/interface específica: Tela de Análise de Garantia e Vistoria

**Funcionalidade Detalhada:**
A funcionalidade permite ao usuário verificar a garantia do produto, realizar uma vistoria e aprovar ou reprovar a assistência técnica. O usuário pode também documentar o processo através de comentários e gerenciar a solicitação de materiais necessários para a execução do serviço.

### 🔹 Passo a Passo Detalhado:

1. **Iniciar a Análise**
   - Localização: Tela inicial da Análise de Assistência Técnica
   - Como fazer: Clique no botão **Iniciar Análise** para começar o processo.
   - Resultado esperado: O sistema inicia o processo de análise, levando o usuário à verificação da garantia.

2. **Verificar Garantia**
   - Localização: Seção de Verificação de Garantia
   - Como fazer: Clique no botão **Analisar Garantia**.
   - Campos/Opções disponíveis:
     * `Possui Garantia`: Selecione **Sim** ou **Não**.
     * `Comentários`: Campo de texto para adicionar observações sobre a análise.
   - Resultado esperado: O sistema registra a verificação da garantia e permite a adição de comentários.

3. **Salvar Análise de Garantia**
   - Localização: Após a verificação da garantia
   - Como fazer: Clique no botão **Salvar**.
   - Resultado esperado: As informações da análise de garantia são salvas no sistema.

4. **Vistoria**
   - Localização: Seção de Vistoria
   - Como fazer: Escolha entre as opções:
     * **Pular Etapa**: Se necessário, clique em **Pular** e forneça uma justificativa.
     * **Pré-Vistoria**: Clique em **Realizar Pré-Vistoria**.
   - Observações importantes: Se optar por pular, é necessário justificar a decisão.
   - Resultado esperado: O sistema avança para a próxima etapa ou registra a pré-vistoria.

5. **Realizar Pré-Vistoria**
   - Localização: Tela de Pré-Vistoria
   - Como fazer: Preencha os campos:
     * `Data da Pré-Vistoria`: Selecione a data em que a vistoria foi realizada.
     * `Comentários`: Campo de texto para descrever o processo da pré-vistoria.
   - Resultado esperado: O sistema registra a pré-vistoria e permite a adição de comentários.

6. **Salvar Pré-Vistoria**
   - Localização: Após preencher os dados da pré-vistoria
   - Como fazer: Clique no botão **Salvar**.
   - Resultado esperado: As informações da pré-vistoria são salvas no sistema.

7. **Aprovação da Assistência**
   - Localização: Seção de Aprovação
   - Como fazer: Escolha entre as opções:
     * **Aprovar**: Clique em **Aprovar** e adicione um parecer sobre a decisão.
     * **Reprovar**: Clique em **Reprovar** para interromper o fluxo de assistência.
   - Observações importantes: Se a assistência for reprovada, o serviço não será executado.
   - Resultado esperado: O sistema registra a decisão de aprovação ou reprovação.

8. **Salvar Aprovação**
   - Localização: Após a decisão de aprovação ou reprovação
   - Como fazer: Clique no botão **Salvar**.
   - Resultado esperado: A decisão é registrada no sistema.

9. **Gerenciamento de Materiais**
   - Localização: Seção de Materiais
   - Como fazer: Escolha entre as opções:
     * **Pular Etapa**: Clique em **Pular** e forneça uma justificativa.
     * **Solicitar Material**: Clique em **Solicitar Material** para iniciar o fluxo de compras.
     * **Compra Direta**: Clique em **Compra Direta** se o material já foi adquirido.
   - Resultado esperado: O sistema avança conforme a opção escolhida.

10. **Salvar Etapa de Materiais**
    - Localização: Após a escolha na seção de materiais
    - Como fazer: Clique no botão **Salvar**.
    - Resultado esperado: As informações sobre materiais são salvas no sistema.

**Campos e Parâmetros:**

| Campo                | Tipo         | Obrigatório | Descrição                                               | Exemplo                |
|----------------------|--------------|-------------|--------------------------------------------------------|------------------------|
| `Possui Garantia`    | Dropdown     | Sim         | Indica se o produto possui garantia.                   | Sim / Não              |
| `Comentários`        | Texto livre  | Não         | Observações sobre a análise de garantia ou vistoria.   | "Produto em garantia." |
| `Data da Pré-Vistoria` | Data       | Sim         | Data em que a pré-vistoria foi realizada.             | 01/10/2023             |
| `Parecer`            | Texto livre  | Não         | Observações sobre a decisão de aprovação ou reprovação. | "Aprovação necessária." |
| `Justificativa`      | Texto livre  | Sim (se pular) | Justificativa para pular etapas.                       | "Produtos em estoque." |

**Regras de Negócio:**
- A verificação da garantia deve ser realizada antes de qualquer vistoria.
- Se a assistência for reprovada, o fluxo de assistência é interrompido.
- Justificativas são obrigatórias ao pular etapas.

**Observações Importantes:**
- É importante documentar todo o processo através de comentários.
- Erros comuns incluem não salvar as etapas após preenchimento.
- Verifique se todos os campos obrigatórios estão preenchidos antes de salvar.

**Conceitos-Chave:**
- **Pré-Vistoria**: Avaliação inicial do produto antes da execução do serviço.
- **Aprovação/Reprovação**: Decisão final sobre a assistência técnica solicitada.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como verificar a garantia de um produto no sistema?
- O que fazer se a assistência técnica for reprovada?
- Como gerenciar a solicitação de materiais necessários para a assistência?

---


---


---

## 4. Dinâmica de Serviços

**📋 METADADOS:**
- **ID:** sec_4
- **⏱️ Minutagem:** 07:32 → 10:09
- **⏲️ Duração:** 156s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/lefybyzpmgY?si=YfjXcK_ZY3ZoekrC&t=452)
- **📦 Módulo:** Serviços
- **🏷️ Categorias:** Operacional, Agendamento, Execução, Vistoria
- **🔑 Palavras-chave:** agendamento, assistência técnica, execução de serviço, pós-vistoria, comentários

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de agendamento e execução de serviços de assistência técnica, incluindo a realização de vistorias e a documentação necessária. O objetivo é garantir que os usuários possam gerenciar eficientemente as assistências técnicas, desde o agendamento até a finalização.

**Contexto:**
Estamos no módulo de Serviços do sistema, onde o usuário pode gerenciar assistências técnicas. Esta seção foca na dinâmica de serviços, que envolve o agendamento, execução e vistoria das assistências.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Serviços > Dinâmica de Serviços
- Tela/interface específica: Tela de Gestão de Assistências Técnicas

**Funcionalidade Detalhada:**

A funcionalidade de dinâmica de serviços permite ao usuário agendar, executar e realizar vistorias em serviços de assistência técnica. O processo começa com a aprovação de uma assistência técnica, seguido pelo agendamento com o cliente. Após a execução do serviço, o usuário pode finalizar o atendimento e registrar informações relevantes, incluindo comentários e arquivos relacionados.

### 🔹 Passo a Passo Detalhado:

1. **Agendar Serviço**
   - Localização: Tela de Gestão de Assistências Técnicas
   - Como fazer: Clique no botão **"Mais Agendamento"**.
   - Campos/Opções disponíveis:
     * `Data`: Seletor de data para escolher o dia do agendamento.
     * `Horário`: Campo para inserir o horário do agendamento.
     * `Comentários`: Campo de texto para adicionar observações sobre o que foi alinhado com o cliente.
   - Resultado esperado: O agendamento é salvo e registrado no sistema.

2. **Executar Serviço**
   - Localização: Tela de Gestão de Assistências Técnicas, após o agendamento.
   - Como fazer: Clique no botão **"Finalizar Serviço"**.
   - Observações importantes: É necessário verificar se o serviço foi finalizado corretamente.
   - Resultado esperado: O status do serviço é atualizado e comentários podem ser adicionados.

3. **Registrar Informativos**
   - Localização: Após a finalização do serviço.
   - Como fazer: Utilize a opção para adicionar arquivos, como fotos ou documentos relacionados à execução do serviço.
   - Resultado esperado: Os informativos são salvos e associados ao serviço.

4. **Realizar Pós-Vistoria**
   - Localização: Tela de Gestão de Assistências Técnicas, após a execução do serviço.
   - Como fazer: Clique em **"Realizar Pós-Vistoria"**.
   - Campos/Opções disponíveis:
     * `Data`: Seletor de data para registrar quando a vistoria foi realizada.
     * `Aprovada`: Opção para indicar se a vistoria foi aprovada ou não.
     * `Comentários`: Campo de texto para adicionar observações sobre a vistoria.
   - Resultado esperado: A pós-vistoria é registrada e salva no sistema.

5. **Reabrir Assistência (se necessário)**
   - Localização: Tela de Gestão de Assistências Técnicas.
   - Como fazer: Utilize a opção de reabrir a assistência, caso necessário.
   - Resultado esperado: A assistência é reaberta para novas ações.

6. **Finalizar Assistência Técnica**
   - Localização: Após a aprovação da assistência técnica.
   - Como fazer: Confirme a aprovação para concluir o processo.
   - Resultado esperado: A assistência técnica é marcada como concluída.

7. **Visualizar Assistências**
   - Localização: Tela inicial do módulo de Serviços.
   - Como fazer: Utilize os filtros e a pesquisa direta para visualizar assistências em aberto ou finalizadas.
   - Resultado esperado: Uma listagem de todas as assistências, com seus respectivos status.

**Campos e Parâmetros:**

| Campo             | Tipo      | Obrigatório | Descrição                                        | Exemplo               |
|-------------------|-----------|-------------|--------------------------------------------------|-----------------------|
| `Data`            | Data      | Sim         | Data do agendamento ou da vistoria.             | 15/10/2023            |
| `Horário`         | Horário   | Sim         | Horário do agendamento.                          | 14:00                 |
| `Comentários`     | Texto     | Não         | Observações sobre o agendamento ou vistoria.    | "Cliente preferiu à tarde." |
| `Aprovada`        | Checkbox  | Sim         | Indica se a vistoria foi aprovada.              | [ ] Sim / [ ] Não     |

**Regras de Negócio:**
- O agendamento deve ser realizado após a aprovação da assistência técnica.
- A execução do serviço deve ser finalizada antes de registrar a pós-vistoria.
- Comentários são opcionais, mas recomendados para melhor documentação.
- A assistência pode ser reaberta se necessário, caso contrário, deve ser marcada como concluída.

**Observações Importantes:**
- Sempre verifique a data e horário do agendamento com o cliente.
- Evite erros comuns, como não registrar a pós-vistoria.
- Certifique-se de que todos os campos obrigatórios estão preenchidos antes de salvar.

**Conceitos-Chave:**
- **Agendamento**: Processo de marcar uma data e horário para a execução do serviço.
- **Pós-Vistoria**: Avaliação realizada após a execução do serviço para verificar a qualidade do trabalho.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como agendar um serviço de assistência técnica?
- O que fazer após a execução do serviço?
- Como registrar uma pós-vistoria e quais informações são necessárias?

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
- **🏷️ Categorias:** Suporte, Pós-venda, Atendimento ao Cliente
- **🔑 Palavras-chave:** assistência técnica, suporte, pós-venda, atendimento, cliente

> **🔍 RESUMO EXECUTIVO:** Esta seção aborda a funcionalidade de assistência técnica após as vendas, destacando a importância do suporte ao cliente e como ele pode ser acessado.

**Contexto:**
Estamos na interface do módulo de assistência técnica, onde os usuários podem acessar recursos e informações relacionadas ao suporte pós-venda. O objetivo desta seção é explicar como a assistência técnica é disponibilizada aos clientes após a conclusão de uma venda.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Assistência Técnica
- Tela/interface específica: Tela de Assistência Técnica

**Funcionalidade Detalhada:**

A funcionalidade de assistência técnica após as vendas permite que os clientes tenham acesso a suporte e resolução de problemas relacionados aos produtos adquiridos. Este suporte é essencial para garantir a satisfação do cliente e a continuidade do uso dos produtos. A assistência técnica pode incluir desde orientações sobre o uso do produto até a resolução de problemas técnicos.

### 🔹 Passo a Passo Detalhado:

1. **Acessar a Assistência Técnica**
   - Localização: Menu Principal > Módulo Assistência Técnica
   - Como fazer: Clique no menu "Assistência Técnica" no painel lateral esquerdo da interface.
   - Resultado esperado: A tela de assistência técnica será exibida, mostrando opções de suporte disponíveis.

2. **Selecionar Tipo de Suporte**
   - Localização: Tela de Assistência Técnica
   - Como fazer: Na tela, você verá uma lista de opções de suporte, como "Suporte Técnico", "FAQ", "Contato com o Suporte".
   - Observações importantes: Escolha a opção que melhor se adequa à sua necessidade.
   - Resultado esperado: A seção correspondente ao tipo de suporte selecionado será aberta, apresentando informações detalhadas.

**Campos e Parâmetros:**

| Campo                  | Tipo       | Obrigatório | Descrição                                      | Exemplo                     |
|------------------------|------------|-------------|------------------------------------------------|-----------------------------|
| Tipo de Suporte        | Dropdown   | Sim         | Seleciona o tipo de suporte desejado           | Suporte Técnico, FAQ        |
| Descrição do Problema  | Texto livre| Sim         | Campo para descrever o problema enfrentado     | "O produto não liga."      |
| Contato                | Texto      | Não         | Informações de contato do cliente               | "cliente@exemplo.com"      |

**Regras de Negócio:**
- O cliente deve selecionar um tipo de suporte antes de prosseguir.
- A descrição do problema deve ser clara e concisa para facilitar a assistência.
- O contato é opcional, mas recomendado para um retorno mais rápido.

**Observações Importantes:**
- É importante que o cliente forneça o máximo de detalhes possível sobre o problema para uma melhor assistência.
- Erros comuns a evitar incluem não selecionar um tipo de suporte ou deixar a descrição do problema em branco.
- Dependências incluem ter um produto registrado no sistema para acessar a assistência técnica.

**Conceitos-Chave:**
- **Assistência Técnica**: Suporte oferecido aos clientes após a venda de um produto, visando resolver problemas e dúvidas.
- **Suporte Pós-venda**: Conjunto de serviços e assistência fornecidos aos clientes após a compra, essencial para a satisfação do cliente.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso acessar a assistência técnica após a compra?
- Quais tipos de suporte estão disponíveis para mim?
- O que devo incluir na descrição do meu problema para obter ajuda?

---


---

