"""Embute as fotos de fotos/*.jpg no index.html (bloco FOTOS). Rode após trocar qualquer foto."""
import base64, pathlib, re
root = pathlib.Path(__file__).resolve().parent.parent
ids = ["elefante", "espelho", "raiva", "cafe", "passaro", "eco"]
entries = ",\n".join(
    f'  {i}: "data:image/jpeg;base64,{base64.b64encode((root/"fotos"/(i+".jpg")).read_bytes()).decode()}"'
    for i in ids)
block = "/*FOTOS*/const FOTOS = {\n" + entries + "\n};/*/FOTOS*/"
html = (root/"index.html").read_text(encoding="utf-8")
if "/*FOTOS*/" in html:
    html = re.sub(r"/\*FOTOS\*/.*?/\*/FOTOS\*/", lambda m: block, html, flags=re.S)
else:
    html = html.replace("\nconst CATEGORIAS = [", "\n" + block + "\n\nconst CATEGORIAS = [", 1)
(root/"index.html").write_text(html, encoding="utf-8")
