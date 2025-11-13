# 📚 Documentação: Passo a passo - Módulo de Suprimentos

**🎥 Vídeo Original:** https://youtu.be/6vX7wYe8cIw?si=5Xf_VmLvM7bj6M73

**📊 Total de Seções:** 11

---

---

## 1. Acesso ao Módulo de Suplementos e Solicitações de Produtos

**📋 METADADOS:**
- **ID:** sec_1
- **⏱️ Minutagem:** 00:00 → 02:34
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/6vX7wYe8cIw?si=5Xf_VmLvM7bj6M73&t=0)
- **📦 Módulo:** Suplementos
- **🏷️ Categorias:** Operacional, Cadastro, Solicitação
- **🔑 Palavras-chave:** módulo de suplementos, solicitações, produtos, especificações, obra

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como acessar o módulo de suplementos e realizar solicitações de produtos, detalhando cada passo do processo de pedido e a importância do relacionamento com a obra.

**Contexto:**
Estamos no módulo de suplementos do sistema, onde o objetivo é realizar pedidos iniciais de produtos necessários para o fluxo de compras. A seção foca na aba de solicitações, que é o ponto de partida para a criação de pedidos.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Suplementos > Aba Solicitações
- Tela/interface específica: Tela de Solicitações de Produtos

**Funcionalidade Detalhada:**

A funcionalidade da aba de solicitações permite ao usuário realizar pedidos de produtos já cadastrados no sistema. O usuário pode buscar produtos utilizando filtros de categoria, subcategoria ou pesquisa direta. Após localizar o produto desejado, o usuário pode definir especificações como marcas, parâmetros e cores, além de adicionar a quantidade necessária. É crucial que o usuário relacione o pedido à obra correspondente, especialmente se a obra já tiver um acompanhamento pronto, pois isso permitirá comparativos entre o planejado e o executado.

### 🔹 Passo a Passo Detalhado:

1. **Acessar a Aba de Solicitações**
   - Localização: Menu Principal > Módulo Suplementos > Aba Solicitações
   - Como fazer: Clique na aba "Solicitações" para acessar a tela de pedidos.
   - Resultado esperado: A tela de solicitações de produtos é exibida, permitindo visualizar todos os produtos cadastrados.

2. **Criar uma Nova Solicitação**
   - Localização: Tela de Solicitações
   - Como fazer: Clique no botão **"Mais Solicitação"**.
   - Resultado esperado: Uma listagem de todos os produtos já cadastrados é exibida.

3. **Buscar um Produto**
   - Localização: Tela de listagem de produtos
   - Como fazer: Utilize os filtros disponíveis para buscar o item desejado. Os filtros incluem:
     * **Categoria**: Selecione uma categoria específica.
     * **Subcategoria**: Selecione uma subcategoria específica.
     * **Pesquisa Direta**: Digite o nome do produto na barra de pesquisa.
   - Resultado esperado: O sistema filtra a lista de produtos de acordo com os critérios selecionados.

4. **Selecionar um Produto**
   - Localização: Tela de listagem filtrada
   - Como fazer: Arraste o produto desejado para o lado ou clique no ícone da **"mãozinha"** ao lado do produto.
   - Resultado esperado: A tela de especificações do produto é exibida.

5. **Definir Especificações do Produto**
   - Localização: Tela de Especificações
   - Como fazer: Preencha os campos de especificações, como marcas, parâmetros e cores. Em seguida, insira a quantidade desejada e clique em **"Adicionar"**.
   - Resultado esperado: O produto é adicionado à solicitação com as especificações definidas.

6. **Relacionar o Produto à Obra**
   - Localização: Tela de Local de Consumo
   - Como fazer: Selecione a obra correspondente ao pedido. O sistema verifica se a obra possui acompanhamento pronto no módulo de engenharia.
   - Observações importantes: Se a obra já tiver acompanhamento, o sistema exibirá comparativos entre o planejado e o executado. Caso contrário, esses comparativos não estarão disponíveis.
   - Resultado esperado: O sistema valida a obra e, se aplicável, abre a tela de **"Especificar Serviços"**.

7. **Especificar Serviços**
   - Localização: Tela de Especificar Serviços
   - Como fazer: Clique na opção para especificar serviços. O sistema divide os serviços em duas categorias:
     * **Serviços com recurso alocado**: Serviços que já foram planejados para o uso do produto.
     * **Serviços sem recurso alocado**: Serviços que não foram vinculados ao produto.
   - Resultado esperado: O usuário pode realizar os vínculos necessários entre o produto e os serviços de execução.

8. **Salvar a Solicitação**
   - Localização: Tela de Solicitações
   - Como fazer: Após realizar todos os vínculos necessários, clique no botão **"Salvar"**.
   - Resultado esperado: A solicitação é salva no sistema, e o pedido é registrado.

**Campos e Parâmetros:**

| Campo                     | Tipo         | Obrigatório | Descrição                                               | Exemplo               |
|---------------------------|--------------|-------------|---------------------------------------------------------|-----------------------|
| **Produto**               | Dropdown     | Sim         | Seleção do produto desejado a ser solicitado.          | "Cimento"             |
| **Marca**                 | Texto        | Não         | Marca do produto a ser especificada.                   | "Marca X"             |
| **Parâmetros**            | Texto        | Não         | Parâmetros técnicos do produto.                         | "30kg"                |
| **Cores**                 | Texto        | Não         | Cores disponíveis para o produto.                       | "Cinza"               |
| **Quantidade**            | Numérico     | Sim         | Quantidade do produto a ser solicitada.                | "10"                  |
| **Obra**                  | Dropdown     | Sim         | Seleção da obra à qual o pedido será relacionado.      | "Obra A"              |

**Regras de Negócio:**
- Se a obra já tiver acompanhamento pronto, o sistema exibirá comparativos entre o planejado e o executado.
- Se a obra não tiver acompanhamento, os comparativos não estarão disponíveis.
- É necessário especificar serviços para realizar vínculos com os produtos solicitados.

**Observações Importantes:**
- Sempre verifique se a obra possui acompanhamento antes de realizar a solicitação.
- Evite selecionar produtos que não estão relacionados a serviços alocados, pois isso pode gerar inconsistências no planejamento.

**Conceitos-Chave:**
- **Acompanhamento Pronto**: Refere-se a uma obra que já possui dados de planejamento e execução registrados no sistema.
- **Especificar Serviços**: Processo de vincular produtos a serviços de execução dentro do sistema.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso acessar o módulo de suplementos e realizar uma solicitação de produto?
- Quais são os passos para buscar e selecionar um produto no sistema?
- O que devo fazer se a obra não tiver acompanhamento pronto no sistema?

---


---


---

## 2. Configuração de Data Limite de Entrega e Comentários em Solicitações

**📋 METADADOS:**
- **ID:** sec_2
- **⏱️ Minutagem:** 02:32 → 05:07
- **⏲️ Duração:** 155s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/6vX7wYe8cIw?si=5Xf_VmLvM7bj6M73&t=152)
- **📦 Módulo:** Solicitações de Compras
- **🏷️ Categorias:** Configuração, Solicitações, Compras
- **🔑 Palavras-chave:** data limite, entrega, comentários, status urgente, salvar, editar, excluir, histórico

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como configurar a data limite de entrega em solicitações de compras, adicionar comentários e gerenciar o status das solicitações, permitindo que os usuários acompanhem o fluxo de compras e ajustem suas solicitações conforme necessário.

**Contexto:**
Estamos na interface de criação e gerenciamento de solicitações de compras, onde o usuário pode definir prazos e adicionar informações relevantes para facilitar o processo de aprovação e acompanhamento das solicitações.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Solicitações de Compras > Tela de Criação de Solicitações
- Tela/interface específica: Tela de Criação de Solicitações

**Funcionalidade Detalhada:**

A funcionalidade permite ao usuário configurar uma data limite de entrega para os itens solicitados, que é crucial para o gerenciamento de prazos. Caso o solicitante precise dos itens antes do prazo estipulado, a solicitação será marcada como urgente. Além disso, o usuário pode optar por exibir essa data limite ao fornecedor e adicionar comentários que serão visíveis tanto para a equipe de compras quanto para o fornecedor durante o processo de orçamento.

### 🔹 Passo a Passo Detalhado:

1. **Configuração da Data Limite de Entrega**
   - Localização: Lateral da tela de criação de solicitações, no campo "Data Limite de Entrega".
   - Como fazer: Clique no campo "Data Limite de Entrega" e selecione a data desejada no calendário que aparecerá. A data pode ser configurada para um prazo específico, como 7 dias a partir da data atual.
   - Campos/Opções disponíveis:
     * `Data Limite de Entrega`: Campo de seleção de data (tipo: data).
   - Resultado esperado: A data limite de entrega é salva e utilizada para determinar o status da solicitação.

2. **Exibição do Limite ao Fornecedor**
   - Localização: Abaixo do campo "Data Limite de Entrega".
   - Como fazer: Marque a opção "Exibir limite ao fornecedor" se desejar que o fornecedor veja a data limite configurada.
   - Observações importantes: Se não marcado, o fornecedor não terá acesso à informação da data limite.
   - Resultado esperado: O fornecedor será informado ou não sobre a data limite, dependendo da seleção.

3. **Adição de Comentários**
   - Localização: Campo de comentários na tela de criação de solicitações.
   - Como fazer: Clique no campo de comentários e digite a mensagem que deseja adicionar. Este comentário será visível para a equipe de compras e pode ser exibido ao fornecedor.
   - Resultado esperado: O comentário é salvo e associado à solicitação, permitindo que a equipe de compras e o fornecedor tenham contexto adicional sobre a solicitação.

4. **Salvar Solicitação**
   - Localização: Botão "Salvar" na parte inferior da tela.
   - Como fazer: Clique em "Salvar" para registrar a solicitação. Você também pode optar por "Salvar como Rascunho" se desejar fazer alterações posteriormente.
   - Resultado esperado: A solicitação é salva no sistema, e o usuário pode continuar a edição ou retornar mais tarde.

5. **Gerenciamento de Solicitações**
   - Localização: Tela inicial de solicitações.
   - Como fazer: Após salvar, você pode visualizar a solicitação na lista de pedidos em aberto. Aqui, você pode editar ou excluir a solicitação, desde que o status esteja em aberto.
   - Observações importantes: As opções de editar e excluir só estarão disponíveis enquanto a solicitação estiver com status "Em Aberto".
   - Resultado esperado: O usuário pode acompanhar o status da solicitação e realizar alterações conforme necessário.

**Campos e Parâmetros:**

| Campo                        | Tipo     | Obrigatório | Descrição                                                                 | Exemplo          |
|------------------------------|----------|-------------|---------------------------------------------------------------------------|------------------|
| Data Limite de Entrega       | Data     | Sim         | Data até a qual os itens devem ser entregues.                           | 2023-10-30       |
| Exibir limite ao fornecedor   | Checkbox | Não         | Opção para mostrar ou ocultar a data limite para o fornecedor.          | [ ] Exibir       |
| Comentários                  | Texto    | Não         | Campo para adicionar observações que serão visíveis para a equipe de compras e fornecedor. | "Urgente!"       |

**Regras de Negócio:**
- Se a data limite de entrega for inferior ao prazo configurado, a solicitação será marcada como "Urgente".
- A opção de editar ou excluir a solicitação só estará disponível enquanto o status da solicitação estiver "Em Aberto".
- Comentários adicionados serão visíveis para a equipe de compras e podem ser exibidos ao fornecedor.

**Observações Importantes:**
- É recomendável revisar a data limite de entrega antes de salvar a solicitação para evitar problemas de urgência.
- Evite deixar o campo de comentários em branco se houver informações relevantes a serem compartilhadas.

**Conceitos-Chave:**
- **Data Limite de Entrega**: Prazo estabelecido para a entrega dos itens solicitados.
- **Status Urgente**: Indicação de que a solicitação precisa ser tratada com prioridade devido a um prazo menor que o configurado.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso configurar a data limite de entrega em uma solicitação?
- O que acontece se eu precisar dos itens antes da data limite configurada?
- Como adicionar comentários que serão visíveis para a equipe de compras e o fornecedor?

---


---


---

## 3. Gestão de Divergências na Entrada de Produtos

**📋 METADADOS:**
- **ID:** sec_3
- **⏱️ Minutagem:** 05:04 → 07:37
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/6vX7wYe8cIw?si=5Xf_VmLvM7bj6M73&t=304)
- **📦 Módulo:** Gestão de Entradas
- **🏷️ Categorias:** Operacional, Controle de Estoque, Gestão de Fornecedores
- **🔑 Palavras-chave:** divergência, entrada de produtos, justificativa, quantidade recebida, crédito fornecedor

> **🔍 RESUMO EXECUTIVO:** Esta seção aborda o processo de gestão de divergências na entrada de produtos, detalhando como identificar, justificar e resolver discrepâncias entre a quantidade prevista e a quantidade recebida.

**Contexto:**
Estamos na funcionalidade de gestão de entradas de produtos, onde o usuário pode registrar e validar a quantidade de produtos recebidos em relação ao que foi previsto. O objetivo é garantir que as entradas sejam corretamente registradas e que qualquer divergência seja tratada de maneira adequada.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Gestão de Entradas > Tela de Registro de Entradas
- Tela/interface específica: Tela de Registro de Entradas

**Funcionalidade Detalhada:**
A funcionalidade de gestão de divergências permite que o usuário verifique se a quantidade de produtos recebidos corresponde à quantidade prevista. Caso haja divergências, o sistema solicita uma justificativa e oferece opções para resolver a situação, como criar uma entrada vulsa, ignorar a divergência ou gerar um crédito com o fornecedor.

### 🔹 Passo a Passo Detalhado:

1. **Verificação da Entrada**
   - Localização: Tela de Registro de Entradas, seção de conferência de produtos.
   - Como fazer: O usuário deve comparar a quantidade prevista com a quantidade recebida. Para isso, deve acessar a entrada específica e verificar os campos correspondentes.
   - Campos/Opções disponíveis:
     * `Quantidade Prevista`: Número total de unidades que deveriam ter chegado.
     * `Quantidade Recebida`: Número total de unidades que realmente chegaram.
   - Resultado esperado: Se as quantidades coincidirem, a entrada é finalizada e o produto é disponibilizado no estoque.

2. **Identificação de Divergência**
   - Localização: Tela de Registro de Entradas, após a conferência.
   - Como fazer: Caso as quantidades não coincidam, o usuário deve registrar a quantidade recebida e clicar no botão **Salvar**.
   - Observações importantes: O sistema automaticamente solicitará uma justificativa para a divergência.
   - Resultado esperado: O sistema não finaliza a entrada e sinaliza a divergência em amarelo na lista de entradas.

3. **Registro da Justificativa**
   - Localização: Pop-up de justificativa que aparece após salvar a entrada com divergência.
   - Como fazer: O usuário deve inserir uma justificativa no campo designado e clicar em **Salvar**.
   - Campos/Opções disponíveis:
     * `Justificativa`: Campo de texto onde o usuário deve descrever o motivo da divergência.
   - Resultado esperado: A justificativa é salva e a entrada permanece pendente.

4. **Ações a partir da Divergência**
   - Localização: Tela de Registro de Entradas, na entrada com divergência sinalizada.
   - Como fazer: O responsável pode clicar na entrada pendente para visualizar as opções disponíveis.
   - Opções disponíveis:
     * **Criar Entrada Vulsa**: Para registrar a quantidade restante dos produtos divergentes.
     * **Ignorar Divergência**: Para finalizar a entrada pendente mesmo com a divergência.
     * **Gerar Crédito com o Fornecedor**: Para registrar a quantidade recebida e gerar um crédito no financeiro.
   - Resultado esperado: Dependendo da ação escolhida, o sistema executará a operação correspondente e atualizará o status da entrada.

5. **Finalização da Ação Escolhida**
   - Localização: Tela de Registro de Entradas, após selecionar uma das opções de ação.
   - Como fazer: O usuário deve inserir uma justificativa para a ação escolhida e clicar em **Salvar**.
   - Campos/Opções disponíveis:
     * `Justificativa da Ação`: Campo de texto onde o usuário deve descrever o motivo da escolha da ação.
   - Resultado esperado: O sistema finaliza a entrada e gera os fluxos necessários de acordo com a ação escolhida.

**Campos e Parâmetros:**

| Campo                     | Tipo     | Obrigatório | Descrição                                               | Exemplo            |
|---------------------------|----------|-------------|--------------------------------------------------------|--------------------|
| `Quantidade Prevista`     | Numérico | Sim         | Total de unidades que deveriam ter chegado.           | 16                 |
| `Quantidade Recebida`     | Numérico | Sim         | Total de unidades que realmente chegaram.              | 8                  |
| `Justificativa`           | Texto    | Sim         | Motivo da divergência ou da ação escolhida.           | "Recebido em atraso"|
| `Justificativa da Ação`   | Texto    | Sim         | Motivo da escolha da ação (entrada vulsa, ignorar, etc.)| "Produto não chegou"|

**Regras de Negócio:**
- A entrada só é finalizada se a quantidade recebida for igual à quantidade prevista.
- Se houver divergência, a entrada permanece pendente e é sinalizada em amarelo.
- O sistema exige uma justificativa para qualquer divergência registrada.
- O responsável pode optar por criar uma entrada vulsa, ignorar a divergência ou gerar um crédito com o fornecedor.

**Observações Importantes:**
- É essencial que a justificativa seja clara e precisa para evitar problemas futuros.
- Erros comuns incluem não registrar a justificativa ou finalizar a entrada sem resolver a divergência.
- O sistema pode exigir permissões específicas para realizar algumas ações, como gerar créditos.

**Conceitos-Chave:**
- **Entrada Vulsa**: Registro de produtos que chegaram após uma divergência, criando uma nova entrada pendente para o restante.
- **Justificativa**: Explicação necessária para registrar divergências ou ações tomadas em relação a entradas de produtos.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como registro uma divergência na entrada de produtos?
- O que fazer se a quantidade recebida for menor que a prevista?
- Quais opções estão disponíveis para resolver uma divergência na entrada?

---


---


---

## 4. Registro de Entrada e Consumo de Produtos no Estoque

**📋 METADADOS:**
- **ID:** sec_4
- **⏱️ Minutagem:** 07:35 → 10:10
- **⏲️ Duração:** 155s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/6vX7wYe8cIw?si=5Xf_VmLvM7bj6M73&t=455)
- **📦 Módulo:** Estoque
- **🏷️ Categorias:** Operacional, Cadastro, Administração
- **🔑 Palavras-chave:** entrada de estoque, consumo de produtos, devolução, registro inicial, transferência

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como registrar a entrada e o consumo de produtos no estoque, incluindo devoluções e registros iniciais, além de como gerenciar o consumo de itens utilizados em obras.

**Contexto:**
Estamos na interface do módulo de Estoque, onde o usuário pode gerenciar a entrada e saída de produtos. O objetivo desta seção é ensinar como registrar entradas de produtos no estoque e como registrar o consumo desses produtos durante o uso em obras.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Estoque > Registro de Entrada e Consumo
- Tela/interface específica: Tela de Registro de Entrada e Consumo

**Funcionalidade Detalhada:**

A funcionalidade de registro de entrada e consumo de produtos permite ao usuário adicionar produtos ao estoque e registrar a quantidade de produtos consumidos. Isso é essencial para manter um controle preciso do inventário e do uso de materiais em obras. O registro de entrada pode ser feito através de devoluções, registros iniciais ou outros tipos de entradas que não se encaixem em um fluxo definido.

### 🔹 Passo a Passo Detalhado:

1. **Registrar Entrada de Produtos**
   - Localização: Tela de Registro de Entrada e Consumo, seção de entrada.
   - Como fazer: Clique no botão **Mais Entrada** para iniciar o registro de uma nova entrada de produto.
   - Campos/Opções disponíveis:
     * `Tipo`: Selecione o tipo de entrada, que pode ser "Devolução ao Estoque", "Registros Iniciais" ou "Outros".
     * `Produto`: Selecione o produto que deseja adicionar ao estoque.
   - Resultado esperado: Após selecionar o tipo e o produto, clique em **Salvar**. O produto será adicionado ao estoque e estará disponível para uso.

2. **Registrar Consumo de Produtos**
   - Localização: Tela de Registro de Entrada e Consumo, seção de consumo.
   - Como fazer: Clique no botão **Mais Consumo** para registrar o consumo de produtos.
   - Observações importantes: É necessário vincular o local de consumo, que é a obra escolhida. Se a obra tiver um acompanhamento, você pode vincular ao serviço, mas isso é opcional.
   - Resultado esperado: Após selecionar a obra, uma lista de produtos disponíveis no estoque será exibida. Clique no ícone de **mais** ao lado do produto que deseja consumir.

3. **Inserir Quantidade de Uso**
   - Localização: Tela de registro de consumo, após adicionar o produto.
   - Como fazer: Insira a quantidade de uso no campo correspondente.
   - Observações importantes: O sistema mostrará a quantidade disponível. Por exemplo, se a quantidade disponível for 20, você pode registrar que consumiu 15. 
   - Resultado esperado: Após inserir a quantidade de uso, clique em **Salvar** e **Confirmar**. A quantidade será retirada do estoque e o consumo será registrado, mantendo um histórico.

4. **Transferências de Produtos**
   - Localização: Tela de Registro de Entrada e Consumo, seção de transferências.
   - Como fazer: Clique no botão **Mais Transferência** para iniciar uma nova transferência de produtos.
   - Observações importantes: Você pode iniciar a transferência a partir de uma solicitação de aprovação ou diretamente na tela de transferências.
   - Resultado esperado: Defina o local de origem e o local de destino para a transferência de produtos.

**Campos e Parâmetros:**

| Campo               | Tipo     | Obrigatório | Descrição                                           | Exemplo           |
|---------------------|----------|-------------|-----------------------------------------------------|-------------------|
| `Tipo`              | Dropdown | Sim         | Tipo de entrada, como devolução, registro inicial ou outros. | Devolução ao Estoque |
| `Produto`           | Dropdown | Sim         | Seleção do produto a ser adicionado ao estoque.    | Produto A         |
| `Quantidade de Uso` | Numérico | Sim         | Quantidade de produto consumido.                    | 15                |
| `Local de Origem`   | Dropdown | Sim         | Local de onde os produtos estão sendo transferidos. | Armazém 1         |
| `Local de Destino`  | Dropdown | Sim         | Local para onde os produtos estão sendo transferidos. | Obra 2            |

**Regras de Negócio:**
- O registro de entrada não interfere em outros módulos do sistema.
- O consumo de produtos deve ser registrado para manter o histórico de uso.
- A quantidade consumida deve ser menor ou igual à quantidade disponível no estoque.

**Observações Importantes:**
- Sempre verifique a quantidade disponível antes de registrar o consumo.
- Evite registrar consumos que excedam a quantidade disponível para evitar inconsistências no estoque.
- O registro de devolução deve ser feito com atenção para garantir que os produtos retornem corretamente ao estoque.

**Conceitos-Chave:**
- **Devolução ao Estoque**: Processo de registrar produtos que estão sendo retornados ao estoque.
- **Registro Inicial**: Adição de produtos ao estoque pela primeira vez.
- **Consumo**: Registro da quantidade de produtos utilizados em uma obra.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como registrar a entrada de produtos no estoque?
- O que é necessário para registrar o consumo de produtos?
- Como transferir produtos entre locais no sistema?

---


---


---

## 5. Processo de Transferência de Produtos

**📋 METADADOS:**
- **ID:** sec_5
- **⏱️ Minutagem:** 10:08 → 12:42
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/6vX7wYe8cIw?si=5Xf_VmLvM7bj6M73&t=608)
- **📦 Módulo:** Gestão de Estoque
- **🏷️ Categorias:** Transferência, Operacional, Estoque, Solicitação
- **🔑 Palavras-chave:** transferência, produtos, estoque, solicitação, romaneio, entrada, conferência

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de transferência de produtos entre estoques, incluindo a solicitação, confirmação e entrada dos itens na nova localização. O objetivo é garantir que a quantidade correta de produtos seja transferida e registrada adequadamente.

**Contexto:**
Estamos na interface de gestão de estoque, especificamente na funcionalidade de transferência de produtos. O objetivo desta seção é guiar o usuário através do processo de transferência, desde a solicitação até a entrada dos produtos na nova obra.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Gestão de Estoque > Submenu Transferência de Produtos
- Tela/interface específica: Tela de Transferência de Produtos

**Funcionalidade Detalhada:**
A funcionalidade de transferência de produtos permite que o usuário selecione um local de origem e visualize os produtos disponíveis nesse estoque. O usuário pode arrastar itens ou clicar na mãozinha para selecionar os produtos a serem transferidos. Após definir a quantidade desejada, o usuário deve salvar a solicitação, que será registrada como uma transferência pendente. O sistema permite que o usuário visualize e confirme a quantidade real a ser transferida, além de gerar um romaneio se necessário.

### 🔹 Passo a Passo Detalhado:

1. **Definir Local de Origem**
   - Localização: Tela de Transferência de Produtos
   - Como fazer: Selecione o local de origem no campo designado. Isso irá carregar uma lista de produtos disponíveis nesse estoque.
   - Campos/Opções disponíveis:
     * `Local de Origem`: Campo para selecionar o estoque de origem.
   - Resultado esperado: A lista de produtos disponíveis no estoque selecionado é exibida.

2. **Selecionar Produtos para Transferência**
   - Localização: Lista de produtos carregada após a seleção do local de origem.
   - Como fazer: Arraste os produtos desejados para o lado ou clique no ícone da mãozinha ao lado de cada produto.
   - Resultado esperado: Os produtos selecionados são marcados para transferência.

3. **Definir Quantidade a Ser Transferida**
   - Localização: Ao lado de cada produto selecionado.
   - Como fazer: Insira a quantidade desejada no campo correspondente.
   - Campos/Opções disponíveis:
     * `Quantidade Disponível`: Mostra a quantidade disponível do produto.
     * `Quantidade Prevista`: Mostra a quantidade que está prevista para transferência.
     * `Quantidade Real`: Campo para inserir a quantidade que realmente será transferida.
   - Resultado esperado: A quantidade real a ser transferida é registrada.

4. **Salvar Solicitação de Transferência**
   - Localização: Botão "Salvar" na parte inferior da tela.
   - Como fazer: Clique no botão "Salvar" para registrar a solicitação de transferência.
   - Resultado esperado: A transferência é registrada como pendente na tela.

5. **Visualizar Transferências Pendentes**
   - Localização: Tela de Transferências Pendentes.
   - Como fazer: Clique na transferência pendente para visualizar os itens aguardando confirmação.
   - Resultado esperado: Um agrupamento de todos os itens pendentes é exibido.

6. **Confirmar ou Cancelar Transferência**
   - Localização: Tela de Transferências Pendentes.
   - Como fazer: Para os itens que não serão transferidos, selecione a opção de cancelar. Para os demais, confirme a quantidade real a ser transferida.
   - Observações importantes: Certifique-se de que a quantidade real corresponde à quantidade prevista.
   - Resultado esperado: A transferência é confirmada ou cancelada conforme a escolha do usuário.

7. **Gerar Romaneio**
   - Localização: Opção de impressão na tela de confirmação da transferência.
   - Como fazer: Se desejar, marque a opção para imprimir um romaneio, que é um documento referente às informações do que está sendo transferido.
   - Resultado esperado: O romaneio é gerado para os itens transferidos.

8. **Realizar Entrada na Nova Obra**
   - Localização: Tela de Entrada de Produtos.
   - Como fazer: Na tela de entrada, confirme se a quantidade prevista é a que chegou na nova obra. Se sim, clique em "Salvar".
   - Resultado esperado: A entrada dos produtos é registrada e o fluxo de transferência é finalizado.

**Campos e Parâmetros:**

| Campo                  | Tipo     | Obrigatório | Descrição                                                         | Exemplo        |
|------------------------|----------|-------------|-------------------------------------------------------------------|----------------|
| `Local de Origem`      | Dropdown | Sim         | Seleciona o estoque de origem para a transferência.               | Estoque A      |
| `Quantidade Disponível` | Numérico | Não         | Mostra a quantidade disponível do produto selecionado.            | 100            |
| `Quantidade Prevista`  | Numérico | Não         | Mostra a quantidade que está prevista para transferência.         | 50             |
| `Quantidade Real`      | Numérico | Sim         | Insira a quantidade que realmente será transferida.              | 50             |

**Regras de Negócio:**
- A quantidade real a ser transferida deve ser menor ou igual à quantidade disponível.
- A transferência deve ser confirmada antes da entrada na nova obra.
- O romaneio é opcional, mas recomendado para documentação.

**Observações Importantes:**
- É importante verificar a quantidade disponível antes de realizar a transferência.
- Erros comuns incluem não confirmar a quantidade real ou esquecer de salvar a solicitação.
- A entrada deve ser realizada assim que os produtos chegarem na nova obra.

**Conceitos-Chave:**
- **Romaneio**: Documento que detalha as informações dos produtos transferidos.
- **Transferência Pendente**: Solicitação de transferência que ainda não foi confirmada.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso solicitar a transferência de produtos entre estoques?
- O que devo fazer se não quiser transferir todos os itens selecionados?
- Como confirmo a entrada dos produtos na nova obra após a transferência?

---


---


---

## 6. Vinculação de Produtos com Categorias e Especificações

**📋 METADADOS:**
- **ID:** sec_6
- **⏱️ Minutagem:** 12:40 → 15:13
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/6vX7wYe8cIw?si=5Xf_VmLvM7bj6M73&t=760)
- **📦 Módulo:** Cadastro de Produtos
- **🏷️ Categorias:** Configuração, Cadastro, Produtos, Especificações
- **🔑 Palavras-chave:** vinculação, categoria, subcategoria, especificação, produto, embalagem, componentes

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de vinculação de produtos a categorias e subcategorias, além de como definir especificações e embalagens. O objetivo é garantir que o sistema gerencie corretamente os produtos, diferenciando entre equipamentos e materiais.

**Contexto:**
Estamos na etapa de cadastro de produtos dentro do módulo de Cadastro de Produtos. O objetivo é estruturar as informações do produto, vinculando-o a categorias e definindo suas especificações.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Cadastro de Produtos > Vinculação de Produtos
- Tela/interface específica: Tela de Cadastro de Produtos

**Funcionalidade Detalhada:**
A funcionalidade permite ao usuário vincular um produto a uma categoria e subcategoria específicas, além de definir se o produto é um equipamento ou um material. Isso é crucial para o gerenciamento adequado dos produtos no sistema, uma vez que equipamentos e materiais são tratados de maneira diferente. O usuário também pode especificar detalhes sobre a embalagem e os componentes do produto.

### 🔹 Passo a Passo Detalhado:

1. **Vinculação de Categoria e Subcategoria**
   - Localização: Tela de Cadastro de Produtos, seção de Categorias
   - Como fazer: Selecione a categoria "Pinturas, Texturas e Tintas" e a subcategoria "Tintas" no menu suspenso.
   - Campos/Opções disponíveis:
     * `Categoria`: Opções incluem "Pinturas, Texturas e Tintas", "Ferramentas", "Materiais de Construção", etc.
     * `Subcategoria`: Opções incluem "Tintas", "Pincéis", "Rolos", etc.
   - Resultado esperado: O produto é vinculado à categoria e subcategoria selecionadas.

2. **Definição do Tipo de Produto**
   - Localização: Seção de Informações Gerais
   - Como fazer: Selecione se o produto é um "Equipamento" ou "Material" através de um botão de opção.
   - Observações importantes: Essa definição é crucial para o gerenciamento correto dos produtos no sistema.
   - Resultado esperado: O sistema reconhece o tipo de produto para gerenciá-lo adequadamente.

3. **Configuração de Embalagens**
   - Localização: Tela de Cadastro de Produtos, seção de Embalagens
   - Como fazer: Clique no botão **Próximo** para avançar para a seção de embalagens. Em seguida, adicione uma nova embalagem clicando em **Adicionar Embalagem**.
   - Campos/Opções disponíveis:
     * `Tipo de Embalagem`: Opções incluem "Caixa", "Lata", "Galão", etc.
     * `Quantidade`: Número de unidades ou litros na embalagem.
   - Resultado esperado: O produto é associado a uma embalagem específica, com a quantidade definida.

4. **Adição de Componentes**
   - Localização: Tela de Cadastro de Produtos, seção de Componentes
   - Como fazer: Clique em **Mais Componente** para adicionar itens relacionados ao produto.
   - Observações importantes: Os componentes podem incluir itens que fazem parte de um kit.
   - Resultado esperado: Os componentes são adicionados ao produto, permitindo uma gestão mais detalhada.

5. **Definição de Especificações**
   - Localização: Tela de Cadastro de Produtos, seção de Especificações
   - Como fazer: Clique em **Mais Específico** para adicionar detalhes sobre o produto.
   - Campos/Opções disponíveis:
     * `Tipo`: Opções incluem "Tinta", "Verniz", etc.
     * `Cor`: Selecione a cor do produto.
     * `Marca`: Nome da marca do produto.
     * `Parâmetro`: Defina parâmetros como resistência ou volume.
   - Resultado esperado: As especificações do produto são salvas, permitindo uma descrição detalhada.

6. **Revisão e Salvamento**
   - Localização: Tela de Cadastro de Produtos, seção de Revisão
   - Como fazer: Após preencher todos os campos, clique em **Pronto** para revisar as informações.
   - Resultado esperado: O usuário pode revisar todos os campos preenchidos e, se tudo estiver correto, clicar em **Salvar** para finalizar o cadastro.

**Campos e Parâmetros:**

| Campo                | Tipo         | Obrigatório | Descrição                                           | Exemplo      |
|----------------------|--------------|-------------|----------------------------------------------------|--------------|
| `Categoria`          | Dropdown     | Sim         | Categoria do produto, como "Pinturas"              | Pinturas     |
| `Subcategoria`       | Dropdown     | Sim         | Subcategoria do produto, como "Tintas"             | Tintas       |
| `Tipo de Produto`    | Radio Button | Sim         | Define se o produto é um "Equipamento" ou "Material"| Material     |
| `Tipo de Embalagem`  | Dropdown     | Sim         | Tipo de embalagem do produto                        | Caixa        |
| `Quantidade`         | Número       | Sim         | Quantidade de unidades ou litros na embalagem      | 20           |
| `Tipo`               | Dropdown     | Sim         | Tipo de especificação do produto                    | Tinta        |
| `Cor`                | Dropdown     | Sim         | Cor do produto                                     | Azul         |
| `Marca`              | Texto        | Sim         | Nome da marca do produto                            | Marca X      |
| `Parâmetro`         | Texto        | Não         | Parâmetro adicional, como resistência               | 20 L         |

**Regras de Negócio:**
- O produto deve ser vinculado a uma categoria e subcategoria antes de ser salvo.
- A definição do tipo de produto (Equipamento ou Material) é obrigatória para o gerenciamento correto.
- As especificações devem ser preenchidas para produtos que requerem detalhes adicionais.

**Observações Importantes:**
- É recomendável revisar todos os campos antes de clicar em **Salvar** para evitar erros.
- Erros comuns incluem não selecionar uma categoria ou subcategoria, o que pode impedir o salvamento do produto.
- Certifique-se de que todas as informações estão corretas, pois isso impacta na gestão do produto no sistema.

**Conceitos-Chave:**
- **Vinculação**: Processo de associar um produto a uma categoria e subcategoria específicas.
- **Especificação**: Detalhes adicionais sobre um produto, como tipo, cor e marca.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como vincular um produto a uma categoria e subcategoria?
- O que devo considerar ao definir se um produto é um equipamento ou material?
- Como adicionar especificações e componentes a um produto no sistema?

---


---


---

## 7. Gerenciamento de Equipamentos

**📋 METADADOS:**
- **ID:** sec_7
- **⏱️ Minutagem:** 15:11 → 17:46
- **⏲️ Duração:** 154s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/6vX7wYe8cIw?si=5Xf_VmLvM7bj6M73&t=911)
- **📦 Módulo:** Equipamentos
- **🏷️ Categorias:** Cadastro, Gerenciamento, Operacional
- **🔑 Palavras-chave:** equipamentos, ativo, desativado, aluguel, compra, manutenção, cadastro

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de gerenciamento de equipamentos no sistema, incluindo como cadastrar e visualizar equipamentos próprios e alugados, além de gerenciar seus status e manutenção.

**Contexto:**
Estamos na fase de gerenciamento de equipamentos dentro do sistema, onde é possível cadastrar e gerenciar tanto equipamentos próprios quanto alugados. O objetivo é facilitar o controle e a visualização do status dos equipamentos.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Equipamentos > Gerenciamento de Equipamentos
- Tela/interface específica: Tela de Listagem de Equipamentos

**Funcionalidade Detalhada:**
A funcionalidade de gerenciamento de equipamentos permite ao usuário visualizar e controlar o status dos equipamentos cadastrados, podendo desativá-los ou ativá-los conforme necessário. O sistema diferencia entre equipamentos próprios, que são cadastrados automaticamente após a compra, e equipamentos alugados, que requerem um cadastro manual através de uma ordem de serviço.

### 🔹 Passo a Passo Detalhado:

1. **Visualizar Status dos Produtos**
   - Localização: Tela de Listagem de Equipamentos
   - Como fazer: Na tela inicial, observe a coluna de status que indica se o produto está **ativo** ou **desativado**.
   - Resultado esperado: O usuário pode identificar rapidamente quais equipamentos estão ativos e quais estão desativados.

2. **Cadastrar Equipamento**
   - Localização: Botão **Mais Equipamento** na tela de gerenciamento
   - Como fazer: Clique no botão **Mais Equipamento** para iniciar o cadastro de um novo equipamento.
   - Campos/Opções disponíveis:
     * `Nome`: Campo de texto onde deve ser inserido o nome do equipamento, incluindo códigos e referências importantes.
     * `Tipo`: Seleção entre **Alugado** ou **Próprio**.
   - Resultado esperado: O sistema inicia o processo de cadastro do equipamento.

3. **Definir Informações do Equipamento**
   - Localização: Formulário de cadastro que aparece após clicar em **Mais Equipamento**
   - Como fazer: Preencha os campos obrigatórios, incluindo:
     * `Vínculo com o Produto Principal`: Seleção do produto relacionado.
     * `Data de Aquisição`: Campo de data para registrar quando o equipamento foi adquirido.
     * `Local Alocado`: Campo de texto para indicar a obra onde o equipamento será utilizado.
   - Resultado esperado: As informações do equipamento são salvas e o equipamento aparece na listagem.

4. **Adicionar Especificações do Equipamento**
   - Localização: Formulário de cadastro
   - Como fazer: Opcionalmente, preencha o campo de `Especificação` com detalhes como marcas, parâmetros e tipos.
   - Resultado esperado: Informações adicionais sobre o equipamento são registradas.

5. **Registrar Manutenção do Equipamento**
   - Localização: Formulário de cadastro
   - Como fazer: Indique se o equipamento requer um plano de manutenção e, se sim, defina a frequência e a última manutenção realizada.
   - Resultado esperado: O sistema registra as informações de manutenção, permitindo o acompanhamento futuro.

6. **Salvar Cadastro do Equipamento**
   - Localização: Botão **Salvar** no formulário de cadastro
   - Como fazer: Clique no botão **Salvar** para finalizar o cadastro do equipamento.
   - Resultado esperado: O equipamento aparece na tela inicial da listagem de equipamentos.

**Campos e Parâmetros:**

| Campo                       | Tipo         | Obrigatório | Descrição                                                                 | Exemplo                     |
|-----------------------------|--------------|-------------|---------------------------------------------------------------------------|-----------------------------|
| Nome                        | Texto        | Sim         | Nome do equipamento, incluindo códigos e referências.                    | "Escavadeira Modelo X"      |
| Tipo                        | Dropdown     | Sim         | Indica se o equipamento é **Alugado** ou **Próprio**.                   | "Próprio"                   |
| Vínculo com o Produto Principal | Dropdown | Sim         | Seleção do produto relacionado ao equipamento.                           | "Produto A"                 |
| Data de Aquisição           | Data         | Sim         | Data em que o equipamento foi adquirido.                                 | "01/01/2023"                |
| Local Alocado               | Texto        | Sim         | Local onde o equipamento será utilizado (ex: obra).                     | "Obra XYZ"                  |
| Especificação               | Texto        | Não         | Detalhes adicionais sobre o equipamento, como marcas e parâmetros.       | "Marca A, Tipo B"           |
| Ano de Fabricação           | Número       | Não         | Ano em que o equipamento foi fabricado.                                 | "2020"                      |
| Ano Modelo                  | Número       | Não         | Ano do modelo do equipamento.                                            | "2021"                      |
| Plano de Manutenção         | Checkbox     | Não         | Indica se o equipamento requer um plano de manutenção.                  | "Sim"                       |
| Frequência de Manutenção    | Texto        | Não         | Intervalo de tempo para as manutenções.                                 | "A cada 6 meses"            |
| Última Manutenção           | Data         | Não         | Data da última manutenção realizada.                                     | "01/06/2023"                |

**Regras de Negócio:**
- Um equipamento pode ser **ativado** ou **desativado** conforme a necessidade do usuário.
- Equipamentos próprios são cadastrados automaticamente após a compra, enquanto equipamentos alugados requerem um cadastro manual.
- A nota de serviço para equipamentos alugados não gera estoque.

**Observações Importantes:**
- É importante que o nome do equipamento seja claro e contenha todas as informações necessárias para sua identificação.
- Evite deixar campos obrigatórios em branco, pois isso pode impedir o cadastro do equipamento.
- Verifique se as informações de manutenção estão atualizadas para garantir a conformidade com o planejamento.

**Conceitos-Chave:**
- **Equipamento Próprio**: Equipamento que foi adquirido pela empresa e registrado no sistema.
- **Equipamento Alugado**: Equipamento que é alugado e gerenciado através de uma ordem de serviço.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso cadastrar um novo equipamento no sistema?
- O que devo fazer para desativar um equipamento?
- Quais informações são necessárias para registrar a manutenção de um equipamento?

---


---


---

## 8. Início de Transferência e Registro de Manutenções

**📋 METADADOS:**
- **ID:** sec_8
- **⏱️ Minutagem:** 17:46 → 20:21
- **⏲️ Duração:** 155s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/6vX7wYe8cIw?si=5Xf_VmLvM7bj6M73&t=1066)
- **📦 Módulo:** Transferências e Manutenções
- **🏷️ Categorias:** Operacional, Gestão de Equipamentos, Manutenção
- **🔑 Palavras-chave:** transferência, equipamento, manutenção, histórico, solicitação, andamento, conclusão

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de iniciar transferências de produtos e equipamentos, além de registrar manutenções. O objetivo é garantir que o usuário consiga acompanhar o histórico de alocações e manutenções de forma organizada e eficiente.

**Contexto:**
Estamos na tela de transferências do sistema, onde o usuário pode iniciar transferências de produtos e equipamentos, além de gerenciar manutenções. O foco é garantir que todas as etapas do processo sejam seguidas corretamente para manter um histórico preciso.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Transferências > Tela de Transferências
- Tela/interface específica: Tela de Transferências

**Funcionalidade Detalhada:**
A funcionalidade permite ao usuário iniciar transferências de produtos diretamente na tela de transferências. Para equipamentos, é necessário acessar o equipamento específico, clicar na opção "mais transferência" e definir o local de destino. O fluxo continua com a aprovação e geração da entrada, permitindo manter um histórico detalhado das alocações, incluindo as obras em que o equipamento esteve e o período de permanência.

### 🔹 Passo a Passo Detalhado:

1. **Iniciar Transferência de Produto**
   - Localização: Tela de Transferências
   - Como fazer: Na tela de transferências, localize a opção para iniciar a transferência de produtos.
   - Campos/Opções disponíveis:
     * `Produto`: Selecionar o produto a ser transferido.
   - Resultado esperado: A transferência do produto é iniciada e registrada no sistema.

2. **Iniciar Transferência de Equipamento**
   - Localização: Tela de Equipamentos
   - Como fazer: Acesse o equipamento desejado, clique na opção **mais transferência**.
   - Campos/Opções disponíveis:
     * `Local de Destino`: Definir o local para onde o equipamento será transferido.
   - Observações importantes: É necessário definir o local de destino antes de prosseguir.
   - Resultado esperado: O fluxo de transferência do equipamento é iniciado, permitindo a continuidade para aprovação e geração da entrada.

3. **Aprovar e Gerar Entrada**
   - Localização: Após definir o local de destino
   - Como fazer: Siga as instruções na tela para aprovar a transferência e gerar a entrada.
   - Resultado esperado: A transferência é aprovada e o registro é atualizado no sistema.

4. **Registrar Manutenções**
   - Localização: Tela de Manutenções
   - Como fazer: Clique na opção **registrar manutenções**.
   - Campos/Opções disponíveis:
     * `Motivo`: Campo para descrever o motivo da manutenção.
   - Resultado esperado: A manutenção é registrada com a data de solicitação.

5. **Solicitar Manutenção**
   - Localização: Tela de Manutenções
   - Como fazer: Clique em **solicitar manutenção** e insira o motivo, por exemplo, "motivo X".
   - Resultado esperado: A solicitação de manutenção é salva, registrando a data de solicitação.

6. **Atualizar Status da Manutenção**
   - Localização: Tela de Manutenções
   - Como fazer: Clique na opção **mais comentário** para atualizar o status da manutenção.
   - Observações importantes: Altere o status para "em andamento", identificando a data e adicionando um comentário.
   - Resultado esperado: O status da manutenção é atualizado para "em andamento", e o histórico é mantido.

7. **Finalizar Manutenção**
   - Localização: Tela de Manutenções
   - Como fazer: Utilize a opção **mais comentário** novamente para marcar a manutenção como finalizada.
   - Resultado esperado: O status da manutenção é atualizado para "finalizada", e o histórico é atualizado.

8. **Baixar Equipamento**
   - Localização: Tela de Equipamentos
   - Como fazer: Quando não for mais utilizar o equipamento, clique na opção **dar baixa**.
   - Campos/Opções disponíveis:
     * `Data`: Definir a data da baixa.
   - Resultado esperado: O equipamento é baixado do sistema.

9. **Acessar Página de Balanços**
   - Localização: Menu Principal > Módulo Balanços
   - Como fazer: Acesse a página de balanços.
   - Observações importantes: Não há botão de adicionar, pois os balanços são gerados automaticamente.
   - Resultado esperado: Visualização dos balanços gerados automaticamente.

**Campos e Parâmetros:**

| Campo               | Tipo      | Obrigatório | Descrição                                               | Exemplo          |
|---------------------|-----------|-------------|---------------------------------------------------------|------------------|
| `Produto`           | Dropdown  | Sim         | Selecionar o produto a ser transferido.                | Produto A        |
| `Local de Destino`  | Dropdown  | Sim         | Definir o local para onde o equipamento será transferido.| Local B          |
| `Motivo`            | Texto     | Sim         | Descrição do motivo da manutenção.                      | Motivo X         |
| `Data`              | Data      | Sim         | Data da baixa do equipamento.                           | 01/01/2023       |

**Regras de Negócio:**
- A transferência de produtos é iniciada diretamente na tela de transferências.
- Para equipamentos, é necessário acessar o equipamento e definir o local de destino.
- O registro de manutenções não influencia outros módulos, mas mantém um histórico.
- O status da manutenção deve passar por três etapas: início, andamento e conclusão.
- A baixa do equipamento requer a definição de uma data.

**Observações Importantes:**
- Ao solicitar manutenção, sempre insira um motivo claro.
- Utilize os comentários para atualizar o status da manutenção.
- Verifique se o equipamento está realmente fora de uso antes de dar baixa.

**Conceitos-Chave:**
- **Transferência**: Ato de mover um produto ou equipamento de um local para outro.
- **Manutenção**: Processo de solicitar e registrar a manutenção de um equipamento.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como iniciar a transferência de um produto ou equipamento?
- Quais são as etapas para registrar uma manutenção?
- Como atualizar o status de uma manutenção no sistema?

---


---


---

## 9. Balanço de Estoque

**📋 METADADOS:**
- **ID:** sec_9
- **⏱️ Minutagem:** 20:18 → 22:52
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/6vX7wYe8cIw?si=5Xf_VmLvM7bj6M73&t=1218)
- **📦 Módulo:** Gestão de Estoque
- **🏷️ Categorias:** Relatório, Operacional, Inventário
- **🔑 Palavras-chave:** balanço, estoque, validação, consumo, entrada, periodicidade

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como realizar um balanço de estoque, permitindo a validação das quantidades de produtos em relação ao que está registrado no sistema. O balanço serve como um inventário para garantir a precisão dos dados de estoque.

**Contexto:**
Estamos na funcionalidade de balanço de estoque dentro do módulo de Gestão de Estoque. O objetivo é permitir que os usuários realizem uma conferência das quantidades de produtos disponíveis em suas obras, comparando com os registros do sistema.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Gestão de Estoque > Balanço de Estoque
- Tela/interface específica: Tela de Balanço de Estoque

**Funcionalidade Detalhada:**
A funcionalidade de balanço de estoque permite que os usuários realizem uma conferência das quantidades de produtos disponíveis em suas obras. O balanço pode ser realizado em períodos de 7, 14, 21 ou 28 dias. Após a geração do balanço, é possível analisar a obra, o setor, e o status dos produtos. O objetivo principal é validar se as quantidades físicas na obra correspondem às registradas no sistema.

### 🔹 Passo a Passo Detalhado:

1. **Definir o Período do Balanço**
   - Localização: Tela de Balanço de Estoque
   - Como fazer: Selecione a periodicidade desejada para o balanço, que pode ser a cada 7, 14, 21 ou 28 dias.
   - Resultado esperado: O balanço é gerado com base na periodicidade selecionada.

2. **Analisar Produtos no Balanço**
   - Localização: Tela de Balanço de Estoque
   - Como fazer: Após a geração do balanço, visualize a lista de produtos, incluindo a `quantidade atual` e a `quantidade real`.
   - Resultado esperado: Uma lista detalhada dos produtos com suas respectivas quantidades.

3. **Conferir Quantidades**
   - Localização: Tela de Balanço de Estoque
   - Como fazer: Compare a `quantidade atual` (registrada no sistema) com a `quantidade real` (física na obra). Insira as diferenças:
     * Se a quantidade for inferior, registre como **consumo**.
     * Se a quantidade for superior, registre como **entrada**.
   - Resultado esperado: As diferenças são registradas e atualizadas no sistema.

4. **Salvar as Informações**
   - Localização: Botão **Salvar** na Tela de Balanço de Estoque
   - Como fazer: Após inserir as diferenças, clique no botão **Salvar** para registrar as alterações. Se necessário, clique novamente em **Salvar** para confirmar.
   - Resultado esperado: As informações do balanço são salvas, e os produtos pendentes são listados.

5. **Visualizar Balanços Finalizados**
   - Localização: Tela de Balanço de Estoque
   - Como fazer: Acesse a seção de balanços finalizados para visualizar os balanços que já foram concluídos.
   - Resultado esperado: Uma lista de balanços finalizados é exibida.

6. **Configurar Locais de Estoque**
   - Localização: Tela de Locais de Estoque
   - Como fazer: Acesse a tela de locais de estoque para visualizar as obras e a matriz pré-cadastrada. Você pode editar as informações de cada local.
   - Resultado esperado: A possibilidade de editar a periodicidade do balanço e o tempo de alerta para a realização do balanço.

7. **Definir Prazo de Limite de Entrega**
   - Localização: Tela de Edição de Local de Estoque
   - Como fazer: Durante a edição, defina o prazo de limite de entrega conforme discutido na solicitação.
   - Resultado esperado: O prazo de limite de entrega é configurado para o local de estoque selecionado.

**Campos e Parâmetros:**

| Campo                     | Tipo       | Obrigatório | Descrição                                               | Exemplo         |
|---------------------------|------------|-------------|---------------------------------------------------------|------------------|
| `Periodicidade`           | Dropdown   | Sim         | Define a frequência do balanço (7, 14, 21 ou 28 dias)  | 14 dias          |
| `Quantidade Atual`        | Numérico   | Sim         | Quantidade de produtos registrada no sistema            | 60               |
| `Quantidade Real`         | Numérico   | Sim         | Quantidade de produtos disponível na obra               | 52               |
| `Diferença`               | Numérico   | Não         | Diferença entre a quantidade atual e a real            | -8 (consumo)     |
| `Salvar`                  | Botão      | Sim         | Botão para salvar as informações inseridas              | [Salvar]         |

**Regras de Negócio:**
- O balanço deve ser realizado em períodos de 7, 14, 21 ou 28 dias.
- As diferenças nas quantidades devem ser registradas como consumo ou entrada, dependendo se a quantidade real é inferior ou superior à quantidade atual.
- Produtos não conferidos permanecem como pendentes até que sejam validados.

**Observações Importantes:**
- É possível imprimir o balanço e enviar o relatório para validação antes de preencher no sistema.
- Erros comuns incluem não registrar as diferenças corretamente, o que pode levar a inconsistências no estoque.
- Certifique-se de que todos os produtos foram conferidos antes de salvar as informações.

**Conceitos-Chave:**
- **Balanço de Estoque**: Processo de conferência das quantidades de produtos disponíveis em relação ao que está registrado no sistema.
- **Consumo**: Registro de uma quantidade inferior à registrada no sistema, indicando que o produto foi utilizado.
- **Entrada**: Registro de uma quantidade superior à registrada no sistema, indicando que o produto foi adicionado ao estoque.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso realizar um balanço de estoque no sistema?
- O que devo fazer se a quantidade real de um produto for diferente da quantidade registrada?
- Como posso visualizar os balanços que já foram finalizados?

---


---


---

## 10. Transferência e Controle de Estoque

**📋 METADADOS:**
- **ID:** sec_10
- **⏱️ Minutagem:** 22:49 → 25:24
- **⏲️ Duração:** 154s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/6vX7wYe8cIw?si=5Xf_VmLvM7bj6M73&t=1369)
- **📦 Módulo:** Suprimentos
- **🏷️ Categorias:** Configuração, Controle de Estoque, Relatório, Administração
- **🔑 Palavras-chave:** transferência, relacionamento, histórico de movimentação, setores, estoque mínimo, solicitação

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como realizar transferências entre obras, configurar setores e gerenciar o controle de estoque, incluindo a definição de limites mínimos e máximos de produtos, além de gerar relatórios de movimentação.

**Contexto:**
Estamos na interface do módulo de suprimentos, onde o usuário pode gerenciar a transferência de produtos entre obras, configurar setores de organização e controlar o estoque de forma eficiente.

**Localização no Sistema:**
- Caminho de navegação: Menu Principal > Módulo Suprimentos > Controle de Estoque
- Tela/interface específica: Tela de Controle de Estoque

**Funcionalidade Detalhada:**

A funcionalidade de transferência entre obras permite que o usuário crie um relacionamento entre diferentes obras, facilitando a gestão de recursos. O usuário pode selecionar uma obra específica e adicionar um relacionamento, além de acessar relatórios e um histórico de movimentação que registra todas as alterações no estoque, como transferências, balanços, entradas e saídas. Também é possível criar setores para organizar os produtos dentro da obra, como hidráulica, elétrica e materiais diversos, melhorando a consulta e visualização do estoque.

### 🔹 Passo a Passo Detalhado:

1. **Selecionar Obra e Adicionar Relacionamento**
   - Localização: Tela de Controle de Estoque
   - Como fazer: Clique na obra desejada e, em seguida, clique no botão **Adicionar Relacionamento**.
   - Resultado esperado: Um novo relacionamento entre as obras será criado.

2. **Gerar Relatório**
   - Localização: Tela de Controle de Estoque
   - Como fazer: Clique na opção **Relatório** disponível na interface.
   - Resultado esperado: Um relatório detalhado sobre as movimentações de estoque será exibido.

3. **Visualizar Histórico de Movimentação**
   - Localização: Tela de Controle de Estoque
   - Como fazer: Role para baixo até a seção **Histórico de Movimentação**.
   - Resultado esperado: Uma lista de todas as alterações feitas no estoque, incluindo data, hora e tipo de movimentação (transferência, balanço, entradas, saídas).

4. **Criar Setores**
   - Localização: Tela de Controle de Estoque
   - Como fazer: Clique no botão **Mais Setor**.
   - Campos/Opções disponíveis:
     * `Nome do Setor`: Campo para inserir o nome do setor (ex: hidráulica, elétrica, materiais diversos).
   - Resultado esperado: O setor será criado e aparecerá na lista de setores.

5. **Configurar Controle de Estoque**
   - Localização: Tela de Controle de Estoque
   - Como fazer: Clique no botão **Mais Produto** para adicionar um novo item ao estoque.
   - Campos/Opções disponíveis:
     * `Item`: Selecione o produto desejado.
     * `Quantidade Mínima`: Insira a quantidade mínima permitida.
     * `Quantidade Máxima`: Insira a quantidade máxima permitida (opcional).
   - Resultado esperado: O produto será adicionado ao controle de estoque com as quantidades mínimas e máximas definidas.

6. **Gerar Solicitação Automática**
   - Localização: Tela de Controle de Estoque
   - Como fazer: Após definir a quantidade mínima, o sistema automaticamente gerará uma solicitação quando a quantidade do produto ficar abaixo do limite estabelecido.
   - Resultado esperado: Uma solicitação de reabastecimento será criada automaticamente pelo sistema.

**Campos e Parâmetros:**

| Campo                  | Tipo       | Obrigatório | Descrição                                               | Exemplo                |
|------------------------|------------|-------------|---------------------------------------------------------|------------------------|
| `Nome do Setor`       | Texto      | Sim         | Nome do setor a ser criado para organização do estoque. | Hidráulica             |
| `Item`                | Dropdown   | Sim         | Seleção do produto a ser adicionado ao estoque.        | Tubos de PVC           |
| `Quantidade Mínima`   | Numérico   | Sim         | Quantidade mínima permitida para o produto.            | 10                     |
| `Quantidade Máxima`   | Numérico   | Não         | Quantidade máxima informativa para o produto.          | 50                     |

**Regras de Negócio:**
- O sistema gera uma solicitação automática quando a quantidade de um produto fica abaixo da `Quantidade Mínima` definida.
- Os setores devem ser criados para facilitar a organização e consulta dos produtos no estoque.
- O histórico de movimentação deve registrar todas as alterações feitas no estoque, incluindo transferências e balanços.

**Observações Importantes:**
- Ao criar setores, é importante nomeá-los de forma clara para facilitar a identificação.
- Verifique sempre as quantidades mínimas e máximas para evitar faltas ou excessos no estoque.
- O sistema pode gerar solicitações automaticamente, portanto, mantenha as configurações de estoque sempre atualizadas.

**Conceitos-Chave:**
- **Setor**: Divisão organizacional dentro do estoque que agrupa produtos semelhantes.
- **Histórico de Movimentação**: Registro de todas as alterações realizadas no estoque, incluindo transferências e entradas/saídas de produtos.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso transferir produtos entre obras?
- O que é o histórico de movimentação e como posso acessá-lo?
- Como configurar o estoque mínimo e máximo para um produto?

---


---


---

## 11. Cadastro de Unidade de Medida e Embalagens

**📋 METADADOS:**
- **ID:** sec_11
- **⏱️ Minutagem:** 25:21 → 26:02
- **⏲️ Duração:** 41s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/6vX7wYe8cIw?si=5Xf_VmLvM7bj6M73&t=1521)
- **📦 Módulo:** Suprimentos
- **🏷️ Categorias:** Configuração, Cadastro, Operacional
- **🔑 Palavras-chave:** unidade de medida, embalagem, cadastro, produto, sistema

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como cadastrar unidades de medida e embalagens no sistema, permitindo que os usuários vinculem essas informações ao cadastro de produtos, facilitando a gestão de suprimentos.

**Contexto:**
Estamos no módulo de suprimentos do sistema, onde o objetivo é cadastrar unidades de medida e embalagens que serão utilizadas nos produtos. Essa funcionalidade é essencial para garantir que os produtos sejam gerenciados corretamente em termos de quantidades e formatos de embalagem.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Suprimentos > Cadastro de Unidades e Embalagens
- Tela/interface específica: Tela de Cadastro de Unidades e Embalagens

**Funcionalidade Detalhada:**
A funcionalidade permite que os usuários cadastrem novas unidades de medida e embalagens. As unidades de medida são utilizadas para definir como os produtos serão quantificados, enquanto as embalagens são as formas físicas em que os produtos são armazenados e transportados. Esta funcionalidade é utilizada sempre que um novo produto é cadastrado ou quando há necessidade de atualizar as informações de unidades e embalagens existentes.

### 🔹 Passo a Passo Detalhado:

1. **Cadastrar Unidade de Medida**
   - Localização: Tela de Cadastro de Unidades e Embalagens
   - Como fazer: Clique no botão **Mais Unidade** para iniciar o cadastro de uma nova unidade de medida.
   - Campos/Opções disponíveis:
     * `Nome`: Campo onde você deve inserir o nome da unidade de medida (ex: "met²").
     * `Símbolo`: Campo onde você deve inserir o símbolo correspondente à unidade de medida (ex: "M2").
   - Resultado esperado: Após preencher os campos e salvar, a nova unidade de medida será cadastrada e estará disponível para uso em outros campos do sistema.

2. **Cadastrar Embalagem**
   - Localização: Tela de Cadastro de Unidades e Embalagens
   - Como fazer: Clique no botão **Mais Embalagem** para iniciar o cadastro de uma nova embalagem.
   - Campos/Opções disponíveis:
     * `Nome`: Campo onde você deve inserir o nome da embalagem (ex: "Caixa").
     * `Símbolo`: Campo onde você deve inserir o símbolo correspondente à embalagem (ex: "CX").
   - Observações importantes: Certifique-se de que a embalagem esteja cadastrada antes de vinculá-la ao produto.
   - Resultado esperado: Após preencher os campos e salvar, a nova embalagem será cadastrada e estará disponível para vinculação no cadastro do produto.

**Campos e Parâmetros:**

| Campo     | Tipo   | Obrigatório | Descrição                                   | Exemplo   |
|-----------|--------|-------------|---------------------------------------------|-----------|
| Nome      | Texto  | Sim         | Nome da unidade de medida ou embalagem      | met²      |
| Símbolo   | Texto  | Sim         | Símbolo correspondente à unidade ou embalagem| M2        |

**Regras de Negócio:**
- A unidade de medida deve ser única e não pode ser duplicada.
- A embalagem deve ser cadastrada antes de ser vinculada a um produto.
- Os campos `Nome` e `Símbolo` são obrigatórios para o cadastro de unidades e embalagens.

**Observações Importantes:**
- Sempre verifique se a unidade de medida ou embalagem já existe no sistema para evitar duplicações.
- Erros comuns incluem não preencher os campos obrigatórios, o que impedirá o salvamento das informações.
- As unidades de medida e embalagens cadastradas são essenciais para a correta gestão de produtos no sistema.

**Conceitos-Chave:**
- **Unidade de Medida**: Representa a forma como a quantidade de um produto é medida (ex: metros quadrados).
- **Embalagem**: Refere-se ao formato físico em que um produto é armazenado ou transportado (ex: caixa).

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como cadastrar uma nova unidade de medida no sistema?
- Quais informações são necessárias para cadastrar uma embalagem?
- O que fazer se a unidade de medida ou embalagem já estiver cadastrada?

---


---

