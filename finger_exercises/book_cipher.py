from typing import Any, Callable


gen_code_keys: Callable[[str, str], Any] = lambda book, plain_text:(
  {c: str(book.find(c)) for c in plain_text})

encoder: Callable[[dict[str, str], str], str] = (
  lambda code_keys, plain_text: ''.join(['*' + code_keys[c] for c in plain_text])
  )

encrypt: Callable[[str, str], str] = (lambda book, plain_text:
  encoder(gen_code_keys(book, plain_text), plain_text))

coding_dictionary = 'Once upon a time, in a house in a land far away'

gen_decode_keys: Callable[[str, str], dict[str, str]] = (lambda book, cipher_text:
  {s: book[int(s)] for s in cipher_text.split('*')})

encrypted_message = encrypt(coding_dictionary, 'no is no')
print(gen_decode_keys(coding_dictionary, encrypted_message))