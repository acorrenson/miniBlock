import datetime
import time
import hashlib

import cheater

class Block:
  def __init__(self, data):
    self.index = None
    self.prevHash = None
    self.data = data
    self.nonce = 0
    self.timestamp = datetime.datetime.now().isoformat()

  def getHash(self):
    c = str(self.index) + str(self.nonce) + str(self.data) + str(self.timestamp) + str(self.prevHash)
    self.hash = hashlib.sha256(c.encode()).hexdigest()
    return self.hash

  def checkDiff(self, diff):
    for i in range(0, diff):
      if self.hash[i] != "0":
        return False
    return True

  def mine(self, diff):
    print("Mining block " + str(self.index) + "...")
    d = time.time()
    self.getHash()
    while not self.checkDiff(diff):
      self.nonce += 1
      print(self.nonce)
      self.getHash()
    dt = time.time() - d
    print("Mined in " + str(dt) + " " + self.hash)
    return self.hash

class Chain:
  def __init__(self, diff):
    self.diff = diff
    self.blocks = []
    self.number = 0

  def createGenesis(self):
    b = Block("")
    b.index = 0
    b.prevHash = "0"
    b.mine(self.diff)
    self.number += 1
    self.blocks.append(b)

  def addBlock(self, newBlock):
    newBlock.prevHash = self.getPrevHash()
    newBlock.index = self.number
    newBlock.mine(self.diff)
    self.number += 1
    self.blocks.append(newBlock)

  def getPrevHash(self):
    ph = self.blocks[len(self.blocks)-1].getHash()
    return ph

  def isChainValid(self):
    for i in range(0, len(self.blocks)):
      if i == 0:
        prevHash = "0"
      else:
        prevHash = self.blocks[i-1].getHash()

      if self.blocks[i].prevHash != prevHash:
        print("Chain is'nt Valid !")
        return False

      if self.blocks[i].hash != self.blocks[i].getHash():
        print("hash of block " + str(i) + " is wrong")
        return False

      if not self.blocks[i].checkDiff(self.diff):
        print("No proof of work for block " + str(i))
        return False

    print("Chain is Valid !")
    return True

  def printChain(self):
    for b in self.blocks:
      print("--- Block " + str(b.index) + " ---")
      print("|| transactions : " + b.data)
      print("|| hash : " + b.hash)
      print("|| prevHash : " + b.prevHash)
      print("--- END ---\n")


# mining difficulty = 4
c = Chain(4)
c.createGenesis()
c.addBlock(Block("3 to ARthur"))
c.addBlock(Block("5 to Bob"))
c.addBlock(Block("12 to Jean"))
c.addBlock(Block("7 to Jake"))
c.addBlock(Block("2 to Camille"))
c.addBlock(Block("13 to Marth"))
c.addBlock(Block("9 to Felix"))

print(c.isChainValid())

cheater.cheat(c, 1, "6 to jean")

print(c.isChainValid())

c.printChain()


