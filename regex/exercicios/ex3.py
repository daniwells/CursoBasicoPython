import re

txt = "Escreva uma regex capaz de encontrar no texto deste parágrafo todas as palavras que teriminam com a letra “o”."

st = re.compile(r'(([a-zA-Zá]?)+[Oo])+ ')
check = [c for c in st.finditer(txt)]

print(check)