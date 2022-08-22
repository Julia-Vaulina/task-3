import re
import os
from pprint import pprint

new_list = [x for x in os.listdir(path=".") if x[-4:] == '.txt']
print(new_list)


dict_of_txt = {}
for text in new_list:
    dict_of_txt[((len(re.findall(r"\n+?", open(text).read())) + 1), open(text, 'r').read())] = [text]
mysorted = sorted(dict_of_txt.items(), reverse=True)
pprint(mysorted)
for line in mysorted:
    open("new_text_file.txt", "a", encoding='utf-8').write(str("".join(line[-1])) + '\n' +
                                               str(line[0][0]) + '\n' +
                                               str(line[0][1]) + '\n')

