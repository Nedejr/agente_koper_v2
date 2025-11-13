# 📚 Documentação: Passo a passo - Módulo Financeiro

**🎥 Vídeo Original:** https://youtu.be/DMvowd7eCAA?si=qrXiuODXTH9y2zNZ

**📊 Total de Seções:** 18

---

---

## 1. Cadastro de Contas Bancárias no Módulo Financeiro

**📋 METADADOS:**
- **ID:** sec_1
- **⏱️ Minutagem:** 00:03 → 02:35
- **⏲️ Duração:** 152s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/DMvowd7eCAA?si=qrXiuODXTH9y2zNZ&t=3)
- **📦 Módulo:** Financeiro
- **🏷️ Categorias:** Cadastro, Configuração, Operacional
- **🔑 Palavras-chave:** conta bancária, saldo inicial, chave Pix, bloqueio, movimentações financeiras, permissões, extrato

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de cadastro de contas bancárias no módulo financeiro, incluindo campos obrigatórios, configurações de bloqueio e permissões de usuários, permitindo um gerenciamento eficaz das contas.

**Contexto:**
Estamos no módulo financeiro do sistema, onde o objetivo é cadastrar e gerenciar contas bancárias. Este processo é fundamental para o controle financeiro e a validação de saldos.

**Localização no Sistema:**
- Caminho de navegação: Menu Principal > Módulo Financeiro > Cadastro de Contas Bancárias
- Tela/interface específica: Tela de Cadastro de Contas Bancárias

**Funcionalidade Detalhada:**

O cadastro de contas bancárias permite que os usuários registrem informações essenciais sobre suas contas, como tipo de conta, saldo inicial e configurações de movimentação. É crucial para o acompanhamento do saldo atual e para a validação com o saldo físico.

### 🔹 Passo a Passo Detalhado:

1. **Selecionar o Tipo de Conta**
   - Localização: Tela de Cadastro de Contas Bancárias
   - Como fazer: Clique no campo de seleção para escolher o tipo de conta desejado.
   - Campos/Opções disponíveis:
     * `Tipo de Conta`: Opções incluem "Corrente", "Poupança", "Conta Salário", entre outros.
   - Resultado esperado: O tipo de conta selecionado será exibido no campo.

2. **Preencher Campos Obrigatórios**
   - Localização: Tela de Cadastro de Contas Bancárias
   - Como fazer: Preencha todos os campos marcados com um asterisco (*), que indica que são obrigatórios.
   - Campos/Opções disponíveis:
     * `Nome da Conta`: Campo de texto para nomear a conta.
     * `Banco`: Campo de seleção para escolher o banco da conta.
   - Resultado esperado: O sistema aceita o cadastro se todos os campos obrigatórios forem preenchidos corretamente.

3. **Inserir Saldo Inicial**
   - Localização: Tela de Cadastro de Contas Bancárias
   - Como fazer: Insira o valor do saldo inicial no campo correspondente.
   - Observações importantes: Embora não seja obrigatório, é recomendado preencher este campo para acompanhar o saldo atual.
   - Resultado esperado: O saldo inicial é salvo e pode ser visualizado posteriormente.

4. **Adicionar Chave Pix**
   - Localização: Tela de Cadastro de Contas Bancárias
   - Como fazer: Se a conta possui chave Pix, selecione o tipo da chave (ex: CPF, CNPJ, e-mail) e insira o valor correspondente.
   - Campos/Opções disponíveis:
     * `Tipo de Chave`: Opções incluem "CPF", "CNPJ", "E-mail", "Telefone".
   - Resultado esperado: A chave Pix é registrada e associada à conta.

5. **Configurar Período de Bloqueio**
   - Localização: Tela de Cadastro de Contas Bancárias
   - Como fazer: Defina um período para bloqueio de movimentações financeiras, especificando a data de início e a data de término.
   - Observações importantes: O bloqueio impede movimentações financeiras para a conta durante o período definido e retroativamente.
   - Resultado esperado: O sistema não permitirá movimentações financeiras dentro do período bloqueado.

6. **Selecionar Tipo de Cheques (se aplicável)**
   - Localização: Tela de Cadastro de Contas Bancárias
   - Como fazer: Se a conta emite cheques, selecione a opção "Emit Check" e escolha o tipo de cheques.
   - Campos/Opções disponíveis:
     * `Tipo de Cheque`: Opções incluem "Cheque Normal", "Cheque Especial".
   - Resultado esperado: O tipo de cheque é registrado e associado à conta.

7. **Definir Permissões de Usuários**
   - Localização: Tela de Cadastro de Contas Bancárias
   - Como fazer: Configure as permissões para usuários que terão acesso à conta bancária.
   - Observações importantes: É possível restringir ou permitir acesso total às informações da conta.
   - Resultado esperado: As permissões são salvas e aplicadas aos usuários selecionados.

8. **Visualizar Extrato da Conta**
   - Localização: Tela de Cadastro de Contas Bancárias
   - Como fazer: Após realizar movimentações financeiras, acesse o extrato da conta para visualizar entradas e saídas.
   - Resultado esperado: O extrato exibe todas as movimentações realizadas, permitindo um acompanhamento detalhado.

9. **Realizar Movimentações Financeiras**
   - Localização: Tela de Cadastro de Contas Bancárias
   - Como fazer: Realize movimentações de entrada ou saída diretamente na conta, sem a necessidade de acessar contas a pagar ou a receber.
   - Observações importantes: Movimentações feitas diretamente na conta não geram registros em contas a pagar ou a receber, apenas aparecem no extrato e no fluxo de caixa.
   - Resultado esperado: As movimentações são registradas no extrato da conta.

**Campos e Parâmetros:**

| Campo                | Tipo         | Obrigatório | Descrição                                           | Exemplo            |
|----------------------|--------------|-------------|----------------------------------------------------|--------------------|
| `Tipo de Conta`      | Dropdown     | Sim         | Seleciona o tipo de conta bancária.                | Corrente           |
| `Nome da Conta`      | Texto        | Sim         | Nome que identifica a conta bancária.              | Conta Pessoal      |
| `Banco`              | Dropdown     | Sim         | Seleciona o banco onde a conta está registrada.    | Banco do Brasil     |
| `Saldo Inicial`      | Numérico     | Não         | Valor inicial da conta para controle de saldo.     | 1000.00            |
| `Tipo de Chave`      | Dropdown     | Não         | Tipo de chave Pix associada à conta.               | CPF                |
| `Data de Início`     | Data         | Não         | Data de início do bloqueio de movimentações.       | 01/08/2023         |
| `Data de Término`    | Data         | Não         | Data de término do bloqueio de movimentações.      | 31/08/2023         |
| `Tipo de Cheque`     | Dropdown     | Não         | Tipo de cheque que pode ser emitido pela conta.    | Cheque Normal      |
| `Permissões de Usuário` | Checkbox   | Não         | Define se o usuário terá acesso à conta.           | [ ] Acesso Total   |

**Regras de Negócio:**
- Campos obrigatórios devem ser preenchidos para que o cadastro da conta seja aceito.
- O saldo inicial, embora não obrigatório, é recomendado para controle financeiro.
- O bloqueio de movimentações impede qualquer transação durante o período especificado e retroativamente.
- Movimentações financeiras realizadas diretamente na conta não geram registros em contas a pagar ou a receber.

**Observações Importantes:**
- É importante validar se o saldo inicial cadastrado bate com o saldo físico da conta.
- Evite deixar campos obrigatórios em branco, pois isso impede o cadastro.
- Lembre-se de revisar as permissões de usuários para garantir a segurança das informações.

**Conceitos-Chave:**
- **Chave Pix**: Identificador utilizado para realizar transferências instantâneas via sistema Pix.
- **Bloqueio de Movimentações**: Configuração que impede transações financeiras em um período específico.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como cadastrar uma nova conta bancária no sistema?
- Quais campos são obrigatórios no cadastro de contas bancárias?
- Como configurar um bloqueio de movimentações financeiras para uma conta?

---


---


---

## 2. Conciliação de Extratos Bancários

**📋 METADADOS:**
- **ID:** sec_2
- **⏱️ Minutagem:** 02:33 → 05:06
- **⏲️ Duração:** 152s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/DMvowd7eCAA?si=qrXiuODXTH9y2zNZ&t=153)
- **📦 Módulo:** Conciliação Bancária
- **🏷️ Categorias:** Relatório, Operacional, Configuração
- **🔑 Palavras-chave:** conciliação, extrato, OFX, importação, COPER, movimentações, validação

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como realizar a conciliação de extratos bancários no sistema, permitindo a validação dos valores do extrato importado com os lançamentos registrados no sistema COPER.

**Contexto:**
Estamos na funcionalidade de conciliação bancária do sistema, onde o usuário pode importar extratos bancários no formato OFX e validar os valores lançados no sistema com os valores do extrato.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Conciliação Bancária > Submenu Importar Extrato
- Tela/interface específica: Tela de Conciliação

**Funcionalidade Detalhada:**
A funcionalidade de conciliação permite que os usuários importem extratos bancários no formato OFX e comparem os valores contidos no extrato com os lançamentos registrados no sistema COPER. O objetivo é validar se todos os lançamentos estão corretos e se não há valores faltantes.

### 🔹 Passo a Passo Detalhado:

1. **Exportar Relatório do Extrato**
   - Localização: Tela de Conciliação
   - Como fazer: O usuário deve primeiro exportar o extrato da conta bancária desejada no formato OFX. Este arquivo será utilizado para a importação no sistema.
   - Campos/Opções disponíveis:
     * `Formato`: OFX (o sistema aceita apenas este formato para importação)
   - Resultado esperado: O extrato bancário é salvo no formato OFX no dispositivo do usuário.

2. **Importar Extrato**
   - Localização: Tela de Conciliação, botão **Importar Extrato**
   - Como fazer: Após ter o arquivo OFX, o usuário deve clicar no botão **Importar Extrato**. Uma janela de seleção de arquivo será aberta, onde o usuário deve localizar e selecionar o arquivo OFX exportado.
   - Observações importantes: Certifique-se de que o arquivo está no formato OFX, pois outros formatos não serão aceitos.
   - Resultado esperado: O sistema processa o arquivo e exibe todos os valores do extrato importado em uma lista à esquerda da tela.

3. **Validação dos Valores**
   - Localização: Tela de Conciliação, área de comparação de valores
   - Como fazer: Após a importação, o usuário verá os valores do extrato à esquerda e os valores lançados no sistema à direita. O usuário deve comparar ambos os lados para identificar discrepâncias.
   - Observações importantes: Se o sistema não reconheceu automaticamente os valores, isso pode indicar que os lançamentos não foram feitos corretamente no COPER.
   - Resultado esperado: O usuário identifica quais valores estão faltando ou não foram lançados.

4. **Lançar Valores Faltantes**
   - Localização: Tela de Movimentações
   - Como fazer: Se um valor não foi reconhecido, o usuário deve navegar até a tela de **Movimentações** e procurar pelo valor correspondente. Caso não encontre, deve lançar o valor manualmente.
   - Observações importantes: O lançamento deve ser feito antes de tentar conciliar novamente, pois o sistema não atualiza automaticamente os valores após a importação.
   - Resultado esperado: O valor é lançado no sistema e, ao retornar à tela de conciliação, o usuário pode selecionar o valor recém-lançado para confirmar a conciliação.

5. **Selecionar e Confirmar Movimentações**
   - Localização: Tela de Conciliação, área de seleção de movimentações
   - Como fazer: O usuário pode selecionar várias movimentações que correspondem ao valor do extrato. Após selecionar, deve clicar no botão **Confirmar**.
   - Observações importantes: Isso é especialmente útil para pagamentos de faturas de cartão, onde múltiplas movimentações podem ser necessárias para igualar o valor do extrato.
   - Resultado esperado: As movimentações selecionadas são confirmadas e a conciliação é finalizada.

**Campos e Parâmetros:**

| Campo                     | Tipo   | Obrigatório | Descrição                                           | Exemplo          |
|---------------------------|--------|-------------|----------------------------------------------------|------------------|
| `Importar Extrato`       | Botão  | Sim         | Botão para iniciar a importação do extrato OFX    | -                |
| `Movimentações`          | Lista  | Sim         | Lista de movimentações lançadas no sistema         | R$ 62,50         |
| `Valor do Extrato`       | Número | Sim         | Valor correspondente no extrato importado          | R$ 52,62         |
| `Confirmar`              | Botão  | Sim         | Botão para confirmar a seleção de movimentações    | -                |

**Regras de Negócio:**
- O sistema aceita apenas arquivos no formato OFX para importação.
- Os valores do extrato devem ser lançados no sistema antes da conciliação.
- O usuário deve confirmar manualmente as movimentações que não foram reconhecidas automaticamente.

**Observações Importantes:**
- É importante realizar a importação do extrato antes de lançar novos valores.
- Erros comuns incluem não encontrar valores no sistema, que podem indicar lançamentos ausentes.
- O sistema não atualiza automaticamente os valores após a importação; os lançamentos devem ser feitos manualmente.

**Conceitos-Chave:**
- **Conciliação**: Processo de validação dos valores do extrato bancário com os lançamentos no sistema.
- **OFX**: Formato de arquivo utilizado para a importação de extratos bancários.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso importar um extrato bancário no sistema?
- O que fazer se o sistema não reconhecer os valores do extrato?
- Como lançar valores que não foram importados automaticamente?

---


---


---

## 3. Conciliação de Movimentações Financeiras

**📋 METADADOS:**
- **ID:** sec_3
- **⏱️ Minutagem:** 05:04 → 07:37
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/DMvowd7eCAA?si=qrXiuODXTH9y2zNZ&t=304)
- **📦 Módulo:** Conciliação Financeira
- **🏷️ Categorias:** Conciliação, Movimentação Financeira, Registro, Transferência
- **🔑 Palavras-chave:** conciliação, movimentações, transferência, tarifas, estorno, cheque, boletos, extratos

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como conciliar movimentações financeiras no sistema, permitindo registrar transferências, tarifas e estornos, garantindo que os valores sejam compatíveis para a conclusão da conciliação.

**Contexto:**
Estamos na funcionalidade de conciliação financeira do sistema, onde o usuário pode reconciliar as movimentações bancárias com as faturas correspondentes, registrando transferências e outras operações financeiras.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Conciliação Financeira > Aba de Conciliação
- Tela/interface específica: Tela de Conciliação de Movimentações

**Funcionalidade Detalhada:**
A funcionalidade de conciliação permite que o usuário selecione várias movimentações financeiras até que o valor total corresponda ao valor da fatura. O sistema possibilita registrar transferências, tarifas e estornos simultaneamente, assegurando que os valores sejam compatíveis para a conclusão da conciliação.

### 🔹 Passo a Passo Detalhado:

1. **Selecionar Movimentações**
   - Localização: Aba de Conciliação
   - Como fazer: O usuário deve selecionar as movimentações financeiras que correspondem ao valor total da fatura. Para isso, basta clicar nas caixas de seleção ao lado de cada movimentação.
   - Campos/Opções disponíveis:
     * `Movimentação`: Lista de movimentações disponíveis para seleção.
   - Resultado esperado: As movimentações selecionadas são somadas e o valor total é exibido.

2. **Registrar Transferência**
   - Localização: Aba de Conciliação, campo de transferência
   - Como fazer: O usuário deve selecionar o campo de transferência, indicar a conta para a qual foi realizada a transferência e clicar no botão "Adicionar".
   - Campos/Opções disponíveis:
     * `Conta de Destino`: Campo para selecionar a conta para a qual a transferência foi feita.
   - Resultado esperado: A transferência é registrada e a conciliação é concluída automaticamente.

3. **Adicionar Tarifas**
   - Localização: Aba de Conciliação, seção de tarifas
   - Como fazer: O usuário deve clicar na parte de tarifas, adicionar uma classificação para a tarifa e clicar em "Adicionar".
   - Observações importantes: Caso a classificação desejada não esteja disponível, o usuário pode criar uma nova classificação temporária.
   - Resultado esperado: A tarifa é registrada e a conciliação é atualizada.

4. **Registrar Estorno**
   - Localização: Aba de Conciliação, subárea de estorno
   - Como fazer: O usuário deve selecionar a opção de estorno, indicar a movimentação correspondente e clicar em "Concluir".
   - Observações importantes: O sistema não permitirá a conciliação se os valores não coincidirem.
   - Resultado esperado: O estorno é registrado e a conciliação é atualizada.

5. **Associar Cheque**
   - Localização: Aba de Conciliação, campo de cheque
   - Como fazer: O usuário deve acessar o campo de cheque, selecionar a conta associada ao cheque e clicar em "Adicionar".
   - Resultado esperado: O cheque é associado à movimentação e a conciliação é atualizada.

6. **Finalizar Conciliações**
   - Localização: Aba de Conciliação
   - Como fazer: Após registrar todas as movimentações, o usuário deve verificar se todas as conciliações estão corretas e clicar em "Concluir".
   - Resultado esperado: Todas as conciliações finalizadas são movidas para a aba de finalizadas.

7. **Visualizar Extratos**
   - Localização: Aba de Extratos
   - Como fazer: O usuário pode acessar a aba de extratos para visualizar o histórico de todos os extratos importados para a conta bancária.
   - Resultado esperado: O sistema exibe todos os extratos importados.

8. **Emitir Boletos**
   - Localização: Aba de Boletos
   - Como fazer: Caso a integração bancária esteja contratada, o usuário pode emitir boletos diretamente pelo sistema.
   - Resultado esperado: O sistema mostra todos os boletos emitidos para a conta bancária no período selecionado.

9. **Visualizar Cheques Emitidos**
   - Localização: Aba de Cheques
   - Como fazer: O usuário deve acessar a aba de cheques para visualizar todos os cheques emitidos para a conta bancária conforme o período selecionado.
   - Resultado esperado: O sistema exibe todos os cheques emitidos.

**Campos e Parâmetros:**

| Campo                  | Tipo         | Obrigatório | Descrição                                             | Exemplo               |
|------------------------|--------------|-------------|-----------------------------------------------------|-----------------------|
| `Movimentação`         | Lista        | Sim         | Lista de movimentações disponíveis para seleção     | Transferência 100,00  |
| `Conta de Destino`     | Dropdown     | Sim         | Conta para a qual a transferência foi realizada     | Conta Corrente 1234   |
| `Classificação`        | Texto livre  | Não         | Classificação da tarifa ou estorno                   | Tarifa de Manutenção   |
| `Movimentação de Estorno` | Lista     | Sim         | Movimentação à qual o estorno se refere             | Transferência 50,00   |
| `Cheque`               | Dropdown     | Sim         | Conta associada ao cheque                            | Conta Corrente 5678   |

**Regras de Negócio:**
- Os valores das movimentações devem coincidir para que a conciliação seja concluída.
- O sistema não permitirá a conciliação se os valores não baterem.
- Todas as conciliações finalizadas serão movidas para a aba de finalizadas.

**Observações Importantes:**
- O usuário deve garantir que todas as movimentações estejam corretas antes de finalizar a conciliação.
- Caso uma classificação não esteja disponível, o usuário pode criar uma nova classificação temporária.
- Erros comuns incluem não selecionar todas as movimentações necessárias para a conciliação.

**Conceitos-Chave:**
- **Conciliação**: Processo de verificar se os registros financeiros correspondem aos extratos bancários.
- **Transferência**: Movimento financeiro que envolve a transferência de valores entre contas.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso conciliar movimentações financeiras no sistema?
- O que fazer se não encontrar uma classificação para tarifas?
- Como registrar uma transferência durante a conciliação?

---


---


---

## 4. Configuração de Boletos pelo COPER

**📋 METADADOS:**
- **ID:** sec_4
- **⏱️ Minutagem:** 07:34 → 10:10
- **⏲️ Duração:** 155s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/DMvowd7eCAA?si=qrXiuODXTH9y2zNZ&t=454)
- **📦 Módulo:** Configuração de Boletos
- **🏷️ Categorias:** Configuração, Administração, Financeiro
- **🔑 Palavras-chave:** comissão, boletos, configuração, automação, Anexera, transferências, etiquetas, contas

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de configuração de boletos no sistema COPER, incluindo a habilitação da automação com a Anexera e a gestão de contas. O objetivo é garantir que os usuários possam realizar operações financeiras de forma eficiente e organizada.

**Contexto:**
Estamos na interface de configuração do sistema COPER, onde os usuários podem ajustar as definições necessárias para a emissão e gestão de boletos. Esta seção é crucial para garantir que todas as informações obrigatórias sejam preenchidas corretamente antes de iniciar o uso do sistema.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo de Configuração de Boletos
- Tela/interface específica: Tela de Configuração de Boletos

**Funcionalidade Detalhada:**

A funcionalidade de configuração de boletos permite que os usuários preencham informações obrigatórias para a emissão de boletos. É necessário que essas informações sejam fornecidas pelo gerente de cada conta. Além disso, a automação com a Anexera deve ser habilitada, pois esta empresa parceira é responsável pelo tráfego dos arquivos referentes aos boletos emitidos e sua comunicação com o banco. Caso uma conta não seja mais utilizada, o sistema não permite a exclusão, mas sim a desativação, permitindo que o histórico de movimentações seja consultado posteriormente.

### 🔹 Passo a Passo Detalhado:

1. **Preencher Informações Obrigatórias**
   - Localização: Tela de Configuração de Boletos
   - Como fazer: Identifique os campos marcados com um asterisco (*) que indicam informações obrigatórias. Preencha cada um deles com os dados fornecidos pelo gerente da conta.
   - Campos/Opções disponíveis:
     * `Campo 1`: Nome da Conta (texto)
     * `Campo 2`: Número da Conta (número)
   - Resultado esperado: As informações obrigatórias são salvas e a configuração dos boletos pode prosseguir.

2. **Habilitar Automação com Anexera**
   - Localização: Tela de Configuração de Boletos
   - Como fazer: Localize a opção de habilitação da automação com a Anexera. Clique no botão correspondente para ativar essa funcionalidade.
   - Observações importantes: Certifique-se de que todas as informações obrigatórias estejam preenchidas antes de habilitar a automação.
   - Resultado esperado: A automação com a Anexera é ativada, permitindo o tráfego de arquivos de boletos para o banco.

3. **Desativar Conta**
   - Localização: Tela de Gerenciamento de Contas
   - Como fazer: Se uma conta não for mais utilizada, selecione a conta desejada e clique no botão de desativação.
   - Observações importantes: Não é possível excluir a conta se houver movimentações associadas. A desativação é suficiente para interromper o uso da conta.
   - Resultado esperado: A conta é desativada e não aparecerá mais nas contas ativas, mas seu histórico permanece acessível.

4. **Realizar Transferências**
   - Localização: Tela de Transferências
   - Como fazer: Para realizar transferências entre contas, selecione a conta de origem e a conta de destino. Insira o valor a ser transferido e clique no botão de "Transferir".
   - Observações importantes: Se o plano incluir multiempresas, transferências entre empresas também são permitidas.
   - Resultado esperado: A transferência é processada e um registro é criado no histórico de movimentações.

5. **Cadastro de Etiquetas**
   - Localização: Tela de Cadastro de Etiquetas
   - Como fazer: Clique no botão "Adicionar" para criar uma nova etiqueta. Insira o nome da etiqueta e clique em "Salvar".
   - Resultado esperado: A nova etiqueta é criada e pode ser associada a parcelas a pagar ou a receber.

6. **Configurações de Pagamento**
   - Localização: Tela de Configuração de Pagamentos
   - Como fazer: Habilite ou desabilite a opção que permite o pagamento das parcelas mesmo sem a confirmação do recebimento do material.
   - Observações importantes: Se a opção estiver desabilitada, o pagamento só poderá ser realizado após a confirmação do recebimento do material no local de entrega.
   - Resultado esperado: As configurações de pagamento são salvas conforme a escolha do usuário.

**Campos e Parâmetros:**

| Campo                       | Tipo   | Obrigatório | Descrição                                               | Exemplo                |
|-----------------------------|--------|-------------|--------------------------------------------------------|------------------------|
| Nome da Conta               | Texto  | Sim         | Nome que identifica a conta no sistema.                | "Conta Principal"      |
| Número da Conta             | Número | Sim         | Número da conta bancária associada.                    | "123456789"            |
| Habilitar Automação         | Checkbox | Sim       | Permite ativar a automação com a Anexera.             | [X] Habilitar          |
| Nome da Etiqueta            | Texto  | Sim         | Nome que identifica a etiqueta a ser cadastrada.      | "Urgente"              |
| Permitir Pagamento Sem Confirmação | Checkbox | Sim | Permite o pagamento de parcelas sem confirmação.       | [ ] Permitir           |

**Regras de Negócio:**
- As informações obrigatórias devem ser preenchidas antes de habilitar a automação.
- Não é possível excluir uma conta que possui movimentações associadas; apenas desativá-la.
- O pagamento das parcelas pode ser configurado para exigir ou não a confirmação do recebimento do material.

**Observações Importantes:**
- Sempre verifique se todas as informações obrigatórias estão preenchidas antes de prosseguir com a configuração.
- Evite desativar contas que ainda possuem movimentações ativas, pois isso pode gerar confusão no histórico financeiro.
- Utilize etiquetas para organizar melhor as parcelas a pagar e a receber.

**Conceitos-Chave:**
- **Anexera**: Empresa parceira responsável pelo tráfego de arquivos de boletos emitidos para o banco.
- **Desativação de Conta**: Processo de interromper o uso de uma conta sem excluí-la, mantendo o histórico acessível.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como configurar os boletos no sistema COPER?
- O que fazer se uma conta não for mais utilizada?
- Como habilitar a automação com a Anexera?

---


---


---

## 5. Cadastro de Categorias e Tributos

**📋 METADADOS:**
- **ID:** sec_5
- **⏱️ Minutagem:** 10:07 → 12:44
- **⏲️ Duração:** 156s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/DMvowd7eCAA?si=qrXiuODXTH9y2zNZ&t=607)
- **📦 Módulo:** Cadastro de Tributos
- **🏷️ Categorias:** Configuração, Cadastro, Administração
- **🔑 Palavras-chave:** categorias, tributos, cadastro, parcelas, periodicidade, indexadores

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como cadastrar categorias e tributos no sistema, permitindo a classificação de parcelas a pagar ou a receber. O processo inclui a definição de periodicidade e a associação de guias específicas para cada tributo.

**Contexto:**
Estamos na seção de cadastro do sistema, onde o usuário pode adicionar categorias e tributos que serão utilizados na geração de parcelas a pagar ou a receber. O objetivo é permitir uma melhor organização e classificação das transações financeiras.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Cadastro de Tributos > Submenu Cadastro de Categorias e Tributos
- Tela/interface específica: Tela de Cadastro de Categorias e Tributos

**Funcionalidade Detalhada:**
A funcionalidade de cadastro de categorias e tributos permite que os usuários classifiquem as parcelas geradas no sistema. As categorias podem incluir classificações como "comissão", "pagamento de terceiros", "empréstimos" e "material de consumo". O sistema já possui algumas categorias pré-cadastradas, mas os usuários têm a opção de adicionar novas. Além disso, é possível cadastrar tributos, definindo seu nome, sigla, periodicidade e associando guias específicas.

### 🔹 Passo a Passo Detalhado:

1. **Cadastro de Categorias**
   - Localização: Tela de Cadastro de Categorias e Tributos
   - Como fazer: Para adicionar uma nova categoria, o usuário deve clicar no botão **Adicionar Categoria**.
   - Campos/Opções disponíveis:
     * `Nome da Categoria`: Campo de texto onde o usuário insere o nome da nova categoria.
   - Resultado esperado: A nova categoria é adicionada à lista de categorias disponíveis para classificação de parcelas.

2. **Cadastro de Tributos**
   - Localização: Tela de Cadastro de Categorias e Tributos
   - Como fazer: O usuário deve clicar no botão **Adicionar Tributo**.
   - Campos/Opções disponíveis:
     * `Nome do Tributo`: Campo de texto onde o usuário insere o nome do tributo.
     * `Sigla`: Campo de texto para a sigla do tributo.
     * `Periodicidade`: Dropdown onde o usuário seleciona a periodicidade do tributo (ex: mensal, trimestral, anual).
     * `Utilizado em Notas de Serviços`: Checkbox que deve ser marcado se o tributo será utilizado em notas de serviços.
   - Observações importantes: Campos obrigatórios são indicados com um asterisco (*). O usuário deve preencher todos os campos obrigatórios antes de salvar.
   - Resultado esperado: O tributo é cadastrado e fica disponível para uso nas notas de serviço e lançamentos financeiros.

3. **Cadastro de Modelos de Guias**
   - Localização: Tela de Cadastro de Tributos
   - Como fazer: Após cadastrar o tributo, o usuário deve associar um modelo de guia clicando no botão **Adicionar Modelo de Guia**.
   - Campos/Opções disponíveis:
     * `Modelo de Guia`: Seleção de um dos quatro modelos de guia disponíveis (não é possível adicionar novos modelos).
   - Resultado esperado: O modelo de guia é associado ao tributo cadastrado.

4. **Cadastro de Indexadores**
   - Localização: Tela de Cadastro de Indexadores
   - Como fazer: O usuário deve clicar no botão **Adicionar Indexador**.
   - Campos/Opções disponíveis:
     * `Nome do Indexador`: Campo de texto para o nome do indexador.
     * `Gatilho de Cobrança`: Dropdown com quatro opções de gatilho de cobrança.
     * `Categoria de Lançamento`: Dropdown onde o usuário seleciona a categoria de lançamento do valor do indexador.
   - Resultado esperado: O indexador é cadastrado e pode ser utilizado nas parcelas de venda.

5. **Adicionar Índices ao Indexador**
   - Localização: Tela de Cadastro de Indexadores
   - Como fazer: Após cadastrar o indexador, o usuário deve clicar no botão **Adicionar Valor**.
   - Campos/Opções disponíveis:
     * `Mês`: Campo de texto onde o usuário insere o mês referente ao índice.
     * `Valor`: Campo de texto onde o usuário insere o valor do índice.
   - Resultado esperado: O índice é adicionado ao indexador cadastrado.

**Campos e Parâmetros:**

| Campo                      | Tipo         | Obrigatório | Descrição                                                                 | Exemplo                |
|----------------------------|--------------|-------------|---------------------------------------------------------------------------|------------------------|
| Nome da Categoria           | Texto        | Sim         | Nome da nova categoria a ser cadastrada.                                 | "Comissão"             |
| Nome do Tributo            | Texto        | Sim         | Nome do tributo a ser cadastrado.                                        | "ICMS"                 |
| Sigla                      | Texto        | Sim         | Sigla que representa o tributo.                                          | "ICMS"                 |
| Periodicidade              | Dropdown     | Sim         | Frequência com que o tributo será aplicado.                             | "Mensal"               |
| Utilizado em Notas de Serviços | Checkbox | Não         | Indica se o tributo será utilizado em notas de serviços.                | [ ] (marcado ou não)   |
| Nome do Indexador          | Texto        | Sim         | Nome do indexador a ser cadastrado.                                      | "IGPM"                 |
| Gatilho de Cobrança        | Dropdown     | Sim         | Opção que define o gatilho de cobrança do indexador.                    | "Anual"                |
| Categoria de Lançamento    | Dropdown     | Sim         | Categoria onde o valor do indexador deve ser registrado.                | "Venda"                |
| Mês                        | Texto        | Sim         | Mês referente ao índice a ser cadastrado.                                | "Janeiro"              |
| Valor                      | Texto        | Sim         | Valor do índice a ser cadastrado.                                        | "5.00"                 |

**Regras de Negócio:**
- Todos os campos obrigatórios devem ser preenchidos antes de salvar o cadastro.
- O sistema possui apenas quatro modelos de guias que podem ser associados aos tributos; não é possível adicionar novos modelos.
- A periodicidade deve ser selecionada corretamente para que o sistema gere a recorrência do tributo.

**Observações Importantes:**
- É importante verificar se todos os campos obrigatórios estão preenchidos para evitar erros ao salvar.
- O usuário deve estar ciente de que a opção "Utilizado em Notas de Serviços" permite que o tributo seja automaticamente lançado ao gerar uma nota de serviço.
- Erros comuns incluem não preencher campos obrigatórios e não selecionar a periodicidade correta.

**Conceitos-Chave:**
- **Periodicidade**: Refere-se à frequência com que um tributo ou indexador será aplicado, podendo ser mensal, trimestral, anual, etc.
- **Indexador**: Um índice de correção que pode ser aplicado a parcelas de venda, ajustando seu valor ao longo do tempo.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso cadastrar uma nova categoria no sistema?
- Quais informações são necessárias para cadastrar um tributo?
- O que devo fazer para adicionar um indexador e seus valores?

---


---


---

## 6. Gestão de Créditos e Débitos

**📋 METADADOS:**
- **ID:** sec_6
- **⏱️ Minutagem:** 12:40 → 15:16
- **⏲️ Duração:** 155s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/DMvowd7eCAA?si=qrXiuODXTH9y2zNZ&t=760)
- **📦 Módulo:** Contas a Pagar e Receber
- **🏷️ Categorias:** Operacional, Financeiro, Gestão de Créditos, Gestão de Débitos
- **🔑 Palavras-chave:** créditos, débitos, contas a pagar, contas a receber, amortização, indexador

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de gestão de créditos e débitos dentro do sistema, explicando como criar, associar e acompanhar esses valores, além de como realizar a amortização de parcelas.

**Contexto:**
Estamos na funcionalidade de gestão financeira do sistema, onde os usuários podem registrar e acompanhar créditos e débitos associados a parceiros e clientes. O objetivo é garantir que as parcelas sejam corrigidas automaticamente e que os registros financeiros sejam mantidos de forma organizada.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Financeiro > Gestão de Créditos e Débitos
- Tela/interface específica: Tela de Gestão de Créditos e Débitos

**Funcionalidade Detalhada:**
A funcionalidade de gestão de créditos e débitos permite que os usuários registrem e acompanhem valores que devem ser pagos ou recebidos. Os créditos são utilizados para amortizar parcelas no contas a pagar, enquanto os débitos são utilizados para amortizar parcelas no contas a receber. Os créditos podem ser gerados automaticamente ou manualmente, enquanto os débitos devem ser criados manualmente.

### 🔹 Passo a Passo Detalhado:

1. **Registro de Créditos**
   - Localização: Tela de Gestão de Créditos e Débitos
   - Como fazer: Para registrar um crédito, o usuário deve clicar no botão **"Adicionar Crédito"**.
   - Campos/Opções disponíveis:
     * `Parceiro`: Selecionar o parceiro associado ao crédito (dropdown com lista de parceiros).
     * `Tipo de Crédito`: Selecionar o tipo de crédito (opções: **Crédito Avulso**, **Pagamento Duplicado**, **Permuta**).
   - Resultado esperado: O crédito é salvo e aparece na lista de créditos disponíveis.

2. **Visualização do Histórico de Créditos**
   - Localização: Tela de Gestão de Créditos e Débitos
   - Como fazer: Após registrar um crédito, o usuário pode visualizar o histórico clicando na aba **"Histórico de Créditos"**.
   - Observações importantes: O histórico mostra o valor inicial do crédito, quanto já foi utilizado e o saldo restante.
   - Resultado esperado: O usuário consegue acompanhar a utilização dos créditos.

3. **Registro de Débitos**
   - Localização: Tela de Gestão de Créditos e Débitos
   - Como fazer: Para registrar um débito, o usuário deve clicar no botão **"Adicionar Débito"**.
   - Campos/Opções disponíveis:
     * `Valor`: Inserir o valor do débito.
     * `Data do Recebimento Duplicado`: Inserir a data em que o pagamento duplicado foi recebido.
     * `Conta Bancária`: Selecionar a conta bancária onde o valor foi creditado (dropdown com lista de contas).
   - Resultado esperado: O débito é salvo e aparece na lista de débitos disponíveis.

**Campos e Parâmetros:**

| Campo                       | Tipo       | Obrigatório | Descrição                                               | Exemplo           |
|-----------------------------|------------|-------------|--------------------------------------------------------|-------------------|
| `Parceiro`                  | Dropdown   | Sim         | Seleciona o parceiro associado ao crédito.             | "Fornecedor A"    |
| `Tipo de Crédito`           | Dropdown   | Sim         | Define o tipo de crédito a ser registrado.             | "Pagamento Duplicado" |
| `Valor`                     | Numérico   | Sim         | Valor do débito a ser registrado.                      | 1000.00           |
| `Data do Recebimento Duplicado` | Data   | Sim         | Data em que o pagamento duplicado foi recebido.        | "2023-10-01"      |
| `Conta Bancária`            | Dropdown   | Sim         | Conta onde o valor do débito foi creditado.           | "Conta Corrente"  |

**Regras de Negócio:**
- Os créditos devem ser utilizados no contas a pagar.
- Os débitos devem ser utilizados no contas a receber.
- Créditos podem ser gerados automaticamente a partir da antecipação de ordens de compra ou de serviço.
- Débitos só podem ser criados manualmente.

**Observações Importantes:**
- Sempre que houver uma atualização do indexador referente a um determinado mês, o processo de correção das parcelas deve ser realizado.
- É importante acompanhar o histórico de créditos para evitar confusões sobre valores utilizados e saldos.

**Conceitos-Chave:**
- **Crédito**: Valor que pode ser utilizado para amortizar parcelas no contas a pagar.
- **Débito**: Valor que deve ser registrado e amortizado no contas a receber, geralmente relacionado a pagamentos duplicados.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como registro um crédito no sistema?
- Quais tipos de crédito posso selecionar ao registrar um?
- Como visualizo o histórico de créditos e débitos registrados?

---


---


---

## 7. Registro de Pagamentos e Emissão de Cheques

**📋 METADADOS:**
- **ID:** sec_7
- **⏱️ Minutagem:** 15:13 → 17:46
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/DMvowd7eCAA?si=qrXiuODXTH9y2zNZ&t=913)
- **📦 Módulo:** Financeiro
- **🏷️ Categorias:** Pagamentos, Cheques, Contas a Receber
- **🔑 Palavras-chave:** pagamento, parcela, débito avulso, cheque, compensação, boleto

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como registrar pagamentos de parcelas, incluindo a criação de débitos avulsos e a emissão de cheques. O objetivo é garantir que os usuários compreendam como registrar corretamente os pagamentos e gerenciar cheques no sistema.

**Contexto:**
Estamos na seção do módulo financeiro do sistema, onde o usuário pode registrar pagamentos recebidos e gerenciar cheques. Esta funcionalidade é essencial para manter o controle financeiro e garantir que os pagamentos sejam corretamente associados às parcelas devidas.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Financeiro > Submenu Pagamentos
- Tela/interface específica: Tela de Registro de Pagamentos

**Funcionalidade Detalhada:**

A funcionalidade de registro de pagamentos permite que o usuário associe um valor pago a uma parcela específica. Caso o pagamento seja referente a um débito avulso, o sistema gera automaticamente uma conta a receber, permitindo que o valor seja amortizado nas próximas parcelas do cliente. Além disso, o sistema oferece suporte para a gestão de cheques, incluindo a emissão e compensação.

### 🔹 Passo a Passo Detalhado:

1. **Registrar Pagamento de Parcela**
   - Localização: Tela de Registro de Pagamentos
   - Como fazer: O usuário deve inserir o valor recebido e associá-lo à parcela correspondente.
   - Campos/Opções disponíveis:
     * `Valor`: Campo numérico onde o usuário insere o valor pago.
     * `Parcela`: Dropdown onde o usuário seleciona a parcela correspondente ao pagamento.
   - Resultado esperado: O pagamento é registrado e associado à parcela selecionada.

2. **Criar Débito Avulso**
   - Localização: Tela de Registro de Pagamentos
   - Como fazer: Se o pagamento for um débito avulso, o usuário deve selecionar a opção de "Débito Avulso" e inserir o valor recebido.
   - Observações importantes: O sistema gera automaticamente uma conta a receber e permite que o usuário indique que o valor será amortizado nas próximas parcelas.
   - Resultado esperado: Um débito avulso é criado e o valor é registrado para amortização futura.

3. **Emitir Cheque**
   - Localização: Tela de Registro de Pagamentos
   - Como fazer: O usuário deve selecionar a opção de "Emitir Cheque", associar o cheque às parcelas que devem ser pagas e inserir os detalhes do cheque.
   - Campos/Opções disponíveis:
     * `Número Inicial`: Campo numérico para inserir o número inicial do talão de cheques.
     * `Número Final`: Campo numérico para inserir o número final do talão de cheques.
   - Resultado esperado: O cheque é emitido e associado às parcelas selecionadas.

4. **Compensar Cheque**
   - Localização: Tela de Registro de Pagamentos
   - Como fazer: Após a emissão do cheque, o usuário deve selecionar a opção de "Compensar Cheque" quando o cheque for efetivamente compensado.
   - Observações importantes: O sistema reconhece que o pagamento da parcela foi realizado e atualiza o extrato da conta bancária associada ao cheque.
   - Resultado esperado: O pagamento da parcela é registrado como compensado e os valores aparecem no extrato da conta bancária.

5. **Retirar Compensação do Cheque**
   - Localização: Tela de Registro de Pagamentos
   - Como fazer: O usuário deve selecionar a opção de "Retirar Compensação" para um cheque específico.
   - Resultado esperado: A compensação do cheque é removida, e o status do pagamento é atualizado no sistema.

**Campos e Parâmetros:**

| Campo               | Tipo       | Obrigatório | Descrição                                           | Exemplo         |
|---------------------|------------|-------------|-----------------------------------------------------|------------------|
| `Valor`             | Numérico   | Sim         | Valor pago pelo cliente.                            | 150,00           |
| `Parcela`           | Dropdown   | Sim         | Seleção da parcela à qual o pagamento se refere.   | Parcela X        |
| `Número Inicial`    | Numérico   | Sim         | Número inicial do talão de cheques.                | 001              |
| `Número Final`      | Numérico   | Sim         | Número final do talão de cheques.                  | 100              |

**Regras de Negócio:**
- O sistema deve gerar uma conta a receber automaticamente ao registrar um débito avulso.
- O pagamento de parcelas só é considerado efetivo após a compensação do cheque.
- O usuário deve associar corretamente os cheques às parcelas para garantir a correta contabilização.

**Observações Importantes:**
- É importante verificar se o cheque foi compensado antes de considerar o pagamento como efetivo.
- Evitar registrar pagamentos duplicados para a mesma parcela.
- O sistema pode permitir a edição de cheques emitidos, mas a compensação deve ser feita corretamente.

**Conceitos-Chave:**
- **Débito Avulso**: Um pagamento que não está associado a uma parcela específica, mas que deve ser registrado para controle financeiro.
- **Compensação de Cheque**: O processo pelo qual um cheque é processado pelo banco, confirmando que o pagamento foi realizado.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como registrar um pagamento de uma parcela específica no sistema?
- O que é um débito avulso e como ele é registrado?
- Como emitir e compensar um cheque no sistema?

---


---


---

## 8. Emissão e Gerenciamento de Boletos e Tributos

**📋 METADADOS:**
- **ID:** sec_8
- **⏱️ Minutagem:** 17:44 → 20:18
- **⏲️ Duração:** 154s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/DMvowd7eCAA?si=qrXiuODXTH9y2zNZ&t=1064)
- **📦 Módulo:** Financeiro
- **🏷️ Categorias:** Emissão de Boletos, Gestão de Tributos, Integração Bancária
- **🔑 Palavras-chave:** boletos, remessa, retorno, tributos, contas a pagar, integração, Nexera, COPER

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de emissão de boletos e o gerenciamento de tributos dentro do sistema, incluindo a integração bancária que automatiza a remessa e o retorno dos pagamentos, facilitando a gestão financeira.

**Contexto:**
Estamos na interface do módulo financeiro do sistema, onde os usuários podem emitir boletos para seus clientes e registrar tributos relacionados a notas fiscais. O objetivo é simplificar o processo de cobrança e garantir que os pagamentos sejam registrados automaticamente.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Financeiro > Emissão de Boletos e Gestão de Tributos
- Tela/interface específica: Tela de Emissão de Boletos e Registro de Tributos

**Funcionalidade Detalhada:**

A funcionalidade permite que os usuários emitam boletos para seus clientes e gerenciem tributos relacionados a notas fiscais. Quando a integração bancária está ativa, o sistema gera automaticamente a remessa dos boletos e importa os retornos, registrando pagamentos de forma automática. Os usuários podem também lançar tributos, associando-os a centros de custo e gerando contas a pagar.

### 🔹 Passo a Passo Detalhado:

1. **Emissão de Boletos**
   - Localização: Tela de Emissão de Boletos
   - Como fazer: O usuário deve preencher os dados do cliente e selecionar as parcelas a serem cobradas. Após isso, clicar no botão **Emitir Boleto**.
   - Campos/Opções disponíveis:
     * `Cliente`: Selecionar o cliente da lista de clientes cadastrados.
     * `Parcelas`: Selecionar as parcelas que serão incluídas no boleto.
   - Resultado esperado: O sistema gera os boletos e cria uma remessa automaticamente.

2. **Integração com a Nexera**
   - Localização: Após a emissão dos boletos
   - Como fazer: O sistema automaticamente envia a remessa para a Nexera, que é a empresa parceira responsável pelo envio ao banco.
   - Observações importantes: Certifique-se de que a integração com a Nexera está configurada corretamente no sistema.
   - Resultado esperado: A remessa é enviada para o banco através da Nexera.

3. **Importação de Retornos**
   - Localização: Tela de Importação de Retornos
   - Como fazer: O sistema aguarda o arquivo de retorno do banco, que é enviado pela Nexera. O COPER, que é o sistema de gestão, importa automaticamente esse arquivo.
   - Resultado esperado: Se o arquivo de retorno indicar que o boleto foi pago, o sistema registra automaticamente a parcela como recebida.

4. **Registro de Tributos**
   - Localização: Tela de Registro de Tributos
   - Como fazer: Clique no botão **Mais Tributo** para adicionar um novo tributo. Se o tributo não estiver cadastrado, clique em **Mais Adicionar** para cadastrá-lo instantaneamente.
   - Campos/Opções disponíveis:
     * `Centro de Custo`: Selecionar o centro de custo relacionado ao tributo.
     * `Valor do Imposto`: Inserir o valor do tributo.
     * `Data de Vencimento`: Definir a data de vencimento do tributo.
     * `Acréscimos`: Preencher se houver.
     * `Multas`: Preencher se houver.
     * `Juros`: Preencher se houver.
     * `Per de Apuração`: Inserir o período de apuração.
     * `Descrição`: Adicionar uma descrição do tributo.
     * `Classificação Financeira`: Associar uma classificação financeira para controle no fluxo de caixa.
   - Resultado esperado: O tributo é registrado e um contas a pagar é gerado automaticamente.

5. **Anexar Guia de Tributo**
   - Localização: Após o registro do tributo
   - Como fazer: Clique no botão **Anexar Guia** para adicionar a guia do tributo.
   - Resultado esperado: A guia é anexada ao registro do tributo e o contas a pagar é atualizado.

**Campos e Parâmetros:**

| Campo                     | Tipo         | Obrigatório | Descrição                                               | Exemplo               |
|---------------------------|--------------|-------------|---------------------------------------------------------|-----------------------|
| `Cliente`                 | Dropdown     | Sim         | Seleciona o cliente para emissão do boleto.            | João da Silva         |
| `Parcelas`                | Checkbox     | Sim         | Seleciona as parcelas a serem cobradas.                | Parcela 1, Parcela 2  |
| `Centro de Custo`         | Dropdown     | Sim         | Seleciona o centro de custo relacionado ao tributo.    | Vendas, Serviços      |
| `Valor do Imposto`        | Numérico     | Sim         | Valor a ser pago referente ao tributo.                 | 150,00                |
| `Data de Vencimento`      | Data         | Sim         | Data em que o tributo deve ser pago.                   | 30/11/2023            |
| `Acréscimos`              | Numérico     | Não         | Valor adicional a ser incluído.                         | 10,00                 |
| `Multas`                  | Numérico     | Não         | Valor de multa a ser aplicado.                          | 5,00                  |
| `Juros`                   | Numérico     | Não         | Valor de juros a ser aplicado.                          | 2,00                  |
| `Per de Apuração`         | Texto        | Não         | Período de apuração do tributo.                         | Novembro/2023         |
| `Descrição`               | Texto        | Não         | Descrição do tributo.                                  | ICMS sobre vendas     |
| `Classificação Financeira` | Dropdown     | Não         | Classificação para controle financeiro.                 | Tributos a Pagar     |

**Regras de Negócio:**
- A remessa dos boletos é gerada automaticamente após a emissão.
- O sistema deve estar integrado com a Nexera para o envio e recebimento de arquivos.
- O retorno do banco deve ser importado automaticamente pelo COPER.
- Se um boleto é marcado como pago no retorno, a parcela correspondente é automaticamente registrada como recebida.
- Os tributos devem ser associados a um centro de custo e geram contas a pagar automaticamente.

**Observações Importantes:**
- Utilize os atalhos disponíveis para cadastros rápidos.
- Verifique se todos os tributos estão cadastrados antes de registrar um novo.
- Evite erros comuns como não associar tributos a centros de custo.

**Conceitos-Chave:**
- **Remessa**: Arquivo gerado pelo sistema que contém informações sobre os boletos a serem enviados ao banco.
- **Retorno**: Arquivo enviado pelo banco que informa sobre o status dos boletos (pagos ou não).

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como emitir boletos para meus clientes?
- O que acontece após a emissão dos boletos?
- Como registrar e gerenciar tributos no sistema?

---


---


---

## 9. Funcionalidade de Contas a Pagar

**📋 METADADOS:**
- **ID:** sec_9
- **⏱️ Minutagem:** 20:21 → 22:55
- **⏲️ Duração:** 154s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/DMvowd7eCAA?si=qrXiuODXTH9y2zNZ&t=1221)
- **📦 Módulo:** Contas a Pagar
- **🏷️ Categorias:** Operacional, Relatório, Configuração
- **🔑 Palavras-chave:** contas a pagar, etiquetas, filtros, pagamento, parcelas

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha a funcionalidade de gerenciamento de contas a pagar, incluindo a visualização de parcelas, uso de etiquetas para identificação, aplicação de filtros e a possibilidade de realizar pagamentos, dependendo da configuração de recebimento de produtos.

**Contexto:**
Estamos na página inicial do módulo de **Contas a Pagar**, onde o usuário pode visualizar e gerenciar as contas que precisam ser pagas. O objetivo desta seção é explicar como utilizar as funcionalidades disponíveis para facilitar o controle financeiro.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Contas a Pagar
- Tela/interface específica: Página Inicial do Contas a Pagar

**Funcionalidade Detalhada:**

A funcionalidade de **Contas a Pagar** permite ao usuário visualizar as contas que precisam ser pagas, agrupá-las, aplicar filtros para facilitar a busca e realizar pagamentos. As contas são apresentadas com informações relevantes, como status de pagamento e etiquetas que ajudam na identificação de cada parcela.

### 🔹 Passo a Passo Detalhado:

1. **Visualização das Contas**
   - Localização: Página Inicial do módulo **Contas a Pagar**
   - Como fazer: Ao acessar a página, o usuário verá uma lista de contas a pagar. As contas que estão em vermelho indicam que foram agrupadas para pagamento.
   - Campos/Opções disponíveis:
     * **Coluna de Etiquetas**: Exibe as etiquetas associadas a cada parcela, como "empréstimo".
   - Resultado esperado: O usuário consegue identificar rapidamente a que se refere cada parcela sem precisar clicar em cada uma.

2. **Aplicação de Filtros**
   - Localização: Área de filtros na página inicial do **Contas a Pagar**
   - Como fazer: O usuário pode aplicar filtros por:
     * **Obra**: Selecionar uma obra específica.
     * **Empresa**: Filtrar por empresa.
     * **Tipo de Contas**: Escolher entre contas pagas, não pagas, vencidas ou recorrentes.
     * **Periodicidade**: Definir a periodicidade desejada.
     * **Etiquetas**: Filtrar por etiquetas específicas.
     * **Conta Bancária**: Selecionar a conta bancária relacionada.
   - Resultado esperado: O sistema apresenta apenas as contas que atendem aos critérios de filtro selecionados.

3. **Visualização de Totalizadores**
   - Localização: Parte inferior da página inicial do **Contas a Pagar**
   - Como fazer: Após aplicar filtros, o sistema automaticamente atualiza e exibe os totalizadores.
   - Campos/Opções disponíveis:
     * **Valor Total do Contas a Pagar**: Total de todas as contas a pagar.
     * **Valor Pago**: Total das contas já pagas.
     * **Valor Não Pago**: Total das contas pendentes.
     * **Valor de Desconto**: Total de descontos aplicados.
     * **Valor Total de Juros e Multas**: Total de juros e multas acumulados.
   - Resultado esperado: O usuário visualiza um resumo financeiro claro e conciso.

4. **Exportação de Relatório**
   - Localização: Botão de exportação na página inicial do **Contas a Pagar**
   - Como fazer: O usuário pode clicar no botão de exportação para gerar um relatório em PDF com as informações filtradas.
   - Resultado esperado: Um relatório em PDF é gerado contendo todas as informações visíveis na tela, de acordo com os filtros aplicados.

5. **Acesso a uma Parcela**
   - Localização: Clique em uma parcela específica na lista de contas a pagar.
   - Como fazer: O usuário clica na parcela desejada para visualizar detalhes.
   - Observações importantes: Se a configuração de pagamento estiver habilitada, o botão de pagamento aparecerá. Caso contrário, o pagamento não poderá ser realizado.
   - Resultado esperado: O usuário visualiza os detalhes da parcela e, dependendo da configuração, pode ou não realizar o pagamento.

6. **Realização do Pagamento**
   - Localização: Tela de detalhes da parcela
   - Como fazer: Se a configuração permitir, o usuário verá o botão **Pagar**. Ao clicar, o pagamento será processado.
   - Resultado esperado: O pagamento da parcela é realizado com sucesso.

**Campos e Parâmetros:**

| Campo                      | Tipo   | Obrigatório | Descrição                                              | Exemplo               |
|----------------------------|--------|-------------|-------------------------------------------------------|-----------------------|
| **Etiqueta**               | Texto  | Não         | Identificação da parcela, como "empréstimo".         | "empréstimo"          |
| **Valor Total do Contas a Pagar** | Moeda | Não         | Total de todas as contas a pagar.                     | R$ 10.000,00          |
| **Valor Pago**             | Moeda  | Não         | Total das contas que já foram pagas.                  | R$ 5.000,00           |
| **Valor Não Pago**         | Moeda  | Não         | Total das contas que ainda estão pendentes.           | R$ 5.000,00           |
| **Valor de Desconto**      | Moeda  | Não         | Total de descontos aplicados nas contas.              | R$ 500,00             |
| **Valor Total de Juros e Multas** | Moeda | Não         | Total de juros e multas acumulados.                   | R$ 200,00             |

**Regras de Negócio:**
- As contas que estão em vermelho são agrupadas para pagamento.
- As etiquetas servem para identificar cada parcela, facilitando a visualização.
- O pagamento de parcelas só pode ser realizado se os produtos relacionados já tiverem chegado ao local de entrega, conforme configuração.
- O botão de pagamento só aparece se a configuração permitir.

**Observações Importantes:**
- É importante verificar se a configuração de recebimento de produtos está habilitada para evitar problemas ao tentar realizar pagamentos.
- Erros comuns incluem não visualizar o botão de pagamento devido à falta de recebimento dos produtos.

**Conceitos-Chave:**
- **Etiquetas**: Identificadores que ajudam a categorizar e localizar parcelas de forma mais eficiente.
- **Totalizadores**: Resumo financeiro que apresenta a situação das contas a pagar, facilitando a gestão financeira.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso visualizar as contas a pagar no sistema?
- Quais filtros posso aplicar para encontrar uma conta específica?
- O que fazer se não consigo realizar o pagamento de uma parcela?

---


---


---

## 10. Parcelamento de Contas

**📋 METADADOS:**
- **ID:** sec_10
- **⏱️ Minutagem:** 22:52 → 25:26
- **⏲️ Duração:** 154s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/DMvowd7eCAA?si=qrXiuODXTH9y2zNZ&t=1372)
- **📦 Módulo:** Financeiro
- **🏷️ Categorias:** Operacional, Gestão de Contas, Pagamentos
- **🔑 Palavras-chave:** parcelar, contas, vencimento, pagamento, comprovante, histórico

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como parcelar contas no sistema, incluindo a alteração de parcelas, datas de vencimento e formas de pagamento. O objetivo é facilitar a gestão de pagamentos e garantir que os usuários possam ajustar informações conforme necessário.

**Contexto:**
Estamos na interface do módulo financeiro do sistema, onde o usuário pode gerenciar contas a pagar. Esta seção foca na funcionalidade de parcelamento de contas, permitindo que o usuário ajuste detalhes das parcelas e registre pagamentos.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Financeiro > Gestão de Contas
- Tela/interface específica: Tela de Detalhes da Conta

**Funcionalidade Detalhada:**
A funcionalidade de parcelamento de contas permite que o usuário divida o valor total de uma conta em várias parcelas. O usuário pode definir a quantidade de parcelas, o valor de cada uma, a data de vencimento e a forma de pagamento. Além disso, é possível alterar a data de vencimento de uma parcela já criada e anexar comprovantes de pagamento.

### 🔹 Passo a Passo Detalhado:

1. **Definir Parcelas**
   - Localização: Tela de Detalhes da Conta, seção de Parcelamento
   - Como fazer: O usuário deve inserir a quantidade de parcelas desejadas no campo `Quantidade de Parcelas`.
   - Campos/Opções disponíveis:
     * `Quantidade de Parcelas`: Número inteiro que representa quantas parcelas a conta será dividida.
     * `Valor de Cada Parcela`: Campo que permite a edição do valor de cada parcela.
   - Resultado esperado: O sistema calcula e exibe o valor total das parcelas e atualiza a interface.

2. **Alterar Data de Vencimento**
   - Localização: Tela de Detalhes da Conta, seção de Parcelamento
   - Como fazer: O usuário deve clicar no campo `Data de Vencimento` da parcela que deseja alterar e inserir a nova data.
   - Observações importantes: O sistema exibe a data de vencimento original e a nova data após a alteração.
   - Resultado esperado: A data de vencimento da parcela é atualizada e salva no sistema.

3. **Alterar Forma de Pagamento**
   - Localização: Tela de Detalhes da Conta, seção de Pagamento
   - Como fazer: O usuário deve selecionar a nova forma de pagamento no dropdown `Forma de Pagamento`.
   - Observações importantes: A nomenclatura do comprovante de pagamento muda conforme a forma de pagamento selecionada (ex: de "boleto" para "recibo").
   - Resultado esperado: O sistema atualiza a nomenclatura do comprovante de pagamento de acordo com a forma selecionada.

4. **Anexar Comprovante de Pagamento**
   - Localização: Tela de Detalhes da Conta, seção de Anexos
   - Como fazer: O usuário deve clicar no botão `Anexar Comprovante` e selecionar o arquivo desejado.
   - Resultado esperado: O comprovante é anexado à conta e fica disponível para consulta.

5. **Visualizar Histórico da Conta**
   - Localização: Tela de Detalhes da Conta, seção de Histórico
   - Como fazer: O usuário pode visualizar todas as ações realizadas na conta, incluindo data, horário e usuário responsável.
   - Resultado esperado: O histórico é exibido com todas as informações relevantes.

6. **Realizar Pagamento**
   - Localização: Tela de Detalhes da Conta, botão `Pagar`
   - Como fazer: O usuário deve clicar no botão `Pagar`, associar a conta bancária e inserir o valor pago.
   - Resultado esperado: O pagamento é efetivado e registrado no sistema.

7. **Excluir Pagamento**
   - Localização: Tela de Detalhes da Conta, seção de Pagamentos
   - Como fazer: O usuário deve localizar o pagamento que deseja excluir e clicar no botão `Excluir`.
   - Observações importantes: O usuário pode refazer o pagamento após a exclusão, corrigindo informações como data ou valores de juros/multa/desconto.
   - Resultado esperado: O pagamento é removido do sistema, permitindo uma nova tentativa.

8. **Agrupar Contas**
   - Localização: Tela de Detalhes da Conta, seção de Agrupamento
   - Como fazer: O usuário pode selecionar várias contas e clicar no botão `Agrupar`.
   - Resultado esperado: As contas selecionadas são agrupadas, permitindo um único pagamento.

9. **Adicionar Observações**
   - Localização: Tela de Detalhes da Conta, campo `Observações`
   - Como fazer: O usuário deve clicar no campo `Observações` e inserir o texto desejado.
   - Resultado esperado: As observações são salvas e ficam disponíveis para consulta futura.

**Campos e Parâmetros:**

| Campo                     | Tipo        | Obrigatório | Descrição                                           | Exemplo            |
|---------------------------|-------------|-------------|----------------------------------------------------|--------------------|
| `Quantidade de Parcelas`  | Numérico    | Sim         | Número de parcelas em que a conta será dividida    | 3                  |
| `Valor de Cada Parcela`   | Monetário   | Sim         | Valor individual de cada parcela                     | R$ 43,33           |
| `Data de Vencimento`      | Data        | Sim         | Data em que a parcela deve ser paga                 | 30/11/2023         |
| `Forma de Pagamento`      | Dropdown     | Sim         | Método de pagamento utilizado                        | Boleto, Pix, Em mãos|
| `Comprovante de Pagamento` | Anexo       | Não         | Arquivo que comprova o pagamento realizado          | comprovante.pdf     |
| `Observações`             | Texto       | Não         | Notas adicionais sobre a conta                       | Pagamento em atraso |

**Regras de Negócio:**
- O usuário pode parcelar uma conta em até 12 vezes.
- A data de vencimento não pode ser anterior à data atual.
- O sistema deve gerar recibos automaticamente para pagamentos realizados via depósito em conta, em mãos ou Pix.
- O histórico deve registrar todas as ações realizadas, incluindo alterações e pagamentos.

**Observações Importantes:**
- É recomendável revisar as informações antes de efetuar o pagamento para evitar erros.
- O usuário deve garantir que a forma de pagamento selecionada corresponda ao método utilizado.
- Caso ocorra um erro no pagamento, o usuário pode excluir e refazer o pagamento sem complicações.

**Conceitos-Chave:**
- **Parcelamento**: Divisão do valor total de uma conta em várias parcelas a serem pagas em datas específicas.
- **Forma de Pagamento**: Método utilizado para efetuar o pagamento, que pode influenciar na nomenclatura do comprovante.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso parcelar uma conta no sistema?
- É possível alterar a data de vencimento de uma parcela já criada?
- O que devo fazer se cometi um erro ao registrar um pagamento?

---


---


---

## 11. Agrupamento de Contas a Pagar

**📋 METADADOS:**
- **ID:** sec_11
- **⏱️ Minutagem:** 25:22 → 27:57
- **⏲️ Duração:** 155s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/DMvowd7eCAA?si=qrXiuODXTH9y2zNZ&t=1522)
- **📦 Módulo:** Financeiro
- **🏷️ Categorias:** Contas a Pagar, Agrupamento, Gestão Financeira
- **🔑 Palavras-chave:** agrupamento, parcelas, contas a pagar, parceiro, desagrupar, editar

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como agrupar contas a pagar no sistema, permitindo que o usuário organize parcelas relacionadas a um parceiro ou outro critério, facilitando a gestão financeira e o fluxo de caixa.

**Contexto:**
Estamos na interface do módulo financeiro do sistema, onde o usuário pode gerenciar contas a pagar. O objetivo desta seção é detalhar o processo de agrupamento de contas, que permite consolidar várias parcelas em uma única conta a pagar, simplificando o controle financeiro.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Financeiro > Contas a Pagar
- Tela/interface específica: Tela de Listagem de Contas a Pagar

**Funcionalidade Detalhada:**
A funcionalidade de agrupamento de contas a pagar permite que o usuário selecione várias parcelas e as consolide em uma única conta a pagar. Isso é útil para gerenciar pagamentos relacionados a um mesmo parceiro, comissão, folha de pagamento ou tributo. O sistema gera uma nova conta a pagar com o valor total das parcelas selecionadas, enquanto as parcelas agrupadas são destacadas em vermelho.

### 🔹 Passo a Passo Detalhado:

1. **Agrupar Contas a Pagar**
   - Localização: Tela de Listagem de Contas a Pagar, botão **Agrupar**
   - Como fazer: Clique no botão **Agrupar** para iniciar o processo de agrupamento de contas.
   - Campos/Opções disponíveis:
     * `Tipo de Agrupamento`: Selecione o tipo de agrupamento desejado (ex: parceiro, comissão, folha de pagamento, tributo).
   - Resultado esperado: O sistema exibirá opções para selecionar o parceiro e as parcelas a serem agrupadas.

2. **Selecionar Tipo de Agrupamento**
   - Localização: Menu suspenso que aparece após clicar em **Agrupar**.
   - Como fazer: Escolha a opção **Parceiro** para agrupar as parcelas relacionadas a um parceiro específico.
   - Resultado esperado: O sistema permite que você selecione o parceiro desejado para o agrupamento.

3. **Selecionar Parcelas para Agrupamento**
   - Localização: Lista de parcelas disponíveis na tela.
   - Como fazer: Marque as parcelas que deseja agrupar. Você pode selecionar várias parcelas ao mesmo tempo.
   - Resultado esperado: As parcelas selecionadas são preparadas para serem agrupadas em uma nova conta a pagar.

4. **Adicionar Nova Data de Vencimento**
   - Localização: Campo de data que aparece após selecionar as parcelas.
   - Como fazer: Insira uma nova data de vencimento para a conta a pagar que será gerada.
   - Resultado esperado: O sistema cria uma nova conta a pagar com o valor total das parcelas selecionadas e a nova data de vencimento.

5. **Visualizar Contas Agrupadas**
   - Localização: Tela de Listagem de Contas a Pagar.
   - Como fazer: Após o agrupamento, as parcelas agrupadas aparecerão em vermelho.
   - Resultado esperado: Você verá as parcelas agrupadas destacadas, indicando que foram consolidadas em uma nova conta a pagar.

6. **Realizar Pagamento da Conta Agrupada**
   - Localização: Tela de Listagem de Contas a Pagar, na nova conta gerada.
   - Como fazer: Clique na conta a pagar gerada para realizar o pagamento.
   - Resultado esperado: O sistema permitirá que você prossiga com o pagamento da conta agrupada.

7. **Desagrupar Contas**
   - Localização: Tela de Listagem de Contas a Pagar, opção **Desagrupar** ao lado da conta agrupada.
   - Como fazer: Clique em **Desagrupar** para separar as parcelas que foram agrupadas.
   - Resultado esperado: As parcelas voltarão a ser exibidas individualmente na lista de contas a pagar.

8. **Editar Agrupamento**
   - Localização: Tela de Listagem de Contas a Pagar, opção **Editar** ao lado da conta agrupada.
   - Como fazer: Clique em **Editar** para modificar o agrupamento, permitindo adicionar ou excluir parcelas.
   - Resultado esperado: O sistema permitirá que você ajuste as parcelas que estão agrupadas.

**Campos e Parâmetros:**

| Campo                     | Tipo         | Obrigatório | Descrição                                               | Exemplo               |
|---------------------------|--------------|-------------|---------------------------------------------------------|-----------------------|
| `Tipo de Agrupamento`     | Dropdown     | Sim         | Seleciona o critério para o agrupamento das parcelas.  | Parceiro              |
| `Parcelas`                | Lista        | Sim         | Lista de parcelas disponíveis para agrupamento.        | Parcela 1, Parcela 2  |
| `Nova Data de Vencimento` | Data         | Sim         | Data de vencimento da nova conta a pagar gerada.       | 30/11/2023            |

**Regras de Negócio:**
- O sistema permite agrupar contas a pagar de diferentes centros de custo, mas na análise financeira, as contas serão separadas por obra.
- As parcelas agrupadas são destacadas em vermelho na tela de listagem.
- É possível desagrupar contas a qualquer momento, permitindo ajustes no agrupamento.

**Observações Importantes:**
- Ao agrupar contas, certifique-se de selecionar corretamente as parcelas, pois é possível que uma parcela errada seja incluída.
- O sistema não permite o agrupamento de contas a receber, apenas de contas a pagar.
- Para emitir boletos, o usuário deve acessar a parcela individualmente.

**Conceitos-Chave:**
- **Agrupamento**: Processo de consolidar várias parcelas em uma única conta a pagar.
- **Desagrupar**: Ação de separar parcelas que foram agrupadas anteriormente.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como agrupar contas a pagar no sistema?
- O que acontece com as parcelas após o agrupamento?
- É possível desagrupar contas a pagar? Como?

---


---


---

## 12. Emissão e Gerenciamento de Boletos

**📋 METADADOS:**
- **ID:** sec_12
- **⏱️ Minutagem:** 27:55 → 30:27
- **⏲️ Duração:** 152s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/DMvowd7eCAA?si=qrXiuODXTH9y2zNZ&t=1675)
- **📦 Módulo:** Contas a Receber
- **🏷️ Categorias:** Emissão de Boletos, Gerenciamento Financeiro, Relatórios
- **🔑 Palavras-chave:** boleto, emissão, cancelamento, extrato, parcelas, pagamento, integração bancária

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de emissão e gerenciamento de boletos dentro do sistema, incluindo a alteração de dados, envio para clientes e cancelamento de boletos. O objetivo é fornecer um guia completo para usuários que precisam gerenciar suas contas a receber de forma eficiente.

**Contexto:**
Estamos na interface do módulo de **Contas a Receber**, onde o usuário pode emitir boletos, gerenciar pagamentos e acessar informações financeiras relacionadas aos clientes.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Contas a Receber > Emissão de Boletos
- Tela/interface específica: Tela de Emissão de Boletos

**Funcionalidade Detalhada:**
A funcionalidade de emissão e gerenciamento de boletos permite ao usuário associar uma conta bancária ao boleto, alterar informações como data de vencimento e juros, e enviar o boleto ao cliente. Além disso, o sistema possibilita o cancelamento de boletos e a geração de extratos financeiros dos clientes.

### 🔹 Passo a Passo Detalhado:

1. **Associar Conta Bancária ao Boleto**
   - Localização: Tela de Emissão de Boletos
   - Como fazer: Selecione a conta bancária desejada no campo de seleção de contas.
   - Campos/Opções disponíveis:
     * `Conta Bancária`: Lista de contas disponíveis para seleção.
   - Resultado esperado: A conta bancária é associada ao boleto a ser emitido.

2. **Alterar Campos do Boleto**
   - Localização: Tela de Emissão de Boletos
   - Como fazer: Preencha ou altere os campos de data de vencimento, juros e instruções.
   - Campos/Opções disponíveis:
     * `Data de Vencimento`: Campo para inserir a nova data de vencimento.
     * `Juros`: Campo para adicionar juros ao boleto.
     * `Instrução`: Campo para adicionar instruções ou recados ao cliente.
   - Resultado esperado: Os campos são atualizados conforme as informações inseridas.

3. **Emitir o Boleto**
   - Localização: Tela de Emissão de Boletos
   - Como fazer: Clique no botão **Concluir** para emitir o boleto.
   - Resultado esperado: O boleto é emitido e seu status muda para "Emitido".

4. **Enviar Boleto ao Cliente**
   - Localização: Tela de Emissão de Boletos
   - Como fazer: Utilize as opções de envio por e-mail ou WhatsApp.
   - Observações importantes: O envio pode ser feito diretamente pelo sistema, utilizando o botão correspondente.
   - Resultado esperado: O boleto é enviado ao cliente pelo meio selecionado.

5. **Cancelar Boleto**
   - Localização: Tela de Emissão de Boletos
   - Como fazer: Clique no botão **Excluir Boletos**.
   - Observações importantes: Esta ação cancela o boleto, impedindo que o cliente realize o pagamento.
   - Resultado esperado: O boleto é cancelado e não pode mais ser pago.

6. **Gerar Extrato do Cliente**
   - Localização: Tela de Emissão de Boletos
   - Como fazer: Clique na opção para gerar o extrato.
   - Resultado esperado: Um extrato em PDF é gerado, contendo todas as parcelas pagas e pendentes do cliente, além do saldo devedor.

7. **Parcelar Conta a Receber**
   - Localização: Tela de Emissão de Boletos
   - Como fazer: Acesse a opção de parcelamento e altere a data de vencimento e o valor de cada parcela.
   - Campos/Opções disponíveis:
     * `Data de Vencimento`: Campo para inserir a nova data de vencimento da parcela.
     * `Valor`: Campo para definir o valor de cada parcela.
     * `Forma de Pagamento`: Campo para selecionar a forma de pagamento.
   - Resultado esperado: As parcelas são configuradas conforme as informações inseridas.

8. **Receber Pagamento**
   - Localização: Tela de Emissão de Boletos
   - Como fazer: Clique no botão **Receber** para registrar o pagamento.
   - Observações importantes: Para usuários sem integração bancária, o registro é manual. Para usuários com integração, o sistema registra automaticamente ao importar o retorno.
   - Resultado esperado: A parcela é marcada como recebida.

**Campos e Parâmetros:**

| Campo                 | Tipo         | Obrigatório | Descrição                                              | Exemplo               |
|-----------------------|--------------|-------------|--------------------------------------------------------|-----------------------|
| Conta Bancária        | Dropdown     | Sim         | Seleção da conta bancária para emissão do boleto.     | Conta Corrente 1234   |
| Data de Vencimento    | Data         | Sim         | Data limite para pagamento do boleto.                  | 30/12/2023            |
| Juros                 | Numérico     | Não         | Taxa de juros a ser aplicada ao boleto.                | 2%                    |
| Instrução             | Texto livre  | Não         | Mensagem ou instrução adicional para o cliente.        | "Favor pagar até a data." |
| Valor                 | Numérico     | Sim         | Valor total do boleto a ser pago.                      | R$ 150,00             |
| Forma de Pagamento     | Dropdown     | Sim         | Método de pagamento selecionado.                        | Cartão, Boleto, etc.  |

**Regras de Negócio:**
- O boleto só pode ser cancelado antes do pagamento.
- O sistema deve registrar automaticamente o pagamento se a integração bancária estiver ativa.
- O extrato deve incluir todas as parcelas, tanto pagas quanto pendentes.

**Observações Importantes:**
- Sempre verifique a data de vencimento antes de emitir o boleto.
- Evite cancelar boletos após o envio ao cliente para não gerar confusão.
- O extrato pode ser útil para acompanhar a situação financeira do cliente.

**Conceitos-Chave:**
- **Emissão de Boleto**: Processo de criação de um documento de cobrança que pode ser enviado ao cliente.
- **Integração Bancária**: Conexão do sistema com o banco para automatizar o registro de pagamentos.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso emitir um boleto para um cliente?
- O que acontece se eu cancelar um boleto já emitido?
- Como posso gerar um extrato das contas a receber do meu cliente?

---


---


---

## 13. Lançamento de Notas Fiscais no Sistema

**📋 METADADOS:**
- **ID:** sec_13
- **⏱️ Minutagem:** 30:25 → 33:01
- **⏲️ Duração:** 156s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/DMvowd7eCAA?si=qrXiuODXTH9y2zNZ&t=1825)
- **📦 Módulo:** Contas a Pagar
- **🏷️ Categorias:** Operacional, Cadastro, Relatório
- **🔑 Palavras-chave:** notas fiscais, XML, recibo de produto, ordem de compra, integração CFI

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de lançamento de notas fiscais no sistema, abordando tanto notas eletrônicas no formato XML quanto notas manuais. O objetivo é garantir que os usuários compreendam como registrar corretamente as notas e associá-las a ordens de compra.

**Contexto:**
Estamos na funcionalidade de lançamento de notas fiscais dentro do módulo de Contas a Pagar. O objetivo é registrar notas fiscais, seja manualmente ou através de importação de notas eletrônicas, e associá-las a ordens de compra existentes.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Contas a Pagar > Lançamento de Notas
- Tela/interface específica: Tela de Lançamento de Notas Fiscais

**Funcionalidade Detalhada:**
A funcionalidade de lançamento de notas fiscais permite que os usuários registrem notas fiscais eletrônicas no formato XML ou notas manuais. As notas eletrônicas são importadas automaticamente do CNPJ da empresa, enquanto as notas manuais podem ser inseridas diretamente no sistema. O sistema também permite a associação de notas a ordens de compra, facilitando o controle de estoque e a gestão financeira.

### 🔹 Passo a Passo Detalhado:

1. **Selecionar o Tipo de Nota**
   - Localização: Tela de Lançamento de Notas Fiscais
   - Como fazer: No campo de seleção de tipo de nota, escolha entre "Nota Eletrônica" ou "Nota Manual".
   - Campos/Opções disponíveis:
     * `Tipo de Nota`: Opções incluem "Nota Eletrônica" (somente formato XML) e "Nota Manual".
   - Resultado esperado: O sistema ajusta os campos disponíveis com base na seleção do tipo de nota.

2. **Associar a Nota a um Parceiro**
   - Localização: Campo de seleção de parceiro na tela de lançamento
   - Como fazer: Clique no campo de seleção e escolha o parceiro relacionado à nota. O sistema exibirá uma lista de parceiros cadastrados.
   - Observações importantes: Se houver uma ordem de compra em aberto para o parceiro selecionado, essa informação será utilizada para associar a nota.
   - Resultado esperado: O parceiro é associado à nota e a ordem de compra correspondente é identificada.

3. **Preencher a Data de Emissão**
   - Localização: Campo "Data de Emissão"
   - Como fazer: Clique no campo e insira a data em que a nota foi emitida.
   - Campos/Opções disponíveis:
     * `Data de Emissão`: Formato de data (DD/MM/AAAA).
   - Resultado esperado: A data é registrada e utilizada para relatórios e controle financeiro.

4. **Adicionar Observações (Opcional)**
   - Localização: Campo "Observações"
   - Como fazer: Clique no campo e insira qualquer observação relevante sobre a nota.
   - Resultado esperado: As observações são salvas junto com os dados da nota.

5. **Inserir o Número da Nota**
   - Localização: Campo "Número da Nota"
   - Como fazer: Clique no campo e insira o número da nota fiscal.
   - Resultado esperado: O número da nota é registrado para referência futura.

6. **Anexar Arquivo da Nota (PDF)**
   - Localização: Botão "Adicionar Arquivo"
   - Como fazer: Clique no botão e selecione o arquivo PDF da nota fiscal em seu dispositivo.
   - Resultado esperado: O arquivo PDF é anexado à nota fiscal no sistema.

7. **Visualizar Produtos da Ordem de Compra**
   - Localização: Seção de produtos na tela de lançamento
   - Como fazer: Após associar a nota a uma ordem de compra, os produtos dessa ordem aparecerão automaticamente.
   - Resultado esperado: Os produtos são listados com suas respectivas quantidades e valores unitários.

8. **Ajustar Quantidade Recebida**
   - Localização: Campo "Quantidade"
   - Como fazer: No campo correspondente ao produto, insira a quantidade recebida. Por exemplo, se a ordem de compra tinha 12 unidades, mas foram recebidas apenas 5, insira "5".
   - Observações importantes: A ordem de compra permanecerá com status "Em Andamento" até que a quantidade total seja recebida.
   - Resultado esperado: A quantidade recebida é registrada e a ordem de compra é atualizada.

**Campos e Parâmetros:**

| Campo                     | Tipo       | Obrigatório | Descrição                                             | Exemplo            |
|---------------------------|------------|-------------|-----------------------------------------------------|--------------------|
| Tipo de Nota              | Dropdown   | Sim         | Seleção entre Nota Eletrônica ou Nota Manual        | Nota Eletrônica     |
| Parceiro                  | Dropdown   | Sim         | Seleção do parceiro associado à nota                 | Fornecedor XYZ      |
| Data de Emissão           | Data       | Sim         | Data em que a nota foi emitida                       | 15/10/2023          |
| Observações               | Texto      | Não         | Observações adicionais sobre a nota                   | Nota referente a... |
| Número da Nota            | Texto      | Sim         | Número da nota fiscal emitida                        | 123456              |
| Arquivo da Nota (PDF)     | Upload     | Não         | Anexo do arquivo PDF da nota fiscal                  | nota_fiscal.pdf     |
| Quantidade                | Numérico   | Sim         | Quantidade de produtos recebidos                     | 5                  |

**Regras de Negócio:**
- Notas eletrônicas devem estar no formato XML.
- Notas de serviço ainda não são suportadas.
- A associação de notas a ordens de compra é obrigatória se houver uma ordem em aberto.
- A quantidade recebida deve ser menor ou igual à quantidade total da ordem de compra.

**Observações Importantes:**
- É recomendável verificar se a ordem de compra está correta antes de associar a nota.
- Evite inserir manualmente produtos se eles já estiverem listados na ordem de compra.
- O sistema não permitirá o lançamento de notas sem um parceiro associado.

**Conceitos-Chave:**
- **Nota Eletrônica**: Documento fiscal digital que substitui a nota fiscal em papel, emitida em formato XML.
- **Ordem de Compra**: Documento que formaliza a compra de produtos ou serviços, que pode ser associado a notas fiscais.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como lançar uma nota fiscal eletrônica no sistema?
- Quais são os tipos de notas que posso registrar?
- Como associar uma nota fiscal a uma ordem de compra existente?

---


---


---

## 14. Rateio de Produtos em Notas Fiscais

**📋 METADADOS:**
- **ID:** sec_14
- **⏱️ Minutagem:** 32:58 → 35:32
- **⏲️ Duração:** 154s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/DMvowd7eCAA?si=qrXiuODXTH9y2zNZ&t=1978)
- **📦 Módulo:** Gestão de Notas Fiscais
- **🏷️ Categorias:** Operacional, Financeiro, Rateio
- **🔑 Palavras-chave:** rateio, nota fiscal, despesas, parcelas, contas a pagar

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como realizar o rateio de produtos em notas fiscais, permitindo a distribuição de despesas entre diferentes obras ou projetos, facilitando a gestão financeira da empresa.

**Contexto:**
Estamos na funcionalidade de rateio de produtos dentro do módulo de Gestão de Notas Fiscais. O objetivo é permitir que empresas que realizam compras únicas possam distribuir os custos entre diferentes obras ou projetos, garantindo um controle financeiro mais eficaz.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Gestão de Notas Fiscais > Rateio de Produtos
- Tela/interface específica: Tela de Rateio de Notas Fiscais

**Funcionalidade Detalhada:**
A funcionalidade de rateio permite que o usuário distribua os produtos de uma nota fiscal entre diferentes obras. Ao clicar no ícone de rateio, o usuário pode especificar quantas unidades de um produto vão para cada obra e associar uma classificação a essa despesa. É importante notar que, ao realizar o rateio, não é possível adicionar parcelas adicionais à nota, sendo necessário lançar a nota com o valor integral primeiro.

### 🔹 Passo a Passo Detalhado:

1. **Acessar a Tela de Rateio**
   - Localização: Menu Principal > Gestão de Notas Fiscais > Rateio de Produtos
   - Como fazer: Clique no ícone de rateio ao lado da nota fiscal que deseja ratear.
   - Campos/Opções disponíveis:
     * `Unidades`: Campo onde você insere a quantidade de produtos a serem rateados.
     * `Obra`: Dropdown para selecionar a obra para a qual as unidades estão sendo rateadas.
   - Resultado esperado: O sistema permitirá que você insira a quantidade de unidades e a obra correspondente.

2. **Distribuir as Unidades**
   - Localização: Tela de Rateio de Produtos
   - Como fazer: Após selecionar a obra, insira a quantidade de unidades que serão alocadas para essa obra e clique em "Adicionar".
   - Observações importantes: Você pode repetir esse processo para cada obra que deseja ratear. O restante das unidades deve ser alocado a outra obra ou ao responsável indicado, como "Adriano Mouras".
   - Resultado esperado: As unidades serão distribuídas conforme especificado, e a tela mostrará um resumo da distribuição.

3. **Associar Classificação à Despesa**
   - Localização: Após a distribuição das unidades
   - Como fazer: Selecione uma classificação para a despesa no campo correspondente.
   - Campos/Opções disponíveis:
     * `Classificação`: Dropdown com opções de classificação de despesas.
   - Resultado esperado: A despesa será classificada corretamente, facilitando a gestão financeira.

4. **Preencher Campos de Desconto ou Frete**
   - Localização: Tela de Rateio de Produtos
   - Como fazer: Insira valores nos campos de desconto ou frete, se aplicável.
   - Campos/Opções disponíveis:
     * `Desconto`: Campo numérico para inserir o valor do desconto.
     * `Frete`: Campo numérico para inserir o valor do frete.
   - Resultado esperado: Os valores de desconto e frete serão registrados na nota fiscal.

5. **Finalizar o Rateio**
   - Localização: Tela de Rateio de Produtos
   - Como fazer: Clique no botão "Salvar" para concluir o rateio.
   - Resultado esperado: O sistema gera automaticamente uma conta a pagar referente à nota fiscal, agrupando as parcelas de acordo com as obras rateadas.

**Campos e Parâmetros:**

| Campo          | Tipo      | Obrigatório | Descrição                                               | Exemplo         |
|----------------|-----------|-------------|---------------------------------------------------------|------------------|
| `Unidades`     | Numérico  | Sim         | Quantidade de produtos a serem rateados                | 3                |
| `Obra`         | Dropdown  | Sim         | Seleção da obra para a qual as unidades estão sendo rateadas | Terceira Obra    |
| `Classificação`| Dropdown  | Sim         | Classificação da despesa relacionada à nota            | Despesa de Material |
| `Desconto`     | Numérico  | Não         | Valor do desconto aplicado à nota                       | 50,00            |
| `Frete`        | Numérico  | Não         | Valor do frete aplicado à nota                          | 20,00            |

**Regras de Negócio:**
- Não é possível adicionar parcelas a uma nota que já foi rateada; a nota deve ser lançada com valor integral.
- O sistema gera automaticamente uma conta a pagar para cada obra rateada.
- O pagamento é realizado de forma agrupada, mas as parcelas são registradas individualmente para cada obra.

**Observações Importantes:**
- Ao realizar o rateio, certifique-se de que todas as unidades foram alocadas corretamente.
- Evite deixar campos obrigatórios em branco, pois isso pode causar erros no registro da nota.
- O pagamento deve ser feito de forma agrupada, mas as despesas devem ser acompanhadas individualmente.

**Conceitos-Chave:**
- **Rateio**: Processo de distribuição de custos entre diferentes obras ou projetos.
- **Conta a Pagar**: Registro financeiro que representa uma obrigação de pagamento da empresa.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso ratear produtos de uma nota fiscal entre diferentes obras?
- É possível adicionar parcelas a uma nota já rateada?
- O que acontece com as despesas após o rateio ser concluído?

---


---


---

## 15. Geração de Notas Fiscais com Recorrência

**📋 METADADOS:**
- **ID:** sec_15
- **⏱️ Minutagem:** 35:29 → 38:04
- **⏲️ Duração:** 155s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/DMvowd7eCAA?si=qrXiuODXTH9y2zNZ&t=2129)
- **📦 Módulo:** Financeiro
- **🏷️ Categorias:** Configuração, Cadastro, Operacional
- **🔑 Palavras-chave:** recorrência, nota fiscal, serviços, pagamento, consolidação

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como gerar notas fiscais com recorrência mensal, associar serviços a essas notas e realizar o pagamento diretamente no sistema, evitando etapas adicionais.

**Contexto:**
Estamos na interface do módulo financeiro do sistema, onde o usuário pode lançar notas fiscais com a opção de recorrência. O objetivo é facilitar a gestão de despesas e receitas que ocorrem em intervalos regulares.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Financeiro > Lançamento de Notas Fiscais
- Tela/interface específica: Tela de Lançamento de Notas Fiscais

**Funcionalidade Detalhada:**
A funcionalidade permite ao usuário gerar notas fiscais com a opção de recorrência, facilitando o lançamento de despesas ou receitas que se repetem mensalmente. O usuário pode associar serviços a essas notas e, caso necessário, adicionar novos serviços. Além disso, é possível realizar o pagamento diretamente na tela de lançamento, sem a necessidade de acessar outra área do sistema.

### 🔹 Passo a Passo Detalhado:

1. **Selecionar Tipo de Recorrência**
   - Localização: Campo de seleção de tipo de recorrência na tela de lançamento de notas fiscais.
   - Como fazer: Clique na lista suspensa e selecione a opção "Recorrência Mensal".
   - Campos/Opções disponíveis:
     * `Tipo de Recorrência`: Opções incluem "Mensal", "Semanal", "Anual".
   - Resultado esperado: O sistema configura a nota fiscal para ser gerada mensalmente.

2. **Associar Ordem de Serviço (se aplicável)**
   - Localização: Campo de associação de ordem de serviço na tela de lançamento.
   - Como fazer: Se houver uma ordem de serviço em aberto, selecione-a. Caso contrário, prossiga para adicionar serviços.
   - Observações importantes: A associação é opcional e depende da existência de ordens de serviço abertas.
   - Resultado esperado: A nota fiscal é associada à ordem de serviço selecionada, se aplicável.

3. **Adicionar Serviços**
   - Localização: Botão "Mais Serviço" na tela de lançamento.
   - Como fazer: Clique em "Mais Serviço" para abrir a tela de cadastro de novos serviços.
   - Resultado esperado: O usuário pode adicionar um novo serviço que será incluído na nota fiscal.

4. **Lançar Valor Consolidado**
   - Localização: Campo de valor na tela de lançamento.
   - Como fazer: Insira o valor real da nota fiscal que está sendo lançada.
   - Resultado esperado: O valor é registrado como o valor consolidado da nota fiscal.

5. **Classificação da Nota**
   - Localização: Campo de classificação na tela de lançamento.
   - Como fazer: Preencha a classificação, se desejado. Este campo não é obrigatório.
   - Observações importantes: A classificação ajuda a evitar que despesas ou receitas apareçam como não identificadas no fluxo de caixa.
   - Resultado esperado: A nota fiscal é classificada corretamente, se a informação for fornecida.

6. **Consolidação de Parcelas**
   - Localização: Campo de parcelas na tela de lançamento.
   - Como fazer: Para notas não recorrentes, insira a quantidade de parcelas, data de vencimento e valor de cada parcela.
   - Observações importantes: Notas com recorrência não podem ser parceladas.
   - Resultado esperado: As informações de parcelamento são registradas, se aplicável.

7. **Realizar Pagamento**
   - Localização: Botão de pagamento na tela de lançamento.
   - Como fazer: Se a conta já foi paga, clique no botão para realizar o pagamento diretamente.
   - Resultado esperado: O pagamento é registrado sem a necessidade de acessar a área de contas a pagar.

8. **Consolidação Mensal**
   - Localização: Campo de consolidação na tela de lançamento.
   - Como fazer: Para as parcelas que aparecem em amarelo, acesse a nota e insira a data de vencimento e o valor referente ao mês.
   - Observações importantes: É necessário consolidar a nota antes de realizar o pagamento.
   - Resultado esperado: A nota fica habilitada para pagamento após a consolidação.

9. **Adicionar PDF da Nota**
   - Localização: Opção para anexar PDF na tela de lançamento.
   - Como fazer: Clique na opção para adicionar o PDF da nota fiscal.
   - Resultado esperado: O PDF da nota fiscal é anexado à nota lançada.

**Campos e Parâmetros:**

| Campo                     | Tipo         | Obrigatório | Descrição                                                                 | Exemplo            |
|---------------------------|--------------|-------------|---------------------------------------------------------------------------|--------------------|
| Tipo de Recorrência       | Dropdown     | Sim         | Seleção do tipo de recorrência da nota fiscal.                           | Mensal             |
| Ordem de Serviço          | Dropdown     | Não         | Associação com uma ordem de serviço em aberto, se existir.               | Ordem #123         |
| Valor                     | Numérico     | Sim         | Valor total da nota fiscal a ser lançada.                               | 110,00             |
| Classificação             | Texto        | Não         | Classificação da nota fiscal para identificação no fluxo de caixa.       | Despesa de Água     |
| Parcelas                  | Numérico     | Não         | Quantidade de parcelas, se aplicável.                                    | 3                  |
| Data de Vencimento        | Data         | Não         | Data de vencimento de cada parcela, se aplicável.                        | 30/11/2023         |
| PDF da Nota               | Anexo        | Não         | Anexo do PDF da nota fiscal.                                            | nota_fiscal.pdf    |

**Regras de Negócio:**
- Notas fiscais com recorrência não podem ser parceladas.
- A classificação da nota é opcional, mas recomendada para melhor organização.
- As parcelas que não foram consolidadas aparecem em amarelo e não podem ser pagas até que sejam consolidadas.

**Observações Importantes:**
- É recomendável sempre consolidar o valor da nota antes de realizar o pagamento.
- Evite deixar parcelas não consolidadas, pois isso pode gerar confusão no fluxo de caixa.
- O sistema permite o pagamento direto na tela de lançamento, facilitando a gestão financeira.

**Conceitos-Chave:**
- **Recorrência**: Refere-se à repetição de uma transação financeira em intervalos regulares, como mensalmente.
- **Consolidação**: Processo de registrar o valor real de uma nota fiscal, permitindo que ela seja paga.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso gerar uma nota fiscal com recorrência mensal?
- O que fazer se eu não tiver um serviço cadastrado?
- Como realizar o pagamento de uma nota fiscal diretamente na tela de lançamento?

---


---


---

## 16. Exclusão de Notas Não Consolidada e Fluxo de Caixa

**📋 METADADOS:**
- **ID:** sec_16
- **⏱️ Minutagem:** 38:03 → 40:37
- **⏲️ Duração:** 154s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/DMvowd7eCAA?si=qrXiuODXTH9y2zNZ&t=2283)
- **📦 Módulo:** Gestão Financeira
- **🏷️ Categorias:** Exclusão, Relatório, Fluxo de Caixa
- **🔑 Palavras-chave:** nota, exclusão, recorrência, fluxo de caixa, gráficos

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como excluir notas não consolidadas no sistema e como utilizar a funcionalidade de fluxo de caixa para gerar gráficos e estatísticas financeiras. O objetivo é permitir que o usuário gerencie suas notas e visualize informações financeiras de maneira eficaz.

**Contexto:**
Estamos na interface do módulo de Gestão Financeira, onde o usuário pode gerenciar suas notas fiscais e visualizar o fluxo de caixa. Esta seção aborda a exclusão de notas não consolidadas e a criação de gráficos para análise financeira.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Gestão Financeira > Notas Fiscais
- Tela/interface específica: Tela de Notas Fiscais

**Funcionalidade Detalhada:**

A funcionalidade permite que o usuário exclua notas não consolidadas, removendo também as recorrências associadas a essas notas. É importante notar que as notas já pagas não serão afetadas pela exclusão. Além disso, o sistema gera automaticamente uma nova parcela sempre que uma nota é consolidada, renovando a recorrência até que o usuário decida excluí-la.

### 🔹 Passo a Passo Detalhado:

1. **Acessar Notas Não Consolidadas**
   - Localização: Tela de Notas Fiscais
   - Como fazer: Navegue até a seção de notas não consolidadas na tela de Notas Fiscais.
   - Resultado esperado: O sistema exibirá uma lista de notas não consolidadas.

2. **Excluir Nota Não Consolidada**
   - Localização: Ao lado da nota não consolidada desejada, haverá um botão **Excluir**.
   - Como fazer: Clique no botão **Excluir** correspondente à nota que deseja remover.
   - Observações importantes: A exclusão não afetará notas já pagas; apenas notas em aberto serão removidas, incluindo suas recorrências.
   - Resultado esperado: A nota não consolidada e suas recorrências serão excluídas do sistema.

3. **Visualizar Fluxo de Caixa**
   - Localização: Menu Principal > Gestão Financeira > Fluxo de Caixa
   - Como fazer: Acesse a seção de Fluxo de Caixa para visualizar as informações financeiras.
   - Resultado esperado: O sistema mostrará um resumo do fluxo de caixa, incluindo saldos anteriores.

4. **Criar Gráficos de Estatísticas**
   - Localização: Dentro da seção de Fluxo de Caixa, procure pela funcionalidade **Estatísticas**.
   - Como fazer: Clique em **Estatísticas** para abrir a interface de criação de gráficos.
   - Campos/Opções disponíveis:
     * `Nome do Gráfico`: Campo para inserir o nome do gráfico que deseja criar.
     * `Tipo`: Selecione entre quatro opções disponíveis para o tipo de gráfico.
     * `Período`: Defina o período para o gráfico, podendo ser diário, semanal, mensal ou uma data específica.
   - Resultado esperado: O sistema permitirá que você visualize gráficos baseados nas informações financeiras selecionadas.

5. **Selecionar Itens para Gráficos**
   - Localização: Na interface de criação de gráficos.
   - Como fazer: Selecione até três itens por categoria para incluir no gráfico.
   - Observações importantes: Se você tentar adicionar mais de três itens em uma categoria, o sistema retirará itens de outra categoria automaticamente.
   - Resultado esperado: O gráfico será gerado com base nas seleções feitas.

**Campos e Parâmetros:**

| Campo               | Tipo         | Obrigatório | Descrição                                               | Exemplo              |
|---------------------|--------------|-------------|---------------------------------------------------------|----------------------|
| Nome do Gráfico     | Texto        | Sim         | Nome que identifica o gráfico criado.                  | "Despesas Mensais"   |
| Tipo                 | Dropdown     | Sim         | Tipo de gráfico a ser gerado (ex: Barra, Linha, Pizza).| "Barra"              |
| Período             | Dropdown     | Sim         | Período de análise (Diário, Semanal, Mensal, Específico).| "Mensal"             |

**Regras de Negócio:**
- A exclusão de notas não consolidadas remove também suas recorrências.
- Notas já pagas permanecem no sistema e não são afetadas pela exclusão.
- O sistema gera uma nova parcela sempre que uma nota é consolidada, mantendo a recorrência ativa até que o usuário a exclua.

**Observações Importantes:**
- Sempre verifique se a nota a ser excluída não possui pagamentos associados.
- Evite adicionar mais de três itens em uma única categoria ao criar gráficos para evitar a remoção de itens de outras categorias.

**Conceitos-Chave:**
- **Nota Não Consolidada**: Nota fiscal que ainda não foi consolidada no sistema, podendo ser excluída.
- **Fluxo de Caixa**: Relatório que mostra a movimentação financeira, incluindo entradas e saídas.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso excluir uma nota não consolidada no sistema?
- O que acontece com as recorrências ao excluir uma nota?
- Como posso criar gráficos para visualizar meu fluxo de caixa?

---


---


---

## 17. Análise Financeira e Fluxo de Caixa

**📋 METADADOS:**
- **ID:** sec_17
- **⏱️ Minutagem:** 40:34 → 43:08
- **⏲️ Duração:** 154s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/DMvowd7eCAA?si=qrXiuODXTH9y2zNZ&t=2434)
- **📦 Módulo:** Análise Financeira
- **🏷️ Categorias:** Relatório, Operacional, Finanças
- **🔑 Palavras-chave:** saldo atual, contas bancárias, receitas, despesas, classificação, movimentações

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como visualizar e analisar o saldo atual e as movimentações financeiras em um sistema de fluxo de caixa, permitindo ao usuário filtrar informações específicas sobre receitas e despesas, além de classificar e corrigir movimentações financeiras.

**Contexto:**
Estamos na interface do módulo de Análise Financeira, onde o usuário pode monitorar as entradas e saídas efetivadas, bem como o saldo atual e previsto das contas bancárias cadastradas no sistema.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Análise Financeira > Fluxo de Caixa
- Tela/interface específica: Tela de Análise de Fluxo de Caixa

**Funcionalidade Detalhada:**
A funcionalidade permite ao usuário visualizar o saldo atual, que é o somatório de todas as contas bancárias cadastradas, além de exibir as entradas e saídas previstas. O sistema apresenta um gráfico padrão que ilustra as receitas, despesas e saldos das contas bancárias. O usuário pode filtrar as informações exibidas, focando apenas nas receitas e despesas, e obter uma análise detalhada das movimentações financeiras.

### 🔹 Passo a Passo Detalhado:

1. **Visualizar Saldo Atual**
   - Localização: Tela de Análise de Fluxo de Caixa, seção superior.
   - Como fazer: O saldo atual é exibido automaticamente na tela, calculado a partir do somatório de todas as contas bancárias cadastradas.
   - Resultado esperado: O usuário visualiza o saldo atual de todas as contas bancárias.

2. **Visualizar Saldo Final Previsto**
   - Localização: Abaixo do saldo atual na mesma tela.
   - Como fazer: O saldo final previsto é exibido automaticamente, representando o somatório das contas bancárias cadastradas.
   - Resultado esperado: O usuário vê o saldo final previsto.

3. **Analisar Gráfico de Movimentações**
   - Localização: Abaixo dos saldos, na seção de gráficos.
   - Como fazer: O gráfico padrão apresenta informações sobre receitas, despesas e saldos. O usuário pode passar o mouse sobre o gráfico para verificar valores específicos de entradas e saídas em cada dia.
   - Resultado esperado: O usuário obtém uma visualização gráfica das movimentações financeiras.

4. **Filtrar Informações**
   - Localização: Área de filtro na parte superior do gráfico.
   - Como fazer: O usuário pode selecionar opções de filtro para visualizar apenas receitas e despesas. Para isso, deve clicar na opção desejada.
   - Resultado esperado: O gráfico e as informações exibidas são atualizados para mostrar apenas as receitas e despesas selecionadas.

5. **Análise Financeira por Obra**
   - Localização: Seção de análise financeira abaixo do gráfico.
   - Como fazer: O usuário pode filtrar por obra, tipo (atrasado, previsto, realizado) e período. Para isso, deve selecionar as opções desejadas nos dropdowns.
   - Resultado esperado: O sistema exibe informações sobre quanto já foi recebido e quanto falta receber, além de quanto já foi pago e quanto falta pagar referente à obra selecionada.

6. **Classificação de Movimentações**
   - Localização: Seção de classificações na tela de fluxo de caixa.
   - Como fazer: O usuário pode selecionar uma classificação para as receitas e despesas. Se não preencher, as movimentações aparecerão como "despesas ou receitas não identificadas".
   - Resultado esperado: O sistema atualiza as movimentações com a classificação selecionada.

7. **Alterar Classificação de Movimentação**
   - Localização: Ao lado de cada movimentação listada.
   - Como fazer: O usuário deve clicar em "Alterar Classificação" e selecionar a classificação correta desejada.
   - Resultado esperado: A movimentação é atualizada com a nova classificação.

**Campos e Parâmetros:**

| Campo                       | Tipo        | Obrigatório | Descrição                                                                 | Exemplo                |
|-----------------------------|-------------|-------------|---------------------------------------------------------------------------|------------------------|
| Saldo Atual                 | Numérico    | Não         | Somatório de todas as contas bancárias cadastradas.                       | R$ 10.000,00           |
| Saldo Final Previsto        | Numérico    | Não         | Somatório previsto das contas bancárias cadastradas.                      | R$ 15.000,00           |
| Classificação               | Dropdown    | Não         | Classificação das receitas e despesas.                                    | "Receita de Vendas"    |
| Tipo de Análise             | Dropdown    | Não         | Tipo de análise a ser realizada (atrasado, previsto, realizado).         | "Previsto"             |
| Período                     | Dropdown    | Não         | Período para o qual a análise será realizada.                            | "Últimos 30 dias"      |

**Regras de Negócio:**
- O saldo atual é calculado automaticamente com base nas contas bancárias cadastradas.
- As movimentações sem classificação aparecem como "despesas ou receitas não identificadas".
- O usuário pode alterar a classificação de uma movimentação a qualquer momento.

**Observações Importantes:**
- É recomendável preencher a classificação para evitar confusões nas análises.
- O usuário deve verificar se as movimentações estão corretamente classificadas para evitar erros na análise financeira.
- O sistema permite a visualização de dados históricos, facilitando o acompanhamento financeiro.

**Conceitos-Chave:**
- **Saldo Atual**: O total disponível em todas as contas bancárias cadastradas no sistema.
- **Classificação**: Categoria atribuída a uma receita ou despesa, que ajuda na organização e análise financeira.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso visualizar o saldo atual das minhas contas bancárias?
- O que fazer se uma movimentação financeira estiver classificada incorretamente?
- Como posso filtrar as informações para ver apenas receitas e despesas específicas?

---


---


---

## 18. Exportação de Relatórios de Fluxo de Caixa

**📋 METADADOS:**
- **ID:** sec_18
- **⏱️ Minutagem:** 43:04 → 44:01
- **⏲️ Duração:** 57s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/DMvowd7eCAA?si=qrXiuODXTH9y2zNZ&t=2584)
- **📦 Módulo:** Módulo Financeiro
- **🏷️ Categorias:** Relatório, Financeiro, Exportação
- **🔑 Palavras-chave:** fluxo de caixa, relatório, totalizadores, movimentações, cliente, CPF, CNPJ, conciliação

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como exportar relatórios de fluxo de caixa, detalhando as opções disponíveis e as informações que podem ser obtidas a partir desses relatórios, como totalizadores e movimentações associadas.

**Contexto:**
Estamos no Módulo Financeiro do sistema, onde o usuário pode acessar funcionalidades relacionadas à gestão financeira, incluindo a exportação de relatórios que ajudam a visualizar e analisar o fluxo de caixa.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Financeiro > Relatórios > Exportação de Relatórios
- Tela/interface específica: Tela de Exportação de Relatórios

**Funcionalidade Detalhada:**

A funcionalidade de exportação de relatórios de fluxo de caixa permite que os usuários obtenham informações financeiras de forma resumida ou detalhada. Existem duas opções principais para a exportação: **Fluxo de Caixa Resumido** e **Fluxo de Caixa Completo**. O fluxo de caixa resumido traz totalizadores referentes a cada classificação, enquanto o fluxo de caixa completo inclui todas as movimentações associadas a essas classificações, como o nome do cliente, CPF ou CNPJ, e o status de conciliação da conta.

### 🔹 Passo a Passo Detalhado:

1. **Selecionar Tipo de Relatório**
   - Localização: Tela de Exportação de Relatórios
   - Como fazer: Na tela, o usuário deve escolher entre as opções disponíveis para exportação. As opções são:
     * **Fluxo de Caixa Resumido**: Traz totalizadores de cada classificação.
     * **Fluxo de Caixa Completo**: Inclui totalizadores e todas as movimentações associadas.
   - Resultado esperado: O sistema ajusta a visualização de acordo com a opção selecionada.

2. **Visualizar Informações do Relatório**
   - Localização: Após selecionar o tipo de relatório
   - Como fazer: O usuário pode visualizar as informações na tela, que incluem:
     * Totalizadores de cada classificação.
     * Movimentações associadas, que incluem:
       - Nome do cliente
       - CPF ou CNPJ
       - Status de conciliação (se a conta já foi conciliada ou não)
   - Observações importantes: O usuário deve verificar se as informações estão corretas antes de prosseguir com a exportação.
   - Resultado esperado: O usuário tem uma visão clara das informações que serão exportadas.

3. **Exportar Relatório**
   - Localização: Botão de exportação na tela
   - Como fazer: Após revisar as informações, o usuário deve clicar no botão **Exportar** para gerar o relatório no formato desejado (ex: PDF, Excel).
   - Resultado esperado: O sistema gera o relatório e inicia o download do arquivo.

**Campos e Parâmetros:**

| Campo                     | Tipo         | Obrigatório | Descrição                                           | Exemplo                |
|---------------------------|--------------|-------------|-----------------------------------------------------|------------------------|
| Tipo de Relatório         | Dropdown     | Sim         | Seleciona o tipo de relatório a ser exportado.     | Fluxo de Caixa Completo|
| Nome do Cliente           | Texto        | Não         | Nome do cliente associado à movimentação.           | João da Silva          |
| CPF                       | Texto        | Não         | CPF do cliente associado à movimentação.            | 123.456.789-00         |
| CNPJ                      | Texto        | Não         | CNPJ do cliente associado à movimentação.           | 12.345.678/0001-95     |
| Status de Conciliação     | Checkbox      | Não         | Indica se a conta foi conciliada ou não.           | [ ] Conciliada         |

**Regras de Negócio:**
- O relatório de fluxo de caixa resumido deve sempre apresentar totalizadores por classificação.
- O relatório de fluxo de caixa completo deve incluir todas as movimentações, com informações detalhadas sobre cada uma.
- O status de conciliação deve ser atualizado no sistema antes da exportação do relatório.

**Observações Importantes:**
- É recomendado revisar as informações exibidas na tela antes de realizar a exportação.
- Erros comuns incluem a seleção do tipo de relatório incorreto, o que pode levar a uma visualização inadequada das informações.
- Certifique-se de que todas as movimentações estejam corretamente registradas no sistema antes de gerar o relatório.

**Conceitos-Chave:**
- **Fluxo de Caixa Resumido**: Relatório que apresenta apenas os totalizadores de cada classificação financeira.
- **Fluxo de Caixa Completo**: Relatório que inclui totalizadores e todas as movimentações financeiras detalhadas.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso exportar um relatório de fluxo de caixa?
- Quais informações estão disponíveis no relatório de fluxo de caixa completo?
- O que significa o status de conciliação no relatório de fluxo de caixa?

---


---

