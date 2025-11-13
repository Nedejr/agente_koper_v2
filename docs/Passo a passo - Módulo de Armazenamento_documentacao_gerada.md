# 📚 Documentação: Passo a passo - Módulo de Armazenamento

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
- **🏷️ Categorias:** Administração, Configuração, Operacional
- **🔑 Palavras-chave:** módulo armazenamento, permissões, usuários, pastas, edição

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como gerenciar as permissões de acesso ao módulo de armazenamento, incluindo como editar usuários e configurar suas permissões, além de descrever as funcionalidades básicas do módulo.

**Contexto:**
Estamos no módulo de armazenamento de um sistema, onde o objetivo é entender como gerenciar as permissões de acesso dos usuários e as funcionalidades disponíveis para manipulação de pastas.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Módulo Administração > Aba Usuários
- Tela/interface específica: Tela de Edição de Usuários e Tela Inicial do Módulo Armazenamento

**Funcionalidade Detalhada:**

O módulo de armazenamento permite que os usuários gerenciem arquivos e pastas dentro do sistema. Inicialmente, apenas o usuário admin possui acesso total. Os administradores podem conceder permissões a outros usuários, definindo se eles terão acesso sem autorização, apenas visualização ou autorização total. Além disso, o módulo permite a criação, edição e exclusão de pastas, bem como a configuração de permissões específicas para cada pasta.

### 🔹 Passo a Passo Detalhado:

1. **Acessar o Módulo Administração**
   - Localização: Menu Principal > Módulo Administração
   - Como fazer: Clique no módulo "Administração" para abrir as opções disponíveis.
   - Resultado esperado: A tela de administração é exibida, permitindo acesso à aba de usuários.

2. **Editar Usuário**
   - Localização: Aba Usuários dentro do Módulo Administração
   - Como fazer: Selecione o usuário que deseja editar e clique no botão "Editar".
   - Resultado esperado: A tela de edição do usuário é exibida, permitindo modificar suas permissões.

3. **Configurar Permissões do Módulo de Armazenamento**
   - Localização: Tela de Edição de Usuário, seção de permissões do módulo de armazenamento
   - Como fazer: Role para baixo até encontrar o módulo de armazenamento. Aqui, você verá três opções:
     * **Sem autorização**: O usuário não terá acesso ao módulo.
     * **Apenas visualização**: O usuário poderá visualizar as pastas, mas não editar.
     * **Autorização total**: O usuário terá acesso completo, podendo editar e excluir pastas.
   - Resultado esperado: Após selecionar a opção desejada, clique em "Concluir Edição" para salvar as alterações.

4. **Acessar o Módulo de Armazenamento**
   - Localização: Menu Principal > Módulo Armazenamento
   - Como fazer: Clique no módulo "Armazenamento" para visualizar a tela inicial do módulo.
   - Resultado esperado: A tela inicial do módulo de armazenamento é exibida, mostrando o espaço total, espaço utilizado e pastas criadas.

5. **Gerenciar Pastas**
   - Localização: Tela Inicial do Módulo Armazenamento
   - Como fazer: Para gerenciar pastas, clique nos três pontinhos ao lado da pasta desejada. As opções disponíveis são:
     * **Abrir**: Visualizar as informações da pasta.
     * **Renomear**: Alterar o nome da pasta. Digite o novo nome e clique em "Salvar".
     * **Permissões**: Visualizar e alterar as permissões dos usuários para essa pasta. Clique para ver os usuários e ajuste suas permissões conforme necessário, clicando em "Salvar" após as alterações.
     * **Excluir**: Remover a pasta do sistema.
   - Resultado esperado: As ações realizadas nas pastas são aplicadas conforme selecionado.

6. **Criar Nova Pasta**
   - Localização: Tela Inicial do Módulo Armazenamento
   - Como fazer: Clique no botão "Nova Pasta", defina o nome da nova pasta e clique em "Criar".
   - Resultado esperado: A nova pasta é criada e aparece na tela inicial do módulo de armazenamento.

**Campos e Parâmetros:**

| Campo                       | Tipo       | Obrigatório | Descrição                                                        | Exemplo               |
|-----------------------------|------------|-------------|------------------------------------------------------------------|-----------------------|
| Nome do Usuário             | Texto      | Sim         | Nome do usuário que está sendo editado                          | João da Silva         |
| Permissão de Acesso         | Dropdown   | Sim         | Nível de acesso ao módulo de armazenamento                       | Sem autorização        |
| Nome da Pasta               | Texto      | Sim         | Nome da nova pasta a ser criada                                  | Documentos            |

**Regras de Negócio:**
- Apenas o usuário admin tem acesso total ao módulo de armazenamento por padrão.
- As permissões podem ser alteradas a qualquer momento por um usuário admin.
- A exclusão de pastas é irreversível e deve ser feita com cautela.

**Observações Importantes:**
- Sempre salve as alterações após modificar permissões ou renomear pastas.
- Verifique se os usuários têm as permissões corretas antes de compartilhar informações sensíveis.
- Evite renomear pastas frequentemente para não confundir os usuários.

**Conceitos-Chave:**
- **Permissão de Acesso**: Nível de acesso que um usuário tem a um módulo ou funcionalidade do sistema.
- **Pasta**: Estrutura de armazenamento que organiza arquivos dentro do módulo de armazenamento.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso editar as permissões de um usuário no módulo de armazenamento?
- Quais são as opções de permissão disponíveis para os usuários?
- Como criar uma nova pasta dentro do módulo de armazenamento?

---


---


---

## 2. Criação e Gerenciamento de Pastas e Subpastas

**📋 METADADOS:**
- **ID:** sec_2
- **⏱️ Minutagem:** 02:35 → 04:56
- **⏲️ Duração:** 140s
- **🎬 Link:** [Assistir este trecho](https://youtu.be/VC6EkQJoLEY?si=k9wjmlsuMeBR7kmV&t=155)
- **📦 Módulo:** Gerenciamento de Arquivos
- **🏷️ Categorias:** Organização, Arquivos, Pastas, Upload
- **🔑 Palavras-chave:** criar pasta, subpasta, renomear, excluir, carregar arquivo, carregar pasta, download, arquivos

> **🔍 RESUMO EXECUTIVO:** Esta seção ensina como criar e gerenciar pastas e subpastas dentro do sistema, permitindo ao usuário organizar seus documentos de forma eficiente. O objetivo é facilitar a localização e o controle dos arquivos armazenados.

**Contexto:**
Estamos na interface de gerenciamento de arquivos do sistema, onde o usuário pode criar pastas e subpastas para organizar documentos. Esta seção detalha as funcionalidades disponíveis para a criação e manipulação dessas estruturas de pastas.

**Localização no Sistema:**
- Caminho de navegação completo: Menu Principal > Gerenciamento de Arquivos > Pastas
- Tela/interface específica: Tela de Gerenciamento de Pastas

**Funcionalidade Detalhada:**
A funcionalidade permite ao usuário criar uma subpasta dentro de uma pasta principal, renomear, excluir e fazer o download de arquivos. O usuário pode também carregar arquivos ou pastas inteiras para o sistema, facilitando a organização e o acesso aos documentos.

### 🔹 Passo a Passo Detalhado:

1. **Criar Subpasta**
   - Localização: Dentro da pasta principal, na interface de gerenciamento de arquivos.
   - Como fazer: Clique na opção de **Criar Pasta**. Um campo de texto aparecerá para que você identifique o nome da nova subpasta.
   - Campos/Opções disponíveis:
     * `Nome da Subpasta`: Campo de texto onde você insere o nome desejado para a subpasta.
   - Resultado esperado: Após clicar em **Criar**, a subpasta será apresentada na tela, visível dentro da pasta principal.

2. **Abrir Arquivo**
   - Localização: Dentro da pasta ou subpasta onde o arquivo está armazenado.
   - Como fazer: Clique no nome do arquivo que deseja abrir.
   - Resultado esperado: O arquivo será aberto na interface do sistema, permitindo visualização ou edição.

3. **Renomear Arquivo**
   - Localização: Na lista de arquivos dentro da pasta ou subpasta.
   - Como fazer: Clique nos três pontinhos (menu de opções) ao lado do arquivo e selecione **Renomear**. Um campo de texto aparecerá para você inserir o novo nome.
   - Observações importantes: O novo nome deve ser único dentro da mesma pasta.
   - Resultado esperado: O arquivo será renomeado conforme o novo nome inserido.

4. **Excluir Arquivo**
   - Localização: Na lista de arquivos dentro da pasta ou subpasta.
   - Como fazer: Clique nos três pontinhos ao lado do arquivo e selecione **Excluir**. Confirme a exclusão quando solicitado.
   - Resultado esperado: O arquivo será removido da pasta ou subpasta.

5. **Baixar Arquivo**
   - Localização: Na lista de arquivos dentro da pasta ou subpasta.
   - Como fazer: Clique nos três pontinhos ao lado do arquivo e selecione **Baixar**.
   - Resultado esperado: O arquivo será baixado para o dispositivo do usuário.

6. **Carregar Arquivo**
   - Localização: Na tela inicial da pasta principal, acessível através do botão **Carregar Arquivo**.
   - Como fazer: Clique em **Carregar Arquivo** e selecione os documentos que deseja importar do seu dispositivo. Você pode selecionar mais de um arquivo.
   - Resultado esperado: Os arquivos selecionados serão carregados e aparecerão na lista de arquivos da pasta.

7. **Carregar Pasta**
   - Localização: Na tela inicial da pasta principal, acessível através do botão **Carregar Pasta**.
   - Como fazer: Clique em **Carregar Pasta** e selecione a pasta desejada do seu dispositivo.
   - Resultado esperado: A pasta inteira será carregada para o sistema, incluindo todos os arquivos contidos nela.

8. **Gerenciar Subpasta**
   - Localização: Dentro da subpasta criada.
   - Como fazer: Clique nos três pontinhos ao lado da subpasta para acessar opções como **Abrir**, **Renomear**, **Excluir**.
   - Resultado esperado: Você poderá gerenciar a subpasta da mesma forma que faz com a pasta principal.

**Campos e Parâmetros:**

| Campo                | Tipo        | Obrigatório | Descrição                                           | Exemplo             |
|----------------------|-------------|-------------|-----------------------------------------------------|---------------------|
| Nome da Subpasta     | Texto       | Sim         | Nome a ser atribuído à nova subpasta.              | "Documentos 2023"   |
| Arquivo              | Arquivo     | Não         | Arquivo a ser carregado ou baixado.                | "relatório.pdf"     |
| Pasta                | Pasta       | Não         | Pasta a ser carregada, contendo arquivos.          | "Projetos"          |

**Regras de Negócio:**
- O nome da subpasta deve ser único dentro da pasta principal.
- Arquivos e pastas podem ser excluídos, mas a exclusão é irreversível.
- O usuário pode carregar múltiplos arquivos simultaneamente.

**Observações Importantes:**
- Ao criar uma subpasta, assegure-se de que o nome não contenha caracteres especiais que possam causar erros.
- Evite renomear arquivos para nomes muito semelhantes, pois isso pode causar confusão na organização.
- Verifique a conexão de internet antes de carregar arquivos ou pastas grandes para evitar falhas no upload.

**Conceitos-Chave:**
- **Subpasta**: Uma pasta criada dentro de outra pasta, utilizada para melhor organização de arquivos.
- **Upload**: O processo de transferir arquivos do dispositivo local para o sistema.

**❓ PERGUNTAS QUE ESTA SEÇÃO RESPONDE:**
- Como posso criar uma subpasta dentro da minha pasta principal?
- Quais opções estão disponíveis para gerenciar arquivos e pastas?
- Como faço para carregar múltiplos arquivos ou uma pasta inteira no sistema?

---


---

