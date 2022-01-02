fib_handle = open('fib_file', 'w')
#  TODO: Mock fib_num. Search the real value when internet is available.
fib_num = str(((1/7) * 1E10))[:10]
for digit in fib_num:
  fib_handle.write(digit + '\n')
fib_handle.close()

fib_handle = open('fib_file', 'r')
for line in fib_handle:
  print(line[:-1])
fib_handle.close()
