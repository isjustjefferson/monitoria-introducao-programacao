# -*- coding: utf-8 -*-
"""Gera um PDF de resolucoes por lista de exercicios.

Uso:
    pip install reportlab
    python scripts/gerar_pdfs.py

Os PDFs sao gravados em "Unidade 1/" com os nomes:
    resolucao_lista_1.pdf
    resolucao_lista_2.pdf
    resolucao_lista_3.pdf
    resolucao_lista_condicionais.pdf
    resolucao_lista_variaveis_expressoes.pdf

Nota: os PDFs nao sao versionados no Git (ver .gitignore).
"""
import html
import pathlib
import re
import sys

try:
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import cm
    from reportlab.platypus import (BaseDocTemplate, Frame, PageBreak,
                                    PageTemplate, Paragraph, Spacer, Table,
                                    TableStyle, XPreformatted)
    from reportlab.platypus.tableofcontents import TableOfContents
except ImportError:
    sys.exit("Faltou a biblioteca reportlab. Instale com: pip install reportlab")


RAIZ = pathlib.Path(__file__).resolve().parent.parent
BASE = RAIZ / "Unidade 1"
OUT = BASE

LISTAS = [
    ("Lista 1", "Lista 1", "resolucao_lista_1.pdf"),
    ("Lista 2", "Lista 2", "resolucao_lista_2.pdf"),
    ("Lista 3", "Lista 3", "resolucao_lista_3.pdf"),
    ("Lista Condicionais", "Lista de Comandos Condicionais",
     "resolucao_lista_condicionais.pdf"),
    ("Lista Variáveis e Expressões", "Lista de Variáveis e Expressões",
     "resolucao_lista_variaveis_expressoes.pdf"),
]

PALETA = {
    "palavra": "#0B5FA5",
    "builtin": "#7A3E9D",
    "string": "#A31515",
    "comentario": "#3F7A3F",
    "numero": "#8A4B08",
    "texto": "#1A1A1A",
}

KEYWORDS = {
    "if", "elif", "else", "for", "while", "in", "not", "and", "or", "def", "return",
    "import", "from", "as", "pass", "break", "continue", "True", "False", "None",
    "class", "lambda", "with", "try", "except", "global", "del", "is",
}

BUILTINS = {
    "print", "input", "int", "float", "str", "bool", "list", "len", "range", "abs",
    "min", "max", "sum", "round", "math", "random",
}

TOKEN = re.compile(
    r"(?P<comentario>#.*)"
    r"|(?P<string>\"(?:[^\"\\]|\\.)*\"|'(?:[^'\\]|\\.)*')"
    r"|(?P<numero>\b\d+(?:[.,]\d+)?\b)"
    r"|(?P<nome>[A-Za-z_][A-Za-z_0-9]*)"
)


def esc(t):
    return html.escape(t, quote=False)


def realcar(linha):
    """Aplica cores a uma linha de codigo Python (retorna HTML)."""
    partes = []
    pos = 0
    for m in TOKEN.finditer(linha):
        partes.append(esc(linha[pos:m.start()]))
        pos = m.end()
        texto = esc(m.group())
        if m.lastgroup == "comentario":
            cor = PALETA["comentario"]
        elif m.lastgroup == "string":
            cor = PALETA["string"]
        elif m.lastgroup == "numero":
            cor = PALETA["numero"]
        else:
            nome = m.group()
            if nome in KEYWORDS:
                cor = PALETA["palavra"]
            elif nome in BUILTINS:
                cor = PALETA["builtin"]
            else:
                cor = PALETA["texto"]
        partes.append('<font color="%s">%s</font>' % (cor, texto))
    partes.append(esc(linha[pos:]))
    return "".join(partes)


def ler_questao(caminho):
    """Separa o arquivo de uma questao em (numero, enunciado, codigo)."""
    linhas = caminho.read_text(encoding="utf-8").split("\n")
    i = next(i for i, l in enumerate(linhas) if l.startswith("# Questão"))
    j = next(k for k in range(i + 1, len(linhas)) if linhas[k].startswith("# ---"))
    numero = int(linhas[i].split("Questão")[1].strip())

    enunciado = []
    for l in linhas[i + 1:j]:
        l = l[1:] if l.startswith("#") else l
        enunciado.append(l[1:] if l.startswith(" ") else l)

    codigo = linhas[j + 1:]
    while codigo and codigo[0].strip() == "":
        codigo.pop(0)
    while codigo and codigo[-1].strip() == "":
        codigo.pop()
    return numero, enunciado, codigo


def criar_estilos():
    st = getSampleStyleSheet()
    st.add(ParagraphStyle(name="ListTitle", parent=st["Title"],
                          fontName="Helvetica-Bold", fontSize=20, leading=26,
                          alignment=TA_CENTER,
                          textColor=colors.HexColor("#0B3C5D"), spaceAfter=12))
    st.add(ParagraphStyle(name="Centered", parent=st["Normal"],
                          fontName="Helvetica", fontSize=10.5, leading=16,
                          alignment=TA_CENTER,
                          textColor=colors.HexColor("#444444")))
    st.add(ParagraphStyle(name="QTitle", parent=st["Heading2"],
                          fontName="Helvetica-Bold", fontSize=13, leading=18,
                          spaceBefore=10, spaceAfter=4,
                          textColor=colors.HexColor("#0B3C5D")))
    st.add(ParagraphStyle(name="SecaoTitle", parent=st["Heading2"],
                          fontName="Helvetica-Bold", fontSize=12, leading=16,
                          spaceBefore=8, spaceAfter=4,
                          textColor=colors.HexColor("#0B3C5D")))
    st.add(ParagraphStyle(name="Enunciado", fontName="Courier", fontSize=8,
                          leading=10.5, textColor=colors.HexColor("#333333")))
    st.add(ParagraphStyle(name="Codigo", fontName="Courier", fontSize=7.5,
                          leading=10, textColor=colors.HexColor(PALETA["texto"])))
    st.add(ParagraphStyle(name="TOCLista", fontName="Helvetica", fontSize=9.5,
                          leading=11.5, spaceBefore=1.5,
                          textColor=colors.HexColor("#0B3C5D")))
    return st


def construir(caminho, estilos, titulo_lista, largura):
    flow = []

    flow.append(Paragraph(titulo_lista, estilos["ListTitle"]))
    flow.append(Spacer(1, 0.4 * cm))
    flow.append(Paragraph(
        "Resoluções das questões, com o enunciado de cada uma e o código em Python.",
        estilos["Centered"]))
    flow.append(Spacer(1, 0.3 * cm))
    flow.append(Paragraph(
        "Disciplina: Introdução à Programação &nbsp;|&nbsp; Unidade 1",
        estilos["Centered"]))
    flow.append(Spacer(1, 0.3 * cm))
    flow.append(Paragraph(
        "Total de questões: %d" % len(sorted(caminho.glob("questao_*.py"))),
        estilos["Centered"]))
    flow.append(Spacer(1, 0.8 * cm))
    flow.append(Paragraph("Sumário", estilos["SecaoTitle"]))

    questoes = sorted(caminho.glob("questao_*.py"))
    toc = TableOfContents()
    toc.levelStyles = [estilos["TOCLista"]]
    flow.append(toc)
    flow.append(PageBreak())

    for arquivo in questoes:
        numero, enunciado, codigo = ler_questao(arquivo)

        titulo = Paragraph("Questão %d" % numero, estilos["QTitle"])
        enun = XPreformatted("\n".join(enunciado), estilos["Enunciado"])
        bloco = XPreformatted("\n".join(realcar(l) for l in codigo),
                              estilos["Codigo"])

        caixa = Table([[bloco]], colWidths=[largura])
        caixa.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F6F8FA")),
            ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#D0D7DE")),
            ("LEFTPADDING", (0, 0), (-1, -1), 8),
            ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 7),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ]))

        flow.append(titulo)
        flow.append(enun)
        flow.append(Spacer(1, 0.3 * cm))
        flow.append(caixa)
        flow.append(Spacer(1, 0.7 * cm))

    return flow


class ResolucaoDoc(BaseDocTemplate):
    def __init__(self, filename, titulo, **kw):
        BaseDocTemplate.__init__(self, filename, **kw)
        self.titulo = titulo
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height,
                      id="normal")
        self.addPageTemplates([PageTemplate(id="todos", frames=[frame],
                                            onPage=self.decorar)])

    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph):
            if flowable.style.name == "QTitle":
                self.notify("TOCEntry", (0, flowable.getPlainText(), self.page))

    def decorar(self, canvas, doc):
        canvas.saveState()
        largura, altura = A4
        canvas.setStrokeColor(colors.HexColor("#D0D7DE"))
        canvas.setLineWidth(0.6)
        canvas.line(doc.leftMargin, altura - doc.topMargin + 0.4 * cm,
                    largura - doc.rightMargin, altura - doc.topMargin + 0.4 * cm)
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.HexColor("#777777"))
        canvas.drawString(doc.leftMargin, 1.2 * cm, self.titulo)
        canvas.drawRightString(largura - doc.rightMargin, 1.2 * cm,
                               "Página %d" % doc.page)
        canvas.restoreState()


def main():
    estilos = criar_estilos()
    margem = 2 * cm
    largura_util = A4[0] - 2 * margem

    if not BASE.exists():
        sys.exit("Pasta nao encontrada: %s" % BASE)

    for pasta, titulo, nome_pdf in LISTAS:
        caminho = BASE / pasta
        if not caminho.exists():
            print("AVISO: pasta nao encontrada, ignorando: %s" % pasta)
            continue
        destino = OUT / nome_pdf
        doc = ResolucaoDoc(
            str(destino), titulo,
            pagesize=A4,
            leftMargin=margem, rightMargin=margem,
            topMargin=margem, bottomMargin=margem,
            title="Resolucao %s" % titulo,
            author="Monitoria - Introducao a Programacao",
            subject="Resolucoes das listas de exercicios",
        )
        doc.multiBuild(construir(caminho, estilos, titulo, largura_util))
        print("%s -> %s" % (pasta, destino.name))


if __name__ == "__main__":
    main()
