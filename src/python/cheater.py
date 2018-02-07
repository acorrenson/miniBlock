def cheat(chain, index, newData):
  chain.blocks[index].data = newData
  chain.blocks[index].mine(chain.diff)

  for i in range(index, len(chain.blocks)):
    print("Cheating block " + str(i))
    a = chain.blocks[i].mine(chain.diff)
    if i < len(chain.blocks)-1:
      chain.blocks[i+1].prevHash = a