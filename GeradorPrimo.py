from random import randrange, getrandbits

class GeradorNumeroPrimo:
    def __init__(self):
        self.nprimo = self.geradorprimo()

    #Teste Miller Rabin, descobrir se o número é primo ou não
    def MRabin(self,n, qtdteste=200):
       
       #Teste de casos, validando os mesmos
        if n < 6:
            return [False, False, True, True, False, True][n]
        
        # Verifica N = par
        if n <= 1 or n % 2 == 0:
            return False
            
        # Achar r/s > fórmula(MRabin): (n-1) = r * (2^s) 
        s = 0
        r = n - 1
        while r & 1 == 0:
            s += 1
            r //= 2
        
        for _ in range(qtdteste):
            a = randrange(2, n - 1)
            x = pow(a, r, n)
            if x != 1 and x != n - 1:
                j = 1
                while j < s and x != n - 1:
                    x = pow(x, 2, n)
                    if x == 1:
                        return False
                    j += 1
                if x != n - 1:
                    return False
        return True

    def geradorcandidatoprimo(self,length):
        
        self.nprimo = getrandbits(length)
        self.nprimo |= (1 << length - 1) | 1
        return self.nprimo

    def geradorprimo(self,length=6):
       
        self.nprimo  = 10

        while not self.MRabin(self.nprimo, 200):
            self.nprimo  = self.geradorcandidatoprimo(length)
        return self.nprimo