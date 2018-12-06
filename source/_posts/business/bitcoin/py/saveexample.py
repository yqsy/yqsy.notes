# int nFile;
# unsigned int nPos;
class DiskBlockPos(object):
    self.nFile = None
    self.nPos = None


# unsigned int nBlocks;      //!< number of blocks stored in file
# unsigned int nSize;        //!< number of used bytes of block file
# unsigned int nUndoSize;    //!< number of used bytes in the undo file
# unsigned int nHeightFirst; //!< lowest height of block in file
# unsigned int nHeightLast;  //!< highest height of block in file
# uint64_t nTimeFirst;       //!< earliest time of block in file
# uint64_t nTimeLast;        //!< latest time of block in file
class BlockFileInfo(object):
    self.nBlocks = None 
    self.nSize = None
    # self.nUndoSize = None
    self.nHeightFirst = None
    self.nHeightLast = None
    self.nTimeFirst = None
    self.nTimeLast = None


# BlockFileInfo vector  
# (索引会持久化到leveldb中,这里不做示范)
vinfoBlockFile = []

# 上一个写入的nFile (文件序号)
nLastBlockFile

def FindBlockPos(nAddSize, nHeight, nTime):
    


# 1. GetSerializeSize 获取存储区块的大小
nBlockSize = 285

nBlockWithPrefixSize = nBlockSize + 8

# 2. FindBlockPos 寻找到存储的位置

