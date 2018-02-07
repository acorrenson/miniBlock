import hashlib

# Proof of Work
def checkHash(ha, diff):
  """ha = hash to check; diff = difficulty"""
  for i in range(0, diff):
    if ha[i] != "0":
      return False
  return True

# mine to validate PoW
def mine():
  i = 0;
  nounce = str(i).encode()
  a = hashlib.sha256(nounce).hexdigest()

  while checkHash(a, 4) != True:
    i += 1
    nounce = str(i).encode()
    print(nounce);
    a = hashlib.sha256(nounce).hexdigest()

  print(a)

mine()