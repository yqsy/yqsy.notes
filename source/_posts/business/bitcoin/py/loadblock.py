import sys

from blockstruct import *


def main():
    if len(sys.argv) < 2:
        print("usage: loadblock.py *.blk")
        exit(0)

    with open(sys.argv[1], 'rb') as stream:

        while True:
            block = Block(stream)

            if not block.isMagicNoValid():
                break

            print(block)
            print(block.blockHeader)
            print("")

            for i in range(len(block.vtx)):
                tx = block.vtx[i]
                print(tx)

                print("")
                for k in range(len(tx.vin)):
                    print(tx.vin[k])

                print("")
                for j in range(len(tx.vout)):
                    print(tx.vout[j])

            print("")

if __name__ == "__main__":
    main()
