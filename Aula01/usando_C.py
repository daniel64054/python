#usar importação para bibliote criada
import ctypes

lib = ctypes.CDLL("./mensagem.so")
lib.mensagem()