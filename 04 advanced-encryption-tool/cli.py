import argparse
from encrypt import encrypt_file
from decrypt import decrypt_file

parser = argparse.ArgumentParser(description="Advanced Encryption Tool")

parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Mode")
parser.add_argument("file", help="File path")
parser.add_argument("password", help="Password")

args = parser.parse_args()

if args.mode == "encrypt":
    encrypt_file(args.file, args.password)
elif args.mode == "decrypt":
    decrypt_file(args.file, args.password)