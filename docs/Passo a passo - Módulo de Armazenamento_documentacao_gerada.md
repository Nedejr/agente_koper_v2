# 📚 Documentação: Passo a passo - Módulo de Armazenamento


[video:https://youtu.be/VC6EkQJoLEY?si=k9wjmlsuMeBR7kmV]


**🎥 Vídeo Original:** https://youtu.be/VC6EkQJoLEY?si=k9wjmlsuMeBR7kmV

**📊 Total de Seções:** 2

---

---

## 1. Funcionamento do Módulo Armazenamento

**📋 METADADOS:**
- **ID:** sec_1
- **⏱️ Minutagem:** 00:01 → 02:37
- **⏲️ Duração:** 156s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/VC6EkQJoLEY?si=k9wjmlsuMeBR7kmV&t=1)
- **📦 Módulo:** Armazenamento
- **🏷️ Categorias:** Configuração, Administração, Operacional
- **🔑 Palavras-chave:** armazenamento, usuário, permissões, pasta, editar

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como configurar o acesso ao módulo de armazenamento para diferentes usuários, incluindo a criação e gerenciamento de pastas, além de definir permissões de acesso.

**Contexto:**
Estamos no módulo de armazenamento de um sistema, onde o objetivo é gerenciar o acesso e as permissões dos usuários, além de organizar os dados em pastas.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Administração > Aba Usuários
- Tela/interface específica: Módulo Armazenamento

**Funcionalidade Detalhada:**
O módulo de armazenamento permite que os usuários organizem e gerenciem arquivos em pastas. A funcionalidade principal inclui a configuração de permissões de acesso para diferentes usuários, a criação de novas pastas, e a edição e exclusão de pastas existentes.

### 🔹 Passo a Passo Detalhado:

1. **Configurar Permissões de Usuário**
   - Localização: Menu Principal > Módulo Administração > Aba Usuários
   - Como fazer: Acesse o módulo de administração e clique na aba de usuários. Selecione o usuário que deseja alterar e clique em **Editar**.
   - Campos/Opções disponíveis:
     * `Módulo de Armazenamento`: Aqui você verá três opções:
       - **Sem autorização**: O usuário não terá acesso ao módulo.
       - **Apenas visualização**: O usuário poderá visualizar, mas não editar.
       - **Autorização total**: O usuário terá acesso completo ao módulo.
   - Resultado esperado: As permissões do usuário selecionado são atualizadas conforme a escolha feita.

2. **Acessar o Módulo de Armazenamento**
   - Localização: Menu Principal > Módulo Armazenamento
   - Como fazer: Clique no módulo de armazenamento para visualizar a tela inicial.
   - Resultado esperado: A tela inicial exibe o espaço total de armazenamento, o espaço já utilizado e as pastas criadas.

3. **Gerenciar Pastas Existentes**
   - Localização: Tela inicial do módulo de armazenamento
   - Como fazer: Clique nos três pontinhos ao lado da pasta desejada para abrir o menu de opções.
   - Observações importantes: As opções disponíveis incluem:
     - **Abrir**: Para visualizar as informações da pasta.
     - **Renomear**: Clique na opção, altere o nome da pasta e clique em **Salvar** para aplicar a mudança.
     - **Permissões**: Visualize e altere as permissões dos usuários que têm acesso à pasta.
     - **Excluir**: Para remover a pasta, selecione esta opção.
   - Resultado esperado: As ações realizadas nas pastas são aplicadas conforme as escolhas feitas.

4. **Criar Nova Pasta**
   - Localização: Tela inicial do módulo de armazenamento
   - Como fazer: Clique no botão **Nova Pasta**, insira o nome desejado e clique em **Criar**.
   - Resultado esperado: A nova pasta é criada e aparece na tela inicial.

5. **Visualizar Opções Dentro da Pasta**
   - Localização: Dentro da nova pasta criada
   - Como fazer: Clique nos três pontinhos ao lado da pasta para acessar mais opções.
   - Resultado esperado: Um menu com opções adicionais para gerenciar a pasta.

**Campos e Parâmetros:**

| Campo                     | Tipo    | Obrigatório | Descrição                                       | Exemplo               |
|---------------------------|---------|-------------|-------------------------------------------------|-----------------------|
| Módulo de Armazenamento   | Dropdown| Sim         | Define o nível de acesso do usuário ao módulo. | Autorização total     |
| Nome da Pasta             | Texto   | Sim         | Nome que será atribuído à nova pasta.          | Contratos_2024        |

**Regras de Negócio:**
- Apenas o usuário admin tem acesso total ao módulo de armazenamento por padrão.
- As permissões podem ser alteradas a qualquer momento por um usuário com acesso ao módulo de administração.
- A exclusão de pastas é permanente e não pode ser desfeita.

**Observações Importantes:**
- Sempre verifique as permissões antes de criar ou editar pastas.
- Evite renomear pastas com nomes já existentes para prevenir confusões.
- As alterações nas permissões são salvas imediatamente após clicar em **Salvar**.

**Conceitos-Chave:**
- **Permissões**: Controle de acesso que determina o que um usuário pode fazer dentro do módulo.
- **Pasta**: Estrutura de organização que permite armazenar arquivos de forma hierárquica.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                     | Solução                                      | Prevenção                               |
|-----------------------------------|------------------------------------|----------------------------------------------|-----------------------------------------|
| Usuário não consegue acessar o módulo | Permissões não configuradas corretamente | Acesse o módulo de administração e ajuste as permissões do usuário. | Verifique as permissões antes de salvar. |
| Pasta não aparece após criação    | Falha na criação da pasta          | Tente criar a pasta novamente e verifique se o nome é único. | Use nomes distintos para cada pasta.   |

**💡 DICAS E BOAS PRÁTICAS:**
- Sempre mantenha um registro das permissões concedidas a cada usuário.
- Utilize nomes descritivos para pastas para facilitar a localização.
- Revise as permissões periodicamente para garantir que estão atualizadas.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Configuração de Permissões**
```
Situação: Um novo funcionário precisa acessar o módulo de armazenamento.
Ação: Acesse o módulo de administração, selecione o usuário "Maria Oliveira", clique em Editar, e mude a permissão para "Autorização total".
Resultado: Maria agora pode acessar e gerenciar o módulo de armazenamento.
```

**Exemplo 2: Criação de Nova Pasta**
```
Situação: Você precisa organizar documentos financeiros.
Ação: No módulo de armazenamento, clique em "Nova Pasta", insira "Financeiros_2024" e clique em "Criar".
Resultado: A pasta "Financeiros_2024" aparece na tela inicial do módulo.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O usuário deve ter permissões de administrador para alterar configurações de outros usuários.
- **Habilita:** A criação de pastas permite uma melhor organização dos arquivos armazenados.
- **Relacionado a:** Módulo de Administração, onde as permissões são configuradas.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como configurar permissões no módulo de armazenamento?"
- **Com problema:** "Não consigo acessar o módulo de armazenamento, o que fazer?"
- **Informal:** "Como eu libero o acesso para a galera no armazenamento?"
- **Por sintoma:** "Quando um usuário não pode ver as pastas, o que está errado?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Criar pasta", "Adicionar pasta", "Nova pasta", "Cadastrar pasta"
- "Gerenciar permissões", "Alterar acesso", "Configurar usuários"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como eu configuro as permissões de um usuário no módulo de armazenamento?
- O que fazer se um usuário não consegue acessar o módulo de armazenamento?
- Como posso criar uma nova pasta no módulo de armazenamento?
- O que fazer se a pasta que criei não aparece?
- O que preciso fazer antes de alterar as permissões de um usuário?

---


---


---

## 2. Gerenciamento de Pastas e Subpastas

**📋 METADADOS:**
- **ID:** sec_2
- **⏱️ Minutagem:** 02:35 → 04:56
- **⏲️ Duração:** 140s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/VC6EkQJoLEY?si=k9wjmlsuMeBR7kmV&t=155)
- **📦 Módulo:** Gerenciamento de Documentos
- **🏷️ Categorias:** Organização, Armazenamento, Documentação
- **🔑 Palavras-chave:** pasta, subpasta, criar, renomear, excluir, carregar, download

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como criar e gerenciar pastas e subpastas dentro do sistema, permitindo uma melhor organização dos documentos. Ela resolve o problema de armazenamento desorganizado, facilitando o acesso e a manipulação de arquivos.

**Contexto:**
Estamos na interface do módulo de gerenciamento de documentos, onde o usuário pode organizar seus arquivos em pastas e subpastas, facilitando a localização e o controle dos documentos armazenados.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Gerenciamento de Documentos > Pastas
- Tela/interface específica: Tela de Gerenciamento de Pastas

**Funcionalidade Detalhada:**
A funcionalidade de gerenciamento de pastas e subpastas permite ao usuário criar uma estrutura hierárquica para armazenar documentos de forma organizada. O usuário pode criar novas pastas, subdividi-las em subpastas, e gerenciar arquivos através de opções como abrir, renomear, excluir e baixar.

### 🔹 Passo a Passo Detalhado:

1. **Criar Subpasta**
   - Localização: Tela de Gerenciamento de Pastas
   - Como fazer: Clique na opção de **Criar Pasta**. Um campo de texto será exibido para que você insira o nome da nova subpasta.
   - Campos/Opções disponíveis:
     * `Nome da Subpasta`: Campo de texto onde você deve inserir o nome desejado.
   - Resultado esperado: Após clicar em **Criar**, a nova subpasta será apresentada na tela.

2. **Gerenciar Arquivos na Pasta Principal**
   - Localização: Tela de Gerenciamento de Pastas
   - Como fazer: Selecione um arquivo e utilize as opções disponíveis para **Abrir**, **Renomear** ou **Excluir**.
   - Observações importantes: Para excluir um arquivo, certifique-se de que ele não está em uso por outro usuário.
   - Resultado esperado: O arquivo será aberto, renomeado ou excluído conforme a opção escolhida.

3. **Baixar Arquivo**
   - Localização: Tela de Gerenciamento de Pastas
   - Como fazer: Selecione um arquivo já importado e clique na opção **Baixar**.
   - Resultado esperado: O arquivo será baixado para o dispositivo do usuário.

4. **Gerenciar Arquivos na Subpasta**
   - Localização: Dentro da subpasta criada
   - Como fazer: Clique na subpasta e utilize as opções de **Abrir**, **Renomear** ou **Excluir**.
   - Resultado esperado: O arquivo será manipulado conforme a opção escolhida.

5. **Carregar Arquivo**
   - Localização: Tela de Gerenciamento de Pastas
   - Como fazer: Clique nos três pontinhos (menu de opções) e selecione **Carregar Arquivo**. Uma janela será aberta para que você selecione os documentos que deseja importar.
   - Observações importantes: Você pode selecionar múltiplos arquivos para upload.
   - Resultado esperado: Os arquivos selecionados serão carregados para o sistema e aparecerão na tela.

6. **Carregar Pasta**
   - Localização: Tela de Gerenciamento de Pastas
   - Como fazer: Clique nos três pontinhos e selecione **Carregar Pasta**. Uma janela será aberta para que você selecione a pasta desejada no seu dispositivo.
   - Resultado esperado: A pasta inteira será carregada para o sistema, incluindo todos os arquivos contidos nela.

**Campos e Parâmetros:**

| Campo                   | Tipo         | Obrigatório | Descrição                                           | Exemplo                  |
|-------------------------|--------------|-------------|----------------------------------------------------|--------------------------|
| Nome da Subpasta       | Texto        | Sim         | Nome que será atribuído à nova subpasta.          | "Contratos_2024"        |
| Arquivo Selecionado     | Arquivo      | Sim         | Arquivo que será baixado ou manipulado.           | "Relatório_Mensal.pdf"  |
| Pasta Selecionada      | Pasta        | Sim         | Pasta que será carregada para o sistema.          | "Documentos Importantes" |

**Regras de Negócio:**
- O nome da subpasta deve ser único dentro da pasta principal.
- Arquivos não podem ser excluídos se estiverem em uso por outro usuário.
- O sistema permite o upload de múltiplos arquivos simultaneamente.

**Observações Importantes:**
- Ao criar uma subpasta, escolha um nome descritivo para facilitar a identificação.
- Evite nomes de arquivos ou pastas com caracteres especiais, pois podem causar erros no upload.
- Verifique as permissões de usuário se não conseguir acessar ou manipular arquivos.

**Conceitos-Chave:**
- **Subpasta**: Uma pasta criada dentro de outra pasta, permitindo uma organização mais granular dos documentos.
- **Upload**: O processo de transferir arquivos do dispositivo local para o sistema.

**🔧 SOLUÇÃO DE PROBLEMAS (Troubleshooting):**

| Problema                          | Causa Provável                | Solução                                               | Prevenção                                          |
|-----------------------------------|-------------------------------|-------------------------------------------------------|---------------------------------------------------|
| Não consigo criar uma subpasta    | Nome da subpasta já existe    | Tente um nome diferente para a subpasta.             | Verifique se o nome desejado já está em uso.      |
| Arquivo não baixa                 | Problemas de conexão          | Verifique sua conexão com a internet e tente novamente.| Mantenha uma conexão estável ao baixar arquivos.   |
| Erro ao carregar arquivos          | Formato de arquivo não suportado | Verifique se o formato do arquivo é compatível.      | Use formatos comuns como PDF, DOCX, JPG.          |

**💡 DICAS E BOAS PRÁTICAS:**
- Utilize nomes descritivos para pastas e arquivos para facilitar a busca.
- Organize seus documentos em subpastas temáticas para uma melhor gestão.
- Revise as permissões de acesso antes de compartilhar pastas com outros usuários.

**📚 EXEMPLOS PRÁTICOS:**

**Exemplo 1: Criando uma Subpasta para Contratos**
```
Situação: Você precisa organizar contratos de 2024.
Ação: 
  • Clique em **Criar Pasta**.
  • Campo: "Nome da Subpasta": "Contratos_2024".
Resultado: A subpasta "Contratos_2024" é criada e aparece na tela.
```

**Exemplo 2: Carregando uma Pasta de Documentos**
```
Situação: Você deseja carregar uma pasta inteira de documentos.
Ação: 
  • Clique nos três pontinhos e selecione **Carregar Pasta**.
  • Selecione a pasta "Documentos Importantes" no seu dispositivo.
Resultado: A pasta "Documentos Importantes" e todos os seus arquivos são carregados para o sistema.
```

**🔗 DEPENDÊNCIAS E RELAÇÕES:**
- **Pré-requisitos:** O usuário deve ter permissões adequadas para criar pastas e carregar arquivos.
- **Habilita:** A criação de subpastas permite uma organização mais eficiente dos documentos, facilitando a busca e o acesso.
- **Relacionado a:** Funcionalidades de compartilhamento de pastas e gerenciamento de permissões.

**🔍 VARIAÇÕES DE BUSCA (Otimização RAG):**

Esta seção responde perguntas formuladas de diferentes formas. Um usuário pode perguntar:
- **Forma direta:** "Como criar uma subpasta?"
- **Com problema:** "Não consigo criar uma subpasta, o que fazer?"
- **Informal:** "Como faço pra adicionar uma pasta nova?"
- **Por sintoma:** "Quando tento carregar uma pasta, dá erro, como resolver?"

**Termos alternativos e sinônimos usados para esta funcionalidade:**
- "Criar pasta", "Adicionar pasta", "Nova pasta", "Cadastrar pasta"
- "Subpasta", "Pasta secundária", "Divisão de pasta"
- "Upload de arquivos", "Carregar documentos"

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como criar uma subpasta no sistema?
- O que fazer se não consigo baixar um arquivo?
- Como carregar múltiplos arquivos de uma vez?
- O que fazer se a opção de excluir não está disponível?
- O que preciso fazer antes de carregar uma pasta? 

---


---




---


## 🎬 DADOS DE TIMESTAMPS (Para Sistema RAG)


[VIDEO_TIMESTAMPS_DATA]

{
  "Passo a passo - Módulo de Armazenamento": [
    {
      "start": "00:01",
      "end": "02:37",
      "line": "Olá, neste vídeo irei apresentar o funcionamento do módulo armazenamento. O nosso primeiro ponto de "
    },
    {
      "start": "02:35",
      "end": "04:56",
      "line": "Aqui dentro temos a opção de criar uma subpasta. Então, atualmente há a pasta principal e há a possi"
    }
  ]
}

[/VIDEO_TIMESTAMPS_DATA]
