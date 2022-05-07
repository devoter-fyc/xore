# py xore.py fromfile password(0~255) tofile
import argparse,sys
def cli_main():
    argp = argparse.ArgumentParser(prog="xore",description="Xor encryption")
    argp.add_argument("-eod","--encrypt-or-decrypt",nargs="+",dest="enc")
    args = argp.parse_args()
    if len(args.enc) != 3: raise ValueError("You should use enough args");exit(1)
    fw = open(args.enc[2],'wb');f = open(args.enc[0],'rb')
    try:
        while True:
            tmpb = f.read(1)
            if not tmpb : break
            tmpw = int.from_bytes(tmpb,"big") ^ int(args.enc[1])
            fw.write(tmpw.to_bytes(1,"big",signed=False))
    finally:
        f.close();fw.close();print("LOG");print("Program exiting...")
    return 0
if 1 <= len(sys.argv) <= 5:
    cli_main()
else:
    raise RuntimeError("Invalid arguments")