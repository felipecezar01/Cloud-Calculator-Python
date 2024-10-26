# ☁️ Cloud Calculator - Python Flask Web App

Este projeto de uma **calculadora web** em Python com Flask foi desenvolvido com o objetivo de praticar o deploy na **AWS EC2** e aprender sobre configurações de ambiente de produção.

---

## 🔍 O que Aprendi

### 1. Deploy de Aplicação na Nuvem com AWS EC2
   - Configuração de uma instância EC2 do zero, usando uma **AMI Ubuntu** e o tipo de instância `t2.micro`.
   - Criação de **grupos de segurança** para liberar as portas necessárias (SSH e HTTP) para acesso externo.
   - Configuração de segurança e monitoramento de uso para controle de custos.

### 2. Configuração de Ambiente de Desenvolvimento Remoto
   - Utilização do SSH para conexão com a instância na AWS.
   - Criação e ativação de um **ambiente virtual Python** na máquina remota para isolar dependências.
   - Instalação e configuração do **Flask** no servidor remoto.

### 3. Transferência de Arquivos e Execução Remota
   - Uso de `scp` para transferir arquivos do projeto local para o servidor AWS.
   - Execução de uma aplicação Flask em ambiente de produção, entendendo as diferenças entre ambiente local e nuvem.

### 4. Monitoramento de Custos na AWS
   - Configuração de **alertas de orçamento** e **detecção de anomalias de custo** para evitar gastos inesperados, garantindo que o uso da AWS EC2 permaneça dentro do limite gratuito.

---

## 📂 Estrutura do Projeto

```plaintext
Cloud-Calculator-Python/
├── app.py          # Código principal da calculadora em Flask
├── index.html      # Interface da calculadora
└── README.md       # Documentação do projeto
