#Installation: pip install translate
from translate import Translator
#translate from de to en
translator= Translator(to_lang="en", from_lang="de")
#you must have file(ex:test.txt) that contain de text and this section create a new file in en  
try:
    with open('./test.txt', mode='r') as m2:
        text = m2.read()
        translation = translator.translate(text)
        print(translation)
        with open('./test-de.txt', mode='w') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as err:
    print("check file path")