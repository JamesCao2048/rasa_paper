import re
text = ""
with open('bracket_input.txt') as f:
    text = f.read()
bracket_pattern = re.compile('\\\\\w*{')
cite_pattern = re.compile('\\\\cite{[\w\-_]*}')

text = re.sub(cite_pattern, '', text)
text = re.sub(bracket_pattern, '', text)
text = re.sub('}', '', text)
text = text.replace("\"", "")
text = text.replace("``", "")
text = text.replace("\\", "")
print(text)
