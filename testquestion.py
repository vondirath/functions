import cgi

list_content = """
<ul>

{list_item}
</ul>
"""

list = ["<h1>a", "bunch", "of", "list", "items"]


def format_list(list):
    output = ''
    for x in range(len(list)):
        
        output += ('\t' + '<li>' + list[x] + '</li>' + '\n')
    return output

def open_page(list):
    output_file = open('index.html', 'w')
    content = list_content.format(list_item=format_list(list))
    output_file.write(content)
    output_file.close()

open_page(list)

# to handle input

