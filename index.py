from docx import Document
import os

# Carregue o arquivo DOCX existente
doc = Document('proposta.docx')

# Acesse o conteúdo do documento
for paragraph in doc.paragraphs:
    if "casa" == paragraph.text:
        paragraph.text = paragraph.text.replace("casa", "alucom")

    if "rato, amor" == paragraph.text:
        paragraph.text = paragraph.text.replace("rato, amor", "Fortaleza, Ceara")

    if "jogo" == paragraph.text:
        paragraph.text = paragraph.text.replace("jogo", "Saúde")

# Salve as alterações no mesmo arquivo ou em um novo arquivo
expd = os.path.expanduser('~\desktop')
file = 'meu_documento_editado.docx'
path = os.path.join(expd, file)
doc.save(path)
