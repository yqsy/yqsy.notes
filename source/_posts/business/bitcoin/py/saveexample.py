# int nFile;
# unsigned int nPos;
class DiskBlockPos(object):
    nFile = 0
    nPos = 0

# unsigned int nBlocks;      //!< number of blocks stored in file
# unsigned int nSize;        //!< number of used bytes of block file
# unsigned int nUndoSize;    //!< number of used bytes in the undo file
# unsigned int nHeightFirst; //!< lowest height of block in file
# unsigned int nHeightLast;  //!< highest height of block in file
# uint64_t nTimeFirst;       //!< earliest time of block in file
# uint64_t nTimeLast;        //!< latest time of block in file
class BlockFileInfo(object):
    nBlocks = 0
    nSize = 0
    # nUndoSize = 0
    nHeightFirst = -1
    nHeightLast = -1
    nTimeFirst = -1
    nTimeLast = -1

    def addblock(nHeight, nTime):
        if (self.nBlocks == 0 or self.nHeightFirst > nHeight):
            self.nHeightFirst = nHeight
        if (self.nBlocks == 0 or self.nTimeFirst > nTime):
            self.nTimeFirst = nTime
        self.nBlocks += 1
        if (nHeight > self.nHeightLast):
            self.nHeightLast = nHeight
        if (nTime > self.nTimeLast):
            self.nTimeLast = nTime
        

# BlockFileInfo vector  
# (索引会持久化到leveldb中,这里不做示范)
vinfoBlockFile = []

# 上一个写入的nFile (文件序号)
nLastBlockFile = 0


MAX_BLOCKFILE_SIZE = 0x8000000 # 128 MiB
BLOCKFILE_CHUNK_SIZE = 0x1000000 # 16 MiB
def FindBlockPos(nAddSize, nHeight, nTime):
    nFile = nLastBlockFile
    if len(vinfoBlockFile) <= nFile:
        vinfoBlockFile.append(BlockFileInfo())

    # 这个判断应该是 > 吧, 不然不能够存储满128MiB了
    while(vinfoBlockFile[nFile].nSize + nAddSize >= MAX_BLOCKFILE_SIZE):
        nFile += 1
        if len(vinfoBlockFile) <= nFile:
            vinfoBlockFile.append(BlockFileInfo())
        pos.nFile = nFile
        pos.nPos = vinfoBlockFile[nFile].nSize

    if (nFile != nLastBlockFile):
        print("nLastBlockFile changed")
        nLastBlockFile = nFile

    vinfoBlockFile[nFile].addblock(nHeight, nTime)
    vinfoBlockFile[nFile].nSize += nAddSize

    nOldChunks = (pos.pos + BLOCKFILE_CHUNK_SIZE - 1) / BLOCKFILE_CHUNK_SIZE




# 1. GetSerializeSize 获取存储区块的大小
nBlockSize = 285

nBlockWithPrefixSize = nBlockSize + 8

# 2. FindBlockPos 寻找到存储的位置

