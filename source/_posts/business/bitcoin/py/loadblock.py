import struct
import sys


def peekuint1(stream):
    # bytes to int
    return ord(stream.peek(1)[:1])


def uint1(stream):
    # bytes to int
    return ord(stream.read(1))


def uint2(stream):
    return struct.unpack('H', stream.read(2))[0]


def uint4(stream):
    return struct.unpack('I', stream.read(4))[0]


def uint8(stream):
    return struct.unpack('Q', stream.read(8))[0]


def hash32(stream):
    # return bytes
    return stream.read(32)[::-1]


def time(stream):
    time = uint4(stream)
    return time


def varint(stream):
    size = uint1(stream)

    if size < 0xfd:
        return size
    if size == 0xfd:
        return uint2(stream)
    if size == 0xfe:
        return uint4(stream)
    if size == 0xff:
        return uint8(stream)
    return -1


def hashStr(bytebuffer):
    return ''.join(('%02x' % a) for a in bytebuffer)


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
        str = str + "hashPrevBlock: {0}\n".format(hashStr(self.hashPrevBlock))
        str = str + "hashMerkleRoot: {0}\n".format(hashStr(self.hashMerkleRoot))
        str = str + "nTime: {0}\n".format(self.nTime)
        str = str + "nBits: 0x{0:x}\n".format(self.nBits)
        str = str + "nNonce: {0}".format(self.nNonce)
        return str


class Block:
    def __init__(self, stream):
        self.magicno = uint4(stream)
        self.blockSize = uint4(stream)
        self.blockHeader = BlockHeader(stream)

        self.txcount = varint(stream)
        self.vtx = []

        for i in range(0, self.txcount):
            self.vtx.append(Tx(stream))

    def is_magic_no_valid(self):
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
        self.version = uint4(stream)
        self.dummy = peekuint1(stream)
        self.flags = peekuint1(stream)

        if self.dummy == 0x00 and self.flags == 1:
            # 隔离见证 (不能读取vin 0 vout 1 flag = 0)
            uint1(stream) and uint1(stream)
            self.read_vin(stream)
            self.read_vout(stream)
            for i in range(0, len(self.vin)):
                self.vin[i].scriptwitnesslen = varint(stream)
                self.vin[i].scriptwitness = stream.read(self.vin[i].scriptwitnesslen)
            self.locktime = uint4(stream)
        if self.dummy == 0x00 and self.flags != 1:
            raise Exception("error")
        else:
            # 普通读取
            self.read_vin(stream)
            self.read_vout(stream)
            self.locktime = uint4(stream)

    def read_vin(self, stream):
        self.vin_count = varint(stream)
        self.vin = []
        for i in range(0, self.vin_count):
            self.vin.append(In(stream))

    def read_vout(self, stream):
        self.vout_count = varint(stream)
        self.vout = []
        for i in range(0, self.vout_count):
            self.vout.append(Out(stream))


class In:
    def __init__(self, stream):
        self.prevtxhash = hash32(stream)
        self.prevtxoutidx = uint4(stream)
        self.scriptsiglen = varint(stream)
        self.scriptsig = stream.read(self.scriptsiglen)
        self.sequence = uint4(stream)
        self.scriptwitnesslen = None
        self.scriptwitness = None


class Out:
    def __init__(self, stream):
        self.value = uint8(stream)
        self.outscriptlen = varint(stream)
        self.outscript = stream.read(self.outscriptlen)


def main():
    if len(sys.argv) < 2:
        print("usage: loadblock.py *.blk")
        exit(0)

    with open(sys.argv[1], 'rb') as stream:

        while True:
            block = Block(stream)

            if not block.is_magic_no_valid():
                break

            print(block)
            print(block.blockHeader)
            print("")


if __name__ == "__main__":
    main()
