import random
import string
import sys
    
if (len(sys.argv) != 2):
    print("Usage: python3 passGenerator.py <length>")
    print("Exiting...")
    sys.exit(1)
else:
    try:
        length = int(sys.argv[1])
        if (length < 1 or length > 128):
            print("<length> must be between 1 and 128")
            print("Exiting...")
            sys.exit(1)
    except ValueError:
        print("<length> must be an integer")
        print("Exiting...")
        sys.exit(1)
        
characters = list(string.ascii_letters+string.digits+":,~!@#$%^&*_:,~!@#$%^&*_")
random.shuffle(characters)

passwd = []
for i in range(length):
    passwd.append(random.choice(characters))

print(''.join(passwd))

if __name__ == "__main__":
    pass