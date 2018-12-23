import os
import sys

from impl.block import *


def main():
    if len(sys.argv) < 2:
        print("usage: iterversion.py {basedirectory}")
        exit(0)

    nVersions = []

    for i in range(2000):
        fileName = "{0}/blk{1:05d}.dat".format(sys.argv[1], i)

        try:
            with open(fileName, 'rb') as stream:
                while True:
                    if stream.tell() == os.fstat(stream.fileno()).st_size:
                        break

                    block = Block(stream)

                    if block.isMagicZero():
                        break
                    if not block.isMagicNoValid():
                        raise Exception("error")

                    if block.blockHeader.nVersion not in nVersions:
                        nVersions.append(block.blockHeader.nVersion)

            print("{0} => {1}".format(fileName, nVersions))

        except IOError:
            break


if __name__ == "__main__":
    main()
