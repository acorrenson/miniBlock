import hashlib

def checkNounce(nounce, diff):
  for i in range(0, diff):
    if nounce[i] != "0":
      return False
  return True

def mine():
  i = 0;
  nounce = str(i).encode()
  a = hashlib.sha256(nounce).hexdigest()

  while checkNounce(a, 4) != True:
    i += 1
    nounce = str(i).encode()
    print(nounce);
    a = hashlib.sha256(nounce).hexdigest()

  print(a)

mine()