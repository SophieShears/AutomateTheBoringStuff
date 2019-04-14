#! Python3.6
# bruteForcePDF.py - Try every english word on a pdf password to try to open it.

import PyPDF2

# Add each line in the dictionary to a list.
with open(r'E:\Scripts\Automate\automate_online-materials\dictionary.txt', 'r') as f:
    allWords = [line.strip() for line in f]

pdfReader = PyPDF2.PdfFileReader(open(r'E:\Scripts\Automate\automate_online-materials\encrypted.pdf', 'rb'))

# Loop through all the words in english to try to decrypt the PDF.
for word in allWords:
    if pdfReader.decrypt(word.upper()) or pdfReader.decrypt(word.lower()) == 1:
        print('The password was: ' + word)
    else:
        continue
