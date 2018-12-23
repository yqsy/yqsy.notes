from datetime import datetime
from serialize import *
from script import *

# 区块结构体解析

class BlockHeader:
    def __init__(self, stream):
        self.nVersion = uint4(stream)
        self.hashPrevBlock = hash32(stream)
        self.hashMerkleRoot = hash32(stream)
        self.nTime = uint4(stream)
        self.nBits = uint4(stream)
        self.nNonce = uint4(stream)

    def __str__(self):
        str = "nVersion: 0x{0:x}\n".format(self.nVersion)
        str = str + "hashPrevBlock: 0x{0}\n".format(hashStr(self.hashPrevBlock))
        str = str + "hashMerkleRoot: 0x{0}\n".format(hashStr(self.hashMerkleRoot))
        str = str + "nTime: {0}\n".format(self.decodeTime(self.nTime))
        str = str + "nBits: 0x{0:x}\n".format(self.nBits)
        str = str + "nNonce: {0}".format(self.nNonce)
        return str

    def decodeTime(self, time):
        utcTime = datetime.utcfromtimestamp(time)
        return utcTime.strftime("%Y-%m-%d %H:%M:%S.%f+00:00 (UTC)")


class Block:
    def __init__(self, stream):
        self.magicno = uint4(stream)
        self.blockSize = uint4(stream)
        self.blockHeader = BlockHeader(stream)

        self.txcount = varint(stream)
        self.vtx = []

        for i in range(0, self.txcount):
            self.vtx.append(Tx(stream))

    def isMagicNoValid(self):
        if self.magicno == 0xD9B4BEF9:
            return True
        else:
            return False

    def __str__(self):
        str = "blocksize: {0}\n".format(self.blockSize)
        str = str + "txcount: {0}".format(self.txcount)
        return str


class Tx:
    def __init__(self, stream):
        self.nVersion = uint4(stream)
        self.dummy = peekuint1(stream)
        self.flags = peekuint1(stream)

        if self.dummy == 0x00 and self.flags == 1:
            # 隔离见证 (不能读取vin 0 vout 1 flag = 0)
            uint1(stream) and uint1(stream)
            self.readVin(stream)
            self.readVout(stream)
            for i in range(0, len(self.vin)):
                self.vin[i].scriptWitnesslen = varint(stream)
                self.vin[i].scriptWitness = stream.read(self.vin[i].scriptWitnesslen)
            self.nLockTime = uint4(stream)
        if self.dummy == 0x00 and self.flags != 1:
            raise Exception("error")
        else:
            # 普通读取
            self.readVin(stream)
            self.readVout(stream)
            self.nLockTime = uint4(stream)

    def readVin(self, stream):
        self.vinCount = varint(stream)
        self.vin = []
        for i in range(0, self.vinCount):
            self.vin.append(In(stream))

    def readVout(self, stream):
        self.voutCount = varint(stream)
        self.vout = []
        for i in range(0, self.voutCount):
            self.vout.append(Out(stream))

    def isWitness(self):
        return self.dummy == 0x00 and self.flags == 1

    def __str__(self):
        str = "nVersion: 0x{0:x}\n".format(self.nVersion)
        str = str + "vincount:{0}\n".format(len(self.vin))
        str = str + "voutcount: {0}\n".format(len(self.vout))
        str = str + "nLockTime: {0}\n".format(self.nLockTime)
        str = str + "--witness: {0}".format(self.isWitness())
        return str


class In:
    def __init__(self, stream):
        self.prevouthash = hash32(stream)
        self.preoutn = uint4(stream)
        self.scriptSiglen = varint(stream)
        self.scriptSig = stream.read(self.scriptSiglen)
        self.nSequence = uint4(stream)
        self.scriptWitnesslen = None
        self.scriptWitness = None

    def __str__(self):
        str = "prevout 0x{0} {1}\n".format(hashStr(self.prevouthash), self.preoutn)
        str = str + "scriptSiglen: {0}\n".format(self.scriptSiglen)
        str = str + "scriptSig: {0}\n".format(scriptToAsmStr(self.scriptSig))
        str = str + "nSequence: 0x{0:x}\n".format(self.nSequence)
        str = str + "scriptWitnesslen: {0}".format(self.scriptWitnesslen)
        return str


class Out:
    def __init__(self, stream):
        self.nValue = uint8(stream)
        self.scriptPubkeylen = varint(stream)
        self.scriptPubkey = stream.read(self.scriptPubkeylen)

    def valueFromAmount(self, amount):
        COIN = 100000000
        sign = amount < 0
        abs = 0 - amount if sign else amount
        quotient = int(abs / COIN)
        remainder = int(abs % COIN)
        return "{0:s}{1:d}.{2:d}".format("-" if sign else "", quotient, remainder)

    def __str__(self):
        str = "nValue {0}\n".format(self.valueFromAmount(self.nValue))
        str = str + "scriptPubkeylen: {0}\n".format(self.scriptPubkeylen)
        str = str + "scriptPubkey: {0}".format(scriptToAsmStr(self.scriptPubkey))
        return str
