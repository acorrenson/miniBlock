from cheater import *
from main import *

# new Chain instance with
# mining difficulty = 4
c = Chain(4)
c.createGenesis()

# simulate transactions
c.addBlock(Block("3$ to Arthur"))
c.addBlock(Block("5$ to Bob"))
c.addBlock(Block("12$ to Jean"))
c.addBlock(Block("7$ to Jake"))
c.addBlock(Block("2$ to Camille"))
c.addBlock(Block("13$ to Marth"))
c.addBlock(Block("9$ to Felix"))

# chech chain validity
c.isChainValid()

# fake transaction
cheat(c, 1, "6 to jean")

# check chain validity
c.isChainValid()

# print all blocks
c.printChain()

print("len", len(c.blocks[0].hash) + 15)
