
import re
import main
links_pdf = set()

def valida_link(links_processados: set(), links_com_erro: set(), link: str) -> bool:
    
    if link is None:    
        return False
    
    #INVALIDO
    regex_extensoes = re.compile(r"\.(css|gif|js|png|jpg|php|jpeg|doc|docx|xlsx|xml|zip|rar|pptx|ppt|xls|txt|htm|mp4|)$", re.IGNORECASE)
    regex_palavras = re.compile(r"(wp-json|jcarousel|ajax|wp-content|ufopa|adufop|.xml|soc)", re.IGNORECASE)
    regex_autenticacao = re.compile(r"(minha.ufop|minhaufop|proad|user|moodle)", re.IGNORECASE)
    regex_rede_social = re.compile(r"(facebook|instagram|google|twitter|linkedin|pinterest|wordpress|github|webmail|pesquisa@ufop|youtube)", re.IGNORECASE)
    regex_downloads = re.compile(r"(export|download)", re.IGNORECASE)

    calendario = "dia|day|mes|month|ano|year|semana|week|calendario|calendar|"
    noticias = "noticias|news|eventos|evento|event|jornal|blog|publications|"
    repetitivos = "repositorio|editais|edital|resolucao|monografias|editora|article|periodicos|resolucao|archive|academia|tag|mostrar|dados|files|"
    pesados = "revistacuringa|imobilis|tv.ufop|radio"

    regex_absurdos = re.compile(r"("+calendario + noticias + repetitivos + pesados +")", re.IGNORECASE)
    regex_openScholar = re.compile(r"(quick_tabs_sidebar|front)", re.IGNORECASE)
    regex_barra_dupla = re.compile(r"\\\\")

    #VALIDO
    regex_ufop = re.compile(r""+main.dominio, re.IGNORECASE)
    regex_http_https = re.compile(r"https?://", re.IGNORECASE)
    regex_pdf = re.compile(r"\.pdf", re.IGNORECASE)

    if regex_ufop.search(link) and regex_http_https.search(link):
        if not (regex_extensoes.search(link) or regex_palavras.search(link) or regex_barra_dupla.search(link) or regex_autenticacao.search(link) or regex_absurdos.search(link) or regex_openScholar.search(link) or regex_rede_social.search(link) or regex_downloads.search(link)):
            if regex_pdf.search(link):
                #Tratar link que é pdf
                return False
            
            if link not in links_processados and link not in links_com_erro:
                return True
   
    return False


