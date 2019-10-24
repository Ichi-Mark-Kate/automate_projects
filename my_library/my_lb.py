import pyperclip
import os, re

def rename_image(path, file_format = "jpg", result_name = 'img'):
    """Example: my_lb.rename_image(path = '/home/NIX/kshapovalova/automate_projects/test_rename_img_in_diff_folder');
       - don't reuse this function on the same images. If you should then rename images: for new name not 
       available image old name and result_name;
    """
    regexp = re.compile(r".*." + file_format)
    i = 0
    for folderName, subfolders, imgfilenames in sorted(os.walk(path)):
        for img in sorted(imgfilenames):
                mo = regexp.sub(result_name + str(i + 1) + "." + file_format, img)
                os.rename(folderName + "/" + img, folderName + "/" + mo)
                i += 1
                if mo == None:
                    continue

"""
The functions below are deprecated functions. Why:

* comment() - can easily replace by multiline comment, which less time consuming;

"""
def comment(comand='drop'):
    """Example: my_lb.comment(comand = 'add');
       - copy text that you would like comment out and run this function;
       - be aware when copying: first string must have all space symbols like in original text otherwise you to lose original format;
    """
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
    
     
