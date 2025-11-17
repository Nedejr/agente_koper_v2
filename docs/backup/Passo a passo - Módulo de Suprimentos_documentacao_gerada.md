# 📚 Documentação: Passo a passo - Módulo de Suprimentos


[video:https://youtu.be/6vX7wYe8cIw?si=5Xf_VmLvM7bj6M73]


**🎥 Vídeo Original:** https://youtu.be/6vX7wYe8cIw?si=5Xf_VmLvM7bj6M73

**📊 Total de Seções:** 11

---

---

## 1. Módulo de Suplementos - Aba de Solicitações

**📋 METADADOS:**
- **ID:** sec_1
- **⏱️ Minutagem:** 00:00 → 02:34
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/6vX7wYe8cIw?si=5Xf_VmLvM7bj6M73&t=0)
- **📦 Módulo:** Suplementos
- **🏷️ Categorias:** Solicitações, Compras, Gestão de Suprimentos
- **🔑 Palavras-chave:** solicitações, produtos, especificações, obra, serviços

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de criação de solicitações de produtos no módulo de suplementos, permitindo que os usuários realizem pedidos iniciais e vinculem itens a obras específicas.

**Contexto:**
Estamos na aba de solicitações do módulo de suplementos, onde o objetivo é realizar pedidos iniciais para iniciar o fluxo de compras de produtos necessários para obras.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Suplementos > Aba Solicitações
- Tela/interface específica: Tela de Solicitações de Produtos

**Funcionalidade Detalhada:**
A aba de solicitações permite que os usuários realizem pedidos de produtos necessários para obras. Os usuários podem visualizar uma listagem de todos os produtos cadastrados e utilizar filtros para localizar itens específicos. Após encontrar o produto desejado, é possível definir suas especificações e vincular o pedido a uma obra, o que é crucial para o acompanhamento do fluxo de compras e comparativos entre o planejado e o executado.

### 🔹 Passo a Passo Detalhado:

1. **Acessar a Aba de Solicitações**
   - Localização: Menu Principal > Módulo Suplementos > Aba Solicitações
   - Como fazer: Clique na aba "Solicitações" para acessar a tela de pedidos.
   - Resultado esperado: A tela de solicitações é exibida, mostrando a listagem de produtos cadastrados.

2. **Criar Nova Solicitação**
   - Localização: Tela de Solicitações
   - Como fazer: Clique no botão **Mais Solicitação**.
   - Resultado esperado: Uma nova tela é aberta, permitindo visualizar todos os produtos já cadastrados.

3. **Buscar Produto**
   - Localização: Tela de listagem de produtos
   - Como fazer: Utilize os filtros de **Categoria**, **Subcategoria** ou a **Pesquisa Direta** para localizar o item desejado.
   - Campos/Opções disponíveis:
     * `Categoria`: Filtro para selecionar a categoria do produto.
     * `Subcategoria`: Filtro para selecionar a subcategoria do produto.
     * `Pesquisa Direta`: Campo de texto para busca direta pelo nome do produto.
   - Resultado esperado: A lista de produtos é filtrada de acordo com os critérios selecionados.

4. **Selecionar Produto**
   - Localização: Tela de listagem de produtos
   - Como fazer: Arraste o item desejado para o lado ou clique no ícone da **mãozinha** ao lado do produto.
   - Resultado esperado: A tela de especificações do produto é exibida.

5. **Definir Especificações do Produto**
   - Localização: Tela de Especificações do Produto
   - Como fazer: Preencha os campos de **Marcas**, **Parâmetros**, **Cores**, entre outros.
   - Campos/Opções disponíveis:
     * `Marca`: Campo para selecionar a marca do produto.
     * `Parâmetros`: Campo para definir parâmetros técnicos do produto.
     * `Cor`: Campo para selecionar a cor do produto.
   - Resultado esperado: As especificações do produto são definidas.

6. **Adicionar Quantidade**
   - Localização: Tela de Especificações do Produto
   - Como fazer: Insira a quantidade desejada no campo de **Quantidade** e clique em **Adicionar**.
   - Resultado esperado: O produto é adicionado à solicitação.

7. **Selecionar Local de Consumo**
   - Localização: Tela de Solicitações
   - Como fazer: No campo **Local de Consumo**, selecione a obra relacionada ao pedido.
   - Observações importantes: Se a obra já tiver um acompanhamento pronto dentro do módulo de engenharia, o sistema irá gerar comparativos entre o planejado e o executado.
   - Resultado esperado: A obra é vinculada à solicitação.

8. **Especificar Serviços**
   - Localização: Tela de Local de Consumo
   - Como fazer: Se a obra estiver completa, clique em **Especificar Serviços** para vincular os serviços de execução.
   - Resultado esperado: Uma tela é aberta para especificar os serviços relacionados ao produto.

9. **Salvar Solicitação**
   - Localização: Tela de Especificar Serviços
   - Como fazer: Após realizar os vínculos necessários, clique no botão **Salvar**.
   - Resultado esperado: A solicitação é salva no sistema.

**Campos e Parâmetros:**

| Campo                | Tipo       | Obrigatório | Descrição                                         | Exemplo               |
|----------------------|------------|-------------|---------------------------------------------------|-----------------------|
| `Categoria`          | Dropdown   | Sim         | Seleção da categoria do produto                   | Materiais de Construção|
| `Subcategoria`       | Dropdown   | Não         | Seleção da subcategoria do produto                 | Elétricos             |
| `Pesquisa Direta`    | Texto      | Não         | Campo para busca direta pelo nome do produto      | "Cimento"             |
| `Marca`              | Dropdown   | Sim         | Seleção da marca do produto                        | "Marca X"             |
| `Parâmetros`         | Texto      | Não         | Definição de parâmetros técnicos do produto        | "Resistente à água"    |
| `Cor`                | Dropdown   | Não         | Seleção da cor do produto                          | "Cinza"               |
| `Quantidade`         | Número     | Sim         | Quantidade do produto a ser solicitada            | 100                   |
| `Local de Consumo`   | Dropdown   | Sim         | Seleção da obra onde o produto será consumido     | "Obra A"              |

**Regras de Negócio:**
- A obra deve ter acompanhamento pronto para gerar comparativos entre o planejado e o executado.
- Se a obra não tiver acompanhamento, não será possível visualizar os comparativos.
- Os serviços devem estar vinculados corretamente para que a solicitação seja processada.

**Observações Importantes:**
- Certifique-se de que a obra selecionada possui acompanhamento completo para evitar problemas de comparativos.
- Evite selecionar produtos que não estejam relacionados aos serviços da obra.

**Conceitos-Chave:**
- **Solicitação de Produto**: Pedido formal para aquisição de itens necessários para a execução de uma obra.
- **Especificação**: Detalhamento das características do produto a ser solicitado.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                     | Solução                                           | Prevenção                                   |
|-----------------------------------|------------------------------------|---------------------------------------------------|---------------------------------------------|
| Produto não encontrado             | Filtros aplicados incorretamente   | Verifique os filtros de categoria e subcategoria  | Use a pesquisa direta para facilitar a busca |
| Tela de especificações não abre    | Obra não possui acompanhamento      | Verifique se a obra está completa no módulo de engenharia | Confirme o status da obra antes de solicitar |
| Botão de salvar desabilitado       | Campos obrigatórios não preenchidos | Preencha todos os campos obrigatórios              | Revise os campos antes de salvar            |

**💡 DICAS E BOAS PRÁTICAS:**
- Utilize a pesquisa direta para localizar rapidamente produtos específicos.
- Sempre verifique se a obra está com acompanhamento completo para evitar problemas futuros.
- Mantenha a lista de produtos atualizada para facilitar as solicitações.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Solicitação de Cimento**
```
Situação: Um engenheiro precisa solicitar cimento para a obra.
Ação: 
  • Campo Categoria: "Materiais de Construção"
  • Campo Subcategoria: "Cimentos"
  • Campo Quantidade: 200
Resultado: O cimento é adicionado à solicitação e vinculado à obra "Obra A".
```

**Exemplo 2: Solicitação de Tinta**
```
Situação: Um responsável pela pintura precisa solicitar tinta.
Ação: 
  • Campo Categoria: "Acabamentos"
  • Campo Subcategoria: "Tintas"
  • Campo Quantidade: 50
Resultado: A tinta é adicionada à solicitação e vinculada à obra "Obra B".
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** A obra deve estar cadastrada e, preferencialmente, com acompanhamento completo.
- **Habilita:** A geração de relatórios de comparativos entre o planejado e o executado.
- **Relacionado a:** Módulo de Engenharia, onde as obras são gerenciadas.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como criar uma solicitação de produto?"
- **Com problema:** "Não consigo encontrar um produto para solicitar, o que fazer?"
- **Informal:** "Como faço pra pedir um produto?"
- **Por sintoma:** "Quando a tela de especificações não abre, o que eu faço?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Criar solicitação", "Adicionar produto", "Pedir item", "Cadastrar produto"
- "Especificar produto", "Vincular produto"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como faço para criar uma nova solicitação de produto?
- Quais filtros posso usar para buscar produtos?
- O que fazer se a tela de especificações não abrir?
- O que preciso ter pronto antes de fazer uma solicitação?
- Como vincular um produto a uma obra específica?

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
- **🔑 Palavras-chave:** data limite, entrega, comentários, status urgente, salvar rascunho, editar, excluir

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como configurar a data limite de entrega em solicitações de compras, adicionar comentários e gerenciar o status das solicitações. O objetivo é garantir que os itens sejam entregues dentro do prazo desejado e que informações adicionais possam ser comunicadas ao fornecedor.

**Contexto:**
Estamos na interface de criação de solicitações de compras, onde o usuário pode definir prazos e adicionar informações relevantes que impactam o fluxo de compras e a comunicação com fornecedores.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo de Compras > Solicitações
- Tela/interface específica: Tela de Criação de Solicitações

**Funcionalidade Detalhada:**
A funcionalidade permite ao usuário configurar uma data limite de entrega para os itens solicitados, que pode ser ajustada conforme as necessidades do solicitante. Além disso, o usuário pode optar por adicionar comentários que serão visíveis tanto para a equipe de compras quanto para o fornecedor, facilitando a comunicação e a clareza nas solicitações.

### 🔹 Passo a Passo Detalhado:

1. **Configurar Data Limite de Entrega**
   - Localização: Campo de data limite na lateral da tela de criação de solicitações.
   - Como fazer: Clique no campo de data limite e selecione uma data no calendário que aparece. O sistema permite que você configure a data conforme a necessidade, sendo que, neste exemplo, foi configurado um prazo de 7 dias.
   - Campos/Opções disponíveis:
     * `Data Limite de Entrega`: Campo de seleção de data, onde o usuário pode escolher a data desejada.
   - Resultado esperado: A data limite de entrega é salva e refletida na solicitação, impactando o status da mesma se o prazo for inferior ao limite.

2. **Exibir Limite ao Fornecedor**
   - Localização: Abaixo do campo de data limite, há uma opção de checkbox.
   - Como fazer: Marque ou desmarque a opção "Exibir limite ao fornecedor" conforme a necessidade.
   - Observações importantes: Se marcado, o fornecedor será notificado sobre a data limite, o que pode influenciar sua resposta e agilidade na entrega.
   - Resultado esperado: O fornecedor terá conhecimento do prazo, ajudando a priorizar a solicitação.

3. **Adicionar Comentários**
   - Localização: Campo de comentários, acessível através de um botão ou campo específico na tela de criação de solicitações.
   - Como fazer: Clique no campo de comentários e digite a mensagem que deseja adicionar. Esta mensagem será visível para a equipe de compras e, se desejado, para o fornecedor.
   - Resultado esperado: O comentário é salvo junto com a solicitação e pode ser visualizado durante o processo de aprovação e orçamento.

4. **Salvar Solicitação**
   - Localização: Botão "Salvar" na parte inferior da tela.
   - Como fazer: Clique em "Salvar" para finalizar a criação da solicitação. Você também pode optar por "Salvar como rascunho" se desejar voltar e realizar alterações posteriormente.
   - Resultado esperado: A solicitação é salva no sistema, podendo ser editada ou excluída enquanto o status estiver em aberto.

5. **Gerenciar Solicitações**
   - Localização: Tela inicial de solicitações, onde são listadas as solicitações em aberto.
   - Como fazer: Acompanhe a situação das solicitações através do histórico de ações visível nesta tela.
   - Observações importantes: O status da solicitação será atualizado conforme o fluxo de compras avança, e a sinalização de "urgente" aparecerá se o prazo for inferior ao limite configurado.
   - Resultado esperado: O usuário pode visualizar o status e histórico das solicitações, facilitando o acompanhamento.

**Campos e Parâmetros:**

| Campo                       | Tipo          | Obrigatório | Descrição                                                       | Exemplo              |
|-----------------------------|---------------|-------------|---------------------------------------------------------------|----------------------|
| `Data Limite de Entrega`    | Data          | Sim         | Data limite para a entrega dos itens solicitados.            | 2023-10-30           |
| `Exibir limite ao fornecedor`| Checkbox      | Não         | Indica se o fornecedor deve ser notificado sobre o limite.   | [X] Sim              |
| `Comentários`               | Texto livre   | Não         | Mensagem adicional que pode ser enviada ao fornecedor.        | "Favor priorizar."   |

**Regras de Negócio:**
- Se a data limite de entrega for inferior ao prazo configurado, a solicitação será marcada como "urgente".
- Comentários adicionados são visíveis para a equipe de compras e, se configurado, para o fornecedor.
- Solicitações podem ser editadas ou excluídas apenas enquanto o status estiver "em aberto".

**Observações Importantes:**
- É recomendável revisar a data limite antes de salvar a solicitação para evitar problemas de entrega.
- Evite deixar o campo de comentários vazio se houver informações relevantes a serem comunicadas.
- Verifique se a opção de exibir o limite ao fornecedor está marcada conforme a necessidade.

**Conceitos-Chave:**
- **Data Limite de Entrega**: Prazo estabelecido para a entrega dos itens solicitados, que pode impactar o status da solicitação.
- **Status Urgente**: Indicação de que a solicitação requer atenção imediata devido a um prazo de entrega curto.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                        | Causa Provável                     | Solução                                           | Prevenção                                       |
|---------------------------------|------------------------------------|--------------------------------------------------|-------------------------------------------------|
| Solicitação não salva           | Campo de data limite vazio         | Preencha o campo de data limite antes de salvar. | Sempre verificar todos os campos obrigatórios.   |
| Comentário não aparece          | Checkbox "Exibir limite" não marcado | Marque a opção para que o fornecedor veja o comentário. | Revisar as opções antes de salvar.               |
| Status não atualizado           | Fluxo de compras não iniciado      | Acompanhe o fluxo de compras para atualizações. | Verificar o andamento do processo de compras.    |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre configure a data limite de entrega com antecedência para evitar urgências.
- Utilize comentários para esclarecer dúvidas ou fornecer instruções adicionais ao fornecedor.
- Salve como rascunho se não tiver certeza sobre todos os detalhes da solicitação.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Solicitação com Data Limite**
```
Situação: Um departamento precisa de materiais para um evento em 5 dias.
Ação: 
  • Campo `Data Limite de Entrega`: "2023-10-25"
  • Campo `Comentários`: "Favor entregar até o dia 25."
Resultado: A solicitação é marcada como urgente e o fornecedor é notificado sobre a data limite.
```

**Exemplo 2: Solicitação sem Comentários**
```
Situação: Um pedido padrão sem necessidade de urgência.
Ação: 
  • Campo `Data Limite de Entrega`: "2023-11-05"
  • Campo `Comentários`: (deixado em branco)
Resultado: A solicitação é salva normalmente, sem urgência, e sem comentários adicionais.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O módulo de compras deve estar habilitado e configurado corretamente.
- **Habilita:** A visualização do histórico de ações e acompanhamento do status da solicitação.
- **Relacionado a:** Funcionalidades de aprovação de pedidos e comunicação com fornecedores.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como configurar a data limite de entrega?"
- **Com problema:** "Minha solicitação não está sendo salva, o que fazer?"
- **Informal:** "Como coloco a data de entrega?"
- **Por sintoma:** "Por que meu pedido não aparece como urgente?"
- **Com dúvida:** "Como adicionar comentários na solicitação?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Definir prazo", "data de entrega", "comentários na solicitação", "urgente", "salvar pedido".

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como configurar a data limite de entrega em uma solicitação?
- O que fazer se a solicitação não está sendo salva?
- Como adicionar comentários que serão visíveis para o fornecedor?
- O que significa o status "urgente" na minha solicitação?
- O que preciso fazer antes de salvar uma solicitação de compra?

---


---


---

## 3. Registro de Entradas e Tratamento de Divergências

**📋 METADADOS:**
- **ID:** sec_3
- **⏱️ Minutagem:** 05:04 → 07:37
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/6vX7wYe8cIw?si=5Xf_VmLvM7bj6M73&t=304)
- **📦 Módulo:** Gestão de Estoque
- **🏷️ Categorias:** Operacional, Registro, Divergências
- **🔑 Palavras-chave:** entrada, divergência, justificativa, estoque, produto

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de registro de entradas de produtos no sistema, incluindo como lidar com divergências entre a quantidade prevista e a quantidade recebida, além das ações disponíveis para resolver essas divergências.

**Contexto:**
Estamos na interface de registro de entradas de produtos, onde o usuário deve verificar e registrar a quantidade de produtos recebidos em relação ao que foi previsto. O objetivo é garantir que as quantidades estejam corretas e, em caso de divergências, tomar as ações apropriadas.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Gestão de Estoque > Submenu Registro de Entradas
- Tela/interface específica: Tela de Registro de Entradas

**Funcionalidade Detalhada:**
A funcionalidade de registro de entradas permite ao usuário registrar a quantidade de produtos que chegaram ao estoque e verificar se essa quantidade corresponde ao que foi previsto. Em caso de divergências, o sistema solicita uma justificativa e oferece opções para resolver a situação, garantindo que o estoque esteja sempre atualizado e correto.

### 🔹 Passo a Passo Detalhado:

1. **Verificar Quantidade Recebida**
   - Localização: Tela de Registro de Entradas
   - Como fazer: Acesse a entrada pendente e compare a quantidade prevista com a quantidade recebida. 
   - Campos/Opções disponíveis:
     * `Quantidade Prevista`: Campo que exibe a quantidade que deveria ter chegado.
     * `Quantidade Recebida`: Campo onde o usuário insere a quantidade que realmente chegou.
   - Resultado esperado: Se as quantidades coincidirem, a entrada é finalizada e o produto é disponibilizado no estoque.

2. **Registrar Divergência**
   - Localização: Tela de Registro de Entradas, após a verificação de quantidades.
   - Como fazer: Se a quantidade recebida for diferente da prevista, clique em "Salvar". O sistema solicitará uma justificativa.
   - Observações importantes: A justificativa deve ser clara e relacionada ao motivo da divergência.
   - Resultado esperado: A entrada não será finalizada e ficará sinalizada em amarelo na tela inicial de entradas.

3. **Visualizar Detalhes da Divergência**
   - Localização: Tela inicial de entradas, clique na entrada sinalizada em amarelo.
   - Como fazer: Ao clicar, o usuário verá informações detalhadas sobre a divergência, incluindo:
     * `Produto`: Nome do produto.
     * `Quantidade Prevista`: Quantidade que deveria ter chegado.
     * `Quantidade Recebida`: Quantidade que realmente chegou.
     * `Diferença`: A diferença entre as quantidades.
     * `Comentário`: Justificativa inserida pelo usuário.
   - Resultado esperado: O usuário tem uma visão clara da divergência e pode decidir a próxima ação.

4. **Tomar Ação sobre a Divergência**
   - Localização: Tela de detalhes da entrada divergente.
   - Como fazer: O responsável pode escolher entre três ações:
     * **Criar Entrada Vulsa**: Para registrar a quantidade restante dos produtos divergentes.
     * **Ignorar Divergência**: Para finalizar a entrada pendente, caso a divergência seja considerada aceitável.
     * **Gerar Crédito com o Fornecedor**: Para registrar a quantidade recebida e gerar um crédito financeiro pela diferença.
   - Resultado esperado: Dependendo da ação escolhida, o sistema irá gerar os fluxos necessários e finalizar a entrada conforme a escolha do usuário.

5. **Inserir Justificativa para Ação Escolhida**
   - Localização: Após selecionar uma das ações acima.
   - Como fazer: O sistema solicitará uma justificativa para a ação escolhida. Insira a justificativa e clique em "Salvar".
   - Resultado esperado: O sistema processará a ação e atualizará o status da entrada conforme a justificativa e a ação escolhida.

**Campos e Parâmetros:**

| Campo                   | Tipo    | Obrigatório | Descrição                                       | Exemplo                |
|-------------------------|---------|-------------|-------------------------------------------------|------------------------|
| `Quantidade Prevista`   | Numérico| Sim         | Quantidade de produtos que deveria ter chegado. | 16                     |
| `Quantidade Recebida`   | Numérico| Sim         | Quantidade de produtos que realmente chegaram.  | 8                      |
| `Justificativa`        | Texto   | Sim         | Motivo da divergência ou da ação escolhida.    | "Recebido em atraso"   |

**Regras de Negócio:**
- A entrada só é finalizada se a quantidade recebida for igual à quantidade prevista.
- Se houver divergência, a entrada ficará sinalizada em amarelo até que uma ação seja tomada.
- O sistema requer justificativa para qualquer divergência registrada.

**Observações Importantes:**
- Sempre verifique as quantidades antes de salvar para evitar erros.
- Caso a divergência seja ignorada, certifique-se de que a situação é realmente aceitável.
- É importante documentar as justificativas de forma clara para futuras referências.

**Conceitos-Chave:**
- **Entrada Vulsa**: Registro de uma nova entrada para a quantidade restante de produtos que não foram recebidos.
- **Justificativa**: Explicação fornecida pelo usuário sobre a divergência ou a ação tomada.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                               | Causa Provável                     | Solução                                         | Prevenção                                   |
|----------------------------------------|------------------------------------|------------------------------------------------|---------------------------------------------|
| Divergência não registrada              | Quantidade recebida não conferida  | Verifique as quantidades e registre corretamente.| Sempre conferir antes de salvar.           |
| Botão "Salvar" desabilitado            | Campos obrigatórios não preenchidos| Preencha todos os campos obrigatórios.         | Verifique se todos os campos estão completos.|
| Justificativa não aceita               | Justificativa muito vaga           | Forneça uma justificativa clara e específica.  | Use descrições detalhadas.                 |

**💡 DICAS E BOAS PRÁTICAS:**
- Utilize sempre justificativas detalhadas para facilitar a análise futura.
- Mantenha um registro de entradas e divergências para auditorias.
- Familiarize-se com as opções de ações disponíveis para resolver divergências rapidamente.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Divergência na Recepção de Produtos**
```
Situação: O previsto era 16 unidades de cimento, mas apenas 8 chegaram.
Ação: Registre a quantidade recebida como 8 e insira a justificativa "Recebido em atraso".
  • Quantidade Prevista: 16
  • Quantidade Recebida: 8
Resultado: A entrada ficará pendente e sinalizada em amarelo, aguardando ação.
```

**Exemplo 2: Ignorando uma Divergência Aceitável**
```
Situação: O previsto era 10 unidades de tinta, mas 9 chegaram e a divergência é considerada aceitável.
Ação: Clique em "Ignorar Divergência" e finalize a entrada.
Resultado: A entrada será finalizada e o produto será disponibilizado no estoque.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O usuário deve ter permissão para registrar entradas e visualizar divergências.
- **Habilita:** A funcionalidade de gerar créditos financeiros com fornecedores.
- **Relacionado a:** Módulo de Compras, onde as entradas são geradas a partir de pedidos.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como registrar uma entrada de produtos?"
- **Com problema:** "O que fazer se a quantidade recebida não é a mesma que a prevista?"
- **Informal:** "Como lidar com divergências na entrega?"
- **Por sintoma:** "O que fazer quando a entrada fica pendente?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Registrar entrada", "Adicionar entrada", "Entrada de produtos", "Conferir recebimento".

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como registro uma entrada de produtos no sistema?
- O que fazer se a quantidade recebida é diferente da prevista?
- Como posso justificar uma divergência?
- O que fazer se o botão de salvar não está habilitado?
- Quais são as opções disponíveis para resolver uma divergência?

---


---


---

## 4. Registro de Entrada e Consumo de Produtos no Estoque

**📋 METADADOS:**
- **ID:** sec_4
- **⏱️ Minutagem:** 07:35 → 10:10
- **⏲️ Duração:** 155s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/6vX7wYe8cIw?si=5Xf_VmLvM7bj6M73&t=455)
- **📦 Módulo:** Gestão de Estoque
- **🏷️ Categorias:** Operacional, Cadastro, Relatório
- **🔑 Palavras-chave:** entrada de estoque, consumo de produtos, registro inicial, devolução, transferência

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como registrar a entrada e o consumo de produtos no estoque, permitindo ao usuário gerenciar eficientemente os itens disponíveis e seu uso em obras. O processo é essencial para manter um controle preciso do inventário.

**Contexto:**
Estamos na interface do módulo de Gestão de Estoque, onde o usuário pode registrar a entrada de produtos, seu consumo e transferências entre locais. O objetivo é garantir que o estoque esteja sempre atualizado e que o histórico de uso seja mantido.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Gestão de Estoque > Registro de Entrada e Consumo
- Tela/interface específica: Tela de Registro de Entrada e Consumo

**Funcionalidade Detalhada:**
A funcionalidade de registro de entrada e consumo de produtos permite ao usuário adicionar novos itens ao estoque, registrar o consumo desses itens e realizar transferências entre diferentes locais. É uma ferramenta crucial para o gerenciamento de materiais em obras, garantindo que a quantidade de produtos disponíveis esteja sempre atualizada.

### 🔹 Passo a Passo Detalhado:

1. **Registrar Entrada de Produto**
   - Localização: Tela de Registro de Entrada e Consumo, seção "Entrada"
   - Como fazer: Clique no botão **"Mais Entrada"** para iniciar o registro.
   - Campos/Opções disponíveis:
     * `Tipo de Registro`: Selecione entre as opções **Devolução ao Estoque**, **Registros Iniciais** ou **Outros**.
     * `Produto`: Selecione o produto desejado a partir da listagem disponível.
   - Resultado esperado: O produto selecionado será adicionado ao estoque, e a quantidade será atualizada.

2. **Registrar Consumo de Produto**
   - Localização: Tela de Registro de Entrada e Consumo, seção "Consumo"
   - Como fazer: Clique no botão **"Mais Consumo"** para registrar o uso de produtos.
   - Observações importantes: É possível vincular o consumo a um local de obra e, opcionalmente, a um serviço específico.
   - Resultado esperado: O consumo registrado será subtraído da quantidade disponível no estoque.

3. **Selecionar Local de Consumo**
   - Localização: Tela de Registro de Consumo, campo **"Local de Consumo"**
   - Como fazer: Selecione a obra desejada na lista de locais disponíveis.
   - Resultado esperado: A listagem de produtos disponíveis para consumo será atualizada com base na obra selecionada.

4. **Adicionar Produto ao Consumo**
   - Localização: Tela de Registro de Consumo, seção de listagem de produtos
   - Como fazer: Clique no ícone **"+"** ao lado do produto que deseja consumir.
   - Campos/Opções disponíveis:
     * `Quantidade de Uso`: Insira a quantidade do produto que foi consumida.
   - Resultado esperado: A quantidade inserida será registrada, e o histórico de consumo será atualizado.

5. **Salvar Registro de Consumo**
   - Localização: Tela de Registro de Consumo, botão **"Salvar"**
   - Como fazer: Após inserir a quantidade de uso, clique em **"Salvar"** para confirmar o registro.
   - Resultado esperado: A quantidade consumida será subtraída do estoque, e o registro de consumo será salvo.

6. **Registrar Transferência de Produtos**
   - Localização: Tela de Registro de Entrada e Consumo, seção "Transferências"
   - Como fazer: Clique no botão **"Mais Transferência"** para iniciar o processo de transferência.
   - Campos/Opções disponíveis:
     * `Local de Origem`: Selecione o local de onde os produtos estão sendo transferidos.
     * `Local de Destino`: Selecione o local para onde os produtos estão sendo enviados.
   - Resultado esperado: A transferência será registrada, e os produtos serão movidos entre os locais selecionados.

**Campos e Parâmetros:**

| Campo                  | Tipo         | Obrigatório | Descrição                                           | Exemplo                  |
|------------------------|--------------|-------------|----------------------------------------------------|--------------------------|
| `Tipo de Registro`     | Dropdown     | Sim         | Tipo de entrada a ser registrada.                  | Devolução ao Estoque     |
| `Produto`              | Dropdown     | Sim         | Produto a ser adicionado ou consumido.             | Cimento                   |
| `Local de Consumo`     | Dropdown     | Sim         | Local onde o produto será consumido.               | Obra A                   |
| `Quantidade de Uso`    | Numérico     | Sim         | Quantidade do produto que foi consumida.           | 15                       |
| `Local de Origem`      | Dropdown     | Sim         | Local de onde os produtos estão sendo transferidos. | Armazém Central          |
| `Local de Destino`     | Dropdown     | Sim         | Local para onde os produtos estão sendo enviados.   | Obra B                   |

**Regras de Negócio:**
- O registro de entrada não interfere em outros módulos do sistema.
- O consumo deve ser registrado para manter o histórico atualizado.
- Transferências devem ser registradas corretamente para refletir a movimentação de produtos.

**Observações Importantes:**
- Sempre verifique a quantidade disponível antes de registrar o consumo.
- Evite registrar consumos que excedam a quantidade disponível no estoque.
- As transferências devem ser feitas com atenção para não causar desbalanceamento no estoque.

**Conceitos-Chave:**
- **Entrada de Estoque**: Processo de adicionar produtos ao inventário.
- **Consumo**: Registro da utilização de produtos em uma obra.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                  | Solução                                                   | Prevenção                          |
|-----------------------------------|---------------------------------|----------------------------------------------------------|------------------------------------|
| Produto não aparece na listagem   | Não foi registrado no estoque   | Verifique se o produto foi adicionado corretamente.      | Sempre registrar a entrada primeiro. |
| Quantidade de consumo inválida     | Excede a quantidade disponível  | Ajuste a quantidade para um valor menor ou igual.       | Verifique a quantidade disponível antes. |
| Transferência não registrada      | Falta de informações obrigatórias| Complete todos os campos obrigatórios e tente novamente. | Certifique-se de preencher todos os campos. |

**💡 DICAS E BOAS PRÁTICAS:**
- Utilize a funcionalidade de comentários para anotar informações relevantes sobre o consumo.
- Mantenha um registro regular das entradas e saídas para evitar discrepâncias.
- Use a opção de filtro na listagem de produtos para facilitar a busca.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Registro de Consumo em Obra**
```
Situação: O produto "Cimento" foi utilizado na obra "Obra A".
Ação: 
  • Tipo de Registro: "Consumo"
  • Local de Consumo: "Obra A"
  • Produto: "Cimento"
  • Quantidade de Uso: 15
Resultado: O estoque de "Cimento" será reduzido em 15 unidades.
```

**Exemplo 2: Transferência de Produtos**
```
Situação: Transferir "Areia" do "Armazém Central" para "Obra B".
Ação:
  • Local de Origem: "Armazém Central"
  • Local de Destino: "Obra B"
  • Produto: "Areia"
  • Quantidade: 10
Resultado: O estoque de "Areia" será ajustado nos dois locais.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O produto deve estar cadastrado no sistema antes de ser registrado como entrada ou consumo.
- **Habilita:** A funcionalidade de relatórios de consumo e estoque.
- **Relacionado a:** Módulo de Relatórios de Estoque, onde os dados de consumo e entrada são utilizados para gerar análises.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como registrar a entrada de um produto?"
- **Com problema:** "Não consigo registrar o consumo de um produto, o que fazer?"
- **Informal:** "Como eu coloco um produto no estoque?"
- **Por sintoma:** "Quando o produto não aparece na lista, como resolver?"
- **Com variação:** "Qual o passo a passo para transferir produtos entre locais?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Adicionar produto", "Registrar entrada", "Consumir produto", "Transferir itens", "Gerenciar estoque"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como faço para registrar a entrada de um produto no estoque?
- O que fazer se não consigo registrar o consumo de um produto?
- Como transferir produtos entre diferentes locais?
- O que fazer se a quantidade de consumo não é válida?
- O que preciso fazer antes de registrar uma entrada de estoque?

---


---


---

## 5. Solicitação e Transferência de Produtos

**📋 METADADOS:**
- **ID:** sec_5
- **⏱️ Minutagem:** 10:08 → 12:42
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/6vX7wYe8cIw?si=5Xf_VmLvM7bj6M73&t=608)
- **📦 Módulo:** Gestão de Estoque
- **🏷️ Categorias:** Transferência, Produtos, Estoque, Operacional
- **🔑 Palavras-chave:** transferência, produtos, quantidade, romaneio, entrada

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de solicitação e transferência de produtos entre estoques, incluindo a criação de uma transferência pendente, a confirmação da quantidade a ser transferida e a entrada dos produtos na nova obra.

**Contexto:**
Estamos na interface do sistema de gestão de estoque, especificamente na funcionalidade de transferência de produtos. O objetivo é realizar a transferência de itens de um local de origem para um novo destino, garantindo que as quantidades sejam corretamente registradas e confirmadas.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Gestão de Estoque > Submenu Transferência de Produtos
- Tela/interface específica: Tela de Solicitação de Transferência

**Funcionalidade Detalhada:**
A funcionalidade de solicitação e transferência de produtos permite que o usuário selecione um local de origem e visualize os produtos disponíveis nesse estoque. O usuário pode arrastar os itens ou clicar na mãozinha para selecionar os produtos que deseja transferir. Após definir a quantidade a ser transferida, o usuário deve salvar a solicitação, que será registrada como uma transferência pendente. O sistema também permite a impressão de um romaneio, que é um documento que detalha as informações dos produtos transferidos.

### 🔹 Passo a Passo Detalhado:

1. **Definir Local de Origem**
   - Localização: Tela de Solicitação de Transferência
   - Como fazer: Clique no campo de seleção do local de origem e escolha o estoque desejado.
   - Campos/Opções disponíveis:
     * `Local de Origem`: Seleção de estoque disponível.
   - Resultado esperado: O sistema exibirá a lista de produtos disponíveis no estoque selecionado.

2. **Selecionar Produtos para Transferência**
   - Localização: Lista de produtos disponíveis no estoque.
   - Como fazer: Arraste os produtos desejados para o lado ou clique na mãozinha ao lado de cada produto.
   - Observações importantes: Certifique-se de que a quantidade disponível é suficiente para a transferência.
   - Resultado esperado: Os produtos selecionados serão adicionados à solicitação de transferência.

3. **Definir Quantidade a Ser Transferida**
   - Localização: Campo de quantidade ao lado de cada produto selecionado.
   - Como fazer: Insira a quantidade desejada para cada produto.
   - Resultado esperado: A quantidade a ser transferida é registrada para cada item.

4. **Salvar Solicitação de Transferência**
   - Localização: Botão **Salvar** na parte inferior da tela.
   - Como fazer: Clique no botão **Salvar** para registrar a solicitação.
   - Resultado esperado: A transferência é registrada como pendente na tela.

5. **Visualizar Transferências Pendentes**
   - Localização: Tela de Transferências Pendentes.
   - Como fazer: Clique na transferência pendente para visualizar os itens aguardando confirmação.
   - Resultado esperado: O sistema agrupa todos os itens que estão aguardando confirmação.

6. **Confirmar Transferência ou Cancelar**
   - Localização: Tela de Transferências Pendentes.
   - Como fazer: Para os itens que deseja transferir, insira a quantidade real a ser transferida e clique em **Salvar** novamente.
   - Observações importantes: Você pode optar por não transferir alguns itens, que não serão incluídos na confirmação.
   - Resultado esperado: A transferência é atualizada e os itens confirmados são registrados.

7. **Imprimir Romaneio**
   - Localização: Opção de impressão na tela de confirmação.
   - Como fazer: Se desejar, marque a opção para imprimir o romaneio antes de salvar.
   - Resultado esperado: Um documento referente às informações do que está sendo transferido é gerado.

8. **Realizar Entrada na Nova Obra**
   - Localização: Tela de Entrada de Produtos.
   - Como fazer: Confirme se a quantidade prevista é a que chegou na nova obra e clique em **Salvar**.
   - Resultado esperado: A entrada dos produtos é registrada, finalizando o fluxo de transferência.

**Campos e Parâmetros:**

| Campo                   | Tipo       | Obrigatório | Descrição                                               | Exemplo               |
|-------------------------|------------|-------------|--------------------------------------------------------|-----------------------|
| `Local de Origem`       | Dropdown   | Sim         | Seleção do estoque de origem para a transferência.     | "Estoque A"           |
| `Produto`               | Lista      | Sim         | Lista de produtos disponíveis no estoque selecionado.  | "Cimento", "Areia"    |
| `Quantidade`            | Numérico   | Sim         | Quantidade de cada produto a ser transferido.         | 50                    |
| `Romaneio`              | Checkbox   | Não         | Opção para imprimir o romaneio da transferência.       | [ ] Imprimir Romaneio |
| `Código da Transferência`| Texto      | Sim         | Código gerado para identificar a transferência.        | "TRANSF_001"          |

**Regras de Negócio:**
- A quantidade a ser transferida não pode exceder a quantidade disponível no estoque de origem.
- A transferência deve ser confirmada antes de realizar a entrada na nova obra.
- O romaneio é opcional, mas recomendado para documentação.

**Observações Importantes:**
- Verifique sempre a quantidade disponível antes de realizar a transferência.
- Caso a transferência não seja confirmada, os itens permanecerão pendentes.
- É importante manter a documentação atualizada para evitar erros de estoque.

**Conceitos-Chave:**
- **Transferência de Produtos**: Processo de mover produtos de um estoque para outro.
- **Romaneio**: Documento que detalha os produtos e quantidades transferidos.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                     | Solução                                           | Prevenção                                      |
|-----------------------------------|------------------------------------|--------------------------------------------------|------------------------------------------------|
| Quantidade não disponível          | Tentativa de transferir mais do que o estoque permite. | Verifique a quantidade disponível antes de transferir. | Sempre conferir o estoque antes da transferência. |
| Transferência não aparece na tela  | Falha ao salvar a solicitação.    | Tente salvar novamente e verifique se há mensagens de erro. | Salvar frequentemente durante o processo.     |
| Erro ao imprimir romaneio         | Impressora não configurada ou sem papel. | Verifique a impressora e tente novamente.       | Testar a impressora antes de gerar documentos. |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre mantenha um registro das transferências realizadas.
- Utilize o romaneio para facilitar a conferência na nova obra.
- Realize transferências em horários de menor movimento para evitar erros.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Transferência de Cimento**
```
Situação: Transferir 50 sacos de cimento do Estoque A para a obra.
Ação: 
  • Campo `Local de Origem`: "Estoque A"
  • Campo `Produto`: "Cimento"
  • Campo `Quantidade`: 50
Resultado: A transferência é registrada e aparece como pendente.
```

**Exemplo 2: Transferência de Areia**
```
Situação: Transferir 30 toneladas de areia do Estoque B para a obra.
Ação: 
  • Campo `Local de Origem`: "Estoque B"
  • Campo `Produto`: "Areia"
  • Campo `Quantidade`: 30
Resultado: A transferência é confirmada e os produtos são registrados na nova obra.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O estoque de origem deve ter produtos disponíveis para transferência.
- **Habilita:** A entrada de produtos na nova obra após a confirmação da transferência.
- **Relacionado a:** Módulo de Gestão de Estoque e Relatórios de Transferência.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como transferir produtos entre estoques?"
- **Com problema:** "Não consigo transferir produtos, o que fazer?"
- **Informal:** "Como eu faço pra mover os produtos?"
- **Por sintoma:** "Quando a quantidade não bate, como resolver?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Transferir itens", "Mover produtos", "Solicitar transferência", "Registrar transferência"
- "Romaneio", "Documento de transferência", "Relatório de produtos"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como faço para solicitar uma transferência de produtos?
- O que fazer se a quantidade disponível não é suficiente para a transferência?
- Como confirmar uma transferência pendente?
- O que fazer se o romaneio não imprime corretamente?
- O que preciso ter configurado antes de realizar uma transferência?

---


---


---

## 6. Vinculação de Produtos com Categorias e Subcategorias

**📋 METADADOS:**
- **ID:** sec_6
- **⏱️ Minutagem:** 12:40 → 15:13
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/6vX7wYe8cIw?si=5Xf_VmLvM7bj6M73&t=760)
- **📦 Módulo:** Cadastro de Produtos
- **🏷️ Categorias:** Configuração, Cadastro, Produtos, Especificações
- **🔑 Palavras-chave:** vinculação, categoria, subcategoria, especificações, produtos

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de vinculação de produtos a categorias e subcategorias, permitindo uma organização mais eficiente e específica dos itens no sistema. O objetivo é garantir que o sistema gerencie corretamente os produtos, diferenciando entre equipamentos e materiais.

**Contexto:**
Estamos na fase de cadastro de um novo produto no sistema, onde é necessário definir a categoria e subcategoria do item, além de especificar se se trata de um equipamento ou material. Essa estruturação é crucial para o gerenciamento adequado dos produtos.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Cadastro de Produtos > Tela de Vinculação de Produtos
- Tela/interface específica: Tela de Cadastro de Produtos

**Funcionalidade Detalhada:**
A funcionalidade permite ao usuário vincular um produto a uma categoria e subcategoria específicas, além de definir se o produto é um equipamento ou um material. Essa categorização é essencial para que o sistema possa gerenciar os produtos de maneira adequada, pois equipamentos e materiais são tratados de forma distinta.

### 🔹 Passo a Passo Detalhado:

1. **Vincular Categoria e Subcategoria**
   - Localização: Tela de Cadastro de Produtos, seção de categorias.
   - Como fazer: Clique no campo de seleção de categoria e escolha "Pinturas, Texturas e Tintas". Em seguida, selecione a subcategoria "Tintas".
   - Campos/Opções disponíveis:
     * `Categoria`: Opções incluem "Pinturas, Texturas e Tintas", "Ferramentas", "Materiais de Construção", etc.
     * `Subcategoria`: Opções incluem "Tintas", "Pincéis", "Rolos", etc.
   - Resultado esperado: O produto é vinculado à categoria e subcategoria selecionadas, permitindo uma organização mais específica.

2. **Definir Tipo de Produto**
   - Localização: Abaixo da seção de categorias, na área de informações gerais.
   - Como fazer: Selecione se o produto é um "Equipamento" ou "Material" através do campo de seleção.
   - Observações importantes: É crucial escolher a opção correta, pois o sistema gerencia equipamentos e materiais de formas diferentes.
   - Resultado esperado: O tipo de produto é definido, permitindo que o sistema aplique as regras de gerenciamento apropriadas.

3. **Adicionar Embalagens**
   - Localização: Tela de Cadastro de Produtos, seção de embalagens.
   - Como fazer: Clique no botão **Adicionar Embalagem** e insira as informações sobre a embalagem do produto, como quantidade e unidade de medida.
   - Campos/Opções disponíveis:
     * `Quantidade`: Número de unidades na embalagem (ex: 12).
     * `Unidade de Medida`: Opções incluem "litros", "unidades", "caixas", etc.
   - Resultado esperado: A embalagem é registrada, permitindo que o sistema saiba como o produto é comercializado.

4. **Adicionar Componentes**
   - Localização: Tela de Cadastro de Produtos, seção de componentes.
   - Como fazer: Clique em **Mais Componente** para adicionar itens relacionados ao kit do produto.
   - Observações importantes: É possível adicionar múltiplos componentes, que podem ser outros produtos ou acessórios.
   - Resultado esperado: Os componentes são vinculados ao produto, formando um kit.

5. **Definir Especificações**
   - Localização: Tela de Cadastro de Produtos, seção de especificações.
   - Como fazer: Clique em **Mais Específico** e escolha o tipo de especificação que deseja adicionar (ex: tipo, cor, marca, parâmetro, resistência).
   - Campos/Opções disponíveis:
     * `Tipo`: Opções como "Tinta Acrílica", "Tinta à Base de Água", etc.
     * `Cor`: Selecione a cor desejada para o produto.
   - Resultado esperado: As especificações são adicionadas ao produto, permitindo uma descrição mais detalhada.

6. **Salvar as Informações**
   - Localização: Tela de Cadastro de Produtos, botão **Salvar** na parte inferior.
   - Como fazer: Após revisar todas as informações preenchidas, clique em **Salvar** para registrar o produto no sistema.
   - Resultado esperado: O produto é salvo com todas as informações e vinculações definidas.

**Campos e Parâmetros:**

| Campo                | Tipo         | Obrigatório | Descrição                                           | Exemplo         |
|----------------------|--------------|-------------|-----------------------------------------------------|------------------|
| Categoria            | Dropdown     | Sim         | Categoria principal do produto                       | Pinturas         |
| Subcategoria         | Dropdown     | Sim         | Subcategoria específica do produto                   | Tintas           |
| Tipo de Produto      | Dropdown     | Sim         | Define se o produto é um equipamento ou material     | Material         |
| Quantidade           | Numérico     | Sim         | Número de unidades na embalagem                      | 12               |
| Unidade de Medida    | Dropdown     | Sim         | Unidade de medida da embalagem                       | Litros           |
| Tipo de Especificação| Dropdown     | Sim         | Tipo de especificação a ser adicionada              | Cor              |
| Cor                  | Dropdown     | Não         | Cor específica do produto                            | Azul             |

**Regras de Negócio:**
- O produto deve ser vinculado a uma categoria e subcategoria para ser salvo.
- O tipo de produto deve ser definido corretamente para que o sistema aplique as regras de gerenciamento apropriadas.
- As especificações podem ser adicionadas em múltiplas instâncias, permitindo uma descrição detalhada do produto.

**Observações Importantes:**
- Sempre revise as informações antes de clicar em **Salvar** para evitar erros.
- Se o botão **Salvar** estiver desabilitado, verifique se todos os campos obrigatórios foram preenchidos.
- É recomendável adicionar fotos para cada especificação para melhor visualização.

**Conceitos-Chave:**
- **Categoria**: Classificação ampla que agrupa produtos semelhantes.
- **Subcategoria**: Classificação mais específica dentro de uma categoria.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                   | Solução                                           | Prevenção                                       |
|-----------------------------------|----------------------------------|--------------------------------------------------|------------------------------------------------|
| Botão **Salvar** desabilitado     | Campos obrigatórios não preenchidos | Preencha todos os campos obrigatórios.           | Revise os campos antes de tentar salvar.       |
| Erro ao adicionar embalagem        | Quantidade inválida              | Insira um número válido para a quantidade.       | Verifique a quantidade antes de adicionar.     |
| Não consegue adicionar componentes  | Produto não salvo previamente    | Salve o produto antes de adicionar componentes.   | Salve o produto após preencher as informações. |

**💡 DICAS E BOAS PRÁTICAS:**
- Utilize sempre as opções de dropdown para evitar erros de digitação.
- Adicione fotos relevantes para cada especificação para facilitar a identificação do produto.
- Revise as especificações e componentes antes de finalizar o cadastro.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Cadastro de Tinta**
```
Situação: Cadastro de uma nova tinta para venda.
Ação: 
  • Categoria: "Pinturas, Texturas e Tintas"
  • Subcategoria: "Tintas"
  • Tipo de Produto: "Material"
  • Embalagem: 12 unidades de 20 L
Resultado: O produto "Tinta Acrílica Azul" é cadastrado com sucesso.
```

**Exemplo 2: Cadastro de Kit de Pintura**
```
Situação: Cadastro de um kit de pintura que inclui tinta e pincéis.
Ação: 
  • Categoria: "Pinturas, Texturas e Tintas"
  • Subcategoria: "Tintas"
  • Tipo de Produto: "Material"
  • Componentes: Adicionar "Pincel" e "Rolo"
Resultado: O kit de pintura é cadastrado com todos os componentes vinculados.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O usuário deve ter permissão para cadastrar produtos no sistema.
- **Habilita:** A vinculação de produtos a categorias e subcategorias permite a geração de relatórios mais detalhados sobre vendas e estoque.
- **Relacionado a:** Funcionalidades de relatórios de vendas e gestão de estoque.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como vincular um produto a uma categoria?"
- **Com problema:** "Não consigo salvar meu produto, o que fazer?"
- **Informal:** "Como eu coloco uma tinta na categoria certa?"
- **Por sintoma:** "Meu produto não aparece na lista, como resolver?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Adicionar categoria", "Vincular subcategoria", "Cadastrar produto", "Definir tipo de produto"
- "Classificação de produtos", "Organização de itens"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como vincular um produto a uma categoria e subcategoria?
- O que fazer se o botão de salvar estiver desabilitado?
- Como adicionar especificações a um produto?
- O que fazer se não conseguir adicionar componentes ao produto?
- O que preciso ter feito antes de cadastrar um novo produto?

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
- **🔑 Palavras-chave:** equipamentos, cadastro, ativo, desativado, aluguel, manutenção

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de cadastro e gerenciamento de equipamentos no sistema, incluindo a distinção entre equipamentos próprios e alugados, e como registrar suas informações essenciais.

**Contexto:**
Estamos na fase de gerenciamento de equipamentos dentro do módulo de Equipamentos do sistema. O objetivo desta seção é ensinar como cadastrar e gerenciar tanto equipamentos próprios quanto alugados, além de como definir seu status de atividade.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Equipamentos > Gerenciamento de Equipamentos
- Tela/interface específica: Tela de Listagem de Equipamentos

**Funcionalidade Detalhada:**
A funcionalidade de gerenciamento de equipamentos permite ao usuário cadastrar e gerenciar todos os equipamentos, sejam eles próprios ou alugados. O sistema oferece a opção de desativar um produto, caso não esteja em uso, e reativá-lo posteriormente. Para equipamentos próprios, o fluxo de compras é integrado, permitindo que, após a entrada da nota, o equipamento apareça automaticamente na listagem. Para equipamentos alugados, é necessário criar uma ordem de serviço, pois a nota de serviço não gera estoque.

### 🔹 Passo a Passo Detalhado:

1. **Cadastrar Novo Equipamento**
   - Localização: Tela de Listagem de Equipamentos, botão **+ Equipamento**
   - Como fazer: Clique no botão **+ Equipamento** para iniciar o cadastro de um novo equipamento.
   - Campos/Opções disponíveis:
     * `Nome`: Campo de texto onde deve ser inserido o nome do equipamento, incluindo códigos e referências.
     * `Tipo`: Seletor para escolher entre "Alugado" ou "Próprio".
     * `Vínculo com Produto Principal`: Campo para associar o equipamento a um produto já cadastrado.
     * `Data de Aquisição`: Campo de data para registrar quando o equipamento foi adquirido.
     * `Local Alocado`: Campo de texto para indicar a obra onde o equipamento será utilizado.
     * `Especificação`: Campo opcional para detalhar marcas, parâmetros e tipos.
     * `Ano de Fabricação`: Campo numérico para registrar o ano de fabricação do equipamento.
     * `Ano do Modelo`: Campo numérico para registrar o ano do modelo do equipamento.
     * `Plano de Manutenção`: Checkbox para indicar se o equipamento requer manutenção regular.
   - Resultado esperado: Após preencher todos os campos obrigatórios e clicar em **Salvar**, o equipamento aparecerá na tela inicial na listagem de equipamentos.

2. **Definir Manutenção do Equipamento**
   - Localização: Tela de Cadastro de Equipamentos, seção de **Plano de Manutenção**
   - Como fazer: Se o checkbox de **Plano de Manutenção** estiver marcado, defina a frequência da manutenção e registre a data da última manutenção realizada.
   - Observações importantes: É crucial que as informações registradas sobre a manutenção estejam alinhadas com o que foi programado para evitar inconsistências.
   - Resultado esperado: As informações de manutenção serão salvas e poderão ser consultadas posteriormente na listagem de equipamentos.

3. **Visualizar Equipamentos Cadastrados**
   - Localização: Tela de Listagem de Equipamentos
   - Como fazer: Na tela inicial, todos os equipamentos cadastrados serão listados. Clique em um equipamento específico para visualizar seus detalhes.
   - Resultado esperado: Ao selecionar um equipamento, suas informações detalhadas serão exibidas, permitindo ao usuário revisar e editar conforme necessário.

**Campos e Parâmetros:**

| Campo                     | Tipo        | Obrigatório | Descrição                                                                 | Exemplo                  |
|---------------------------|-------------|-------------|---------------------------------------------------------------------------|--------------------------|
| Nome                      | Texto       | Sim         | Nome do equipamento, incluindo códigos e referências.                    | "Escavadeira_2024"      |
| Tipo                      | Seletor     | Sim         | Indica se o equipamento é "Alugado" ou "Próprio".                        | "Próprio"                |
| Vínculo com Produto       | Seletor     | Não         | Associa o equipamento a um produto principal já cadastrado.              | "Produto_A"             |
| Data de Aquisição         | Data        | Sim         | Data em que o equipamento foi adquirido.                                  | "2023-01-15"            |
| Local Alocado             | Texto       | Sim         | Local onde o equipamento será utilizado, geralmente a obra.              | "Obra_Centro"           |
| Especificação             | Texto       | Não         | Detalhes adicionais sobre o equipamento, como marcas e parâmetros.       | "Marca_X, Tipo_Y"       |
| Ano de Fabricação         | Numérico    | Sim         | Ano em que o equipamento foi fabricado.                                  | "2022"                   |
| Ano do Modelo             | Numérico    | Sim         | Ano do modelo do equipamento.                                             | "2023"                   |
| Plano de Manutenção       | Checkbox    | Não         | Indica se o equipamento requer um plano de manutenção regular.           | [✓]                     |

**Regras de Negócio:**
- Equipamentos podem ser desativados e reativados conforme a necessidade.
- Equipamentos próprios são cadastrados automaticamente após a entrada da nota de compra.
- Equipamentos alugados devem ser tratados como ordens de serviço, sem geração de estoque.
- A manutenção deve ser registrada e validada conforme o plano estabelecido.

**Observações Importantes:**
- É importante que o nome do equipamento seja claro e identificável para evitar confusões.
- Erros comuns incluem não preencher campos obrigatórios, o que impede o salvamento do cadastro.
- Verifique se o equipamento está corretamente vinculado ao produto principal, se aplicável.

**Conceitos-Chave:**
- **Equipamento Próprio**: Equipamento adquirido pela empresa, que gera estoque no sistema.
- **Equipamento Alugado**: Equipamento que não é de propriedade da empresa, tratado como uma ordem de serviço.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                             | Causa Provável                       | Solução                                           | Prevenção                                      |
|--------------------------------------|--------------------------------------|--------------------------------------------------|------------------------------------------------|
| Não consigo salvar o equipamento     | Campos obrigatórios não preenchidos  | Preencha todos os campos obrigatórios e tente novamente. | Verifique os campos antes de salvar.          |
| Equipamento não aparece na listagem  | Cadastro não foi realizado corretamente | Revise o cadastro e confirme se foi salvo.      | Sempre confirme a mensagem de sucesso após o cadastro. |
| Dificuldade em vincular produto      | Produto não cadastrado previamente   | Cadastre o produto principal antes de vincular. | Mantenha um registro atualizado dos produtos. |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre utilize nomes descritivos para facilitar a identificação dos equipamentos.
- Utilize a funcionalidade de manutenção para garantir que os equipamentos estejam sempre em boas condições.
- Revise periodicamente a listagem de equipamentos para garantir que todos estão ativos e atualizados.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Cadastro de Equipamento Próprio**
```
Situação: A empresa adquiriu uma nova escavadeira.
Ação: 
  • Campo Nome: "Escavadeira_2024"
  • Campo Tipo: "Próprio"
  • Campo Data de Aquisição: "2023-01-15"
  • Campo Local Alocado: "Obra_Centro"
Resultado: O equipamento é cadastrado e aparece na listagem de equipamentos.
```

**Exemplo 2: Cadastro de Equipamento Alugado**
```
Situação: A empresa precisa alugar um gerador.
Ação: 
  • Campo Nome: "Gerador_Alugado"
  • Campo Tipo: "Alugado"
  • Campo Data de Aquisição: "2023-02-01"
  • Campo Local Alocado: "Obra_Norte"
Resultado: O equipamento alugado é registrado como uma ordem de serviço e aparece na listagem.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O produto principal deve estar cadastrado para vinculação.
- **Habilita:** O gerenciamento de manutenção e relatórios de uso de equipamentos.
- **Relacionado a:** Módulo de Compras, onde os equipamentos próprios são adquiridos.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como cadastrar um equipamento?"
- **Com problema:** "Não consigo cadastrar um equipamento, o que fazer?"
- **Informal:** "Como eu coloco um equipamento no sistema?"
- **Por sintoma:** "O que fazer se o equipamento não aparece na lista?"
- **Com dúvida:** "Como saber se meu equipamento está ativo ou desativado?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Adicionar equipamento", "Cadastrar equipamento", "Novo equipamento", "Gerenciar equipamentos"
- "Equipamento alugado", "Equipamento próprio", "Cadastro de equipamentos"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como cadastrar um novo equipamento?
- O que fazer se o equipamento não aparece na listagem?
- Como desativar um equipamento?
- O que fazer se não consigo salvar o cadastro do equipamento?
- O que preciso fazer antes de cadastrar um equipamento alugado? 

---


---


---

## 8. Iniciar Transferência de Equipamentos e Registro de Manutenções

**📋 METADADOS:**
- **ID:** sec_8
- **⏱️ Minutagem:** 17:46 → 20:21
- **⏲️ Duração:** 155s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/6vX7wYe8cIw?si=5Xf_VmLvM7bj6M73&t=1066)
- **📦 Módulo:** Transferências e Manutenções
- **🏷️ Categorias:** Operacional, Gestão de Equipamentos, Manutenção
- **🔑 Palavras-chave:** transferência, equipamento, manutenção, histórico, alocação

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de iniciar a transferência de equipamentos e registrar manutenções no sistema, permitindo o acompanhamento do histórico de alocações e manutenções realizadas.

**Contexto:**
Estamos na tela de transferências do sistema, onde o usuário pode iniciar a transferência de equipamentos e registrar manutenções. O objetivo é garantir que o histórico de alocações e manutenções seja mantido de forma organizada e acessível.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Transferências e Manutenções > Tela de Transferências
- Tela/interface específica: Tela de Transferências

**Funcionalidade Detalhada:**
A funcionalidade permite ao usuário iniciar a transferência de equipamentos e registrar manutenções. Para produtos, a transferência é iniciada diretamente na tela de transferências. Para equipamentos, é necessário acessá-los, clicar em "mais transferência" e definir o local de destino. O fluxo é guiado para aprovar e gerar a entrada, mantendo um histórico das alocações, incluindo as obras em que o equipamento esteve e o período de permanência.

### 🔹 Passo a Passo Detalhado:

1. **Iniciar Transferência de Equipamento**
   - Localização: Tela de Transferências
   - Como fazer: Na tela de transferências, clique na opção para iniciar a transferência.
   - Campos/Opções disponíveis:
     * `Local de Destino`: Campo onde você deve definir o novo local para o equipamento.
   - Resultado esperado: A transferência é iniciada e o histórico de alocação é atualizado.

2. **Acessar Equipamento para Transferência**
   - Localização: Tela de Equipamentos
   - Como fazer: Selecione o equipamento desejado e clique em "mais transferência".
   - Observações importantes: Certifique-se de que o equipamento está disponível para transferência.
   - Resultado esperado: O sistema permite definir o local de destino para a transferência.

3. **Registrar Manutenção**
   - Localização: Tela de Manutenções
   - Como fazer: Clique na opção "solicitar manutenção".
   - Campos/Opções disponíveis:
     * `Motivo`: Campo onde você deve inserir o motivo da solicitação de manutenção.
   - Resultado esperado: A manutenção é registrada com a data de solicitação.

4. **Atualizar Status da Manutenção**
   - Localização: Tela de Manutenções
   - Como fazer: Clique na opção "mais comentário" e altere o status para "em andamento".
   - Observações importantes: Inclua a data e um comentário sobre o andamento da manutenção.
   - Resultado esperado: O status da manutenção é atualizado e o histórico é mantido.

5. **Finalizar Manutenção**
   - Localização: Tela de Manutenções
   - Como fazer: Clique novamente em "mais comentário" e altere o status para "finalizada".
   - Resultado esperado: O histórico da manutenção é atualizado com a conclusão.

6. **Baixar Equipamento**
   - Localização: Tela de Equipamentos
   - Como fazer: Quando o equipamento não for mais utilizado, clique na opção para dar baixa.
   - Campos/Opções disponíveis:
     * `Data`: Defina a data da baixa.
   - Resultado esperado: O equipamento é baixado do sistema.

**Campos e Parâmetros:**

| Campo               | Tipo       | Obrigatório | Descrição                                        | Exemplo               |
|---------------------|------------|-------------|--------------------------------------------------|-----------------------|
| `Local de Destino`  | Texto      | Sim         | Local onde o equipamento será transferido        | "Obra A"              |
| `Motivo`            | Texto      | Sim         | Motivo da solicitação de manutenção               | "Manutenção preventiva"|
| `Data`              | Data       | Sim         | Data em que a baixa do equipamento é realizada   | "2023-10-01"          |

**Regras de Negócio:**
- A transferência de equipamentos deve ser aprovada antes de ser finalizada.
- O registro de manutenções não influencia outros módulos do sistema, mas mantém um histórico.
- Cada manutenção deve passar pelas etapas de início, andamento e conclusão.

**Observações Importantes:**
- Sempre verifique se o equipamento está disponível para transferência antes de iniciar o processo.
- Evite registrar manutenções desnecessárias para manter o histórico limpo.
- A data de baixa deve ser a data em que o equipamento realmente não será mais utilizado.

**Conceitos-Chave:**
- **Transferência de Equipamento**: Processo de mover um equipamento de um local para outro, mantendo o histórico de alocações.
- **Registro de Manutenção**: Ação de documentar a solicitação e o andamento das manutenções realizadas em equipamentos.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                     | Solução                                        | Prevenção                                   |
|-----------------------------------|------------------------------------|------------------------------------------------|---------------------------------------------|
| Não consigo iniciar a transferência| Equipamento não disponível         | Verifique se o equipamento está disponível.    | Confirme a disponibilidade antes de iniciar.|
| Erro ao registrar manutenção       | Campo motivo não preenchido       | Preencha o campo motivo antes de salvar.      | Sempre verifique campos obrigatórios.      |
| Status da manutenção não atualiza  | Falta de comentários               | Adicione um comentário antes de atualizar.    | Inclua comentários sempre que atualizar.   |

**💡 DICAS E BOAS PRÁTICAS:**
- Utilize descrições claras nos campos de motivo para facilitar o acompanhamento.
- Mantenha o histórico de manutenções atualizado para evitar confusões futuras.
- Sempre revise as informações antes de salvar para evitar erros.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Solicitação de Manutenção**
```
Situação: O equipamento "Escavadeira X" precisa de manutenção preventiva.
Ação: 
  • Campo Motivo: "Manutenção preventiva"
Resultado: A manutenção é registrada com a data de solicitação e fica disponível no histórico.
```

**Exemplo 2: Transferência de Equipamento**
```
Situação: Transferir o equipamento "Guindaste Y" para a obra "Obra B".
Ação: 
  • Local de Destino: "Obra B"
Resultado: A transferência é iniciada e o histórico de alocação é atualizado.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O equipamento deve estar disponível para transferência.
- **Habilita:** O registro de manutenções permite acompanhar a periodicidade e o histórico de manutenções.
- **Relacionado a:** Funcionalidades de gestão de equipamentos e relatórios de manutenção.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como iniciar a transferência de um equipamento?"
- **Com problema:** "Não consigo registrar uma manutenção, o que fazer?"
- **Informal:** "Como faço para transferir um equipamento?"
- **Por sintoma:** "Quando o equipamento não está disponível, como proceder?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Transferir equipamento", "mover equipamento", "registrar manutenção", "solicitar manutenção", "dar baixa no equipamento".

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como iniciar a transferência de um equipamento?
- O que fazer se não consigo registrar uma manutenção?
- Como atualizar o status de uma manutenção?
- O que fazer se o equipamento não está disponível para transferência?
- O que preciso fazer antes de dar baixa em um equipamento? 

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
- **🔑 Palavras-chave:** balanço, estoque, inventário, produtos, quantidade, validação

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como realizar um balanço de estoque, permitindo a validação das quantidades de produtos entre o sistema e a obra, além de possibilitar a impressão e o envio de relatórios.

**Contexto:**
Estamos na funcionalidade de balanço de estoque dentro do módulo de Gestão de Estoque. O objetivo é garantir que as quantidades de produtos registradas no sistema correspondam às quantidades físicas disponíveis nas obras.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Gestão de Estoque > Balanço de Estoque
- Tela/interface específica: Tela de Balanço de Estoque

**Funcionalidade Detalhada:**
O balanço de estoque permite a conferência das quantidades de produtos disponíveis em uma obra em comparação com as registradas no sistema. É possível realizar o balanço a cada 7, 14, 21 ou 28 dias. O sistema fornece uma visão detalhada dos produtos, suas quantidades atuais e reais, e permite registrar diferenças como consumo ou entrada.

### 🔹 Passo a Passo Detalhado:

1. **Acessar o Balanço de Estoque**
   - Localização: Menu Principal > Gestão de Estoque > Balanço de Estoque
   - Como fazer: Clique na opção "Balanço de Estoque" para acessar a tela de balanço.
   - Campos/Opções disponíveis:
     * `Período`: Selecione a periodicidade desejada (7, 14, 21 ou 28 dias).
   - Resultado esperado: A tela de balanço é exibida, mostrando os produtos, quantidade atual e quantidade real.

2. **Conferir Quantidades de Produtos**
   - Localização: Tela de Balanço de Estoque
   - Como fazer: Compare as quantidades listadas. Por exemplo, se o sistema mostra 60 e na obra você tem 52, registre a diferença.
   - Observações importantes: As quantidades devem ser conferidas uma a uma para garantir precisão.
   - Resultado esperado: As diferenças são registradas corretamente.

3. **Registrar Diferenças**
   - Localização: Tela de Balanço de Estoque
   - Como fazer: Para registrar uma diferença, clique no campo correspondente ao produto e insira a quantidade correta.
   - Campos/Opções disponíveis:
     * `Quantidade Real`: Insira a quantidade encontrada na obra.
   - Resultado esperado: Se a quantidade for inferior, a diferença é registrada como consumo; se superior, como entrada.

4. **Salvar o Balanço**
   - Localização: Tela de Balanço de Estoque
   - Como fazer: Após registrar todas as diferenças, clique no botão **Salvar** e, em seguida, clique novamente em **Salvar** para confirmar.
   - Resultado esperado: O balanço é salvo, e as quantidades pendentes são exibidas.

5. **Visualizar Balanços Finalizados**
   - Localização: Tela de Balanço de Estoque
   - Como fazer: Acesse a seção de balanços finalizados para visualizar os registros anteriores.
   - Resultado esperado: Uma lista de balanços finalizados é exibida, permitindo a consulta de dados históricos.

6. **Imprimir ou Enviar Relatório**
   - Localização: Tela de Balanço de Estoque
   - Como fazer: Utilize a opção de impressão ou envio de relatório para compartilhar os dados com outros usuários.
   - Resultado esperado: O relatório é gerado e pode ser impresso ou enviado por e-mail.

**Campos e Parâmetros:**

| Campo               | Tipo    | Obrigatório | Descrição                                       | Exemplo         |
|---------------------|---------|-------------|-------------------------------------------------|------------------|
| `Período`           | Dropdown| Sim         | Define a periodicidade do balanço (7, 14, 21, 28 dias) | 14 dias         |
| `Quantidade Real`   | Numérico| Sim         | Quantidade de produtos encontrada na obra       | 52               |

**Regras de Negócio:**
- O balanço deve ser realizado a cada 7, 14, 21 ou 28 dias.
- Diferenças de quantidade devem ser registradas como consumo (se inferior) ou entrada (se superior).
- Produtos não conferidos permanecem como pendentes até que sejam validados.

**Observações Importantes:**
- Sempre verifique as quantidades com atenção para evitar erros.
- Caso um produto não esteja disponível, registre como consumo zero.
- É recomendável realizar o balanço em um horário em que a movimentação de produtos seja mínima.

**Conceitos-Chave:**
- **Balanço de Estoque**: Processo de conferência das quantidades de produtos disponíveis em comparação com o que está registrado no sistema.
- **Consumo**: Registro de uma quantidade inferior à registrada no sistema.
- **Entrada**: Registro de uma quantidade superior à registrada no sistema.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                      | Solução                                           | Prevenção                                         |
|-----------------------------------|-------------------------------------|---------------------------------------------------|--------------------------------------------------|
| Diferença não registrada           | Quantidade não conferida corretamente | Revise as quantidades e registre novamente         | Conferir todas as quantidades antes de salvar    |
| Balanço não salva                 | Erro de conexão ou falta de permissões | Verifique a conexão e as permissões do usuário    | Garantir que o usuário tenha permissões adequadas |
| Relatório não gera                 | Falta de dados completos            | Complete todos os campos obrigatórios antes de gerar | Conferir se todos os produtos foram validados    |

**💡 DICAS E BOAS PRÁTICAS:**
- Realize o balanço em um horário fixo para criar uma rotina.
- Utilize a impressão do relatório para facilitar a conferência física.
- Mantenha um registro dos balanços anteriores para comparação futura.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Conferência de Produtos**
```
Situação: Conferindo o estoque de cimento.
Ação: O sistema mostra 100 sacos de cimento, mas na obra há apenas 90.
  • Campo `Quantidade Real`: "90"
Resultado: A diferença de 10 sacos é registrada como consumo.
```

**Exemplo 2: Registro de Entrada**
```
Situação: Conferindo o estoque de areia.
Ação: O sistema mostra 50 m³ de areia, mas na obra há 55 m³.
Resultado: A diferença de 5 m³ é registrada como entrada.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O usuário deve ter acesso ao módulo de Gestão de Estoque.
- **Habilita:** A realização de balanços permite a atualização do inventário e a gestão de estoque.
- **Relacionado a:** Funcionalidades de relatórios e controle de estoque.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como realizar o balanço de estoque?"
- **Com problema:** "Não consigo registrar a diferença no balanço, o que fazer?"
- **Informal:** "Como eu faço pra conferir o estoque?"
- **Por sintoma:** "Quando a quantidade no sistema não bate com a da obra, como corrigir?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Conferir estoque", "validar estoque", "balanço de inventário", "controle de produtos"
- "Quantidade de produtos", "registro de estoque", "atualização de balanço"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como faço para realizar um balanço de estoque?
- O que fazer se as quantidades não conferem?
- Como posso imprimir o relatório do balanço?
- O que fazer se o balanço não está salvando?
- Quais são os períodos disponíveis para o balanço de estoque?

---


---


---

## 10. Gerenciamento de Estoque e Setores

**📋 METADADOS:**
- **ID:** sec_10
- **⏱️ Minutagem:** 22:49 → 25:24
- **⏲️ Duração:** 154s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/6vX7wYe8cIw?si=5Xf_VmLvM7bj6M73&t=1369)
- **📦 Módulo:** Suprimentos
- **🏷️ Categorias:** Configuração, Cadastro, Relatório, Operacional
- **🔑 Palavras-chave:** estoque, transferência, setores, histórico, movimentação, categorias, produtos

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como gerenciar o estoque de obras, incluindo a criação de relacionamentos entre obras, a visualização do histórico de movimentação e a configuração de setores. O objetivo é otimizar a organização e o controle do estoque.

**Contexto:**
Estamos na interface do módulo de suprimentos, onde o usuário pode gerenciar o estoque de produtos relacionados a obras. Esta seção foca em como criar relacionamentos entre obras, visualizar o histórico de movimentação e organizar o estoque em setores.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Suprimentos > Gerenciamento de Estoque
- Tela/interface específica: Tela de Estoque

**Funcionalidade Detalhada:**

Esta funcionalidade permite ao usuário criar relacionamentos entre diferentes obras, visualizar o histórico de movimentação de produtos e organizar o estoque em setores específicos. É útil para manter um controle rigoroso sobre as entradas e saídas de materiais, além de facilitar a consulta e a organização dos produtos.

### 🔹 Passo a Passo Detalhado:

1. **Criar Relacionamento entre Obras**
   - Localização: Tela de Estoque
   - Como fazer: Selecione a obra desejada na lista de obras disponíveis e clique no botão **Adicionar Relacionamento**.
   - Campos/Opções disponíveis:
     * `Obra`: Seleção da obra a ser relacionada.
   - Resultado esperado: Um novo relacionamento é criado entre as obras selecionadas, permitindo a transferência de produtos entre elas.

2. **Visualizar Histórico de Movimentação**
   - Localização: Tela de Estoque, seção "Histórico de Movimentação"
   - Como fazer: Role para baixo na tela de estoque até encontrar a seção "Histórico de Movimentação".
   - Observações importantes: O histórico mostrará todas as alterações feitas no estoque, incluindo transferências, balanços, entradas e saídas.
   - Resultado esperado: Uma lista com a data, hora e tipo de movimentação realizada.

3. **Criar Setores**
   - Localização: Tela de Estoque, botão **Mais Setor**
   - Como fazer: Clique no botão **Mais Setor** para adicionar um novo setor.
   - Campos/Opções disponíveis:
     * `Nome do Setor`: Campo para inserir o nome do setor (ex: Hidráulica, Elétrica, Materiais Diversos).
   - Resultado esperado: Um novo setor é criado, permitindo uma melhor organização dos produtos dentro do estoque.

4. **Configurar Controle de Estoque**
   - Localização: Tela de Estoque, seção de configuração de produtos
   - Como fazer: Clique em **Mais Produto** para adicionar um novo item ao estoque e defina a quantidade mínima e máxima.
   - Campos/Opções disponíveis:
     * `Produto`: Seleção do item a ser adicionado.
     * `Quantidade Mínima`: Campo para inserir a quantidade mínima permitida.
     * `Quantidade Máxima`: Campo para inserir a quantidade máxima permitida (opcional).
   - Resultado esperado: O sistema configurará o controle de estoque, gerando solicitações automáticas quando a quantidade mínima for atingida.

**Campos e Parâmetros:**

| Campo                   | Tipo        | Obrigatório | Descrição                                           | Exemplo                     |
|-------------------------|-------------|-------------|----------------------------------------------------|-----------------------------|
| `Obra`                  | Dropdown    | Sim         | Seleção da obra para criar relacionamento           | "Obra A"                    |
| `Nome do Setor`        | Texto       | Sim         | Nome do setor a ser criado                          | "Hidráulica"                |
| `Produto`               | Dropdown    | Sim         | Seleção do produto a ser adicionado ao estoque     | "Cimento"                   |
| `Quantidade Mínima`     | Numérico    | Sim         | Quantidade mínima permitida para o produto         | 10                          |
| `Quantidade Máxima`     | Numérico    | Não         | Quantidade máxima permitida para o produto         | 50                          |

**Regras de Negócio:**
- O sistema gera uma solicitação automática quando a quantidade de um produto fica abaixo da quantidade mínima configurada.
- As categorias de produtos podem ser expandidas com novas categorias e subcategorias conforme necessário.

**Observações Importantes:**
- É importante definir corretamente as quantidades mínimas para evitar faltas de produtos.
- Erros comuns incluem não configurar a quantidade mínima, resultando em falta de produtos.

**Conceitos-Chave:**
- **Histórico de Movimentação**: Registro de todas as alterações feitas no estoque, incluindo transferências e balanços.
- **Setor**: Divisão organizacional dentro do estoque para facilitar a consulta e o gerenciamento de produtos.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                | Solução                                         | Prevenção                               |
|-----------------------------------|-------------------------------|------------------------------------------------|-----------------------------------------|
| Solicitações automáticas não geradas | Quantidade mínima não configurada | Verifique se a quantidade mínima está definida | Sempre configurar a quantidade mínima   |
| Erro ao adicionar setor           | Nome do setor já existente    | Tente um nome diferente                        | Verifique a lista de setores existentes |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre revise o histórico de movimentação para manter controle sobre as alterações.
- Utilize setores para facilitar a localização de produtos no estoque.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Criando um Setor para Materiais Elétricos**
```
Situação: Você deseja organizar o estoque em setores.
Ação: Clique em **Mais Setor** e insira "Materiais Elétricos".
Resultado: O setor "Materiais Elétricos" é criado e os produtos podem ser alocados a ele.
```

**Exemplo 2: Configurando Estoque Mínimo para Cimento**
```
Situação: Você precisa garantir que nunca falte cimento no estoque.
Ação: Clique em **Mais Produto**, selecione "Cimento", e defina a quantidade mínima como 20.
Resultado: O sistema gerará uma solicitação quando a quantidade de cimento ficar abaixo de 20.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** As obras devem estar cadastradas antes de criar relacionamentos.
- **Habilita:** A visualização do histórico de movimentação e a organização em setores.
- **Relacionado a:** Módulo de Relatórios, onde você pode gerar relatórios sobre movimentações e estoque.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como criar um setor no estoque?"
- **Com problema:** "Não consigo visualizar o histórico de movimentação, o que fazer?"
- **Informal:** "Como eu organizo os produtos no estoque?"
- **Por sintoma:** "O que fazer se o sistema não gerar solicitações automáticas?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Adicionar setor", "Criar setor", "Organizar estoque", "Gerenciar produtos"
- "Histórico de movimentação", "Registro de movimentação", "Controle de estoque"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como criar um relacionamento entre obras?
- Como visualizar o histórico de movimentação no estoque?
- Como adicionar um novo setor no estoque?
- O que fazer se o sistema não gerar solicitações automáticas?
- O que preciso configurar antes de gerenciar o estoque?

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

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como cadastrar unidades de medida e embalagens no sistema, permitindo que os produtos sejam vinculados corretamente a suas especificações. Isso é essencial para a gestão eficiente de suprimentos.

**Contexto:**
Estamos no módulo de suprimentos do sistema, onde é possível gerenciar as especificações dos produtos, incluindo suas unidades de medida e embalagens. O objetivo desta seção é detalhar o processo de cadastro dessas informações, que são fundamentais para a correta operação do sistema.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Suprimentos > Submenu Cadastro de Produtos
- Tela/interface específica: Tela de Cadastro de Produtos

**Funcionalidade Detalhada:**
Esta funcionalidade permite ao usuário cadastrar novas unidades de medida e embalagens que serão utilizadas nos produtos. O cadastro correto dessas informações é crucial para garantir que os produtos sejam gerenciados de forma adequada dentro do sistema.

### 🔹 Passo a Passo Detalhado:

1. **Cadastrar Unidade de Medida**
   - Localização: Tela de Cadastro de Produtos, seção de unidades de medida.
   - Como fazer: Clique no botão **Mais Unidade** para iniciar o cadastro de uma nova unidade de medida.
   - Campos/Opções disponíveis:
     * `Nome`: Nome da unidade de medida (ex: "met²").
     * `Símbolo`: Símbolo que representa a unidade de medida (ex: "M2").
   - Resultado esperado: Após preencher os campos e clicar em **Salvar**, a nova unidade de medida será adicionada ao sistema e estará disponível para uso nos produtos.

2. **Cadastrar Embalagem**
   - Localização: Tela de Cadastro de Produtos, seção de embalagens.
   - Como fazer: Clique no botão **Mais Embalagem** para iniciar o cadastro de uma nova embalagem.
   - Campos/Opções disponíveis:
     * `Nome`: Nome da embalagem (ex: "Caixa de Papelão").
     * `Símbolo`: Símbolo que representa a embalagem (ex: "CP").
   - Observações importantes: Certifique-se de que a embalagem esteja cadastrada antes de vinculá-la ao produto.
   - Resultado esperado: Após preencher os campos e clicar em **Salvar**, a nova embalagem será adicionada ao sistema e estará disponível para uso no cadastro de produtos.

**Campos e Parâmetros:**

| Campo     | Tipo   | Obrigatório | Descrição                                   | Exemplo               |
|-----------|--------|-------------|---------------------------------------------|-----------------------|
| Nome      | Texto  | Sim         | Nome da unidade de medida ou embalagem      | "met²" ou "Caixa"     |
| Símbolo   | Texto  | Sim         | Símbolo que representa a unidade ou embalagem| "M2" ou "CP"          |

**Regras de Negócio:**
- As unidades de medida e embalagens devem ser cadastradas antes de serem vinculadas a um produto.
- Não é permitido cadastrar duas unidades de medida ou embalagens com o mesmo nome.

**Observações Importantes:**
- Ao cadastrar uma unidade de medida, verifique se o nome e o símbolo não estão em uso.
- Erros comuns incluem tentar salvar uma unidade de medida ou embalagem com um nome já existente.

**Conceitos-Chave:**
- **Unidade de Medida**: Refere-se a uma quantidade padrão utilizada para medir uma dimensão, como área, volume, peso, etc.
- **Embalagem**: Refere-se ao recipiente ou material utilizado para acondicionar um produto.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                      | Solução                                         | Prevenção                                   |
|-----------------------------------|-------------------------------------|------------------------------------------------|---------------------------------------------|
| Não consigo salvar a unidade de medida | Nome já cadastrado                  | Verifique se o nome da unidade é único e tente novamente. | Sempre verifique a lista de unidades cadastradas antes de criar uma nova. |
| Botão de salvar desabilitado      | Campos obrigatórios não preenchidos | Preencha todos os campos obrigatórios e tente novamente. | Certifique-se de que todos os campos obrigatórios estão preenchidos. |

**💡 DICAS E BOAS PRÁTICAS:**
- Utilize nomes claros e descritivos para unidades de medida e embalagens para facilitar a identificação.
- Mantenha um registro das unidades de medida e embalagens cadastradas para evitar duplicações.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Cadastro de Unidade de Medida**
```
Situação: Cadastro de uma nova unidade de medida para área.
Ação: 
  • Campo Nome: "met²"
  • Campo Símbolo: "M2"
Resultado: A unidade de medida "met²" com símbolo "M2" é cadastrada com sucesso e disponível para uso.
```

**Exemplo 2: Cadastro de Embalagem**
```
Situação: Cadastro de uma nova embalagem para produtos.
Ação: 
  • Campo Nome: "Caixa de Papelão"
  • Campo Símbolo: "CP"
Resultado: A embalagem "Caixa de Papelão" com símbolo "CP" é cadastrada com sucesso e disponível para uso.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** As unidades de medida e embalagens devem ser cadastradas antes de serem vinculadas a um produto.
- **Habilita:** O cadastro de produtos, permitindo a correta especificação de suas características.
- **Relacionado a:** Módulo de Estoque, onde as unidades de medida e embalagens são utilizadas para controle de inventário.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como cadastrar uma unidade de medida?"
- **Com problema:** "Não consigo cadastrar uma embalagem, o que fazer?"
- **Informal:** "Como eu coloco uma nova medida no sistema?"
- **Por sintoma:** "Quando tento salvar, dá erro, como resolver?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Adicionar unidade de medida", "Criar embalagem", "Cadastrar medida", "Novo símbolo", "Registrar embalagem".

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como cadastrar uma nova unidade de medida no sistema?
- Quais são os passos para adicionar uma embalagem?
- O que fazer se o nome da unidade de medida já estiver em uso?
- O que fazer se não consigo salvar a embalagem?
- O que preciso ter feito antes de cadastrar uma unidade de medida ou embalagem? 

---


---




---


## 🎬 DADOS DE TIMESTAMPS (Para Sistema RAG)


[VIDEO_TIMESTAMPS_DATA]

{
  "Passo a passo - Módulo de Suprimentos": [
    {
      "start": "00:00",
      "end": "02:34",
      "line": "Olá, neste vídeo iremos realizar uma apresentação completa do módulo de suplementos. Nosso primeiro "
    },
    {
      "start": "02:32",
      "end": "05:07",
      "line": "Na lateral também tem o campo de data limite de entrega. Essa data é configurada por vocês dentro de"
    },
    {
      "start": "05:04",
      "end": "07:37",
      "line": "quantidade real e o código da nota. Então, como dito, na entrada, vamos verificar se o previsto foi "
    },
    {
      "start": "07:35",
      "end": "10:10",
      "line": "utilizada, mas normalmente ela vai servir para uma referência de devolução de estoque, de uma entrad"
    },
    {
      "start": "10:08",
      "end": "12:42",
      "line": "Ao definir o local de origem, ele irá trazer uma referência dos produtos que estão dentro desse esto"
    },
    {
      "start": "12:40",
      "end": "15:13",
      "line": "demonstrativo, irei vincular com a categoria de pinturas, texturas e tintas e a subcategoria tintas."
    },
    {
      "start": "15:11",
      "end": "17:46",
      "line": "quanto aos produtos já cadastrados, também conseguimos visualizar um campo bem importante, que são o"
    },
    {
      "start": "17:46",
      "end": "20:21",
      "line": "temos um pouco abaixo a opção de iniciar a transferência. Então, para produto, a transferência é ini"
    },
    {
      "start": "20:18",
      "end": "22:52",
      "line": "pode definir é a relação de período. O balanço ele pode ser feito a cada 7, 14, 21 ou 28 dias. Aqui,"
    },
    {
      "start": "22:49",
      "end": "25:24",
      "line": "transferência entre as obras, é criado um relacionamento entre elas. Basta selecionar a obra e adici"
    },
    {
      "start": "25:21",
      "end": "26:02",
      "line": "Outro ponto, unidade de medida, que é utilizada no produto em alguns outros campos do sistema. Basta"
    }
  ]
}

[/VIDEO_TIMESTAMPS_DATA]
