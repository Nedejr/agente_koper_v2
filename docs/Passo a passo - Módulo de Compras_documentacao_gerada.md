# 📚 Documentação: Passo a passo - Módulo de Compras

**🎥 Vídeo Original:** https://youtu.be/qFzqzIoiVE4?si=YoVxiJOkipNVbQWb

**📊 Total de Seções:** 14

---

---

## 1. Fluxo de Compras no Módulo de Compras

**📋 METADADOS:**
- **ID:** sec_1
- **⏱️ Minutagem:** 00:00 → 02:33
- **⏲️ Duração:** 152s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/qFzqzIoiVE4?si=YoVxiJOkipNVbQWb&t=0)
- **📦 Módulo:** Compras
- **🏷️ Categorias:** Operacional, Solicitação, Compras
- **🔑 Palavras-chave:** fluxo de compras, solicitação, suprimentos, cotação, ordem de compra

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o fluxo de compras no sistema, desde a solicitação até a chegada do produto no estoque. Ela orienta o usuário sobre as diferentes formas de iniciar o processo de compras e como realizar uma solicitação de suprimentos.

**Contexto:**
Estamos no módulo de compras do sistema, onde o objetivo é entender e executar o fluxo de compras, que abrange desde a solicitação de produtos até a sua chegada no estoque.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Compras > Suprimentos > Solicitações
- Tela/interface específica: Aba de Solicitações

**Funcionalidade Detalhada:**

O fluxo de compras permite que os usuários solicitem produtos de forma organizada e eficiente. Existem três maneiras principais de iniciar esse fluxo:

1. **Solicitação em Suprimentos**: Ideal para situações onde mais de um usuário está envolvido, como quando um colaborador em uma obra faz uma solicitação que será processada pelo departamento de compras.
2. **Compras Direto em Orçamentos**: Utilizado quando um único usuário está realizando todo o fluxo, permitindo que ele inicie diretamente a cotação com fornecedores sem a necessidade de uma solicitação prévia.
3. **Início Direto na Ordem de Compra**: Comum para compras retroativas ou para formalizar compras feitas de última hora.

### 🔹 Passo a Passo Detalhado:

1. **Acessar a Aba de Solicitações**
   - Localização: Menu Principal > Módulo Compras > Suprimentos > Aba de Solicitações
   - Como fazer: Clique na aba "Solicitações" para acessar a interface de solicitações de produtos.
   - Resultado esperado: A tela de solicitações é exibida, permitindo que o usuário inicie uma nova solicitação.

2. **Criar uma Nova Solicitação**
   - Localização: Dentro da aba de solicitações, clique no botão **"Mais Solicitação"**.
   - Como fazer: Clique no botão **"Mais Solicitação"** para abrir o formulário de nova solicitação.
   - Campos/Opções disponíveis:
     * `Produto`: Selecione um produto da lista de produtos cadastrados.
   - Resultado esperado: Um formulário para adicionar novos produtos à solicitação é exibido.

3. **Selecionar um Produto**
   - Localização: Tela de especificações da nova solicitação.
   - Como fazer: Utilize o filtro por categoria, subcategoria ou pesquisa direta para localizar o produto desejado. Você pode arrastar para o lado ou clicar na mãozinha para selecionar o item.
   - Observações importantes: Se o produto não estiver cadastrado, clique em **"Mais Produto"** para adicionar um novo item.
   - Resultado esperado: O produto selecionado é adicionado à solicitação.

4. **Definir Especificações do Produto**
   - Localização: Tela de especificações do produto.
   - Como fazer: Após selecionar o produto, defina o tipo do produto. Por exemplo, selecione "cimento Portland CP1 de 50 kg".
   - Campos/Opções disponíveis:
     * `Tipo de Produto`: Selecione o tipo específico do produto desejado.
     * `Quantidade`: Insira a quantidade desejada do produto.
   - Resultado esperado: O tipo e a quantidade do produto são definidos e prontos para serem adicionados à solicitação.

5. **Adicionar o Produto à Solicitação**
   - Localização: Na tela de especificações, após definir o tipo e a quantidade.
   - Como fazer: Clique no botão **"Adicionar"** para incluir o produto na solicitação.
   - Resultado esperado: O produto é adicionado à lista de produtos da solicitação, permitindo que o usuário selecione vários produtos conforme necessário.

**Campos e Parâmetros:**

| Campo                | Tipo         | Obrigatório | Descrição                                                   | Exemplo                     |
|----------------------|--------------|-------------|------------------------------------------------------------|-----------------------------|
| Produto              | Dropdown     | Sim         | Lista de produtos cadastrados no sistema.                  | Cimento Portland CP1 de 50 kg |
| Tipo de Produto      | Dropdown     | Sim         | Especificação do tipo do produto selecionado.              | Cimento Portland CP1        |
| Quantidade           | Numérico     | Sim         | Quantidade do produto a ser solicitado.                    | 10                          |

**Regras de Negócio:**
- A solicitação deve ser iniciada a partir da aba de solicitações no módulo de suprimentos.
- É possível adicionar múltiplos produtos à solicitação antes de finalizá-la.
- Se um produto não estiver cadastrado, o usuário deve adicionar um novo produto antes de prosseguir.

**Observações Importantes:**
- Utilize filtros para facilitar a busca de produtos na lista.
- Verifique se o tipo de produto selecionado é o correto antes de adicionar à solicitação.
- Evite adicionar produtos desnecessários para manter a solicitação organizada.

**Conceitos-Chave:**
- **Fluxo de Compras**: Processo que abrange desde a solicitação de produtos até a sua chegada no estoque.
- **Solicitação em Suprimentos**: Método de iniciar o fluxo de compras que envolve múltiplos usuários.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como iniciar o fluxo de compras no sistema?
- Quais são as diferentes formas de solicitar produtos?
- O que fazer se o produto desejado não estiver cadastrado no sistema?

---


---


---

## 2. Especificação de Serviços e Vínculo com Obras

**📋 METADADOS:**
- **ID:** sec_2
- **⏱️ Minutagem:** 02:30 → 05:04
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/qFzqzIoiVE4?si=YoVxiJOkipNVbQWb&t=150)
- **📦 Módulo:** Compras
- **🏷️ Categorias:** Configuração, Operacional, Cadastro
- **🔑 Palavras-chave:** especificar serviços, obra, fluxo de compras, data limite de entrega, comentários

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de especificação de serviços vinculados a obras no sistema, abordando a configuração de recursos alocados, a definição de datas limite de entrega e a adição de comentários para aprovação, garantindo um fluxo de compras eficiente.

**Contexto:**
Estamos na interface do módulo de Compras, onde o usuário pode especificar serviços relacionados a produtos que serão utilizados em obras. O objetivo é garantir que os serviços estejam corretamente vinculados e que as informações necessárias para a aprovação e execução das compras sejam fornecidas.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Compras > Especificação de Serviços
- Tela/interface específica: Tela de Especificação de Serviços

**Funcionalidade Detalhada:**
A funcionalidade de especificação de serviços permite ao usuário vincular produtos a serviços específicos dentro de uma obra. Isso é crucial para o gerenciamento de contas a pagar e fluxo de caixa, especialmente em obras onde o acompanhamento de engenharia está completo. O sistema diferencia entre serviços com recursos alocados e aqueles sem, permitindo uma gestão mais eficiente dos insumos necessários.

### 🔹 Passo a Passo Detalhado:

1. **Arrastar e Definir Especificações**
   - Localização: Lateral da tela de especificação de serviços
   - Como fazer: O usuário deve arrastar o item desejado para o lado e definir as especificações necessárias.
   - Resultado esperado: As especificações do serviço são definidas e o sistema atualiza as informações correspondentes.

2. **Selecionar Local de Consumo**
   - Localização: Lateral da tela
   - Como fazer: O usuário deve identificar o local de consumo da obra. Se a obra ainda não tiver o acompanhamento de engenharia completo, o vínculo será apenas com a obra, sem comparativos.
   - Resultado esperado: O sistema registra o vínculo com a obra, permitindo o gerenciamento de contas a pagar e fluxo de caixa.

3. **Especificar Serviços**
   - Localização: Botão "Especificar Serviços"
   - Como fazer: Clicar no botão "Especificar Serviços" para abrir a interface de seleção.
   - Observações importantes: O sistema separa serviços com recursos alocados e serviços sem recursos alocados.
   - Resultado esperado: O usuário pode visualizar e selecionar serviços disponíveis.

4. **Visualizar Comparativo de Quantidades**
   - Localização: Interface de especificação de serviços
   - Como fazer: O sistema já demonstra um comparativo entre a quantidade planejada e a quantidade já solicitada até o momento.
   - Resultado esperado: O usuário pode verificar a disponibilidade dos insumos necessários para os serviços.

5. **Definir Data Limite de Entrega**
   - Localização: Campo "Data Limite de Entrega"
   - Como fazer: O campo é preenchido automaticamente com uma data pré-configurada. O usuário pode alterar essa data conforme necessário.
   - Observações importantes: Se a data limite de entrega for inferior à data solicitada, a solicitação será marcada como urgente.
   - Resultado esperado: O sistema atualiza o status da solicitação conforme a data limite definida.

6. **Exibir Data Limite ao Fornecedor**
   - Localização: Campo de seleção para exibir a data limite
   - Como fazer: O usuário deve selecionar se deseja ou não exibir a data limite ao fornecedor.
   - Resultado esperado: A configuração é salva e aplicada na comunicação com o fornecedor.

7. **Adicionar Comentários**
   - Localização: Campo de comentários
   - Como fazer: Clicar no campo de comentários e digitar a mensagem que será enviada para a aprovação da solicitação.
   - Observações importantes: O comentário também pode ser exibido para o fornecedor no momento do orçamento, se a opção for selecionada.
   - Resultado esperado: O comentário é salvo e associado à solicitação.

8. **Salvar Especificações**
   - Localização: Botão "Salvar"
   - Como fazer: Clicar no botão "Salvar" para registrar todas as especificações feitas.
   - Resultado esperado: As informações são salvas no sistema e a solicitação é registrada.

**Campos e Parâmetros:**

| Campo                       | Tipo       | Obrigatório | Descrição                                                                 | Exemplo                |
|-----------------------------|------------|-------------|---------------------------------------------------------------------------|------------------------|
| `Local de Consumo`          | Dropdown   | Sim         | Seleção do local onde o produto será consumido.                          | Obra A                 |
| `Especificar Serviços`      | Botão      | Sim         | Ação para abrir a interface de seleção de serviços.                      | -                      |
| `Data Limite de Entrega`    | Data       | Sim         | Data limite para a entrega do produto, preenchida automaticamente.       | 2023-10-30             |
| `Exibir Data ao Fornecedor` | Checkbox   | Não         | Opção para exibir a data limite ao fornecedor.                           | [ ] Exibir             |
| `Comentários`               | Texto      | Não         | Campo para adicionar comentários sobre a solicitação.                    | "Urgente, por favor."  |

**Regras de Negócio:**
- Se a obra não tiver o acompanhamento de engenharia completo, o vínculo será apenas com a obra, sem comparativos.
- Para obras com engenharia completa, o sistema solicitará a especificação do serviço.
- A data limite de entrega é preenchida automaticamente, podendo ser alterada pelo usuário.
- Solicitações com data inferior ao limite serão marcadas como urgentes.
- Comentários podem ser exibidos para o fornecedor, dependendo da seleção do usuário.

**Observações Importantes:**
- É importante verificar a configuração da data limite de entrega para evitar solicitações urgentes desnecessárias.
- Comentários devem ser claros e objetivos para facilitar a aprovação.

**Conceitos-Chave:**
- **Vínculo com Obra**: Relação entre o produto e a obra, que permite o gerenciamento financeiro.
- **Data Limite de Entrega**: Data que determina a urgência da solicitação e o prazo para entrega do produto.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como especificar serviços vinculados a uma obra?
- O que acontece se a data limite de entrega for inferior à data solicitada?
- Como adicionar comentários para a aprovação da solicitação?

---


---


---

## 3. Salvamento e Aprovação de Solicitações

**📋 METADADOS:**
- **ID:** sec_3
- **⏱️ Minutagem:** 05:01 → 07:34
- **⏲️ Duração:** 152s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/qFzqzIoiVE4?si=YoVxiJOkipNVbQWb&t=301)
- **📦 Módulo:** Compras
- **🏷️ Categorias:** Operacional, Aprovação, Solicitações
- **🔑 Palavras-chave:** salvar, rascunho, editar, excluir, aprovação, histórico, comentários, transferência

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de salvamento de solicitações no sistema, incluindo a opção de salvar como rascunho e as etapas de aprovação no módulo de compras. O objetivo é garantir que os usuários compreendam como gerenciar suas solicitações e acompanhar seu status.

**Contexto:**
Estamos na interface do módulo de compras, onde o usuário pode salvar solicitações de compra e gerenciar seu status. O foco é entender como salvar uma solicitação, as opções disponíveis e como acompanhar o fluxo de aprovação.

**Localização no Sistema:**
- Caminho de navegação: Menu Principal > Módulo Compras > Solicitações
- Tela/interface específica: Tela de Solicitações

**Funcionalidade Detalhada:**
A funcionalidade permite que o usuário salve suas solicitações de compra de duas maneiras: como rascunho ou como uma solicitação completa. Salvar como rascunho permite que o usuário feche a tela e retorne posteriormente para completar a solicitação. Uma vez que a solicitação é salva completamente, ela é enviada para o módulo de compras para aprovação. Importante notar que apenas solicitações com status "aberto" podem ser editadas ou excluídas pelo solicitante; após isso, apenas o departamento de compras pode realizar alterações.

### 🔹 Passo a Passo Detalhado:

1. **Salvar Solicitação**
   - Localização: Botão **Salvar** na parte inferior da tela de solicitações.
   - Como fazer: Clique no botão **Salvar**. Uma janela de opções aparecerá.
   - Campos/Opções disponíveis:
     * `Salvar como Rascunho`: Permite que a solicitação seja salva sem ser enviada para aprovação, possibilitando edições futuras.
     * `Salvar Completo`: Envia a solicitação para o módulo de compras.
   - Resultado esperado: A solicitação é salva conforme a opção escolhida. Se salva como rascunho, o usuário pode fechar a tela e retornar mais tarde.

2. **Acompanhar Solicitação**
   - Localização: Tela inicial do módulo de compras.
   - Como fazer: Acesse a tela inicial para visualizar todas as solicitações pendentes para aprovação.
   - Observações importantes: O status da solicitação deve ser "aberto" para que o solicitante possa editar ou excluir.
   - Resultado esperado: O usuário vê um histórico das ações realizadas no fluxo de compras, incluindo a solicitação que acabou de realizar.

3. **Aprovar Solicitações**
   - Localização: Tela de Aprovação de Solicitações no módulo de compras.
   - Como fazer: Clique na solicitação pendente que deseja aprovar.
   - Observações importantes: O campo de urgência é destacado, e um ícone de comentário em verde indica que há um comentário disponível.
   - Resultado esperado: O responsável pela aprovação pode visualizar detalhes da solicitação e tomar ações.

4. **Opções de Aprovação**
   - Localização: Tela de Aprovação de Solicitações.
   - Como fazer: Clique no ícone de polegar para aprovar ou reprovar a solicitação.
   - Observações importantes: A aprovação pode ser feita de forma individual (item a item) ou rápida (todos de uma vez).
   - Resultado esperado: A solicitação é aprovada ou reprovada conforme a ação escolhida.

5. **Transferência de Produtos**
   - Localização: Opção de transferência na tela de aprovação.
   - Como fazer: Após clicar no polegar para aprovar, selecione a opção de transferência.
   - Observações importantes: O usuário pode escolher entre comprar, transferir ou realizar ambas as ações.
   - Resultado esperado: O sistema puxa todas as obras relacionadas ao produto e permite que o usuário defina a quantidade a ser transferida.

**Campos e Parâmetros:**

| Campo                | Tipo      | Obrigatório | Descrição                                               | Exemplo               |
|----------------------|-----------|-------------|--------------------------------------------------------|-----------------------|
| Salvar como Rascunho| Botão     | Não         | Opção para salvar a solicitação sem enviá-la para aprovação. | [Botão Salvar]        |
| Salvar Completo      | Botão     | Não         | Opção para enviar a solicitação para o módulo de compras. | [Botão Salvar]        |
| Status               | Texto     | Sim         | Indica o status da solicitação (aberto, aprovado, etc.). | Aberto                |
| Comentário           | Texto     | Não         | Campo para inserir ou visualizar comentários sobre a solicitação. | "Urgente"             |
| Urgente              | Checkbox  | Não         | Indica se a solicitação é urgente.                     | [ ] Urgente           |

**Regras de Negócio:**
- Solicitações podem ser editadas ou excluídas apenas se estiverem com status "aberto".
- Após a aprovação, o fluxo da solicitação é interrompido se for reprovada.
- O responsável pela aprovação pode realizar alterações, como trocar produtos, se necessário.

**Observações Importantes:**
- É recomendado salvar como rascunho se houver incertezas sobre a solicitação.
- Evite deixar solicitações pendentes por muito tempo para não atrasar o processo de compras.
- Verifique sempre o status da solicitação antes de tentar editá-la.

**Conceitos-Chave:**
- **Rascunho**: Estado em que a solicitação é salva, mas não enviada para aprovação.
- **Aprovação Rápida**: Método que permite aprovar várias solicitações de uma vez, sem a necessidade de aprovar item a item.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso salvar uma solicitação no sistema?
- O que acontece se eu salvar uma solicitação como rascunho?
- Quais são as opções disponíveis para aprovar uma solicitação no módulo de compras?

---


---


---

## 4. Aprovação e Finalização de Produtos

**📋 METADADOS:**
- **ID:** sec_4
- **⏱️ Minutagem:** 07:31 → 10:04
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/qFzqzIoiVE4?si=YoVxiJOkipNVbQWb&t=451)
- **📦 Módulo:** Aprovação de Produtos
- **🏷️ Categorias:** Aprovação, Orçamento, Fornecedores
- **🔑 Palavras-chave:** aprovação, produtos, orçamento, fornecedores, cotação, e-mail

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de aprovação de produtos, incluindo a definição do local de entrega e a finalização do processo, seja para gerar um orçamento ou uma compra. O objetivo é otimizar a gestão de cotações com fornecedores.

**Contexto:**
Estamos na etapa de aprovação de produtos dentro do módulo de Aprovação de Produtos. O objetivo é aprovar os itens selecionados, definir o local de entrega e finalizar o processo para seguir com a cotação ou compra.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Aprovação de Produtos > Aprovação
- Tela/interface específica: Tela de Aprovação de Produtos

**Funcionalidade Detalhada:**
A funcionalidade de aprovação permite que o usuário aprove múltiplos produtos de uma só vez, evitando a necessidade de aprovar item a item. Após a aprovação, o usuário deve identificar o local de entrega dos produtos e finalizar o processo, escolhendo entre gerar um orçamento ou uma compra direta.

### 🔹 Passo a Passo Detalhado:

1. **Confirmar as Quantidades e Salvar**
   - Localização: Tela de Aprovação de Produtos
   - Como fazer: Após revisar as quantidades dos produtos, clique no botão **Salvar**.
   - Campos/Opções disponíveis:
     * `Quantidade`: Campo onde o usuário insere a quantidade de cada produto.
   - Resultado esperado: Os produtos aparecem como **aprovados** na tela.

2. **Identificar o Local de Entrega**
   - Localização: Tela de Aprovação de Produtos, seção de entrega.
   - Como fazer: Após salvar, localize a seção para identificar o **local de entrega** e preencha as informações necessárias.
   - Resultado esperado: O local de entrega é definido e salvo.

3. **Aprovação e Fluxo de Finalização**
   - Localização: Parte superior da tela de Aprovação de Produtos.
   - Como fazer: Clique no botão **Aprovar**. É importante notar que se o usuário sair dessa aba sem aprovar, a aprovação será desfeita.
   - Resultado esperado: Produtos aprovados são gerados para o local de entrega.

4. **Finalizar o Processo**
   - Localização: Após a aprovação, clique na opção **Finalizar**.
   - Como fazer: Na tela de finalização, escolha entre as opções de **Gerar Orçamento** ou **Compra Vulsa**.
   - Observações importantes: A opção de **Compra Vulsa** é utilizada quando o usuário já tem um fornecedor definido e os valores acordados.
   - Resultado esperado: O sistema avança para a próxima etapa, dependendo da opção escolhida.

5. **Selecionar Fornecedores**
   - Localização: Tela de listagem de fornecedores.
   - Como fazer: O sistema automaticamente puxa fornecedores que fornecem o tipo de produto. O usuário pode optar por excluir todos e selecionar apenas os fornecedores desejados.
   - Campos/Opções disponíveis:
     * `Fornecedor`: Lista de fornecedores disponíveis.
   - Resultado esperado: Apenas os fornecedores selecionados são incluídos na cotação.

6. **Enviar E-mail para Fornecedores**
   - Localização: Após selecionar os fornecedores.
   - Como fazer: O sistema possui um processo automático que envia um e-mail para os fornecedores selecionados, que poderão acessar as informações e preencher os dados necessários.
   - Resultado esperado: O e-mail é enviado e as informações retornam automaticamente para o sistema.

7. **Salvar a Aprovação Finalizada**
   - Localização: Tela de Aprovação de Produtos.
   - Como fazer: Clique no botão **Salvar** para finalizar a aprovação e manter o histórico.
   - Resultado esperado: A aprovação é finalizada e registrada no histórico do sistema.

**Campos e Parâmetros:**

| Campo                | Tipo         | Obrigatório | Descrição                                           | Exemplo                |
|----------------------|--------------|-------------|----------------------------------------------------|------------------------|
| `Quantidade`         | Numérico     | Sim         | Quantidade de produtos a serem aprovados.         | 10                     |
| `Local de Entrega`   | Texto        | Sim         | Endereço onde os produtos serão entregues.        | Rua Exemplo, 123       |
| `Fornecedor`         | Dropdown     | Sim         | Lista de fornecedores disponíveis para cotação.    | Fornecedor A, B, C     |

**Regras de Negócio:**
- A aprovação de produtos deve ser realizada antes de finalizar o processo.
- Se o usuário sair da aba sem aprovar, a aprovação será desfeita.
- O sistema filtra automaticamente os fornecedores com base nos produtos selecionados.
- O envio de e-mail para fornecedores é automático após a seleção.

**Observações Importantes:**
- É essencial salvar as alterações após cada etapa para evitar perda de dados.
- Evite sair da aba de aprovação antes de finalizar, pois isso pode desfazer as aprovações realizadas.
- Certifique-se de que os fornecedores estão corretamente cadastrados e vinculados aos produtos.

**Conceitos-Chave:**
- **Aprovação de Produtos**: Processo de validar e autorizar a aquisição de produtos no sistema.
- **Compra Vulsa**: Compra direta de produtos sem passar pelo processo de cotação.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como aprovar múltiplos produtos de uma só vez?
- O que acontece se eu sair da aba de aprovação sem finalizar?
- Como selecionar fornecedores para a cotação de produtos aprovados?

---


---


---

## 5. Preenchimento de Cotações pelo Fornecedor

**📋 METADADOS:**
- **ID:** sec_5
- **⏱️ Minutagem:** 10:02 → 12:34
- **⏲️ Duração:** 152s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/qFzqzIoiVE4?si=YoVxiJOkipNVbQWb&t=602)
- **📦 Módulo:** Processo de Compras
- **🏷️ Categorias:** Operacional, Cadastro, Relatório
- **🔑 Palavras-chave:** cotações, fornecedor, proposta, condições de pagamento, entrega

> **🔍 RESUMO EXECUTIVO:** Esta seção orienta sobre o processo de preenchimento de cotações por fornecedores, detalhando cada etapa desde o recebimento do e-mail até a proposta de condições de pagamento e informações de entrega.

**Contexto:**
Estamos no módulo de Processo de Compras, onde o fornecedor é convidado a participar do processo de cotações. O objetivo é permitir que o fornecedor preencha e envie suas propostas de forma clara e organizada.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Processo de Compras > Submenu Cotações
- Tela/interface específica: Tela de Preenchimento de Cotações

**Funcionalidade Detalhada:**

A funcionalidade permite que o fornecedor receba um e-mail com um convite para participar do processo de compras, onde ele poderá acessar um link para preencher sua oferta. O sistema apresenta informações sobre a empresa do fornecedor, lista de produtos, quantidades solicitadas e campos para preenchimento de valores e condições de pagamento.

### 🔹 Passo a Passo Detalhado:

1. **Recebimento do E-mail**
   - Localização: Caixa de entrada do e-mail do fornecedor
   - Como fazer: O fornecedor deve abrir o e-mail que contém o convite.
   - Conteúdo do e-mail: O e-mail inicia com "Olá, nome do fornecedor. Como parceiro credenciado, nome da sua empresa, você está convidado para fazer parte do nosso processo de compras. Por favor, clique abaixo e preencha sua oferta."
   - Resultado esperado: O fornecedor visualiza o convite e o link para o orçamento.

2. **Acesso ao Link de Orçamento**
   - Localização: E-mail recebido
   - Como fazer: O fornecedor deve clicar no link fornecido no e-mail.
   - Resultado esperado: O fornecedor é direcionado para uma nova página onde poderá preencher a proposta.

3. **Visualização das Informações da Empresa**
   - Localização: Página de preenchimento de cotações
   - Como fazer: O fornecedor visualiza as informações da sua empresa na parte superior da página.
   - Resultado esperado: O fornecedor confirma que as informações estão corretas.

4. **Preenchimento da Relação de Produtos e Quantidades**
   - Localização: Abaixo das informações da empresa
   - Como fazer: O fornecedor visualiza a lista de produtos e quantidades solicitadas, onde a quantidade a ser entregue é preenchida automaticamente.
   - Observações importantes: O fornecedor pode alterar a quantidade se necessário.
   - Resultado esperado: O fornecedor ajusta a quantidade conforme desejado.

5. **Inserção do Valor Unitário**
   - Localização: Campo de valor unitário
   - Como fazer: O fornecedor deve preencher o valor unitário do produto.
   - Exemplo: O fornecedor pode inserir um valor como "R$ 100,00".
   - Resultado esperado: O sistema calcula e apresenta automaticamente o valor total.

6. **Preenchimento do Prazo de Entrega e Desconto**
   - Localização: Campos de prazo de entrega e desconto
   - Como fazer: O fornecedor deve inserir o prazo de entrega e, opcionalmente, um desconto.
   - Observações importantes: O campo de desconto é opcional.
   - Resultado esperado: O fornecedor pode visualizar os comentários inseridos e sugestões.

7. **Adição de Sugestões**
   - Localização: Campo de sugestões
   - Como fazer: O fornecedor pode indicar outros valores ou marcas para o mesmo produto.
   - Resultado esperado: As sugestões são salvas e podem ser visualizadas.

8. **Proposta de Condições de Pagamento**
   - Localização: Botão "Próximo" e seção de condições de pagamento
   - Como fazer: O fornecedor clica em "Próximo" e é direcionado para a seção onde pode propor condições de pagamento.
   - Exemplos de condições: 
     * Pagamento à vista: "Conseguimos 5% de desconto."
     * Pagamento a prazo: "Parcelamento em até 10 vezes."
     * Pagamento antecipado: "Conseguimos até 10% de desconto."
   - Resultado esperado: O fornecedor pode selecionar uma condição ou criar uma nova.

9. **Informações sobre o Local de Entrega**
   - Localização: Seção de informações de entrega
   - Como fazer: O fornecedor deve preencher a validade do orçamento e o tipo de frete.
   - Resultado esperado: As informações de entrega são salvas.

**Campos e Parâmetros:**

| Campo                     | Tipo         | Obrigatório | Descrição                                           | Exemplo            |
|---------------------------|--------------|-------------|----------------------------------------------------|--------------------|
| Nome do Fornecedor        | Texto        | Sim         | Nome da empresa do fornecedor                       | "Fornecedor XYZ"   |
| Valor Unitário            | Moeda        | Sim         | Valor por unidade do produto                        | "R$ 100,00"        |
| Quantidade                | Número       | Sim         | Quantidade de produtos solicitados                 | "10"               |
| Prazo de Entrega          | Texto        | Sim         | Prazo em dias para entrega do produto              | "5 dias"           |
| Desconto                  | Percentual   | Não         | Percentual de desconto oferecido                    | "10%"              |
| Sugestões                 | Texto        | Não         | Sugestões de outros valores ou marcas               | "Marca A, Marca B" |
| Condições de Pagamento    | Texto        | Sim         | Propostas de condições de pagamento                 | "À vista, parcelado"|
| Validade do Orçamento     | Data         | Sim         | Data de validade da proposta                        | "30/12/2023"       |
| Tipo de Frete             | Dropdown     | Sim         | Opções de frete disponíveis                         | "Normal, Expresso"  |

**Regras de Negócio:**
- O valor unitário deve ser preenchido para que o sistema calcule o valor total.
- O desconto é opcional, mas se preenchido, deve ser um valor percentual.
- O fornecedor pode alterar a quantidade de produtos solicitados.
- As condições de pagamento devem ser propostas pelo fornecedor e podem ser selecionadas ou criadas novas.

**Observações Importantes:**
- O fornecedor deve verificar se todas as informações estão corretas antes de enviar a proposta.
- Erros comuns incluem não preencher o valor unitário ou a quantidade.
- O sistema pode ter restrições quanto ao tipo de frete disponível.

**Conceitos-Chave:**
- **Cotação**: Proposta de preços e condições para fornecimento de produtos.
- **Condições de Pagamento**: Termos que definem como e quando o pagamento será realizado.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como o fornecedor deve preencher a cotação?
- Quais informações são necessárias para enviar uma proposta?
- O que o fornecedor deve fazer se quiser sugerir outras marcas ou valores?

---


---


---

## 6. Visualização e Comparação de Orçamentos

**📋 METADADOS:**
- **ID:** sec_6
- **⏱️ Minutagem:** 12:32 → 15:04
- **⏲️ Duração:** 152s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/qFzqzIoiVE4?si=YoVxiJOkipNVbQWb&t=752)
- **📦 Módulo:** Compras
- **🏷️ Categorias:** Orçamentos, Visualização, Comparação, Relatórios
- **🔑 Palavras-chave:** orçamento, fornecedor, comparação, visualização, cotação, entrega, valor, frete

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como visualizar e comparar orçamentos no sistema, permitindo que o usuário analise diferentes fornecedores e suas propostas de forma eficiente, facilitando a tomada de decisão.

**Contexto:**
Estamos na área de orçamentos do módulo de compras, onde o usuário pode visualizar as cotações recebidas de diferentes fornecedores e compará-las com base em critérios como preço e prazo de entrega.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Compras > Orçamentos
- Tela/interface específica: Tela de Orçamentos

**Funcionalidade Detalhada:**
A funcionalidade de visualização e comparação de orçamentos permite que o usuário analise as cotações recebidas de fornecedores. O sistema oferece diferentes formas de visualização, permitindo que o usuário escolha entre visualizar por produto, por fornecedor ou por conjunto de orçamento. Cada visualização apresenta informações detalhadas sobre os orçamentos, como valor unitário, total, prazo de entrega, frete e condições de pagamento.

### 🔹 Passo a Passo Detalhado:

1. **Visualizar Orçamentos por Produto**
   - Localização: Aba de Orçamentos na tela principal do módulo de Compras.
   - Como fazer: Clique na opção "Por Produto" localizada na parte superior da tela.
   - Campos/Opções disponíveis:
     * `Histórico de Cotação`: Mostra o histórico de cotações para cada produto.
     * `Comparativo`: Exibe a comparação entre o melhor valor e a entrega mais rápida, sinalizando com cores.
   - Resultado esperado: O sistema separa cada produto, permitindo visualizar o histórico de cotações e comparações de forma clara.

2. **Visualizar Orçamentos por Fornecedor**
   - Localização: Aba de Orçamentos na tela principal do módulo de Compras.
   - Como fazer: Clique na opção "Por Fornecedor" na parte superior da tela.
   - Observações importantes: Esta visualização mostra todos os orçamentos cotados com um parceiro, independentemente de terem sido respondidos ou não.
   - Resultado esperado: O usuário vê todos os orçamentos relacionados a um fornecedor específico, como "Casas d'Água", e pode acessar os orçamentos 467 e 468, que contêm produtos diferentes.

3. **Visualizar Orçamentos por Conjunto de Orçamento**
   - Localização: Aba de Orçamentos na tela principal do módulo de Compras.
   - Como fazer: Clique na opção "Por Conjunto de Orçamento" na parte superior da tela.
   - Resultado esperado: O usuário visualiza todos os orçamentos agrupados, como o orçamento 468, onde são listados os fornecedores A e B, além de informações sobre retornos pendentes.

4. **Visualizar Detalhes do Orçamento**
   - Localização: Dentro da visualização de orçamentos por conjunto.
   - Como fazer: Clique no orçamento específico (ex: orçamento 468) para expandir e visualizar detalhes.
   - Campos/Opções disponíveis:
     * `Valor Unitário`: O preço por unidade do produto.
     * `Total`: O valor total do orçamento.
     * `Prazo de Entrega`: O tempo estimado para a entrega do produto.
     * `Frete`: Campo onde o fornecedor pode informar o valor do frete (opcional).
     * `Condições de Pagamento`: Informações sobre como o pagamento deve ser realizado.
   - Resultado esperado: O usuário obtém uma visão detalhada de cada orçamento, incluindo informações sobre valores, prazos e condições.

5. **Preenchimento de Orçamento**
   - Localização: Tela de Orçamentos ao criar ou editar um orçamento.
   - Como fazer: O usuário pode optar por preencher as informações automaticamente via e-mail ou manualmente.
   - Observações importantes: O preenchimento automático pode ser útil se o usuário já tiver recebido o retorno do fornecedor.
   - Resultado esperado: O orçamento é salvo com sucesso, e o usuário pode visualizar as informações na aba de orçamentos.

**Campos e Parâmetros:**

| Campo                  | Tipo         | Obrigatório | Descrição                                           | Exemplo               |
|------------------------|--------------|-------------|----------------------------------------------------|-----------------------|
| `Valor Unitário`       | Numérico     | Sim         | Preço por unidade do produto                        | 10,00                 |
| `Total`                | Numérico     | Sim         | Valor total do orçamento                            | 100,00                |
| `Prazo de Entrega`     | Texto        | Sim         | Tempo estimado para a entrega                      | 5 dias                |
| `Frete`                | Numérico     | Não         | Valor do frete cobrado pelo fornecedor             | 15,00                 |
| `Condições de Pagamento`| Texto       | Sim         | Informações sobre as condições de pagamento        | À vista, 30 dias      |

**Regras de Negócio:**
- O campo `Frete` é opcional e pode ser preenchido pelo fornecedor se desejar cobrar pelo frete.
- As informações exibidas nas visualizações são baseadas nos dados preenchidos pelo usuário ou pelo fornecedor.
- O sistema permite diferentes formas de visualização, mas as informações permanecem consistentes.

**Observações Importantes:**
- O usuário deve sempre verificar se as informações estão corretas antes de salvar o orçamento.
- Erros comuns incluem não preencher todos os campos obrigatórios, o que pode impedir o salvamento do orçamento.
- O preenchimento automático via e-mail é uma opção que pode economizar tempo, mas deve ser utilizado com cautela para garantir a precisão dos dados.

**Conceitos-Chave:**
- **Orçamento**: Proposta de preço e condições de fornecimento de produtos ou serviços.
- **Fornecedor**: Entidade responsável pela entrega dos produtos e serviços cotados.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso visualizar os orçamentos recebidos de diferentes fornecedores?
- Quais informações estão disponíveis ao comparar orçamentos por produto ou fornecedor?
- O que devo fazer se não obtive retorno de um fornecedor em um orçamento?

---


---


---

## 7. Adição e Negociação de Fornecedores

**📋 METADADOS:**
- **ID:** sec_7
- **⏱️ Minutagem:** 15:02 → 17:35
- **⏲️ Duração:** 152s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/qFzqzIoiVE4?si=YoVxiJOkipNVbQWb&t=902)
- **📦 Módulo:** Gestão de Fornecedores
- **🏷️ Categorias:** Operacional, Negociação, Compras
- **🔑 Palavras-chave:** fornecedor, orçamento, negociar, carrinho, pagamento, desconto, ordem de compra

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de adição de fornecedores e a negociação de orçamentos, permitindo ao usuário selecionar opções de pagamento, revisar informações de entrega e criar uma ordem de compra.

**Contexto:**
Estamos na etapa de negociação com fornecedores dentro do sistema de gestão de compras. O objetivo é selecionar um fornecedor, revisar as cotações e formalizar a compra através da criação de uma ordem de compra.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Gestão de Fornecedores > Negociação de Orçamentos
- Tela/interface específica: Tela de Negociação de Fornecedores

**Funcionalidade Detalhada:**

A funcionalidade permite ao usuário editar orçamentos de fornecedores, visualizar diferentes cotações e selecionar a melhor opção para prosseguir com a compra. O usuário pode adicionar produtos ao carrinho, negociar condições de entrega e pagamento, e finalmente criar uma ordem de compra.

### 🔹 Passo a Passo Detalhado:

1. **Selecionar Fornecedor**
   - Localização: Tela de Negociação de Fornecedores
   - Como fazer: Clique nos três pontinhos ao lado do fornecedor desejado para acessar opções adicionais.
   - Campos/Opções disponíveis:
     * `Editar Orçamento`: Permite ao usuário preencher informações sobre o retorno do orçamento.
   - Resultado esperado: O orçamento do fornecedor é exibido para edição.

2. **Adicionar ao Carrinho**
   - Localização: Tela de Negociação de Fornecedores
   - Como fazer: Após decidir com qual fornecedor você irá comprar, clique no botão **Adicionar**.
   - Resultado esperado: O produto é adicionado ao carrinho de compras.

3. **Acessar Carrinho**
   - Localização: Parte superior da tela, clique em **Carrinho**.
   - Como fazer: Clique na opção **Negociar** dentro do carrinho.
   - Resultado esperado: A tela de negociação é exibida, mostrando as referências dos produtos definidos.

4. **Remover Negociações**
   - Localização: Tela de Negociação
   - Como fazer: Se houver negociações em aberto, você pode removê-las clicando na opção correspondente.
   - Resultado esperado: Apenas os produtos que você deseja levar adiante permanecem na negociação.

5. **Visualizar Dados do Fornecedor**
   - Localização: Tela de Negociação
   - Como fazer: Visualize os dados do fornecedor, incluindo o histórico de compras.
   - Resultado esperado: Informações detalhadas sobre o fornecedor são exibidas.

6. **Definir Informações de Entrega**
   - Localização: Tela de Negociação
   - Como fazer: Insira informações sobre entrega, incluindo o valor do frete.
   - Resultado esperado: O valor do frete é avaliado e considerado na negociação.

7. **Selecionar Opções de Pagamento**
   - Localização: Tela de Negociação
   - Como fazer: O fornecedor propõe três opções de pagamento. Se nenhuma delas atender, clique em **Adicionar nova forma de pagamento**.
   - Resultado esperado: Uma nova opção de pagamento é adicionada à negociação.

8. **Inserir Comentários**
   - Localização: Tela de Negociação
   - Como fazer: Utilize o campo para inserir um comentário sobre a negociação.
   - Resultado esperado: O comentário é salvo e associado à negociação.

9. **Revisar Resumo do Pedido**
   - Localização: Lateral da tela, opção **Resumo do Pedido**.
   - Como fazer: Analise os subtotais, local de entrega e data.
   - Resultado esperado: Informações detalhadas do pedido são apresentadas.

10. **Inserir Descontos**
    - Localização: Resumo do Pedido
    - Como fazer: Preencha os campos para desconto negociado em relação ao produto e desconto negociado em relação ao frete.
    - Resultado esperado: O valor total é reajustado automaticamente.

11. **Criar Ordem de Compra**
    - Localização: Tela de Negociação
    - Como fazer: Após validar todas as informações, clique em **Criar Ordem de Compra**.
    - Resultado esperado: A ordem de compra é criada e um segundo e-mail pode ser enviado ao fornecedor.

12. **Enviar E-mail ao Fornecedor**
    - Localização: Tela de Negociação
    - Como fazer: Se desejar, envie um e-mail ao fornecedor com a mensagem "Parabéns, você foi escolhido".
    - Resultado esperado: O fornecedor recebe um e-mail com um relatório dos dados da compra e a opção de aprovar ou não.

**Campos e Parâmetros:**

| Campo                          | Tipo       | Obrigatório | Descrição                                                                 | Exemplo                     |
|--------------------------------|------------|-------------|---------------------------------------------------------------------------|-----------------------------|
| `Editar Orçamento`            | Botão      | Não         | Permite editar o orçamento do fornecedor.                                | -                           |
| `Adicionar`                    | Botão      | Sim         | Adiciona o produto selecionado ao carrinho.                             | -                           |
| `Negociar`                    | Botão      | Sim         | Acessa a tela de negociação para o produto no carrinho.                | -                           |
| `Forma de Pagamento`          | Dropdown   | Não         | Opções de pagamento propostas pelo fornecedor.                           | Cartão, Boleto, Transferência|
| `Comentários`                  | Campo de texto | Não      | Campo para inserir comentários sobre a negociação.                       | "Negociar melhor preço"    |
| `Desconto Produto`            | Campo      | Não         | Campo para inserir desconto negociado em relação ao produto.            | 10%                         |
| `Desconto Frete`              | Campo      | Não         | Campo para inserir desconto negociado em relação ao frete.              | R$ 15,00                    |

**Regras de Negócio:**
- O usuário deve selecionar um fornecedor antes de adicionar produtos ao carrinho.
- O e-mail ao fornecedor é opcional e não é necessário para lançar a nota.
- Os descontos inseridos devem ser validados para não ultrapassarem o valor total.

**Observações Importantes:**
- É importante revisar todas as informações antes de criar a ordem de compra.
- Erros comuns incluem não verificar o valor do frete antes de finalizar a negociação.
- O sistema permite a edição de orçamentos, mas é necessário ter cuidado para não perder informações importantes.

**Conceitos-Chave:**
- **Ordem de Compra**: Documento que formaliza a compra de produtos ou serviços, contendo detalhes como preços, quantidades e condições de pagamento.
- **Negociação**: Processo de discussão entre comprador e fornecedor para chegar a um acordo sobre preços e condições.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso adicionar um fornecedor ao meu carrinho de compras?
- Quais informações posso editar no orçamento do fornecedor?
- Como envio um e-mail de confirmação ao fornecedor após a negociação?

---


---


---

## 8. Processo de Criação e Lançamento de Nota Fiscal

**📋 METADADOS:**
- **ID:** sec_8
- **⏱️ Minutagem:** 17:33 → 20:07
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/qFzqzIoiVE4?si=YoVxiJOkipNVbQWb&t=1053)
- **📦 Módulo:** Compras
- **🏷️ Categorias:** Operacional, Financeiro, Compras
- **🔑 Palavras-chave:** ordem de compra, nota fiscal, lançamento, recibo, financeiro

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de criação de uma ordem de compra e o subsequente lançamento de uma nota fiscal, abordando a necessidade de aprovação interna e os campos obrigatórios para o registro financeiro.

**Contexto:**
Estamos no módulo de Compras do sistema, onde o usuário finaliza a criação de uma ordem de compra e, em seguida, realiza o lançamento de uma nota fiscal para gerar o pagamento. O objetivo é garantir que todas as informações necessárias sejam registradas corretamente para o fluxo financeiro.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Compras > Submenu Ordem de Compra
- Tela/interface específica: Tela de Criação de Ordem de Compra e Lançamento de Nota Fiscal

**Funcionalidade Detalhada:**
Esta funcionalidade permite que o usuário crie uma ordem de compra que deve ser aprovada internamente antes de prosseguir. Após a aprovação, o usuário pode lançar uma nota fiscal, que pode ser eletrônica ou manual, para formalizar o pagamento. O sistema já preenche automaticamente as informações da ordem de compra, facilitando o processo.

### 🔹 Passo a Passo Detalhado:

1. **Criação da Ordem de Compra**
   - Localização: Tela de Criação de Ordem de Compra
   - Como fazer: Após definir se deseja enviar um e-mail de confirmação, clique no botão **Salvar**.
   - Campos/Opções disponíveis:
     * `E-mail de Confirmação`: Opção para enviar ou não um e-mail.
   - Resultado esperado: A ordem de compra é criada automaticamente, com todas as informações necessárias preenchidas, como produtos, quantidades e valores.

2. **Complementação da Ordem de Compra**
   - Localização: Tela de Ordem de Compra
   - Como fazer: Verifique se há necessidade de complementar informações sobre o estado da ordem, dependendo do retorno do fornecedor.
   - Observações importantes: O fluxo de compras é interrompido até que a ordem de compra seja formalizada.
   - Resultado esperado: A ordem de compra permanece no sistema, aguardando a formalização.

3. **Lançamento da Nota Fiscal**
   - Localização: Módulo Financeiro
   - Como fazer: Acesse a opção de lançamento de nota e escolha entre **Nota Eletrônica** ou **Nota Manual**. Neste caso, selecione **Nota Manual**.
   - Campos/Opções disponíveis:
     * `Tipo de Recibo`: Selecione **Recibo de Produtos**.
   - Resultado esperado: O sistema solicita a escolha da ordem de compra associada.

4. **Seleção da Ordem de Compra**
   - Localização: Tela de Lançamento de Nota Fiscal
   - Como fazer: Escolha a ordem de compra desejada, que já trará algumas informações preenchidas automaticamente.
   - Campos/Opções disponíveis:
     * `Data de Emissão`: Campo obrigatório para inserir a data.
   - Resultado esperado: Com a ordem de compra selecionada, o sistema avança para o próximo passo.

5. **Complementação de Informações da Nota**
   - Localização: Tela de Lançamento de Nota Fiscal
   - Como fazer: Opcionalmente, adicione informações como número de documento, anexe a nota e insira observações.
   - Observações importantes: Esses campos são opcionais, mas podem ser úteis para registro.
   - Resultado esperado: As informações complementares são salvas, se inseridas.

6. **Relação de Produtos e Valores**
   - Localização: Tela de Lançamento de Nota Fiscal
   - Como fazer: Verifique a relação de produtos, quantidades e valores que já foram preenchidos a partir da ordem de compra.
   - Observações importantes: O financeiro validará se as informações correspondem à nota em mãos.
   - Resultado esperado: A relação de produtos é confirmada e validada.

7. **Definição de Pagamento**
   - Localização: Tela de Lançamento de Nota Fiscal
   - Como fazer: Classifique o fluxo de caixa, identificando o custo relacionado. Preencha os campos de desconto e frete, que já podem estar preenchidos automaticamente.
   - Campos/Opções disponíveis:
     * `Classificação`: Campo para identificar o custo.
     * `Desconto`: Campo para inserir valores de desconto.
     * `Frete`: Campo para inserir valores de frete.
   - Resultado esperado: O sistema gera o financeiro, permitindo definir parcelas, vencimento e formas de pagamento.

8. **Geração do Financeiro**
   - Localização: Tela de Lançamento de Nota Fiscal
   - Como fazer: Clique em **Gerar Financeiro** e defina a quantidade de parcelas, vencimento e formas de pagamento.
   - Campos/Opções disponíveis:
     * `Quantidade de Parcelas`: Campo para definir quantas parcelas.
     * `Vencimento`: Campo para definir a data de vencimento.
     * `Forma de Pagamento`: Dropdown com opções de pagamento.
   - Resultado esperado: O financeiro é gerado com as informações inseridas.

**Campos e Parâmetros:**

| Campo                     | Tipo          | Obrigatório | Descrição                                                                 | Exemplo              |
|---------------------------|---------------|-------------|---------------------------------------------------------------------------|----------------------|
| E-mail de Confirmação     | Checkbox      | Não         | Opção para enviar um e-mail de confirmação da ordem de compra.           | Sim/Não              |
| Tipo de Recibo            | Dropdown      | Sim         | Tipo de recibo a ser gerado.                                             | Recibo de Produtos    |
| Ordem de Compra           | Dropdown      | Sim         | Seleção da ordem de compra associada à nota fiscal.                      | Ordem #123           |
| Data de Emissão           | Data          | Sim         | Data em que a nota fiscal é emitida.                                    | 01/01/2023           |
| Número de Documento        | Texto         | Não         | Número do documento da nota fiscal.                                      | 123456               |
| Observação                | Texto          | Não         | Observações adicionais sobre a nota fiscal.                              | Nota referente ao pedido. |
| Classificação             | Texto          | Sim         | Classificação do fluxo de caixa referente ao custo.                      | Compra de Materiais  |
| Desconto                  | Número        | Não         | Valor de desconto aplicado à nota fiscal.                                | 10.00                |
| Frete                     | Número        | Não         | Valor do frete associado à compra.                                       | 15.00                |
| Quantidade de Parcelas    | Número        | Sim         | Número de parcelas para pagamento.                                        | 3                    |
| Vencimento                | Data          | Sim         | Data de vencimento da primeira parcela.                                   | 01/02/2023           |
| Forma de Pagamento        | Dropdown      | Sim         | Método de pagamento a ser utilizado.                                     | Cartão de Crédito    |

**Regras de Negócio:**
- A ordem de compra deve ser aprovada internamente antes de ser formalizada.
- O lançamento da nota fiscal pode ser feito como eletrônica ou manual, sendo que o exemplo dado é de uma nota manual.
- O campo **Data de Emissão** é obrigatório para o lançamento da nota fiscal.
- O financeiro deve validar se as informações da nota correspondem à ordem de compra.

**Observações Importantes:**
- É opcional anexar documentos ou adicionar observações durante o lançamento da nota fiscal.
- Erros comuns incluem não preencher campos obrigatórios, o que pode impedir a conclusão do processo.
- A formalização da ordem de compra é crucial para o fluxo de pagamentos.

**Conceitos-Chave:**
- **Ordem de Compra**: Documento que formaliza a intenção de compra de produtos ou serviços.
- **Nota Fiscal**: Documento que registra a transação comercial e é necessário para o processo de pagamento.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como criar uma ordem de compra no sistema?
- Quais são os campos obrigatórios para lançar uma nota fiscal?
- O que fazer se a ordem de compra não for aprovada?

---


---


---

## 9. Lançamento de Nota e Entrada de Produto no Estoque

**📋 METADADOS:**
- **ID:** sec_9
- **⏱️ Minutagem:** 20:04 → 22:39
- **⏲️ Duração:** 154s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/qFzqzIoiVE4?si=YoVxiJOkipNVbQWb&t=1204)
- **📦 Módulo:** Suprimentos
- **🏷️ Categorias:** Operacional, Compras, Estoque
- **🔑 Palavras-chave:** nota, ordem de compra, estoque, cronograma financeiro, contas a pagar

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de lançamento de uma nota fiscal e a entrada do produto no estoque, explicando como a quantidade lançada impacta a ordem de compra e o cronograma financeiro.

**Contexto:**
Estamos no módulo de Suprimentos, onde o usuário realiza o lançamento de notas fiscais vinculadas a ordens de compra. O objetivo é garantir que a quantidade de produtos recebidos corresponda à quantidade solicitada, permitindo a atualização do estoque e a geração de informações financeiras.

**Localização no Sistema:**
- Caminho de navegação: Menu Principal > Módulo Suprimentos > Submenu Entradas
- Tela/interface específica: Tela de Lançamento de Nota e Conferência de Entradas

**Funcionalidade Detalhada:**
A funcionalidade de lançamento de nota permite registrar a entrada de produtos no estoque. Este processo é crucial, pois, ao lançar a nota, a ordem de compra vinculada é automaticamente finalizada se a quantidade recebida corresponder à quantidade solicitada. Caso contrário, a ordem de compra permanece em andamento, permitindo o lançamento de notas adicionais. Além disso, a nota fiscal gera um cronograma financeiro que é utilizado para comparativos no setor de engenharia.

### 🔹 Passo a Passo Detalhado:

1. **Salvar Nota Fiscal**
   - Localização: Tela de Lançamento de Nota
   - Como fazer: Após preencher todos os campos necessários da nota, clique no botão **Salvar**.
   - Resultado esperado: A nota fiscal é registrada no sistema e a ordem de compra vinculada é avaliada.

2. **Verificação da Ordem de Compra**
   - Localização: Tela de Ordens de Compra
   - Como fazer: Acesse a lista de ordens de compra e verifique o status da ordem vinculada à nota lançada.
   - Observações importantes: Se a quantidade recebida for igual à quantidade solicitada, a ordem de compra será finalizada automaticamente. Se não, o status permanecerá como "Andamento".
   - Resultado esperado: O status da ordem de compra é atualizado conforme a quantidade recebida.

3. **Geração do Cronograma Financeiro**
   - Localização: Tela de Cronograma Financeiro
   - Como fazer: Após o lançamento da nota, o sistema automaticamente gera o cronograma financeiro baseado nas informações da nota.
   - Resultado esperado: O cronograma financeiro é atualizado e disponível para consulta.

4. **Conferência de Entradas**
   - Localização: Menu Suprimentos > Submenu Entradas
   - Como fazer: Acesse a aba **Entradas** para visualizar as pendências de conferência.
   - Campos/Opções disponíveis:
     * `Quantidade Prevista`: Quantidade que foi solicitada na nota.
     * `Quantidade Real`: Quantidade que foi recebida.
   - Resultado esperado: Visualização das quantidades previstas e reais para conferência.

5. **Definir Setor**
   - Localização: Tela de Conferência de Entradas
   - Como fazer: Selecione o setor correspondente ao produto recebido no campo **Setor**.
   - Observações importantes: O setor deve ser previamente cadastrado no sistema.
   - Resultado esperado: O setor é definido e a conferência pode prosseguir.

6. **Salvar Conferência**
   - Localização: Tela de Conferência de Entradas
   - Como fazer: Após verificar que a `Quantidade Prevista` e a `Quantidade Real` estão corretas, clique no botão **Salvar**.
   - Resultado esperado: A conferência é registrada e o produto é adicionado ao estoque.

**Campos e Parâmetros:**

| Campo                | Tipo       | Obrigatório | Descrição                                           | Exemplo         |
|----------------------|------------|-------------|----------------------------------------------------|------------------|
| `Quantidade Prevista`| Numérico   | Sim         | Quantidade de produtos solicitados na nota         | 100              |
| `Quantidade Real`    | Numérico   | Sim         | Quantidade de produtos efetivamente recebidos      | 100              |
| `Setor`              | Dropdown   | Sim         | Setor responsável pela conferência da entrada      | Suprimentos      |

**Regras de Negócio:**
- A ordem de compra é finalizada automaticamente se a `Quantidade Real` for igual à `Quantidade Prevista`.
- Se a `Quantidade Real` for menor que a `Quantidade Prevista`, a ordem de compra permanece com status "Andamento".
- O cronograma financeiro é gerado automaticamente após o lançamento da nota.

**Observações Importantes:**
- Certifique-se de que todos os dados da nota estão corretos antes de salvar.
- Evite lançar notas com quantidades incorretas para evitar complicações no estoque.
- O setor deve ser previamente cadastrado para que a conferência seja realizada corretamente.

**Conceitos-Chave:**
- **Nota Fiscal**: Documento que formaliza a compra de produtos, essencial para o controle de estoque e financeiro.
- **Ordem de Compra**: Documento que autoriza a aquisição de produtos, vinculando a solicitação à entrega.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como lançar uma nota fiscal no sistema?
- O que acontece com a ordem de compra após o lançamento da nota?
- Como verificar se a quantidade recebida corresponde à quantidade solicitada?

---


---


---

## 10. Criação de Ordem de Serviço

**📋 METADADOS:**
- **ID:** sec_10
- **⏱️ Minutagem:** 22:36 → 25:12
- **⏲️ Duração:** 155s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/qFzqzIoiVE4?si=YoVxiJOkipNVbQWb&t=1356)
- **📦 Módulo:** Gestão de Obras
- **🏷️ Categorias:** Operacional, Cadastro, Administração
- **🔑 Palavras-chave:** ordem de serviço, prestador, centro de custo, serviços, pagamento

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de criação de uma ordem de serviço no sistema, incluindo a seleção de prestadores, definição de centros de custo e formas de pagamento, permitindo uma gestão eficiente das atividades relacionadas a obras.

**Contexto:**
Estamos na interface de criação de uma ordem de serviço dentro do módulo de Gestão de Obras. O objetivo desta seção é guiar o usuário através do processo de formalização de uma ordem de serviço e o lançamento da nota no financeiro.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Gestão de Obras > Ordem de Serviço
- Tela/interface específica: Tela de Criação de Ordem de Serviço

**Funcionalidade Detalhada:**
A funcionalidade de criação de ordem de serviço permite ao usuário formalizar a contratação de prestadores de serviços para obras específicas. O sistema possibilita a seleção de serviços já cadastrados, a definição de centros de custo e a configuração de formas de pagamento. Essa funcionalidade é essencial para garantir que os serviços sejam registrados corretamente e que os pagamentos sejam processados de acordo com as condições acordadas.

### 🔹 Passo a Passo Detalhado:

1. **Criar Ordem de Serviço**
   - Localização: Tela de Criação de Ordem de Serviço
   - Como fazer: Clique no botão **"Mais Ordem de Serviço"** para iniciar o processo de criação.
   - Campos/Opções disponíveis:
     * `Prestador`: Selecionar o prestador de serviços que irá realizar a atividade.
     * `Centro de Custo`: Selecionar o centro de custo relacionado à obra.
   - Resultado esperado: Uma nova ordem de serviço é iniciada, permitindo a configuração dos detalhes necessários.

2. **Definir Prestador e Centro de Custo**
   - Localização: Seção de seleção de prestador e centro de custo na tela de criação.
   - Como fazer: Escolha o prestador desejado (ex: **Edivaldo**) e o centro de custo (ex: **Vila Real**) nos respectivos campos.
   - Observações importantes: O prestador deve estar previamente cadastrado no sistema. O centro de custo deve estar relacionado à obra em questão.
   - Resultado esperado: O prestador e o centro de custo são definidos, permitindo prosseguir para a próxima etapa.

3. **Selecionar Serviço**
   - Localização: Lateral da tela, onde há uma listagem dos serviços cadastrados.
   - Como fazer: Escolha o serviço desejado (ex: **Assentamento**) da lista. Se o serviço não estiver disponível, utilize a opção para adicionar um novo serviço.
   - Resultado esperado: O serviço selecionado é adicionado à ordem de serviço.

4. **Especificar Acompanhamento de Obra**
   - Localização: Campo de acompanhamento de obra na tela.
   - Como fazer: Se necessário, especifique o acompanhamento de obra, que cria um relacionamento com a estrutura de engenharia. Caso não seja necessário, este campo não aparecerá.
   - Resultado esperado: A ordem de serviço é configurada com ou sem acompanhamento, dependendo da necessidade.

5. **Definir Quantidade e Etapas**
   - Localização: Campo para definir a quantidade de serviços na etapa correspondente.
   - Como fazer: Insira a quantidade de serviços a serem realizados na etapa relacionada.
   - Resultado esperado: A quantidade é registrada na ordem de serviço.

6. **Salvar Informações**
   - Localização: Botão **"Salvar"** na parte inferior da tela.
   - Como fazer: Após preencher todos os campos necessários, clique em **"Salvar"** para registrar as informações.
   - Resultado esperado: As informações da ordem de serviço são salvas no sistema.

7. **Preencher Campos Complementares**
   - Localização: Campos de descrição, data inicial e final abaixo da quantidade.
   - Como fazer: Preencha a descrição do serviço e as datas inicial e final conforme necessário.
   - Resultado esperado: Informações complementares são adicionadas à ordem de serviço.

8. **Definir Forma de Pagamento**
   - Localização: Seção de formas de pagamento na tela.
   - Como fazer: Escolha a forma de pagamento desejada. As opções disponíveis incluem:
     * **À vista**: Valor pago inicialmente, com a possibilidade de adicionar um desconto.
     * **Parcelado**: Defina as condições de parcelamento, como número de parcelas (ex: 10 vezes) ou quantidades de dias para boletos.
   - Observações importantes: As opções de pagamento são semelhantes às vistas nas ordens de compra.
   - Resultado esperado: A forma de pagamento é configurada para a ordem de serviço.

**Campos e Parâmetros:**

| Campo                | Tipo        | Obrigatório | Descrição                                               | Exemplo              |
|----------------------|-------------|-------------|--------------------------------------------------------|----------------------|
| Prestador            | Dropdown    | Sim         | Seleciona o prestador de serviços para a ordem.       | Edivaldo             |
| Centro de Custo      | Dropdown    | Sim         | Seleciona o centro de custo relacionado à obra.       | Vila Real            |
| Serviço              | Dropdown    | Sim         | Seleciona o serviço a ser realizado.                   | Assentamento         |
| Quantidade           | Numérico    | Sim         | Define a quantidade de serviços a serem realizados.    | 10                   |
| Descrição            | Texto       | Não         | Campo para adicionar uma descrição do serviço.         | Assentamento de piso  |
| Data Inicial         | Data        | Não         | Define a data de início do serviço.                    | 01/01/2024           |
| Data Final           | Data        | Não         | Define a data de término do serviço.                   | 10/01/2024           |
| Forma de Pagamento    | Dropdown    | Sim         | Seleciona a forma de pagamento (à vista ou parcelado). | À vista              |

**Regras de Negócio:**
- O prestador deve estar cadastrado no sistema para ser selecionado.
- O centro de custo deve estar vinculado à obra em questão.
- O serviço deve ser previamente cadastrado para ser selecionado.
- A forma de pagamento deve ser definida antes de finalizar a ordem de serviço.

**Observações Importantes:**
- Certifique-se de que todos os campos obrigatórios estejam preenchidos antes de salvar a ordem de serviço.
- Evite selecionar serviços que não estão relacionados ao prestador escolhido.
- Verifique as condições de pagamento para evitar erros na configuração.

**Conceitos-Chave:**
- **Ordem de Serviço**: Documento que formaliza a contratação de serviços para uma obra específica.
- **Centro de Custo**: Categoria que permite o controle financeiro e orçamentário das despesas relacionadas a uma obra.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como criar uma ordem de serviço no sistema?
- Quais informações são necessárias para formalizar uma ordem de serviço?
- Como definir a forma de pagamento para uma ordem de serviço?

---


---


---

## 11. Cadastro e Gestão de Parceiros

**📋 METADADOS:**
- **ID:** sec_11
- **⏱️ Minutagem:** 25:07 → 27:39
- **⏲️ Duração:** 152s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/qFzqzIoiVE4?si=YoVxiJOkipNVbQWb&t=1507)
- **📦 Módulo:** Cadastro de Parceiros
- **🏷️ Categorias:** Cadastro, Operacional, Administração
- **🔑 Palavras-chave:** cadastro, fornecedor, prestador de serviço, CNPJ, CPF, e-mail, endereço

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como cadastrar e gerenciar parceiros no sistema, incluindo fornecedores e prestadores de serviço, detalhando os campos obrigatórios e opções disponíveis para garantir um cadastro completo e funcional.

**Contexto:**
Estamos na aba de parceiros do sistema, onde o objetivo é cadastrar novos fornecedores, prestadores de serviço, imobiliárias e transportadoras. O sistema permite tanto o cadastro manual quanto a importação de dados via planilha.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Cadastro de Parceiros
- Tela/interface específica: Aba de Parceiros

**Funcionalidade Detalhada:**
A funcionalidade de cadastro de parceiros permite que o usuário registre informações essenciais sobre fornecedores e prestadores de serviço. O sistema requer o preenchimento de campos obrigatórios, como CNPJ ou CPF, nome fantasia e razão social, para que o cadastro seja efetivado. Além disso, é possível editar informações de parceiros já cadastrados e importar dados de planilhas.

### 🔹 Passo a Passo Detalhado:

1. **Iniciar Cadastro de Novo Parceiro**
   - Localização: Tela da aba de parceiros, botão **"Mais Novo Parceiro"**.
   - Como fazer: Clique no botão **"Mais Novo Parceiro"** para abrir o formulário de cadastro.
   - Campos/Opções disponíveis:
     * `CNPJ ou CPF`: Campo obrigatório onde deve ser inserido o CNPJ (para pessoas jurídicas) ou CPF (para pessoas físicas).
     * `Nome Fantasia`: Campo obrigatório para o nome pelo qual o parceiro é conhecido.
     * `Razão Social`: Campo obrigatório que representa o nome legal do parceiro.
   - Resultado esperado: O parceiro é cadastrado no sistema, desde que os campos obrigatórios sejam preenchidos corretamente.

2. **Selecionar e Editar Parceiro Cadastrado**
   - Localização: Lista de parceiros já cadastrados, botão **"Editar"** ao lado do parceiro selecionado.
   - Como fazer: Clique no botão **"Editar"** ao lado do parceiro desejado para modificar suas informações.
   - Observações importantes: É recomendável preencher o campo de **e-mail** do fornecedor, pois isso é necessário para processos automáticos e comunicação.
   - Resultado esperado: As informações do parceiro são atualizadas no sistema.

3. **Preencher Informações Adicionais**
   - Localização: Formulário de edição do parceiro, aba **"Informações Gerais"**.
   - Como fazer: Após selecionar um parceiro, preencha os campos adicionais conforme necessário.
   - Campos/Opções disponíveis:
     * `E-mail`: Campo onde deve ser inserido o e-mail do parceiro.
     * `Endereço`: Campo para preenchimento do endereço do parceiro.
   - Resultado esperado: As informações adicionais são salvas e o cadastro do parceiro fica mais completo.

4. **Preencher Endereço do Parceiro**
   - Localização: Formulário de edição, seção **"Endereço"**.
   - Como fazer: Insira um **CEP** válido no campo correspondente.
   - Observações importantes: Ao inserir um CEP válido, o sistema automaticamente preencherá os demais campos de endereço, como cidade, estado e bairro.
   - Resultado esperado: O endereço do parceiro é preenchido automaticamente, facilitando o cadastro.

**Campos e Parâmetros:**

| Campo             | Tipo       | Obrigatório | Descrição                                             | Exemplo               |
|-------------------|------------|-------------|------------------------------------------------------|-----------------------|
| CNPJ ou CPF       | Texto      | Sim         | Número de identificação do parceiro                   | 12.345.678/0001-95    |
| Nome Fantasia     | Texto      | Sim         | Nome pelo qual o parceiro é conhecido                 | "Fornecedor XYZ"      |
| Razão Social      | Texto      | Sim         | Nome legal do parceiro                                | "Fornecedor XYZ Ltda." |
| E-mail            | Texto      | Não         | Endereço de e-mail para comunicação                   | contato@xyz.com.br    |
| Endereço          | Texto      | Não         | Endereço físico do parceiro                            | "Rua Exemplo, 123"    |
| CEP               | Texto      | Não         | Código de Endereçamento Postal                        | "12345-678"           |

**Regras de Negócio:**
- O cadastro de um parceiro só é efetivado se os campos **CNPJ ou CPF**, **Nome Fantasia** e **Razão Social** forem preenchidos.
- O e-mail do fornecedor é importante para processos automáticos e comunicação.
- O preenchimento do **CEP** deve ser válido para que o sistema complete automaticamente os demais campos de endereço.

**Observações Importantes:**
- É recomendável sempre verificar se o e-mail do parceiro está correto para evitar problemas de comunicação.
- Erros comuns incluem a inserção de CNPJ ou CPF inválidos, o que impede o cadastro.
- O sistema permite a importação de dados de planilhas, facilitando o cadastro em massa.

**Conceitos-Chave:**
- **Cadastro de Parceiros**: Processo de registrar informações sobre fornecedores e prestadores de serviço no sistema.
- **E-mail do Fornecedor**: Informação essencial para comunicação e processos automáticos.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como cadastrar um novo parceiro no sistema?
- Quais campos são obrigatórios para o cadastro de um fornecedor?
- Como editar as informações de um parceiro já cadastrado?

---


---


---

## 12. Cadastro de Parceiros

**📋 METADADOS:**
- **ID:** sec_12
- **⏱️ Minutagem:** 27:37 → 30:10
- **⏲️ Duração:** 152s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/qFzqzIoiVE4?si=YoVxiJOkipNVbQWb&t=1657)
- **📦 Módulo:** Cadastro de Parceiros
- **🏷️ Categorias:** Configuração, Cadastro, Operacional
- **🔑 Palavras-chave:** parceiro, contato, fornecedor, categorias de produto, dados bancários, relacionamento

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de cadastro de parceiros no sistema, incluindo a definição de contatos específicos, informações bancárias e categorias de produtos. O objetivo é garantir que os usuários possam registrar e gerenciar eficazmente as informações dos parceiros.

**Contexto:**
Estamos na interface de cadastro de parceiros do sistema, onde o usuário pode adicionar e gerenciar informações sobre fornecedores, prestadores de serviços, transportadoras e imobiliárias. Esta seção é crucial para organizar as relações comerciais e facilitar a comunicação e transações.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Cadastro de Parceiros > Submenu Cadastro
- Tela/interface específica: Tela de Cadastro de Parceiros

**Funcionalidade Detalhada:**
A funcionalidade de cadastro de parceiros permite que os usuários registrem informações detalhadas sobre cada parceiro comercial. Isso inclui a definição de contatos específicos, como vendedores, informações bancárias para transações e a categorização dos produtos ou serviços oferecidos. O sistema possibilita que, ao cadastrar um fornecedor, o usuário especifique as categorias de produtos que ele fornece, o que é essencial para a realização de cotações.

### 🔹 Passo a Passo Detalhado:

1. **Cadastro de Contato**
   - Localização: Tela de Cadastro de Parceiros, seção "Contato"
   - Como fazer: Clique na opção "Adicionar Contato" e insira o nome do vendedor, por exemplo, "João".
   - Campos/Opções disponíveis:
     * `Nome`: Campo de texto para inserir o nome do contato.
     * `E-mail`: Campo de texto para inserir o e-mail do contato.
   - Resultado esperado: O contato "João" é adicionado à lista de contatos do parceiro e será o responsável por receber e-mails de orçamento ou ordens de compra.

2. **Cadastro de Filiais**
   - Localização: Tela de Cadastro de Parceiros, seção "Filiais"
   - Como fazer: Preencha os campos com as informações da filial, como CNPJ, telefone, endereço e e-mail.
   - Campos/Opções disponíveis:
     * `CNPJ`: Campo de texto para inserir o CNPJ da filial.
     * `Telefone`: Campo de texto para inserir o telefone da filial.
     * `Endereço`: Campo de texto para inserir o endereço da filial.
     * `E-mail`: Campo de texto para inserir o e-mail da filial.
   - Resultado esperado: As informações da filial são salvas e associadas ao parceiro.

3. **Cadastro de Dados Bancários**
   - Localização: Tela de Cadastro de Parceiros, seção "Dados Bancários"
   - Como fazer: Clique em "Adicionar Dados Bancários" e preencha os campos com as informações necessárias.
   - Campos/Opções disponíveis:
     * `Banco`: Dropdown para selecionar o banco.
     * `Agência`: Campo de texto para inserir o número da agência.
     * `Conta`: Campo de texto para inserir o número da conta.
     * `Chave Pix`: Campo de texto para inserir a chave Pix.
   - Resultado esperado: As informações bancárias são registradas, permitindo que pagamentos via Pix ou depósito sejam processados corretamente.

4. **Definição de Relacionamento**
   - Localização: Tela de Cadastro de Parceiros, seção "Relacionamento"
   - Como fazer: Clique em "Selecionar" para definir o tipo de relacionamento do parceiro.
   - Observações importantes: O tipo de relacionamento pode ser "Fornecedor", "Prestador de Serviço", "Transportadora" ou "Imobiliária". A escolha do tipo influencia as opções de categorias de produtos disponíveis.
   - Resultado esperado: O tipo de relacionamento é definido, e se "Fornecedor" for selecionado, o sistema abrirá a seção de categorias de produtos.

5. **Cadastro de Categorias de Produto**
   - Localização: Tela de Cadastro de Parceiros, seção "Categorias de Produto" (apenas se "Fornecedor" for selecionado)
   - Como fazer: Selecione as categorias de produtos que o parceiro fornece, como "Hidráulica" e "Elétrica".
   - Campos/Opções disponíveis:
     * `Categorias`: Checkbox para selecionar as categorias relevantes.
   - Resultado esperado: As categorias de produtos são associadas ao parceiro, permitindo que o sistema filtre fornecedores durante o processo de cotação.

**Campos e Parâmetros:**

| Campo               | Tipo      | Obrigatório | Descrição                                               | Exemplo                |
|---------------------|-----------|-------------|---------------------------------------------------------|------------------------|
| Nome                | Texto     | Sim         | Nome do contato do parceiro.                            | João                   |
| E-mail              | Texto     | Não         | E-mail do contato do parceiro.                          | joao@exemplo.com       |
| CNPJ                | Texto     | Sim         | CNPJ da filial do parceiro.                             | 12.345.678/0001-90     |
| Telefone            | Texto     | Não         | Telefone da filial do parceiro.                         | (11) 91234-5678        |
| Endereço            | Texto     | Não         | Endereço da filial do parceiro.                         | Rua Exemplo, 123       |
| Chave Pix           | Texto     | Não         | Chave Pix para transações.                             | joao@exemplo.com       |
| Tipo de Relacionamento | Dropdown | Sim         | Tipo de relacionamento do parceiro.                     | Fornecedor             |
| Categorias          | Checkbox   | Não         | Categorias de produtos fornecidos pelo parceiro.       | Hidráulica, Elétrica   |

**Regras de Negócio:**
- O campo `Nome` é obrigatório para o cadastro de contatos.
- O tipo de relacionamento deve ser definido antes de associar categorias de produtos.
- Se o tipo de relacionamento for "Fornecedor", as categorias de produtos devem ser selecionadas para que o sistema funcione corretamente durante as cotações.

**Observações Importantes:**
- É recomendável cadastrar sempre um contato responsável para facilitar a comunicação.
- Verifique se o CNPJ está correto para evitar problemas com a documentação fiscal.
- As informações bancárias devem ser inseridas com atenção, pois são essenciais para pagamentos.

**Conceitos-Chave:**
- **Fornecedor**: Entidade que fornece produtos ou serviços, essencial para o processo de cotação.
- **Chave Pix**: Identificador único utilizado para realizar transações financeiras via Pix.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso cadastrar um novo parceiro no sistema?
- Quais informações são necessárias para cadastrar um fornecedor?
- Como definir o contato responsável para um parceiro cadastrado?

---


---


---

## 13. Cadastro e Gerenciamento de Serviços

**📋 METADADOS:**
- **ID:** sec_13
- **⏱️ Minutagem:** 30:08 → 32:42
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/qFzqzIoiVE4?si=YoVxiJOkipNVbQWb&t=1808)
- **📦 Módulo:** Serviços
- **🏷️ Categorias:** Cadastro, Operacional, Relatório
- **🔑 Palavras-chave:** cadastro de serviço, categoria, unidade de medida, clima, descrição, grupo de parceiros

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de cadastro de serviços no sistema, incluindo a definição de categorias e unidades de medida, e como essas informações são utilizadas para relatórios e filtragens.

**Contexto:**
Estamos na aba de serviços do sistema, onde o objetivo é cadastrar novos serviços que serão utilizados em ordens de serviço. O cadastro correto é essencial para a organização e filtragem de informações relacionadas a serviços prestados.

**Localização no Sistema:**
- Caminho de navegação: Menu Principal > Módulo Serviços > Aba de Cadastro de Serviços
- Tela/interface específica: Tela de Cadastro de Serviços

**Funcionalidade Detalhada:**

A funcionalidade de cadastro de serviços permite que o usuário registre novos serviços que serão utilizados em ordens de serviço. É necessário que o serviço esteja cadastrado antes de ser utilizado. O sistema permite o cadastro através da aba de serviços, bem como por meio de importação de planilhas ou pelo módulo de engenharia. O cadastro inclui a definição de nome, unidade de medida e categoria do serviço.

### 🔹 Passo a Passo Detalhado:

1. **Cadastrar Novo Serviço**
   - Localização: Aba de Cadastro de Serviços, botão **Mais Serviço**.
   - Como fazer: Clique no botão **Mais Serviço** para iniciar o cadastro de um novo serviço.
   - Campos/Opções disponíveis:
     * `Nome do Serviço`: Campo de texto onde você deve inserir o nome do serviço a ser cadastrado.
     * `Unidade de Medida`: Campo de seleção onde você deve escolher a unidade de medida pela qual o serviço será controlado (ex: horas, metros, etc.).
     * `Categoria`: Campo de seleção onde você deve escolher a categoria do serviço. As categorias são agrupamentos que facilitam a localização de serviços e produtos durante processos de compras e financeiros.
   - Resultado esperado: O serviço será cadastrado e estará disponível para uso em outras áreas do sistema.

2. **Definir Categoria do Serviço**
   - Localização: Durante o cadastro do serviço, no campo **Categoria**.
   - Como fazer: Selecione a categoria apropriada para o serviço. Por exemplo, você pode vincular o serviço à categoria de **Pintura e Revestimento**.
   - Observações importantes: A definição das categorias é crucial para a organização e filtragem de serviços. As categorias ajudam a agrupar serviços com o mesmo intuito.
   - Resultado esperado: O serviço será vinculado à categoria selecionada, facilitando sua localização futura.

3. **Adicionar Descrição e Orientações**
   - Localização: Campo de descrição no formulário de cadastro de serviço.
   - Como fazer: Insira uma descrição ou orientações adicionais sobre o serviço, se necessário. Também é possível identificar se o clima pode atrapalhar a execução do serviço.
   - Resultado esperado: A descrição e as orientações serão salvas junto com o serviço cadastrado, proporcionando informações adicionais para usuários futuros.

4. **Salvar o Cadastro do Serviço**
   - Localização: Botão **Salvar** na parte inferior do formulário de cadastro.
   - Como fazer: Após preencher todos os campos necessários, clique no botão **Salvar** para concluir o cadastro do serviço.
   - Resultado esperado: O serviço será salvo no sistema e estará disponível para uso em ordens de serviço e relatórios.

**Campos e Parâmetros:**

| Campo                | Tipo          | Obrigatório | Descrição                                                                 | Exemplo                  |
|----------------------|---------------|-------------|---------------------------------------------------------------------------|--------------------------|
| Nome do Serviço      | Texto         | Sim         | Nome que identifica o serviço cadastrado.                                | Pintura de Parede        |
| Unidade de Medida    | Seleção       | Sim         | Unidade pela qual o serviço será controlado.                             | Horas, Metros            |
| Categoria            | Seleção       | Sim         | Agrupamento do serviço para facilitar a localização.                     | Pintura e Revestimento   |
| Descrição            | Texto         | Não         | Informações adicionais sobre o serviço, incluindo orientações.          | Serviço a ser realizado em clima seco. |

**Regras de Negócio:**
- O serviço deve estar cadastrado antes de ser utilizado em ordens de serviço.
- As categorias devem ser definidas para facilitar a filtragem e localização de serviços.
- O clima pode ser registrado como um fator que influencia a execução do serviço.

**Observações Importantes:**
- É recomendável revisar as categorias pré-definidas antes de criar novas.
- Erros comuns incluem não selecionar a unidade de medida ou a categoria, o que pode resultar em dificuldades na localização do serviço posteriormente.
- O cadastro de serviços pode ser realizado também através da importação de planilhas, facilitando a inclusão em massa.

**Conceitos-Chave:**
- **Unidade de Medida**: Refere-se à forma como o serviço será quantificado (ex: horas, metros).
- **Categoria**: Agrupamento de serviços com o mesmo intuito, utilizado para facilitar a busca e relatórios.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como cadastrar um novo serviço no sistema?
- Quais informações são necessárias para o cadastro de um serviço?
- Como as categorias influenciam o cadastro e a busca de serviços?

---


---


---

## 14. Cadastro e Vínculo de Lojas no Sistema Casas d'Água

**📋 METADADOS:**
- **ID:** sec_14
- **⏱️ Minutagem:** 32:39 → 34:28
- **⏲️ Duração:** 109s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/qFzqzIoiVE4?si=YoVxiJOkipNVbQWb&t=1959)
- **📦 Módulo:** Módulo de Compras
- **🏷️ Categorias:** Cadastro, Configuração, Operacional
- **🔑 Palavras-chave:** lojas, CNPJ, grupo de parceiros, crédito, ordem de compra

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como cadastrar diferentes lojas que fazem parte da rede Casas d'Água e como vincular essas lojas em grupos de parceiros, permitindo a gestão eficiente de compras e créditos financeiros entre elas.

**Contexto:**
Estamos no Módulo de Compras do sistema Casas d'Água, onde é necessário gerenciar múltiplas lojas que operam sob diferentes CNPJs, mas que pertencem ao mesmo grupo. O objetivo é garantir que as ordens de compra e os créditos financeiros sejam corretamente atribuídos e gerenciados entre as lojas.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo de Compras > Grupo de Parceiros
- Tela/interface específica: Tela de Cadastro de Grupo de Parceiros

**Funcionalidade Detalhada:**
A funcionalidade permite o cadastro de cada loja como um parceiro distinto no sistema, considerando que cada loja possui um CNPJ diferente. Isso é crucial para a correta formalização de ordens de compra e a gestão de créditos financeiros. Através do vínculo entre as lojas, é possível evitar divergências nas transações e garantir que os créditos sejam compartilhados entre as lojas do grupo.

### 🔹 Passo a Passo Detalhado:

1. **Cadastro de Lojas como Parceiros**
   - Localização: Menu Principal > Módulo de Compras > Cadastro de Lojas
   - Como fazer: Acesse a tela de cadastro de lojas e insira os dados de cada loja individualmente.
   - Campos/Opções disponíveis:
     * `Nome da Loja`: Campo de texto onde você insere o nome da loja (ex: "Loja Biguaçu").
     * `CNPJ`: Campo de texto onde você insere o CNPJ da loja (ex: "12.345.678/0001-90").
   - Resultado esperado: Cada loja é cadastrada como um parceiro distinto no sistema.

2. **Criação de um Novo Grupo de Parceiros**
   - Localização: Menu Principal > Módulo de Compras > Grupo de Parceiros
   - Como fazer: Clique no botão **"Mais Novo Grupo"** para iniciar o cadastro de um novo grupo.
   - Campos/Opções disponíveis:
     * `Nome do Grupo`: Campo de texto onde você define o nome do grupo (ex: "Grupo Casas d'Água").
   - Resultado esperado: Um novo grupo de parceiros é criado no sistema.

3. **Vinculação de Lojas ao Grupo de Parceiros**
   - Localização: Tela de Cadastro de Grupo de Parceiros
   - Como fazer: Após criar o grupo, clique na **mãozinha** (ícone de seleção) ao lado de cada loja que deseja incluir no grupo e, em seguida, clique no botão **"Salvar"**.
   - Observações importantes: Certifique-se de que todas as lojas que você deseja vincular estão selecionadas antes de salvar.
   - Resultado esperado: As lojas selecionadas são vinculadas ao grupo de parceiros, permitindo a gestão conjunta de ordens de compra e créditos.

**Campos e Parâmetros:**

| Campo               | Tipo        | Obrigatório | Descrição                                           | Exemplo                     |
|---------------------|-------------|-------------|-----------------------------------------------------|-----------------------------|
| Nome da Loja        | Texto       | Sim         | Nome da loja a ser cadastrada                       | Loja Biguaçu                |
| CNPJ                | Texto       | Sim         | Cadastro Nacional da Pessoa Jurídica da loja       | 12.345.678/0001-90         |
| Nome do Grupo       | Texto       | Sim         | Nome do grupo de parceiros a ser criado             | Grupo Casas d'Água         |

**Regras de Negócio:**
- Cada loja deve ser cadastrada com um CNPJ único.
- As ordens de compra não podem ser formalizadas com uma loja e a nota lançada em outra, a menos que as lojas pertençam ao mesmo grupo de parceiros.
- Os créditos financeiros criados para uma loja influenciam nas demais lojas do grupo.

**Observações Importantes:**
- É importante cadastrar cada loja como um parceiro diferente para evitar divergências nas transações.
- Erros comuns incluem não selecionar todas as lojas desejadas ao criar um grupo de parceiros.
- As lojas devem ser cadastradas antes de serem vinculadas a um grupo.

**Conceitos-Chave:**
- **CNPJ**: Cadastro Nacional da Pessoa Jurídica, número que identifica uma empresa no Brasil.
- **Grupo de Parceiros**: Conjunto de lojas que podem compartilhar informações financeiras e operacionais dentro do sistema.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como cadastrar uma nova loja no sistema?
- O que fazer se uma ordem de compra precisa ser vinculada a uma loja diferente da que foi cadastrada?
- Como criar e vincular um grupo de parceiros no sistema?

---


---

