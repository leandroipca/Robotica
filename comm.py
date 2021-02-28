

def formMSG(msg, idMsg):
    READVARIABLE = 0

    varNameLen = len(msg)
    hByte1 = (varNameLen & 0xff00) >> 8
    lByte1 = (varNameLen & 0x00ff)

    bl = (READVARIABLE).to_bytes(1, 'big') + (hByte1).to_bytes(1, 'big') + (lByte1).to_bytes(1, 'big')
    blo = bytearray(msg, 'utf-8')
    bloc = bl + blo


    lunghezza = len(bloc)

    hByte = (lunghezza & 0xff00) >> 8
    lByte = (lunghezza & 0x00ff)

    hByteMsg = (idMsg & 0xff00) >> 8
    lByteMsg = (idMsg & 0x00ff)
    he = (hByteMsg).to_bytes(1, 'big') + (lByteMsg).to_bytes(1, 'big') + (hByte).to_bytes(1, 'big') + (lByte).to_bytes(
        1, 'big')
    bfinal = he + bloc
    print("aqui")
    print(str(bfinal))
    return bfinal


def formMSG2(msg, value, idMsg):

    WRITEVARIABLE = 1

    varNameLen = len(msg)
    hByte1 = (varNameLen & 0xff00) >> 8
    lByte1 = (varNameLen & 0x00ff)



    bl = (WRITEVARIABLE).to_bytes(1, 'big') + (hByte1).to_bytes(1, 'big') +(lByte1).to_bytes(1, 'big')
    blo = bytearray(msg, 'utf-8')
    bloc = bl + blo


    varValueLen = len(value)
    hByte2 = (varValueLen & 0xff00) >> 8
    lByte2 = (varValueLen & 0x00ff)

    b2 = (hByte2).to_bytes(1, 'big') + (lByte2).to_bytes(1, 'big')
    blo2 = bytearray(value, 'utf-8')
    bloc = bloc + b2 + blo2



    lunghezza = len(bloc)

    hByte = (lunghezza & 0xff00) >> 8
    lByte = (lunghezza & 0x00ff)

    hByteMsg = (idMsg & 0xff00) >> 8
    lByteMsg = (idMsg & 0x00ff)
    he = (hByteMsg).to_bytes(1, 'big') + (lByteMsg).to_bytes(1, 'big') + (hByte).to_bytes(1, 'big') + (lByte).to_bytes(1, 'big')
    bfinal = he + bloc
    print("aqui")
    print(str(bfinal))

    return bfinal

def clearMsg(msg):
    lenValue = msg[5]<<8 | msg[6]
    value = msg[7:7+lenValue]

    v = str(value)
    f = v.replace('b','')
    f = f.replace("'", "")
    print(f)

    return f


