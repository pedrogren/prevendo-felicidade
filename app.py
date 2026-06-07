import streamlit as st
import pandas as pd
model = pd.read_pickle('model_feliz.pkl')

st.markdown("# Descubra a felicidade")

cursos_opt = ['0', '2', '1', '3', 'Mais que 3']
cursos = st.selectbox("Quantos cursos acompanhou do Téo Me Why?", options=cursos_opt)

redes_opt = ['LinkedIn', 'Twitch', 'YouTube', 'Instagram', 'Amigos', 'Twitter / X',
 'Outra rede social']
redes = st.selectbox("Como conheceu o Téo Me Why?", options=redes_opt)

Estado_opt = ['AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MT', 'PA',
               'PB', 'PE', 'PR', 'RJ', 'RN', 'RS', 'SC', 'SP']
Estado = st.selectbox("Estado em que mora atualmente", options=Estado_opt)

Formação_opt = ['Biológicas', 'Exatas', "Humanas"]
Formação = st.selectbox("Área de formação", options=Formação_opt)

tempo_opt = ['De 0 a 6 meses', 'De 1 ano a 2 anos', 'De 6 meses a 1 ano',
              'Mais de 4 anos', 'Não atuo', 'de 2 anos a 4 anos']
tempo = st.selectbox("Tempo que atua na área de dados", options=tempo_opt)

posição_opt = ['C-Level', 'Coordenação', 'Diretoria', 'Especialista', 
               'Gerência', 'Iniciante', 'Júnior', 'Pleno', 'Sênior']
posição = st.selectbox("Posição da cadeira (Senioridade)", options=posição_opt)
col1, col2, col3 =  st.columns(3)
with col1:
    video_game = st.radio("Curte VideoGame?", ["Sim", "Não"])
    livros = st.radio("Curte livros?", ["Sim", "Não"])
with col2:
    futebol = st.radio("Curte futebol?", ["Sim", "Não"])
    tabuleiro = st.radio("Curte jogos de tabuleiro?", ["Sim", "Não"])
with col3:
    Formula1 = st.radio("Curte jogos de Formula 1?", ["Sim", "Não"])
    mma = st.radio("Curte MMA?", ["Sim", "Não"])

idade = st.number_input("Sua idade", 18, 100)

data = {
    'Como conheceu o Téo Me Why?': [redes], 
    'Quantos cursos acompanhou do Téo Me Why?': [cursos], 
    'Curte games?': [1 if video_game == 'Sim' else 0], 
    'Curte futebol?': [1 if futebol == 'Sim' else 0], 
    'Curte livros?': [1 if livros == 'Sim' else 0], 
    'Curte jogos de tabuleiro?': [1 if tabuleiro == 'Sim' else 0], 
    'Curte jogos de fórmula 1?': [1 if Formula1 == 'Sim' else 0], 
    'Curte jogos de MMA?': [1 if mma == 'Sim' else 0], 
    'Idade': [idade],
    'Estado que mora atualmente': [Estado], 
    'Área de Formação': [Formação], 
    'Tempo que atua na área de dados': [tempo], 
    'Posição da cadeira (senioridade)': [posição], 
    'Você se considera uma pessoa feliz?': [0] 
}

df = pd.DataFrame(data)
st.data_editor(df)

dummies = ['Como conheceu o Téo Me Why?', 'Quantos cursos acompanhou do Téo Me Why?', 
           'Estado que mora atualmente', 'Área de Formação',
           'Tempo que atua na área de dados', 'Posição da cadeira (senioridade)']

num_var = ['Curte games?', 'Curte futebol?', 'Curte livros?', 
           'Curte jogos de tabuleiro?', 'Curte jogos de fórmula 1?',
           'Curte jogos de MMA?', 'Idade']

df = pd.get_dummies(df, columns=dummies).astype(int)
df[num_var] = df[num_var].copy()
df['pessoa feliz'] = df['Você se considera uma pessoa feliz?'].copy()
df = df.dropna()
df['pessoa feliz'] = df['pessoa feliz'].astype(int)


df_template = pd.DataFrame(columns=['Como conheceu o Téo Me Why?_Amigos',
       'Como conheceu o Téo Me Why?_Instagram',
       'Como conheceu o Téo Me Why?_LinkedIn',
       'Como conheceu o Téo Me Why?_Outra rede social',
       'Como conheceu o Téo Me Why?_Twitch',
       'Como conheceu o Téo Me Why?_Twitter / X',
       'Como conheceu o Téo Me Why?_YouTube',
       'Quantos cursos acompanhou do Téo Me Why?_0',
       'Quantos cursos acompanhou do Téo Me Why?_1',
       'Quantos cursos acompanhou do Téo Me Why?_2',
       'Quantos cursos acompanhou do Téo Me Why?_3',
       'Quantos cursos acompanhou do Téo Me Why?_Mais que 3',
       'Estado que mora atualmente_AM', 'Estado que mora atualmente_BA',
       'Estado que mora atualmente_CE', 'Estado que mora atualmente_DF',
       'Estado que mora atualmente_ES', 'Estado que mora atualmente_GO',
       'Estado que mora atualmente_MA', 'Estado que mora atualmente_MG',
       'Estado que mora atualmente_MT', 'Estado que mora atualmente_PA',
       'Estado que mora atualmente_PB', 'Estado que mora atualmente_PE',
       'Estado que mora atualmente_PR', 'Estado que mora atualmente_RJ',
       'Estado que mora atualmente_RN', 'Estado que mora atualmente_RS',
       'Estado que mora atualmente_SC', 'Estado que mora atualmente_SP',
       'Área de Formação_Biológicas', 'Área de Formação_Exatas',
       'Área de Formação_Humanas',
       'Tempo que atua na área de dados_De 0 a 6 meses',
       'Tempo que atua na área de dados_De 1 ano a 2 anos',
       'Tempo que atua na área de dados_De 6 meses a 1 ano',
       'Tempo que atua na área de dados_Mais de 4 anos',
       'Tempo que atua na área de dados_Não atuo',
       'Tempo que atua na área de dados_de 2 anos a 4 anos',
       'Posição da cadeira (senioridade)_C-Level',
       'Posição da cadeira (senioridade)_Coordenação',
       'Posição da cadeira (senioridade)_Diretoria',
       'Posição da cadeira (senioridade)_Especialista',
       'Posição da cadeira (senioridade)_Gerência',
       'Posição da cadeira (senioridade)_Iniciante',
       'Posição da cadeira (senioridade)_Júnior',
       'Posição da cadeira (senioridade)_Pleno',
       'Posição da cadeira (senioridade)_Sênior', 'Curte games?',
       'Curte futebol?', 'Curte livros?', 'Curte jogos de tabuleiro?',
       'Curte jogos de fórmula 1?', 'Curte jogos de MMA?', 'Idade',
       'pessoa feliz'])

df = pd.concat([df_template, df]).fillna(0)

proba = model['model'].predict_proba(df[model['features']])[:, -1][0]

if proba > 0.7:
    st.success('Muito bem, você é feliz!')
elif proba > 0.4:
    st.warning('Você está no meio termo...')
else:
    st.error('Você é triste :(') 
