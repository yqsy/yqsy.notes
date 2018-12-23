
from io import BytesIO

from impl.serialize import *

# * The block header
# * The height.
# * The number of transactions.
# * To what extent this block is validated.
# * In which file, and where in that file, the block data is stored.
# * In which file, and where in that file, the undo data is stored.
class DBBlockIndex():
    def __init__(self, blkHash, rawHex):
        self.hash = blkHash

