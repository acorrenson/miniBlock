# miniBlock
A mini blockchain in python

# exemple

Here is a little exemple

```Python
# create a new BlockChain with difficulty 4
chain = Chain(4)

# add a new block containing the transactions :
# "3 from Bob to Claris"
# "2 from Claris to Jean"
chain.addBlock( Block("3 from Bob to Claris, 2 from Claris to Jean") )

# check validity
chain.isChainValid()
# true

# let's try to modify the chain
chain.blocks[0].transaction = "9 from Bob to Claris, 9 from Claris to Jean"
chain.blocks[0].mine(chain.diff)

# check validity again
chain.isChainValid()
# false
```

# doc

## Block(data)

Block class.

+ parameters :
  - data : `string` <= transactions stored in the block
+ fields
  - index: `int` index of the block
  - hash: `string` hash of the block
  - prevHash: `string` hash of the previous block
  - data: `string` transactions written in the block
  - nonce: `int` nonce (to mine)
  - timestamp: `string` date of creation
+ methods
  - getHash: `string`
  - checkDiff: `boolean`
  - mine: `string`

### Block.getHash()

Calculate the hahs according to :
self.index,
self.nonce,
self.data,
self.prevHash,
self.timestamp

+ parameters : none
+ return : `string` => self.hash

### Block.checkDiff(diff)

Check if the hash matches with the difficulty

+ parameters:
  - diff : `int` <= number of 0 needed at the begining of the hash
+ return : `string` => self.hash

### Block.mine(diff)

Increment the nonce to have a valid hash (according to a specific difficulty)

+ parameters:
  - diff : `int` <= number of 0 needed at the begining of the hash
+ return : `string` => self.hash

## Chain(diff)

Chain class (block container)

+ parametres : 
  - diff : `int` difficulty to mine a block
+ fields :
  - diff : `int` difficulty to mine a block
  - blocks : `array` container for all blocks
  - number : `int` actual number of blocks
+ methods :
  - createGenesis : `none`
  - addBlock: `none`
  - getPrevHash : `none`
  - isChainValid : `boolean`
  - printChain : `none`

### Chain.createGenesis()

Init the chain with a genesis block

+ parameters : none
+ return : none

### Chain.addBlock(block)

Add a new block to the chain. (it mines the block before)

+ parameters : 
  - block : `Block`
+ return : none

### Chain.getPrevHash()

Compute hash of the last block and return it.

+ parameters : none
+ return : `string` => hash of the last block

### Chain.isChainValid()

Check if all blocks match the difficulty and if all blocks have a valid hash.

+ parameters : none
+ return : `boolean`

### Chain.printChain()

Display all blocks of the chain in the console.

+ parameters : none
+ return : none

# Cheater

Just to have fun, we can try to cheat the chain with the *cheater* module.

## cheat(chain, index, blockData)

Replace data in a specific block and reset hashs to have a valid chain again.

+ parameters : 
  - chain : `Chain` <= chain to modify
  - index : `int` <= index of the targeted block
  - blockData : `string` <= fake data to change
+ return : none

## exemple

```Python
chain = Chain(4)

# add a new block containing the transactions :
# "3 from Bob to Claris"
# "2 from Claris to Jean"
chain.addBlock( Block("3 from Bob to Claris, 2 from Claris to Jean") )

# check validity
chain.isChainValid()
# TRUE

# let's try to modify the chain
cheat(chain, 0, "9 from Bob to Claris, 9 from Claris to Jean")

# check validity again
chain.isChainValid()
# TRUE <= success
```


