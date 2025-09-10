import codecs
import re


def delete_html_tags(html_file: str, result_file: str) -> None:
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

        cleaned_text = re.sub(r'<.*?>', '\n', html, flags=re.DOTALL)

    with codecs.open(result_file, 'w', 'utf-8') as cleaned_file:
        cleaned_file.write(cleaned_text)

delete_html_tags('draft.html', 'cleaned.txt')