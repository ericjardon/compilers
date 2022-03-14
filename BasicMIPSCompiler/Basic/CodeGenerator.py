MIPS_TYPES = {
    'int':'.word'
}


def printInti(n:int):
    # immediate int
    printInstruction('li', args=['$v0', 1])
    printInstruction('lw', args=[n])
    printInstruction('syscall')


def printInt(name:str):
    # labeled int
    printInstruction('li', args=['$v0', 1])
    printInstruction('lw', args=[name])
    printInstruction('syscall')

def printAssignment(id, value=None, type='int'):
    printLabel(id, value, type)

def printReAssignment(id:str, newvalue:int):
    # Assumes id points to an int (.word)
    # printInstruction('lw', ['$a0', id])  #get current value
    printInstruction('la', ['$a0', id])       # get address
    printInstruction('li', ['$a1', newvalue])    # new val
    printInstruction('sw', ['$a1', '0($a0)'])    # save new value
    
    # lw $a2, globalVariable  #get new value
    # https://stackoverflow.com/questions/45686296/how-to-modify-data-values-inside-the-text-segment-in-mips

def printDataSegment(memory):
    print('.data')
    for key, val in memory.items():
        printLabel(key, val)

def printLabel(id, value=None, type='int'):
    value = '' if value is None else value
    line = '\t' + f'{id}:' + '\t' + MIPS_TYPES[type] + ' ' + str(value)
    print(line)

def printInstruction(inst:str, args:list=[], tabs:int=1):
    line = '\t'*tabs + inst + ','.join(args[:-1]) + args[-1]
    print(line)


def printString(s:str):
    raise NotImplementedError
    args = ['$a0', s]
    printInstruction('la', args)
    