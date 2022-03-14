MIPS_TYPES = {
    'int':'.word'
}

RESULT_REGISTER = '$t0'


def printInti(n:int):
    # immediate int
    printInstruction('li', args=['$v0', 1])
    printInstruction('lw', args=[n])
    printInstruction('syscall')

def printTextSegment():
    print('.text')

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
    printInstruction('li', ['$a1', RESULT_REGISTER])    # new val in v0
    printInstruction('sw', ['$a1', '0($a0)'])    # save new value
    
    # lw $a2, globalVariable  #get new value
    # https://stackoverflow.com/questions/45686296/how-to-modify-data-values-inside-the-text-segment-in-mips

def printMul(left:int, right:int):
    # left and right are evaluated ints
    # load immediates to t1 and t2
    loadValues(left, right)
    printInstruction('mul', [RESULT_REGISTER, left, right])
    

def printDiv(left:int, right:int):
    loadValues(left, right)
    printInstruction('div', [RESULT_REGISTER, left, right])


def printAdd(left:int, right:int):
    loadValues(left, right)
    printInstruction('addu', [RESULT_REGISTER, left, right])

def printSub(left:int, right:int):
    loadValues(left, right)
    printInstruction('subu', [RESULT_REGISTER, left, right])


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

def loadValues(left, right):
    # li versus move depends on whether we copy a value or load an immediate value
    printInstruction('li', ['$t1', left])
    printInstruction('li', ['$t2', right])

def printString(s:str):
    raise NotImplementedError
    args = ['$a0', s]
    printInstruction('la', args)
    