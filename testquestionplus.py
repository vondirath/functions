import re

# making an empty template
list_content = """
<ul>

{list_item}
</ul>
"""

# this is a list accomidating for a good amount of edge cases
# for html and python.
list = ["this", "<h1>is</h1>", "a   ", "list {list_content}(open_page() } \|"]


def format_list(list):
    """
        formats a list by using python regular expression substitution.
        this will autoescape most non-alphanumeric characters replaced
        by empty string all numbers allowed all alphabetical upper and
        lower case and spaces. output is saved to a empty string as the
        list is iterated through using the regex as it iterates. tab
        character is added with html tags and a new line tag so it
        renders an easy to read format.

    """
    output = ''
    for x in range(len(list)):
        new = re.sub('[^0-9a-zA-Z-\s]+', '', list[x])
        output += ('\t' + '<li>' + new + '</li>' + '\n')
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

# calls open_page method with hardcoded list as argument
open_page(list)
