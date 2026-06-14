# 🛡️ Security Research PoC (Keylogging & Remote Command Execution) v1.0

Este projeto é uma **Proof of Concept (PoC) v1.0** desenvolvida para fins educacionais e de pesquisa em segurança ofensiva.

O sistema simula um ambiente controlado de laboratório com comunicação entre cliente e servidor, incluindo execução remota de comandos e captura de eventos de teclado para análise de comportamento em sistemas.

---

## ⚙️ Funcionalidades

- 💻 Execução remota de comandos em ambiente controlado  
- ⌨️ Captura de eventos de teclado para fins de análise  
- 🌐 Comunicação via sockets em rede local  
- 🔄 Estrutura cliente-servidor para simulação de interação remota  
- 📡 Envio de dados em formato JSON entre os módulos  

---

## 🎯 Objetivo

Estudo e compreensão de técnicas utilizadas em ferramentas de administração remota e mecanismos de monitoramento de entrada e execução de comandos em sistemas operacionais.

O projeto tem foco em aprendizado prático de:
- Comunicação em rede (sockets)
- Processamento de eventos do sistema
- Execução remota de comandos em ambientes controlados

---

## 📌 Interface de comandos

O projeto possui uma interface simples de comandos para controle do ambiente de teste.

 
- `start keylogger` → Inicia o módulo de monitoramento de eventos de teclado (ambiente de laboratório)  
- `stop keylogger` → Interrompe o módulo de monitoramento de teclado
- `help` → Exibe a lista de comandos disponíveis 
- Outros comandos → Encaminhados para execução no sistema remoto dentro do ambiente de teste  

---

## 🔄 Comunicação

A comunicação entre cliente e servidor é realizada via sockets, permitindo interação em tempo real durante o ambiente controlado de testes.

---

## 🧪 Ambiente de Uso

Este projeto foi desenvolvido para execução em:
- 🧑‍💻 Máquinas de laboratório  
- 🔒 Ambientes controlados  
- 🧰 Cenários de testes e pesquisa  

---

## ⚠️ Aviso Legal

Este projeto foi desenvolvido **exclusivamente para fins educacionais e de pesquisa em segurança**.

Qualquer uso em sistemas, redes ou dispositivos sem autorização explícita é de responsabilidade do usuário e pode violar leis e políticas aplicáveis.

O autor não se responsabiliza pelo uso indevido desta ferramenta.
