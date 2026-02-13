

def markdown_to_blocks(markdown):
    markdown = markdown.replace("\r\n", "\n")
    if markdown.find("```") != -1:
        # handle fenced code blocks separately
        parts = markdown.split("```")
        for i in range(1, len(parts), 2):
            parts[i] = parts[i].replace("\n\n", "\n<<BLANKLINE>>\n")
        markdown = "```".join(parts)
    lines = markdown.split("\n\n")
    blocks = []
    for line in lines:
        line = line.strip()
        line = line.replace("<<BLANKLINE>>", '')
        if line:
            blocks.append(line)

    
    
    return blocks