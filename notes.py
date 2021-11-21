# %%
# Approximate solution
cube = 27
increment_size = 1/3
epsilon = 0.01
guess = 0.0
num_guesses = 0

while abs(guess ** 3 - cube) > epsilon and guess < cube:
  guess += increment_size
  num_guesses += 1

if abs(guess ** 3 - cube) <= epsilon:
  print("Result:", guess)
else:
  print("Couldn't find a solution for an epsilon of", epsilon)
print("Number of guesses:", num_guesses)
# %%
cube = 0.9
epsilon = 0.01
num_guesses = 0

low = 0.0
high = cube
guess = (high + low)/2.0

while abs(guess**3 - cube) >= epsilon:
  if guess**3 < cube:
    low = guess
  else:
    high = guess
  guess = (high + low)/2.0
  num_guesses += 1

print('num_guesses ='), num_guesses
print(guess, 'is close to the cube root of', cube)
