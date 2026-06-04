import random 
  
class JogoDaForca: 
    def __init__(self, palavras): 
        self.palavras = palavras 
        self.palavra_secreta = self._escolher_palavra() 
        self.letras_corretas = [] 
        self.letras_erradas = [] 
        self.tentativas_restantes = 6 # Número de partes do corpo da forca 
        self.estado_forca = [ 
            """  +---+ 
  |   | 
      | 
      | 
      | 
      = 
""", 
            """  +---+ 
  |   | 
  O   | 
      | 
      | 
      = 
""", 
            """  +---+ 
  |   | 
  O   | 
  |   | 
      | 
      = 
""", 
            """  +---+ 
  |   | 
  O   | 
 /|   | 
      | 
      = 
""", 
            """  +---+ 
  |   | 
  O   | 
 /|\  | 
      | 
      = 
""", 
            """  +---+ 
  |   | 
  O   | 
 /|\  | 
 /    | 
      = 
""", 
            """  +---+ 
  |   | 
  O   | 
 /|\  | 
 / \  | 
      = 
""" 
        ] 
  
    def _escolher_palavra(self): 
        return random.choice(self.palavras).upper() 
  
    def _exibir_palavra_escondida(self): 
        exibicao = "" 
        for letra in self.palavra_secreta: 
            if letra in self.letras_corretas: 
                exibicao += letra + " " 
            else: 
                exibicao += "_ " 
        return exibicao.strip() 
  
    def _desenhar_forca(self): 
        print(self.estado_forca[6 - self.tentativas_restantes]) 
  
    def jogar(self): 
        print("\n--- Jogo da Forca --- ") 
        print("Adivinhe a palavra!") 
  
        while self.tentativas_restantes > 0: 
            self._desenhar_forca() 
            print(f"Palavra: {self._exibir_palavra_escondida()}") 
            print(f"Letras erradas: {', '.join(self.letras_erradas)}") 
            print(f"Tentativas restantes: {self.tentativas_restantes}") 
  
            tentativa = input("Digite uma letra: ").upper() 
  
            if len(tentativa) != 1 or not tentativa.isalpha(): 
                print("Entrada inválida. Digite apenas uma letra.") 
                continue 
  
            if tentativa in self.letras_corretas or tentativa in self.letras_erradas: 
                print(f"Você já tentou a letra '{tentativa}'.") 
                continue 
  
            if tentativa in self.palavra_secreta: 
                self.letras_corretas.append(tentativa) 
                print(f"Boa! A letra '{tentativa}' está na palavra.") 
            else: 
                self.letras_erradas.append(tentativa) 
                self.tentativas_restantes -= 1 
                print(f"Que pena! A letra '{tentativa}' não está na palavra.") 
  
            if "_" not in self._exibir_palavra_escondida(): 
                print("\nParabéns! Você adivinhou a palavra!") 
                print(f"A palavra era: {self.palavra_secreta}") 
                self._desenhar_forca() 
                break 
        else: 
            self._desenhar_forca() 
            print("\nGAME OVER! Você ficou sem tentativas.") 
            print(f"A palavra secreta era: {self.palavra_secreta}") 
  
# Lista de palavras para o jogo 
palavras_forca = ["CASA", "LASANHA", "SATURNO", "DAZAI", 
"GATO", "NIETZSCHE", "PYTHON", "FUTEBOL", "MONTANHA", "CACHORRO"] 
jogo = JogoDaForca(palavras_forca) 
jogo.jogar()