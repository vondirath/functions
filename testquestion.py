# empty template
list_content = """
<ul>

{list_item}
</ul>
"""

# list while providing a simple edge case that is NOT accomidated for.
list = ["<h1>a", "bunch", "of", "list", "items"]


def format_list(list):
    """
    Formats the list argument by adding list tags tabs and a new line.
    """
    output = ''
    for x in range(len(list)):
        output += ('\t' + '<li>' + list[x] + '</li>' + '\n')
    return output


def open_page(list):
    """
        this creates the page by writing a html file named 'index.html'
        calling the format_list method taking a list argument and
        inserting it into the lost_content template.
        file is then written to and closed.
    """
    output_file = open('index.html', 'w')
    content = list_content.format(list_item=format_list(list))
    output_file.write(content)
    output_file.close()

open_page(list)
