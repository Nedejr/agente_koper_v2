# 📚 Documentação: Passo a passo - Módulo de RH

**🎥 Vídeo Original:** https://youtu.be/0SpGZ3et0qs?si=o_T6kuqnOGErZtoO

**📊 Total de Seções:** 17

**ℹ️ Nota:** Cada seção abaixo contém um link direto para o trecho específico do vídeo tutorial.

---

---

## 1. Cadastro de Colaboradores no Módulo de Recursos Humanos

**📋 METADADOS:**
- **ID:** sec_1
- **⏱️ Minutagem:** 00:00 → 02:35
- **⏲️ Duração:** 155s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/0SpGZ3et0qs?si=o_T6kuqnOGErZtoO&t=0)
- **📦 Módulo:** Recursos Humanos
- **🏷️ Categorias:** Cadastro, Administração, Operacional
- **🔑 Palavras-chave:** cadastro de colaboradores, informações gerais, cargo, salário, alocação

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como cadastrar colaboradores no módulo de Recursos Humanos, detalhando os campos obrigatórios e complementares necessários para um registro completo e eficaz.

**Contexto:**
Estamos no módulo de Recursos Humanos, especificamente na aba de colaboradores, onde o objetivo é cadastrar novos colaboradores de acordo com as diretrizes da empresa.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Recursos Humanos > Aba Colaboradores
- Tela/interface específica: Tela de Cadastro de Colaboradores

**Funcionalidade Detalhada:**

O cadastro de colaboradores permite que a empresa registre informações essenciais sobre seus funcionários, facilitando a gestão de recursos humanos. É crucial que os dados sejam preenchidos corretamente, pois influenciam na geração de folhas de pagamento e eventos relacionados.

### 🔹 Passo a Passo Detalhado:

1. **Acessar a aba de colaboradores**
   - Localização: Menu Principal > Módulo Recursos Humanos > Aba Colaboradores
   - Como fazer: Clique na aba "Colaboradores" para acessar a tela de gerenciamento de colaboradores.
   - Resultado esperado: A tela de colaboradores será exibida, mostrando a lista de colaboradores cadastrados e opções para adicionar novos.

2. **Cadastrar um novo colaborador**
   - Localização: Tela de Colaboradores
   - Como fazer: Clique no botão **"Mais Colaborador"**.
   - Campos/Opções disponíveis:
     * `Nome do Colaborador`: Campo de texto para inserir o nome completo do colaborador.
     * `Departamento`: Dropdown para selecionar o departamento ao qual o colaborador pertence.
     * `Data de Admissão`: Campo de data para inserir a data em que o colaborador foi admitido.
   - Resultado esperado: Após preencher os campos obrigatórios, clique em **"Salvar"** para registrar o colaborador no sistema.

3. **Acessar informações adicionais do colaborador**
   - Localização: Tela de detalhes do colaborador recém-cadastrado
   - Como fazer: Selecione o colaborador na lista e clique para editar ou visualizar detalhes.
   - Observações importantes: Após o cadastro inicial, você poderá acessar vários outros campos para complementar as informações do colaborador.
   - Resultado esperado: A tela de detalhes do colaborador será exibida, permitindo o preenchimento de informações adicionais.

4. **Preencher informações gerais**
   - Localização: Tela de detalhes do colaborador
   - Como fazer: Na lateral da tela, localize a seção de **Informações Gerais** e clique em **"Mais Associar Cargo"**.
   - Campos/Opções disponíveis:
     * `Cargo`: Dropdown com pré-cadastros de cargos. Você pode selecionar um existente ou cadastrar um novo.
     * `Tipo de Vínculo`: Dropdown para selecionar o tipo de vínculo (ex: aprendiz, LT, estagiário, PJ).
     * `Data Inicial`: Campo de data para inserir a data de início no cargo.
     * `Data Final`: Campo de data opcional, normalmente não preenchido a menos que haja uma estrutura de carreira definida.
   - Resultado esperado: O cargo e tipo de vínculo do colaborador serão associados, permitindo a geração de folhas e eventos.

**Campos e Parâmetros:**

| Campo               | Tipo       | Obrigatório | Descrição                                                       | Exemplo               |
|---------------------|------------|-------------|-----------------------------------------------------------------|-----------------------|
| Nome do Colaborador  | Texto      | Sim         | Nome completo do colaborador                                    | João Silva            |
| Departamento        | Dropdown   | Sim         | Departamento ao qual o colaborador pertence                    | Recursos Humanos      |
| Data de Admissão    | Data       | Sim         | Data em que o colaborador foi admitido                         | 01/01/2023            |
| Cargo               | Dropdown   | Sim         | Cargo que o colaborador ocupa                                   | Analista de RH        |
| Tipo de Vínculo     | Dropdown   | Sim         | Tipo de vínculo do colaborador (ex: PJ, CLT, Estagiário)      | CLT                   |
| Data Inicial        | Data       | Sim         | Data de início no cargo                                         | 01/01/2023            |
| Data Final          | Data       | Não         | Data de término do cargo, se aplicável                         | 31/12/2023            |

**Regras de Negócio:**
- O preenchimento dos campos `Nome do Colaborador`, `Departamento` e `Data de Admissão` é obrigatório para o cadastro.
- Os campos `Cargo`, `Salário` e `Alocação` são essenciais para a geração de folhas de pagamento e eventos.
- A `Data Final` deve ser preenchida apenas em casos de alteração de cargo.

**Observações Importantes:**
- É recomendável revisar as informações antes de salvar para evitar erros.
- Erros comuns incluem não preencher os campos obrigatórios, o que impede o cadastro do colaborador.
- Certifique-se de que os cargos e departamentos estejam previamente cadastrados para evitar confusões.

**Conceitos-Chave:**
- **Cargo**: Posição ou função que o colaborador ocupa na empresa.
- **Tipo de Vínculo**: Classificação do relacionamento do colaborador com a empresa (ex: CLT, PJ).

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                     | Solução                                              | Prevenção                          |
|-----------------------------------|------------------------------------|------------------------------------------------------|------------------------------------|
| Não é possível salvar o colaborador | Campos obrigatórios não preenchidos | Verifique se todos os campos obrigatórios estão preenchidos | Revise as informações antes de salvar |
| Cargo não aparece na lista         | Cargo não cadastrado               | Cadastre o cargo na seção de cargos antes de associá-lo | Mantenha a lista de cargos atualizada |

**💡 DICAS E BOAS PRÁTICAS:**
- Utilize sempre nomes completos e corretos para evitar confusões futuras.
- Mantenha os cargos e departamentos atualizados no sistema para facilitar o cadastro.
- Revise as permissões de acesso para garantir que todos os usuários possam cadastrar colaboradores.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Cadastro de um novo colaborador**
```
Situação: A empresa contrata um novo analista de recursos humanos.
Ação: 
  • Campo Nome do Colaborador: "Maria Oliveira"
  • Campo Departamento: "Recursos Humanos"
  • Campo Data de Admissão: "15/10/2023"
Resultado: O colaborador "Maria Oliveira" é cadastrado com sucesso no sistema.
```

**Exemplo 2: Alteração de cargo de um colaborador**
```
Situação: João Silva foi promovido a gerente de projetos.
Ação: 
  • Campo Cargo: "Gerente de Projetos"
  • Campo Tipo de Vínculo: "CLT"
  • Campo Data Inicial: "01/11/2023"
Resultado: O cargo de João Silva é atualizado para "Gerente de Projetos" no sistema.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** Os cargos e departamentos devem estar previamente cadastrados no sistema.
- **Habilita:** A geração de folhas de pagamento e eventos relacionados ao colaborador.
- **Relacionado a:** Módulo de Folha de Pagamento, Módulo de Treinamentos.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como cadastrar um colaborador?"
- **Com problema:** "Não consigo cadastrar um colaborador, o que fazer?"
- **Informal:** "Como eu coloco um novo funcionário no sistema?"
- **Por sintoma:** "O que fazer se o sistema não deixar salvar o colaborador?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Adicionar colaborador", "Cadastrar funcionário", "Novo colaborador", "Inserir colaborador"
- "Registro de colaborador", "Cadastro de funcionário"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como faço para cadastrar um novo colaborador?
- Quais campos são obrigatórios no cadastro de colaboradores?
- O que fazer se não conseguir salvar o cadastro de um colaborador?
- Quais informações adicionais posso preencher após o cadastro?
- O que preciso fazer antes de cadastrar um colaborador?

---


---


---

## 2. Configuração da Jornada de Trabalho e Salário

**📋 METADADOS:**
- **ID:** sec_2
- **⏱️ Minutagem:** 02:32 → 05:04
- **⏲️ Duração:** 152s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/0SpGZ3et0qs?si=o_T6kuqnOGErZtoO&t=152)
- **📦 Módulo:** Gestão de Colaboradores
- **🏷️ Categorias:** Configuração, Cadastro, Administração
- **🔑 Palavras-chave:** jornada de trabalho, salário, cargo, alocação, controle de ponto

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de configuração da jornada de trabalho e do salário de colaboradores, permitindo ajustes específicos para cada colaborador, mesmo que uma base já tenha sido definida para o cargo.

**Contexto:**
Estamos na interface de configuração de colaboradores, onde é possível definir a jornada de trabalho e o salário de cada colaborador. O objetivo é personalizar as informações de acordo com as necessidades específicas de cada funcionário, mesmo que existam configurações padrão para os cargos.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Gestão de Colaboradores > Configuração de Colaboradores
- Tela/interface específica: Tela de Configuração de Colaboradores

**Funcionalidade Detalhada:**
A funcionalidade permite que o usuário configure a jornada de trabalho e o salário de colaboradores. É possível ajustar horários de expediente e definir diferentes tipos de salário (diarista, horista, mensalista, semanal) conforme a categoria do colaborador. Além disso, o sistema permite o registro de períodos iniciais e finais para os salários, possibilitando um histórico de alterações.

### 🔹 Passo a Passo Detalhado:

1. **Definir a Jornada de Trabalho**
   - Localização: Tela de Configuração de Colaboradores, seção de Jornada de Trabalho
   - Como fazer: Após adicionar um colaborador, clique em **Próximo** para acessar a seção de jornada de trabalho. Aqui, você verá os campos preenchidos automaticamente com base no cargo configurado.
   - Campos/Opções disponíveis:
     * `Dia da Semana`: Selecione o dia (ex: **Sexta-feira**)
     * `Horário de Expediente`: Insira o horário final (ex: **15:00**)
   - Resultado esperado: A jornada de trabalho do colaborador é atualizada com o novo horário.

2. **Definir o Salário**
   - Localização: Tela de Configuração de Colaboradores, seção de Salário
   - Como fazer: Clique em **Mais Salário** para adicionar um novo registro de salário. Selecione o tipo de salário desejado (ex: **Salário Mensal**).
   - Observações importantes: O tipo de salário varia conforme a categoria do colaborador. Para um diarista, preencha o salário diário e as horas trabalhadas por dia. Para um horista, preencha o valor da hora. Para um mensalista, insira o salário mensal e a quantidade de horas mensais.
   - Resultado esperado: O salário é salvo e aparece na tela inicial, junto com o cargo do colaborador.

3. **Adicionar Período de Salário**
   - Localização: Tela de Configuração de Salário
   - Como fazer: Após definir o salário, insira o **Período Inicial** e, se necessário, o **Período Final**. O período final não é obrigatório, mas é recomendado para manter um histórico.
   - Resultado esperado: As informações de salário são salvas e ficam disponíveis para consulta futura.

4. **Editar Salário e Cargo**
   - Localização: Tela de Configuração de Colaboradores
   - Como fazer: Para editar um salário ou cargo, clique na opção de **Editar** ao lado do registro desejado. Preencha a **Data Final** e adicione um novo registro.
   - Resultado esperado: O histórico de alterações é mantido, permitindo rastrear as mudanças de cargo e salário do colaborador.

5. **Configurar Alocações**
   - Localização: Tela de Configuração de Colaboradores, seção de Alocações
   - Como fazer: Adicione as alocações referentes às obras nas quais o colaborador esteve envolvido. É possível adicionar mais de uma alocação por mês.
   - Resultado esperado: As alocações são registradas e ficam vinculadas ao colaborador.

**Campos e Parâmetros:**

| Campo                | Tipo               | Obrigatório | Descrição                                           | Exemplo               |
|----------------------|--------------------|-------------|-----------------------------------------------------|-----------------------|
| `Dia da Semana`      | Dropdown           | Sim         | Seleciona o dia da semana para a jornada de trabalho| Sexta-feira           |
| `Horário de Expediente` | Horário         | Sim         | Define o horário final do expediente                 | 15:00                 |
| `Tipo de Salário`    | Dropdown           | Sim         | Seleciona o tipo de salário (Diarista, Horista, etc.)| Salário Mensal        |
| `Valor do Salário`   | Numérico           | Sim         | Valor do salário a ser pago ao colaborador          | 3000,00               |
| `Período Inicial`    | Data               | Sim         | Data de início do salário                            | 01/01/2023            |
| `Período Final`      | Data               | Não         | Data de término do salário                           | 31/12/2023            |

**Regras de Negócio:**
- O campo **Período Final** não é obrigatório, mas é recomendado para manter um histórico.
- O tipo de salário deve ser selecionado de acordo com a categoria do colaborador.
- As alocações podem ser adicionadas em múltiplas entradas por mês.

**Observações Importantes:**
- Sempre verifique se os horários de expediente estão corretos antes de salvar.
- Evite deixar o **Período Final** em branco se houver uma alteração de cargo ou salário, para garantir um histórico completo.
- As alocações devem ser registradas para garantir que o colaborador tenha um histórico de suas atividades.

**Conceitos-Chave:**
- **Jornada de Trabalho**: Refere-se ao horário que o colaborador deve cumprir, podendo ser ajustado conforme a necessidade.
- **Salário**: Valor que o colaborador recebe, que pode variar conforme a categoria e o tipo de contrato.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                     | Solução                                         | Prevenção                                   |
|-----------------------------------|------------------------------------|------------------------------------------------|---------------------------------------------|
| Não consigo salvar a jornada de trabalho | Campo de horário não preenchido | Preencha todos os campos obrigatórios          | Verifique se todos os campos obrigatórios estão preenchidos antes de salvar |
| Salário não aparece na tela inicial | Salário não foi salvo corretamente | Revise os passos e salve novamente             | Sempre confirme que o salário foi salvo após a configuração |
| Alocação não registrada           | Falta de informações necessárias   | Adicione as informações faltantes e salve      | Certifique-se de que todas as alocações estão completas antes de finalizar |

**💡 DICAS E BOAS PRÁTICAS:**
- Utilize a opção de **Editar** para manter um histórico claro de alterações.
- Sempre revise as configurações de jornada e salário após cada alteração.
- Mantenha registros atualizados para facilitar futuras consultas.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Configuração de um Mensalista**
```
Situação: João Silva é um colaborador mensalista.
Ação: 
  • Campo Tipo de Salário: "Salário Mensal"
  • Campo Valor do Salário: "3000,00"
  • Campo Período Inicial: "01/01/2023"
Resultado: O salário de João Silva é registrado como 3000,00 mensais, com início em 01/01/2023.
```

**Exemplo 2: Ajuste de Jornada de Trabalho**
```
Situação: Maria Oliveira tem um horário de expediente que precisa ser ajustado.
Ação: 
  • Campo Dia da Semana: "Sexta-feira"
  • Campo Horário de Expediente: "15:00"
Resultado: O horário de expediente de Maria é atualizado para terminar às 15:00 na sexta-feira.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O cargo do colaborador deve estar previamente configurado.
- **Habilita:** A configuração de alocações e relatórios de horas trabalhadas.
- **Relacionado a:** Módulo de Relatórios de Colaboradores e Gestão de Projetos.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como configurar a jornada de trabalho de um colaborador?"
- **Com problema:** "Não consigo adicionar o salário de um colaborador, o que fazer?"
- **Informal:** "Como eu coloco o horário de trabalho do funcionário?"
- **Por sintoma:** "Quando tento salvar a jornada, não funciona, por que?"
- **Com variação:** "Qual é o processo para ajustar o salário de um colaborador?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Definir jornada", "ajustar horário", "configurar salário", "editar salário", "adicionar alocação"
- "Salário mensal", "salário por hora", "salário diário", "salário semanal"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como faço para definir a jornada de trabalho de um colaborador?
- Quais são os tipos de salário que posso configurar?
- O que fazer se o salário não aparecer na tela inicial?
- Como posso editar o salário de um colaborador?
- O que preciso fazer antes de configurar a jornada de trabalho?

---


---


---

## 3. Cadastro e Controle de Ponto de Colaboradores

**📋 METADADOS:**
- **ID:** sec_3
- **⏱️ Minutagem:** 05:02 → 07:35
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/0SpGZ3et0qs?si=o_T6kuqnOGErZtoO&t=302)
- **📦 Módulo:** Cadastro de Colaboradores
- **🏷️ Categorias:** Cadastro, Controle de Ponto, Folha de Pagamento
- **🔑 Palavras-chave:** cadastro, colaborador, ponto, alocação, demissão

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de cadastro e controle de ponto de colaboradores, incluindo como registrar alocações, editar informações e inativar colaboradores. O objetivo é garantir que as informações estejam corretas para a geração automática da folha de pagamento.

**Contexto:**
Estamos na seção de cadastro de colaboradores dentro do sistema, onde o usuário pode gerenciar as informações dos colaboradores e registrar suas alocações e pontos.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Cadastro de Colaboradores > Submenu Controle de Ponto
- Tela/interface específica: Tela de Cadastro de Colaboradores

**Funcionalidade Detalhada:**
Esta funcionalidade permite ao usuário cadastrar colaboradores, registrar suas alocações e controlar o ponto. O sistema gera automaticamente a folha de pagamento com base nas alocações registradas. É importante que as informações estejam sempre atualizadas, especialmente em casos de demissão ou alteração de alocação.

### 🔹 Passo a Passo Detalhado:

1. **Cadastro de Alocação**
   - Localização: Tela de Cadastro de Colaboradores
   - Como fazer: Preencha os campos necessários para a obra já cadastrada, incluindo a data inicial. Após preencher, clique no botão **Salvar**.
   - Campos/Opções disponíveis:
     * `Data Inicial`: Campo de data onde deve ser inserida a data de início da alocação.
     * `Data Final`: Campo de data que deve ser preenchido se houver uma alteração na alocação.
   - Resultado esperado: A alocação do colaborador é registrada e estará disponível para referência na geração da folha de pagamento.

2. **Edição de Alocação**
   - Localização: Tela de Cadastro de Colaboradores
   - Como fazer: Se houver uma alteração na alocação, clique em **Editar**, preencha a `Data Final` e adicione uma nova alocação.
   - Observações importantes: Mesmo que a alteração ocorra dentro do mesmo mês, é necessário registrar a nova alocação para que o sistema possa gerar o rateio corretamente.
   - Resultado esperado: O sistema atualiza as alocações do colaborador e gera a folha de pagamento com as informações corretas.

3. **Inativação de Colaborador**
   - Localização: Aba de Dados Profissionais
   - Como fazer: Clique em **Dados Profissionais**, edite as informações gerais e preencha a `Data de Demissão`. 
   - Resultado esperado: O colaborador se torna inativo no sistema a partir da data de demissão preenchida.

4. **Registro de Ponto**
   - Localização: Tela de Controle de Ponto
   - Como fazer: Na tela inicial, utilize os filtros para localizar o colaborador ou clique em **+ Data Ponto** para registrar manualmente. Selecione o colaborador e a data desejada.
   - Observações importantes: O registro de ponto é mais eficiente quando todos os campos do colaborador estão preenchidos, pois ele aparecerá automaticamente na tela.
   - Resultado esperado: O colaborador é adicionado à lista para registro de ponto.

5. **Registrar Batida de Ponto**
   - Localização: Tela Inicial de Controle de Ponto
   - Como fazer: Clique no símbolo de **Registrar Batida de Ponto**. Insira os horários de entrada, saída para o almoço, retorno e conclusão do expediente.
   - Campos/Opções disponíveis:
     * `Horário de Entrada`: Campo para inserir o horário de início do expediente.
     * `Saída para Almoço`: Campo para registrar o horário de saída para o intervalo.
     * `Retorno`: Campo para registrar o horário de retorno do intervalo.
     * `Conclusão do Expediente`: Campo para registrar o horário de término do expediente.
   - Resultado esperado: O ponto do colaborador é registrado para o dia específico.

**Campos e Parâmetros:**

| Campo                  | Tipo     | Obrigatório | Descrição                                           | Exemplo            |
|------------------------|----------|-------------|----------------------------------------------------|--------------------|
| Data Inicial           | Data     | Sim         | Data de início da alocação do colaborador          | 01/10/2023         |
| Data Final             | Data     | Não         | Data de término da alocação, se houver alteração   | 31/10/2023         |
| Data de Demissão       | Data     | Sim         | Data em que o colaborador foi demitido             | 15/11/2023         |
| Horário de Entrada      | Hora     | Sim         | Horário em que o colaborador inicia o expediente    | 08:00               |
| Saída para Almoço      | Hora     | Sim         | Horário em que o colaborador sai para o almoço      | 12:00               |
| Retorno                | Hora     | Sim         | Horário em que o colaborador retorna do almoço      | 13:00               |
| Conclusão do Expediente | Hora     | Sim         | Horário em que o colaborador finaliza o expediente  | 17:00               |

**Regras de Negócio:**
- A alocação deve ser registrada com a `Data Inicial` e, se houver alteração, a `Data Final` deve ser preenchida.
- Um colaborador se torna inativo ao preencher a `Data de Demissão`.
- O registro de ponto deve ser feito diariamente e deve incluir todos os horários relevantes.

**Observações Importantes:**
- É essencial que todos os campos do colaborador estejam preenchidos para que ele apareça na tela de registro de ponto.
- Evite registrar o ponto manualmente se o colaborador já estiver cadastrado corretamente.

**Conceitos-Chave:**
- **Alocação**: Registro de onde e quando um colaborador está designado para trabalhar.
- **Inativação**: Processo de desativar um colaborador no sistema após a demissão.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                  | Solução                                                  | Prevenção                                   |
|-----------------------------------|----------------------------------|----------------------------------------------------------|---------------------------------------------|
| Colaborador não aparece para registro de ponto | Campos não preenchidos corretamente | Verifique se todos os campos obrigatórios estão preenchidos | Sempre complete o cadastro do colaborador  |
| Erro ao salvar a alocação        | Data final não preenchida       | Preencha a `Data Final` se houver alteração             | Registre sempre a data final quando necessário |
| Colaborador não se torna inativo  | Data de demissão não preenchida | Preencha a `Data de Demissão` corretamente               | Verifique as informações antes de inativar |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre mantenha as informações dos colaboradores atualizadas para evitar problemas na geração da folha de pagamento.
- Utilize a função de filtros para facilitar a busca de colaboradores na tela de controle de ponto.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Cadastro de Alocação**
```
Situação: João Silva foi alocado para um novo projeto.
Ação: 
  • Campo Data Inicial: "01/10/2023"
Resultado: A alocação de João Silva é registrada e estará disponível para a folha de pagamento.
```

**Exemplo 2: Registro de Ponto**
```
Situação: Maria Oliveira registrou seu ponto no dia 10/10/2023.
Ação: 
  • Horário de Entrada: "08:00"
  • Saída para Almoço: "12:00"
  • Retorno: "13:00"
  • Conclusão do Expediente: "17:00"
Resultado: O ponto de Maria Oliveira é registrado corretamente para o dia.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O colaborador deve estar cadastrado e com todos os campos obrigatórios preenchidos.
- **Habilita:** A geração da folha de pagamento com base nas alocações e pontos registrados.
- **Relacionado a:** Módulo de Folha de Pagamento, onde as informações de alocação e ponto são utilizadas.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como cadastrar um colaborador?"
- **Com problema:** "Não consigo registrar o ponto do colaborador, o que fazer?"
- **Informal:** "Como faço para colocar o ponto do funcionário?"
- **Por sintoma:** "Quando o colaborador não aparece na lista de ponto, o que pode ser?"
- **Sobre demissão:** "Como inativar um colaborador no sistema?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Registrar ponto", "Controlar ponto", "Cadastrar alocação", "Inativar colaborador", "Editar colaborador"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como cadastrar uma alocação para um colaborador?
- O que fazer se o colaborador não aparecer na tela de registro de ponto?
- Como inativar um colaborador no sistema?
- O que fazer se a data de demissão não estiver sendo aceita?
- O que preciso ter preenchido antes de registrar o ponto de um colaborador?

---


---


---

## 4. Registro de Ponto do Colaborador

**📋 METADADOS:**
- **ID:** sec_4
- **⏱️ Minutagem:** 07:33 → 10:07
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/0SpGZ3et0qs?si=o_T6kuqnOGErZtoO&t=453)
- **📦 Módulo:** Controle de Ponto
- **🏷️ Categorias:** Registro, Importação, Exportação, Colaboradores
- **🔑 Palavras-chave:** registro de ponto, colaborador, planilha, Excel, importação, exportação, datas, horários

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como registrar o ponto de um colaborador utilizando diferentes métodos, incluindo a opção de registrar todos os pontos de uma vez e a utilização de planilhas Excel para facilitar o processo.

**Contexto:**
Estamos na página de controle de ponto do sistema, onde é possível gerenciar o registro de horas trabalhadas pelos colaboradores. O objetivo desta seção é detalhar como registrar pontos de forma eficiente, seja individualmente ou em massa, utilizando planilhas.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Controle de Ponto > Página de Controle de Ponto
- Tela/interface específica: Página de Controle de Ponto do Colaborador

**Funcionalidade Detalhada:**
A funcionalidade de registro de ponto permite que os usuários registrem as horas trabalhadas pelos colaboradores de maneira prática. É possível registrar pontos individualmente, em massa (registrar todos) ou através da importação de uma planilha Excel. O uso de planilhas é especialmente útil para registrar dados de forma padronizada e em grandes quantidades.

### 🔹 Passo a Passo Detalhado:

1. **Registrar Todos os Pontos**
   - Localização: Na página de controle de ponto, abaixo da lista de colaboradores.
   - Como fazer: Clique na opção **Registrar Todos**. Isso permitirá que você registre várias datas para um único colaborador de uma só vez.
   - Campos/Opções disponíveis:
     * `Data`: Data específica que você deseja registrar.
     * `Horários`: Horários de entrada e saída do colaborador.
   - Resultado esperado: O sistema irá registrar os pontos para o colaborador selecionado para as datas especificadas.

2. **Exportar Planilha**
   - Localização: Clique nos três pontinhos (menu de opções) na interface de controle de ponto.
   - Como fazer: Selecione a opção **Exportar Planilha**. Isso irá gerar uma planilha Excel padronizada que contém os campos necessários para o registro de ponto.
   - Observações importantes: A planilha é um modelo feito pelo COPER, já com os campos de acordo com o que é necessário dentro do sistema.
   - Resultado esperado: Uma planilha Excel será baixada, pronta para edição.

3. **Importar Planilha**
   - Localização: Na mesma área onde você exportou a planilha, utilize a opção de **Importar**.
   - Como fazer: Após preencher a planilha com os dados dos colaboradores, clique na opção **Importar** para carregar os dados no sistema.
   - Observações importantes: Certifique-se de que a planilha esteja no formato correto e que todos os campos obrigatórios estejam preenchidos.
   - Resultado esperado: Os dados da planilha serão importados para o sistema, registrando os pontos conforme especificado.

4. **Preencher Campos na Planilha**
   - Localização: Na planilha Excel exportada.
   - Como fazer: Preencha os campos conforme necessário:
     * `Código`: Código do colaborador (ex: 182).
     * `Nome`: Nome do colaborador (ex: Laura Nascimento).
     * `Data`: Data do registro de ponto.
     * `Horários`: Horários de entrada e saída. Para faltas, digite "falta".
   - Resultado esperado: A planilha será preenchida corretamente com os dados dos colaboradores.

**Campos e Parâmetros:**

| Campo         | Tipo   | Obrigatório | Descrição                                         | Exemplo               |
|---------------|--------|-------------|---------------------------------------------------|-----------------------|
| Código        | Numérico | Sim         | Identificação única do colaborador.               | 182                   |
| Nome          | Texto  | Sim         | Nome completo do colaborador.                      | Laura Nascimento       |
| Data          | Data   | Sim         | Data em que o ponto está sendo registrado.        | 01/10/2023            |
| Horários      | Texto  | Sim         | Horários de entrada e saída ou "falta".           | 08:00 - 17:00         |

**Regras de Negócio:**
- O registro de ponto pode ser feito semanalmente, quinzenalmente ou próximo ao fechamento da folha.
- A planilha deve seguir o modelo padronizado para que a importação funcione corretamente.
- Se um colaborador estiver ausente, o campo de horários deve conter a palavra "falta".

**Observações Importantes:**
- Sempre verifique se a planilha está no formato correto antes de importar.
- É possível preencher a planilha para um período de 30 dias, facilitando o registro em massa.
- Limpe o histórico de registros anteriores se necessário, para evitar duplicidade.

**Conceitos-Chave:**
- **Registro de Ponto**: Processo de registrar as horas trabalhadas por um colaborador.
- **Planilha Excel**: Ferramenta utilizada para facilitar a entrada de dados em massa.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                       | Solução                                      | Prevenção                                   |
|-----------------------------------|--------------------------------------|----------------------------------------------|---------------------------------------------|
| Erro ao importar planilha         | Formato da planilha incorreto       | Verifique se a planilha segue o modelo padrão. | Sempre utilize a planilha exportada como base. |
| Dados não aparecem após importação | Campos obrigatórios não preenchidos  | Certifique-se de que todos os campos obrigatórios estão preenchidos. | Revise a planilha antes da importação.     |
| Registro duplicado                | Importação realizada mais de uma vez | Limpe o histórico antes de uma nova importação. | Mantenha um controle de importações realizadas. |

**💡 DICAS E BOAS PRÁTICAS:**
- Utilize a opção de **Registrar Todos** para economizar tempo ao registrar pontos de vários colaboradores.
- Preencha a planilha com antecedência para facilitar o processo de importação.
- Sempre revise os dados antes de finalizar o registro para evitar erros.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Registro de Ponto Semanal**
```
Situação: Registrar o ponto de Laura Nascimento para a semana.
Ação: Preencher a planilha com os seguintes dados:
  • Campo Código: "182"
  • Campo Nome: "Laura Nascimento"
  • Campo Data: "01/10/2023"
  • Campo Horários: "08:00 - 17:00"
Resultado: O ponto de Laura será registrado corretamente para a data especificada.
```

**Exemplo 2: Registro de Faltas**
```
Situação: Registrar a falta de João Silva.
Ação: Preencher a planilha com os seguintes dados:
  • Campo Código: "183"
  • Campo Nome: "João Silva"
  • Campo Data: "02/10/2023"
  • Campo Horários: "falta"
Resultado: A falta de João será registrada no sistema.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O colaborador deve estar cadastrado no sistema.
- **Habilita:** O registro de ponto permite gerar relatórios de horas trabalhadas.
- **Relacionado a:** Funcionalidades de folha de pagamento e relatórios de horas.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como registrar o ponto de um colaborador?"
- **Com problema:** "Não consigo registrar o ponto, o que fazer?"
- **Informal:** "Como faço pra marcar o ponto do funcionário?"
- **Por sintoma:** "Quando a planilha não importa, o que eu faço?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Registrar ponto", "marcar ponto", "entrada e saída", "horário de trabalho"
- "Planilha de ponto", "importar dados", "exportar dados"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como registrar o ponto de um colaborador?
- O que fazer se a planilha não importar corretamente?
- Quais campos são obrigatórios para o registro de ponto?
- O que fazer se um colaborador estiver ausente?
- Como posso registrar pontos de vários colaboradores ao mesmo tempo?

---


---


---

## 5. Importação e Registro de Ponto

**📋 METADADOS:**
- **ID:** sec_5
- **⏱️ Minutagem:** 10:05 → 12:40
- **⏲️ Duração:** 154s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/0SpGZ3et0qs?si=o_T6kuqnOGErZtoO&t=605)
- **📦 Módulo:** Controle de Ponto
- **🏷️ Categorias:** Importação, Registro, Controle, Automação
- **🔑 Palavras-chave:** importação de planilha, registro de ponto, ajuste de ponto, controle ID, falta

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como importar uma planilha de registro de ponto, registrar faltas e ajustar pontos no sistema, além de descrever a integração com o sistema Control ID, proporcionando uma visão abrangente das opções de registro de ponto disponíveis.

**Contexto:**
Estamos na seção de Controle de Ponto do sistema, onde o usuário pode registrar e gerenciar a frequência dos colaboradores. O objetivo é ensinar como importar dados de ponto de uma planilha, registrar faltas e ajustar entradas de ponto.

**Localização no Sistema:**
- Caminho de navegação: Menu Principal > Controle de Ponto
- Tela/interface específica: Tela de Registro de Ponto

**Funcionalidade Detalhada:**
A funcionalidade permite ao usuário importar uma planilha previamente preenchida com dados de ponto, registrar faltas e ajustar entradas de ponto de colaboradores. O sistema também oferece uma integração com o Control ID para automação do registro de ponto.

### 🔹 Passo a Passo Detalhado:

1. **Importar Planilha de Registro de Ponto**
   - Localização: Tela de Controle de Ponto, ícone de três pontinhos (menu de opções).
   - Como fazer: Clique nos três pontinhos e selecione a opção de **Importar Planilha**. Em seguida, escolha o arquivo da planilha que deseja importar.
   - Campos/Opções disponíveis:
     * `Arquivo`: Seletor de arquivo para escolher a planilha.
   - Resultado esperado: A planilha é importada e os dados de ponto dos colaboradores são atualizados no sistema. Por exemplo, a colaboradora Laura Nascimento terá suas datas de ponto registradas corretamente.

2. **Registrar Falta**
   - Localização: Tela de Controle de Ponto, ícone de "X" ao lado do nome do colaborador.
   - Como fazer: Clique no ícone "X" para registrar uma falta para o colaborador selecionado.
   - Observações importantes: O sistema confirmará que a falta foi registrada.
   - Resultado esperado: A falta é registrada e refletida no histórico de ponto do colaborador.

3. **Ajustar Ponto**
   - Localização: Tela de Controle de Ponto, ícone de ajuste (símbolo de lápis ou similar).
   - Como fazer: Clique no ícone de ajuste ao lado do registro de ponto do colaborador. Insira uma justificativa para o ajuste e clique em **Salvar**.
   - Observações importantes: O sistema calculará a diferença entre as horas registradas e as horas ajustadas.
   - Resultado esperado: O ponto do colaborador é ajustado e a justificativa é salva.

4. **Visualizar Dados do Colaborador**
   - Localização: Tela de Controle de Ponto, clique no nome do colaborador.
   - Como fazer: Selecione o colaborador desejado para visualizar detalhes.
   - Campos/Opções disponíveis:
     * `Período`: Seletor para definir o intervalo de datas a ser visualizado.
     * `Jornada de Trabalho`: Exibe a jornada padrão do colaborador.
     * `Totais de Horas`: Mostra horas trabalhadas, horas negativas e atestados.
   - Resultado esperado: O sistema exibe todas as informações de ponto do colaborador, incluindo a jornada e totais de horas.

**Campos e Parâmetros:**

| Campo                     | Tipo      | Obrigatório | Descrição                                   | Exemplo                |
|---------------------------|-----------|-------------|---------------------------------------------|------------------------|
| `Arquivo`                 | Upload    | Sim         | Campo para selecionar a planilha a ser importada | `Registro_Ponto.xlsx`  |
| `Justificativa`           | Texto     | Sim         | Campo para inserir a justificativa do ajuste | `Consulta médica`      |
| `Período`                 | Data      | Não         | Seletor de intervalo de datas               | `01/01/2023 - 31/01/2023` |

**Regras de Negócio:**
- A planilha deve estar no formato correto para ser importada.
- O registro de falta deve ser confirmado pelo sistema.
- O ajuste de ponto deve incluir uma justificativa válida.

**Observações Importantes:**
- Verifique se a planilha está preenchida corretamente antes da importação.
- Evite registrar faltas em dias em que o colaborador já possui justificativas.
- O ajuste de ponto deve ser feito com cautela para evitar inconsistências.

**Conceitos-Chave:**
- **Importação de Planilha**: Processo de carregar dados de ponto de um arquivo externo para o sistema.
- **Ajuste de Ponto**: Modificação de um registro de ponto já existente, geralmente requerendo justificativa.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável               | Solução                                        | Prevenção                                     |
|-----------------------------------|------------------------------|------------------------------------------------|-----------------------------------------------|
| Erro ao importar planilha         | Formato de arquivo incorreto | Verifique se a planilha está no formato .xlsx  | Use sempre o modelo de planilha fornecido    |
| Falta não registrada              | Confirmação não realizada    | Certifique-se de clicar no botão de confirmação | Revise as ações antes de finalizar             |
| Ajuste de ponto não salvo         | Justificativa não preenchida | Preencha o campo de justificativa              | Sempre insira uma justificativa ao ajustar    |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre faça um backup da planilha antes de importá-la.
- Utilize a funcionalidade de visualização de dados para verificar informações antes de registrar faltas ou ajustes.
- Mantenha a planilha atualizada para evitar erros de importação.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Importação de Planilha**
```
Situação: Importar a planilha de ponto para o dia 19.
Ação: 
  • Campo `Arquivo`: Selecionar `Ponto_Colaboradores_19.xlsx`
Resultado: Os dados de ponto para Laura Nascimento são atualizados com as datas corretas.
```

**Exemplo 2: Ajuste de Ponto**
```
Situação: Ajustar o ponto de João Silva que saiu mais cedo.
Ação: 
  • Campo `Justificativa`: Inserir "Consulta médica"
Resultado: O ponto de João Silva é ajustado e a justificativa é salva, mostrando a diferença de horas.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** A planilha deve ser preenchida corretamente e estar no formato adequado.
- **Habilita:** A funcionalidade de registro automático de ponto com o sistema Control ID.
- **Relacionado a:** Funcionalidades de relatórios de ponto e gestão de colaboradores.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como importar uma planilha de ponto?"
- **Com problema:** "Não consigo registrar faltas, o que fazer?"
- **Informal:** "Como faço pra ajustar o ponto do meu funcionário?"
- **Por sintoma:** "O que fazer se a planilha não carrega?"
- **Com dúvida:** "Como visualizar os dados de um colaborador?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Importar dados", "Carregar planilha", "Registrar ausência", "Ajustar horas", "Control ID integração"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como importar uma planilha de ponto?
- O que fazer se a importação falhar?
- Como registrar uma falta para um colaborador?
- O que fazer se o ajuste de ponto não for salvo?
- Quais são os pré-requisitos para a importação de planilhas?

---


---


---

## 6. Controle de Documentações dos Colaboradores

**📋 METADADOS:**
- **ID:** sec_6
- **⏱️ Minutagem:** 12:37 → 15:12
- **⏲️ Duração:** 155s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/0SpGZ3et0qs?si=o_T6kuqnOGErZtoO&t=757)
- **📦 Módulo:** Documentações
- **🏷️ Categorias:** Cadastro, Relatório, Administração
- **🔑 Palavras-chave:** documentações, colaboradores, validade, controle, registro

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como gerenciar as documentações dos colaboradores dentro do sistema, incluindo a criação de novos documentos, visualização de documentos vencidos e a importância da validade dos documentos.

**Contexto:**
Estamos na seção de documentações do sistema, onde é possível controlar e gerenciar todos os documentos relacionados aos colaboradores, garantindo que as informações estejam sempre atualizadas e em conformidade com as exigências legais.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Documentações
- Tela/interface específica: Tela Inicial de Documentações

**Funcionalidade Detalhada:**
A funcionalidade de controle de documentações permite que os usuários registrem, visualizem e gerenciem todos os documentos dos colaboradores. Isso inclui a capacidade de identificar documentos vencidos e registrar novos documentos com informações detalhadas, como data de emissão e validade.

### 🔹 Passo a Passo Detalhado:

1. **Visualização de Documentos**
   - Localização: Tela Inicial de Documentações
   - Como fazer: Ao acessar a tela inicial, você verá uma lista de todos os colaboradores que possuem algum tipo de documentação registrada no sistema.
   - Resultado esperado: Uma lista clara e organizada de colaboradores com seus respectivos documentos, incluindo a sinalização de documentos vencidos.

2. **Registro de Novo Documento**
   - Localização: Botão **"Mais Documento"** na Tela Inicial de Documentações
   - Como fazer: Clique no botão **"Mais Documento"** para iniciar o registro de um novo documento.
   - Campos/Opções disponíveis:
     * `Modelo`: Seletor para escolher o tipo de documento (ex: Atestado, Férias, etc.)
     * `Colaborador`: Campo para selecionar o colaborador ao qual o documento se refere.
     * `Tipo do Documento`: Campo para especificar o tipo de documento que está sendo registrado.
     * `Data de Emissão`: Campo para inserir a data em que o documento foi emitido.
     * `Data de Validade`: Campo para inserir a data de validade do documento (se aplicável).
     * `Descrição`: Campo opcional para adicionar informações adicionais sobre o documento.
   - Observações importantes: O campo de `Data de Validade` se tornará obrigatório se o modelo de documento configurado exigir validade.
   - Resultado esperado: O novo documento é registrado no sistema e aparece na lista de documentações do colaborador.

3. **Visualização e Download de Documentos**
   - Localização: Tela Inicial de Documentações
   - Como fazer: Na lista de documentações, você pode clicar no ícone de visualização ou download ao lado de cada documento.
   - Resultado esperado: O documento é aberto em uma nova janela ou baixado para o seu dispositivo, conforme a opção escolhida.

**Campos e Parâmetros:**

| Campo               | Tipo         | Obrigatório | Descrição                                           | Exemplo                |
|---------------------|--------------|-------------|----------------------------------------------------|------------------------|
| Modelo              | Dropdown     | Sim         | Tipo de documento a ser registrado                  | Atestado               |
| Colaborador          | Dropdown     | Sim         | Nome do colaborador ao qual o documento se refere   | João Silva             |
| Tipo do Documento    | Dropdown     | Sim         | Especifica o tipo de documento                      | Férias                 |
| Data de Emissão      | Data         | Sim         | Data em que o documento foi emitido                 | 01/10/2023             |
| Data de Validade     | Data         | Não         | Data em que o documento expira (se aplicável)      | 01/12/2023             |
| Descrição            | Texto livre  | Não         | Informações adicionais sobre o documento            | Atestado médico        |

**Regras de Negócio:**
- O campo `Data de Validade` é obrigatório se o modelo de documento exigir validade.
- O sistema sinaliza documentos vencidos com uma cor diferente e um símbolo de urgência.
- Documentos devem ser registrados corretamente para garantir a conformidade legal.

**Observações Importantes:**
- Sempre verifique se o modelo de documento requer uma data de validade antes de registrar.
- Evite registrar documentos sem a devida descrição, pois isso pode dificultar a identificação futura.

**Conceitos-Chave:**
- **Documentação**: Conjunto de documentos que precisam ser geridos para cada colaborador.
- **Validade**: Data limite até a qual um documento é considerado válido.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                     | Solução                                           | Prevenção                                      |
|-----------------------------------|------------------------------------|--------------------------------------------------|------------------------------------------------|
| Documento não aparece na lista     | Não foi registrado corretamente     | Verifique se todos os campos obrigatórios foram preenchidos | Sempre preencher todos os campos obrigatórios   |
| Campo de validade não aceita data | Modelo de documento não requer validade | Verifique as configurações do modelo de documento | Configurar corretamente os modelos de documento |

**💡 DICAS E BOAS PRÁTICAS:**
- Utilize descrições detalhadas para facilitar a identificação dos documentos no futuro.
- Mantenha os documentos sempre atualizados para evitar problemas com validade.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Registro de Atestado**
```
Situação: Um colaborador apresenta um atestado médico.
Ação: 
  • Campo Modelo: "Atestado"
  • Campo Colaborador: "Maria Oliveira"
  • Campo Tipo do Documento: "Atestado Médico"
  • Campo Data de Emissão: "01/10/2023"
  • Campo Data de Validade: "01/11/2023"
  • Campo Descrição: "Atestado de 3 dias"
Resultado: O atestado é registrado e aparece na lista de documentações de Maria Oliveira.
```

**Exemplo 2: Registro de Férias**
```
Situação: Um colaborador solicita férias.
Ação: 
  • Campo Modelo: "Férias"
  • Campo Colaborador: "Carlos Pereira"
  • Campo Tipo do Documento: "Solicitação de Férias"
  • Campo Data de Emissão: "01/10/2023"
  • Campo Data de Validade: "01/12/2023"
  • Campo Descrição: "Férias de 15 dias"
Resultado: A solicitação de férias é registrada e aparece na lista de documentações de Carlos Pereira.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O modelo de documento deve estar previamente configurado no sistema.
- **Habilita:** O registro de documentos permite a geração de relatórios sobre a situação documental dos colaboradores.
- **Relacionado a:** Funcionalidades de relatórios e controle de ponto, pois atestados e férias podem interferir na contabilização de horas.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como registrar um documento para um colaborador?"
- **Com problema:** "Não consigo ver os documentos de um colaborador, o que fazer?"
- **Informal:** "Como eu coloco um documento no sistema?"
- **Por sintoma:** "Os documentos não estão aparecendo, como resolver isso?"
- **Por necessidade:** "Quais documentos preciso registrar para cada colaborador?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Adicionar documento", "Cadastrar documento", "Registrar documentação", "Gerenciar documentos"
- "Controle de documentos", "Documentação de colaboradores"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como faço para registrar um novo documento para um colaborador?
- O que fazer se o campo de validade não estiver aceitando a data?
- Como posso visualizar os documentos vencidos de um colaborador?
- O que fazer se não consigo encontrar um documento registrado?
- Quais são os requisitos para registrar um documento no sistema?

---


---


---

## 7. Controle de Atestados e Férias

**📋 METADADOS:**
- **ID:** sec_7
- **⏱️ Minutagem:** 15:09 → 17:42
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/0SpGZ3et0qs?si=o_T6kuqnOGErZtoO&t=909)
- **📦 Módulo:** Controle de Ponto
- **🏷️ Categorias:** Cadastro, Controle, Relatório
- **🔑 Palavras-chave:** atestado, férias, colaborador, registro, controle de ponto

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como registrar e gerenciar atestados e férias de colaboradores dentro do sistema de controle de ponto, permitindo um acompanhamento eficaz das ausências e garantindo a conformidade com as normas trabalhistas.

**Contexto:**
Estamos na interface do módulo de Controle de Ponto, onde é possível gerenciar informações relacionadas a atestados e férias dos colaboradores. O objetivo é facilitar o registro e a consulta dessas informações, assegurando que todos os dados estejam organizados e acessíveis.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Controle de Ponto > Atestados e Férias
- Tela/interface específica: Tela de Controle de Ponto

**Funcionalidade Detalhada:**
A funcionalidade permite que o usuário registre e controle atestados e férias dos colaboradores de forma simples e intuitiva. O sistema possibilita a inclusão de informações detalhadas sobre cada atestado, como tipo, datas e anexos, além de registrar as férias com as respectivas datas de início e fim.

### 🔹 Passo a Passo Detalhado:

1. **Registrar Atestado**
   - Localização: Aba "Atestado" na tela de Controle de Ponto
   - Como fazer: Clique no botão **Mais Atestado** para iniciar o registro.
   - Campos/Opções disponíveis:
     * `Colaborador`: Seletor para escolher o colaborador que receberá o atestado.
     * `Tipo de Atestado`: Opções para definir se o atestado é referente a um acidente de trabalho.
     * `Data Inicial`: Campo para inserir a data de início do atestado.
     * `Data Final`: Campo para inserir a data de término do atestado.
     * `Horário`: Campo opcional para registrar o horário do atestado.
     * `CID`: Campo para preencher o Código Internacional de Doenças.
     * `Anexar Atestado`: Opção para fazer upload do documento do atestado.
     * `Descrição`: Campo para adicionar uma descrição sobre o atestado.
   - Resultado esperado: Após clicar em **Salvar**, o atestado aparecerá na tela inicial com todas as informações registradas. Se o documento estiver importado, ele será exibido em verde.

2. **Importar Atestado**
   - Localização: Na mesma aba "Atestado", após o registro.
   - Como fazer: Se o atestado não foi importado, clique na opção **Importar** para anexar o documento.
   - Observações importantes: O atestado deve ser um arquivo compatível e deve ser verificado se o colaborador está corretamente selecionado.
   - Resultado esperado: O atestado será registrado e poderá ser consultado no controle de ponto do colaborador.

3. **Registrar Férias**
   - Localização: Aba "Férias" na tela de Controle de Ponto
   - Como fazer: Clique no botão **Mais Férias** para iniciar o registro.
   - Campos/Opções disponíveis:
     * `Colaborador`: Seletor para escolher o colaborador que irá tirar férias.
     * `Data Inicial`: Campo para inserir a data de início das férias.
     * `Data Final`: Campo para inserir a data de término das férias.
   - Resultado esperado: Após clicar em **Salvar**, as férias serão registradas e aparecerão na tela para consulta.

4. **Gerenciar Cargos**
   - Localização: Aba "Cargos" na tela de Controle de Ponto
   - Como fazer: Clique no botão **Mais Cargo** para adicionar um novo cargo.
   - Campos/Opções disponíveis:
     * `Nome do Cargo`: Campo para definir o nome do cargo (ex: Gestor Financeiro).
     * `CBO`: Campo opcional para preencher a Classificação Brasileira de Ocupações.
     * `Salário Base`: Campo para definir o salário base do cargo.
     * `Categoria`: Campo para selecionar a categoria do cargo.
   - Resultado esperado: Após preencher os campos e clicar em **Salvar**, o novo cargo será adicionado ao sistema.

**Campos e Parâmetros:**

| Campo                | Tipo         | Obrigatório | Descrição                                         | Exemplo                  |
|----------------------|--------------|-------------|---------------------------------------------------|--------------------------|
| Colaborador           | Seletor      | Sim         | Seleciona o colaborador relacionado ao atestado ou férias | João Silva               |
| Tipo de Atestado     | Dropdown     | Sim         | Define o tipo de atestado (ex: Acidente de Trabalho) | Acidente de Trabalho     |
| Data Inicial          | Data         | Sim         | Data de início do atestado ou férias               | 01/10/2023               |
| Data Final            | Data         | Sim         | Data de término do atestado ou férias              | 05/10/2023               |
| Horário               | Horário      | Não         | Horário do atestado (opcional)                     | 09:00                    |
| CID                   | Texto        | Não         | Código Internacional de Doenças                    | J20                      |
| Anexar Atestado      | Upload       | Não         | Anexar documento do atestado                       | [Selecionar Arquivo]     |
| Descrição            | Texto livre  | Não         | Descrição adicional sobre o atestado               | Atestado por gripe       |
| Nome do Cargo        | Texto        | Sim         | Nome do cargo a ser cadastrado                     | Gestor Financeiro        |
| CBO                   | Texto        | Não         | Classificação Brasileira de Ocupações              | 1234-56                  |
| Salário Base         | Numérico     | Sim         | Salário base do cargo                              | 5000                     |
| Categoria            | Dropdown     | Sim         | Categoria do cargo                                 | Administração            |

**Regras de Negócio:**
- O registro de atestados deve incluir obrigatoriamente o colaborador, data inicial e data final.
- O campo de horário é opcional, mas pode ser utilizado para maior precisão.
- As férias devem ser registradas com datas que não se sobreponham a outros registros de férias ou atestados.
- O cargo deve ser associado a um colaborador para que as informações sejam válidas.

**Observações Importantes:**
- Verifique se o colaborador está ativo antes de registrar atestados ou férias.
- Evite sobreposição de datas ao registrar férias e atestados.
- O sistema permite a edição de registros, mas é recomendável manter um histórico das alterações.

**Conceitos-Chave:**
- **Atestado**: Documento que comprova a ausência do colaborador por motivos de saúde.
- **Férias**: Período de descanso a que o colaborador tem direito após um período de trabalho.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                  | Solução                                          | Prevenção                                   |
|-----------------------------------|----------------------------------|-------------------------------------------------|---------------------------------------------|
| Atestado não aparece na tela      | Documento não importado          | Verifique se o atestado foi anexado corretamente | Sempre anexar o documento ao registrar      |
| Erro ao salvar férias             | Datas sobrepostas                | Verifique se as datas não coincidem com outros registros | Conferir datas antes de salvar              |
| Campo de colaborador não habilita | Colaborador inativo              | Ative o colaborador no sistema                   | Manter cadastro de colaboradores atualizado  |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre anexe o atestado no momento do registro para evitar perda de informações.
- Utilize a descrição para adicionar detalhes que possam ser úteis em consultas futuras.
- Revise os registros periodicamente para garantir que todas as informações estejam corretas.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Registro de Atestado**
```
Situação: João Silva apresentou um atestado médico.
Ação: 
  • Campo Colaborador: "João Silva"
  • Campo Tipo de Atestado: "Acidente de Trabalho"
  • Campo Data Inicial: "01/10/2023"
  • Campo Data Final: "05/10/2023"
  • Campo CID: "J20"
Resultado: O atestado de João Silva é registrado e aparece na tela inicial em verde.
```

**Exemplo 2: Registro de Férias**
```
Situação: Maria Oliveira vai tirar férias.
Ação: 
  • Campo Colaborador: "Maria Oliveira"
  • Campo Data Inicial: "10/11/2023"
  • Campo Data Final: "24/11/2023"
Resultado: As férias de Maria Oliveira são registradas e ficam disponíveis para consulta.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O colaborador deve estar cadastrado e ativo no sistema.
- **Habilita:** O registro de atestados e férias permite a geração de relatórios de ausências.
- **Relacionado a:** Funcionalidades de gestão de colaboradores e relatórios de ponto.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como registrar um atestado?"
- **Com problema:** "Não consigo salvar o atestado, o que fazer?"
- **Informal:** "Como faço pra colocar um atestado no sistema?"
- **Por sintoma:** "O que fazer se o atestado não aparece na tela?"
- **Com variação:** "Como adicionar férias para um colaborador?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Adicionar atestado", "Cadastrar atestado", "Registrar férias", "Inserir férias"
- "Colaborador", "Funcionário", "Empregado"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como registrar um atestado para um colaborador?
- Quais informações são necessárias para registrar férias?
- O que fazer se o atestado não aparece na tela inicial?
- Como posso editar um atestado já registrado?
- O que preciso fazer antes de registrar férias para um colaborador?

---


---


---

## 8. Cadastro e Configuração de Grupos de Cargos e Feriados

**📋 METADADOS:**
- **ID:** sec_8
- **⏱️ Minutagem:** 17:39 → 20:13
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/0SpGZ3et0qs?si=o_T6kuqnOGErZtoO&t=1059)
- **📦 Módulo:** Gestão de Recursos Humanos
- **🏷️ Categorias:** Configuração, Cadastro, Administração
- **🔑 Palavras-chave:** grupo de cargos, cadastro de feriados, jornada de trabalho, gestor financeiro, feriados fixos, feriados variáveis

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como cadastrar grupos de cargos e feriados no sistema COPER, facilitando a organização de cargos e a gestão de feriados, otimizando o controle de ponto e a jornada de trabalho dos colaboradores.

**Contexto:**
Estamos na interface de gestão de recursos humanos do sistema COPER, onde o usuário pode organizar cargos e feriados, permitindo uma melhor administração de colaboradores e suas jornadas de trabalho.

**Localização no Sistema:**
- Caminho de navegação: Menu Principal > Módulo Gestão de Recursos Humanos > Submenu Cadastro de Cargos e Feriados
- Tela/interface específica: Tela de Cadastro de Cargos e Feriados

**Funcionalidade Detalhada:**

A funcionalidade permite ao usuário cadastrar grupos de cargos e feriados, organizando as informações de maneira que facilite a gestão de colaboradores. O grupo de cargos é utilizado para agrupar funções semelhantes, como, por exemplo, um gestor financeiro que se encaixa em um grupo administrativo. Além disso, o sistema já possui feriados nacionais e fixos pré-definidos, mas permite a configuração de feriados variáveis, estaduais e municipais.

### 🔹 Passo a Passo Detalhado:

1. **Cadastro de Grupo de Cargos**
   - Localização: Tela de Cadastro de Cargos
   - Como fazer: Clique no botão **"Adicionar Grupo"** ou **"Mais Grupo"**.
   - Campos/Opções disponíveis:
     * `Nome do Grupo`: Campo de texto onde você deve inserir a nomenclatura do grupo (ex: "Grupo Administrativo").
     * `Descrição`: Campo opcional para adicionar informações adicionais sobre o grupo.
   - Resultado esperado: O grupo de cargos será cadastrado e aparecerá na lista de grupos disponíveis.

2. **Definição da Jornada de Trabalho**
   - Localização: Após cadastrar o grupo de cargos, você pode definir a jornada de trabalho na mesma tela.
   - Como fazer: Preencha o campo de **"Jornada de Trabalho"** com a carga horária padrão (ex: "40 horas semanais").
   - Observações importantes: Esta configuração evita a necessidade de preencher a jornada para cada colaborador individualmente.
   - Resultado esperado: A jornada de trabalho será pré-definida para todos os colaboradores vinculados ao grupo.

3. **Cadastro de Feriados**
   - Localização: Tela de Cadastro de Feriados
   - Como fazer: Clique no botão **"Adicionar Feriado"** ou **"Mais Feriado"**.
   - Campos/Opções disponíveis:
     * `Nome do Feriado`: Campo de texto para inserir o nome do feriado (ex: "Aniversário do Município").
     * `Tipo de Feriado`: Dropdown com opções como "Estadual", "Municipal" e "Nacional".
     * `Data`: Campos para inserir o dia, mês e ano do feriado.
     * `Fixo`: Checkbox para indicar se o feriado é fixo ou não.
   - Resultado esperado: O feriado será cadastrado e aparecerá na lista de feriados configurados.

4. **Configuração de Feriados Fixos e Variáveis**
   - Localização: Na tela de cadastro de feriados, após preencher os campos.
   - Como fazer: Se o feriado for fixo, marque a opção **"Fixo"**. Se não for, preencha o campo de ano.
   - Observações importantes: Feriados fixos não requerem atualização anual, enquanto feriados variáveis precisam ser atualizados a cada ano.
   - Resultado esperado: O sistema entenderá automaticamente a periodicidade do feriado e ajustará o controle de ponto.

**Campos e Parâmetros:**

| Campo                  | Tipo         | Obrigatório | Descrição                                           | Exemplo                      |
|------------------------|--------------|-------------|----------------------------------------------------|------------------------------|
| Nome do Grupo          | Texto        | Sim         | Nome do grupo de cargos que está sendo cadastrado  | "Grupo Administrativo"       |
| Descrição              | Texto        | Não         | Informações adicionais sobre o grupo                | "Grupo para gestores"       |
| Nome do Feriado        | Texto        | Sim         | Nome do feriado a ser cadastrado                    | "Aniversário do Município"  |
| Tipo de Feriado        | Dropdown     | Sim         | Tipo do feriado (Estadual, Municipal, Nacional)    | "Municipal"                 |
| Data                   | Data         | Sim         | Data do feriado (dia, mês, ano)                    | "15/11/2024"                |
| Fixo                   | Checkbox     | Sim         | Indica se o feriado é fixo ou variável             | [ ] Fixo                    |

**Regras de Negócio:**
- O grupo de cargos deve ser único e não pode ser duplicado.
- Feriados fixos não precisam ser atualizados anualmente, enquanto feriados variáveis devem ser revisados a cada ano.
- A jornada de trabalho deve ser preenchida para cada grupo de cargos.

**Observações Importantes:**
- Sempre verifique se o nome do grupo de cargos já existe para evitar duplicações.
- Feriados estaduais e municipais devem ser configurados manualmente, pois não estão pré-definidos no sistema.
- É recomendável revisar os feriados anualmente para garantir que estão atualizados.

**Conceitos-Chave:**
- **Grupo de Cargos**: Agrupamento de funções semelhantes dentro da organização.
- **Feriado Fixo**: Feriado que ocorre na mesma data todos os anos.
- **Feriado Variável**: Feriado cuja data muda a cada ano.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                  | Solução                                                   | Prevenção                                      |
|-----------------------------------|----------------------------------|----------------------------------------------------------|------------------------------------------------|
| Não consigo cadastrar um grupo     | Nome do grupo já existe         | Verifique a lista de grupos e escolha um nome diferente  | Sempre verifique a lista antes de cadastrar    |
| Feriado não aparece no controle    | Feriado não foi salvo corretamente | Certifique-se de que todos os campos obrigatórios estão preenchidos | Preencha todos os campos obrigatórios           |
| Campo de data bloqueado            | Feriado marcado como fixo       | Desmarque a opção "Fixo" se o feriado não for fixo      | Verifique a periodicidade do feriado antes de cadastrar |

**💡 DICAS E BOAS PRÁTICAS:**
- Utilize descrições claras para grupos de cargos para facilitar a identificação.
- Revise os feriados anualmente para garantir que estão atualizados e corretos.
- Utilize a pré-definição da jornada de trabalho para economizar tempo no cadastro de colaboradores.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Cadastro de Grupo de Cargos**
```
Situação: Um novo grupo de cargos para a área administrativa precisa ser criado.
Ação: 
  • Campo Nome do Grupo: "Grupo Administrativo"
  • Campo Descrição: "Grupo para gestores e assistentes administrativos"
Resultado: O grupo "Grupo Administrativo" é cadastrado com sucesso e aparece na lista de grupos.
```

**Exemplo 2: Cadastro de Feriado Municipal**
```
Situação: O feriado de aniversário do município precisa ser adicionado.
Ação: 
  • Campo Nome do Feriado: "Aniversário do Município"
  • Campo Tipo de Feriado: "Municipal"
  • Campo Data: "15/11/2024"
  • Checkbox Fixo: [ ] (desmarcado)
Resultado: O feriado "Aniversário do Município" é cadastrado e aparecerá na lista de feriados.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O usuário deve ter permissões adequadas para cadastrar grupos de cargos e feriados.
- **Habilita:** A configuração de grupos de cargos permite uma melhor organização e gestão de colaboradores.
- **Relacionado a:** Funcionalidades de controle de ponto e gestão de jornada de trabalho.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como cadastrar um grupo de cargos?"
- **Com problema:** "Não consigo adicionar um feriado, o que fazer?"
- **Informal:** "Como eu coloco um feriado no sistema?"
- **Por sintoma:** "O que fazer se o feriado não aparece no controle de ponto?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Criar grupo de cargos", "Adicionar grupo", "Cadastrar feriado", "Configurar feriado"
- "Feriado fixo", "Feriado variável", "Grupo administrativo", "Grupo de cargos"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como cadastrar um grupo de cargos?
- Quais campos são obrigatórios para cadastrar um feriado?
- O que fazer se o sistema não aceita o nome do grupo?
- O que fazer se o feriado não aparece no controle de ponto?
- O que preciso fazer antes de cadastrar um feriado municipal?

---


---


---

## 9. Configurações de Controle de Ponto e Folha de Pagamento

**📋 METADADOS:**
- **ID:** sec_9
- **⏱️ Minutagem:** 20:10 → 22:44
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/0SpGZ3et0qs?si=o_T6kuqnOGErZtoO&t=1210)
- **📦 Módulo:** Cadastros
- **🏷️ Categorias:** Configuração, Folha de Pagamento, Controle de Ponto
- **🔑 Palavras-chave:** configurações, controle de ponto, folha de pagamento, tolerância, arredondamento

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como configurar as opções de controle de ponto e folha de pagamento no sistema, incluindo tolerâncias de horário e frações de arredondamento, permitindo uma gestão mais eficiente das jornadas de trabalho dos colaboradores.

**Contexto:**
Estamos na aba de configurações dentro do módulo de cadastros do sistema, onde o objetivo é ajustar as definições que impactam diretamente o controle de ponto e a geração de folhas de pagamento.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Cadastros > Aba Configurações
- Tela/interface específica: Tela de Configurações de Controle de Ponto e Folha de Pagamento

**Funcionalidade Detalhada:**
Esta funcionalidade permite ao usuário configurar parâmetros que influenciam o controle de ponto e a geração de folhas de pagamento. As configurações incluem o tempo de tolerância para chegada e saída dos colaboradores, frações de arredondamento, dia de fechamento da folha e limites para DSR (Descanso Semanal Remunerado).

### 🔹 Passo a Passo Detalhado:

1. **Preencher Cidade**
   - Localização: Campo de preenchimento na aba de cadastro de colaboradores
   - Como fazer: Insira o nome da cidade onde o colaborador está alocado.
   - Campos/Opções disponíveis:
     * `Cidade`: Campo de texto livre
   - Resultado esperado: A cidade será registrada e vinculada ao colaborador.

2. **Configurar Tempo de Tolerância**
   - Localização: Seção de configurações de controle de ponto
   - Como fazer: Insira o valor desejado em minutos no campo de "Tempo de Tolerância".
   - Campos/Opções disponíveis:
     * `Tempo de Tolerância`: Campo numérico (ex: 10)
   - Resultado esperado: O sistema considerará a tolerância ao calcular as horas de entrada e saída.

3. **Definir Fração de Arredondamento**
   - Localização: Seção de configurações de controle de ponto
   - Como fazer: Selecione a fração de arredondamento desejada em um dropdown.
   - Campos/Opções disponíveis:
     * `Fração de Arredondamento`: Opções como 0,25, 0,5, 1
   - Resultado esperado: O sistema aplicará a fração de arredondamento nas horas registradas.

4. **Estabelecer Dia de Fechamento**
   - Localização: Seção de configurações de folha de pagamento
   - Como fazer: Escolha o dia do mês em que a folha será fechada.
   - Campos/Opções disponíveis:
     * `Dia de Fechamento`: Campo numérico (ex: 30)
   - Resultado esperado: O sistema utilizará esta data para o fechamento da folha de pagamento.

5. **Configurar Limite de DSR**
   - Localização: Seção de configurações de folha de pagamento
   - Como fazer: Insira o limite de minutos permitidos para faltas no campo correspondente.
   - Campos/Opções disponíveis:
     * `Limite de DSR`: Campo numérico (ex: 60)
   - Resultado esperado: O sistema considerará este limite ao calcular o DSR na folha de pagamento.

6. **Configurar Tolerância em Atestados**
   - Localização: Seção de configurações de atestados
   - Como fazer: Marque a opção para permitir tolerância em horários de atestados.
   - Campos/Opções disponíveis:
     * `Permitir Tolerância em Atestados`: Checkbox
   - Resultado esperado: O sistema aplicará a tolerância definida para horários registrados em atestados.

7. **Selecionar Tipo de Salário**
   - Localização: Seção de configurações de salário
   - Como fazer: Escolha o tipo de salário desejado em um dropdown.
   - Campos/Opções disponíveis:
     * `Tipo de Salário`: Opções como "Salário Contábil" (pré-cadastrado)
   - Resultado esperado: O sistema aplicará o tipo de salário selecionado nas folhas de pagamento.

**Campos e Parâmetros:**

| Campo                       | Tipo         | Obrigatório | Descrição                                                                 | Exemplo         |
|-----------------------------|--------------|-------------|---------------------------------------------------------------------------|------------------|
| Cidade                      | Texto livre  | Sim         | Nome da cidade onde o colaborador está alocado.                          | "São Paulo"      |
| Tempo de Tolerância         | Numérico     | Sim         | Tempo em minutos que o colaborador pode atrasar sem penalização.        | 10               |
| Fração de Arredondamento    | Dropdown     | Sim         | Fração para arredondar as horas trabalhadas.                             | 0,25             |
| Dia de Fechamento           | Numérico     | Sim         | Dia do mês em que a folha de pagamento será fechada.                    | 30               |
| Limite de DSR               | Numérico     | Sim         | Limite de minutos de faltas para considerar o DSR na folha.              | 60               |
| Permitir Tolerância em Atestados | Checkbox | Não         | Permite definir tolerância para horários registrados em atestados.       | [ ] Sim          |
| Tipo de Salário             | Dropdown     | Sim         | Tipo de salário a ser utilizado nas folhas de pagamento.                 | "Salário Contábil" |

**Regras de Negócio:**
- O tempo de tolerância deve ser configurado em minutos e é aplicado ao controle de ponto.
- A fração de arredondamento deve ser escolhida entre as opções disponíveis e impacta o cálculo das horas.
- O dia de fechamento deve ser um número válido entre 1 e 31.
- O limite de DSR deve ser definido em minutos e é utilizado para calcular a folha de pagamento.
- A configuração de tolerância em atestados é opcional e pode ser ativada conforme a política da empresa.

**Observações Importantes:**
- É importante revisar as configurações periodicamente para garantir que estejam alinhadas com as políticas da empresa.
- Erros comuns incluem a inserção de valores inválidos nos campos numéricos, que podem resultar em mensagens de erro.

**Conceitos-Chave:**
- **Tempo de Tolerância**: Período em que a chegada do colaborador é aceito sem penalização.
- **Fração de Arredondamento**: Método utilizado para ajustar as horas trabalhadas para cima ou para baixo.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                            | Causa Provável                     | Solução                                               | Prevenção                                         |
|-------------------------------------|------------------------------------|------------------------------------------------------|--------------------------------------------------|
| Campo de tempo de tolerância não aceita valor | Valor fora do intervalo permitido | Verifique se o valor está entre 0 e 60 minutos.     | Defina um intervalo padrão para evitar erros.    |
| Fração de arredondamento não aparece | Não configurada previamente        | Acesse as configurações e adicione a fração desejada.| Mantenha as frações atualizadas no sistema.      |
| Dia de fechamento inválido          | Número fora do intervalo 1-31     | Insira um número válido entre 1 e 31.                | Valide as entradas antes de salvar.              |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre teste as configurações em um ambiente de desenvolvimento antes de aplicar em produção.
- Utilize a opção de ajuda do sistema para entender melhor cada campo.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Configuração de Tolerância**
```
Situação: Um colaborador tem horário de expediente das 8h às 18h.
Ação: Configurar tempo de tolerância de 10 minutos.
  • Campo Tempo de Tolerância: "10"
Resultado: O colaborador pode chegar até 8h10 sem penalização.
```

**Exemplo 2: Definição de Dia de Fechamento**
```
Situação: A empresa fecha a folha de pagamento no último dia do mês.
Ação: Definir dia de fechamento como 30.
  • Campo Dia de Fechamento: "30"
Resultado: A folha será fechada no dia 30 de cada mês.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** As configurações de colaboradores devem estar completas antes de ajustar as configurações de folha.
- **Habilita:** A configuração de tolerância permite uma gestão mais flexível das horas trabalhadas.
- **Relacionado a:** Funcionalidades de geração de relatórios de ponto e folha de pagamento.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como configurar o tempo de tolerância?"
- **Com problema:** "O que fazer se o campo de tolerância não aceita meu valor?"
- **Informal:** "Como eu coloco a tolerância no ponto?"
- **Por sintoma:** "Quando meu colaborador chega atrasado, como evitar penalização?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Configurar tolerância", "ajustar horários", "definir fechamento de folha", "salário contábil"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como configurar o tempo de tolerância no controle de ponto?
- O que é a fração de arredondamento e como utilizá-la?
- Como definir o dia de fechamento da folha de pagamento?
- O que fazer se o limite de DSR não está sendo considerado?
- O que preciso fazer antes de configurar as opções de folha de pagamento?

---


---


---

## 10. Cadastro de Rúbricas e Eventos na Folha de Pagamento

**📋 METADADOS:**
- **ID:** sec_10
- **⏱️ Minutagem:** 22:41 → 25:16
- **⏲️ Duração:** 154s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/0SpGZ3et0qs?si=o_T6kuqnOGErZtoO&t=1361)
- **📦 Módulo:** Folha de Pagamento
- **🏷️ Categorias:** Configuração, Cadastro, Eventos
- **🔑 Palavras-chave:** rúbricas, eventos, folha de pagamento, cadastro, tipos de desconto, cálculo automático

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como cadastrar rúbricas e eventos na folha de pagamento, detalhando os tipos de itens que podem ser registrados e suas características. O objetivo é garantir que os usuários possam configurar corretamente os elementos que influenciam a folha de pagamento.

**Contexto:**
Estamos na interface do módulo de Folha de Pagamento, onde o usuário pode cadastrar diferentes tipos de rúbricas e eventos que serão utilizados na geração da folha de pagamento. Esta funcionalidade é crucial para a correta configuração dos itens que impactam os cálculos de salários e descontos.

**Localização no Sistema:**
- Caminho de navegação: Menu Principal > Folha de Pagamento > Cadastro de Rúbricas
- Tela/interface específica: Tela de Cadastro de Rúbricas e Eventos

**Funcionalidade Detalhada:**
A funcionalidade de cadastro de rúbricas permite ao usuário registrar itens que serão utilizados na folha de pagamento. As rúbricas podem ser classificadas como eventos, que são itens independentes que não dependem da folha de pagamento para serem gerados. O usuário pode definir se a rúbrica será um desconto, um vencimento ou um item neutro, além de escolher entre cálculo manual ou automático.

### 🔹 Passo a Passo Detalhado:

1. **Adicionar Nomenclaturas e Definições**
   - Localização: Tela de Cadastro de Rúbricas
   - Como fazer: Clique no botão **"Mais Tipo"** para adicionar uma nova nomenclatura. Em seguida, preencha o campo com o nome desejado.
   - Campos/Opções disponíveis:
     * `Nome`: Campo de texto para inserir a nova nomenclatura.
   - Resultado esperado: A nova nomenclatura é adicionada à lista de tipos disponíveis.

2. **Registrar Tipos de Sindicato**
   - Localização: Tela de Cadastro de Rúbricas
   - Como fazer: Clique no botão **"Mais Sindicato"** e preencha o campo com o nome do sindicato que atua na empresa.
   - Campos/Opções disponíveis:
     * `Nome do Sindicato`: Campo de texto para inserir o nome do sindicato.
   - Resultado esperado: O tipo de sindicato é registrado e aparece na lista de sindicatos.

3. **Cadastrar Rúbricas**
   - Localização: Tela de Cadastro de Rúbricas
   - Como fazer: Clique no botão **"Mais Item"** para iniciar o cadastro de uma nova rúbrica.
   - Campos/Opções disponíveis:
     * `Código`: Campo numérico para definir o código da rúbrica, seguindo a sequência dos códigos já pré-cadastrados.
     * `Descrição`: Campo de texto para descrever a rúbrica (ex: "Remuneração Diarista").
     * `Evento`: Checkbox para definir se a rúbrica é um evento (marcar se for o caso).
     * `Tipo`: Dropdown com opções de:
       - Desconto
       - Vencimento
       - Neutro
     * `Tipo de Cálculo`: Dropdown com opções de:
       - Manual
       - Automático
   - Observações importantes: É essencial atualizar os cálculos automáticos antes de utilizar as rúbricas, pois muitos podem estar desatualizados.
   - Resultado esperado: A nova rúbrica é cadastrada e aparece na lista de rúbricas disponíveis.

**Campos e Parâmetros:**

| Campo                  | Tipo    | Obrigatório | Descrição                                               | Exemplo                      |
|------------------------|---------|-------------|---------------------------------------------------------|------------------------------|
| Nome                   | Texto   | Sim         | Nome da nomenclatura ou tipo de sindicato.             | "Sindicato dos Trabalhadores"|
| Código                 | Numérico| Sim         | Código único da rúbrica, seguindo a sequência existente.| "001"                        |
| Descrição              | Texto   | Sim         | Descrição da rúbrica.                                  | "Remuneração Diarista"       |
| Evento                 | Checkbox| Não         | Define se a rúbrica é um evento.                       | [ ] Evento                   |
| Tipo                   | Dropdown| Sim         | Tipo da rúbrica (Desconto, Vencimento, Neutro).       | "Vencimento"                 |
| Tipo de Cálculo       | Dropdown| Sim         | Método de cálculo (Manual ou Automático).              | "Automático"                 |

**Regras de Negócio:**
- As rúbricas devem ser cadastradas com códigos únicos.
- O tipo de cálculo deve ser definido corretamente para evitar erros nos cálculos da folha.
- Rúbricas do tipo evento não devem ser utilizadas como itens fixos de folha.

**Observações Importantes:**
- Atualize os cálculos automáticos antes de usar as rúbricas.
- Verifique se os tipos de sindicatos e nomenclaturas estão corretos para evitar confusões.

**Conceitos-Chave:**
- **Rúbrica**: Item que compõe a folha de pagamento, podendo ser um desconto, vencimento ou neutro.
- **Evento**: Item independente que pode ser gerado sem depender da folha de pagamento.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                       | Causa Provável                     | Solução                                        | Prevenção                                   |
|--------------------------------|------------------------------------|------------------------------------------------|---------------------------------------------|
| Rúbrica não aparece na folha   | Não cadastrada corretamente        | Verifique se a rúbrica foi salva e está ativa.| Sempre revisar o cadastro após a inclusão.  |
| Cálculo automático não funciona| Cálculo desatualizado             | Atualize os cálculos na tela de configurações.| Realizar atualizações periódicas.           |
| Erro ao adicionar sindicato     | Nome já existente                  | Verifique a lista de sindicatos cadastrados.  | Usar nomes únicos para cada sindicato.      |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre utilize descrições claras para facilitar a identificação das rúbricas.
- Mantenha um registro de alterações para evitar confusões futuras.
- Utilize a opção de cálculo automático sempre que possível para reduzir erros manuais.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Cadastro de uma Rúbrica de Vencimento**
```
Situação: Cadastro de uma nova rúbrica para remuneração de diaristas.
Ação: 
  • Campo Código: "002"
  • Campo Descrição: "Remuneração Diarista"
  • Campo Evento: [ ] (não marcado)
  • Campo Tipo: "Vencimento"
  • Campo Tipo de Cálculo: "Automático"
Resultado: A rúbrica "Remuneração Diarista" é cadastrada e aparece na lista de rúbricas.
```

**Exemplo 2: Cadastro de uma Rúbrica de Desconto**
```
Situação: Cadastro de uma nova rúbrica para desconto de vale transporte.
Ação: 
  • Campo Código: "003"
  • Campo Descrição: "Desconto Vale Transporte"
  • Campo Evento: [ ] (não marcado)
  • Campo Tipo: "Desconto"
  • Campo Tipo de Cálculo: "Manual"
Resultado: A rúbrica "Desconto Vale Transporte" é cadastrada e aparece na lista de rúbricas.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O módulo de Folha de Pagamento deve estar habilitado e configurado.
- **Habilita:** A geração de folhas de pagamento com os itens cadastrados.
- **Relacionado a:** Módulo de Cálculo de Folha, onde as rúbricas são utilizadas para calcular salários e descontos.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como cadastrar uma rúbrica na folha de pagamento?"
- **Com problema:** "Não consigo adicionar uma rúbrica, o que fazer?"
- **Informal:** "Como eu coloco uma nova rúbrica na folha?"
- **Por sintoma:** "Quando tento adicionar uma rúbrica, não aparece na lista."
- **Alternativa:** "Qual o processo para registrar um evento na folha de pagamento?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Adicionar rúbrica", "Cadastrar item", "Criar evento", "Registrar desconto", "Inserir vencimento"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como cadastrar uma nova rúbrica na folha de pagamento?
- O que fazer se a rúbrica não aparecer na lista?
- Como definir se uma rúbrica é um evento ou não?
- O que fazer se o cálculo automático não estiver funcionando?
- O que preciso ter configurado antes de cadastrar uma rúbrica?

---


---


---

## 11. Cálculo de Remuneração de Diaristas

**📋 METADADOS:**
- **ID:** sec_11
- **⏱️ Minutagem:** 25:13 → 27:46
- **⏲️ Duração:** 152s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/0SpGZ3et0qs?si=o_T6kuqnOGErZtoO&t=1513)
- **📦 Módulo:** Folha de Pagamento
- **🏷️ Categorias:** Cálculo, Configuração, Remuneração, Administração
- **🔑 Palavras-chave:** remuneração, cálculo automático, faixa condicional, simples direta, variáveis, dias trabalhados

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como configurar o cálculo de remuneração para diaristas, abordando as opções de cálculo manual e automático, além das diferenças entre as formas de cálculo condicional e direta.

**Contexto:**
Estamos na seção de configuração da folha de pagamento, onde o usuário pode definir como a remuneração dos colaboradores, especificamente diaristas, será calculada. O objetivo é permitir que o usuário escolha entre cálculos manuais ou automáticos, e entre diferentes formas de cálculo.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Folha de Pagamento > Configuração de Cálculo
- Tela/interface específica: Tela de Configuração de Cálculo de Remuneração

**Funcionalidade Detalhada:**
A funcionalidade permite ao usuário definir como a remuneração de diaristas será calculada. O usuário pode optar por um cálculo manual, onde os valores são inseridos manualmente, ou um cálculo automático, que utiliza variáveis e fórmulas para determinar a remuneração com base em condições específicas.

### 🔹 Passo a Passo Detalhado:

1. **Selecionar Tipo de Cálculo**
   - Localização: Tela de Configuração de Cálculo de Remuneração
   - Como fazer: No campo de seleção de tipo de cálculo, escolha entre "Manual" ou "Automático".
   - Campos/Opções disponíveis:
     * `Tipo de Cálculo`: Opções "Manual" e "Automático"
   - Resultado esperado: Se "Manual" for selecionado, o sistema aguardará que o usuário preencha os valores manualmente. Se "Automático" for selecionado, um novo campo aparecerá.

2. **Definir Forma de Cálculo**
   - Localização: Após selecionar "Automático", um campo adicional chamado "Forma de Cálculo" aparecerá.
   - Como fazer: Clique no campo "Forma de Cálculo" e escolha entre "Faixa Condicional" ou "Simples Direta".
   - Observações importantes: A "Faixa Condicional" requer que uma condição seja definida, enquanto "Simples Direta" não requer condições.
   - Resultado esperado: O sistema ajustará as opções de cálculo com base na seleção feita.

3. **Adicionar Regra para Faixa Condicional**
   - Localização: Ao selecionar "Faixa Condicional", um botão "Mais Regra" aparecerá.
   - Como fazer: Clique em "Mais Regra" para adicionar uma condição específica para o cálculo.
   - Campos/Opções disponíveis:
     * `Condição`: Defina a condição necessária para que a forma de cálculo seja aplicada.
   - Resultado esperado: O sistema permitirá a definição de uma condição que, quando atendida, aplicará a forma de cálculo especificada.

4. **Adicionar Fórmula para Cálculo**
   - Localização: Após definir a forma de cálculo, clique no botão "Adicionar Fórmula".
   - Como fazer: Insira as variáveis e operadores necessários para a fórmula.
   - Campos/Opções disponíveis:
     * `Variáveis`: Ex: "Remuneração", "Dias Trabalhados"
     * `Operadores`: Ex: "+", "-", "*", "/"
   - Resultado esperado: O sistema criará uma fórmula que calculará a remuneração com base nas variáveis e operadores inseridos.

5. **Definir Salário do Colaborador**
   - Localização: Na tela de configuração, ao definir a fórmula.
   - Como fazer: Certifique-se de que o salário do colaborador está definido como "Diarista".
   - Observações importantes: O salário deve estar previamente cadastrado no sistema para que o cálculo funcione corretamente.
   - Resultado esperado: O sistema utilizará o salário do colaborador e a quantidade de dias trabalhados para calcular a remuneração.

**Campos e Parâmetros:**

| Campo                  | Tipo         | Obrigatório | Descrição                                                                 | Exemplo               |
|------------------------|--------------|-------------|---------------------------------------------------------------------------|-----------------------|
| Tipo de Cálculo        | Dropdown     | Sim         | Seleciona entre "Manual" ou "Automático".                                | "Automático"          |
| Forma de Cálculo       | Dropdown     | Sim         | Seleciona entre "Faixa Condicional" ou "Simples Direta".                | "Simples Direta"      |
| Condição               | Texto        | Não         | Define a condição para a faixa condicional.                              | "Mais de 10 dias"     |
| Variáveis              | Texto        | Sim         | Tipos de informação a serem utilizadas no cálculo.                       | "Remuneração"         |
| Operadores             | Dropdown     | Sim         | Operadores matemáticos a serem utilizados na fórmula.                   | "+"                   |

**Regras de Negócio:**
- O cálculo manual requer que o usuário insira todos os valores manualmente.
- O cálculo automático pode ser feito através de condições e fórmulas.
- A "Faixa Condicional" deve ter uma condição definida para ser aplicada.
- O salário do colaborador deve estar configurado como "Diarista" para que o cálculo funcione corretamente.

**Observações Importantes:**
- Certifique-se de que todas as variáveis necessárias estão definidas antes de adicionar a fórmula.
- Evite deixar campos obrigatórios em branco, pois isso pode causar erros no cálculo.
- Verifique se o colaborador está corretamente cadastrado no sistema.

**Conceitos-Chave:**
- **Cálculo Manual**: Método onde o usuário insere todos os valores manualmente.
- **Cálculo Automático**: Método que utiliza variáveis e condições para calcular automaticamente a remuneração.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                        | Causa Provável                       | Solução                                               | Prevenção                                           |
|---------------------------------|--------------------------------------|-------------------------------------------------------|----------------------------------------------------|
| Cálculo não aparece             | Tipo de cálculo não selecionado      | Verifique se o tipo de cálculo foi definido corretamente. | Sempre selecione um tipo de cálculo antes de prosseguir. |
| Erro na fórmula                 | Variáveis ou operadores incorretos   | Revise a fórmula e ajuste as variáveis e operadores. | Teste a fórmula em um ambiente de simulação antes de aplicar. |
| Salário não reconhecido         | Salário do colaborador não definido  | Acesse o cadastro do colaborador e defina o salário. | Mantenha os dados dos colaboradores sempre atualizados. |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre teste as fórmulas em um ambiente de teste antes de aplicá-las na folha de pagamento real.
- Utilize comentários nas fórmulas para lembrar o propósito de cada variável.
- Mantenha um registro das condições utilizadas para facilitar futuras configurações.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Cálculo Simples Direto**
```
Situação: Um diarista com remuneração de R$ 150,00 por dia.
Ação: Configurar o cálculo como "Simples Direta" e multiplicar pela quantidade de dias trabalhados.
  • Campo Remuneração: "150"
  • Campo Dias Trabalhados: "5"
Resultado: O cálculo resultará em R$ 750,00 (150 * 5).
```

**Exemplo 2: Cálculo com Faixa Condicional**
```
Situação: Um diarista que deve receber um bônus se trabalhar mais de 10 dias.
Ação: Configurar o cálculo como "Faixa Condicional" e adicionar a condição "Mais de 10 dias".
  • Campo Condição: "Mais de 10 dias"
  • Campo Remuneração: "150"
  • Campo Dias Trabalhados: "12"
Resultado: O cálculo aplicará a condição e resultará em R$ 1.800,00 (150 * 12) se a condição for atendida.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O colaborador deve estar cadastrado e ter um salário definido como "Diarista".
- **Habilita:** A configuração correta do cálculo de remuneração permite a geração precisa da folha de pagamento.
- **Relacionado a:** Módulo de Controle de Ponto, onde os dias trabalhados são registrados.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como calcular a remuneração de diaristas?"
- **Com problema:** "Não consigo configurar o cálculo automático, o que fazer?"
- **Informal:** "Como faço pra calcular quanto um diarista vai ganhar?"
- **Por sintoma:** "Quando o cálculo não aparece, o que está errado?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Cálculo de salário", "Remuneração de diaristas", "Configuração de pagamento", "Cálculo de folha".

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como configurar o cálculo de remuneração para diaristas?
- Quais são as diferenças entre cálculo manual e automático?
- O que fazer se o salário do colaborador não for reconhecido?
- O que fazer se a fórmula não estiver funcionando?
- O que preciso ter configurado antes de calcular a remuneração?

---


---


---

## 12. Configuração de Rúbricas e Tipos de Folha de Pagamento

**📋 METADADOS:**
- **ID:** sec_12
- **⏱️ Minutagem:** 27:43 → 30:15
- **⏲️ Duração:** 151s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/0SpGZ3et0qs?si=o_T6kuqnOGErZtoO&t=1663)
- **📦 Módulo:** Folha de Pagamento
- **🏷️ Categorias:** Configuração, Cadastro, Folha de Pagamento, Rúbricas
- **🔑 Palavras-chave:** rúbricas, folha de pagamento, INSS, FGTS, condições salariais, tipos de folha

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como configurar rúbricas e tipos de folha de pagamento no sistema, permitindo a personalização de cálculos e a definição de eventos que interferem nas folhas geradas.

**Contexto:**
Estamos na seção de configurações do módulo de Folha de Pagamento, onde o usuário pode definir as rúbricas que influenciam os cálculos de salários e os tipos de folha que serão utilizados para diferentes situações, como rescisões e férias.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Folha de Pagamento > Configurações
- Tela/interface específica: Tela de Configuração de Rúbricas e Tipos de Folha

**Funcionalidade Detalhada:**
A funcionalidade permite ao usuário cadastrar e editar rúbricas que representam valores a serem calculados nas folhas de pagamento, como INSS e FGTS. O sistema possibilita a definição de condições salariais que influenciam a porcentagem aplicada a cada faixa salarial. Além disso, é possível cadastrar diferentes tipos de folha de pagamento, como folha de rescisão e folha de férias, personalizando quais itens e eventos estarão disponíveis em cada tipo.

### 🔹 Passo a Passo Detalhado:

1. **Cadastro de Rúbricas**
   - Localização: Tela de Configuração de Rúbricas
   - Como fazer: Selecione entre as opções de "Valor" ou "Variável". Para "Valor", insira referências como NSS ou FGTS. Para "Variável", escolha itens como "dias trabalhados" e clique em **Salvar**.
   - Campos/Opções disponíveis:
     * `Tipo`: Seleção entre "Valor" e "Variável"
     * `Item`: Seleção de "dias trabalhados" ou outros itens relevantes
   - Resultado esperado: O item será cadastrado e estará disponível para uso nas folhas de pagamento.

2. **Edição de Rúbricas (Exemplo: INSS)**
   - Localização: Tela de Configuração de Rúbricas
   - Como fazer: Clique em **Editar** ao lado da rúbrica INSS. Defina as condições salariais e as porcentagens correspondentes.
   - Observações importantes: As condições devem ser definidas de forma clara, como "salário menor ou igual a 1302" para aplicar 7,5% e "salário entre 1302 e 2571" para aplicar 9%.
   - Resultado esperado: As condições e porcentagens serão salvas e aplicadas corretamente nas folhas de pagamento.

3. **Cadastro de Tipos de Folha de Pagamento**
   - Localização: Tela de Configuração de Tipos de Folha
   - Como fazer: Clique em **Adicionar Tipo**. Insira o nome da folha (ex: "Folha de Rescisão") e selecione os itens que devem aparecer nesta folha.
   - Campos/Opções disponíveis:
     * `Nome da Folha`: Campo de texto para inserir o nome
     * `Itens Selecionados`: Lista de rúbricas disponíveis para seleção
   - Resultado esperado: O novo tipo de folha será cadastrado e estará disponível para uso.

4. **Definição de Eventos**
   - Localização: Tela de Configuração de Tipos de Folha
   - Como fazer: Durante o cadastro do tipo de folha, selecione quais eventos interferirão na folha. Os eventos são itens independentes que podem ser adicionados ou removidos conforme necessário.
   - Observações importantes: Certifique-se de que os eventos selecionados são relevantes para o tipo de folha que está sendo configurado.
   - Resultado esperado: Os eventos selecionados serão aplicados ao tipo de folha, influenciando os cálculos.

**Campos e Parâmetros:**

| Campo                  | Tipo         | Obrigatório | Descrição                                      | Exemplo                     |
|------------------------|--------------|-------------|------------------------------------------------|-----------------------------|
| `Tipo`                 | Dropdown     | Sim         | Seleção entre "Valor" e "Variável"            | "Valor"                     |
| `Item`                 | Dropdown     | Sim         | Seleção de itens como "dias trabalhados"      | "Dias Trabalhados"          |
| `Nome da Folha`       | Texto        | Sim         | Nome que identifica o tipo de folha            | "Folha de Rescisão"        |
| `Itens Selecionados`   | Lista        | Sim         | Rúbricas que aparecerão na folha               | "INSS, FGTS"                |

**Regras de Negócio:**
- As rúbricas devem ser cadastradas antes de serem utilizadas nas folhas de pagamento.
- As condições salariais devem ser definidas de forma não sobreposta para evitar conflitos nos cálculos.
- Cada tipo de folha deve ter pelo menos um item selecionado.

**Observações Importantes:**
- Ao cadastrar rúbricas, verifique se as condições estão corretas para evitar cálculos errôneos.
- Evite deixar campos obrigatórios em branco, pois isso pode causar falhas na geração da folha.
- Sempre revise as porcentagens aplicadas nas faixas salariais.

**Conceitos-Chave:**
- **Rúbrica**: Item que representa um valor a ser calculado na folha de pagamento.
- **Faixa Condicional**: Condição que determina a porcentagem aplicada com base no salário.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                     | Solução                                             | Prevenção                                         |
|-----------------------------------|------------------------------------|----------------------------------------------------|--------------------------------------------------|
| Cálculo incorreto de INSS         | Condições salariais mal definidas  | Revise as condições e porcentagens na rúbrica INSS | Teste as condições antes de salvar                |
| Tipo de folha não aparece         | Nenhum item selecionado            | Adicione pelo menos um item ao tipo de folha      | Sempre selecione itens relevantes ao criar tipos  |
| Erro ao salvar rúbrica            | Campos obrigatórios não preenchidos | Preencha todos os campos obrigatórios              | Verifique os campos antes de tentar salvar        |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre teste as configurações em um ambiente de desenvolvimento antes de aplicar em produção.
- Utilize nomes descritivos para as rúbricas e tipos de folha para facilitar a identificação.
- Mantenha um registro das alterações feitas nas configurações para auditoria futura.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Cadastrando uma Rúbrica de INSS**
```
Situação: Cadastro de uma rúbrica para o INSS.
Ação: 
  • Tipo: "Valor"
  • Item: "Dias Trabalhados"
Resultado: A rúbrica de INSS é cadastrada e estará disponível para cálculo na folha de pagamento.
```

**Exemplo 2: Criando uma Folha de Rescisão**
```
Situação: Criação de uma nova folha de rescisão.
Ação: 
  • Nome da Folha: "Folha de Rescisão"
  • Itens Selecionados: "INSS, FGTS"
Resultado: A folha de rescisão é criada com os itens selecionados e pronta para uso.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** As rúbricas devem ser configuradas antes de criar tipos de folha.
- **Habilita:** A criação de folhas de pagamento personalizadas com base nas configurações realizadas.
- **Relacionado a:** Módulo de Cálculo de Folha, onde as rúbricas e tipos de folha são utilizados para gerar os pagamentos.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como cadastrar uma rúbrica?"
- **Com problema:** "O que fazer se o cálculo do INSS estiver errado?"
- **Informal:** "Como eu coloco o INSS na folha?"
- **Por sintoma:** "Por que minha folha de rescisão não aparece?"
- **Com dúvida:** "Como definir as condições salariais?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Cadastrar rúbrica", "Adicionar rúbrica", "Configurar folha", "Criar tipo de folha"
- "Faixa salarial", "Condição de cálculo", "Evento de folha"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como cadastrar uma rúbrica para o INSS?
- O que fazer se o cálculo do INSS estiver errado?
- Como criar um tipo de folha de rescisão?
- O que fazer se a folha de pagamento não aparece?
- O que preciso ter configurado antes de criar uma folha de pagamento?

---


---


---

## 13. Configuração da Folha de Pagamento e Inclusão de Colaboradores

**📋 METADADOS:**
- **ID:** sec_13
- **⏱️ Minutagem:** 30:13 → 32:47
- **⏲️ Duração:** 154s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/0SpGZ3et0qs?si=o_T6kuqnOGErZtoO&t=1813)
- **📦 Módulo:** Folha de Pagamento
- **🏷️ Categorias:** Configuração, Cadastro, Eventos
- **🔑 Palavras-chave:** folha de pagamento, colaborador, adiantamento de salário, eventos, INSS, FGTS

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha o processo de configuração da folha de pagamento, incluindo a inclusão de colaboradores e a definição de itens que influenciam a folha. O objetivo é garantir que todos os colaboradores estejam corretamente vinculados à folha para a geração precisa de eventos e pagamentos.

**Contexto:**
Estamos na fase de configuração da folha de pagamento dentro do sistema, onde é necessário vincular colaboradores a uma folha específica e definir quais itens de remuneração e descontos serão aplicados a cada um deles.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Folha de Pagamento > Submenu Configuração de Folha
- Tela/interface específica: Tela de Configuração da Folha de Pagamento

**Funcionalidade Detalhada:**
A funcionalidade permite que o usuário configure a folha de pagamento, definindo quais itens (como INSS, FGTS, adiantamento de salário) influenciarão a remuneração dos colaboradores. É essencial que cada colaborador esteja vinculado à folha de pagamento para que os eventos possam ser gerados corretamente.

### 🔹 Passo a Passo Detalhado:

1. **Selecionar Itens da Folha de Pagamento**
   - Localização: Tela de Configuração da Folha de Pagamento
   - Como fazer: Na seção de itens da folha, selecione os itens que deseja incluir, como `INSS`, `FGTS`, e `adiantamento de salário`.
   - Campos/Opções disponíveis:
     * `INSS`: Contribuição previdenciária
     * `FGTS`: Fundo de Garantia do Tempo de Serviço
     * `Adiantamento de Salário`: Pagamento antecipado de parte do salário
   - Resultado esperado: Os itens selecionados são salvos e estarão disponíveis para a folha de pagamento.

2. **Incluir Colaborador na Folha de Pagamento**
   - Localização: Abaixo da lista de itens da folha na mesma tela
   - Como fazer: Clique no botão **Incluir Colaborador**. Selecione o colaborador desejado na lista de colaboradores disponíveis.
   - Observações importantes: É necessário que o colaborador esteja previamente cadastrado no sistema.
   - Resultado esperado: O colaborador é vinculado à folha de pagamento, permitindo que sua remuneração seja calculada.

3. **Definir Itens Específicos para o Colaborador**
   - Localização: Após selecionar o colaborador, uma nova seção aparecerá para definir os itens.
   - Como fazer: Na seção de itens do colaborador, selecione quais itens da folha geral serão aplicáveis a ele. Você pode desmarcar itens que não deseja incluir.
   - Resultado esperado: Apenas os itens selecionados aparecerão na folha de pagamento do colaborador.

4. **Associar Colaborador à Folha**
   - Localização: Após definir os itens, clique no botão **Associar**.
   - Como fazer: Clique em **Associar** para finalizar a vinculação do colaborador à folha de pagamento.
   - Resultado esperado: O colaborador está agora associado à folha de pagamento e pronto para que eventos sejam gerados.

5. **Gerar Eventos de Pagamento**
   - Localização: Menu de Eventos dentro do módulo de Folha de Pagamento
   - Como fazer: Inicie o processo de lançamento de um evento, como um adiantamento de salário. Clique em **Novo Evento** e preencha a descrição, tipo de evento, data e valor.
   - Campos/Opções disponíveis:
     * `Descrição`: Texto livre para descrever o evento (ex: "Adiantamento de Salário")
     * `Tipo`: Selecionar entre as opções disponíveis (ex: "Adiantamento de Salário")
     * `Data de Pagamento`: Data em que o pagamento será realizado
   - Resultado esperado: O evento é criado e, se vinculado à folha, será descontado ou adicionado ao valor total da folha de pagamento.

**Campos e Parâmetros:**

| Campo                     | Tipo        | Obrigatório | Descrição                                           | Exemplo                     |
|---------------------------|-------------|-------------|-----------------------------------------------------|-----------------------------|
| `Colaborador`             | Dropdown    | Sim         | Seleção do colaborador a ser vinculado à folha     | João Silva                  |
| `Item da Folha`          | Checkbox    | Sim         | Itens que influenciam a folha de pagamento          | INSS, FGTS, Adiantamento    |
| `Descrição do Evento`     | Texto livre | Sim         | Descrição do evento a ser lançado                   | Adiantamento de Salário      |
| `Tipo de Evento`          | Dropdown    | Sim         | Tipo de evento a ser registrado                      | Adiantamento de Salário      |
| `Data de Pagamento`       | Data        | Sim         | Data em que o pagamento do evento será realizado    | 01/10/2023                  |
| `Valor`                   | Numérico    | Sim         | Valor do evento a ser adicionado ou descontado      | 500,00                      |

**Regras de Negócio:**
- O colaborador deve estar vinculado à folha de pagamento para que eventos possam ser gerados.
- Itens da folha podem ser adicionados ou removidos para cada colaborador individualmente.
- Eventos de adiantamento de salário devem ser lançados antes da geração da folha de pagamento.

**Observações Importantes:**
- Certifique-se de que todos os colaboradores estejam cadastrados antes de tentar vinculá-los à folha.
- Evite desmarcar itens essenciais que possam impactar a remuneração do colaborador.

**Conceitos-Chave:**
- **Folha de Pagamento**: Documento que compila os valores a serem pagos aos colaboradores, incluindo salários, descontos e benefícios.
- **Evento**: Registro de um pagamento ou desconto que pode influenciar a folha de pagamento.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                             | Causa Provável                     | Solução                                           | Prevenção                                   |
|--------------------------------------|------------------------------------|--------------------------------------------------|---------------------------------------------|
| Colaborador não aparece na lista     | Não cadastrado no sistema          | Cadastrar o colaborador em Menu Principal > Colaboradores | Verificar cadastro antes de vincular       |
| Itens não aparecem na folha          | Não foram salvos corretamente      | Revisar a configuração da folha e salvar novamente | Confirmar seleção antes de salvar          |
| Evento não é descontado na folha     | Não vinculado à folha              | Associar o evento à folha de pagamento correta    | Verificar vínculos antes de gerar a folha  |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre revise os itens da folha antes de associar colaboradores.
- Utilize descrições claras para eventos para facilitar a identificação futura.
- Mantenha um registro de adiantamentos e comissões para evitar confusões.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Inclusão de Colaborador**
```
Situação: Um novo colaborador foi contratado e precisa ser adicionado à folha de pagamento.
Ação: 
  • Campo Colaborador: "Maria Oliveira"
  • Itens da Folha: Selecionar "INSS", "FGTS", "Adiantamento de Salário"
Resultado: Maria Oliveira é vinculada à folha de pagamento com os itens selecionados.
```

**Exemplo 2: Lançamento de Evento**
```
Situação: O colaborador João Silva solicitou um adiantamento de salário.
Ação: 
  • Campo Descrição: "Adiantamento de Salário"
  • Tipo de Evento: "Adiantamento de Salário"
  • Data de Pagamento: "15/10/2023"
  • Valor: "300,00"
Resultado: O evento é registrado e será descontado na próxima folha de pagamento.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O colaborador deve estar cadastrado no sistema antes de ser vinculado à folha.
- **Habilita:** A geração de eventos e a correta apuração da folha de pagamento.
- **Relacionado a:** Módulo de Eventos e Relatórios de Folha de Pagamento.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como vincular um colaborador à folha de pagamento?"
- **Com problema:** "Não consigo adicionar um colaborador à folha, o que fazer?"
- **Informal:** "Como coloco um funcionário na folha?"
- **Por sintoma:** "O que fazer se o colaborador não aparecer na folha?"
- **Com variação:** "Como configurar a folha de pagamento para um novo colaborador?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Adicionar colaborador", "Incluir funcionário", "Vincular colaborador", "Associar colaborador"
- "Folha de pagamento", "Remuneração", "Folha salarial"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como configurar a folha de pagamento para um colaborador?
- O que fazer se um colaborador não aparecer na lista de inclusão?
- Como lançar um evento de adiantamento de salário?
- O que fazer se o evento não for descontado na folha?
- O que preciso ter feito antes de vincular um colaborador à folha de pagamento?

---


---


---

## 14. Lançamento de Adiantamento de Salário

**📋 METADADOS:**
- **ID:** sec_14
- **⏱️ Minutagem:** 32:45 → 35:18
- **⏲️ Duração:** 153s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/0SpGZ3et0qs?si=o_T6kuqnOGErZtoO&t=1965)
- **📦 Módulo:** Financeiro
- **🏷️ Categorias:** Adiantamento, Folha de Pagamento, Relatório Financeiro
- **🔑 Palavras-chave:** adiantamento, salário, colaborador, contas a pagar, fluxo de caixa

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como registrar adiantamentos de salário para colaboradores, detalhando o processo de lançamento, a importância da classificação financeira e como replicar lançamentos frequentes.

**Contexto:**
Estamos na funcionalidade de lançamento de adiantamento de salário dentro do módulo financeiro do sistema. O objetivo é registrar adiantamentos que serão descontados na folha de pagamento, garantindo que as informações financeiras sejam corretamente classificadas e geridas.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Financeiro > Adiantamento de Salário
- Tela/interface específica: Tela de Lançamento de Adiantamento de Salário

**Funcionalidade Detalhada:**
A funcionalidade de lançamento de adiantamento de salário permite que o usuário registre valores que serão adiantados a colaboradores. Esses adiantamentos não são lançados diretamente nas contas a pagar, mas sim vinculados à folha de pagamento do mês e ano correspondente. A correta classificação dos lançamentos é crucial para evitar que valores sejam categorizados como despesas não identificadas.

### 🔹 Passo a Passo Detalhado:

1. **Preencher a Data de Pagamento**
   - Localização: Campo de data na tela de lançamento
   - Como fazer: Clique no campo de data e selecione a data de vencimento do adiantamento.
   - Campos/Opções disponíveis:
     * `Data de Pagamento`: Campo do tipo data, obrigatório.
   - Resultado esperado: A data de pagamento é registrada e será utilizada para o lançamento financeiro.

2. **Classificação do Fluxo de Caixa**
   - Localização: Campo de classificação abaixo da data de pagamento
   - Como fazer: Selecione a classificação apropriada para o fluxo de caixa no dropdown.
   - Observações importantes: É essencial escolher uma classificação correta; caso contrário, o lançamento será categorizado como despesa não identificada.
   - Resultado esperado: A classificação é salva e associada ao lançamento.

3. **Adicionar Colaboradores**
   - Localização: Seção de colaboradores na tela
   - Como fazer: Clique no botão para adicionar colaboradores e selecione os colaboradores desejados na lista.
   - Resultado esperado: Os colaboradores selecionados são adicionados ao lançamento de adiantamento.

4. **Preencher os Valores de Adiantamento**
   - Localização: Campos de valor ao lado de cada colaborador
   - Como fazer: Insira os valores a serem adiantados para cada colaborador. Por exemplo, para um colaborador, insira `350`, para outro `400`, e para um terceiro `500`.
   - Resultado esperado: Os valores são registrados e associados aos respectivos colaboradores.

5. **Salvar o Lançamento**
   - Localização: Botão **Salvar** na parte inferior da tela
   - Como fazer: Clique no botão **Salvar** para finalizar o lançamento.
   - Resultado esperado: O evento de adiantamento de salário é registrado no sistema.

6. **Replicar Lançamentos**
   - Localização: Botão **Replicar** na tela inicial de lançamentos
   - Como fazer: Clique em **Replicar** para criar um novo lançamento baseado em um anterior.
   - Observações importantes: O sistema puxará automaticamente os colaboradores, tipo e valores do lançamento anterior, permitindo que você modifique apenas os dados que mudam.
   - Resultado esperado: Um novo lançamento é criado com base no anterior, facilitando o processo.

**Campos e Parâmetros:**

| Campo                    | Tipo   | Obrigatório | Descrição                                               | Exemplo           |
|--------------------------|--------|-------------|---------------------------------------------------------|-------------------|
| `Data de Pagamento`      | Data   | Sim         | Data em que o adiantamento será pago.                  | 15/11/2023        |
| `Classificação`          | Dropdown | Sim       | Classificação financeira do adiantamento.               | Adiantamento Salário |
| `Colaborador`            | Lista  | Sim         | Nome do colaborador que receberá o adiantamento.       | João Silva        |
| `Valor do Adiantamento`  | Numérico | Sim       | Valor a ser adiantado ao colaborador.                  | 350               |

**Regras de Negócio:**
- Todos os lançamentos devem ter uma classificação financeira para evitar categorização como despesa não identificada.
- É permitido lançar adiantamentos para múltiplos colaboradores simultaneamente.
- O valor do adiantamento deve ser um número positivo.

**Observações Importantes:**
- Sempre verifique a classificação antes de salvar o lançamento.
- Evite deixar campos obrigatórios em branco, pois isso pode causar erros no registro.
- A replicação é uma funcionalidade útil para lançamentos recorrentes.

**Conceitos-Chave:**
- **Adiantamento de Salário**: Valor antecipado ao colaborador que será descontado na folha de pagamento.
- **Classificação Financeira**: Categorização necessária para o correto registro contábil.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                       | Causa Provável                     | Solução                                           | Prevenção                                   |
|--------------------------------|------------------------------------|--------------------------------------------------|---------------------------------------------|
| Campo de classificação não aparece | Falta de permissões de usuário    | Verifique as permissões em Admin > Usuários      | Configure permissões antes de tentar lançar |
| Erro ao salvar o lançamento    | Campos obrigatórios não preenchidos | Preencha todos os campos obrigatórios            | Revise os campos antes de salvar            |
| Valor do adiantamento negativo  | Inserção incorreta pelo usuário    | Corrija o valor para um número positivo          | Use validações de entrada                   |

**💡 DICAS E BOAS PRÁTICAS:**
- Utilize a funcionalidade de replicação para lançamentos frequentes, economizando tempo.
- Sempre revise os lançamentos antes de salvar para evitar erros.
- Mantenha um registro de adiantamentos para controle financeiro.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Lançamento de Adiantamento para um Colaborador**
```
Situação: João Silva precisa de um adiantamento.
Ação: 
  • Campo Data de Pagamento: "15/11/2023"
  • Campo Classificação: "Adiantamento Salário"
  • Colaborador: "João Silva"
  • Valor do Adiantamento: "350"
Resultado: O adiantamento de R$350 é registrado para João Silva.
```

**Exemplo 2: Lançamento de Adiantamento para Vários Colaboradores**
```
Situação: Três colaboradores precisam de adiantamentos.
Ação: 
  • Campo Data de Pagamento: "15/11/2023"
  • Campo Classificação: "Adiantamento Salário"
  • Colaboradores: "João Silva", "Maria Oliveira", "Carlos Souza"
  • Valores: "350", "400", "500"
Resultado: Os adiantamentos são registrados para os três colaboradores.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O usuário deve ter permissões adequadas para registrar adiantamentos.
- **Habilita:** O registro de adiantamentos permite a geração correta da folha de pagamento.
- **Relacionado a:** Folha de Pagamento, Contas a Pagar.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como lançar um adiantamento de salário?"
- **Com problema:** "Não consigo registrar um adiantamento, o que fazer?"
- **Informal:** "Como faço pra adiantar o salário do funcionário?"
- **Por sintoma:** "Quando o valor não é aceito, como resolver?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Registrar adiantamento", "Adicionar adiantamento", "Lançar adiantamento", "Criar adiantamento"
- "Colaborador" pode ser referido como "Funcionário", "Empregado".

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como lançar um adiantamento de salário?
- O que fazer se o campo de classificação não aparecer?
- Como replicar um lançamento de adiantamento?
- O que fazer se o valor do adiantamento não for aceito?
- Quais são os pré-requisitos para registrar um adiantamento de salário? 

---


---


---

## 15. Geração de Folhas de Pagamento

**📋 METADADOS:**
- **ID:** sec_15
- **⏱️ Minutagem:** 35:15 → 37:46
- **⏲️ Duração:** 150s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/0SpGZ3et0qs?si=o_T6kuqnOGErZtoO&t=2115)
- **📦 Módulo:** Folha de Pagamento
- **🏷️ Categorias:** Geração, Relatório, Colaboradores, Configuração
- **🔑 Palavras-chave:** folha normal, folha complementar, colaboradores, gerar, pagamento, configuração

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como gerar folhas de pagamento, diferenciando entre folhas normais e complementares, e aborda a configuração necessária para que todos os colaboradores sejam incluídos corretamente.

**Contexto:**
Estamos na interface de geração de folhas de pagamento, onde o usuário pode criar novas folhas para colaboradores, definindo períodos e tipos de folha. O objetivo é garantir que todos os colaboradores estejam corretamente configurados para aparecer nas folhas geradas.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Folha de Pagamento > Geração de Folhas
- Tela/interface específica: Tela de Geração de Folhas de Pagamento

**Funcionalidade Detalhada:**
A funcionalidade de geração de folhas de pagamento permite ao usuário criar folhas para colaboradores, escolhendo entre dois tipos: **folha normal** e **folha complementar**. A folha normal puxa dados de todo o mês, enquanto a folha complementar permite definir um período específico, como de um dia a outro. O usuário pode optar por gerar a folha para todos os colaboradores ou apenas para alguns específicos, dependendo da configuração de cada colaborador.

### 🔹 Passo a Passo Detalhado:

1. **Selecionar Tipo de Folha**
   - Localização: Botão **Mais Folhas** na tela de geração de folhas.
   - Como fazer: Clique no botão **Mais Folhas** para abrir as opções de tipos de folha.
   - Campos/Opções disponíveis:
     * `Folha Normal`: Gera uma folha com referência do mês inteiro.
     * `Folha Complementar`: Permite definir um período inicial e final.
   - Resultado esperado: O sistema apresenta as opções de folha para seleção.

2. **Definir Período para Folha Complementar**
   - Localização: Campos de data na seção de folha complementar.
   - Como fazer: Se optar por folha complementar, insira a data inicial e final desejadas (ex: de 01/01/2024 a 10/01/2024).
   - Observações importantes: A folha normal não requer definição de período.
   - Resultado esperado: O sistema aceita as datas e prepara a geração da folha.

3. **Selecionar Colaboradores**
   - Localização: Opção de seleção de colaboradores na tela de geração.
   - Como fazer: Escolha entre **Todos os Colaboradores** ou selecione colaboradores específicos.
   - Resultado esperado: O sistema ajusta a lista de colaboradores que serão incluídos na folha.

4. **Gerar Folha**
   - Localização: Botão **Gerar** na parte inferior da tela.
   - Como fazer: Após definir todos os parâmetros, clique no botão **Gerar** para criar a folha de pagamento.
   - Resultado esperado: O sistema processa a geração da folha e apresenta um informativo total com dados como adiantamento, bônus e FGTS.

5. **Verificar Colaboradores Não Incluídos**
   - Localização: Informativo que aparece após a geração da folha.
   - Como fazer: Após a geração, verifique a lista de colaboradores que não foram incluídos e os motivos.
   - Observações importantes: Motivos podem incluir falta de alocação, salário ou associação à folha de pagamento.
   - Resultado esperado: O sistema lista os colaboradores ausentes e os motivos, permitindo ajustes necessários.

6. **Adicionar Colaborador Individualmente**
   - Localização: Botão **Mais Colaborador** na tela da folha gerada.
   - Como fazer: Clique em **Mais Colaborador** para adicionar colaboradores que não foram incluídos.
   - Resultado esperado: O sistema permite a inclusão manual de colaboradores após ajustes nas configurações.

**Campos e Parâmetros:**

| Campo                   | Tipo      | Obrigatório | Descrição                                                                 | Exemplo                  |
|-------------------------|-----------|-------------|---------------------------------------------------------------------------|--------------------------|
| Tipo de Folha           | Dropdown  | Sim         | Seleciona entre folha normal ou complementar.                             | Folha Normal             |
| Data Inicial            | Data      | Condicional | Define o início do período para folhas complementares.                   | 01/01/2024               |
| Data Final              | Data      | Condicional | Define o fim do período para folhas complementares.                      | 10/01/2024               |
| Seleção de Colaboradores | Checkbox  | Sim         | Permite selecionar todos os colaboradores ou apenas alguns específicos.  | Todos                    |
| Botão Gerar             | Botão     | Sim         | Inicia o processo de geração da folha de pagamento.                      | [Gerar]                  |

**Regras de Negócio:**
- A folha normal gera dados para o mês inteiro, enquanto a complementar permite definir um intervalo de datas.
- Colaboradores não configurados corretamente não aparecerão na folha gerada, e o sistema indicará os motivos.
- É necessário ajustar as configurações dos colaboradores antes de gerar a folha para garantir que todos sejam incluídos.

**Observações Importantes:**
- Verifique se todos os colaboradores têm alocação e salário configurados para evitar problemas na geração da folha.
- Caso um colaborador não apareça, ajuste suas configurações e utilize a opção de adicionar colaborador individualmente.

**Conceitos-Chave:**
- **Folha Normal**: Folha que puxa dados de todo o mês.
- **Folha Complementar**: Folha que permite definir um período específico para geração.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                               | Causa Provável                       | Solução                                               | Prevenção                                         |
|----------------------------------------|-------------------------------------|------------------------------------------------------|---------------------------------------------------|
| Colaborador não aparece na folha       | Falta de alocação ou salário        | Ajustar as configurações do colaborador e regenerar. | Verificar configurações antes da geração.         |
| Erro ao gerar folha                    | Campos obrigatórios não preenchidos | Certifique-se de que todos os campos obrigatórios estão preenchidos. | Revisar todos os campos antes de clicar em gerar. |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre verifique as configurações dos colaboradores antes de gerar a folha.
- Utilize a folha complementar para períodos específicos quando necessário.
- Mantenha um registro das configurações de cada colaborador para facilitar a geração futura.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Geração de Folha Normal**
```
Situação: Gerar folha de pagamento para o mês de janeiro.
Ação: 
  • Tipo de Folha: "Folha Normal"
  • Seleção de Colaboradores: "Todos"
Resultado: Folha gerada com todos os colaboradores do mês de janeiro.
```

**Exemplo 2: Geração de Folha Complementar**
```
Situação: Gerar folha de pagamento para o período de 01 a 10 de janeiro.
Ação: 
  • Tipo de Folha: "Folha Complementar"
  • Data Inicial: "01/01/2024"
  • Data Final: "10/01/2024"
  • Seleção de Colaboradores: "Todos"
Resultado: Folha gerada apenas para o período especificado, com colaboradores que têm dados nesse intervalo.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** Configuração correta dos colaboradores, incluindo alocação e salário.
- **Habilita:** A geração de relatórios de pagamento e análise de dados financeiros.
- **Relacionado a:** Módulo de Cadastro de Colaboradores e Relatórios de Folha de Pagamento.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como gerar uma folha de pagamento?"
- **Com problema:** "Não consigo gerar a folha, o que fazer?"
- **Informal:** "Como faço pra criar a folha de pagamento?"
- **Por sintoma:** "Por que meu colaborador não aparece na folha?"
- **Com dúvida:** "Qual a diferença entre folha normal e complementar?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Criar folha", "Adicionar folha", "Nova folha", "Gerar folha de pagamento"
- "Folha mensal", "Folha quinzenal", "Folha semanal"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso gerar uma folha de pagamento normal?
- O que fazer se um colaborador não aparecer na folha gerada?
- Como definir um período específico para a folha complementar?
- O que fazer se a geração da folha falhar?
- Quais configurações preciso verificar antes de gerar a folha?

---


---


---

## 16. Configuração e Finalização da Folha de Pagamento

**📋 METADADOS:**
- **ID:** sec_16
- **⏱️ Minutagem:** 37:47 → 40:22
- **⏲️ Duração:** 155s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/0SpGZ3et0qs?si=o_T6kuqnOGErZtoO&t=2267)
- **📦 Módulo:** Folha de Pagamento
- **🏷️ Categorias:** Configuração, Relatório, Operacional
- **🔑 Palavras-chave:** folha de pagamento, INSS, FGTS, adiantamento de salário, olerite

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como configurar e finalizar a folha de pagamento de colaboradores, incluindo a visualização de totais, ajustes em itens manuais e a exportação de olerites. O objetivo é garantir que todos os cálculos e informações estejam corretos antes da finalização.

**Contexto:**
Estamos na interface de configuração da folha de pagamento, onde é possível visualizar e ajustar os totais relacionados aos colaboradores. O foco é garantir que todos os itens e descontos sejam corretamente configurados antes de finalizar a folha.

**Localização no Sistema:**
- Caminho de navegação: Menu Principal > Módulo Folha de Pagamento > Tela de Configuração da Folha
- Tela/interface específica: Tela de Detalhes da Folha de Pagamento

**Funcionalidade Detalhada:**
Esta funcionalidade permite que o usuário visualize e ajuste os totais da folha de pagamento, incluindo descontos automáticos como INSS e FGTS, além de itens manuais que precisam ser preenchidos manualmente. O usuário pode também finalizar a folha, o que a enviará para o módulo financeiro.

### 🔹 Passo a Passo Detalhado:

1. **Visualização dos Totais**
   - Localização: Tela de Detalhes da Folha de Pagamento
   - Como fazer: Ao acessar a tela, os totais relacionados às configurações da folha são exibidos automaticamente.
   - Campos/Opções disponíveis:
     * `INSS`: Cálculo automático de desconto.
     * `FGTS`: Configurado como neutro, não adiciona nem retira valores.
   - Resultado esperado: Visualização clara dos totais, com destaque para o que foi calculado automaticamente e o que requer intervenção manual.

2. **Configuração do FGTS**
   - Localização: Seção de Itens da Folha
   - Como fazer: O FGTS pode ser configurado como neutro, o que significa que ele aparecerá apenas como informativo.
   - Observações importantes: Itens neutros não impactam o total da folha.
   - Resultado esperado: O FGTS aparece na folha, mas não altera o total.

3. **Adiantamento de Salário**
   - Localização: Seção de Itens da Folha
   - Como fazer: O adiantamento de salário deve ser vinculado à folha de pagamento e configurado como um evento.
   - Campos/Opções disponíveis:
     * `Adiantamento`: Valor a ser descontado conforme eventos lançados.
   - Resultado esperado: O valor do adiantamento é descontado automaticamente da remuneração do colaborador.

4. **Configuração de Bônus**
   - Localização: Seção de Itens da Folha
   - Como fazer: O bônus é um item manual e deve ser preenchido manualmente na folha.
   - Observações importantes: Itens manuais não puxam vencimentos ou descontos automaticamente.
   - Resultado esperado: O bônus não aparece na folha até que seja inserido manualmente.

5. **Edição da Folha**
   - Localização: Tela de Detalhes da Folha de Pagamento
   - Como fazer: O usuário pode adicionar ou remover itens da folha e editar a forma de pagamento.
   - Campos/Opções disponíveis:
     * `Adicionar Item`: Botão para incluir novos itens.
     * `Remover Item`: Opção para excluir itens existentes.
   - Resultado esperado: A folha é atualizada com as modificações realizadas.

6. **Salvar Alterações**
   - Localização: Botão de Salvar na parte inferior da tela
   - Como fazer: Após realizar as modificações, clique no botão **Salvar**.
   - Resultado esperado: As alterações são salvas e refletidas na folha de pagamento.

7. **Finalização da Folha**
   - Localização: Tela de Detalhes da Folha de Pagamento
   - Como fazer: Preencher o vencimento e a classificação e clicar em **Salvar** para concluir a folha.
   - Observações importantes: A finalização da folha envia os dados para o contas a pagar no módulo financeiro.
   - Resultado esperado: A folha é concluída e os dados são enviados corretamente.

8. **Exportação de Olerites**
   - Localização: Tela de Detalhes da Folha de Pagamento
   - Como fazer: Após a finalização, clique na folha de um colaborador específico e acesse a opção de download.
   - Resultado esperado: O olerite é gerado e disponível para download, contendo duas guias: uma para o colaborador e outra para a empresa.

**Campos e Parâmetros:**

| Campo                  | Tipo          | Obrigatório | Descrição                                               | Exemplo                  |
|------------------------|---------------|-------------|--------------------------------------------------------|--------------------------|
| `INSS`                 | Desconto      | Sim         | Desconto automático calculado pela folha.              | R$ 200,00                |
| `FGTS`                 | Informativo   | Não         | Item neutro que não altera o total.                   | R$ 0,00                  |
| `Adiantamento`         | Evento        | Sim         | Valor a ser descontado da remuneração.                 | R$ 500,00                |
| `Bônus`                | Manual        | Não         | Item que deve ser preenchido manualmente.              | R$ 300,00                |
| `Vencimento`           | Data          | Sim         | Data de vencimento da folha.                            | 30/09/2023               |
| `Classificação`        | Texto         | Sim         | Classificação da folha para o contas a pagar.          | Folha de Setembro 2023   |

**Regras de Negócio:**
- O FGTS configurado como neutro não deve impactar o total da folha.
- Itens manuais, como bônus, precisam ser preenchidos manualmente para aparecer na folha.
- A finalização da folha deve ser feita após todos os ajustes e configurações.

**Observações Importantes:**
- Sempre verifique se todos os itens estão corretamente configurados antes de finalizar a folha.
- Evite deixar itens manuais sem preenchimento, pois isso pode gerar inconsistências nos relatórios.

**Conceitos-Chave:**
- **Item Neutro**: Um item que não altera o total da folha, servindo apenas como informativo.
- **Evento**: Um registro que impacta a folha de pagamento, como adiantamento de salário.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                     | Solução                                               | Prevenção                                         |
|-----------------------------------|------------------------------------|------------------------------------------------------|--------------------------------------------------|
| FGTS não aparece na folha         | Configuração como neutro           | Verificar a configuração do FGTS e alterar se necessário. | Revisar configurações antes de finalizar.        |
| Bônus não é calculado             | Item manual não preenchido         | Preencher manualmente o valor do bônus na folha.    | Sempre revisar itens manuais antes da finalização. |
| Olerite não é gerado              | Folha não finalizada               | Finalizar a folha e tentar novamente a exportação.   | Finalizar a folha antes de tentar exportar.      |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre revise os totais antes de finalizar a folha.
- Utilize a função de download para manter registros atualizados dos olerites.
- Mantenha uma lista de itens manuais para não esquecer de preenchê-los.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Configuração de Folha de Pagamento**
```
Situação: Um colaborador chamado João Silva precisa de sua folha de pagamento configurada.
Ação: 
  • Campo INSS: "R$ 200,00"
  • Campo FGTS: "Neutro"
  • Campo Adiantamento: "R$ 500,00"
Resultado: A folha de João é configurada corretamente, com o INSS calculado e o FGTS como informativo.
```

**Exemplo 2: Finalização da Folha**
```
Situação: A folha de pagamento de setembro precisa ser finalizada.
Ação: 
  • Preencher Vencimento: "30/09/2023"
  • Preencher Classificação: "Folha de Setembro 2023"
Resultado: A folha é finalizada e os dados são enviados para o contas a pagar.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** Todos os colaboradores devem estar configurados corretamente na folha.
- **Habilita:** A geração de relatórios financeiros e o pagamento dos colaboradores.
- **Relacionado a:** Módulo Financeiro, onde as folhas finalizadas são enviadas para contas a pagar.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como configurar a folha de pagamento?"
- **Com problema:** "Não consigo finalizar a folha, o que fazer?"
- **Informal:** "Como eu faço pra ajustar a folha do colaborador?"
- **Por sintoma:** "Quando o FGTS não aparece, o que eu devo verificar?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Configurar folha", "ajustar folha de pagamento", "finalizar folha", "exportar olerite"
- "Folha de pagamento", "relatório de pagamento", "documento de pagamento"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como visualizar os totais da folha de pagamento?
- O que fazer se o FGTS não aparecer na folha?
- Como adicionar um bônus manualmente na folha?
- O que fazer se o olerite não for gerado?
- O que preciso fazer antes de finalizar a folha de pagamento?

---


---


---

## 17. Configuração de Proventos e Descontos

**📋 METADADOS:**
- **ID:** sec_17
- **⏱️ Minutagem:** 40:18 → 40:37
- **⏲️ Duração:** 19s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/0SpGZ3et0qs?si=o_T6kuqnOGErZtoO&t=2418)
- **📦 Módulo:** Módulo RH
- **🏷️ Categorias:** Configuração, Lançamento, Proventos, Descontos
- **🔑 Palavras-chave:** provento, desconto, valor total líquido, assinatura, módulo RH

> **🔍 RESUMO EXECUTIVO:** Esta seção detalha como configurar proventos e descontos no sistema, permitindo que os usuários compreendam como calcular o valor total líquido e a importância da assinatura no processo.

**Contexto:**
Estamos no Módulo RH, onde as principais configurações e lançamentos relacionados a proventos e descontos são realizados. O objetivo é garantir que os usuários saibam como inserir e gerenciar essas informações corretamente.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo RH > Configurações de Proventos e Descontos
- Tela/interface específica: Tela de Configuração de Proventos e Descontos

**Funcionalidade Detalhada:**

A funcionalidade de configuração de proventos e descontos permite que os usuários insiram e gerenciem os valores que impactam o salário líquido dos colaboradores. Essa configuração é essencial para garantir que os cálculos de folha de pagamento sejam precisos e reflitam as deduções e adições corretas.

### 🔹 Passo a Passo Detalhado:

1. **Inserir Provento**
   - Localização: Tela de Configuração de Proventos e Descontos, seção "Proventos"
   - Como fazer: Clique no botão **Adicionar Provento** localizado na parte superior direita da tela.
   - Campos/Opções disponíveis:
     * `Nome do Provento`: Campo de texto onde você insere o nome do provento (ex: "Salário Base").
     * `Valor`: Campo numérico onde você insere o valor do provento (ex: "3000").
   - Resultado esperado: O provento é adicionado à lista de proventos, refletindo no cálculo do salário líquido.

2. **Inserir Desconto**
   - Localização: Tela de Configuração de Proventos e Descontos, seção "Descontos"
   - Como fazer: Clique no botão **Adicionar Desconto** localizado na parte superior direita da tela.
   - Observações importantes: Certifique-se de que o desconto não ultrapasse o valor total dos proventos para evitar erros no cálculo.
   - Resultado esperado: O desconto é adicionado à lista de descontos, reduzindo o valor total líquido.

3. **Visualizar Valor Total Líquido**
   - Localização: Tela de Configuração de Proventos e Descontos, seção "Resumo"
   - Como fazer: Após inserir proventos e descontos, o valor total líquido é automaticamente calculado e exibido na seção "Resumo".
   - Resultado esperado: O valor total líquido é atualizado em tempo real, refletindo as alterações feitas.

4. **Assinar Configurações**
   - Localização: Tela de Configuração de Proventos e Descontos, seção "Assinatura"
   - Como fazer: Clique no campo **Assinatura** e insira o nome do responsável pela configuração (ex: "Maria Oliveira").
   - Resultado esperado: A assinatura é registrada, confirmando a responsabilidade pela configuração realizada.

**Campos e Parâmetros:**

| Campo                  | Tipo      | Obrigatório | Descrição                                           | Exemplo               |
|------------------------|-----------|-------------|-----------------------------------------------------|-----------------------|
| Nome do Provento       | Texto     | Sim         | Nome do provento a ser adicionado                   | "Salário Base"        |
| Valor                  | Numérico  | Sim         | Valor monetário do provento                          | "3000"                |
| Nome do Desconto       | Texto     | Sim         | Nome do desconto a ser adicionado                   | "INSS"                |
| Valor do Desconto      | Numérico  | Sim         | Valor monetário do desconto                          | "300"                 |
| Assinatura             | Texto     | Sim         | Nome do responsável pela configuração                | "Maria Oliveira"      |

**Regras de Negócio:**
- O valor total líquido é calculado subtraindo todos os descontos dos proventos.
- A assinatura deve ser preenchida para validar as configurações realizadas.
- Não é permitido que o total de descontos ultrapasse o total de proventos.

**Observações Importantes:**
- Sempre revise os valores inseridos antes de salvar as configurações.
- Erros comuns incluem a inserção de valores negativos ou a falta de assinatura.
- As configurações devem ser feitas mensalmente, antes do fechamento da folha de pagamento.

**Conceitos-Chave:**
- **Provento**: Qualquer valor que aumenta o salário do colaborador, como bônus ou salário base.
- **Desconto**: Qualquer valor que diminui o salário do colaborador, como impostos ou contribuições.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                     | Solução                                       | Prevenção                                   |
|-----------------------------------|------------------------------------|-----------------------------------------------|---------------------------------------------|
| Valor total líquido não aparece    | Campos de proventos ou descontos vazios | Verifique se todos os campos obrigatórios estão preenchidos | Sempre preencher todos os campos necessários |
| Assinatura não salva               | Campo de assinatura vazio          | Preencha o campo de assinatura corretamente   | Lembrar de inserir a assinatura antes de salvar |
| Desconto maior que provento        | Erro de inserção de valores       | Ajuste o valor do desconto para ser menor que o total de proventos | Validar os valores antes de finalizar a configuração |

**💡 DICAS E BOAS PRÁTICAS:**
- Utilize valores reais e atualizados para evitar discrepâncias.
- Revise as configurações mensalmente para garantir que estão corretas.
- Utilize a funcionalidade de pré-visualização, se disponível, para verificar os cálculos.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Configuração de Salário Base**
```
Situação: Um colaborador recebe um salário base de R$ 3000.
Ação: 
  • Campo Nome do Provento: "Salário Base"
  • Campo Valor: "3000"
Resultado: O provento é adicionado e o valor total líquido é atualizado.
```

**Exemplo 2: Configuração de Desconto de INSS**
```
Situação: Um colaborador tem um desconto de INSS de R$ 300.
Ação: 
  • Campo Nome do Desconto: "INSS"
  • Campo Valor do Desconto: "300"
Resultado: O desconto é adicionado e o valor total líquido é recalculado.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O módulo RH deve estar ativo e configurado corretamente.
- **Habilita:** A geração da folha de pagamento e relatórios financeiros.
- **Relacionado a:** Funcionalidades de relatórios de folha de pagamento e gestão de colaboradores.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como configurar proventos e descontos?"
- **Com problema:** "Não consigo ver o valor total líquido, o que fazer?"
- **Informal:** "Como eu coloco os descontos no sistema?"
- **Por sintoma:** "Quando adiciono um desconto, o total não muda, por que?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Adicionar provento", "Cadastrar desconto", "Configurar salário", "Gerenciar proventos"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como inserir um provento no sistema?
- O que fazer se o valor total líquido não aparece?
- Como adicionar um desconto corretamente?
- O que fazer se o desconto é maior que o provento?
- O que preciso fazer antes de configurar proventos e descontos?

---


---




---


## 🎬 DADOS DE TIMESTAMPS (Para Sistema RAG)


[VIDEO_TIMESTAMPS_DATA]

{
  "Passo a passo - Módulo de RH": [
    {
      "start": "00:00",
      "end": "02:35",
      "line": "Olá, neste vídeo irei realizar um treinamento completo do módulo RH. Nosso primeiro passo será acess"
    },
    {
      "start": "02:32",
      "end": "05:04",
      "line": "final e adicionar outro. Em seguida, indicar se ele possui ou não o controle de ponto. Clicando em p"
    },
    {
      "start": "05:02",
      "end": "07:35",
      "line": "preencho a obra que já precisa estar cadastrada e novamente apenas a data inicial e salva. Se houver"
    },
    {
      "start": "07:33",
      "end": "10:07",
      "line": "dentro do colaborador na página de controle de ponto. Vindo um pouco abaixo, você tem a opção de reg"
    },
    {
      "start": "10:05",
      "end": "12:40",
      "line": "Então, depois de realizar o preenchimento, vou salvar o modelo de planilha já preenchido, como dito."
    },
    {
      "start": "12:37",
      "end": "15:12",
      "line": "trabalho. Agora, quando ele fica em laranja, quer dizer que houve alguma divergência, seja para hora"
    },
    {
      "start": "15:09",
      "end": "17:42",
      "line": "diretamente no seu controle de ponto. Lá no seu ponto é possível visualizar a nomenclatura de férias"
    },
    {
      "start": "17:39",
      "end": "20:13",
      "line": "costuma ser um mensalista, por exemplo. E o grupo de cargos? O grupo de cargos é bem semelhante ao q"
    },
    {
      "start": "20:10",
      "end": "22:44",
      "line": "também preciso preencher a cidade. Ao salvar, ele já estará registrado. Esse feriado só vai ser vinc"
    },
    {
      "start": "22:41",
      "end": "25:16",
      "line": "criar outras nomenclaturas, definições para isso, é só clicar em mais tipo e colocar o nome dele. Em"
    },
    {
      "start": "25:13",
      "end": "27:46",
      "line": "desconto e o neutro. Nesse caso será o vencimento, porque a remuneração é o valor adicionado na folh"
    },
    {
      "start": "27:43",
      "end": "30:15",
      "line": "do valor dentro das folhas de pagamento. Aqui há duas opções entre valor e variável. No caso de valo"
    },
    {
      "start": "30:13",
      "end": "32:47",
      "line": "precisa da folha de pagamento para ser gerado, mas você vai definir se ele vai influenciar ou não na"
    },
    {
      "start": "32:45",
      "end": "35:18",
      "line": "folha e se estiver vinculado a ela, ele desconta o valor. Agora, quando o item é um provento, podemo"
    },
    {
      "start": "35:15",
      "end": "37:46",
      "line": "já geradas. Para gerar uma nova, basta clicar em mais folhas. Aqui você terá duas opções, folha norm"
    },
    {
      "start": "37:47",
      "end": "40:22",
      "line": "vemos os totais em relação às configurações da folha dele e um pouco abaixo os itens. Neste meu demo"
    },
    {
      "start": "40:18",
      "end": "40:37",
      "line": "provento e um desconto. E aqui o valor total líquido, assim como um campo de assinatura. Em relação "
    }
  ]
}

[/VIDEO_TIMESTAMPS_DATA]
