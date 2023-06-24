
import re

links_pdf = set()

def valida_link(link: str) -> bool:
    
    if link is None:    
        return False
    
    #INVALIDO
    regex_extensoes = re.compile(r"\.(css|gif|js|png|jpg|php|jpeg|doc|docx|xlsx)$", re.IGNORECASE)
    regex_palavras = re.compile(r"(wp-json|jcarousel|ajax|wp-content|revistacuringa)", re.IGNORECASE)
    regex_autenticacao = re.compile(r"(minha.ufop|minhaufop|proad|facebook|instagram|play.google)", re.IGNORECASE)
    regex_barra_dupla = re.compile(r"\\\\")

    #VALIDO
    regex_ufop = re.compile(r"\.ufop", re.IGNORECASE)
    regex_pdf = re.compile(r"\.pdf", re.IGNORECASE)
    regex_http_https = re.compile(r"https?://", re.IGNORECASE)


    if regex_ufop.search(link) and regex_http_https.search(link):
        if regex_extensoes.search(link) or regex_palavras.search(link) or regex_barra_dupla.search(link) or regex_autenticacao.search(link):
            return False
        else:
            if regex_pdf.search(link):
                #Tratar link que é pdf
                return False
            
            return True
    else:
        return False


