# 🎓 SchoolPassReader

Sistema de gestão de fluxo escolar desenvolvido para automatizar o controle de presença, entrada e saída de alunos, contribuindo para a otimização do tempo em sala de aula, melhoria da segurança escolar e acompanhamento da frequência estudantil.

---

## 📌 Sobre o Projeto

O SchoolPassReader surgiu a partir da observação de um problema comum em muitas instituições de ensino: o tempo gasto com chamadas manuais e a dificuldade de monitorar, em tempo real, a presença e o fluxo de alunos dentro da escola.

A proposta do sistema é centralizar essas informações em uma única plataforma, permitindo o registro automatizado de presença e o acompanhamento de acessos de forma prática e organizada.

O projeto foi apresentado durante o evento Conexão Ciências e continua em desenvolvimento, com novas funcionalidades planejadas para futuras versões.

---

## 🎯 Problemas que o Sistema Busca Resolver

* Tempo excessivo gasto com chamadas manuais em sala de aula.
* Dificuldade de controle da entrada e saída de alunos.
* Falta de informações centralizadas sobre presença escolar.
* Necessidade de maior segurança no ambiente escolar.
* Dificuldade de contabilização diária de alunos presentes.
* Falta de integração entre escola e responsáveis.

---

## 🚀 Funcionalidades Atuais

### Cadastro de Alunos

* Cadastro completo de alunos.
* Registro de número de chamada.
* Registro de matrícula.
* Associação automática do aluno à sua turma.
* Geração de identificação única para cada aluno.

### Pesquisa de Alunos

* Busca por:

  * Nome
  * Matrícula
  * Turma
  * ID do sistema

### Registro de Acesso

* Registro de entrada do aluno.
* Registro de saída do aluno.
* Armazenamento de data e horário dos acessos.

### Controle de Presença

* Registro automático de presença.
* Prevenção de presenças duplicadas durante o mesmo dia.
* Controle adequado para alunos que retornam em contraturno.

### Relatórios

* Relatório de acessos.
* Relatório de presenças.
* Histórico de registros realizados.

### Banco de Dados

* Persistência de dados utilizando SQLite.

---

## 🛠️ Tecnologias Utilizadas

### Back-end

* Python
* Flask

### Banco de Dados

* SQLite

### Front-end

* HTML
* CSS

### Controle de Versão

* Git
* GitHub

---

## 🔄 Fluxo de Funcionamento

1. O aluno é cadastrado no sistema.
2. O sistema armazena suas informações acadêmicas.
3. Ao registrar um acesso, o sistema identifica o aluno através do nome ou matrícula.
4. A entrada é registrada com data e horário.
5. A presença é contabilizada automaticamente.
6. Os registros ficam disponíveis nos relatórios para consulta posterior.

---

## 📈 Próximas Funcionalidades

### Infraestrutura

* Migração do banco SQLite para MySQL.
* Hospedagem em servidor dedicado.

### Segurança

* Integração com leitor biométrico.
* Sistema de reconhecimento facial.
* Validação de identidade estudantil.

### Gestão Escolar

* Sistema de login para coordenadores.
* Sistema de login para professores.
* Controle de permissões por perfil.
* Dashboard administrativo.
* Relatórios avançados.

### Comunicação com Responsáveis

* Aplicativo para pais e responsáveis.
* Notificações automáticas de entrada e saída.
* Envio de justificativas de ausência.
* Integração com documentos e atestados médicos.

---

## 📊 Roadmap

### Versão 1.0

* Cadastro de alunos
* Registro de acessos
* Controle de presença
* Relatórios básicos

### Versão 2.0

* Sistema de login
* Controle de usuários
* Banco MySQL

### Versão 3.0

* Dashboard administrativo
* Relatórios avançados
* Controle de permissões
* Indicadores de frequência

### Versão 4.0

* Biometria
* Reconhecimento facial
* Dashboard interativo

### Versão 5.0

* Aplicativo para responsáveis
* Integração completa escola-família

---

## 🌐 Demonstração

Acesse a versão online do sistema:

🔗 [SchoolPassReader](https://schoolpassreader.onrender.com/)

> Observação: Por estar hospedado no plano gratuito do Render, a primeira inicialização pode levar alguns segundos após períodos de inatividade.

---

## 👨‍💻 Autor

André Cunha Correa

Estudante de Desenvolvimento de Sistemas pelo SENAI, apaixonado por tecnologia, automação e criação de soluções que gerem impacto real através do software.

GitHub: https://github.com/Andrecc-dev
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/andr%C3%A9-cunha-correa-93b4a8398/)

---
## 📚 Aprendizados

Durante o desenvolvimento do SchoolPassReader foram aplicados conceitos de:

* Desenvolvimento Web com Flask
* Estruturação de aplicações MVC
* Manipulação de banco de dados SQLite
* Criação de interfaces utilizando HTML e CSS
* Controle de rotas e requisições HTTP
* Organização de projetos com Git e GitHub
* Deploy de aplicações web utilizando Render
* Modelagem de fluxo de usuários
* Controle de presença e registros em banco de dados