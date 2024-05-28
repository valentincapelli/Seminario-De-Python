import csv
import pandas as pd
from pathlib import Path
import random
import streamlit as st

def looking_for_user(register_file_route, email):
    '''This function finds the email in the file 
    and returns the line in the file according to the 
    email, else returns -1'''
    found = False
    try:
        with open (register_file_route)as file:
            reader = csv.reader(file)
            for line in reader:
                if line[2] == email:
                    found = True
                    break
    finally:
        #Si el archivo o el usuario no existe, devuelvo false
        #sino devuelvo true
        return found
        

def register(register_file_route, user):
    '''This function creates the file with the new user. if it is created,
    adds a new user'''
    with open(register_file_route, 'a', newline='') as csv_file:
        fieldnames = ['Usuario','Nombre','Mail','Fecha de nacimiento','Genero',]
        writer = csv.DictWriter(csv_file,fieldnames=fieldnames)

        #Verifico si el archivo no existe, si no existe creo el header
        if (csv_file.tell() == 0): 
            writer.writeheader()

        writer.writerow({'Usuario': user.username, 'Nombre': user.full_name, 'Mail': user.email,
                         'Fecha de nacimiento': user.date_of_birth, 'Genero': user.gender})


def update_user(register_file_route, user):
    '''This function update an user without changing his email'''
    with open(register_file_route, encoding='utf-8') as file:
        reader = csv.reader(file)
        header, data = next(reader), list(reader)

    for line in data:
        if line[2] == user.email:
            line[0] = user.username 
            line[1] = user.full_name
            line[3] = user.date_of_birth
            line[4] = user.gender
            break

    with open(register_file_route, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)
    return file 


def return_users():
    register_file_route = Path("./files/register.csv")
    list = []
    df_registers = pd.read_csv(register_file_route)
    list = zip(df_registers.Usuario, df_registers.Mail)
    return list 


def generate_questions(dict):
    # Elige una clave random a adivinar (no puede ser un int)
    while True:
        key, value = random.choice(list(dict.items()))
        if (isinstance(value, str)):
            break

    st.session_state.game_state["question_number"] += 1

    with st.form(key=f"questions"):
        st.title(f"Pregunta #{st.session_state.game_state['question_number']}")
        for pos in dict:
            if pos != key:
                st.write(f"{pos}: {dict[pos]}")
        answer = st.text_input(f"Adivine el siguiente campo: {key}")

        submit_button = st.form_submit_button("Responder")

    if submit_button: 
        if answer.lower() == value.lower():
            st.session_state.game_state["correct_answers"] += 1


def airport_options():
    airports_file_route = Path("../custom_datasets/ar-airports.csv")
    df_airports = pd.read_csv(airports_file_route)
    
    # Obtener el número total de filas
    num_rows = df_airports.shape[0]  
    # Restar 1 porque los índices van de 0 a num_rows-1
    random_row = random.randint(0, num_rows - 1)  


    airport_name = df_airports.name[random_row]
    municipality = df_airports.municipality[random_row]
    region_name = df_airports.region_name[random_row]
    airport_type = df_airports.type[random_row]

    dict = {"nombre" : airport_name, "municipalidad" : municipality,
         "provincia" : region_name, "tipo" : airport_type}
    
    return dict


def lakes_options():
    lakes_file_route = Path("../custom_datasets/lagos_arg.csv")
    df_lakes = pd.read_csv(lakes_file_route)
    
    num_rows = df_lakes.shape[0]  
    random_row = random.randint(0, num_rows - 1)  

    lake_name = df_lakes.Nombre[random_row]
    province = df_lakes.Ubicación[random_row]
    size = df_lakes['Sup Tamaño'][random_row]
    surface = df_lakes['Superficie (km²)'][random_row]

    dict = {"nombre" : lake_name, "provincia" : province,
         "tamaño" : size, "superficie" : surface}
    
    return dict


def conectivity_options():
    conectivity_file_route = Path("../custom_datasets/Conectividad_Internet.csv")
    df_conectivity = pd.read_csv(conectivity_file_route)
    
    num_rows = df_conectivity.shape[0]  
    random_row = random.randint(0, num_rows - 1)  

    poblation = df_conectivity.Poblacion[random_row]
    province = df_conectivity.Provincia[random_row]
    city = df_conectivity.Localidad[random_row]
    optical_fiber = df_conectivity.FIBRAOPTICA[random_row]

    dict = {"poblacion" : poblation, "provincia" : province,
         "ciudad" : city, "fibra optica" : optical_fiber}
    
    return dict


def census_options():
    census_file_route = Path("../custom_datasets/c2022_tp_c_resumen_adaptado.csv")
    df_census = pd.read_csv(census_file_route)
    
    num_rows = df_census.shape[0]  
    random_row = random.randint(1, num_rows - 1)  

    poblation = df_census["Total de población"][random_row]
    province = df_census.Jurisdicción[random_row]
    poor_people = df_census["Población en situación de calle(²)"][random_row]
    women_poblation = df_census["Mujeres Total de población"][random_row]

    dict = {"poblacion" : poblation, "provincia" : province,
         "pobres" : poor_people, "mujeres" : women_poblation}
    
    return dict


def census_questions():
    dict = census_options()
    st.session_state.game_state["question_number"] += 1
    
    with st.form(key=f"questions"):
        st.title(f"Pregunta #{st.session_state.game_state['question_number']}")
        st.write("Poblacion: ", dict["poblacion"])
        st.write("Total de mujeres: ", dict["mujeres"])
        st.write("Total de gente en situacion de calle: ", dict["pobres"])
        answer = st.text_input("Adivine la provincia")

        submit_button = st.form_submit_button("Responder")

    if submit_button: 
        if answer.lower() == dict["provincia"].lower():
            st.session_state.game_state["correct_answers"] += 1

            
def save_session (game_state):
    sessions_route = Path ("./files/sessions.csv")
    with open (sessions_route, 'a', newline='') as sessions_file:
        fieldnames = ['Mail', 'Fecha y hora', 'Dificultad', 'Tematica', 'Respuestas correctas', 'Puntaje']
        writer = csv.DictWriter(sessions_file,fieldnames=fieldnames)

        #Verifico si el archivo no existe, si no existe creo el header
        if (sessions_file.tell() == 0): 
            writer.writeheader()
        
        st.session_state.game_state["score"] = st.session_state.game_state["correct_answers"]

        if st.session_state.game_state["difficulty"] == "Media":
            st.session_state.game_state["score"] *= 1.50 
        else:
            if st.session_state.game_state["difficulty"] == "Dificil":
                st.session_state.game_state["score"] *= 2
         

        writer.writerow({'Mail': game_state['mail'], 'Fecha y hora': game_state['date_time'], 'Dificultad': game_state['difficulty'],
                         'Tematica': game_state['thematic'], 'Respuestas correctas': game_state['correct_answers'], 'Puntaje': game_state['score']}) 