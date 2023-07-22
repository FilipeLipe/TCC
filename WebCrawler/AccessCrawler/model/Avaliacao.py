class Avaliacao:
    
    def __init__(self, link):

        self.link = link
        self.titulo = ""
        self.porcentagem = ""
        self.data = ""
        self.tamanho = ""
        self.tempoAvaliacao = ""
        self.secoes = [""]
        self.erros = []
        self.avisos = []

    def to_string(self):
        erros_e_avisos = ""
        max_length = max(len(self.erros), len(self.avisos))

        for i in range(max_length):
            if i < len(self.erros):
                erros_e_avisos += self.erros[i] + ";"
            if i < len(self.avisos):
                erros_e_avisos += self.avisos[i] + ";"

        return self.link +";"+ self.porcentagem +";"+ erros_e_avisos.strip()