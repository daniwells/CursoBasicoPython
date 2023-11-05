import re

txt = "Escreva uma regex capaz de encontrar no texto deste parágrafo todas as palavras que teriminam com a letra “o”."

#st = re.compile(r'\S')
#check = [c for c in st.finditer(txt)]

st = re.compile(r'^[aeiouAEIOU]+([a-zA-Z]+)|[^a-zA-Z][aeiouAEIOU]+([a-zA-Z]+)?')
check = [c for c in st.finditer(txt)]

print(check)