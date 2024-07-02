import re

def convert_headers(line):
    match = re.match(r'^(#{1,6})\s+(.*)', line)
    if match:
        level = len(match.group(1))
        text = match.group(2)
        return f'<h{level}>{text}</h{level}>'
    return line

def convert_bold_italic(line):
    line = re.sub(r'\*\*\*(.*?)\*\*\*', r'<b><i>\1</i></b>', line)
    line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
    line = re.sub(r'\*(.*?)\*', r'<i>\1</i>', line)
    return line

def convert_code_blocks(line):
    line = re.sub(r'`{3}(.*?)`{3}', r'<pre><code>\1</code></pre>', line, flags=re.DOTALL)
    line = re.sub(r'`(.*?)`', r'<code>\1</code>', line)
    return line

def convert_lists(lines):
    in_list = False
    html_lines = []
    for line in lines:
        if line.startswith('- '):
            if not in_list:
                in_list = True
                html_lines.append('<ul>')
            html_lines.append(f'<li>{line[2:]}</li>')
        else:
            if in_list:
                in_list = False
                html_lines.append('</ul>')
            html_lines.append(line)
    if in_list:
        html_lines.append('</ul>')
    return html_lines

def markdown_to_html(markdown):
    lines = markdown.split('\n')
    lines = convert_lists(lines)
    html_lines = []
    for line in lines:
        line = convert_headers(line)
        line = convert_bold_italic(line)
        line = convert_code_blocks(line)
        html_lines.append(line)
    return '\n'.join(html_lines)

def main():
    input_file = input("Enter the path to the Markdown file: ")
    output_file = input("Enter the path to the output HTML file: ")

    with open(input_file, 'r') as f:
        markdown = f.read()

    html = markdown_to_html(markdown)

    with open(output_file, 'w') as f:
        f.write(html)

    print(f"Converted {input_file} to {output_file}")

if __name__ == "__main__":
    main()
