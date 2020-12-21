import streamlit as st
import pandas as pd
import numpy as np


st.set_option('deprecation.showPyplotGlobalUse', False)

st.sidebar.header('**Streamlit CV - Cúrriculo Interativo**') 
 

opcoes = ['Boas-vindas', 
           'Formação', 
		  'Produção Científica',  
		  'Outros trabalhos']

pagina = st.sidebar.selectbox('Navegue pelo menu:', opcoes)

if pagina == 'Boas-vindas':
	st.title('Bem vindo ao meu portfolio') 
	st.write(""" 
		### Rafael Toledo Costa de Almeida

Olá, seja bem vindo! Meu nome é Rafael, sou estudante de graduação em Estatística na UFBA.

Este é o meu Currículo Interativo, onde estão dispostas informações de contato, formações acadêmicas e meus projetos desenvolvidos até o momento.

Deseja-se realizar novas atualizações recorrentes a fim de manter este currículo sempre bem atualizado. 

 	**Email**: rafaell.toledo96@gmail.com

 	**Telefone**: (71)991303645

 	**Lattes**: [http://lattes.cnpq.br/2192564435787089](http://lattes.cnpq.br/2192564435787089)
 	
 	**ORCID**: [https://orcid.org/0000-0002-4731-7975](https://orcid.org/0000-0002-4731-7975) 
 	
 """)

elif pagina == 'Formação':
	st.title('Formação')
	st.write("""
		#### **Formação Acadêmica** 
   		**2006 - 2013:** Ensino Médio Completo. Colégio da Polícia Militar Unidade Dendezeiros. 

   		**2015:** Graduação em andamento em Estatística. Universidade Federal da Bahia, UFBA.

   		#### **Formação Complementar**
   		Proficiência em Espanhol. Universidade Federal da Bahia, UFBA.

   		#### **Idiomas**
   		**Espanhol**: Avançado.

   		**Inglês**: Intermediário.
   	""")

elif pagina == 'Produção Científica':
	st.title('Produção Científica')
	st.write("""
 ### **Artigos publicados em periódicos**


 		:star: ALMEIDA, R.T.C; MUSTAFA, K. A.; RODRIGUES, P. C.
 		**The usefulness of robust multivariate methods: A case study with the menu items of a fast food restaurant chain**. 
   		CIÊNCIA NATURA, v.42, p. 17-32, 2020.
   		[https://periodicos.ufsm.br/cienciaenatura/article/view/39892/html](https://periodicos.ufsm.br/cienciaenatura/article/view/39892/html).
		
### **Projeto de Pesquisa**
:star: (2019-2020) **Análise de Sobrevivência Empresarial na Bahia**. 
   		

   		**Descrição:** Com o objetivo de estudar a sobrevivência das empresas tem-se feito apenas uma análise descritiva dos dados. 
   		No Brasil, as três principais instituições que já realizaram estudos sobre o tema sobrevivência de empresas são o Instituto Brasileiro de Geografia e Estatística - IBGE, o Banco Nacional de Desenvolvimento Econômico e Social - BNDES e o Serviço Brasileiro de Apoio às Micro e Pequenas Empresas - Sebrae. 
   		No presente projeto os tempos de vida das empresas da Bahia serão analisados através de metodologias de análise de sobrevivência que são amplamente utilizadas em epidemiologia e em confiabilidade. Variáveis explicativas serão incorporadas para identificar quais influenciam neste tempo. 
   		Os resultados deverão fornecer informações importantes sobre a sobrevivência das empresas, proporcionando embasamento para decisões que ampliem seus tempos de vida. Inicialmente as análises serão realizadas para o Estado da Bahia e suas mesorregiões e os dados serão coletados em sites oficiais. 
   		Por fim, o interesse é propor um modelo de regressão adequado para estes dados. 
   		ALMEIDA, R.T.C; BRITO, E. 
   		[https://drive.google.com/file/d/1J7xHp7fYl-h8qKcPgkZT_8ZYvQWgBgOB/view?usp=sharing](https://drive.google.com/file/d/1J7xHp7fYl-h8qKcPgkZT_8ZYvQWgBgOB/view?usp=sharing)

 ### **Projeto de Extensão**

:star: (2016-2019) **Estatística no Ensino Médio com apoio de software.**

   		**Descrição:** Este projeto vem dar apoio ao ensino de Estatística no Ensino Médio (EM) da rede pública, visando aprimorar o pensamento estatístico e o uso de softwares, buscando melhorar a formação tecnológica do alunado envolvido. \
   		Propõe-se assim um curso de Estatística Básica com apoio de software para alunos do EM da rede pública. Inicialmente será elaborado um tutorial para ser utilizado nas aulas e, simultaneamente, serão realizadas reuniões com os professores de Matemática das escolas visitadas. \
   		As atividades por turma serão desenvolvidas por dois meses. \
   		O aluno elaborará um relatório e apresentará os resultados de uma pesquisa a ser realizada durante o curso. Este projeto tem duração de um ano e alinha-se a grande demanda atualmente colocada de que o ensino da Estatística ocupa lugar central nos currículos escolares, da educação básica e da superior. \ 
   		Assim, almeja-se melhorar o ensino prático e crítico da Estatística no EM e proporcionar uma melhor qualidade para o ensino público geral. \
   		ALMEIDA, R.T.C.; SILVA, G.O.
   		[https://drive.google.com/file/d/1n-2PtNzFLVta9Ak9dlZoBzUiOb0srJVL/view?usp=sharing](https://drive.google.com/file/d/1n-2PtNzFLVta9Ak9dlZoBzUiOb0srJVL/view?usp=sharing)
   		""")

elif pagina == 'Outros trabalhos':
	st.title('Trabalhos')
	st.write("""

:star: (2020) **Análise de Correspondência Simples e Múltipla: Traçando o perfil dos inscritos do ENEM 2018 residentes no estado do Rio de Janeiro**.
		[https://drive.google.com/file/d/1YpNq-2x0eTpv8jlyrf2taNApTyiZ32gd/view?usp=sharing](https://drive.google.com/file/d/1YpNq-2x0eTpv8jlyrf2taNApTyiZ32gd/view?usp=sharing)
	
:star: (2020) ** Experimento com Redes Neurais utilizando uma base de dados referente as vendas globais dos games da 7ª e 8ª geração de consoles.**
		ALMEIDA, R. T. C.; SANTOS, C.C.
		[https://colab.research.google.com/drive/1Ee1yBLKsE5-X64_JcmXCwfzKdVUZ0eDp?usp=sharing](https://colab.research.google.com/drive/1Ee1yBLKsE5-X64_JcmXCwfzKdVUZ0eDp?usp=sharing)
	
:star: (2020) **Classificação dos tipos de vidro utilizando Árvore de Decisão.**
		ALMEIDA, R. T. C.; SANTOS, C.C.; MUSTAFA, K. A.
		[https://drive.google.com/file/d/1YKyPZ4HjM3QZJdQTJPN1XjwNMiydVXGg/view?usp=sharing](https://drive.google.com/file/d/1YKyPZ4HjM3QZJdQTJPN1XjwNMiydVXGg/view?usp=sharing)

	""")