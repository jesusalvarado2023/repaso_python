import streamlit as st

st.set_page_config(page_title="Estimador de Agua por Huayco", page_icon="💧")

st.title("💧 Estimador de Agua para Damnificados - Basado en la OMS")

st.markdown("""
Este estimador calcula los **requerimientos mínimos de agua** para damnificados durante **1 semana**, 
según las recomendaciones de la **OMS** (15 litros/persona/día para necesidades básicas como beber, cocinar e higiene).
""")

# Entrada: Número de damnificados
num_damnificados = st.number_input("Ingresa el número aproximado de damnificados:", min_value=1, step=1)

# Cálculo
if num_damnificados:
    litros_por_persona_dia = 15
    dias = 7
    total_litros = num_damnificados * litros_por_persona_dia * dias

    st.markdown(f"""
    ### Resultado:
    - **Número de damnificados:** {num_damnificados}
    - **Agua mínima requerida para 1 semana:** **{total_litros:,.0f} litros**
    """)

    st.info("Recuerda que este es el mínimo recomendado. En situaciones de emergencia pueden ser necesarias cantidades mayores.")

st.markdown("---")
st.caption("App desarrollada por Jesus con Streamlit 💙 | Datos basados en la OMS")
