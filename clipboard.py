import pyperclip

text = pyperclip.paste()
if text:
    print(text)
else:
    print('OK')
