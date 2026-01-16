# 🤖 Automação de Cadastro de Produtos

Projeto simples de automação em Python que cadastra produtos automaticamente em um sistema web, eliminando a necessidade de inserção manual repetitiva.

## 📋 Descrição

Este projeto automatiza o processo de cadastro de produtos em um sistema web através da simulação de ações do mouse e teclado. O script lê dados de produtos de um arquivo CSV e preenche automaticamente os formulários do sistema, economizando tempo e reduzindo erros manuais.

## 🎯 Problema que Resolve

**Antes:** Cadastrar centenas de produtos manualmente era um processo demorado, repetitivo e propenso a erros.

**Depois:** Com esta automação, você pode cadastrar todos os produtos de uma vez, de forma rápida e precisa, apenas executando um script.

## ✨ Funcionalidades Principais

- ✅ **Abertura automática do navegador** - Abre o Chrome automaticamente
- ✅ **Login automatizado** - Realiza login no sistema com credenciais configuradas
- ✅ **Leitura de arquivo CSV** - Importa produtos de um arquivo CSV
- ✅ **Cadastro em lote** - Cadastra múltiplos produtos automaticamente
- ✅ **Preenchimento inteligente** - Preenche todos os campos do formulário (código, marca, tipo, categoria, preço, custo, observações)
- ✅ **Tratamento de dados** - Ignora campos vazios (como observações) automaticamente

## 🚀 Como Executar o Script

### Executando o Script

```bash
python codigo.py
```

**⚠️ Importante:** 
- Não mova o mouse ou use o teclado durante a execução
- Certifique-se de que a janela do navegador está visível
- O script aguarda 5 segundos antes de começar (tempo para você posicionar a tela)

## ⚠️ Limitações Conhecidas

1. **Coordenadas Fixas**: O script usa coordenadas fixas da tela (x, y). Se você mudar a resolução da tela ou o tamanho da janela, será necessário atualizar as coordenadas.

2. **Dependência Visual**: O script precisa que a janela do navegador esteja visível e não minimizada.

3. **Interrupção Manual**: Se você mover o mouse ou usar o teclado durante a execução, pode interferir no funcionamento.

4. **Estrutura do Sistema**: O script foi desenvolvido para um sistema específico. Se a estrutura do formulário mudar, será necessário atualizar as coordenadas e a sequência de ações.

5. **Velocidade de Conexão**: Em conexões lentas, pode ser necessário aumentar os tempos de espera (`pyautogui.sleep()`).

6. **Sistema Operacional**: Testado no Windows. Em outros sistemas operacionais, algumas teclas de atalho podem ser diferentes.

## 📁 Estrutura do Projeto

```
.
├── codigo.py          # Script principal de automação
├── auxiliar.py        # Script auxiliar para descobrir coordenadas do mouse
├── produtos.csv       # Arquivo com os dados dos produtos
└── README.md          # Este arquivo
```

## 📝 Formato do Arquivo CSV

O arquivo `produtos.csv` deve ter as seguintes colunas:

- `codigo` - Código do produto
- `marca` - Marca do produto
- `tipo` - Tipo do produto
- `categoria` - Categoria do produto
- `preco_unitario` - Preço unitário
- `custo` - Custo do produto
- `obs` - Observações (opcional, pode estar vazio)

Exemplo:
```csv
codigo,marca,tipo,categoria,preco_unitario,custo,obs
MOLO000251,Logitech,Mouse,1,25.95,6.50,
CAHA000251,Hashtag,Camisa,1,25.00,11.00,Conferir estoque
```

## 💡 Dicas para Iniciantes

1. **Teste com poucos produtos primeiro**: Modifique o CSV para ter apenas 2-3 produtos e teste antes de executar com muitos produtos.

2. **Use o script auxiliar**: O `auxiliar.py` é muito útil para descobrir as coordenadas corretas dos campos.

3. **Mantenha backups**: Sempre mantenha uma cópia do seu arquivo CSV original.

4. **Execute em ambiente de teste**: Se possível, teste primeiro em um ambiente de desenvolvimento antes de usar em produção.

## 🤝 Contribuindo

Este é um projeto simples e educativo. Sinta-se à vontade para adaptar e melhorar conforme suas necessidades!

## 📄 Licença

Este projeto é de código aberto e está disponível para uso educacional.

---

**Desenvolvido com ❤️ usando Python e PyAutoGUI**
