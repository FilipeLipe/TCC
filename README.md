# TCC
Desenvolvimento do meu TCC

\section{Estrutura do Projeto}\label{sec:LABEL_CHP_1_SEC_A}

O projeto tem a estrutura de diretórios e arquivos conforme pode ser visto na figura abaixo:

\begin{lstlisting}[style=codestyle]
- arquivosTXT/
  - links_encontrados.txt
  - links_processados.txt
  - links_com_erro.txt
  - html_link_verificado.txt
- encontrar_links.py
- filtro.py
- main.py
- arquivos.py
- processar_links.py
\end{lstlisting}

O links\_encontrados se refere a todos .... 



\section{Instalação}\label{sec:LABEL_CHP_1_SEC_A}
Certifique-se de que o Python esteja instalado em seu sistema.
Instale as bibliotecas externas requests, BeautifulSoup e re, caso ainda não estejam instaladas, utilizando o gerenciador de pacotes pip. Você pode fazê-lo executando o seguinte comando no terminal:

\begin{lstlisting}[style=codestyle]
pip install requests beautifulsoup4
\end{lstlisting}



\section{Uso}\label{sec:LABEL_CHP_1_SEC_A}

Antes de executar o programa, é necessário realizar algumas configurações iniciais:

\begin{enumerate}
    \item Acesse o arquivo \texttt{main.py}. Na linha 10, você encontrará a variável \texttt{link\_inicial}, que indica em qual link o processamento do programa será iniciado. Neste caso, como iremos analisar o site da Universidade Federal de Ouro Preto (UFOP), colocaremos a página inicial da instituição federal: \texttt{'https://www.ufop.br/'}.
    
    \item Em seguida, na linha 11, temos a variável \texttt{dominio}. Devemos escolher qual o domínio será analisado. No caso da UFOP, como queremos analisar todo o conteúdo pertencente a esse domínio, atribuiremos a ele à variável.

    \item Além disso, existe a opção de escolher um link específico e colocá-lo na variável \texttt{link\_a\_verificar} na linha 12. Caso esse link seja encontrado durante o processamento, o programa notificará em qual página ele foi localizado.
\end{enumerate}

Essas configurações iniciais permitem que o programa saiba de onde começar a analisar os links e o conteúdo da UFOP, garantindo uma execução adequada e focada nas páginas relacionadas a essa instituição específica.



\subsection{Execução do Programa}
Para executar o programa, abra um terminal ou prompt de comando, navegue até o diretório onde os arquivos do projeto estão localizados e execute o seguinte comando:

\begin{lstlisting}[style=codestyle]
python main.py
\end{lstlisting}

O programa irá iniciar a verificação dos links a partir do link escolhido e, a cada novo link encontrado repetirá o processo e encontrará novos links para serem verificados. Durante o processo, as informações serão armazenadas nos arquivos \texttt{arquivosTXT/links\_encontrados.txt}, \texttt{arquivosTXT/links\_processados.txt} e \texttt{arquivosTXT/links\_com\_erro.txt}. Caso algum link encontrado seja o link que está sendo rastreado (\texttt{link\_a\_verificar}), uma mensagem de informação será exibida e o conteúdo HTML dessa página será salvo no arquivo \texttt{arquivosTXT/html\_link\_verificado.txt}.