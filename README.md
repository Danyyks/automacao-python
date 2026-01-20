# 🤖 Automação de Cadastro de Produtos com Python

Criei um script em Python que automatiza o cadastro de produtos em um sistema web, simulando ações do mouse e teclado para eliminar trabalho manual repetitivo.

## O que ele faz?

Quando o script é executado, ele:  
**Abre o navegador:** Inicia automaticamente o Google Chrome.  
**Faz login:** Acessa o sistema com credenciais configuradas.  
**Lê o csv:** Importa os dados dos produtos a partir de um arquivo CSV.  
**Preenche formulários:** Código, marca, tipo, categoria, preço, custo e observação.  
**Cadastro em lote:** Registra múltiplos produtos em sequência.  
**Trata exceções:** Ignora campos vazios automaticamente.

## Anatomia da automação

**Entrada:** Arquivo `produtos.csv` com os dados.  
**Controle:** Python + pyautogui.  
**Interação:** Simulação de mouse e teclado.  
**Precisão:** Uso de coordenadas fixas da tela (x,y).  
**Apoio:** Script auxiliar para descobrir coordenadas do mouse.

## Por que isso é legal?

**Economia de tempo:** Chega de cadastrar produto por produto.  
**Menos erros:** Reduz falhas humanas no preenchimento.  
**Automação real:** Resolve um problema comum do dia a dia.  
**Projeto educacional:** Excelente para aprender automação com Python.

## Requisitos

Python 3.x  
Biblioteca pyautogui (`pip install pyautogui`)  
Navegador Google Chrome  
Sistema web acessível via navegador  
Windows (sistema testado)

## Como usar

1. Clone este repositório.
2. Ajuste credenciais e coordenadas no: codigo.py.
3. Prepare o arquivo `produtos.csv`.
4. Execute o script.

### ⚠️ Atenção!

Não mova o mouse nem use o teclado durante a execução.  
Mantenha o navegador aberto.  
O script aguarda 5 segundos antes de iniciar (tempo para posicionar a tela)
