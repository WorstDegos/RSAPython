from cripto import Criptografia

class Chaves(Criptografia):
   
    def __init__(self, p, q):
        self.p = p
        self.q = q

    # N = p * q
    #Phiφ (n = (p-1)*(q-1))
    def geradorchave(self):
        n = self.p*self.q
        funcphi = (self.p-1)*(self.q-1)  

        #Chave Publica - MDC(φ(n), e) = 1, e > 1, e < φ(n)
        print(str(self.coprimos(funcphi)) + "\n") 
        print("Escolha uma chave pública:\n")
        e=int(input())
        
        #Chave Privada - 1 = d * e - ( r * φ(n) ) 
        d = self.inversomultiplicativo(e,funcphi) 
        return print("\nChave Pública (e=" + str(e) + ", n=" + str(n) + ")" + "\nChave Privada (d=" + str(d) + ", n=" + str(n) + ")\n")

    def mdc(self, a, b):
        while a != 0:
            a, b = b % a, a
        return b

    #Inverso Multiplicativo descobrir como é o coprimo de φ(n)

    def inversomultiplicativo(self, a, m): 
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        
        
    def coprimos(self, a):
        l = []
        for x in range(2, a): 
            if self.mdc(a, x) == 1 and self.inversomultiplicativo(x,a) != None:
                l.append(x)
        for x in l:
            if x == self.inversomultiplicativo(x,a):
                l.remove(x)
        return l

