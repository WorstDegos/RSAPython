class Criptografia (object):
    #conferir essas crip e descrip e adicionar descrição
    def criptografia(self, m, e, n):
        c = (m**e) % n
        return c

    def descriptografia(self, c, d, n):
        m = c**d % n
        return m

    def codifica_msg(self):
        msg = input("Digite o texto a ser encriptografado:   ")
        print("\nDigite os valores da Chave Pública :  ")
        e = int(input("Chave e: "))
        n = int(input("Chave n: ")) 
        #enc = começa a criptografar letra por letra atráves do X, o X representa cada letra baseado na tabela ASCII
        enc = "".join(chr(self.criptografia(ord(x), e, n)) for x in msg)
        print("\nTexto Criptografado: ", enc, '\n')
        return enc
        
        
    def decodifica_msg(self, msg):
        self.msg = msg
        print("Digite os valores da Chave Privada: ")
        d = int(input("Chave d: "))
        n = int(input("Chave n: ")) 
        dec = "".join(chr(self.descriptografia(ord(x), d, n)) for x in msg)
        return print("Texto Descriptografado: ", dec, '\n')