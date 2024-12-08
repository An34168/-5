import re
with open('task2.html', 'r', encoding='utf-8') as file:

    html_content = file.read()

closing_tags = re.findall(r'</\s*([a-zA-Z0-9]+)\s*>', html_content)

unique_closing_tags = sorted(set(closing_tags))

print("Уникальные закрывающие теги:")
for tag in unique_closing_tags:
    print(tag)
