import streamlit as st
from PIL import Image
from app_tools import tools
import datetime as dt

icon = Image.open("icon.png")
st.set_page_config(page_title="Inicio", page_icon=icon, layout="wide")

# Si no existe el estado, lo creo
if "game_state" not in st.session_state:
    st.session_state["game_state"] = {
        "state": "select_user",
        "user": None,
        "mail": None,
        "thematic": None,
        "difficulty": None,
        "score": 0,
        "question_number": 0,
        "ultima_respuesta": None,
        "ultima_pregunta": "",
        "ultimas_opciones": "",
        "date_time": None,
        "correct_answers": 0
    }

if st.session_state.game_state["state"] == "select_user":    
    st.title("Bienvenidos a PyTrivia :wave:")
    st.subheader("Para comenzar con la trivia seleccione su usuario")
    st.write("Si no te registraste aun, toca en el siguiente link")
    st.page_link("pages/03_Formulario_de_registro.py", label="Link")

    with st.form(key="form"):
        user = st.selectbox("Elige al usuario", list(map(lambda tupla: tupla[0] + " / " + tupla[1], tools.return_users())))

        thematic = st.selectbox("Elegi la tematica", ["Aeropuertos", "Lagos", "Conectividad","Censo 2022"])

        difficulty = st.selectbox("Seleccione la dificultad", ["Facil", "Media", "Dificil"])

        submitted = st.form_submit_button("Jugar")

    if submitted:
        user_list = user.replace(" ", "").split("/")
        st.session_state.game_state["state"] = "generate_question"
        st.session_state.game_state["user"] = user_list[0]
        st.session_state.game_state["mail"] = user_list[1]
        st.session_state.game_state["thematic"] = thematic
        st.session_state.game_state["difficulty"] = difficulty
        st.rerun() 

if st.session_state.game_state["state"] == "generate_question":
    if st.session_state.game_state["thematic"] == "Aeropuertos":
        tools.generate_questions(tools.airport_options())
    elif st.session_state.game_state["thematic"] == "Lagos":
        tools.generate_questions(tools.lakes_options())
    elif st.session_state.game_state["thematic"] == "Conectividad":
        tools.generate_questions(tools.conectivity_options())
    else:
        tools.census_questions()  

    if st.session_state.game_state["question_number"] == 6:
        current_date = dt.datetime.now()
        # Convierto la fecha en "Año-Mes-Día Hora:Minuto"
        current_date = current_date.strftime("%Y-%m-%d %H:%M")
        st.session_state.game_state["date_time"] = current_date
        tools.save_session(st.session_state['game_state'])
        st.session_state.game_state["state"] = "ranking"
        st.rerun()

if st.session_state.game_state["state"] == "ranking":
    st.write("Cape gay")