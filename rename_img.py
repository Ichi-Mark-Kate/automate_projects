import os, re

regexp = re.compile(r".*.png")

i = 0
for folderName, subfolders, imgfilenames in sorted(os.walk('/home/NIX/kshapovalova/automate_projects/test_rename_img_in_diff_folder')):
    for img in sorted(imgfilenames):
            mo = regexp.sub("img_test_" + str(i + 1) + ".png", img)
            os.rename(folderName + "/" + img, folderName + "/" + mo)
            i += 1

            if mo == None:
                continue


