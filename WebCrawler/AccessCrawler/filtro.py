
import re
import main
links_pdf = set()

def valida_link(links_processados: set(), links_com_erro: set(), link: str) -> bool:
    
    if link is None:    
        return False
    
    #INVALIDO
    regex_extensoes = re.compile(r"\.(css|gif|js|png|jpg|php|jpeg|doc|docx|xlsx)$", re.IGNORECASE)
    regex_palavras = re.compile(r"(wp-json|jcarousel|ajax|wp-content)", re.IGNORECASE)
    regex_autenticacao = re.compile(r"(minha.ufop|minhaufop|proad|user)", re.IGNORECASE)
    regex_rede_social = re.compile(r"(facebook|instagram|google|twitter|linkedin|pinterest|wordpress)", re.IGNORECASE)
    regex_absurdos = re.compile(r"(calendario|radio|revistacuringa|eventos|noticias|repositorio|editais|edital|event|monografias|dados|calendar|editora|files|article|periodicos|tv.ufop|archive)", re.IGNORECASE)
    regex_openScholar = re.compile(r"(quick_tabs_sidebar|front)", re.IGNORECASE)
    regex_barra_dupla = re.compile(r"\\\\")

    #VALIDO
    regex_ufop = re.compile(r""+main.dominio, re.IGNORECASE)
    regex_http_https = re.compile(r"https?://", re.IGNORECASE)
    regex_pdf = re.compile(r"\.pdf", re.IGNORECASE)

    if regex_ufop.search(link) and regex_http_https.search(link):
        if not (regex_extensoes.search(link) or regex_palavras.search(link) or regex_barra_dupla.search(link) or regex_autenticacao.search(link) or regex_absurdos.search(link) or regex_openScholar.search(link) or regex_rede_social.search(link)):
            if regex_pdf.search(link):
                #Tratar link que é pdf
                return False
            
            if link not in links_processados and link not in links_com_erro:
                return True
   
    return False


