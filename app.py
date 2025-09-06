import streamlit as st
from src.core.balance_hidrico import calcular_balance_hidrico
from src.core.recomendador import generar_recomendacion_riego

# --- Configuración de la página ---
st.set_page_config(
    page_title="Pluviometría - Asesor de Riego",
    page_icon="💧",
    layout="wide"
)

# --- Barra Lateral (Inputs del Usuario) ---
st.sidebar.header("Parámetros del Campo")

agua_ayer = st.sidebar.number_input(
    "Agua disponible ayer (mm)", 
    min_value=0.0, 
    value=20.0, 
    step=0.5,
    help="Humedad en la zona de raíces del día anterior."
)
lluvia_hoy = st.sidebar.number_input(
    "Lluvia efectiva de hoy (mm)", 
    min_value=0.0, 
    value=5.0, 
    step=0.1,
    help="Precipitación que realmente se infiltró en el suelo."
)
riego_hoy = st.sidebar.number_input(
    "Riego aplicado hoy (mm)", 
    min_value=0.0, 
    value=0.0, 
    step=1.0
)
et_hoy = st.sidebar.number_input(
    "Evapotranspiración (ET) hoy (mm)", 
    min_value=0.0, 
    value=3.5, 
    step=0.1,
    help="Agua perdida por evaporación y transpiración de la planta."
)

st.sidebar.markdown("---")
st.sidebar.header("Configuración de Alertas")

umbral_optimo = st.sidebar.slider(
    "Umbral óptimo de humedad (mm)", 
    min_value=10.0, 
    max_value=50.0, 
    value=25.0, 
    step=0.5,
    help="Nivel mínimo de agua deseado para el cultivo."
)
pronostico_lluvia = st.sidebar.number_input(
    "Pronóstico de lluvia para mañana (mm)", 
    min_value=0.0, 
    value=0.0, 
    step=0.1
)


# --- Cuerpo Principal de la Aplicación ---
st.title("💧 Asesor de Riego Inteligente")
st.markdown("Esta herramienta te ayuda a tomar decisiones de riego informadas basadas en el balance hídrico de tu cultivo.")

# --- Cálculos del motor ---
try:
    # 1. Calcular el balance hídrico
    agua_disponible_hoy = calcular_balance_hidrico(
        agua_ayer=agua_ayer,
        lluvia_efectiva=lluvia_hoy,
        riego_aplicado=riego_hoy,
        evapotranspiracion=et_hoy
    )

    # 2. Generar la recomendación de riego
    recomendacion = generar_recomendacion_riego(
        agua_disponible=agua_disponible_hoy,
        umbral_optimo=umbral_optimo,
        pronostico_lluvia_mm=pronostico_lluvia
    )

    # --- Mostrar resultados ---
    st.markdown("---")
    st.header("Resultados y Recomendación")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Balance Hídrico Actual")
        st.metric(
            label="Agua Disponible en el Suelo",
            value=f"{agua_disponible_hoy:.2f} mm",
            delta=f"{(agua_disponible_hoy - agua_ayer):.2f} mm vs ayer",
            help="El delta muestra si la reserva de agua aumentó o disminuyó hoy."
        )

    with col2:
        st.subheader("Recomendación de Riego")
        if "No se requiere riego" in recomendacion:
            st.success(f"✅ {recomendacion}")
        elif "Se recomienda esperar" in recomendacion:
            st.info(f"🤔 {recomendacion}")
        else: # "Se recomienda aplicar"
            st.warning(f"⚠️ {recomendacion}")

except ValueError as e:
    st.error(f"Error en los datos de entrada: {e}")

st.markdown("---")
st.write("Desarrollado para el proyecto Pluviometría.")
