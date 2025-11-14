# 📚 Documentação: Passo a passo - Módulo de Compras

**🎥 Vídeo Original:** https://youtu.be/qFzqzIoiVE4?si=YoVxiJOkipNVbQWb

**📊 Total de Seções:** 14

**ℹ️ Nota:** Cada seção abaixo contém um link direto para o trecho específico do vídeo tutorial.

---

---

## 1. Fluxo de Compras no Módulo de Compras

**📋 METADADOS:**
- **ID:** sec_1
- **⏱️ Minutagem:** 00:00 → 02:33
- **⏲️ Duração:** 152s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/qFzqzIoiVE4?si=YoVxiJOkipNVbQWb&t=0)
- **📦 Módulo:** Compras
- **🏷️ Categorias:** Operacional, Cadastro, Relatório
- **🔑 Palavras-chave:** fluxo de compras, solicitação, suprimentos, orçamento, ordem de compra

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o fluxo de compras, desde a solicitação até a chegada do produto no estoque, abordando as diferentes formas de iniciar o processo e como realizar uma solicitação de compra.

**Contexto:**
Estamos no módulo de compras do sistema, onde o objetivo é entender o fluxo de compras, que abrange desde a solicitação de produtos até a sua formalização e recebimento no estoque.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Compras > Suprimentos > Solicitações
- Tela/interface específica: Aba de Solicitações

**Funcionalidade Detalhada:**
O fluxo de compras permite que os usuários solicitem produtos, citem fornecedores e formalizem ordens de compra. Existem três formas principais de iniciar o fluxo:
1. **Solicitação em Suprimentos:** Usada quando mais de um usuário está envolvido.
2. **Compras Direto em Orçamentos:** Para um único usuário que já sabe o que precisa.
3. **Ordem de Compra Direta:** Para compras retroativas ou de última hora.

### 🔹 Passo a Passo Detalhado:

1. **Acessar a Aba de Solicitações**
   - Localização: Menu Principal > Módulo Compras > Suprimentos > Solicitações
   - Como fazer: Clique na aba "Solicitações".
   - Resultado esperado: A tela de solicitações é exibida, permitindo a visualização de todas as solicitações anteriores.

2. **Criar Nova Solicitação**
   - Localização: Dentro da aba de solicitações, clique no botão **"Mais Solicitação"**.
   - Como fazer: Clique no botão para iniciar uma nova solicitação.
   - Campos/Opções disponíveis:
     * `Produto`: Seleção de produtos já cadastrados.
   - Resultado esperado: A tela de seleção de produtos é exibida.

3. **Selecionar Produto**
   - Localização: Tela de seleção de produtos.
   - Como fazer: Utilize filtros por categoria, subcategoria ou pesquisa direta para localizar o produto desejado.
   - Observações importantes: Caso não encontre o produto, clique em **"Mais Produto"** para adicionar um novo item.
   - Resultado esperado: O produto desejado é selecionado.

4. **Definir Especificações do Produto**
   - Localização: Tela de especificações do produto selecionado.
   - Como fazer: Após selecionar o produto, escolha o tipo específico (ex: cimento Portland CP1 de 50 kg).
   - Campos/Opções disponíveis:
     * `Tipo de Produto`: Seleção de diferentes tipos de cimento.
   - Resultado esperado: O tipo de produto é definido e pronto para adição à solicitação.

5. **Adicionar Quantidade**
   - Localização: Abaixo da seleção do tipo de produto.
   - Como fazer: Insira a quantidade desejada no campo correspondente e clique em **"Adicionar"**.
   - Resultado esperado: O produto e a quantidade são adicionados à solicitação.

6. **Selecionar Vários Produtos**
   - Localização: Tela de especificações.
   - Como fazer: Repita o processo de seleção e adição para outros produtos conforme necessário.
   - Resultado esperado: Múltiplos produtos são adicionados à solicitação.

**Campos e Parâmetros:**

| Campo               | Tipo          | Obrigatório | Descrição                                      | Exemplo                     |
|---------------------|---------------|-------------|------------------------------------------------|-----------------------------|
| Produto             | Dropdown      | Sim         | Seleção de produtos cadastrados                 | Cimento Portland CP1 de 50 kg |
| Tipo de Produto     | Dropdown      | Sim         | Seleção do tipo específico do produto          | Cimento Portland            |
| Quantidade          | Numérico      | Sim         | Quantidade do produto a ser solicitado         | 10                          |

**Regras de Negócio:**
- A solicitação deve ser feita para produtos já cadastrados no sistema.
- É permitido adicionar múltiplos produtos em uma única solicitação.
- A quantidade deve ser um número positivo.

**Observações Importantes:**
- Utilize filtros para facilitar a busca de produtos.
- Verifique se o produto desejado está cadastrado antes de tentar adicionar um novo.
- Evite adicionar produtos em quantidades negativas.

**Conceitos-Chave:**
- **Fluxo de Compras**: Processo que abrange desde a solicitação até a formalização da compra e recebimento do produto.
- **Solicitação em Suprimentos**: Ação de pedir produtos, geralmente envolvendo múltiplos usuários.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                | Solução                                           | Prevenção                                       |
|-----------------------------------|-------------------------------|--------------------------------------------------|-------------------------------------------------|
| Produto não encontrado             | Produto não cadastrado        | Clique em **"Mais Produto"** e cadastre-o.      | Verifique o cadastro de produtos antes da solicitação. |
| Quantidade negativa informada     | Erro de digitação             | Insira um número positivo no campo de quantidade. | Sempre revise os valores antes de adicionar.   |

**💡 DICAS E BOAS PRÁTICAS:**
- Utilize a pesquisa direta para localizar produtos rapidamente.
- Sempre verifique as especificações do produto antes de adicionar.
- Mantenha um registro dos produtos frequentemente solicitados para facilitar futuras solicitações.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Solicitação de Cimento**
```
Situação: Um engenheiro precisa solicitar cimento para uma obra.
Ação: 
  • Acessar a aba de solicitações.
  • Clicar em "Mais Solicitação".
  • Filtrar por categoria "Materiais de Construção".
  • Selecionar "Cimento Portland CP1 de 50 kg".
  • Inserir a quantidade: 20.
Resultado: A solicitação de 20 sacos de cimento é criada com sucesso.
```

**Exemplo 2: Solicitação de Vários Produtos**
```
Situação: Um comprador precisa solicitar materiais diversos.
Ação: 
  • Acessar a aba de solicitações.
  • Clicar em "Mais Solicitação".
  • Filtrar por categoria "Materiais de Construção".
  • Selecionar "Cimento Portland CP1 de 50 kg" e adicionar 10.
  • Selecionar "Areia Média" e adicionar 5.
Resultado: A solicitação é criada com 10 sacos de cimento e 5 de areia.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O produto deve estar cadastrado no sistema.
- **Habilita:** A criação de ordens de compra após a solicitação.
- **Relacionado a:** Módulo de Estoque, onde os produtos solicitados serão recebidos.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como iniciar o fluxo de compras?"
- **Com problema:** "Não consigo solicitar um produto, o que fazer?"
- **Informal:** "Como eu peço um produto?"
- **Por sintoma:** "Quando não encontro um produto, o que fazer?"
- **Com dúvida:** "Qual a diferença entre solicitar e comprar direto?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Fazer uma solicitação", "pedir um produto", "comprar um item", "cadastrar um pedido".
- "Ordem de compra", "cotação", "suprimento".

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como faço para solicitar um produto?
- O que fazer se não encontrar o produto desejado?
- Como adicionar múltiplos produtos em uma solicitação?
- O que fazer se a quantidade informada estiver errada?
- O que preciso ter cadastrado antes de solicitar um produto?

---


---


---

## 2. Especificação de Serviços e Vínculo com Obras

**📋 METADADOS:**
- **ID:** sec_2
- **⏱️ Minutagem:** 02:30 → 05:04
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/qFzqzIoiVE4?si=YoVxiJOkipNVbQWb&t=150)
- **📦 Módulo:** Compras e Serviços
- **🏷️ Categorias:** Configuração, Operacional, Compras
- **🔑 Palavras-chave:** especificação de serviços, vínculo com obra, fluxo de caixa, data limite de entrega, comentários

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de especificação de serviços em obras, incluindo a criação de vínculos entre produtos e serviços, a definição de datas de entrega e a adição de comentários para aprovação. O objetivo é garantir que os produtos sejam corretamente alocados aos serviços necessários, facilitando o acompanhamento financeiro e operacional.

**Contexto:**
Estamos na interface do módulo de Compras e Serviços, onde o usuário pode especificar serviços relacionados a obras. Esta funcionalidade é crucial para gerenciar o fluxo de compras e garantir que os insumos sejam alocados corretamente.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Compras e Serviços > Especificação de Serviços
- Tela/interface específica: Tela de Especificação de Serviços

**Funcionalidade Detalhada:**
A funcionalidade de especificação de serviços permite ao usuário vincular produtos a serviços específicos dentro de uma obra. Isso é especialmente importante quando o acompanhamento da engenharia da obra não está completo, pois o usuário terá acesso apenas ao contas a pagar e ao fluxo de caixa, sem comparativos. Quando a engenharia está completa, o sistema solicita a especificação do serviço, permitindo a criação de apropriações e a visualização de comparativos entre a quantidade planejada e a quantidade já solicitada.

### 🔹 Passo a Passo Detalhado:

1. **Arrastar e Definir Especificações**
   - Localização: Área lateral da tela de Especificação de Serviços
   - Como fazer: Arraste o item desejado para o lado e defina as especificações necessárias.
   - Resultado esperado: As especificações do serviço são definidas e salvas no sistema.

2. **Selecionar Local de Consumo**
   - Localização: Lateral da tela de Especificação de Serviços
   - Como fazer: Escolha o local de consumo para o serviço que está sendo especificado.
   - Observações importantes: Para obras com engenharia incompleta, apenas o vínculo com a obra será criado, sem comparativos.
   - Resultado esperado: O local de consumo é registrado, permitindo o acompanhamento financeiro.

3. **Especificar Serviços**
   - Localização: Botão "Especificar Serviços"
   - Como fazer: Clique no botão para abrir a interface de especificação de serviços.
   - Campos/Opções disponíveis:
     * `Serviços com Recurso Alocado`: Lista de serviços que já possuem insumos programados.
     * `Serviços sem Recurso Alocado`: Lista de serviços que não têm insumos vinculados.
   - Resultado esperado: O usuário pode escolher para qual serviço o produto será utilizado.

4. **Salvar Especificações**
   - Localização: Botão "Salvar" na parte inferior da tela
   - Como fazer: Após preencher todas as informações, clique no botão "Salvar".
   - Resultado esperado: As especificações e vínculos são salvos no sistema.

5. **Definir Data Limite de Entrega**
   - Localização: Campo "Data Limite de Entrega"
   - Como fazer: Verifique a data preenchida automaticamente ou insira uma nova data.
   - Observações importantes: Se a data limite for inferior à data de solicitação, a solicitação será marcada como urgente.
   - Resultado esperado: A data limite de entrega é registrada e, se necessário, a solicitação é marcada como urgente.

6. **Adicionar Comentários**
   - Localização: Campo de comentários abaixo da data limite
   - Como fazer: Clique no campo de comentários e insira a mensagem desejada.
   - Resultado esperado: O comentário é salvo e pode ser exibido ao fornecedor no momento do orçamento.

**Campos e Parâmetros:**

| Campo                       | Tipo      | Obrigatório | Descrição                                                                 | Exemplo                |
|-----------------------------|-----------|-------------|---------------------------------------------------------------------------|------------------------|
| `Local de Consumo`          | Dropdown  | Sim         | Seleção do local onde o serviço será consumido.                          | "Obra A"               |
| `Serviços com Recurso Alocado` | Lista    | Sim         | Lista de serviços que já têm insumos alocados.                          | "Serviço 1"            |
| `Serviços sem Recurso Alocado` | Lista    | Não         | Lista de serviços que não têm insumos vinculados.                       | "Serviço 2"            |
| `Data Limite de Entrega`    | Data      | Sim         | Data limite para a entrega do produto.                                   | "2023-10-30"           |
| `Comentários`               | Texto     | Não         | Campo para adicionar comentários sobre a solicitação.                    | "Urgente, por favor!"  |

**Regras de Negócio:**
- Se a data limite de entrega for inferior à data atual, a solicitação será marcada como urgente.
- Os serviços devem ser vinculados a produtos que já tenham insumos alocados para garantir a correta apropriação.

**Observações Importantes:**
- É recomendável revisar as datas de entrega antes de salvar as especificações.
- Evite selecionar serviços sem recurso alocado se houver insumos disponíveis.

**Conceitos-Chave:**
- **Vínculo com Obra**: Relação entre produtos e serviços dentro de uma obra, essencial para o controle financeiro.
- **Data Limite de Entrega**: Data que determina a urgência da solicitação de um produto.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                     | Solução                                         | Prevenção                                      |
|-----------------------------------|------------------------------------|------------------------------------------------|------------------------------------------------|
| Solicitação não salva             | Campos obrigatórios não preenchidos| Verifique e preencha todos os campos obrigatórios| Sempre revisar os campos antes de salvar       |
| Data limite não aceita            | Data inválida ou no passado        | Insira uma data válida e futura                | Use um calendário para verificar datas         |
| Comentário não aparece para fornecedor | Campo não marcado para exibição | Marque a opção de exibir comentário ao fornecedor | Sempre revisar as opções de exibição           |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre especifique serviços com insumos alocados para evitar problemas de apropriação.
- Utilize comentários para esclarecer solicitações urgentes.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Especificação de Serviço com Insumo Alocado**
```
Situação: O engenheiro precisa solicitar cimento para a obra.
Ação: 
  • Campo Local de Consumo: "Obra A"
  • Selecionar Serviço: "Cimento - Serviço 1"
  • Data Limite de Entrega: "2023-10-25"
Resultado: O produto é vinculado ao serviço e a solicitação é salva com data limite.

```

**Exemplo 2: Solicitação Urgente**
```
Situação: Um serviço precisa de entrega imediata.
Ação: 
  • Campo Local de Consumo: "Obra B"
  • Selecionar Serviço: "Areia - Serviço 2"
  • Data Limite de Entrega: "2023-10-20" (data inferior ao limite)
Resultado: A solicitação é marcada como urgente e salva no sistema.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** A obra deve ter a engenharia completa para realizar comparativos.
- **Habilita:** O acompanhamento financeiro e a gestão de fluxo de caixa.
- **Relacionado a:** Módulo de Engenharia e Módulo de Compras.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como especificar serviços em uma obra?"
- **Com problema:** "Não consigo salvar a especificação de serviços, o que fazer?"
- **Informal:** "Como faço pra colocar um serviço na obra?"
- **Por sintoma:** "Quando a data de entrega é urgente, como isso afeta a solicitação?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Definir serviço", "vincular produto", "especificar insumo", "associar serviço"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como especificar um serviço para uma obra?
- O que fazer se a data limite de entrega não for aceita?
- Como adicionar comentários na solicitação de serviços?
- O que acontece se a data de entrega for urgente?
- Quais são os pré-requisitos para especificar serviços?

---


---


---

## 3. Salvar Solicitação e Aprovação no Módulo de Compras

**📋 METADADOS:**
- **ID:** sec_3
- **⏱️ Minutagem:** 05:01 → 07:34
- **⏲️ Duração:** 152s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/qFzqzIoiVE4?si=YoVxiJOkipNVbQWb&t=301)
- **📦 Módulo:** Compras
- **🏷️ Categorias:** Solicitação, Aprovação, Fluxo de Trabalho, Gestão de Compras
- **🔑 Palavras-chave:** salvar, rascunho, aprovar, solicitar, compras, histórico, editar

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de salvar uma solicitação no sistema de compras, incluindo opções de rascunho e aprovação, além de como acompanhar o status da solicitação.

**Contexto:**
Estamos no módulo de compras, onde o usuário pode salvar solicitações de compra e gerenciar seu fluxo de aprovação. O objetivo é garantir que as solicitações sejam corretamente salvas e que o solicitante possa acompanhar o status de suas requisições.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Compras > Solicitações
- Tela/interface específica: Tela de Solicitação de Compras

**Funcionalidade Detalhada:**
A funcionalidade permite que o usuário salve uma solicitação de compra. O usuário pode optar por salvar a solicitação como um rascunho, permitindo que ele feche a tela e retorne posteriormente para completar ou editar a solicitação. Uma vez que a solicitação é salva completamente, ela é enviada para o módulo de compras para aprovação. É importante notar que a solicitação só pode ser editada ou excluída enquanto estiver com o status "aberto". Após essa etapa, apenas o módulo de compras pode realizar alterações.

### 🔹 Passo a Passo Detalhado:

1. **Salvar Solicitação**
   - Localização: Botão **Salvar** na parte inferior da tela de solicitação.
   - Como fazer: Clique no botão **Salvar**. Uma janela de opções aparecerá.
   - Campos/Opções disponíveis:
     * **Salvar como Rascunho**: Permite que a solicitação seja salva para edição futura.
     * **Salvar Completo**: Envia a solicitação para o módulo de compras.
   - Resultado esperado: A solicitação é salva como rascunho ou enviada para o módulo de compras, dependendo da opção escolhida.

2. **Acompanhar Solicitação**
   - Localização: Tela inicial do módulo de compras, seção de **Histórico de Solicitações**.
   - Como fazer: Acesse a tela inicial do módulo de compras para visualizar todas as solicitações pendentes.
   - Observações importantes: O solicitante pode acompanhar o status da solicitação e visualizar o histórico de ações realizadas.
   - Resultado esperado: O usuário vê uma lista de solicitações, incluindo a que acabou de realizar, com informações sobre seu status.

3. **Aprovar Solicitações**
   - Localização: Tela de **Aprovação de Solicitações** no módulo de compras.
   - Como fazer: Clique na solicitação pendente que deseja aprovar.
   - Campos/Opções disponíveis:
     * **Aprovar**: Botão com ícone de polegar para cima.
     * **Reprovar**: Botão com ícone de polegar para baixo.
     * **Trocar Produto**: Ícone de bolinha com dois risquinhos para substituir por um produto semelhante.
   - Resultado esperado: A solicitação é aprovada ou reprovada, e o fluxo de compras é atualizado.

4. **Inserir Comentário**
   - Localização: Campo de comentários na tela de aprovação.
   - Como fazer: Clique no campo de comentários e digite sua mensagem. Para visualizar comentários existentes, clique no ícone correspondente.
   - Observações importantes: Comentários são destacados em verde quando há novas mensagens.
   - Resultado esperado: O comentário é adicionado ou visualizado, permitindo comunicação entre solicitante e aprovador.

5. **Métodos de Aprovação**
   - Localização: Tela de aprovação de solicitações.
   - Como fazer: Escolha entre **Aprovação Individual** ou **Aprovação Rápida**.
   - Observações importantes:
     * **Aprovação Individual**: Aprova item a item, permitindo transferências de produtos.
     * **Aprovação Rápida**: Aprova todas as solicitações de uma vez, sem opções de transferência.
   - Resultado esperado: A solicitação é aprovada conforme o método escolhido.

**Campos e Parâmetros:**

| Campo                  | Tipo        | Obrigatório | Descrição                                             | Exemplo                  |
|------------------------|-------------|-------------|-----------------------------------------------------|--------------------------|
| **Salvar como Rascunho** | Botão      | Sim         | Salva a solicitação para edição futura.             | -                        |
| **Salvar Completo**    | Botão      | Sim         | Envia a solicitação para o módulo de compras.       | -                        |
| **Comentários**        | Texto       | Não         | Permite adicionar observações sobre a solicitação.   | "Urgente: precisa de revisão" |
| **Aprovar/Reprovar**   | Botão       | Sim         | Aprova ou reprova a solicitação.                     | -                        |
| **Trocar Produto**     | Ícone       | Não         | Permite substituir o produto solicitado por outro.   | -                        |

**Regras de Negócio:**
- A solicitação pode ser editada ou excluída apenas enquanto estiver com o status "aberto".
- O histórico de ações é atualizado conforme o fluxo de compras avança.
- O aprovador pode optar por aprovar individualmente ou rapidamente, dependendo da necessidade.

**Observações Importantes:**
- É recomendável salvar a solicitação como rascunho se não estiver pronta para envio imediato.
- Evite deixar solicitações pendentes por muito tempo para não atrasar o processo de compras.
- Verifique se todos os campos obrigatórios estão preenchidos antes de salvar.

**Conceitos-Chave:**
- **Rascunho**: Estado de uma solicitação que ainda pode ser editada.
- **Aprovação**: Processo de validação de uma solicitação de compra por um responsável.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                       | Causa Provável                  | Solução                                           | Prevenção                                   |
|--------------------------------|---------------------------------|--------------------------------------------------|---------------------------------------------|
| Solicitação não salva          | Campos obrigatórios não preenchidos | Preencha todos os campos obrigatórios e tente novamente. | Verifique os campos antes de salvar.       |
| Não consegue aprovar           | Falta de permissões             | Consulte o administrador para verificar suas permissões. | Solicite as permissões necessárias previamente. |
| Comentário não aparece         | Não foi salvo corretamente      | Verifique se o botão de salvar foi clicado.     | Sempre clique em salvar após adicionar comentários. |

**💡 DICAS E BOAS PRÁTICAS:**
- Utilize a opção de rascunho para evitar perdas de informações.
- Mantenha um registro de solicitações urgentes para priorização.
- Revise os comentários antes de enviar para garantir clareza.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Solicitação de Compra Urgente**
```
Situação: Um funcionário precisa de cimento para uma obra.
Ação: O funcionário salva a solicitação como rascunho para adicionar mais detalhes depois.
  • Campo de produto: "Cimento"
  • Campo de urgência: "Sim"
Resultado: A solicitação é salva e pode ser editada posteriormente.
```

**Exemplo 2: Aprovação de Solicitação**
```
Situação: Um gerente precisa aprovar uma solicitação de compra.
Ação: O gerente acessa a tela de aprovação e clica no botão de aprovar.
Resultado: A solicitação é aprovada e o status é atualizado para "Aprovado".
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O usuário deve ter permissões adequadas para salvar e aprovar solicitações.
- **Habilita:** A aprovação de solicitações permite que o fluxo de compras continue.
- **Relacionado a:** Funcionalidades de gestão de estoque e relatórios de compras.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como salvar uma solicitação de compra?"
- **Com problema:** "Não consigo salvar minha solicitação, o que fazer?"
- **Informal:** "Como faço para guardar meu pedido?"
- **Por sintoma:** "Quando minha solicitação não aparece, o que está errado?"
- **Alternativa:** "Como aprovar uma solicitação de compra?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Salvar pedido", "guardar solicitação", "aprovar compra", "editar solicitação"
- "Rascunho", "aprovação", "fluxo de compras", "status da solicitação"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso salvar uma solicitação de compra?
- O que fazer se minha solicitação não for salva?
- Como aprovar uma solicitação no módulo de compras?
- O que fazer se não consigo aprovar uma solicitação?
- Quais são os requisitos para salvar uma solicitação?

---


---


---

## 4. Aprovação e Finalização de Cotações

**📋 METADADOS:**
- **ID:** sec_4
- **⏱️ Minutagem:** 07:31 → 10:04
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/qFzqzIoiVE4?si=YoVxiJOkipNVbQWb&t=451)
- **📦 Módulo:** Gestão de Compras
- **🏷️ Categorias:** Aprovação, Cotações, Fornecedores, Compras
- **🔑 Palavras-chave:** Aprovação, Cotação, Fornecedor, Orçamento, Compra Vulsa

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de aprovação de produtos e finalização de cotações no sistema, permitindo que o usuário compreenda como gerenciar eficientemente a aprovação de itens e a escolha entre orçamento e compra direta.

**Contexto:**
Estamos na interface de gestão de compras, onde o usuário pode aprovar produtos e definir o próximo passo no processo de aquisição, seja gerando um orçamento ou uma compra direta.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Gestão de Compras > Aprovação de Produtos
- Tela/interface específica: Tela de Aprovação de Produtos

**Funcionalidade Detalhada:**
A funcionalidade de aprovação permite que o usuário aprove produtos em uma única ação, especialmente útil quando há múltiplos itens. Após a aprovação, o usuário pode identificar o local de entrega e finalizar o processo, escolhendo entre gerar um orçamento ou uma compra direta. A escolha de orçamento é comum quando o usuário deseja comparar preços de diferentes fornecedores.

### 🔹 Passo a Passo Detalhado:

1. **Confirmar Quantidades e Salvar**
   - Localização: Tela de Aprovação de Produtos
   - Como fazer: Após revisar as quantidades dos produtos, clique no botão **Salvar**.
   - Campos/Opções disponíveis:
     * `Quantidade`: Campo numérico onde o usuário insere a quantidade de cada produto.
   - Resultado esperado: Os produtos aparecem como aprovados na lista.

2. **Identificar Local de Entrega**
   - Localização: Tela de Aprovação de Produtos
   - Como fazer: Após salvar, localize o campo para identificar o local de entrega e preencha com as informações necessárias.
   - Campos/Opções disponíveis:
     * `Local de Entrega`: Campo de texto onde o usuário insere o endereço ou nome do local.
   - Resultado esperado: O local de entrega é salvo e associado aos produtos aprovados.

3. **Finalizar Aprovação**
   - Localização: Tela de Aprovação de Produtos
   - Como fazer: Clique no botão **Finalizar**.
   - Observações importantes: Se o usuário sair da aba antes de finalizar, a aprovação será desfeita.
   - Resultado esperado: O sistema gera um registro de produtos aprovados e apresenta opções para o próximo passo.

4. **Escolher Próximo Passo**
   - Localização: Tela de Finalização
   - Como fazer: Após clicar em **Finalizar**, selecione entre as opções **Gerar Orçamento** ou **Compra Vulsa**.
   - Campos/Opções disponíveis:
     * `Gerar Orçamento`: Opção para criar uma referência de cotação com fornecedores.
     * `Compra Vulsa`: Opção para criar uma ordem de compra diretamente.
   - Resultado esperado: O sistema direciona o usuário para a tela de listagem de fornecedores.

5. **Selecionar Fornecedores**
   - Localização: Tela de Listagem de Fornecedores
   - Como fazer: O sistema automaticamente filtra fornecedores que fornecem o tipo de produto. O usuário pode optar por excluir fornecedores indesejados e selecionar apenas os desejados.
   - Observações importantes: O relacionamento entre fornecedores e produtos é configurado previamente no cadastro de parceiros.
   - Resultado esperado: Apenas os fornecedores selecionados são considerados para a cotação.

6. **Enviar E-mail para Fornecedores**
   - Localização: Tela de Listagem de Fornecedores
   - Como fazer: Após selecionar os fornecedores, salve as configurações. O sistema enviará automaticamente um e-mail para os fornecedores selecionados.
   - Resultado esperado: Os fornecedores recebem um e-mail com as informações necessárias para preencher e retornar ao sistema.

**Campos e Parâmetros:**

| Campo                | Tipo         | Obrigatório | Descrição                                           | Exemplo                  |
|----------------------|--------------|-------------|----------------------------------------------------|--------------------------|
| `Quantidade`         | Numérico     | Sim         | Quantidade de produtos a serem aprovados.         | 10                       |
| `Local de Entrega`   | Texto        | Sim         | Endereço ou nome do local onde os produtos serão entregues. | Rua das Flores, 123     |
| `Fornecedor`         | Dropdown     | Sim         | Lista de fornecedores disponíveis para cotação.    | Fornecedor A, Fornecedor B |
| `Opção de Finalização` | Botão      | Sim         | Escolha entre gerar orçamento ou compra vulsa.     | Gerar Orçamento, Compra Vulsa |

**Regras de Negócio:**
- A aprovação de produtos deve ser confirmada antes de finalizar o processo.
- Se o usuário sair da aba de aprovação sem salvar, a aprovação será desfeita.
- O sistema filtra automaticamente fornecedores com base nos produtos selecionados.

**Observações Importantes:**
- É crucial salvar as informações após cada etapa para evitar perda de dados.
- Erros comuns incluem não selecionar fornecedores ou não preencher o local de entrega.
- O cadastro de fornecedores deve estar completo para que o filtro funcione corretamente.

**Conceitos-Chave:**
- **Aprovação de Produtos**: Processo de validar e confirmar a aquisição de itens no sistema.
- **Cotação**: Solicitação de preços a fornecedores para comparação antes da compra.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                    | Solução                                      | Prevenção                                 |
|-----------------------------------|-----------------------------------|----------------------------------------------|-------------------------------------------|
| Não consigo salvar a aprovação     | Campos obrigatórios não preenchidos | Verifique se todos os campos obrigatórios estão preenchidos. | Sempre revisar os campos antes de salvar. |
| E-mail não enviado para fornecedores | Problemas de configuração de e-mail | Verifique as configurações de e-mail no sistema. | Testar as configurações de e-mail periodicamente. |
| Fornecedor não aparece na lista    | Não está cadastrado corretamente | Verifique o cadastro do fornecedor e a relação com os produtos. | Manter o cadastro de fornecedores atualizado. |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre revise as quantidades antes de salvar.
- Utilize a opção de orçamento quando não tiver certeza do fornecedor.
- Mantenha um registro dos fornecedores e suas cotações para futuras referências.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Aprovação de Produtos para Orçamento**
```
Situação: O usuário precisa aprovar 15 unidades de um produto específico.
Ação: 
  • Campo `Quantidade`: "15"
  • Campo `Local de Entrega`: "Armazém Central"
Resultado: Os produtos são aprovados e o local de entrega é salvo.
```

**Exemplo 2: Finalização de Compra Vulsa**
```
Situação: O usuário já conhece o fornecedor e deseja realizar uma compra direta.
Ação: 
  • Selecionar a opção `Compra Vulsa`
  • Escolher o fornecedor "Fornecedor A"
Resultado: O sistema cria uma ordem de compra diretamente sem passar pela cotação.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O cadastro de fornecedores deve estar completo e atualizado.
- **Habilita:** A geração de ordens de compra e cotações.
- **Relacionado a:** Módulo de Cadastro de Fornecedores e Gestão de Compras.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como aprovar produtos no sistema?"
- **Com problema:** "Não consigo finalizar a aprovação, o que fazer?"
- **Informal:** "Como eu aprovo os itens que comprei?"
- **Por sintoma:** "O que acontece se eu sair da aba sem salvar?"
- **Com dúvida:** "Qual a diferença entre orçamento e compra vulsa?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Aprovação de itens", "Finalização de cotações", "Gerar orçamento", "Compra direta", "Selecionar fornecedores".

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como aprovar produtos no sistema?
- O que fazer se a aprovação não for salva?
- Como escolher entre orçamento e compra vulsa?
- O que acontece se eu sair da aba sem salvar?
- O que preciso fazer antes de aprovar produtos?

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

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de preenchimento de cotações por fornecedores, incluindo como acessar o link, preencher informações e propor condições de pagamento. O objetivo é garantir que os fornecedores possam enviar suas ofertas de forma clara e organizada.

**Contexto:**
Estamos na fase do sistema onde um fornecedor, após receber um e-mail de convite, deve acessar um link para preencher uma cotação de produtos solicitados pela empresa. Este processo é essencial para a formalização de propostas e condições de pagamento.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Processo de Compras > Submenu Cotações
- Tela/interface específica: Formulário de Preenchimento de Cotações

**Funcionalidade Detalhada:**

A funcionalidade permite que o fornecedor preencha uma cotação com informações sobre produtos e condições de pagamento. O fornecedor acessa um link enviado por e-mail, onde pode visualizar detalhes da empresa solicitante, produtos, quantidades e valores. O sistema calcula automaticamente o valor total e permite sugestões de produtos alternativos.

### 🔹 Passo a Passo Detalhado:

1. **Acesso ao Link de Cotação**
   - Localização: E-mail recebido pelo fornecedor
   - Como fazer: O fornecedor deve abrir o e-mail e clicar no link que diz "clique abaixo e preencha sua oferta".
   - Resultado esperado: O fornecedor é redirecionado para a página de preenchimento da cotação.

2. **Visualização das Informações da Empresa**
   - Localização: Página de preenchimento da cotação
   - Como fazer: Após o redirecionamento, o fornecedor verá as informações da empresa solicitante na parte superior da página.
   - Resultado esperado: O fornecedor tem uma visão clara de quem está solicitando a cotação.

3. **Preenchimento da Cotação**
   - Localização: Seção de produtos e quantidades
   - Como fazer: O fornecedor verá uma lista de produtos e a quantidade solicitada, que já vem preenchida automaticamente. O fornecedor pode alterar a quantidade, se necessário.
   - Campos/Opções disponíveis:
     * `Quantidade`: Campo numérico, preenchido automaticamente, pode ser alterado.
   - Resultado esperado: O fornecedor ajusta a quantidade conforme necessário.

4. **Inserção do Valor Unitário**
   - Localização: Campo de valor unitário na cotação
   - Como fazer: O fornecedor deve inserir o valor unitário de cada produto na coluna correspondente.
   - Resultado esperado: O sistema calcula automaticamente o valor total com base na quantidade e no valor unitário inserido.

5. **Campo de Desconto**
   - Localização: Campo de desconto na cotação
   - Como fazer: O fornecedor pode optar por preencher um desconto, que é um campo opcional.
   - Resultado esperado: O desconto, se inserido, é aplicado ao valor total.

6. **Inserção de Comentários e Sugestões**
   - Localização: Campo de comentários e sugestões
   - Como fazer: O fornecedor pode inserir comentários adicionais e sugestões de outros produtos ou marcas.
   - Resultado esperado: Comentários e sugestões aparecem na cotação para consideração futura.

7. **Proposição de Condições de Pagamento**
   - Localização: Seção de condições de pagamento
   - Como fazer: O fornecedor clica em "Adicionar Condição" para propor condições como pagamento à vista ou parcelado.
   - Observações importantes: O fornecedor pode sugerir condições como "5% de desconto para pagamento à vista" ou "parcelamento em até 10 vezes".
   - Resultado esperado: As condições propostas são apresentadas para seleção ou criação de novas.

8. **Informações sobre Local de Entrega**
   - Localização: Seção de informações de entrega
   - Como fazer: O fornecedor deve preencher a validade da cotação e o tipo de frete.
   - Resultado esperado: As informações de entrega são registradas corretamente na cotação.

**Campos e Parâmetros:**

| Campo                  | Tipo        | Obrigatório | Descrição                                           | Exemplo                  |
|------------------------|-------------|-------------|----------------------------------------------------|--------------------------|
| `Nome do Fornecedor`   | Texto       | Sim         | Nome da empresa fornecedora                        | "Fornecedor XYZ"         |
| `Quantidade`           | Numérico    | Sim         | Quantidade de produtos solicitados                 | 10                       |
| `Valor Unitário`       | Numérico    | Sim         | Preço por unidade do produto                        | 50,00                    |
| `Desconto`             | Numérico    | Não         | Percentual de desconto oferecido                    | 5                        |
| `Comentários`          | Texto       | Não         | Observações adicionais sobre a proposta             | "Sugestão de marca A"    |
| `Condições de Pagamento`| Texto      | Sim         | Propostas de pagamento, como parcelamento          | "10% de desconto à vista" |
| `Validade da Cotação`  | Data        | Sim         | Data até quando a cotação é válida                 | "2024-12-31"             |
| `Tipo de Frete`        | Dropdown    | Sim         | Opções de frete disponíveis                         | "Frete Grátis", "Sedex"  |

**Regras de Negócio:**
- O valor total é calculado automaticamente com base na quantidade e no valor unitário.
- O desconto é opcional e deve ser inserido manualmente.
- As condições de pagamento podem ser propostas pelo fornecedor e selecionadas pelo comprador.
- A validade da cotação deve ser preenchida obrigatoriamente.

**Observações Importantes:**
- É importante que o fornecedor revise todas as informações antes de enviar a cotação.
- Erros comuns incluem não preencher o valor unitário ou a validade da cotação.
- O fornecedor deve garantir que as sugestões de produtos sejam relevantes e viáveis.

**Conceitos-Chave:**
- **Cotação**: Proposta formal de preços e condições de fornecimento de produtos.
- **Condições de Pagamento**: Termos que definem como e quando o pagamento será realizado.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                   | Solução                                           | Prevenção                                      |
|-----------------------------------|----------------------------------|--------------------------------------------------|------------------------------------------------|
| Campo de valor unitário não aceita valores | Formato incorreto (ex: letras) | Verifique se está inserindo apenas números       | Use sempre o formato numérico correto          |
| Desconto não aplicado             | Campo não preenchido corretamente| Certifique-se de que o campo de desconto foi preenchido | Revise todos os campos antes de enviar         |
| Link de cotação não funciona      | E-mail expirado ou inválido      | Solicite um novo link ao comprador               | Verifique a validade do link recebido          |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre revise os valores inseridos antes de enviar a cotação.
- Utilize o campo de comentários para esclarecer dúvidas ou fornecer informações adicionais.
- Considere as condições de pagamento que são mais vantajosas para ambas as partes.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Preenchimento de Cotação para Produtos de Escritório**
```
Situação: O fornecedor recebe um pedido para fornecer 100 canetas.
Ação: O fornecedor acessa o link, altera a quantidade para 100, insere o valor unitário de R$ 1,00 e sugere um desconto de 10%.
  • Campo `Quantidade`: 100
  • Campo `Valor Unitário`: 1,00
Resultado: O valor total aparece como R$ 100,00, e o desconto é aplicado corretamente.
```

**Exemplo 2: Proposição de Condições de Pagamento**
```
Situação: O fornecedor deseja oferecer condições de pagamento.
Ação: O fornecedor clica em "Adicionar Condição" e insere "5% de desconto para pagamento à vista".
Resultado: A condição é adicionada à cotação e pode ser selecionada pelo comprador.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O fornecedor deve ter recebido o e-mail de convite e ter acesso à internet.
- **Habilita:** O envio da cotação permite que o comprador avalie propostas e tome decisões de compra.
- **Relacionado a:** Funcionalidade de gerenciamento de fornecedores e controle de compras.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como preencher uma cotação?"
- **Com problema:** "Não consigo enviar a cotação, o que fazer?"
- **Informal:** "Como faço para mandar uma proposta?"
- **Por sintoma:** "O que fazer se o valor total não aparece?"
- **Com dúvida:** "Quais informações preciso colocar na cotação?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "preencher proposta", "enviar cotação", "oferta de preços", "sugerir produtos"
- "condições de pagamento", "termos de pagamento", "opções de pagamento"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como faço para acessar o link de cotação?
- O que devo preencher na cotação?
- Como posso sugerir condições de pagamento?
- O que fazer se o valor total não está sendo calculado?
- O que preciso ter antes de preencher a cotação?

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
- **🔑 Palavras-chave:** orçamentos, comparação, fornecedores, produtos, histórico

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como visualizar e comparar orçamentos no sistema, permitindo ao usuário analisar diferentes propostas de fornecedores com base em preço e prazo de entrega, facilitando a tomada de decisão.

**Contexto:**
Estamos na seção de orçamentos do módulo de compras, onde o usuário pode visualizar as cotações recebidas de diferentes fornecedores. O objetivo é permitir uma análise detalhada das propostas, considerando tanto o valor quanto o prazo de entrega.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Compras > Orçamentos
- Tela/interface específica: Tela de Visualização de Orçamentos

**Funcionalidade Detalhada:**
A funcionalidade de visualização e comparação de orçamentos permite que o usuário analise as cotações recebidas de diferentes fornecedores. O sistema oferece várias formas de visualização, como por produto, por fornecedor e por conjunto de orçamento. Cada uma dessas opções apresenta informações detalhadas sobre os produtos cotados, incluindo valores, prazos de entrega e condições de pagamento.

### 🔹 Passo a Passo Detalhado:

1. **Selecionar Visualização por Produto**
   - Localização: Parte superior da tela de orçamentos, na aba de visualização.
   - Como fazer: Clique na opção **"Por Produto"**.
   - Campos/Opções disponíveis:
     * `Produto`: Lista de produtos cotados.
     * `Histórico de Cotação`: Exibe o histórico de cotações para cada produto.
   - Resultado esperado: O sistema separa cada produto, mostrando o histórico de cotação e permitindo comparações entre o melhor valor e a entrega mais rápida, sinalizada por cores.

2. **Selecionar Visualização por Fornecedor**
   - Localização: Parte superior da tela de orçamentos, na aba de visualização.
   - Como fazer: Clique na opção **"Por Fornecedor"**.
   - Observações importantes: Esta visualização permite ver todos os orçamentos com um fornecedor específico, independentemente de terem sido respondidos ou não.
   - Resultado esperado: A tela exibirá todos os orçamentos relacionados ao fornecedor selecionado, como **"Casas d'Água"**, mostrando orçamentos como **467** e **468**.

3. **Selecionar Visualização por Conjunto de Orçamento**
   - Localização: Parte superior da tela de orçamentos, na aba de visualização.
   - Como fazer: Clique na opção **"Por Conjunto de Orçamento"**.
   - Resultado esperado: O sistema agrupa todos os orçamentos realizados, permitindo visualizar informações como o orçamento **468**, com detalhes sobre fornecedores e status de retorno.

4. **Visualizar Detalhes do Orçamento**
   - Localização: Dentro da visualização de orçamentos, ao selecionar um orçamento específico.
   - Como fazer: Clique no número do orçamento (ex: **468**).
   - Campos/Opções disponíveis:
     * `Valor Unitário`: Valor de cada item cotado.
     * `Total`: Valor total do orçamento.
     * `Prazo de Entrega`: Tempo estimado para entrega.
     * `Frete`: Campo que pode ser preenchido pelo fornecedor.
     * `Condições de Pagamento`: Informações sobre como o pagamento deve ser realizado.
   - Resultado esperado: O usuário visualiza todos os detalhes do orçamento, incluindo informações sobre retorno de fornecedores.

5. **Preencher Informações de Frete**
   - Localização: Na tela de detalhes do orçamento, próximo ao campo de frete.
   - Como fazer: Preencha o campo de frete se o fornecedor desejar cobrar pelo serviço.
   - Observações importantes: O preenchimento do campo de frete não é obrigatório.
   - Resultado esperado: O campo de frete é atualizado com o valor inserido, se aplicável.

**Campos e Parâmetros:**

| Campo                  | Tipo       | Obrigatório | Descrição                                      | Exemplo                |
|------------------------|------------|-------------|------------------------------------------------|------------------------|
| `Produto`              | Texto      | Sim         | Nome do produto cotado                         | "Argamassa"            |
| `Histórico de Cotação` | Texto      | Não         | Histórico de cotações para o produto           | "Cotações anteriores"   |
| `Valor Unitário`       | Numérico   | Sim         | Valor de cada unidade do produto                | "R$ 25,00"             |
| `Total`                | Numérico   | Sim         | Valor total do orçamento                        | "R$ 250,00"            |
| `Prazo de Entrega`     | Texto      | Sim         | Tempo estimado para entrega do produto         | "5 dias"               |
| `Frete`                | Numérico   | Não         | Valor do frete, se aplicável                   | "R$ 15,00"             |
| `Condições de Pagamento` | Texto    | Sim         | Informações sobre o pagamento                   | "À vista"              |

**Regras de Negócio:**
- O campo de frete é opcional e pode ser preenchido pelo fornecedor.
- As informações exibidas nas visualizações são baseadas nos dados preenchidos pelo usuário ou pelo fornecedor.
- O sistema permite comparação entre diferentes fornecedores com base em preço e prazo de entrega.

**Observações Importantes:**
- Sempre verifique se as informações estão atualizadas antes de tomar uma decisão.
- Evite preencher o campo de frete se não for necessário, para não confundir os dados.
- O sistema sinaliza visualmente o melhor prazo de entrega e o melhor valor.

**Conceitos-Chave:**
- **Orçamento**: Proposta de preço e condições de um fornecedor para um produto ou serviço.
- **Comparação**: Análise entre diferentes orçamentos para determinar a melhor opção.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                     | Solução                                      | Prevenção                                   |
|-----------------------------------|------------------------------------|----------------------------------------------|---------------------------------------------|
| Não aparece o histórico de cotações | Dados não foram preenchidos corretamente | Verifique se todos os produtos estão cadastrados | Sempre preencher todos os campos obrigatórios |
| Campo de frete desabilitado       | Fornecedor não configurou o frete  | Confirme com o fornecedor se o frete é aplicável | Comunicar-se com o fornecedor antes         |

**💡 DICAS E BOAS PRÁTICAS:**
- Utilize a visualização por produto para análises detalhadas.
- Mantenha um registro dos orçamentos anteriores para referência futura.
- Sempre compare prazos de entrega e valores antes de decidir.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Comparação de Orçamentos por Produto**
```
Situação: Você precisa comprar argamassa e recebeu cotações de dois fornecedores.
Ação: 
  • Selecione a visualização "Por Produto".
  • Compare os preços e prazos de entrega.
Resultado: O fornecedor A oferece o melhor prazo de entrega, enquanto o fornecedor B tem o melhor preço.
```

**Exemplo 2: Visualização de Orçamentos por Fornecedor**
```
Situação: Você deseja verificar todos os orçamentos com o fornecedor "Casas d'Água".
Ação: 
  • Selecione a visualização "Por Fornecedor".
Resultado: Você vê todos os orçamentos (467 e 468) e seus respectivos status de retorno.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O usuário deve ter permissões adequadas para visualizar orçamentos.
- **Habilita:** A comparação de orçamentos permite decisões informadas sobre compras.
- **Relacionado a:** Funcionalidades de cadastro de fornecedores e produtos.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como comparar orçamentos?"
- **Com problema:** "Não consigo visualizar os orçamentos, o que fazer?"
- **Informal:** "Como vejo os preços dos fornecedores?"
- **Por sintoma:** "Quando não aparece o histórico de cotações, o que fazer?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "comparar cotações", "visualizar propostas", "analisar orçamentos", "cotação de fornecedores"
- "orçamento", "proposta", "cotações"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso visualizar os orçamentos recebidos?
- Quais são as opções de visualização de orçamentos?
- Como comparar preços e prazos de entrega entre fornecedores?
- O que fazer se o campo de frete não estiver habilitado?
- O que preciso fazer antes de visualizar os orçamentos?

---


---


---

## 7. Processo de Negociação e Criação de Ordem de Compra

**📋 METADADOS:**
- **ID:** sec_7
- **⏱️ Minutagem:** 15:02 → 17:35
- **⏲️ Duração:** 152s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/qFzqzIoiVE4?si=YoVxiJOkipNVbQWb&t=902)
- **📦 Módulo:** Negociação de Fornecedores
- **🏷️ Categorias:** Negociação, Compras, Fornecedores, Ordens de Compra
- **🔑 Palavras-chave:** negociação, fornecedor, orçamento, ordem de compra, frete, pagamento, desconto

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de negociação com fornecedores, incluindo a edição de orçamentos, seleção de produtos, opções de pagamento e criação de ordens de compra. O objetivo é garantir que o usuário compreenda como gerenciar cotações e formalizar compras de forma eficiente.

**Contexto:**
Estamos na etapa de negociação com fornecedores dentro do módulo de compras do sistema. O objetivo é selecionar o fornecedor adequado, negociar condições e formalizar a ordem de compra.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Negociação de Fornecedores > Submenu Criar Ordem de Compra
- Tela/interface específica: Tela de Negociação com Fornecedor

**Funcionalidade Detalhada:**
Esta funcionalidade permite ao usuário gerenciar o processo de negociação com fornecedores, incluindo a edição de orçamentos, seleção de produtos, definição de condições de entrega e pagamento, e criação da ordem de compra. É utilizada quando o usuário decide formalizar a compra após avaliar as cotações de diferentes fornecedores.

### 🔹 Passo a Passo Detalhado:

1. **Selecionar Fornecedor e Editar Orçamento**
   - Localização: Tela de Negociação com Fornecedor, ícone de três pontinhos (⋮)
   - Como fazer: Clique nos três pontinhos para acessar as opções de edição do orçamento. Aqui, você pode preencher as informações necessárias sobre o retorno do fornecedor.
   - Campos/Opções disponíveis:
     * `Orçamento`: Campo para editar as informações do orçamento.
   - Resultado esperado: O orçamento é atualizado com as informações fornecidas.

2. **Adicionar Produtos ao Carrinho**
   - Localização: Tela de Negociação com Fornecedor, botão "Adicionar"
   - Como fazer: Após decidir o fornecedor, clique no botão "Adicionar" para incluir os produtos no carrinho.
   - Resultado esperado: Os produtos selecionados são adicionados ao carrinho de compras.

3. **Acessar Carrinho e Negociar**
   - Localização: Parte superior da tela, opção "Carrinho"
   - Como fazer: Clique na opção "Carrinho" e, em seguida, selecione "Negociar".
   - Observações importantes: O sistema pode puxar negociações anteriores que estão em aberto.
   - Resultado esperado: Você visualiza os produtos definidos e pode remover itens indesejados.

4. **Definir Informações de Entrega e Frete**
   - Localização: Tela de Negociação, seção de entrega
   - Como fazer: Insira as informações relacionadas à entrega, incluindo o valor do frete.
   - Resultado esperado: As informações de entrega e frete são salvas e consideradas na negociação.

5. **Selecionar Opções de Pagamento**
   - Localização: Tela de Negociação, seção de pagamento
   - Como fazer: O fornecedor pode apresentar até três opções de pagamento. Se nenhuma delas for adequada, clique em "Adicionar nova forma de pagamento".
   - Campos/Opções disponíveis:
     * `Forma de Pagamento`: Seletor para escolher entre as opções apresentadas ou adicionar uma nova.
   - Resultado esperado: A forma de pagamento é definida para a negociação.

6. **Inserir Comentários e Resumo do Pedido**
   - Localização: Tela de Negociação, campo de comentários e seção de resumo do pedido
   - Como fazer: Insira um comentário relevante no campo designado e revise o resumo do pedido, que inclui subtotais, local de entrega e data.
   - Campos/Opções disponíveis:
     * `Comentário`: Campo para inserir observações.
     * `Resumo do Pedido`: Exibe informações como subtotais e local de entrega.
   - Resultado esperado: O resumo do pedido é atualizado com as informações inseridas.

7. **Aplicar Descontos Negociados**
   - Localização: Tela de Negociação, campos de desconto
   - Como fazer: Preencha os campos para desconto negociado em relação ao produto e ao frete.
   - Campos/Opções disponíveis:
     * `Desconto Produto`: Campo para inserir o valor do desconto aplicado ao produto.
     * `Desconto Frete`: Campo para inserir o valor do desconto aplicado ao frete.
   - Resultado esperado: O valor total é reajustado automaticamente com base nos descontos inseridos.

8. **Criar Ordem de Compra**
   - Localização: Tela de Negociação, botão "Criar Ordem de Compra"
   - Como fazer: Após validar todas as informações, clique em "Criar Ordem de Compra".
   - Resultado esperado: A ordem de compra é criada e registrada no sistema.

9. **Enviar E-mail ao Fornecedor**
   - Localização: Tela de Negociação, opção para enviar e-mail
   - Como fazer: Se desejar, envie um segundo e-mail ao fornecedor informando que ele foi escolhido. O e-mail pode incluir um relatório com os dados da compra.
   - Observações importantes: Este e-mail não é obrigatório para lançar a nota e dar sequência no fluxo.
   - Resultado esperado: O fornecedor recebe o e-mail e pode aprovar ou não a compra.

**Campos e Parâmetros:**

| Campo                     | Tipo       | Obrigatório | Descrição                                               | Exemplo                  |
|---------------------------|------------|-------------|---------------------------------------------------------|--------------------------|
| `Orçamento`               | Texto      | Sim         | Campo para editar informações do orçamento.             | "Orçamento 2024"         |
| `Forma de Pagamento`      | Dropdown   | Sim         | Opções de pagamento apresentadas pelo fornecedor.       | "Cartão de Crédito"      |
| `Comentário`              | Texto      | Não         | Campo para inserir observações sobre a negociação.      | "Favor confirmar entrega."|
| `Desconto Produto`        | Numérico   | Não         | Valor do desconto aplicado ao produto.                  | "10"                     |
| `Desconto Frete`          | Numérico   | Não         | Valor do desconto aplicado ao frete.                    | "5"                      |

**Regras de Negócio:**
- O orçamento deve ser editado antes de prosseguir com a negociação.
- O usuário pode adicionar ou remover produtos do carrinho antes de criar a ordem de compra.
- O envio do e-mail ao fornecedor é opcional, mas recomendado para formalizar a escolha.

**Observações Importantes:**
- Verifique se todas as informações estão corretas antes de criar a ordem de compra.
- Evite adicionar produtos desnecessários ao carrinho, pois isso pode complicar a negociação.
- O sistema pode não permitir a criação da ordem de compra se campos obrigatórios não forem preenchidos.

**Conceitos-Chave:**
- **Ordem de Compra**: Documento formal que confirma a compra de produtos ou serviços de um fornecedor.
- **Negociação**: Processo de discutir e acordar termos de compra com um fornecedor.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                      | Solução                                           | Prevenção                                       |
|-----------------------------------|-------------------------------------|--------------------------------------------------|-------------------------------------------------|
| Não consigo editar o orçamento     | Permissões insuficientes            | Verifique as permissões do usuário na administração. | Configure permissões adequadas antes.          |
| Botão "Criar Ordem de Compra" desabilitado | Campos obrigatórios não preenchidos | Preencha todos os campos obrigatórios.          | Revise os campos antes de tentar criar a ordem.|
| E-mail não enviado ao fornecedor   | Falha na configuração de e-mail     | Verifique as configurações de e-mail do sistema. | Teste a funcionalidade de envio de e-mail.     |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre revise as cotações de diferentes fornecedores antes de tomar uma decisão.
- Utilize o campo de comentários para registrar informações importantes sobre a negociação.
- Mantenha um histórico de negociações para futuras referências.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Negociação com Fornecedor A**
```
Situação: O usuário decide negociar com o Fornecedor A após avaliar as cotações.
Ação: 
  • Campo Orçamento: "Orçamento 2024"
  • Forma de Pagamento: "Transferência Bancária"
Resultado: O orçamento é atualizado e a ordem de compra é criada com sucesso.
```

**Exemplo 2: Negociação com Fornecedor B**
```
Situação: O usuário precisa adicionar um novo desconto ao frete.
Ação: 
  • Campo Desconto Frete: "5"
Resultado: O valor total da compra é reajustado automaticamente.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O usuário deve ter acesso ao módulo de negociação e permissões para editar orçamentos.
- **Habilita:** A criação de ordens de compra e o envio de e-mails para fornecedores.
- **Relacionado a:** Módulo de Compras, Histórico de Compras, Gestão de Fornecedores.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como negociar com um fornecedor?"
- **Com problema:** "Não consigo criar uma ordem de compra, o que fazer?"
- **Informal:** "Como faço pra fechar negócio com o fornecedor?"
- **Por sintoma:** "Quando o botão de criar ordem não aparece, o que significa?"
- **Com dúvida:** "Quais informações preciso para negociar com um fornecedor?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Fechar compra", "formalizar compra", "negociar preços", "criar pedido", "enviar orçamento"
- "Cotação", "fornecedor", "negociação de preços", "ordem de compra"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como editar o orçamento de um fornecedor?
- O que fazer se o botão de criar ordem de compra estiver desabilitado?
- Como adicionar um novo desconto na negociação?
- O que fazer se o e-mail para o fornecedor não for enviado?
- Quais informações preciso ter antes de criar uma ordem de compra?

---


---


---

## 8. Criação e Lançamento de Nota Fiscal Associada à Ordem de Compra

**📋 METADADOS:**
- **ID:** sec_8
- **⏱️ Minutagem:** 17:33 → 20:07
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/qFzqzIoiVE4?si=YoVxiJOkipNVbQWb&t=1053)
- **📦 Módulo:** Compras
- **🏷️ Categorias:** Compras, Financeiro, Lançamento, Nota Fiscal
- **🔑 Palavras-chave:** ordem de compra, nota fiscal, lançamento manual, recibo de produtos, fluxo de caixa

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de criação de uma nota fiscal associada a uma ordem de compra, incluindo a escolha entre nota eletrônica e manual, e o preenchimento dos campos necessários para formalizar o pagamento.

**Contexto:**
Estamos no módulo de Compras, onde o usuário finaliza a ordem de compra e inicia o processo de lançamento da nota fiscal, que é essencial para a formalização do pagamento ao fornecedor.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Compras > Submenu Ordem de Compra
- Tela/interface específica: Tela de Lançamento de Nota Fiscal

**Funcionalidade Detalhada:**
Esta funcionalidade permite que o usuário crie uma nota fiscal associada a uma ordem de compra previamente aprovada. O sistema já preenche automaticamente as informações necessárias com base nos produtos, quantidades e valores definidos na ordem de compra. O usuário pode optar por lançar uma nota eletrônica ou uma nota manual, sendo que esta última é utilizada como um demonstrativo.

### 🔹 Passo a Passo Detalhado:

1. **Escolha do Tipo de Nota**
   - Localização: Tela de Lançamento de Nota Fiscal
   - Como fazer: Após acessar a tela, o usuário deve selecionar o tipo de nota que deseja lançar. Para isso, clique no botão **"Lançar Nota Manual"**.
   - Campos/Opções disponíveis:
     * `Tipo de Nota`: Opções incluem **Nota Eletrônica** e **Nota Manual**.
   - Resultado esperado: O sistema prepara a tela para o preenchimento dos dados da nota fiscal.

2. **Definição do Tipo de Recibo**
   - Localização: Campo de seleção na tela de lançamento
   - Como fazer: No campo **"Tipo de Recibo"**, selecione **"Recibo de Produtos"**.
   - Observações importantes: Este campo é obrigatório para prosseguir com o lançamento.
   - Resultado esperado: O sistema registra o tipo de recibo e avança para o próximo campo.

3. **Associação à Ordem de Compra**
   - Localização: Campo de seleção para ordem de compra
   - Como fazer: No campo **"Ordem de Compra Associada"**, escolha a ordem de compra que você deseja vincular à nota fiscal.
   - Resultado esperado: O sistema preenche automaticamente algumas informações relevantes da ordem de compra selecionada.

4. **Preenchimento da Data de Emissão**
   - Localização: Campo de data na tela de lançamento
   - Como fazer: No campo **"Data de Emissão"**, insira a data atual ou a data em que a nota foi emitida.
   - Resultado esperado: A data é registrada e permite que o usuário avance para o próximo passo.

5. **Complementação de Informações Opcionais**
   - Localização: Campos adicionais na tela de lançamento
   - Como fazer: O usuário pode optar por preencher campos como **"Número de Documento"**, **"Anexar Nota"** e **"Observações"**. Esses campos são opcionais.
   - Resultado esperado: Informações adicionais podem ser anexadas, mas não são obrigatórias para o lançamento da nota.

6. **Relação de Produtos, Quantidades e Valores**
   - Localização: Seção de produtos na tela de lançamento
   - Como fazer: O sistema já traz a relação de produtos, quantidades e valores da ordem de compra. O usuário deve revisar essas informações.
   - Resultado esperado: O financeiro valida se as informações estão corretas e condizem com a nota que possui.

7. **Definição de Pagamento**
   - Localização: Campo de pagamento na tela de lançamento
   - Como fazer: O usuário deve definir uma **classificação para o fluxo de caixa**, identificando o custo que aparecerá no financeiro. Além disso, preencher os campos de **desconto** e **frete**.
   - Resultado esperado: O sistema registra as informações de pagamento e permite que o usuário avance.

8. **Geração do Financeiro**
   - Localização: Botão de geração na tela de lançamento
   - Como fazer: Clique no botão **"Gerar Financeiro"** para finalizar o lançamento da nota fiscal.
   - Campos/Opções disponíveis:
     * `Quantidade de Parcelas`: Defina quantas parcelas o pagamento terá.
     * `Vencimento`: Insira a data de vencimento da primeira parcela.
     * `Formas de Pagamento`: Selecione entre opções como **Cartão de Crédito**, **Boleto**, etc.
     * `Anexos`: Adicione documentos relevantes, se necessário.
   - Resultado esperado: O sistema finaliza o lançamento e registra a nota fiscal no sistema.

**Campos e Parâmetros:**

| Campo                     | Tipo           | Obrigatório | Descrição                                                       | Exemplo               |
|---------------------------|----------------|-------------|---------------------------------------------------------------|-----------------------|
| Tipo de Nota              | Dropdown       | Sim         | Seleção entre Nota Eletrônica e Nota Manual                   | Nota Manual           |
| Tipo de Recibo            | Dropdown       | Sim         | Tipo de recibo a ser gerado                                   | Recibo de Produtos     |
| Ordem de Compra Associada  | Dropdown       | Sim         | Seleção da ordem de compra vinculada à nota                   | Ordem #12345         |
| Data de Emissão           | Data           | Sim         | Data em que a nota fiscal foi emitida                         | 01/10/2023            |
| Número de Documento       | Texto          | Não         | Número do documento da nota fiscal                             | 123456789             |
| Anexar Nota               | Upload         | Não         | Opção para anexar um arquivo da nota fiscal                   | [Selecionar arquivo]   |
| Observações               | Texto          | Não         | Campo para adicionar observações sobre a nota                  | Nota referente a pedido|
| Quantidade de Parcelas    | Número         | Sim         | Número de parcelas para o pagamento                            | 3                     |
| Vencimento                | Data           | Sim         | Data de vencimento da primeira parcela                         | 01/11/2023            |
| Formas de Pagamento       | Dropdown       | Sim         | Seleção da forma de pagamento a ser utilizada                 | Boleto                |
| Desconto                  | Número         | Não         | Valor de desconto a ser aplicado                               | 10,00                 |
| Frete                     | Número         | Não         | Valor do frete a ser considerado no pagamento                  | 15,00                 |

**Regras de Negócio:**
- A ordem de compra deve ser aprovada antes do lançamento da nota fiscal.
- O tipo de recibo deve ser selecionado obrigatoriamente para prosseguir.
- A data de emissão é um campo obrigatório e deve ser preenchido corretamente.
- O financeiro deve validar se as informações da nota fiscal condizem com a ordem de compra.

**Observações Importantes:**
- É recomendável revisar todas as informações antes de finalizar o lançamento da nota fiscal.
- Erros comuns incluem não selecionar a ordem de compra ou não preencher a data de emissão.
- Certifique-se de que as permissões de usuário estão configuradas para permitir o lançamento de notas fiscais.

**Conceitos-Chave:**
- **Ordem de Compra**: Documento que formaliza a intenção de compra de produtos ou serviços.
- **Nota Fiscal**: Documento que registra a transação comercial e é necessário para a formalização do pagamento.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                       | Solução                                                   | Prevenção                                               |
|-----------------------------------|--------------------------------------|-----------------------------------------------------------|--------------------------------------------------------|
| Não é possível lançar a nota      | Ordem de compra não aprovada        | Verifique se a ordem de compra foi aprovada antes        | Sempre aguarde a aprovação da ordem de compra          |
| Campo de data não aceita          | Formato de data incorreto           | Insira a data no formato correto (DD/MM/AAAA)            | Utilize um calendário para selecionar a data correta   |
| Erro ao gerar financeiro           | Campos obrigatórios não preenchidos  | Preencha todos os campos obrigatórios antes de prosseguir | Revise os campos obrigatórios antes de finalizar        |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre anexe documentos relevantes para facilitar a validação do financeiro.
- Utilize a opção de observações para esclarecer detalhes sobre a nota fiscal.
- Revise as informações da ordem de compra antes de iniciar o lançamento da nota.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Lançamento de Nota Manual**
```
Situação: Lançamento de uma nota manual para a ordem de compra #12345.
Ação: 
  • Campo Tipo de Nota: "Nota Manual"
  • Campo Tipo de Recibo: "Recibo de Produtos"
  • Campo Ordem de Compra Associada: "Ordem #12345"
  • Campo Data de Emissão: "01/10/2023"
Resultado: A nota fiscal é lançada com sucesso e associada à ordem de compra.
```

**Exemplo 2: Lançamento de Nota com Desconto**
```
Situação: Lançamento de uma nota com desconto aplicado.
Ação: 
  • Campo Tipo de Nota: "Nota Manual"
  • Campo Tipo de Recibo: "Recibo de Produtos"
  • Campo Ordem de Compra Associada: "Ordem #12346"
  • Campo Data de Emissão: "02/10/2023"
  • Campo Desconto: "10,00"
Resultado: A nota fiscal é lançada com desconto e associada à ordem de compra.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** A ordem de compra deve estar aprovada e os produtos devem estar definidos.
- **Habilita:** O lançamento da nota fiscal permite a formalização do pagamento ao fornecedor.
- **Relacionado a:** Módulo Financeiro, onde o pagamento será gerado após o lançamento da nota.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como lançar uma nota fiscal associada à ordem de compra?"
- **Com problema:** "Não consigo lançar a nota fiscal, o que fazer?"
- **Informal:** "Como faço para colocar a nota da compra?"
- **Por sintoma:** "Quando a ordem de compra está aprovada, como lanço a nota?"
- **Com dúvida:** "Quais campos são obrigatórios para lançar a nota fiscal?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Criar nota fiscal", "Registrar nota", "Emitir nota", "Lançar nota de compra"
- "Nota eletrônica", "Nota manual", "Recibo de compra", "Recibo de produtos"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como lançar uma nota fiscal associada à ordem de compra?
- Quais campos são obrigatórios para o lançamento da nota fiscal?
- O que fazer se a ordem de compra não estiver aprovada?
- O que fazer se o campo de data não aceitar o formato?
- O que preciso ter feito antes de lançar a nota fiscal?

---


---


---

## 9. Lançamento de Nota e Entrada de Produto no Estoque

**📋 METADADOS:**
- **ID:** sec_9
- **⏱️ Minutagem:** 20:04 → 22:39
- **⏲️ Duração:** 154s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/qFzqzIoiVE4?si=YoVxiJOkipNVbQWb&t=1204)
- **📦 Módulo:** Compras
- **🏷️ Categorias:** Lançamento, Estoque, Compras, Financeiro
- **🔑 Palavras-chave:** nota, ordem de compra, estoque, cronograma financeiro, contas a pagar

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de lançamento de uma nota fiscal e a entrada do produto no estoque, explicando como a quantidade lançada impacta a ordem de compra e o cronograma financeiro da obra.

**Contexto:**
Estamos no módulo de Compras do sistema, onde o usuário realiza o lançamento de notas fiscais que estão diretamente ligadas a ordens de compra. O objetivo é garantir que a quantidade de produtos recebidos esteja correta e que o fluxo financeiro da obra seja atualizado adequadamente.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Compras > Lançamento de Notas
- Tela/interface específica: Tela de Lançamento de Notas

**Funcionalidade Detalhada:**
O lançamento de uma nota fiscal é uma etapa crucial no fluxo de compras, pois determina se a ordem de compra vinculada será finalizada ou permanecerá em andamento. Além disso, este processo gera o cronograma financeiro da obra e atualiza as contas a pagar, refletindo no fluxo de caixa. A funcionalidade permite que o usuário compare a quantidade prevista na nota com a quantidade real recebida, garantindo a precisão no estoque.

### 🔹 Passo a Passo Detalhado:

1. **Salvar Nota Fiscal**
   - Localização: Tela de Lançamento de Notas, botão **Salvar**
   - Como fazer: Após preencher todos os campos necessários da nota, clique no botão **Salvar** para registrar a nota no sistema.
   - Campos/Opções disponíveis:
     * `Número da Nota`: Campo numérico que identifica a nota fiscal.
     * `Data de Emissão`: Campo de data que registra quando a nota foi emitida.
   - Resultado esperado: A nota fiscal é registrada e, se a quantidade lançada na nota corresponder à quantidade da ordem de compra, a ordem será finalizada automaticamente.

2. **Verificar Status da Ordem de Compra**
   - Localização: Tela de Ordens de Compra, seção de status
   - Como fazer: Após o lançamento da nota, verifique o status da ordem de compra vinculada.
   - Observações importantes: Se a quantidade não bater, o status da ordem de compra será "Andamento", permitindo o lançamento de outras notas.
   - Resultado esperado: O status da ordem de compra é atualizado conforme a quantidade recebida.

3. **Gerar Cronograma Financeiro**
   - Localização: Módulo de Acompanhamento da Obra
   - Como fazer: Após o lançamento da nota, acesse o módulo de acompanhamento para visualizar o cronograma financeiro.
   - Resultado esperado: O cronograma financeiro é atualizado com as informações da nota lançada, refletindo no planejamento financeiro da obra.

4. **Registrar Entrada de Produto no Estoque**
   - Localização: Módulo de Suprimentos > Aba de Entradas
   - Como fazer: Acesse a aba de entradas para registrar a entrada do produto no estoque.
   - Observações importantes: É necessário fazer um comparativo entre a quantidade prevista e a quantidade real recebida.
   - Resultado esperado: O produto é registrado no estoque, e uma nova pendência é criada na aba de entradas.

5. **Conferir Quantidade Prevista e Real**
   - Localização: Tela de Conferência de Entradas
   - Como fazer: Compare a quantidade prevista na nota com a quantidade que realmente chegou.
   - Campos/Opções disponíveis:
     * `Quantidade Prevista`: Campo que mostra a quantidade que deveria ter chegado.
     * `Quantidade Real`: Campo que mostra a quantidade que realmente chegou.
   - Resultado esperado: Se as quantidades coincidirem, a entrada é confirmada e salva.

**Campos e Parâmetros:**

| Campo                | Tipo     | Obrigatório | Descrição                                         | Exemplo            |
|----------------------|----------|-------------|---------------------------------------------------|--------------------|
| Número da Nota       | Numérico | Sim         | Identificação única da nota fiscal.               | 123456             |
| Data de Emissão      | Data     | Sim         | Data em que a nota fiscal foi emitida.            | 01/10/2023         |
| Quantidade Prevista  | Numérico | Sim         | Quantidade de produtos que deveriam ter chegado.  | 100                |
| Quantidade Real      | Numérico | Sim         | Quantidade de produtos que realmente chegaram.    | 100                |

**Regras de Negócio:**
- A ordem de compra é finalizada automaticamente se a quantidade da nota fiscal corresponde à quantidade da ordem.
- Se a quantidade não coincidir, a ordem de compra permanece com status "Andamento".
- O cronograma financeiro é gerado automaticamente após o lançamento da nota.

**Observações Importantes:**
- É crucial verificar se a quantidade recebida corresponde à quantidade prevista para evitar problemas no estoque.
- Erros comuns incluem o lançamento de notas com quantidades incorretas, o que pode causar desajustes no estoque e no financeiro.
- As permissões de usuário devem estar configuradas corretamente para permitir o lançamento de notas.

**Conceitos-Chave:**
- **Ordem de Compra**: Documento que formaliza a compra de produtos e equipamentos.
- **Cronograma Financeiro**: Planejamento que detalha as despesas e receitas ao longo da obra.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                   | Solução                                         | Prevenção                                   |
|-----------------------------------|----------------------------------|------------------------------------------------|---------------------------------------------|
| Nota não salva                    | Campos obrigatórios não preenchidos | Verifique se todos os campos obrigatórios estão preenchidos. | Sempre revisar os campos antes de salvar.  |
| Status da ordem não atualiza      | Quantidade da nota não bate com a ordem | Verifique a quantidade lançada e compare com a ordem de compra. | Conferir as quantidades antes do lançamento. |
| Produto não aparece no estoque     | Entrada não registrada corretamente | Acesse a aba de entradas e registre a entrada do produto. | Confirmar a entrada após o recebimento.    |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre salve a nota após cada alteração para evitar perda de dados.
- Utilize a função de comparação de quantidades para garantir a precisão no estoque.
- Mantenha um registro das notas lançadas para facilitar auditorias futuras.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Lançamento de Nota Fiscal**
```
Situação: Recebimento de materiais para a obra.
Ação: Lançar a nota fiscal no sistema.
  • Número da Nota: "123456"
  • Data de Emissão: "01/10/2023"
Resultado: A nota é salva e a ordem de compra é finalizada, pois a quantidade lançada corresponde à quantidade da ordem.
```

**Exemplo 2: Conferência de Entrada de Produto**
```
Situação: Conferir a entrada de materiais recebidos.
Ação: Comparar a quantidade prevista com a quantidade real.
  • Quantidade Prevista: "100"
  • Quantidade Real: "90"
Resultado: A ordem de compra permanece em andamento, permitindo o lançamento de uma nova nota para os 10 itens faltantes.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** A ordem de compra deve estar criada e vinculada à nota fiscal.
- **Habilita:** O fluxo de caixa e o cronograma financeiro são atualizados após o lançamento da nota.
- **Relacionado a:** Módulo de Acompanhamento da Obra e Módulo de Suprimentos.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como lançar uma nota fiscal?"
- **Com problema:** "Não consigo finalizar a ordem de compra, o que fazer?"
- **Informal:** "Como eu coloco a nota no sistema?"
- **Por sintoma:** "Quando a quantidade não bate, como resolver?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Registrar nota", "Adicionar nota", "Lançar nota fiscal", "Entrada de produto", "Atualizar estoque"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como faço para lançar uma nota fiscal no sistema?
- O que acontece se a quantidade da nota não bater com a ordem de compra?
- Como verificar o status da ordem de compra após o lançamento da nota?
- O que fazer se a entrada do produto não aparecer no estoque?
- Quais campos são obrigatórios ao lançar uma nota fiscal?

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
- **🏷️ Categorias:** Operacional, Cadastro, Finanças
- **🔑 Palavras-chave:** Ordem de serviço, prestador, centro de custo, pagamento, serviços cadastrados

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de criação de uma ordem de serviço no sistema, incluindo a seleção de prestadores, definição de centros de custo e opções de pagamento, resolvendo a necessidade de formalização de serviços prestados.

**Contexto:**
Estamos na interface de gestão de obras, onde o usuário precisa formalizar a contratação de um prestador de serviços, criando uma ordem de serviço que será posteriormente utilizada para lançamento financeiro.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Gestão de Obras > Ordem de Serviço
- Tela/interface específica: Tela de Criação de Ordem de Serviço

**Funcionalidade Detalhada:**
A funcionalidade de criação de ordem de serviço permite ao usuário formalizar a contratação de um prestador para a execução de serviços relacionados a uma obra específica. O usuário pode selecionar prestadores, definir centros de custo, e especificar detalhes financeiros, como forma de pagamento e valores.

### 🔹 Passo a Passo Detalhado:

1. **Criar Ordem de Serviço**
   - Localização: Botão **"Mais Ordem de Serviço"** na tela de gestão de obras.
   - Como fazer: Clique no botão **"Mais Ordem de Serviço"** para iniciar o processo de criação.
   - Campos/Opções disponíveis:
     * `Prestador`: Seleção do prestador de serviços.
     * `Centro de Custo`: Seleção do centro de custo relacionado à obra.
   - Resultado esperado: Uma nova tela de criação de ordem de serviço é exibida.

2. **Definir Prestador e Centro de Custo**
   - Localização: Campos na nova tela de criação de ordem de serviço.
   - Como fazer: 
     - No campo **"Prestador"**, selecione o prestador desejado (ex: **Edivaldo**).
     - No campo **"Centro de Custo"**, escolha o centro de custo (ex: **Vila Real**).
   - Observações importantes: A seleção do prestador deve ser feita a partir da lista de prestadores já cadastrados. Se o prestador não estiver na lista, é possível adicioná-lo.
   - Resultado esperado: O prestador e o centro de custo são definidos corretamente.

3. **Selecionar Serviço**
   - Localização: Lateral da tela, onde está a listagem de serviços cadastrados.
   - Como fazer: Escolha o serviço desejado (ex: **Assentamento**) na lista de serviços.
   - Resultado esperado: O serviço selecionado é adicionado à ordem de serviço.

4. **Especificar Acompanhamento de Obra**
   - Localização: Campo de acompanhamento de obra na tela de criação de ordem de serviço.
   - Como fazer: Se necessário, especifique o acompanhamento de obra, que cria um relacionamento com a estrutura de engenharia.
   - Observações importantes: Este campo só aparecerá se houver acompanhamento de obra.
   - Resultado esperado: O acompanhamento de obra é definido, se aplicável.

5. **Definir Quantidade e Etapas**
   - Localização: Campo para definição de quantidade dentro da etapa.
   - Como fazer: Insira a quantidade de serviços a serem realizados na etapa correspondente.
   - Resultado esperado: A quantidade é registrada na ordem de serviço.

6. **Salvar Informações**
   - Localização: Botão **"Salvar"** na parte inferior da tela.
   - Como fazer: Após preencher todos os campos necessários, clique em **"Salvar"**.
   - Resultado esperado: As informações da ordem de serviço são salvas no sistema.

7. **Definir Forma de Pagamento**
   - Localização: Tela de definição de forma de pagamento após salvar.
   - Como fazer: Escolha a forma de pagamento entre as opções disponíveis:
     * **À vista**: Insira o valor e, se aplicável, um desconto.
     * **Parcelado**: Defina o número de parcelas (ex: 10 vezes) e condições de pagamento.
   - Observações importantes: As opções de pagamento são semelhantes às vistas nas ordens de compra.
   - Resultado esperado: A forma de pagamento é definida corretamente.

**Campos e Parâmetros:**

| Campo                | Tipo         | Obrigatório | Descrição                                           | Exemplo                  |
|----------------------|--------------|-------------|----------------------------------------------------|--------------------------|
| Prestador            | Dropdown     | Sim         | Seleção do prestador de serviços                    | Edivaldo                 |
| Centro de Custo      | Dropdown     | Sim         | Seleção do centro de custo relacionado à obra      | Vila Real                |
| Serviço              | Dropdown     | Sim         | Seleção do serviço a ser prestado                  | Assentamento             |
| Quantidade           | Numérico     | Sim         | Quantidade de serviços a serem realizados           | 10                       |
| Forma de Pagamento    | Dropdown     | Sim         | Seleção da forma de pagamento                        | À vista, Parcelado       |
| Descrição            | Texto livre  | Não         | Descrição adicional sobre a ordem de serviço        | Execução de assentamento  |
| Data Inicial         | Data         | Não         | Data de início do serviço                           | 01/11/2023               |
| Data Final           | Data         | Não         | Data de término do serviço                          | 30/11/2023               |

**Regras de Negócio:**
- O prestador deve estar cadastrado no sistema para ser selecionado.
- O centro de custo deve estar vinculado a uma obra existente.
- A forma de pagamento deve ser definida antes do lançamento financeiro.
- O valor da ordem de serviço pode ser alterado após a seleção inicial.

**Observações Importantes:**
- Verifique se todos os campos obrigatórios estão preenchidos antes de salvar.
- Evite selecionar serviços que não estão relacionados ao prestador escolhido.
- Caso o botão **"Salvar"** esteja desabilitado, revise os campos obrigatórios.

**Conceitos-Chave:**
- **Ordem de Serviço**: Documento que formaliza a contratação de serviços.
- **Centro de Custo**: Categoria que agrupa despesas relacionadas a uma obra específica.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                     | Solução                                      | Prevenção                                  |
|-----------------------------------|------------------------------------|----------------------------------------------|--------------------------------------------|
| Botão **"Salvar"** desabilitado   | Campos obrigatórios não preenchidos | Preencha todos os campos obrigatórios       | Revise os campos antes de tentar salvar    |
| Prestador não encontrado           | Prestador não cadastrado           | Adicione o prestador ao sistema             | Verifique a lista de prestadores cadastrados|
| Valor não atualizado               | Alterações não salvas              | Salve as alterações antes de prosseguir     | Sempre salve após alterações                |

**💡 DICAS E BOAS PRÁTICAS:**
- Utilize a descrição para detalhar o serviço prestado.
- Sempre verifique as datas para evitar conflitos de agendamento.
- Mantenha a lista de prestadores atualizada para facilitar a seleção.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Criação de Ordem de Serviço para Assentamento**
```
Situação: Contratação de Edivaldo para assentamento na obra Vila Real.
Ação: 
  • Campo Prestador: "Edivaldo"
  • Campo Centro de Custo: "Vila Real"
  • Campo Serviço: "Assentamento"
  • Campo Quantidade: "10"
Resultado: Ordem de serviço criada e salva com sucesso.
```

**Exemplo 2: Criação de Ordem de Serviço com Pagamento Parcelado**
```
Situação: Contratação de prestador para serviços de pintura.
Ação: 
  • Campo Prestador: "Maria"
  • Campo Centro de Custo: "Centro Comercial"
  • Campo Serviço: "Pintura"
  • Campo Quantidade: "5"
  • Forma de Pagamento: "Parcelado em 5 vezes"
Resultado: Ordem de serviço criada com forma de pagamento definida.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O prestador e o centro de custo devem estar cadastrados no sistema.
- **Habilita:** O lançamento financeiro da ordem de serviço após a criação.
- **Relacionado a:** Módulo de Finanças para o lançamento de notas fiscais.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como criar uma ordem de serviço?"
- **Com problema:** "Não consigo criar uma ordem de serviço, o que fazer?"
- **Informal:** "Como faço para contratar um prestador?"
- **Por sintoma:** "O que fazer se o botão de salvar não está funcionando?"
- **Com dúvida:** "Quais campos preciso preencher para criar uma ordem de serviço?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Criar ordem de serviço", "Adicionar ordem de serviço", "Cadastrar ordem de serviço", "Formalizar serviço"
- "Prestador", "Fornecedor", "Contratado"
- "Centro de custo", "Categoria de despesa", "Grupo de custo"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como criar uma ordem de serviço?
- Quais informações são necessárias para a criação de uma ordem de serviço?
- O que fazer se o prestador não estiver na lista?
- O que fazer se o botão de salvar não estiver habilitado?
- O que preciso ter cadastrado antes de criar uma ordem de serviço?

---


---


---

## 11. Cadastro de Parceiros e Formas de Pagamento Antecipado

**📋 METADADOS:**
- **ID:** sec_11
- **⏱️ Minutagem:** 25:07 → 27:39
- **⏲️ Duração:** 152s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/qFzqzIoiVE4?si=YoVxiJOkipNVbQWb&t=1507)
- **📦 Módulo:** Financeiro
- **🏷️ Categorias:** Cadastro, Financeiro, Operacional
- **🔑 Palavras-chave:** cadastro de parceiros, formas de pagamento, pagamento antecipado, contas a pagar, fornecedores

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de cadastro de parceiros e a configuração de formas de pagamento antecipado no sistema, abordando como gerar contas a pagar antes do lançamento da nota e evitando duplicações financeiras.

**Contexto:**
Estamos na aba de cadastro de parceiros dentro do módulo financeiro do sistema, onde é possível registrar fornecedores, prestadores de serviço, imobiliárias e transportadoras, além de configurar as formas de pagamento, incluindo o pagamento antecipado.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Financeiro > Aba de Parceiros
- Tela/interface específica: Tela de Cadastro de Parceiros

**Funcionalidade Detalhada:**

O sistema permite o cadastro de parceiros, que podem ser fornecedores, prestadores de serviço, imobiliárias ou transportadoras. O cadastro pode ser feito manualmente ou através da importação de uma planilha. Além disso, a funcionalidade de pagamento antecipado gera uma conta a pagar antes mesmo do lançamento da nota, evitando duplicações financeiras.

### 🔹 Passo a Passo Detalhado:

1. **Iniciar Cadastro de Novo Parceiro**
   - Localização: Tela de Cadastro de Parceiros
   - Como fazer: Clique no botão **"Mais Novo Parceiro"**.
   - Campos/Opções disponíveis:
     * `CNPJ ou CPF`: Campo obrigatório para identificação do parceiro, dependendo se é pessoa jurídica ou física.
     * `Nome Fantasia`: Campo obrigatório que identifica o parceiro de forma comercial.
     * `Razão Social`: Campo obrigatório que identifica legalmente o parceiro.
   - Resultado esperado: O parceiro é cadastrado com os dados fornecidos.

2. **Preencher Informações Adicionais**
   - Localização: Após selecionar um parceiro já cadastrado, clique em **"Editar"**.
   - Como fazer: Preencha os campos adicionais, como **e-mail**, que é importante para processos automáticos.
   - Observações importantes: O e-mail do fornecedor é crucial para que o sistema possa direcionar comunicações e processos automáticos.
   - Resultado esperado: As informações do parceiro são atualizadas com sucesso.

3. **Configurar Forma de Pagamento Antecipado**
   - Localização: Na seção de formas de pagamento, selecione a opção de pagamento antecipado.
   - Como fazer: Preencha os campos de **desconto**, **vencimento** e **forma de pagamento**.
   - Campos/Opções disponíveis:
     * `Desconto`: Campo que permite inserir um valor ou percentual de desconto.
     * `Vencimento`: Data em que o pagamento deve ser realizado.
     * `Forma de Pagamento`: Opções como transferência bancária, cartão de crédito, etc.
   - Resultado esperado: Uma conta a pagar é gerada antes do lançamento da nota, registrada como um crédito.

4. **Salvar Informações**
   - Localização: Após preencher todos os campos necessários, clique no botão **"Salvar"**.
   - Como fazer: Confirme as informações e clique novamente em **"Salvar"** para formalizar a ordem de serviço.
   - Resultado esperado: A ordem de serviço é formalizada e as informações são salvas no sistema.

**Campos e Parâmetros:**

| Campo                | Tipo        | Obrigatório | Descrição                                          | Exemplo                |
|----------------------|-------------|-------------|---------------------------------------------------|------------------------|
| CNPJ ou CPF          | Texto       | Sim         | Identificação do parceiro, dependendo do tipo.    | "12.345.678/0001-90"   |
| Nome Fantasia        | Texto       | Sim         | Nome comercial do parceiro.                        | "Fornecedor XYZ"       |
| Razão Social         | Texto       | Sim         | Nome legal do parceiro.                           | "XYZ Comércio Ltda."   |
| E-mail               | Texto       | Não         | E-mail para comunicação e processos automáticos.  | "contato@xyz.com"      |
| Desconto             | Numérico    | Não         | Valor ou percentual de desconto a ser aplicado.   | "10" (ou "10%")        |
| Vencimento           | Data        | Sim         | Data de vencimento do pagamento.                   | "30/11/2023"           |
| Forma de Pagamento    | Dropdown    | Sim         | Método de pagamento a ser utilizado.              | "Transferência"        |

**Regras de Negócio:**
- O cadastro de parceiros requer o preenchimento dos campos **CNPJ ou CPF**, **Nome Fantasia** e **Razão Social**.
- O e-mail do fornecedor é necessário para processos automáticos.
- O pagamento antecipado gera uma conta a pagar antes do lançamento da nota, evitando duplicações.

**Observações Importantes:**
- É recomendável preencher o e-mail do fornecedor para facilitar a comunicação.
- Evite deixar campos obrigatórios em branco, pois isso pode impedir o cadastro.
- Verifique se o CNPJ ou CPF está correto para evitar erros no cadastro.

**Conceitos-Chave:**
- **Pagamento Antecipado**: Forma de pagamento onde a conta a pagar é gerada antes do lançamento da nota, registrada como um crédito.
- **Cadastro de Parceiros**: Processo de registrar fornecedores e prestadores de serviço no sistema.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                       | Solução                                          | Prevenção                                   |
|-----------------------------------|--------------------------------------|-------------------------------------------------|---------------------------------------------|
| Erro ao salvar parceiro            | Campos obrigatórios não preenchidos  | Verifique e preencha todos os campos obrigatórios. | Sempre revisar os campos antes de salvar.  |
| Conta a pagar não gerada           | Forma de pagamento não configurada   | Certifique-se de que a forma de pagamento antecipado está selecionada. | Configurar corretamente as opções de pagamento. |
| E-mail do fornecedor não enviado   | Campo de e-mail vazio                | Preencha o campo de e-mail antes de salvar.    | Sempre incluir o e-mail ao cadastrar fornecedores. |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre verifique a validade do CNPJ ou CPF antes de cadastrar.
- Utilize a importação de planilhas para cadastrar múltiplos parceiros de uma vez.
- Mantenha os dados dos parceiros atualizados para evitar problemas futuros.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Cadastro de Fornecedor**
```
Situação: Cadastrar um novo fornecedor.
Ação: 
  • Campo CNPJ: "12.345.678/0001-90"
  • Campo Nome Fantasia: "Fornecedor XYZ"
  • Campo Razão Social: "XYZ Comércio Ltda."
Resultado: O fornecedor é cadastrado com sucesso e pode ser utilizado nas transações financeiras.
```

**Exemplo 2: Configuração de Pagamento Antecipado**
```
Situação: Configurar um pagamento antecipado para um serviço.
Ação: 
  • Campo Desconto: "10%"
  • Campo Vencimento: "30/11/2023"
  • Campo Forma de Pagamento: "Transferência"
Resultado: Uma conta a pagar é gerada antes do lançamento da nota, registrada como um crédito.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O módulo financeiro deve estar habilitado e configurado.
- **Habilita:** A geração de contas a pagar e a formalização de ordens de serviço.
- **Relacionado a:** Módulo de Contas a Pagar, Módulo de Relatórios Financeiros.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como cadastrar um parceiro?"
- **Com problema:** "Não consigo cadastrar um fornecedor, o que fazer?"
- **Informal:** "Como coloco um fornecedor no sistema?"
- **Por sintoma:** "Por que minha conta a pagar não aparece?"
- **Com variação:** "Como faço para configurar um pagamento antecipado?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Cadastrar fornecedor", "Adicionar parceiro", "Novo parceiro", "Registro de fornecedor"
- "Pagamento antecipado", "Conta a pagar antecipada", "Pagamento prévio"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como cadastrar um novo parceiro no sistema?
- Quais campos são obrigatórios para o cadastro de fornecedores?
- Como configurar uma forma de pagamento antecipado?
- O que fazer se a conta a pagar não for gerada?
- O que preciso ter antes de cadastrar um parceiro?

---


---


---

## 12. Cadastro de Parceiros no Sistema

**📋 METADADOS:**
- **ID:** sec_12
- **⏱️ Minutagem:** 27:37 → 30:10
- **⏲️ Duração:** 152s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/qFzqzIoiVE4?si=YoVxiJOkipNVbQWb&t=1657)
- **📦 Módulo:** Cadastro de Fornecedores e Parceiros
- **🏷️ Categorias:** Cadastro, Configuração, Relacionamento, Operacional
- **🔑 Palavras-chave:** cadastro de parceiros, fornecedor, prestador de serviço, transportadora, imobiliária

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de cadastro de parceiros no sistema, permitindo que usuários definam contatos, informações bancárias e categorias de produtos, facilitando a gestão de fornecedores e prestadores de serviços.

**Contexto:**
Estamos na seção de cadastro de parceiros do sistema, onde é possível registrar informações detalhadas sobre fornecedores, prestadores de serviços, transportadoras e imobiliárias. O objetivo é garantir que todos os dados relevantes sejam coletados para facilitar a comunicação e a gestão de compras.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Cadastro de Fornecedores e Parceiros > Submenu Cadastro de Parceiros
- Tela/interface específica: Tela de Cadastro de Parceiros

**Funcionalidade Detalhada:**
A funcionalidade de cadastro de parceiros permite que o usuário registre informações essenciais sobre cada parceiro comercial. Isso inclui a definição de contatos específicos, informações bancárias e categorias de produtos que o parceiro fornece. O sistema utiliza essas informações para otimizar processos de cotação e compras.

### 🔹 Passo a Passo Detalhado:

1. **Cadastro de Contato**
   - Localização: Tela de Cadastro de Parceiros, seção "Contato"
   - Como fazer: Clique na opção "Adicionar Contato" e preencha os campos necessários.
   - Campos/Opções disponíveis:
     * `Nome do Contato`: Campo de texto (obrigatório) - Nome do vendedor ou responsável pelo contato.
     * `Email`: Campo de texto (opcional) - Email do contato para envio de orçamentos.
   - Resultado esperado: O contato é salvo e associado ao parceiro, permitindo comunicação direta.

2. **Cadastro de Filiais**
   - Localização: Tela de Cadastro de Parceiros, seção "Filiais"
   - Como fazer: Clique em "Adicionar Filial" e preencha os campos solicitados.
   - Campos/Opções disponíveis:
     * `CNPJ`: Campo de texto (obrigatório) - Cadastro Nacional da Pessoa Jurídica da filial.
     * `Telefone`: Campo de texto (opcional) - Número de telefone da filial.
     * `Endereço`: Campo de texto (obrigatório) - Endereço completo da filial.
     * `Email`: Campo de texto (opcional) - Email da filial.
   - Resultado esperado: As informações da filial são registradas e podem ser visualizadas no cadastro do parceiro.

3. **Cadastro de Dados Bancários**
   - Localização: Tela de Cadastro de Parceiros, seção "Dados Bancários"
   - Como fazer: Clique em "Adicionar Dados Bancários" e preencha os campos necessários.
   - Campos/Opções disponíveis:
     * `Banco`: Campo de seleção (obrigatório) - Selecione o banco onde a conta está registrada.
     * `Agência`: Campo de texto (obrigatório) - Número da agência bancária.
     * `Conta`: Campo de texto (obrigatório) - Número da conta bancária.
     * `Chave Pix`: Campo de texto (opcional) - Chave para transações via Pix.
   - Resultado esperado: As informações bancárias são salvas e utilizadas para pagamentos futuros.

4. **Definição do Tipo de Parceiro**
   - Localização: Tela de Cadastro de Parceiros, seção "Tipo de Parceiro"
   - Como fazer: Clique em "Selecionar Tipo" e escolha entre as opções disponíveis.
   - Observações importantes: O tipo de parceiro pode ser "Fornecedor", "Prestador de Serviço", "Transportadora" ou "Imobiliária". A escolha do tipo influencia as categorias de produtos disponíveis.
   - Resultado esperado: O tipo de parceiro é definido, permitindo que o sistema ajuste as opções de categorias de produtos.

5. **Cadastro de Categorias de Produtos**
   - Localização: Tela de Cadastro de Parceiros, seção "Categorias de Produtos"
   - Como fazer: Após selecionar "Fornecedor", clique em "Adicionar Categoria" e escolha as categorias relevantes.
   - Campos/Opções disponíveis:
     * `Categoria`: Campo de seleção (obrigatório) - Selecione as categorias que o fornecedor atende, como "Hidráulica" ou "Elétrica".
   - Resultado esperado: As categorias são registradas, permitindo que o sistema filtre fornecedores durante o processo de cotação.

**Campos e Parâmetros:**

| Campo                | Tipo           | Obrigatório | Descrição                                           | Exemplo                   |
|----------------------|----------------|-------------|-----------------------------------------------------|---------------------------|
| Nome do Contato      | Texto          | Sim         | Nome do responsável pelo contato.                   | João Silva                |
| Email                | Texto          | Não         | Email para comunicação.                              | joao@exemplo.com          |
| CNPJ                 | Texto          | Sim         | Cadastro Nacional da Pessoa Jurídica.               | 12.345.678/0001-90        |
| Telefone             | Texto          | Não         | Número de telefone da filial.                        | (11) 91234-5678           |
| Endereço             | Texto          | Sim         | Endereço completo da filial.                         | Rua Exemplo, 123          |
| Banco                | Seleção        | Sim         | Banco onde a conta está registrada.                 | Banco do Brasil           |
| Agência              | Texto          | Sim         | Número da agência bancária.                          | 1234                       |
| Conta                | Texto          | Sim         | Número da conta bancária.                            | 56789-0                   |
| Chave Pix            | Texto          | Não         | Chave para transações via Pix.                       | joao@exemplo.com          |
| Tipo de Parceiro     | Seleção        | Sim         | Tipo de parceiro (Fornecedor, Prestador, etc.).     | Fornecedor                |
| Categoria            | Seleção        | Sim         | Categoria de produtos fornecidos.                   | Hidráulica                |

**Regras de Negócio:**
- O campo `Nome do Contato` é obrigatório para que o parceiro possa ser cadastrado.
- O tipo de parceiro deve ser definido como "Fornecedor" para que as categorias de produtos sejam exibidas.
- As informações bancárias são necessárias para processar pagamentos via Pix ou depósito.

**Observações Importantes:**
- Certifique-se de que todos os campos obrigatórios estejam preenchidos antes de salvar o cadastro.
- Verifique se o CNPJ informado é válido para evitar erros no cadastro.
- É recomendável manter os dados de contato atualizados para facilitar a comunicação.

**Conceitos-Chave:**
- **Fornecedor**: Entidade que fornece produtos ou serviços para a empresa.
- **Prestador de Serviço**: Entidade que oferece serviços, mas não produtos físicos.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                       | Solução                                           | Prevenção                                      |
|-----------------------------------|--------------------------------------|--------------------------------------------------|------------------------------------------------|
| Cadastro não salva                 | Campos obrigatórios não preenchidos  | Preencha todos os campos obrigatórios e tente novamente. | Verifique os campos antes de salvar.          |
| CNPJ inválido                     | CNPJ digitado incorretamente         | Confirme o CNPJ e digite novamente.              | Utilize um validador de CNPJ.                 |
| Dados bancários não aparecem      | Tipo de parceiro não definido como "Fornecedor" | Altere o tipo de parceiro e adicione as categorias. | Defina corretamente o tipo de parceiro.       |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre mantenha um registro atualizado dos contatos para facilitar a comunicação.
- Utilize categorias específicas para otimizar o processo de cotação.
- Revise os dados bancários periodicamente para evitar problemas em pagamentos.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Cadastro de um Fornecedor**
```
Situação: Cadastro do fornecedor "Lerói Merlin".
Ação: 
  • Nome do Contato: "João Silva"
  • Email: "joao@leroi.com"
  • CNPJ: "12.345.678/0001-90"
  • Telefone: "(11) 91234-5678"
  • Endereço: "Rua Exemplo, 123"
  • Banco: "Banco do Brasil"
  • Agência: "1234"
  • Conta: "56789-0"
  • Chave Pix: "joao@leroi.com"
  • Tipo de Parceiro: "Fornecedor"
  • Categoria: "Hidráulica"
Resultado: O fornecedor é cadastrado com sucesso e aparece nas opções de cotação.
```

**Exemplo 2: Cadastro de um Prestador de Serviço**
```
Situação: Cadastro do prestador "Serviços de Limpeza".
Ação: 
  • Nome do Contato: "Maria Oliveira"
  • Email: "maria@limpeza.com"
  • CNPJ: "98.765.432/0001-01"
  • Telefone: "(11) 99876-5432"
  • Endereço: "Avenida Exemplo, 456"
  • Tipo de Parceiro: "Prestador de Serviço"
Resultado: O prestador é cadastrado e pode ser selecionado para serviços.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O usuário deve ter permissões adequadas para cadastrar parceiros.
- **Habilita:** O cadastro de parceiros permite a realização de cotações e pedidos de compra.
- **Relacionado a:** Funcionalidades de compras e relatórios de fornecedores.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como cadastrar um parceiro?"
- **Com problema:** "Não consigo cadastrar um fornecedor, o que fazer?"
- **Informal:** "Como eu coloco um fornecedor no sistema?"
- **Por sintoma:** "O que fazer se o cadastro não está salvando?"
- **Com variação:** "Como adicionar um prestador de serviço?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Adicionar parceiro", "Cadastrar fornecedor", "Registrar prestador", "Inserir transportadora"
- "Cadastro de fornecedor", "Registro de parceiro", "Cadastro de prestador de serviço"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como cadastrar um parceiro no sistema?
- Quais informações são necessárias para cadastrar um fornecedor?
- O que fazer se o CNPJ não for aceito?
- Como corrigir um erro no cadastro de um parceiro?
- O que preciso ter antes de cadastrar um prestador de serviço?

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
- **🏷️ Categorias:** Cadastro, Relatório, Operacional
- **🔑 Palavras-chave:** cadastro de serviço, categoria, unidade de medida, ordem de serviço, grupo de parceiros

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de cadastro de serviços no sistema, incluindo a definição de categorias e unidades de medida, além de como esses serviços podem ser utilizados em relatórios e ordens de serviço.

**Contexto:**
Estamos na aba de serviços do sistema, onde o usuário pode cadastrar novos serviços que serão utilizados em ordens de serviço e relatórios financeiros. O objetivo é permitir que o usuário organize e categorize serviços de forma eficiente.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Serviços > Aba Cadastro de Serviços
- Tela/interface específica: Tela de Cadastro de Serviços

**Funcionalidade Detalhada:**
A funcionalidade de cadastro de serviços permite que o usuário registre novos serviços que serão utilizados em ordens de serviço e relatórios. O cadastro inclui a definição do nome do serviço, unidade de medida, categoria e outras informações relevantes, como descrições e orientações.

### 🔹 Passo a Passo Detalhado:

1. **Cadastrar Novo Serviço**
   - Localização: Aba de Cadastro de Serviços, botão **+ Serviço**
   - Como fazer: Clique no botão **+ Serviço** para iniciar o cadastro de um novo serviço.
   - Campos/Opções disponíveis:
     * `Nome do Serviço`: Campo de texto onde o usuário deve inserir o nome do serviço a ser cadastrado.
     * `Unidade de Medida`: Dropdown onde o usuário seleciona a unidade de medida pela qual o serviço será controlado (ex: horas, metros quadrados).
     * `Categoria`: Dropdown onde o usuário deve escolher uma categoria que agrupe serviços com o mesmo intuito (ex: pintura e revestimento).
   - Resultado esperado: O serviço é cadastrado e fica disponível para uso em ordens de serviço e relatórios.

2. **Definir Categoria do Serviço**
   - Localização: Durante o cadastro do serviço, no campo **Categoria**.
   - Como fazer: Selecione a categoria apropriada para o serviço no dropdown. Se a categoria desejada não estiver disponível, o usuário pode criar uma nova categoria.
   - Observações importantes: As categorias são utilizadas para facilitar a localização de serviços e produtos durante o processo de compras e financeiro.
   - Resultado esperado: A categoria é vinculada ao serviço cadastrado, permitindo filtragens futuras.

3. **Adicionar Descrição e Orientações**
   - Localização: Campo **Descrição** na tela de cadastro de serviços.
   - Como fazer: Insira uma descrição detalhada do serviço e quaisquer orientações que possam ser relevantes para sua execução.
   - Resultado esperado: A descrição e orientações são salvas junto com o serviço, proporcionando informações adicionais para usuários futuros.

4. **Salvar o Serviço**
   - Localização: Botão **Salvar** na parte inferior da tela de cadastro.
   - Como fazer: Após preencher todos os campos necessários, clique no botão **Salvar** para finalizar o cadastro do serviço.
   - Resultado esperado: O serviço é salvo no sistema e pode ser utilizado em outras áreas, como ordens de serviço e relatórios financeiros.

**Campos e Parâmetros:**

| Campo               | Tipo        | Obrigatório | Descrição                                               | Exemplo                     |
|---------------------|-------------|-------------|---------------------------------------------------------|-----------------------------|
| Nome do Serviço     | Texto       | Sim         | Nome que identifica o serviço cadastrado.               | "Pintura de Parede"        |
| Unidade de Medida   | Dropdown    | Sim         | Unidade pela qual o serviço será controlado.            | "Horas", "Metros Quadrados"|
| Categoria           | Dropdown    | Sim         | Agrupamento do serviço para facilitar a localização.    | "Pintura e Revestimento"   |
| Descrição           | Texto       | Não         | Informações adicionais sobre o serviço.                 | "Serviço de pintura interna."|

**Regras de Negócio:**
- O cadastro de serviços deve incluir obrigatoriamente um nome, uma unidade de medida e uma categoria.
- As categorias podem ser pré-definidas ou novas, dependendo da necessidade do usuário.
- O serviço cadastrado deve ser utilizado em relatórios e ordens de serviço.

**Observações Importantes:**
- É importante verificar se a categoria desejada já existe antes de criar uma nova.
- Evite usar nomes genéricos para serviços, pois isso pode dificultar a localização futura.

**Conceitos-Chave:**
- **Unidade de Medida**: Refere-se à medida pela qual o serviço é controlado, como horas ou metros quadrados.
- **Categoria**: Agrupamento de serviços com o mesmo intuito, facilitando a busca e organização.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                             | Causa Provável                     | Solução                                         | Prevenção                                   |
|--------------------------------------|------------------------------------|------------------------------------------------|---------------------------------------------|
| Não consigo salvar o serviço         | Campos obrigatórios não preenchidos| Verifique se todos os campos obrigatórios estão preenchidos. | Sempre revisar os campos antes de salvar.  |
| Categoria não aparece no dropdown    | Categoria não cadastrada           | Cadastre a nova categoria antes de tentar vincular. | Cadastrar categorias previamente.           |
| Serviço não aparece em relatórios    | Serviço não foi salvo corretamente | Verifique se o serviço foi salvo e se a categoria está correta. | Confirmar o salvamento após cadastro.      |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre utilize nomes descritivos para serviços para facilitar a identificação.
- Utilize as categorias de forma consistente para melhorar a organização dos serviços.
- Revise as orientações e descrições para garantir que sejam claras e úteis.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Cadastro de Serviço de Pintura**
```
Situação: O usuário deseja cadastrar um serviço de pintura.
Ação: 
  • Campo Nome do Serviço: "Pintura de Parede"
  • Campo Unidade de Medida: "Horas"
  • Campo Categoria: "Pintura e Revestimento"
Resultado: O serviço "Pintura de Parede" é cadastrado e pode ser utilizado em ordens de serviço.
```

**Exemplo 2: Cadastro de Serviço de Revestimento**
```
Situação: O usuário deseja cadastrar um serviço de revestimento.
Ação: 
  • Campo Nome do Serviço: "Revestimento de Piso"
  • Campo Unidade de Medida: "Metros Quadrados"
  • Campo Categoria: "Pintura e Revestimento"
Resultado: O serviço "Revestimento de Piso" é cadastrado e pode ser utilizado em relatórios financeiros.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O usuário deve ter permissões adequadas para cadastrar serviços.
- **Habilita:** O serviço cadastrado pode ser utilizado em ordens de serviço e relatórios financeiros.
- **Relacionado a:** Funcionalidade de relatórios financeiros e gerenciamento de ordens de serviço.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como cadastrar um serviço?"
- **Com problema:** "Não consigo cadastrar um serviço, o que fazer?"
- **Informal:** "Como eu coloco um serviço no sistema?"
- **Por sintoma:** "O que fazer se o serviço não aparece nos relatórios?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Adicionar serviço", "Criar serviço", "Registrar serviço", "Cadastrar novo serviço"
- "Grupo de serviços", "Categoria de serviços"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como faço para cadastrar um novo serviço?
- Quais campos são obrigatórios no cadastro de serviços?
- O que fazer se a categoria desejada não estiver disponível?
- O que fazer se o serviço não aparecer nos relatórios?
- O que preciso ter feito antes de cadastrar um serviço?

---


---


---

## 14. Cadastro e Vínculo de Lojas no Grupo de Parceiros

**📋 METADADOS:**
- **ID:** sec_14
- **⏱️ Minutagem:** 32:39 → 34:28
- **⏲️ Duração:** 109s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/qFzqzIoiVE4?si=YoVxiJOkipNVbQWb&t=1959)
- **📦 Módulo:** Compras
- **🏷️ Categorias:** Configuração, Cadastro, Relatório
- **🔑 Palavras-chave:** cadastro de loja, grupo de parceiros, CNPJ, ordem de compra, crédito financeiro

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de cadastro de lojas como parceiros em um sistema, abordando a criação de grupos de parceiros e a importância do vínculo entre lojas com CNPJs diferentes, especialmente em situações de compras e entregas.

**Contexto:**
Estamos no módulo de Compras do sistema, onde o objetivo é cadastrar diferentes lojas que fazem parte da mesma rede, mas possuem CNPJs distintos. Este cadastro é crucial para garantir que as ordens de compra e os créditos financeiros sejam geridos corretamente.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Compras > Grupo de Parceiros
- Tela/interface específica: Tela de Cadastro de Grupo de Parceiros

**Funcionalidade Detalhada:**
A funcionalidade permite que o usuário cadastre cada loja como um parceiro distinto, mesmo que todas façam parte da mesma rede. Isso é importante para a gestão de ordens de compra e créditos financeiros, pois cada loja pode ter um CNPJ diferente. O sistema permite que, ao cadastrar um grupo de parceiros, o usuário vincule essas lojas, facilitando a gestão de compras e a visualização de créditos.

### 🔹 Passo a Passo Detalhado:

1. **Cadastrar Lojas como Parceiros**
   - Localização: Menu Principal > Módulo Compras > Cadastro de Lojas
   - Como fazer: Acesse a tela de cadastro de lojas e insira os dados de cada loja, incluindo nome e CNPJ.
   - Campos/Opções disponíveis:
     * `Nome da Loja`: Campo de texto, obrigatório, onde você insere o nome da loja.
     * `CNPJ`: Campo numérico, obrigatório, onde você insere o CNPJ da loja.
   - Resultado esperado: A loja é cadastrada como um parceiro no sistema, permitindo a criação de ordens de compra.

2. **Criar um Novo Grupo de Parceiros**
   - Localização: Menu Principal > Módulo Compras > Grupo de Parceiros
   - Como fazer: Clique no botão **"Mais Novo Grupo"** para iniciar o cadastro de um novo grupo.
   - Observações importantes: Certifique-se de que todas as lojas que deseja vincular já estejam cadastradas como parceiros.
   - Resultado esperado: Um novo grupo de parceiros é criado, permitindo a vinculação de lojas.

3. **Definir Nome do Grupo**
   - Localização: Tela de Cadastro de Grupo de Parceiros
   - Como fazer: No campo **"Nome do Grupo"**, insira um nome que identifique o grupo de lojas, como "Casas d'Água - Rede".
   - Resultado esperado: O nome do grupo é salvo e associado às lojas que serão vinculadas.

4. **Vincular Lojas ao Grupo**
   - Localização: Tela de Cadastro de Grupo de Parceiros
   - Como fazer: Clique na **mãozinha** (ícone de seleção) ao lado de cada loja que deseja adicionar ao grupo e, em seguida, clique em **"Salvar"**.
   - Resultado esperado: As lojas selecionadas são vinculadas ao grupo de parceiros, permitindo uma gestão unificada.

**Campos e Parâmetros:**

| Campo               | Tipo       | Obrigatório | Descrição                                      | Exemplo              |
|---------------------|------------|-------------|------------------------------------------------|----------------------|
| Nome da Loja        | Texto      | Sim         | Nome da loja a ser cadastrada                  | "Loja Biguaçu"      |
| CNPJ                | Numérico   | Sim         | CNPJ da loja a ser cadastrada                  | "12.345.678/0001-90" |
| Nome do Grupo       | Texto      | Sim         | Nome do grupo de parceiros a ser criado        | "Grupo Casas d'Água" |

**Regras de Negócio:**
- Cada loja deve ser cadastrada com um CNPJ distinto.
- Não é permitido criar uma ordem de compra com uma loja e lançar a nota de outra, a menos que as lojas façam parte do mesmo grupo de parceiros.
- Os créditos financeiros gerados para uma loja influenciam as demais lojas do grupo.

**Observações Importantes:**
- Ao cadastrar as lojas, verifique se os CNPJs estão corretos para evitar divergências.
- Erros comuns incluem tentar vincular lojas que não estão cadastradas como parceiros.
- É importante entender que o vínculo entre as lojas facilita a gestão de compras e créditos.

**Conceitos-Chave:**
- **Grupo de Parceiros**: Conjunto de lojas que podem ser geridas em conjunto, facilitando a gestão de compras e créditos.
- **CNPJ**: Cadastro Nacional da Pessoa Jurídica, utilizado para identificar as lojas no sistema.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                                    | Causa Provável                       | Solução                                   | Prevenção                               |
|---------------------------------------------|-------------------------------------|-------------------------------------------|-----------------------------------------|
| Não é possível salvar o grupo de parceiros  | Lojas não cadastradas como parceiros | Verifique se todas as lojas estão cadastradas | Cadastrar todas as lojas antes de criar o grupo |
| Divergência na ordem de compra              | Lojas com CNPJs diferentes          | Certifique-se de que as lojas estão no mesmo grupo | Criar grupos de parceiros corretamente  |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre verifique os CNPJs antes de cadastrar as lojas.
- Utilize nomes descritivos para os grupos de parceiros para facilitar a identificação.
- Evite criar grupos com lojas que não têm relação entre si.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Cadastro de Lojas**
```
Situação: Você precisa cadastrar a loja "Loja Biguaçu".
Ação: 
  • Nome da Loja: "Loja Biguaçu"
  • CNPJ: "12.345.678/0001-90"
Resultado: A loja "Loja Biguaçu" é cadastrada com sucesso.
```

**Exemplo 2: Criação de Grupo de Parceiros**
```
Situação: Criar um grupo para as lojas "Loja Biguaçu" e "Loja São José".
Ação: 
  • Nome do Grupo: "Grupo Casas d'Água"
  • Selecionar Lojas: "Loja Biguaçu" e "Loja São José"
Resultado: O grupo "Grupo Casas d'Água" é criado e as lojas são vinculadas.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** As lojas devem estar cadastradas como parceiros antes de criar um grupo.
- **Habilita:** A gestão unificada de compras e créditos financeiros entre as lojas do grupo.
- **Relacionado a:** Módulo de Vendas, onde as ordens de compra são geridas.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como cadastrar uma loja como parceiro?"
- **Com problema:** "Não consigo vincular lojas, o que fazer?"
- **Informal:** "Como faço para juntar as lojas?"
- **Por sintoma:** "Quando tento criar um grupo, não aparece a loja."

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Adicionar loja", "Criar grupo de lojas", "Vincular lojas", "Cadastro de parceiros"
- "CNPJ", "Cadastro de loja", "Grupo de parceiros"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como cadastrar uma loja como parceiro?
- O que fazer se não consigo salvar o grupo de parceiros?
- Como vincular lojas em um grupo?
- O que fazer se houver divergência na ordem de compra?
- O que preciso ter cadastrado antes de criar um grupo de parceiros?

---


---




---


## 🎬 DADOS DE TIMESTAMPS (Para Sistema RAG)


[VIDEO_TIMESTAMPS_DATA]

{
  "Passo a passo - Módulo de Compras": [
    {
      "start": "00:00",
      "end": "02:33",
      "line": "Olá, o objetivo desse vídeo é realizarmos um treinamento completo do módulo de compras. Nosso primei"
    },
    {
      "start": "02:30",
      "end": "05:04",
      "line": "Basta ir arrastando pro lado e definindo as especificações. Agora aqui na lateral temos a questão do"
    },
    {
      "start": "05:01",
      "end": "07:34",
      "line": "podemos salvar a nossa solicitação. Clicando em salvar, temos a opção de salvar em rascunho, que é o"
    },
    {
      "start": "07:31",
      "end": "10:04",
      "line": "transferência. Em contrapartida, se tiver mais produtos, pode realizar uma única aprovação sem preci"
    },
    {
      "start": "10:02",
      "end": "12:34",
      "line": "recebem e preenchem essas cotações. Então, lembrando que é um fluxo que o seu parceiro vai fazer. Vo"
    },
    {
      "start": "12:32",
      "end": "15:04",
      "line": "eles, destinatário é onde você é responsável por buscar o produto, tanto que ele bloqueia o campo de"
    },
    {
      "start": "15:02",
      "end": "17:35",
      "line": "fornecedor por algum outro método, clicando nos três pontinhos, também é possível editar o orçamento"
    },
    {
      "start": "17:33",
      "end": "20:07",
      "line": "obrigatório que a sua ordem de compra seja aprovada. vai depender de uma validação interna por parte"
    },
    {
      "start": "20:04",
      "end": "22:39",
      "line": "Após essas definições, vamos salvar e a nota estará lançada. A nota é um dos lançamentos mais import"
    },
    {
      "start": "22:36",
      "end": "25:12",
      "line": "basicamente você irá criar a ordem para ter a formalização e em seguida lançar a nota no financeiro."
    },
    {
      "start": "25:07",
      "end": "27:39",
      "line": "dias, por exemplo, 15 e 30. E por fim, a forma de pagamento antecipado. Essa aqui é um pouco diferen"
    },
    {
      "start": "27:37",
      "end": "30:10",
      "line": "informações. Em próximo, a opção de contato. Nesse momento, você pode definir que, por exemplo, dent"
    },
    {
      "start": "30:08",
      "end": "32:42",
      "line": "que não há nenhum botão de adicionar diferente das outras a quais vimos anteriormente. Neste momento"
    },
    {
      "start": "32:39",
      "end": "34:28",
      "line": "Biguaçu, de Florianópolis e de São José. Neste caso, todas fazem parte da rede casas d'Água, porém c"
    }
  ]
}

[/VIDEO_TIMESTAMPS_DATA]
