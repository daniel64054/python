from class_conta_bancaria import ContaBancaria


class ContaCorrente(ContaBancaria):
    def __init__(self):
        self.__limite = 0.0

    def Abrirconta(self,nb=0,na=0,nc="",Titular="",saldo=0,limite=0.0):
        self._nbanco =nb
        self._nangencia =na
        self._nconta =nc
        self._titular = Titular
        self._saldo = saldo
        self.__limite= limite
        print("A conta "+self._nconta+"do sr(a) "+self._titular+"foi aberta")

    def Sacar(self,valor):
        if(valor > self._saldo+self.__limite):
            print("Saldo insuficiente")
        elif(valor >= self._saldo):
            self._saldo -= valor
            print("Você relizou um saque de "+str(valor)+"seu saldo atual  é "+str(self._saldo))
        else:
            sobra = valor - self._saldo
            self.__limite -= sobra
            self._saldo = 0
            print("Um saque de "+str(valor)+" feito tirando do limite.\n Saldo atual: "+str(self._saldo)+"\nLimite atual"+str(self.__limite)) 
            