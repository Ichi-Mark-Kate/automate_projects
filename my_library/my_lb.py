import pyperclip

def comment(comand='drop'):
    text = pyperclip.paste()
    lines = text.split('\n')

    if comand == 'add':
        for i in range(len(lines)):    
            lines[i] = '# ' + lines[i]
    else:
        for i in range(len(lines)):
            lines[i] = lines[i][2:]    
    
    text = '\n'.join(lines)
    return print(text)
