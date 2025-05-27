import streamlit as st

st.set_page_config(page_title="Quiz de Python", page_icon="🐍")

st.title("🐍 Quiz de Python - Repasa tu sintaxis")

st.write("Responde las siguientes preguntas sobre sintaxis de Python:")

# Definimos las preguntas y respuestas correctas
preguntas = [
    {
        "pregunta": "¿Cómo defines una función en Python?",
        "opciones": [
            "def mi_funcion():",
            "function mi_funcion():",
            "define mi_funcion():",
            "func mi_funcion()"
        ],
        "respuesta": "def mi_funcion():"
    },
    {
        "pregunta": "¿Cuál es la forma correcta de crear una lista?",
        "opciones": [
            "mi_lista = list(1,2,3)",
            "mi_lista = [1,2,3]",
            "mi_lista = {1,2,3}",
            "mi_lista = (1,2,3)"
        ],
        "respuesta": "mi_lista = [1,2,3]"
    },
    {
        "pregunta": "¿Qué hace el siguiente código?\n\nfor i in range(3):\n    print(i)",
        "opciones": [
            "Imprime 0,1,2",
            "Imprime 1,2,3",
            "Imprime 0,1,2,3",
            "No imprime nada"
        ],
        "respuesta": "Imprime 0,1,2"
    },
    {
        "pregunta": "¿Qué operador se usa para comprobar igualdad?",
        "opciones": [
            "=",
            "==",
            "!=",
            "===",
        ],
        "respuesta": "=="
    },
    {
        "pregunta": "¿Qué resultado devuelve este código?\n\nif 5 > 3:\n    print('Sí')\nelse:\n    print('No')",
        "opciones": [
            "No",
            "Error de sintaxis",
            "Sí",
            "None"
        ],
        "respuesta": "Sí"
    }
]

# Generamos una variable de estado para las respuestas del usuario
if "respuestas_usuario" not in st.session_state:
    st.session_state["respuestas_usuario"] = [""] * len(preguntas)

# Mostrar preguntas
for i, p in enumerate(preguntas):
    st.write(f"**{i+1}. {p['pregunta']}**")
    st.session_state["respuestas_usuario"][i] = st.radio(
        f"Selecciona tu respuesta:",
        p["opciones"],
        index=0,
        key=f"pregunta_{i}"
    )

# Botón para verificar respuestas
if st.button("Verificar respuestas"):
    aciertos = 0
    for i, p in enumerate(preguntas):
        if st.session_state["respuestas_usuario"][i] == p["respuesta"]:
            aciertos += 1

    st.success(f"¡Obtuviste {aciertos} de {len(preguntas)} aciertos!")

    if aciertos == len(preguntas):
        st.balloons()
