import streamlit as st
import random

st.set_page_config(page_title="Química Divertida", page_icon="")

st.title("Aprende Química Jugando")

menu = st.sidebar.selectbox(
    "Selecciona una actividad",
    ["Inicio", "Quiz de Química", "Adivina el Elemento"]
)

# ---------------- INICIO ----------------
if menu == "Inicio":
    st.header("Bienvenido ")
    st.image("images/laboratorio.jpg", caption="Laboratorio químico")
    st.write("Aprende química con juegos interactivos e imágenes.")

# ---------------- QUIZ ----------------
elif menu == "Quiz de Química":
    st.header("Quiz de Química")

    preguntas = [
        {
            "pregunta": "¿Cuál es el símbolo del sodio?",
            "opciones": ["Na", "So", "S"],
            "respuesta": "Na",
            "explicacion": "El sodio proviene del latín 'Natrium'.",
            "imagen": "images/tabla_periodica.png"
        },
        {
            "pregunta": "¿Cuántos protones tiene el carbono?",
            "opciones": ["6", "12", "8"],
            "respuesta": "6",
            "explicacion": "El número atómico del carbono es 6.",
            "imagen": "images/tabla_periodica.png"
        },
    ]

    q = random.choice(preguntas)

    st.image(q["imagen"], width=300)
    st.write(q["pregunta"])
    opcion = st.radio("Elige una respuesta:", q["opciones"])

    if st.button("Responder"):
        if opcion == q["respuesta"]:
            st.success("¡Correcto!")
        else:
            st.error("Incorrecto")
        
        if st.checkbox("Mostrar ayuda"):
            st.info(q["explicacion"])

# ---------------- JUEGO ELEMENTOS ----------------
elif menu == "Adivina el Elemento":
    st.header("Adivina el elemento")

    elementos = [
        {
            "pista": "Gas esencial para respirar",
            "respuesta": "Oxígeno",
            "imagen": "images/oxigeno.jpg"
        },
        {
            "pista": "Metal líquido a temperatura ambiente",
            "respuesta": "Mercurio",
            "imagen": "images/mercurio.jpg"
        },
    ]

    e = random.choice(elementos)

    st.image(e["imagen"], width=300)
    st.info(e["pista"])

    respuesta = st.text_input("¿Cuál es el elemento?")

    if st.button("Verificar"):
        if respuesta.lower() == e["respuesta"].lower():
            st.success("¡Correcto!")
        else:
            st.error(f"Era: {e['respuesta']}")

    if st.checkbox("Necesito ayuda"):
        st.warning("Observa la imagen y piensa en sus propiedades")
