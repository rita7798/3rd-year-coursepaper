import os
import re


for file in os.listdir('.'):
    if file.endswith('ipynb') or file.endswith('proc.txt'):
        continue
    else:
        if re.match('.*[0-9]{4}.txt', file):
            #print(file)
            with open (file, 'r', encoding='utf-8') as f:
                text = f.read()
                text_ = re.sub('<br>', '', text)
                text_ = re.sub('&nbsp;', '', text_)
                text_ = re.sub('<a.*</a>', '', text_)
                text_ = re.sub('&quot;', '"', text_)
                with open(file[:-4]+'_proc.txt', 'w', encoding='utf-8') as f:
                    f.write(text_)

