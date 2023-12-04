def caesar(s, k, decode = False):
	if decode: k = 26 - k
	return "".join([chr((ord(i) - 65 + k) % 26 + 65)
				for i in s.upper()
				if ord(i) >= 65 and ord(i) <= 90 ])


def repeat(f,n):
  for i in range(n):
    f();

def procedure():
  print("Example");


import  os 
# diretório atual 
def remover(os . remova) :
def remover(os . rmdir) :
