import os
import sys
import base64

def main():
    endcap = (chr(333) + chr(232) + chr(292) + chr(696)).encode('utf-8')
    print(endcap)

    files = sys.argv[2:]
    out = open(sys.argv[1]+'.mdbl', 'wb')
    outbin = b''
    for file in files:
        ascii85Str = base64.a85encode(open(file, 'rb')) + endcap
        outbin += ascii85Str
    out.write(outbin)
    out.close()

if __name__ == '__main__':
    main()
