import streamlit as st
from docx import Document
import os

# Carregue o arquivo DOCX existente
doc = Document('proposta.docx')

# Título da aplicação
st.title("Formulário Simples")

# Crie os campos do formulário
cliente = st.text_input("Nome do Cliente")
cidade = st.text_input("Cidade")
estado = st.text_input("Estado")
setor = st.text_input("Setor")

# Crie um botão "Submit" para enviar o formulário
if st.button("Gerar"):
    # Quando o botão é clicado, exiba os valores inseridos nos campos
    # st.write("Cliente:", cliente)
    # st.write("Cidade:", cidade)
    # st.write("Estado:", estado)
    # st.write("Setor:", setor)

    # Acesse o conteúdo do documento
    for paragraph in doc.paragraphs:
        if "casa" == paragraph.text:
            paragraph.text = paragraph.text.replace("casa", cliente)

        if "rato, amor" == paragraph.text:
            paragraph.text = paragraph.text.replace("rato, amor", f"{cidade}, {estado}")

        if "jogo" == paragraph.text:
            paragraph.text = paragraph.text.replace("jogo", setor)

    # Salve as alterações no mesmo arquivo ou em um novo arquivo
    expd = os.path.expanduser('~\desktop')
    file = 'meu_documento_editado.docx'
    path = os.path.join(expd, file)
    doc.save(path)
