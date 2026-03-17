import streamlit as st

# Orden de llenado de orbitales (regla de Aufbau)
orbitales = [
    ("1s", 2), ("2s", 2), ("2p", 6), ("3s", 2), ("3p", 6),
    ("4s", 2), ("3d", 10), ("4p", 6), ("5s", 2), ("4d", 10),
    ("5p", 6), ("6s", 2), ("4f", 14), ("5d", 10), ("6p", 6),
    ("7s", 2), ("5f", 14), ("6d", 10), ("7p", 6)
]

def configuracion_electronica(Z):
    electrones = Z
    config = []

    for orbital, capacidad in orbitales:
        if electrones <= 0:
            break
        if electrones >= capacidad:
            config.append(f"{orbital}^{capacidad}")
            electrones -= capacidad
        else:
            config.append(f"{orbital}^{electrones}")
            electrones = 0

    return " ".join(config)

# UI
st.title("Configuración Electrónica")

st.write("Ingresa el número de protones (número atómico):")

Z = st.number_input("Número atómico", min_value=1, max_value=118, step=1)

if st.button("Calcular"):
    resultado = configuracion_electronica(Z)
    st.success(f"Configuración electrónica: {resultado}")
