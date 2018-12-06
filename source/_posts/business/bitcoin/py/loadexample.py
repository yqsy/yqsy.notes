# int32_t nVersion;
# uint256 hashPrevBlock;
# uint256 hashMerkleRoot;
# uint32_t  nTime;
# uint32_t nBits;
# uint32_t nNonce;
# std::vector<CTransactionRef> vtx;
class Block(object):
    self.nVersion = None
    self.hashPrevBlock = None
    self.hashMerkleRoot = None
    self.nTime = None
    self.nBits = None
    self.nNonce = None

    self.vtx = None


# basic
# int32_t nVersion
# std::vector<CTxIn> vin
# std::vector<CTxOut> vout
# uint32_t nLockTime

# witness (隔离见证)
# int32_t nVersion
# unsigned char dummy = 0x00  **
# unsigned char flags (!= 0)  **
# std::vector<CTxIn> vin
# std::vector<CTxOut> vout
# if (flags & 1):
#   CTxWitness wit;           **
# uint32_t nLockTime

class Transaction(object):
    self.nVersion = None
    self.vin = None
    self.vout = None
    self.nLockTime = None

    # self.dummy = None
    # self.flags = None
    # 序列化时输出到磁盘上是放在最末尾的
    # 但是反序列化时将隔离见证数据返还到每一个TxIn内
    # self.wit = None

# COutPoint prevout;
# CScript scriptSig; prevector
# uint32_t nSequence;
# CScriptWitness scriptWitness; std::vector<std::vector<unsigned char> > stack;
class TxIn(object):
    self.prevout = None
    self.scriptSig = None
    self.nSequence = None
    self.scriptWitness = None

# uint256 hash;
# uint32_t n;
class COutPoint(object):
    self.hash = None
    self.n = None

# CAmount nValue;  int64_t
# CScript scriptPubKey; prevector
class TxOut(object):
    self.nValue = None
    self.scriptPubKey = None



    
