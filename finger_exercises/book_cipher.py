from typing import Any, Callable

coding_dictionary = 'Somewhere in La Mancha, in a place whose name I do not care to remember, a gentleman lived not long ago, one of those who has a lance and ancient shield on a shelf and keeps a skinny nag and a greyhound for racing'

# Encrypting functions
gen_code_keys: Callable[[str, str], Any] = lambda book, plain_text:(
  {c: str(book.find(c)) for c in plain_text})

encoder: Callable[[dict[str, str], str], str] = (
  lambda code_keys, plain_text: ''.join(['*' + code_keys[c] for c in plain_text])
  )

encrypt: Callable[[str, str], str] = (lambda book, plain_text:
  encoder(gen_code_keys(book, plain_text), plain_text))

# Decrypting functions
gen_decode_keys: Callable[[str, str], Any] = (lambda book, cipher_text:
  {s: book[int(s)] for s in cipher_text.split("*")[1:] if int(s) > 0})

def decoder():
  pass

def decrypt():
  pass

encrypted_message = encrypt(coding_dictionary, 'No is no')
print(encrypted_message)
print(gen_decode_keys(coding_dictionary, encrypted_message))