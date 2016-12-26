import re 

list_content = """
<ul>

{list_item}
</ul>
"""

list = ["<h1>  a", "<h1>bun ch", "of<h1>", " list items spaces?", "/ul>ite ms<script>"]



def format_list(list):
    output = ''
    for x in range(len(list)):
        new = re.sub('[^0-9a-zA-Z-\s]+', '', list[x])
        output += ('\t' + '<li>' + new + '</li>' + '\n')
    return output

def open_page(list):
    output_file = open('index.html', 'w')
    content = list_content.format(list_item=format_list(list))
    output_file.write(content)
    output_file.close()

open_page(list)

