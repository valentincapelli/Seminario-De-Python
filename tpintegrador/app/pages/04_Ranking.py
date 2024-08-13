import streamlit as st
from PIL import Image
import pandas as pd
from pathlib import Path

icon = Image.open("icon.png")
st.set_page_config(page_title="Ranking", page_icon=icon, layout="wide")

sessions_file_route = Path("./files/sessions.csv")
users_file_route = Path("./files/register.csv")

# Leo los archivos csv
df_sessions = pd.read_csv(sessions_file_route)
df_users = pd.read_csv(users_file_route)

# Filtro las columnas necesarias para el ranking 
df_ranking = df_sessions[['Mail', 'Puntaje', 'Fecha y hora']]

# Ordeno en orden descendente por puntaje
df_ranking = df_ranking.sort_values(by='Puntaje', ascending=False).reset_index(drop=True)

# Muestro el resultado de la partida del jugador 
if st.session_state and st.session_state.game_state['questions_list']:
    st.title("Felicidades, finalizaste tu partida 👏")
    st.subheader("Deseas volver a jugar?")
    if st.button("Jugar de nuevo"):
        st.session_state["game_state"] = {
            "state": "select_user",
            "mail": None,
            "thematic": None,
            "difficulty": None,
            "score": 0,
            "question_number": 0,
            "date_time": None,
            "correct_answers": 0,
            "options": None,
            "correct_key": None,
            "multiple_choice": None,
            "questions_list": None,
        }
        st.switch_page("pages/02_Juego.py")
    
    # Obtengo el puesto en el ranking del usuario actual
    current_mail = st.session_state.game_state['mail']
    current_date = st.session_state.game_state['date_time']
    player_position = df_ranking[(df_ranking['Fecha y hora'] == current_date) & (df_ranking['Mail'] == current_mail)].index[0] + 1
    
    st.subheader("Aquí están tus resultados:")
    st.write(f"Hora de finalización: {st.session_state.game_state['date_time']}")
    st.write(f"Preguntas acertadas: {st.session_state.game_state['correct_answers']}/5")
    st.write(f"Dificultad elegida: {st.session_state.game_state['difficulty']}")
    st.write(f"Puntaje: {st.session_state.game_state['score']}")
    st.write(f"Posición en el ranking: {player_position}")
    for question in st.session_state.game_state['questions_list']:
        with st.container(border=True):
            st.subheader (f"Pregunta #{question.number}")
            for option in question.options:
                if option != question.key:
                    st.markdown(f"**{option}:** {question.options[option]}")
            st.markdown (f'**Incognita:** {question.key}')
            st.markdown(f'**Respuesta correcta:** {question.correct_answer}')
            if question.correct_answer.lower() == question.user_answer.lower():
                st.success (f'Su respuesta: {question.user_answer}')
            else:   
                st.error (f'Su respuesta: {question.user_answer}')

# Ranking de las mejores 15 partidas

# Mergeo los dataframe para obtener los nombres de usuarios
df_combined = pd.merge(df_ranking, df_users, on='Mail', how='left')

# Me quedo con los primeros 15
df_top_15 = df_combined.head(15)

# Creo la columna puesto
df_top_15['Puesto'] = range(1, len(df_top_15) + 1)

# Asigno como indice del ranking la columna puesto
df_top_15 = df_top_15.set_index('Puesto')

# Muestro el ranking
st.title('Ranking historico de puntajes')
st.table(df_top_15[['Usuario','Mail','Fecha y hora','Puntaje']])