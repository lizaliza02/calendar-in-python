def encode(text,key):
  alphabet="abcdefghijklmnopqrstuvwxyz"
  key=key.lower()
  text=text.lower()
  encoded_text=''

  for char in text:
    if char in alphabet:
      index=alphabet.index(char)
      encoded_text += key[index]
    else:
      encoded_text += char
  return encoded_text

def decode(code,key):
  alphabet="abcdefghijklmnopqrstuvwxyz"
  key=key.lower()
  code=code.lower()
  decoded_text=''

  for char in code:
    if char in alphabet:
      index=key.index(char)
      decoded_text += alphabet[index]
    else:
      decoded_text += char
  return decoded_text

key='zyxbjdjdncjsncjmsjcnhcndhc'
text='github'
encoded=encode(text,key)
decoded=decode(encoded,key)

print("Original Text:", text)
print("Encoded Text:", encoded)
print("Decoded Text:", decoded)