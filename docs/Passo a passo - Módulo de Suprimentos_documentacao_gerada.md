## 1. Acesso ao Módulo de Suplementos

**Minutagem:** 00:00 → 02:00

**Contexto:**
Nesta seção, vamos acessar o módulo de suplementos do sistema, que é fundamental para gerenciar pedidos e solicitações de produtos.

**Localização no Sistema:**
- Menu Principal > Módulo Suplementos

**Funcionalidade Detalhada:**
O módulo de suplementos permite que os usuários realizem pedidos iniciais para iniciar o fluxo de compras. A primeira aba que acessaremos é a de solicitações, onde podemos criar novas solicitações de produtos.

### 🔹 Passo a Passo Detalhado:

1. **Acessar a Aba de Solicitações**
   - Localização: Menu Principal > Módulo Suplementos > Aba Solicitações
   - Como fazer: Clique na aba **Solicitações** para visualizar a interface de pedidos.
   - Resultado esperado: A tela de solicitações será exibida, permitindo que você veja as opções de pedidos.

2. **Criar uma Nova Solicitação**
   - Localização: Tela de Solicitações
   - Como fazer: Clique no botão **Mais Solicitação**.
   - Resultado esperado: Uma nova tela será aberta, mostrando uma listagem de todos os produtos já cadastrados no sistema.

3. **Buscar Produtos**
   - Localização: Tela de listagem de produtos
   - Como fazer: Utilize os filtros disponíveis para buscar produtos. Você pode filtrar por:
     * **Categoria**: Selecione uma categoria específica.
     * **Subcategoria**: Selecione uma subcategoria específica.
     * **Pesquisa Direta**: Digite o nome do produto na barra de pesquisa.
   - Resultado esperado: A lista de produtos será filtrada de acordo com os critérios selecionados.

**Campos e Parâmetros:**

| Campo          | Tipo    | Obrigatório | Descrição                                   | Exemplo          |
|----------------|---------|-------------|---------------------------------------------|-------------------|
| Categoria      | Dropdown| Sim         | Categoria do produto                        | Materiais         |
| Subcategoria   | Dropdown| Sim         | Subcategoria do produto                     | Tintas            |
| Pesquisa       | Texto   | Não         | Nome do produto para busca                  | Tinta Acrílica    |

**Regras de Negócio:**
- A pesquisa direta deve corresponder exatamente ao nome do produto para retornar resultados.
- Os filtros de categoria e subcategoria devem ser aplicados antes da pesquisa direta para refinar os resultados.

**Observações Importantes:**
- Utilize sempre os filtros para facilitar a busca de produtos.
- Caso não encontre o produto desejado, você pode clicar em **Mais Produto** para adicionar novos itens.

**Conceitos-Chave:**
- **Solicitação**: Pedido inicial para aquisição de produtos.
- **Filtro**: Ferramenta que permite refinar a busca de produtos.

---

## 2. Seleção de Produtos e Especificações

**Minutagem:** 02:00 → 04:00

**Contexto:**
Após acessar a tela de solicitações e buscar produtos, agora vamos selecionar um produto e definir suas especificações.

**Localização no Sistema:**
- Tela de listagem de produtos

**Funcionalidade Detalhada:**
Nesta etapa, você pode selecionar um produto da lista e definir suas especificações, como marca, parâmetros e cores.

### 🔹 Passo a Passo Detalhado:

1. **Selecionar um Produto**
   - Localização: Tela de listagem de produtos
   - Como fazer: Arraste o produto desejado para o lado ou clique no ícone da **mãozinha** ao lado do produto.
   - Resultado esperado: A tela de especificações do produto será exibida.

2. **Definir Especificações do Produto**
   - Localização: Tela de Especificações
   - Como fazer: Preencha os campos disponíveis, que podem incluir:
     * **Marca**: Selecione a marca do produto.
     * **Parâmetros**: Defina os parâmetros específicos do produto.
     * **Cores**: Escolha a cor desejada.
   - Resultado esperado: As especificações do produto serão salvas para a solicitação.

3. **Adicionar Quantidade**
   - Localização: Tela de Especificações
   - Como fazer: Insira a quantidade desejada no campo **Quantidade** e clique em **Adicionar**.
   - Resultado esperado: O produto com suas especificações e quantidade será adicionado à solicitação.

**Campos e Parâmetros:**

| Campo          | Tipo    | Obrigatório | Descrição                                   | Exemplo          |
|----------------|---------|-------------|---------------------------------------------|-------------------|
| Marca          | Dropdown| Sim         | Marca do produto                            | Marca X           |
| Parâmetros     | Texto   | Sim         | Parâmetros específicos do produto          | Parâmetro Y       |
| Cores          | Dropdown| Sim         | Cores disponíveis para o produto           | Azul              |
| Quantidade     | Número  | Sim         | Quantidade do produto a ser solicitado     | 10                |

**Regras de Negócio:**
- A quantidade deve ser um número inteiro positivo.
- As especificações devem ser preenchidas antes de adicionar o produto à solicitação.

**Observações Importantes:**
- Verifique se todas as especificações estão corretas antes de adicionar o produto.
- As especificações podem ser editadas posteriormente, caso necessário.

**Conceitos-Chave:**
- **Especificações**: Detalhes que definem as características de um produto.
- **Quantidade**: Número de unidades do produto a serem solicitadas.

---

## 3. Relacionamento com a Obra

**Minutagem:** 04:00 → 06:00

**Contexto:**
Após adicionar o produto à solicitação, precisamos estabelecer um relacionamento com a obra onde o produto será utilizado.

**Localização no Sistema:**
- Tela de Especificações

**Funcionalidade Detalhada:**
Esta funcionalidade permite vincular a solicitação a uma obra específica, o que é crucial para o acompanhamento do consumo e comparativos de planejamento.

### 🔹 Passo a Passo Detalhado:

1. **Selecionar Local de Consumo**
   - Localização: Tela de Especificações
   - Como fazer: No campo **Local de Consumo**, selecione a obra desejada a partir da lista de obras disponíveis.
   - Resultado esperado: A obra selecionada será vinculada à solicitação.

2. **Verificar Acompanhamento da Obra**
   - Localização: Tela de Especificações
   - Como fazer: Após selecionar a obra, verifique se a tela de **Especificar Serviços** é exibida. Isso indica que a obra possui acompanhamento pronto.
   - Resultado esperado: Se a tela de especificar serviços não aparecer, significa que a obra não possui acompanhamento completo.

3. **Especificar Serviços (se aplicável)**
   - Localização: Tela de Especificar Serviços
   - Como fazer: Se a tela estiver disponível, você pode vincular a solicitação a serviços de execução. Selecione os serviços que possuem recursos alocados ou não.
   - Resultado esperado: Os serviços selecionados serão vinculados à solicitação.

**Campos e Parâmetros:**

| Campo                | Tipo     | Obrigatório | Descrição                                   | Exemplo          |
|----------------------|----------|-------------|---------------------------------------------|-------------------|
| Local de Consumo     | Dropdown | Sim         | Obra onde o produto será utilizado         | Obra A            |
| Especificar Serviços  | Dropdown | Não         | Serviços relacionados à obra                | Serviço 1         |

**Regras de Negócio:**
- A obra deve estar previamente cadastrada no sistema para que possa ser selecionada.
- Se a obra não tiver acompanhamento, não será possível realizar comparativos.

**Observações Importantes:**
- Certifique-se de que a obra selecionada é a correta para evitar erros no consumo.
- O acompanhamento da obra é essencial para a gestão eficiente dos recursos.

**Conceitos-Chave:**
- **Obra**: Local onde os produtos serão utilizados.
- **Acompanhamento**: Monitoramento do progresso e consumo de recursos na obra.

---

## 4. Configuração da Data Limite de Entrega

**Minutagem:** 06:00 → 08:00

**Contexto:**
Agora que a obra está vinculada à solicitação, precisamos definir a data limite de entrega dos produtos solicitados.

**Localização no Sistema:**
- Tela de Especificações

**Funcionalidade Detalhada:**
A data limite de entrega é um campo importante que determina quando os produtos devem ser entregues. Isso impacta o status da solicitação e a urgência do pedido.

### 🔹 Passo a Passo Detalhado:

1. **Definir Data Limite de Entrega**
   - Localização: Tela de Especificações
   - Como fazer: No campo **Data Limite de Entrega**, insira a data desejada. Você pode configurá-la manualmente ou selecionar a partir de um calendário.
   - Resultado esperado: A data limite será salva e associada à solicitação.

2. **Configurar Prazo de Entrega**
   - Localização: Tela de Especificações
   - Como fazer: Caso tenha configurado o prazo de entrega para 7 dias, isso será refletido no campo. Se o solicitante precisar dos itens antes desse prazo, a solicitação será marcada como urgente.
   - Resultado esperado: O sistema ajustará o status da solicitação conforme a data limite.

3. **Exibir Limite ao Fornecedor**
   - Localização: Tela de Especificações
   - Como fazer: No campo **Exibir Limite ao Fornecedor**, selecione se deseja ou não exibir essa data ao fornecedor.
   - Resultado esperado: A configuração será salva e aplicada na comunicação com o fornecedor.

**Campos e Parâmetros:**

| Campo                        | Tipo     | Obrigatório | Descrição                                   | Exemplo          |
|------------------------------|----------|-------------|---------------------------------------------|-------------------|
| Data Limite de Entrega       | Data     | Sim         | Data limite para entrega dos produtos       | 2023-10-30        |
| Exibir Limite ao Fornecedor   | Checkbox | Não         | Indica se o limite será mostrado ao fornecedor | Sim/Não          |

**Regras de Negócio:**
- Se a data limite for inferior ao prazo configurado, a solicitação será marcada como urgente.
- A data deve ser uma data futura, não podendo ser retroativa.

**Observações Importantes:**
- A data limite deve ser definida com cuidado para evitar atrasos na entrega.
- A comunicação clara com o fornecedor é essencial para garantir a entrega no prazo.

**Conceitos-Chave:**
- **Data Limite de Entrega**: Prazo máximo para a entrega dos produtos solicitados.
- **Urgente**: Status que indica que a solicitação precisa ser tratada com prioridade.

---

## 5. Adição de Comentários à Solicitação

**Minutagem:** 08:00 → 10:00

**Contexto:**
Nesta seção, vamos aprender como adicionar comentários à solicitação, que podem ser úteis para comunicação com a equipe de compras e fornecedores.

**Localização no Sistema:**
- Tela de Especificações

**Funcionalidade Detalhada:**
Os comentários permitem que o solicitante adicione informações adicionais que podem ser relevantes para a aprovação do pedido ou para o fornecedor.

### 🔹 Passo a Passo Detalhado:

1. **Adicionar Comentários**
   - Localização: Tela de Especificações
   - Como fazer: Clique no campo de **Comentários** e digite a mensagem que deseja adicionar.
   - Resultado esperado: O comentário será salvo e associado à solicitação.

2. **Salvar a Solicitação**
   - Localização: Tela de Especificações
   - Como fazer: Após preencher todos os campos, clique no botão **Salvar** para finalizar a solicitação.
   - Resultado esperado: A solicitação será criada e aparecerá na lista de solicitações em aberto.

3. **Salvar como Rascunho (opcional)**
   - Localização: Tela de Especificações
   - Como fazer: Se preferir, você pode clicar em **Salvar como Rascunho** para retornar e editar mais tarde.
   - Resultado esperado: A solicitação será salva como rascunho e poderá ser editada posteriormente.

**Campos e Parâmetros:**

| Campo          | Tipo    | Obrigatório | Descrição                                   | Exemplo          |
|----------------|---------|-------------|---------------------------------------------|-------------------|
| Comentários     | Texto   | Não         | Mensagem adicional para a equipe de compras | "Urgente"         |

**Regras de Negócio:**
- Comentários podem ser editados ou removidos antes de salvar a solicitação.
- Solicitações salvas como rascunho podem ser editadas a qualquer momento antes da finalização.

**Observações Importantes:**
- Utilize os comentários para esclarecer dúvidas ou fornecer informações adicionais.
- Comentários claros e concisos ajudam na comunicação com a equipe de compras.

**Conceitos-Chave:**
- **Comentários**: Informações adicionais que podem ser anexadas a uma solicitação.
- **Rascunho**: Solicitação que ainda não foi finalizada e pode ser editada.

---

## 6. Edição e Exclusão de Solicitações

**Minutagem:** 10:00 → 12:00

**Contexto:**
Após salvar a solicitação, é importante saber como editar ou excluir pedidos, caso necessário.

**Localização no Sistema:**
- Tela de Solicitações

**Funcionalidade Detalhada:**
Esta funcionalidade permite que o solicitante faça alterações em solicitações existentes ou as exclua, dependendo do status da solicitação.

### 🔹 Passo a Passo Detalhado:

1. **Editar uma Solicitação**
   - Localização: Tela de Solicitações
   - Como fazer: Clique na solicitação que deseja editar e, em seguida, clique no botão **Editar**.
   - Resultado esperado: A tela de edição da solicitação será exibida, permitindo que você faça alterações.

2. **Excluir uma Solicitação**
   - Localização: Tela de Solicitações
   - Como fazer: Clique na solicitação que deseja excluir e, em seguida, clique no botão **Excluir**.
   - Resultado esperado: A solicitação será removida do sistema, desde que o status esteja em aberto.

3. **Verificar Status da Solicitação**
   - Localização: Tela de Solicitações
   - Como fazer: Verifique a coluna de **Status** para garantir que a solicitação esteja em aberto antes de tentar editar ou excluir.
   - Resultado esperado: Apenas solicitações com status "Em Aberto" podem ser editadas ou excluídas.

**Campos e Parâmetros:**

| Campo          | Tipo    | Obrigatório | Descrição                                   | Exemplo          |
|----------------|---------|-------------|---------------------------------------------|-------------------|
| Status         | Texto   | Sim         | Indica se a solicitação está em aberto ou finalizada | Em Aberto        |

**Regras de Negócio:**
- Solicitações com status "Finalizada" não podem ser editadas ou excluídas.
- Apenas o criador da solicitação pode realizar edições ou exclusões.

**Observações Importantes:**
- Sempre verifique o status antes de tentar editar ou excluir uma solicitação.
- Alterações em solicitações podem impactar o fluxo de compras.

**Conceitos-Chave:**
- **Edição**: Modificação de uma solicitação existente.
- **Exclusão**: Remoção de uma solicitação do sistema.

---

## 7. Acompanhamento da Situação da Solicitação

**Minutagem:** 12:00 → 14:00

**Contexto:**
Após criar a solicitação, é fundamental acompanhar sua situação e histórico de ações.

**Localização no Sistema:**
- Tela de Solicitações

**Funcionalidade Detalhada:**
Esta funcionalidade permite que o solicitante visualize o status da solicitação e o histórico de ações realizadas.

### 🔹 Passo a Passo Detalhado:

1. **Visualizar Solicitações em Aberto**
   - Localização: Tela de Solicitações
   - Como fazer: Na tela inicial, você verá uma lista de todas as solicitações em aberto.
   - Resultado esperado: A lista exibirá todas as solicitações, incluindo aquelas com status de urgente, se aplicável.

2. **Filtrar Solicitações**
   - Localização: Tela de Solicitações
   - Como fazer: Utilize as opções de filtro disponíveis para refinar a busca por solicitações.
   - Resultado esperado: A lista será atualizada com base nos critérios de filtro selecionados.

3. **Ver Histórico de Ações**
   - Localização: Tela de Solicitações
   - Como fazer: Clique na solicitação desejada para acessar o histórico de ações.
   - Resultado esperado: O histórico mostrará todas as ações realizadas na solicitação, como aprovações e alterações de status.

**Campos e Parâmetros:**

| Campo          | Tipo    | Obrigatório | Descrição                                   | Exemplo          |
|----------------|---------|-------------|---------------------------------------------|-------------------|
| Status         | Texto   | Sim         | Indica o status atual da solicitação       | Em Aberto         |
| Histórico      | Texto   | Não         | Registro de todas as ações realizadas       | "Solicitação aprovada em 01/10" |

**Regras de Negócio:**
- O histórico é atualizado automaticamente conforme ações são realizadas.
- Solicitações com status de urgente devem ser tratadas com prioridade.

**Observações Importantes:**
- Acompanhe regularmente o status das solicitações para evitar atrasos.
- Utilize o histórico para entender o fluxo de aprovações e alterações.

**Conceitos-Chave:**
- **Acompanhamento**: Monitoramento do status e ações de uma solicitação.
- **Histórico**: Registro de todas as ações realizadas em uma solicitação.

---

## 8. Acesso à Aba de Entradas

**Minutagem:** 14:00 → 16:00

**Contexto:**
Agora vamos acessar a aba de entradas, que é utilizada para verificar se os produtos solicitados chegaram conforme o previsto.

**Localização no Sistema:**
- Menu Principal > Módulo Suplementos > Aba Entradas

**Funcionalidade Detalhada:**
A aba de entradas permite que os usuários realizem conferências dos produtos que chegaram na obra, comparando as quantidades previstas com as recebidas.

### 🔹 Passo a Passo Detalhado:

1. **Acessar a Aba de Entradas**
   - Localização: Menu Principal > Módulo Suplementos > Aba Entradas
   - Como fazer: Clique na aba **Entradas** para visualizar a interface de conferência.
   - Resultado esperado: A tela de entradas será exibida, mostrando as opções de conferência.

2. **Gerar Entradas**
   - Localização: Tela de Entradas
   - Como fazer: Você pode gerar entradas a partir de diferentes processos, como lançamento de nota no financeiro ou transferência de produtos.
   - Resultado esperado: As entradas pendentes serão listadas, permitindo que você verifique as quantidades.

3. **Conferir Produtos**
   - Localização: Tela de Entradas
   - Como fazer: Clique na entrada pendente para verificar os produtos, setor, quantidade prevista e quantidade real.
   - Resultado esperado: As informações detalhadas da entrada serão exibidas, permitindo a conferência.

**Campos e Parâmetros:**

| Campo          | Tipo    | Obrigatório | Descrição                                   | Exemplo          |
|----------------|---------|-------------|---------------------------------------------|-------------------|
| Setor          | Dropdown| Sim         | Setor responsável pela conferência          | Setor A           |
| Quantidade Prevista | Número | Sim      | Quantidade que foi solicitada               | 10                |
| Quantidade Real | Número  | Sim         | Quantidade que chegou na obra               | 8                 |
| Código da Nota | Texto   | Não         | Código da nota fiscal relacionada           | 123456            |

**Regras de Negócio:**
- As quantidades devem ser conferidas e comparadas antes de finalizar a entrada.
- Entradas geradas a partir de notas ou transferências são automaticamente listadas.

**Observações Importantes:**
- A conferência deve ser feita com atenção para evitar divergências.
- Utilize sempre o código da nota para referência.

**Conceitos-Chave:**
- **Entrada**: Registro de produtos que chegaram na obra.
- **Conferência**: Verificação das quantidades recebidas em relação ao que foi solicitado.

---

## 9. Finalização de Entradas

**Minutagem:** 16:00 → 18:00

**Contexto:**
Após conferir as entradas, é necessário finalizar o processo, registrando as quantidades corretas.

**Localização no Sistema:**
- Tela de Entradas

**Funcionalidade Detalhada:**
Esta funcionalidade permite que o usuário finalize a entrada, registrando se as quantidades recebidas correspondem ao que foi solicitado.

### 🔹 Passo a Passo Detalhado:

1. **Salvar Conferência**
   - Localização: Tela de Entradas
   - Como fazer: Após conferir as quantidades, clique em **Salvar** para registrar a entrada.
   - Resultado esperado: A entrada será finalizada e os produtos estarão disponíveis no local de estoque.

2. **Salvar Novamente**
   - Localização: Tela de Entradas
   - Como fazer: Clique em **Salvar novamente** para confirmar a finalização da entrada.
   - Resultado esperado: A entrada será registrada como concluída no sistema.

3. **Verificar Divergências**
   - Localização: Tela de Entradas
   - Como fazer: Se as quantidades não baterem, o sistema solicitará uma justificativa para a divergência.
   - Resultado esperado: A entrada ficará sinalizada em amarelo, indicando que há divergências a serem resolvidas.

**Campos e Parâmetros:**

| Campo          | Tipo    | Obrigatório | Descrição                                   | Exemplo          |
|----------------|---------|-------------|---------------------------------------------|-------------------|
| Justificativa   | Texto   | Sim         | Motivo da divergência, se houver           | "Faltaram unidades" |

**Regras de Negócio:**
- Se as quantidades conferidas não coincidirem, uma justificativa deve ser fornecida.
- Entradas com divergências não são finalizadas até que a justificativa seja registrada.

**Observações Importantes:**
- Sempre verifique se as quantidades estão corretas antes de finalizar.
- A justificativa deve ser clara e objetiva para facilitar a resolução.

**Conceitos-Chave:**
- **Finalização**: Processo de concluir a entrada de produtos no sistema.
- **Divergência**: Diferença entre a quantidade solicitada e a quantidade recebida.

---

## 10. Gerenciamento de Divergências

**Minutagem:** 18:00 → 20:00

**Contexto:**
Quando há divergências nas entradas, é necessário gerenciá-las adequadamente para garantir que os registros estejam corretos.

**Localização no Sistema:**
- Tela de Entradas

**Funcionalidade Detalhada:**
Esta funcionalidade permite que o usuário tome ações em relação às divergências encontradas durante a conferência das entradas.

### 🔹 Passo a Passo Detalhado:

1. **Identificar Divergências**
   - Localização: Tela de Entradas
   - Como fazer: Clique na entrada pendente que apresenta divergências.
   - Resultado esperado: As informações sobre a divergência serão exibidas, incluindo quantidade prevista, recebida e a diferença.

2. **Tomar Ação sobre a Divergência**
   - Localização: Tela de Divergências
   - Como fazer: O responsável pode escolher entre três ações:
     * **Criar Entrada Vulsa**: Para registrar a quantidade restante dos produtos divergentes.
     * **Ignorar Divergência**: Para finalizar a entrada sem registrar a diferença.
     * **Gerar Crédito com o Fornecedor**: Para registrar o crédito referente à quantidade não recebida.
   - Resultado esperado: A ação escolhida será registrada e o fluxo será ajustado conforme a decisão.

3. **Registrar Justificativa**
   - Localização: Tela de Divergências
   - Como fazer: Após escolher a ação, insira uma justificativa no campo correspondente e clique em **Salvar**.
   - Resultado esperado: A justificativa será registrada e a ação será finalizada.

**Campos e Parâmetros:**

| Campo          | Tipo    | Obrigatório | Descrição                                   | Exemplo          |
|----------------|---------|-------------|---------------------------------------------|-------------------|
| Justificativa   | Texto   | Sim         | Motivo da escolha da ação sobre a divergência | "Produto não chegou" |

**Regras de Negócio:**
- A justificativa deve ser fornecida para qualquer ação tomada em relação a divergências.
- A opção de ignorar divergências deve ser usada com cautela, pois pode impactar o controle de estoque.

**Observações Importantes:**
- A escolha da ação deve ser feita com base em uma análise cuidadosa da situação.
- Mantenha um registro claro das justificativas para futuras referências.

**Conceitos-Chave:**
- **Divergência**: Diferença entre o que foi solicitado e o que foi recebido.
- **Ação**: Decisão tomada em relação a uma divergência identificada.

---

## 11. Entrada Vulsa

**Minutagem:** 20:00 → 22:00

**Contexto:**
A entrada vulsa é uma opção para registrar produtos que não se encaixam nos fluxos normais de entrada, como devoluções ou registros iniciais.

**Localização no Sistema:**
- Tela de Entradas

**Funcionalidade Detalhada:**
Esta funcionalidade permite que o usuário registre entradas que não estão ligadas a solicitações ou transferências, servindo para manter o controle do estoque.

### 🔹 Passo a Passo Detalhado:

1. **Iniciar uma Entrada Vulsa**
   - Localização: Tela de Entradas
   - Como fazer: Clique no botão **Mais Entrada** para iniciar uma nova entrada vulsa.
   - Resultado esperado: A tela de registro de entrada vulsa será exibida.

2. **Selecionar Produtos**
   - Localização: Tela de Entrada Vulsa
   - Como fazer: Escolha os produtos que deseja registrar na entrada vulsa a partir da listagem disponível.
   - Resultado esperado: Os produtos selecionados serão adicionados à entrada vulsa.

3. **Definir Local e Tipo de Entrada**
   - Localização: Tela de Entrada Vulsa
   - Como fazer: No campo **Local**, selecione a obra correspondente e no campo **Tipo**, escolha entre:
     * **Devolução ao Estoque**
     * **Registros Iniciais**
     * **Outros**
   - Resultado esperado: O tipo de entrada será registrado e associado aos produtos.

4. **Salvar a Entrada Vulsa**
   - Localização: Tela de Entrada Vulsa
   - Como fazer: Clique em **Salvar** para finalizar o registro da entrada vulsa.
   - Resultado esperado: A entrada vulsa será registrada no sistema e os produtos estarão disponíveis no estoque.

**Campos e Parâmetros:**

| Campo          | Tipo    | Obrigatório | Descrição                                   | Exemplo          |
|----------------|---------|-------------|---------------------------------------------|-------------------|
| Local          | Dropdown| Sim         | Obra onde a entrada será registrada        | Obra B            |
| Tipo           | Dropdown| Sim         | Tipo de entrada (Devolução, Registros Iniciais, Outros) | Devolução        |

**Regras de Negócio:**
- A entrada vulsa não interfere em outros módulos do sistema e é utilizada para registros específicos.
- O tipo de entrada deve ser selecionado corretamente para manter a organização do estoque.

**Observações Importantes:**
- Utilize a entrada vulsa para registrar produtos que não estão relacionados a solicitações normais.
- Mantenha um controle rigoroso das entradas vulsas para evitar confusões no estoque.

**Conceitos-Chave:**
- **Entrada Vulsa**: Registro de produtos que não se encaixam nos fluxos normais de entrada.
- **Tipo de Entrada**: Classificação da entrada registrada.

---

## 12. Registro de Consumo

**Minutagem:** 22:00 → 24:00

**Contexto:**
A aba de consumo é utilizada para registrar todos os itens utilizados em uma obra durante um determinado período.

**Localização no Sistema:**
- Menu Principal > Módulo Suplementos > Aba Consumo

**Funcionalidade Detalhada:**
Esta funcionalidade permite que os usuários registrem o consumo de produtos, mantendo um histórico de utilização.

### 🔹 Passo a Passo Detalhado:

1. **Acessar a Aba de Consumo**
   - Localização: Menu Principal > Módulo Suplementos > Aba Consumo
   - Como fazer: Clique na aba **Consumo** para visualizar a interface de registro.
   - Resultado esperado: A tela de consumo será exibida, permitindo o registro de itens utilizados.

2. **Iniciar Registro de Consumo**
   - Localização: Tela de Consumo
   - Como fazer: Clique no botão **Mais Consumo** para iniciar um novo registro.
   - Resultado esperado: A tela de registro de consumo será exibida.

3. **Selecionar Local de Consumo**
   - Localização: Tela de Registro de Consumo
   - Como fazer: No campo **Local de Consumo**, selecione a obra correspondente.
   - Resultado esperado: A obra será vinculada ao registro de consumo.

4. **Vincular ao Serviço (opcional)**
   - Localização: Tela de Registro de Consumo
   - Como fazer: Se a obra tiver acompanhamento, você pode vincular o consumo a um serviço específico.
   - Resultado esperado: O serviço será associado ao registro de consumo.

5. **Adicionar Produtos ao Consumo**
   - Localização: Tela de Registro de Consumo
   - Como fazer: Clique no ícone de **mais** ao lado dos produtos disponíveis para adicionar ao consumo.
   - Resultado esperado: Os produtos selecionados serão adicionados ao registro de consumo.

6. **Definir Quantidade de Uso**
   - Localização: Tela de Registro de Consumo
   - Como fazer: Insira a quantidade utilizada para cada produto adicionado.
   - Resultado esperado: As quantidades de uso serão registradas.

7. **Salvar o Registro de Consumo**
   - Localização: Tela de Registro de Consumo
   - Como fazer: Clique em **Salvar** para finalizar o registro.
   - Resultado esperado: O consumo será registrado e as quantidades serão retiradas do estoque.

**Campos e Parâmetros:**

| Campo          | Tipo    | Obrigatório | Descrição                                   | Exemplo          |
|----------------|---------|-------------|---------------------------------------------|-------------------|
| Local de Consumo | Dropdown| Sim         | Obra onde o consumo está sendo registrado   | Obra C            |
| Quantidade de Uso | Número | Sim         | Quantidade de produto utilizada             | 15                |

**Regras de Negócio:**
- O registro de consumo deve ser feito com base em produtos disponíveis no estoque.
- As quantidades devem ser atualizadas corretamente para refletir o consumo real.

**Observações Importantes:**
- Mantenha um controle rigoroso do consumo para evitar faltas de produtos.
- Utilize o histórico de consumo para planejamento futuro.

**Conceitos-Chave:**
- **Consumo**: Registro de produtos utilizados em uma obra.
- **Histórico de Consumo**: Registro das quantidades utilizadas ao longo do tempo.

---

## 13. Transferências de Produtos

**Minutagem:** 24:00 → 26:00

**Contexto:**
A aba de transferências permite que os usuários iniciem a transferência de produtos entre diferentes locais de estoque.

**Localização no Sistema:**
- Menu Principal > Módulo Suplementos > Aba Transferências

**Funcionalidade Detalhada:**
Esta funcionalidade é utilizada para gerenciar a movimentação de produtos entre obras ou locais de estoque.

### 🔹 Passo a Passo Detalhado:

1. **Acessar a Aba de Transferências**
   - Localização: Menu Principal > Módulo Suplementos > Aba Transferências
   - Como fazer: Clique na aba **Transferências** para visualizar a interface de gerenciamento.
   - Resultado esperado: A tela de transferências será exibida, permitindo o registro de movimentações.

2. **Iniciar uma Transferência**
   - Localização: Tela de Transferências
   - Como fazer: Clique no botão **Mais Transferência** para iniciar uma nova transferência.
   - Resultado esperado: A tela de registro de transferência será exibida.

3. **Definir Local de Origem e Destino**
   - Localização: Tela de Registro de Transferência
   - Como fazer: No campo **Local de Origem**, selecione a obra de onde os produtos serão transferidos e no campo **Local de Destino**, selecione a obra para onde os produtos serão enviados.
   - Resultado esperado: Os locais de origem e destino serão vinculados à transferência.

4. **Selecionar Produtos para Transferência**
   - Localização: Tela de Registro de Transferência
   - Como fazer: A partir da listagem de produtos disponíveis no local de origem, arraste os produtos desejados ou clique no ícone da **mãozinha**.
   - Resultado esperado: Os produtos selecionados serão adicionados à transferência.

5. **Definir Quantidade a Ser Transferida**
   - Localização: Tela de Registro de Transferência
   - Como fazer: Insira a quantidade que deseja transferir para cada produto selecionado.
   - Resultado esperado: As quantidades serão registradas para a transferência.

6. **Salvar a Transferência**
   - Localização: Tela de Registro de Transferência
   - Como fazer: Clique em **Salvar** para finalizar o registro da transferência.
   - Resultado esperado: A transferência será registrada como pendente e aguardará confirmação.

**Campos e Parâmetros:**

| Campo          | Tipo    | Obrigatório | Descrição                                   | Exemplo          |
|----------------|---------|-------------|---------------------------------------------|-------------------|
| Local de Origem | Dropdown| Sim         | Obra de onde os produtos estão sendo transferidos | Obra D            |
| Local de Destino | Dropdown| Sim         | Obra para onde os produtos estão sendo transferidos | Obra E            |
| Quantidade a Ser Transferida | Número | Sim | Quantidade de produto a ser transferida    | 5                 |

**Regras de Negócio:**
- A transferência deve ser registrada corretamente para garantir a movimentação adequada dos produtos.
- Apenas produtos disponíveis no local de origem podem ser transferidos.

**Observações Importantes:**
- Verifique as quantidades disponíveis antes de iniciar a transferência.
- Mantenha um registro claro das transferências para facilitar o controle de estoque.

**Conceitos-Chave:**
- **Transferência**: Movimentação de produtos entre diferentes locais de estoque.
- **Local de Origem**: Local de onde os produtos estão sendo enviados.

---

## 14. Confirmação de Transferências

**Minutagem:** 26:00 → 28:00

**Contexto:**
Após registrar uma transferência, é necessário confirmar a movimentação dos produtos no local de destino.

**Localização no Sistema:**
- Tela de Transferências

**Funcionalidade Detalhada:**
Esta funcionalidade permite que os usuários confirmem a transferência de produtos, garantindo que os registros estejam corretos.

### 🔹 Passo a Passo Detalhado:

1. **Acessar Transferências Pendentes**
   - Localização: Tela de Transferências
   - Como fazer: Clique na transferência pendente que deseja confirmar.
   - Resultado esperado: As informações da transferência serão exibidas, permitindo a confirmação.

2. **Verificar Produtos e Quantidades**
   - Localização: Tela de Transferências
   - Como fazer: Revise a lista de produtos, quantidades previstas e quantidades reais a serem transferidas.
   - Resultado esperado: As informações serão apresentadas para verificação.

3. **Confirmar Transferência**
   - Localização: Tela de Transferências
   - Como fazer: Após verificar as informações, clique em **Salvar** para confirmar a transferência.
   - Resultado esperado: A transferência será finalizada e os produtos estarão disponíveis no local de destino.

4. **Imprimir Romaneio (opcional)**
   - Localização: Tela de Transferências
   - Como fazer: Se desejar, selecione a opção de imprimir um arquivo de romaneio, que contém as informações da transferência.
   - Resultado esperado: Um documento será gerado com os detalhes da transferência.

**Campos e Parâmetros:**

| Campo          | Tipo    | Obrigatório | Descrição                                   | Exemplo          |
|----------------|---------|-------------|---------------------------------------------|-------------------|
| Produtos       | Texto   | Sim         | Lista de produtos a serem transferidos     | Produto A, Produto B |
| Quantidade Prevista | Número | Sim      | Quantidade prevista para a transferência    | 10                |
| Quantidade Real | Número  | Sim         | Quantidade que será confirmada              | 10                |

**Regras de Negócio:**
- A confirmação deve ser feita com base nas quantidades reais recebidas.
- Transferências não confirmadas permanecem pendentes no sistema.

**Observações Importantes:**
- Sempre verifique as quantidades antes de confirmar a transferência.
- O romaneio pode ser útil para documentação e controle.

**Conceitos-Chave:**
- **Confirmação**: Processo de validar a transferência de produtos.
- **Romaneio**: Documento que contém informações sobre a transferência realizada.

---

## 15. Acesso à Aba de Produtos

**Minutagem:** 28:00 → 30:00

**Contexto:**
Agora vamos acessar a aba de produtos, onde podemos visualizar e cadastrar novos produtos no sistema.

**Localização no Sistema:**
- Menu Principal > Módulo Suplementos > Aba Produtos

**Funcionalidade Detalhada:**
Esta funcionalidade permite que os usuários visualizem produtos já cadastrados e adicionem novos itens ao sistema.

### 🔹 Passo a Passo Detalhado:

1. **Acessar a Aba de Produtos**
   - Localização: Menu Principal > Módulo Suplementos > Aba Produtos
   - Como fazer: Clique na aba **Produtos** para visualizar a interface de gerenciamento de produtos.
   - Resultado esperado: A tela de produtos será exibida, mostrando a listagem de itens cadastrados.

2. **Cadastrar um Novo Produto**
   - Localização: Tela de Produtos
   - Como fazer: Clique no botão **Mais Produto** para iniciar o cadastro de um novo produto.
   - Resultado esperado: A tela de cadastro de produto será exibida.

3. **Preencher Informações do Produto**
   - Localização: Tela de Cadastro de Produto
   - Como fazer: Preencha os campos obrigatórios, que incluem:
     * **Nome do Produto**: Insira o nome do produto.
     * **Unidade de Medida**: Selecione a unidade de medida utilizada.
     * **Categorias e Subcategorias**: Escolha a categoria e subcategoria correspondentes.
   - Resultado esperado: As informações do produto serão salvas no sistema.

**Campos e Parâmetros:**

| Campo          | Tipo    | Obrigatório | Descrição                                   | Exemplo          |
|----------------|---------|-------------|---------------------------------------------|-------------------|
| Nome do Produto| Texto   | Sim         | Nome do produto a ser cadastrado           | Tinta Acrílica    |
| Unidade de Medida | Dropdown| Sim       | Unidade de medida do produto                | Litros            |
| Categoria      | Dropdown| Sim         | Categoria do produto                        | Pinturas          |
| Subcategoria   | Dropdown| Sim         | Subcategoria do produto                     | Tintas            |

**Regras de Negócio:**
- Todos os campos obrigatórios devem ser preenchidos antes de salvar o produto.
- O nome do produto deve ser único no sistema.

**Observações Importantes:**
- Utilize categorias e subcategorias para organizar melhor os produtos.
- Verifique se o produto já está cadastrado antes de criar um novo.

**Conceitos-Chave:**
- **Produto**: Item que pode ser solicitado e gerenciado no sistema.
- **Cadastro**: Processo de adicionar novos produtos ao sistema.

---

## 16. Configuração de Embalagens

**Minutagem:** 30:00 → 32:00

**Contexto:**
Após cadastrar um produto, é importante configurar as embalagens associadas a ele.

**Localização no Sistema:**
- Tela de Cadastro de Produto

**Funcionalidade Detalhada:**
Esta funcionalidade permite que os usuários definam como os produtos são embalados, facilitando o gerenciamento de estoque.

### 🔹 Passo a Passo Detalhado:

1. **Configurar Embalagens do Produto**
   - Localização: Tela de Cadastro de Produto
   - Como fazer: Na seção de **Embalagens**, clique em **Adicionar Embalagem**.
   - Resultado esperado: Um novo campo será exibido para inserir as informações da embalagem.

2. **Preencher Informações da Embalagem**
   - Localização: Tela de Embalagem
   - Como fazer: Insira as informações necessárias, como:
     * **Nome da Embalagem**: Nome que identifica a embalagem.
     * **Quantidade por Embalagem**: Quantidade de unidades que a embalagem contém.
   - Resultado esperado: As informações da embalagem serão salvas e associadas ao produto.

3. **Salvar as Configurações**
   - Localização: Tela de Cadastro de Produto
   - Como fazer: Clique em **Salvar** para finalizar o cadastro do produto e suas embalagens.
   - Resultado esperado: O produto e suas embalagens estarão registrados no sistema.

**Campos e Parâmetros:**

| Campo          | Tipo    | Obrigatório | Descrição                                   | Exemplo          |
|----------------|---------|-------------|---------------------------------------------|-------------------|
| Nome da Embalagem | Texto | Sim         | Nome da embalagem do produto                | Caixa             |
| Quantidade por Embalagem | Número | Sim | Quantidade de unidades na embalagem         | 12                |

**Regras de Negócio:**
- As embalagens devem ser configuradas para facilitar o controle de estoque.
- A quantidade por embalagem deve ser um número positivo.

**Observações Importantes:**
- Utilize embalagens para organizar melhor os produtos no estoque.
- Verifique se a embalagem está correta antes de salvar.

**Conceitos-Chave:**
- **Embalagem**: Forma como o produto é acondicionado.
- **Quantidade por Embalagem**: Número de unidades contidas em uma embalagem.

---

## 17. Cadastro de Equipamentos

**Minutagem:** 32:00 → 34:00

**Contexto:**
Agora vamos acessar a funcionalidade de cadastro de equipamentos, que permite gerenciar todos os equipamentos próprios e alugados.

**Localização no Sistema:**
- Menu Principal > Módulo Suplementos > Aba Equipamentos

**Funcionalidade Detalhada:**
Esta funcionalidade permite que os usuários cadastrem e gerenciem equipamentos, incluindo informações sobre custos e manutenção.

### 🔹 Passo a Passo Detalhado:

1. **Acessar a Aba de Equipamentos**
   - Localização: Menu Principal > Módulo Suplementos > Aba Equipamentos
   - Como fazer: Clique na aba **Equipamentos** para visualizar a interface de gerenciamento.
   - Resultado esperado: A tela de equipamentos será exibida, mostrando a listagem de itens cadastrados.

2. **Cadastrar um Novo Equipamento**
   - Localização: Tela de Equipamentos
   - Como fazer: Clique no botão **Mais Equipamento** para iniciar o cadastro de um novo equipamento.
   - Resultado esperado: A tela de cadastro de equipamento será exibida.

3. **Preencher Informações do Equipamento**
   - Localização: Tela de Cadastro de Equipamento
   - Como fazer: Preencha os campos obrigatórios, que incluem:
     * **Nome do Equipamento**: Insira o nome do equipamento.
     * **Data de Aquisição**: Insira a data em que o equipamento foi adquirido.
     * **Local Alocado**: Selecione a obra onde o equipamento será utilizado.
   - Resultado esperado: As informações do equipamento serão salvas no sistema.

**Campos e Parâmetros:**

| Campo          | Tipo    | Obrigatório | Descrição                                   | Exemplo          |
|----------------|---------|-------------|---------------------------------------------|-------------------|
| Nome do Equipamento | Texto | Sim         | Nome do equipamento a ser cadastrado       | Betoneira         |
| Data de Aquisição | Data  | Sim         | Data em que o equipamento foi adquirido    | 2023-01-15        |
| Local Alocado  | Dropdown| Sim         | Obra onde o equipamento será utilizado     | Obra F            |

**Regras de Negócio:**
- Todos os campos obrigatórios devem ser preenchidos antes de salvar o equipamento.
- O nome do equipamento deve ser único no sistema.

**Observações Importantes:**
- Utilize o cadastro de equipamentos para manter um controle rigoroso dos ativos.
- Verifique se o equipamento já está cadastrado antes de criar um novo.

**Conceitos-Chave:**
- **Equipamento**: Item que pode ser utilizado em obras e projetos.
- **Cadastro**: Processo de adicionar novos equipamentos ao sistema.

---

## 18. Registro de Manutenção de Equipamentos

**Minutagem:** 34:00 → 36:00

**Contexto:**
Após cadastrar um equipamento, é importante registrar as manutenções realizadas para garantir seu bom funcionamento.

**Localização no Sistema:**
- Tela de Equipamentos

**Funcionalidade Detalhada:**
Esta funcionalidade permite que os usuários registrem manutenções solicitadas e realizadas em equipamentos.

### 🔹 Passo a Passo Detalhado:

1. **Selecionar um Equipamento**
   - Localização: Tela de Equipamentos
   - Como fazer: Clique no equipamento que deseja registrar a manutenção.
   - Resultado esperado: As informações do equipamento selecionado serão exibidas.

2. **Solicitar Manutenção**
   - Localização: Tela de Equipamentos
   - Como fazer: Clique em **Solicitar Manutenção** e insira o motivo da manutenção.
   - Resultado esperado: A solicitação de manutenção será registrada no sistema.

3. **Atualizar Status da Manutenção**
   - Localização: Tela de Equipamentos
   - Como fazer: Após a manutenção ser iniciada, clique em **Mais Comentário** para atualizar o status para "Em Andamento" e insira a data.
   - Resultado esperado: O status da manutenção será atualizado e registrado.

4. **Finalizar Manutenção**
   - Localização: Tela de Equipamentos
   - Como fazer: Após a manutenção ser concluída, clique em **Mais Comentário** novamente para atualizar o status para "Finalizada".
   - Resultado esperado: O histórico da manutenção será atualizado com a conclusão.

**Campos e Parâmetros:**

| Campo          | Tipo    | Obrigatório | Descrição                                   | Exemplo          |
|----------------|---------|-------------|---------------------------------------------|-------------------|
| Motivo da Manutenção | Texto | Sim         | Motivo pelo qual a manutenção está sendo solicitada | "Quebra do motor" |
| Status         | Texto   | Sim         | Indica o status atual da manutenção         | Em Andamento      |

**Regras de Negócio:**
- O registro de manutenção deve ser feito com base em uma análise cuidadosa do equipamento.
- O histórico de manutenção deve ser mantido para futuras referências.

**Observações Importantes:**
- Mantenha um controle rigoroso das manutenções para garantir a eficiência dos equipamentos.
- Utilize o histórico para planejar futuras manutenções.

**Conceitos-Chave:**
- **Manutenção**: Processo de cuidar e reparar equipamentos.
- **Histórico de Manutenção**: Registro das manutenções realizadas em um equipamento.

---

## 19. Acesso à Aba de Balanços

**Minutagem:** 36:00 → 38:00

**Contexto:**
Agora vamos acessar a aba de balanços, que é utilizada para realizar inventários do estoque.

**Localização no Sistema:**
- Menu Principal > Módulo Suplementos > Aba Balanços

**Funcionalidade Detalhada:**
Esta funcionalidade permite que os usuários realizem balanços periódicos para verificar se as quantidades no sistema correspondem ao que está disponível na obra.

### 🔹 Passo a Passo Detalhado:

1. **Acessar a Aba de Balanços**
   - Localização: Menu Principal > Módulo Suplementos > Aba Balanços
   - Como fazer: Clique na aba **Balanços** para visualizar a interface de gerenciamento.
   - Resultado esperado: A tela de balanços será exibida, mostrando as opções de inventário.

2. **Gerar um Novo Balanço**
   - Localização: Tela de Balanços
   - Como fazer: Clique no botão **Gerar Balanço** para iniciar um novo balanço.
   - Resultado esperado: O balanço será gerado automaticamente com base nas configurações de período.

3. **Selecionar Período do Balanço**
   - Localização: Tela de Balanços
   - Como fazer: Escolha o período desejado para o balanço (7, 14, 21 ou 28 dias).
   - Resultado esperado: O balanço será gerado para o período selecionado.

4. **Conferir Produtos e Quantidades**
   - Localização: Tela de Balanços
   - Como fazer: Revise a lista de produtos, quantidade atual e quantidade real.
   - Resultado esperado: As informações serão apresentadas para verificação.

5. **Salvar o Balanço**
   - Localização: Tela de Balanços
   - Como fazer: Após conferir as quantidades, clique em **Salvar** para registrar o balanço.
   - Resultado esperado: O balanço será registrado no sistema.

**Campos e Parâmetros:**

| Campo          | Tipo    | Obrigatório | Descrição                                   | Exemplo          |
|----------------|---------|-------------|---------------------------------------------|-------------------|
| Período        | Dropdown| Sim         | Período para o qual o balanço será realizado | 14 dias           |
| Quantidade Atual | Número | Sim         | Quantidade que está registrada no sistema   | 20                |
| Quantidade Real | Número  | Sim         | Quantidade que foi verificada na obra       | 18                |

**Regras de Negócio:**
- O balanço deve ser realizado periodicamente para manter o controle do estoque.
- As quantidades devem ser conferidas e registradas corretamente.

**Observações Importantes:**
- Utilize o balanço para identificar discrepâncias entre o estoque físico e o registrado no sistema.
- Mantenha um registro claro dos balanços realizados.

**Conceitos-Chave:**
- **Balanço**: Inventário do estoque para verificar quantidades.
- **Período**: Intervalo de tempo para o qual o balanço é realizado.

---

## 20. Locais de Estoque

**Minutagem:** 38:00 → 40:00

**Contexto:**
Agora vamos acessar a aba de locais de estoque, onde podemos gerenciar as obras e seus respectivos estoques.

**Localização no Sistema:**
- Menu Principal > Módulo Suplementos > Aba Locais de Estoque

**Funcionalidade Detalhada:**
Esta funcionalidade permite que os usuários visualizem e gerenciem os locais de estoque, incluindo a configuração de setores e alertas.

### 🔹 Passo a Passo Detalhado:

1. **Acessar a Aba de Locais de Estoque**
   - Localização: Menu Principal > Módulo Suplementos > Aba Locais de Estoque
   - Como fazer: Clique na aba **Locais de Estoque** para visualizar a interface de gerenciamento.
   - Resultado esperado: A tela de locais de estoque será exibida, mostrando a listagem de obras.

2. **Selecionar uma Obra**
   - Localização: Tela de Locais de Estoque
   - Como fazer: Clique na obra que deseja gerenciar.
   - Resultado esperado: As informações da obra selecionada serão exibidas.

3. **Editar Configurações da Obra**
   - Localização: Tela de Locais de Estoque
   - Como fazer: Clique em **Editar** para modificar as configurações da obra, como periodicidade do balanço e prazo de limite de entrega.
   - Resultado esperado: A tela de edição será exibida, permitindo que você faça alterações.

4. **Adicionar Setores**
   - Localização: Tela de Locais de Estoque
   - Como fazer: Clique em **Mais Setor** para criar novos setores dentro da obra.
   - Resultado esperado: Um novo campo será exibido para inserir o nome do setor.

5. **Salvar Configurações**
   - Localização: Tela de Locais de Estoque
   - Como fazer: Após realizar as alterações, clique em **Salvar** para finalizar as configurações.
   - Resultado esperado: As configurações da obra serão atualizadas no sistema.

**Campos e Parâmetros:**

| Campo          | Tipo    | Obrigatório | Descrição                                   | Exemplo          |
|----------------|---------|-------------|---------------------------------------------|-------------------|
| Nome do Setor  | Texto   | Sim         | Nome do setor a ser criado                  | Hidráulica        |
| Periodicidade do Balanço | Dropdown | Sim | Frequência do balanço                       | 14 dias           |
| Prazo de Limite de Entrega | Número | Sim | Prazo para entrega dos produtos             | 7 dias            |

**Regras de Negócio:**
- As configurações devem ser atualizadas regularmente para garantir a eficiência do estoque.
- Setores devem ser criados para facilitar a organização dos produtos.

**Observações Importantes:**
- Utilize setores para categorizar os produtos de acordo com suas funções.
- Mantenha um controle rigoroso das configurações de cada obra.

**Conceitos-Chave:**
- **Local de Estoque**: Local onde os produtos estão armazenados.
- **Setor**: Divisão dentro da obra para organizar os produtos.

---

## 21. Controle de Estoque Mínimo

**Minutagem:** 40:00 → 42:00

**Contexto:**
Nesta seção, vamos aprender como configurar o controle de estoque mínimo para garantir que os produtos estejam sempre disponíveis.

**Localização no Sistema:**
- Tela de Locais de Estoque

**Funcionalidade Detalhada:**
Esta funcionalidade permite que os usuários definam limites mínimos de estoque para produtos, gerando solicitações automaticamente quando os níveis estiverem baixos.

### 🔹 Passo a Passo Detalhado:

1. **Acessar a Tela de Controle de Estoque**
   - Localização: Tela de Locais de Estoque
   - Como fazer: Clique na obra que deseja gerenciar e acesse a seção de controle de estoque.
   - Resultado esperado: As opções de controle de estoque serão exibidas.

2. **Adicionar Produto ao Controle de Estoque**
   - Localização: Tela de Controle de Estoque
   - Como fazer: Clique em **Mais Produto** para adicionar um novo item ao controle de estoque.
   - Resultado esperado: Um novo campo será exibido para selecionar o produto.

3. **Definir Quantidade Mínima**
   - Localização: Tela de Controle de Estoque
   - Como fazer: Insira a quantidade mínima desejada no campo correspondente.
   - Resultado esperado: A quantidade mínima será registrada e monitorada pelo sistema.

4. **Salvar Configurações de Estoque**
   - Localização: Tela de Controle de Estoque
   - Como fazer: Clique em **Salvar** para finalizar as configurações de controle de estoque.
   - Resultado esperado: As configurações serão salvas e o sistema monitorará os níveis de estoque.

**Campos e Parâmetros:**

| Campo          | Tipo    | Obrigatório | Descrição                                   | Exemplo          |
|----------------|---------|-------------|---------------------------------------------|-------------------|
| Produto        | Dropdown| Sim         | Produto a ser monitorado                   | Tinta Acrílica    |
| Quantidade Mínima | Número | Sim        | Quantidade mínima para o produto           | 5                 |

**Regras de Negócio:**
- O sistema deve gerar solicitações automaticamente quando a quantidade mínima for atingida.
- A quantidade mínima deve ser um número positivo.

**Observações Importantes:**
- Mantenha um controle rigoroso dos produtos para evitar faltas.
- Revise as quantidades mínimas periodicamente para garantir a eficiência do estoque.

**Conceitos-Chave:**
- **Controle de Estoque**: Monitoramento dos níveis de produtos disponíveis.
- **Quantidade Mínima**: Limite inferior que, quando atingido, gera uma solicitação.

---

## 22. Cadastro de Categorias e Subcategorias

**Minutagem:** 42:00 → 44:00

**Contexto:**
Agora vamos aprender como cadastrar categorias e subcategorias, que são essenciais para organizar os produtos no sistema.

**Localização no Sistema:**
- Menu Principal > Módulo Suplementos > Aba Categorias

**Funcionalidade Detalhada:**
Esta funcionalidade permite que os usuários criem categorias e subcategorias para facilitar a busca e organização dos produtos.

### 🔹 Passo a Passo Detalhado:

1. **Acessar a Aba de Categorias**
   - Localização: Menu Principal > Módulo Suplementos > Aba Categorias
   - Como fazer: Clique na aba **Categorias** para visualizar a interface de gerenciamento.
   - Resultado esperado: A tela de categorias será exibida, mostrando a listagem de itens cadastrados.

2. **Cadastrar uma Nova Categoria**
   - Localização: Tela de Categorias
   - Como fazer: Clique no botão **Mais Categoria** para iniciar o cadastro de uma nova categoria.
   - Resultado esperado: A tela de cadastro de categoria será exibida.

3. **Preencher Informações da Categoria**
   - Localização: Tela de Cadastro de Categoria
   - Como fazer: Insira o nome da nova categoria e clique em **Salvar**.
   - Resultado esperado: A nova categoria será registrada no sistema.

4. **Cadastrar uma Subcategoria**
   - Localização: Tela de Cadastro de Categoria
   - Como fazer: Após cadastrar a categoria, clique em **Mais Subcategoria** para adicionar uma subcategoria.
   - Resultado esperado: Um novo campo será exibido para inserir o nome da subcategoria.

5. **Salvar a Subcategoria**
   - Localização: Tela de Cadastro de Subcategoria
   - Como fazer: Insira o nome da subcategoria e clique em **Salvar**.
   - Resultado esperado: A subcategoria será registrada e associada à categoria principal.

**Campos e Parâmetros:**

| Campo          | Tipo    | Obrigatório | Descrição                                   | Exemplo          |
|----------------|---------|-------------|---------------------------------------------|-------------------|
| Nome da Categoria | Texto | Sim         | Nome da categoria a ser cadastrada         | Materiais         |
| Nome da Subcategoria | Texto | Sim      | Nome da subcategoria a ser cadastrada      | Tintas            |

**Regras de Negócio:**
- As categorias e subcategorias devem ser únicas no sistema.
- As subcategorias devem ser associadas a uma categoria principal.

**Observações Importantes:**
- Utilize categorias e subcategorias para organizar os produtos de forma eficiente.
- Revise as categorias periodicamente para garantir que estejam atualizadas.

**Conceitos-Chave:**
- **Categoria**: Agrupamento de produtos com características semelhantes.
- **Subcategoria**: Divisão dentro de uma categoria para maior especificidade.

---

## 23. Cadastro de Unidades de Medida

**Minutagem:** 44:00 → 46:00

**Contexto:**
Agora vamos aprender como cadastrar unidades de medida, que são essenciais para a gestão de produtos no sistema.

**Localização no Sistema:**
- Menu Principal > Módulo Suplementos > Aba Unidades de Medida

**Funcionalidade Detalhada:**
Esta funcionalidade permite que os usuários criem unidades de medida que serão utilizadas no cadastro de produtos.

### 🔹 Passo a Passo Detalhado:

1. **Acessar a Aba de Unidades de Medida**
   - Localização: Menu Principal > Módulo Suplementos > Aba Unidades de Medida
   - Como fazer: Clique na aba **Unidades de Medida** para visualizar a interface de gerenciamento.
   - Resultado esperado: A tela de unidades de medida será exibida, mostrando a listagem de itens cadastrados.

2. **Cadastrar uma Nova Unidade de Medida**
   - Localização: Tela de Unidades de Medida
   - Como fazer: Clique no botão **Mais Unidade** para iniciar o cadastro de uma nova unidade de medida.
   - Resultado esperado: A tela de cadastro de unidade de medida será exibida.

3. **Preencher Informações da Unidade de Medida**
   - Localização: Tela de Cadastro de Unidade de Medida
   - Como fazer: Insira o nome da unidade de medida e o símbolo correspondente, e clique em **Salvar**.
   - Resultado esperado: A nova unidade de medida será registrada no sistema.

**Campos e Parâmetros:**

| Campo          | Tipo    | Obrigatório | Descrição                                   | Exemplo          |
|----------------|---------|-------------|---------------------------------------------|-------------------|
| Nome da Unidade | Texto  | Sim         | Nome da unidade de medida a ser cadastrada | Metro             |
| Símbolo        | Texto   | Sim         | Símbolo que representa a unidade de medida | m                 |

**Regras de Negócio:**
- As unidades de medida devem ser únicas no sistema.
- O símbolo deve ser claro e representativo da unidade.

**Observações Importantes:**
- Utilize unidades de medida para garantir a precisão nas quantidades dos produtos.
- Revise as unidades periodicamente para garantir que estejam atualizadas.

**Conceitos-Chave:**
- **Unidade de Medida**: Sistema de medida utilizado para quantificar produtos.
- **Símbolo**: Representação abreviada da unidade de medida.

---

## 24. Cadastro de Embalagens

**Minutagem:** 46:00 → 48:00

**Contexto:**
Agora vamos aprender como cadastrar embalagens, que são importantes para o gerenciamento de produtos no sistema.

**Localização no Sistema:**
- Menu Principal > Módulo Suplementos > Aba Embalagens

**Funcionalidade Detalhada:**
Esta funcionalidade permite que os usuários criem embalagens que serão utilizadas no cadastro de produtos.

### 🔹 Passo a Passo Detalhado:

1. **Acessar a Aba de Embalagens**
   - Localização: Menu Principal > Módulo Suplementos > Aba Embalagens
   - Como fazer: Clique na aba **Embalagens** para visualizar a interface de gerenciamento.
   - Resultado esperado: A tela de embalagens será exibida, mostrando a listagem de itens cadastrados.

2. **Cadastrar uma Nova Embalagem**
   - Localização: Tela de Embalagens
   - Como fazer: Clique no botão **Mais Embalagem** para iniciar o cadastro de uma nova embalagem.
   - Resultado esperado: A tela de cadastro de embalagem será exibida.

3. **Preencher Informações da Embalagem**
   - Localização: Tela de Cadastro de Embalagem
   - Como fazer: Insira o nome da embalagem e o símbolo correspondente, e clique em **Salvar**.
   - Resultado esperado: A nova embalagem será registrada no sistema.

**Campos e Parâmetros:**

| Campo          | Tipo    | Obrigatório | Descrição                                   | Exemplo          |
|----------------|---------|-------------|---------------------------------------------|-------------------|
| Nome da Embalagem | Texto | Sim         | Nome da embalagem a ser cadastrada         | Caixa             |
| Símbolo        | Texto   | Sim         | Símbolo que representa a embalagem         | cx                |

**Regras de Negócio:**
- As embalagens devem ser únicas no sistema.
- O símbolo deve ser claro e representativo da embalagem.

**Observações Importantes:**
- Utilize embalagens para garantir a organização dos produtos no estoque.
- Revise as embalagens periodicamente para garantir que estejam atualizadas.

**Conceitos-Chave:**
- **Embalagem**: Forma como o produto é acondicionado.
- **Símbolo**: Representação abreviada da embalagem.

---

## 25. Conclusão do Módulo de Suprimentos

**Minutagem:** 48:00 → 50:00

**Contexto:**
Nesta seção, vamos concluir a apresentação do módulo de suprimentos, revisando os principais pontos abordados.

**Localização no Sistema:**
- N/A

**Funcionalidade Detalhada:**
O módulo de suprimentos é essencial para gerenciar pedidos, entradas, consumos e equipamentos, garantindo a eficiência na gestão de recursos.

### 🔹 Passo a Passo Detalhado:

1. **Revisar Funcionalidades**
   - Localização: N/A
   - Como fazer: Revise as funcionalidades abordadas, como solicitações, entradas, consumos, transferências, e cadastros.
   - Resultado esperado: Uma compreensão clara de como cada funcionalidade contribui para a gestão de suprimentos.

2. **Praticar o Uso do Módulo**
   - Localização: N/A
   - Como fazer: Utilize o sistema para praticar as funcionalidades aprendidas.
   - Resultado esperado: Familiarização com o sistema e aumento da eficiência no uso do módulo.

3. **Consultar a Documentação**
   - Localização: N/A
   - Como fazer: Consulte a documentação sempre que necessário para esclarecer dúvidas.
   - Resultado esperado: Acesso a informações detalhadas sobre o uso do módulo.

**Observações Importantes:**
- O módulo de suprimentos é uma ferramenta poderosa para a gestão de recursos.
- A prática constante e a consulta à documentação são essenciais para o domínio do sistema.

**Conceitos-Chave:**
- **Módulo de Suprimentos**: Conjunto de funcionalidades para gerenciar pedidos e recursos.
- **Gestão de Recursos**: Processo de administrar e otimizar o uso de materiais e equipamentos.

---

Essa documentação detalhada cobre todas as funcionalidades do módulo de suprimentos, seguindo a estrutura solicitada e garantindo que cada seção seja autossuficiente e rica em detalhes.