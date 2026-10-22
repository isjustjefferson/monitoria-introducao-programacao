# Monitoria - Introdução à Programação

Resoluções das listas de exercícios da disciplina de **Introdução à Programação**, escritas em **Python** com foco em quem está começando: apenas estruturas básicas (`input`, `print`, `if/elif/else`, `for`, `while`) e comentários explicativos em português.

## Estrutura do repositório

Cada lista tem seu próprio diretório dentro de `Unidade 1/`, e cada questão da lista
é um arquivo `.py` separado.

```
Monitoria/
└── Unidade 1/
    ├── Lista 1/
    │   ├── README.md
    │   ├── questao_xx.py       # onde xx é o número da questão
    │   └── ...
    ├── Lista 2/
    │   ├── README.md
    │   ├── questao_xx.py       # onde xx é o número da questão
    │   └── ...
    ├── Lista 3/
    │   ├── README.md
    │   ├── questao_xx.py       # onde xx é o número da questão
    │   └── ...
    ├── Lista Condicionais/
    │   ├── README.md
    │   ├── questao_xx.py       # onde xx é o número da questão
    │   └── ...
    └── Lista Variáveis e Expressões/
        ├── README.md
        ├── questao_xx.py       # onde xx é o número da questão
        └── ...
```

## Conteúdo

| Diretório | Tema | Questões |
| --- | --- | --- |
| `Unidade 1/Lista 1/` | Lista 1 | 5 |
| `Unidade 1/Lista 2/` | Lista 2 (condicionais) | 10 |
| `Unidade 1/Lista 3/` | Lista 3 (estruturas de repetição) | 8 |
| `Unidade 1/Lista Condicionais/` | Comandos condicionais | 41 |
| `Unidade 1/Lista Variáveis e Expressões/` | Variáveis e expressões | 52 |

Cada arquivo `questao_xx.py` traz o enunciado como comentário (`#`) logo acima da
resolução. Os diretórios também possuem um `README.md` próprio, com orientações
sobre a lista.

## Como executar

É necessário ter o Python 3 instalado. Entre no diretório da lista e execute a
questão desejada:

```bash
python "Unidade 1/Lista 1/questao_01.py"
```

Os programas leem os dados pelo terminal (`input()`). Basta digitá-los quando
solicitado.

## PDFs das resoluções

É possível gerar um PDF por lista, com o enunciado e a resolução de cada questão
(capa, sumário com páginas e destaque de sintaxe no código):

```bash
pip install reportlab
python scripts/gerar_pdfs.py
```

Os arquivos são gravados em `Unidade 1/` como `resolucao_lista_1.pdf`,
`resolucao_lista_2.pdf`, `resolucao_lista_3.pdf`, `resolucao_lista_condicionais.pdf`
e `resolucao_lista_variaveis_expressoes.pdf`.

**Os PDFs não são versionados no Git** (estão ignorados pelo `.gitignore`), assim
como os PDFs de origem das listas. Para obtê-los, basta rodar o comando acima.
Você também pode ter acesso aos PDFs e outros materiais pelo link no Google Drive: https://drive.google.com/drive/folders/1jTws1r_-xFU5PJcR-7Z98p3jfwUyEBHB?usp=drive_link
