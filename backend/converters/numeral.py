import numbersystem as nt

conver=["bin","hexa","octa"]


def numiral_system(value:int, op:str):

    if op.lower()==conver[0].lower():
        return nt.decimalToBinary(value)

    elif op.lower()==conver[1].lower():
        return nt.decimalToHexa(value)

    elif op.lower()==conver[2].lower():
        return nt.decimalToOctal(value)

if __name__=="__main__":
    x=numiral_system(12,"bin")
    print(x)