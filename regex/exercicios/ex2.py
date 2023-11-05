import re

txt = """
772.843.809-34
77284380934
772 843 809/34
772.843.809/34
"""

standard = re.compile(r'([0-9]+\.? ?)+([/0-9-]+)?')
check = [c for c in standard.finditer(txt)]

print(check)