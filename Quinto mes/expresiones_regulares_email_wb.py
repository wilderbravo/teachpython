import re 
mail = re.compile(r"""
\b             # comienzo de delimitador de palabra
[\w.%+-]       # usuario: Cualquier caracter alfanumerico mas los signos (.%+-)
+@             # seguido de @
[a-zA-Z.-]     # dominio: Cualquier caracter alfanumerico mas los signos (.-)
+\.            # seguido de .
[a-zA-Z]{2,6}  # dominio de alto nivel: 2 a 6 letras en minúsculas o mayúsculas.
\b             # fin de delimitador de palabra
""", re.X)

mails = """raul.lopez@relopezbriega.com, Raul Lopez Briega,
foo bar, relopezbriega@relopezbriega.com.ar, raul@github.io, 
https://relopezbriega.com.ar, https://relopezbriega.github.io, 
python@python, river@riverplate.com.ar, pythonAR@python.pythonAR, wilderbravo@gmail.com, ariosto@micorreo.exe
"""

correos = mail.findall(mails)

print(correos)
