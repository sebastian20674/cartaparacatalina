import streamlit as st
from datetime import datetime

# Inicializar el estado de los botones correctamente
if "mensaje" not in st.session_state:
    st.session_state["mensaje"] = ""

# Estilos CSS
st.markdown(
    """
    <style>
    body {
        background-color: #ffebf0;
        font-family: Arial, sans-serif;
    }
    .title {
        color: #d6336c;
        text-align: center;
        font-size: 36px;
        font-weight: bold;
    }
    .message {
        text-align: center;
        font-size: 20px;
        margin-top: 20px;
        font-weight: bold;
    }
    .button-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 20px;
    }
    .stButton>button {
        background-color: #d6336c !important;
        color: white !important;
        font-size: 18px !important;
        padding: 10px !important;
        margin: 5px !important;
        border-radius: 10px !important;
        width: 80%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título
st.markdown('<h1 class="title">Carta para Catita 💖</h1>', unsafe_allow_html=True)

# Fecha de desbloqueo
fecha_actual = datetime.now()
fecha_desbloqueo = datetime(2025, 3, 8, 12, 0)

# Opción de prueba para desbloquear antes de tiempo
if st.button("🔑 Desbloquear (Solo Prueba)"):
    fecha_actual = fecha_desbloqueo

# Verificar si ya se puede acceder
if fecha_actual < fecha_desbloqueo:
    st.markdown('<p class="message">Oh, mi niña, todavía no es el tiempo. ⏳</p>', unsafe_allow_html=True)
else:
    st.markdown('<p class="message">¡Bienvenida, mi amor! 💖</p>', unsafe_allow_html=True)

    # Contenedor de botones
    st.markdown('<div class="button-container">', unsafe_allow_html=True)

    # Botón 1: ¿Por qué me enamoré de ti?
    if st.button("💘 ¿Por qué me enamoré de ti?"):
        st.session_state["mensaje"] = (
            "Me enamoré de ti porque, desde que comenzamos a hablar, sentí una conexión única. "
            "Nuestra primera salida me puso nervioso como nunca antes, y supe que eras la mujer que quería en mi vida. "
            "Aunque a veces te hagas la dura, eres una niña increíble que se preocupa por su futuro, y eso me encanta. ❤️"
        )

    # Botón 2: Lo que más amo de ti
    if st.button("😍 Lo que más amo de ti"):
        st.session_state["mensaje"] = (
            "Amo tus ojos, tus abrazos, aunque a veces seas un poco distante con el cariño. "
            "Me encanta cómo con una sola palabra puedes mejorar mi día. "
            "Amo tu forma única de ser, incluyendo tus mañas, porque eres única en todos los sentidos. 💕"
        )

    # Botón 3: Nuestro futuro juntos
    if st.button("🌍 Nuestro futuro juntos"):
        st.session_state["mensaje"] = (
            "Waaa, esto es lo que más me gusta hablar contigo. Me imagino un futuro juntos lleno de momentos hermosos, "
            "puro leseo y cumpliendo nuestros sueños. Quiero estar contigo en todo, apoyarte y amarte cada día. "
            "Ah, y lo de ir al sur... ¡sí o sí! 😂❤️"
        )

    # Botón 4: Feliz día
    if st.button("🌹 Feliz día"):
        st.session_state["mensaje"] = (
            "Feliz Día de la Mujer, mi niña preciosa. 🌸 "
            "Eres una persona maravillosa, fuerte, luchadora y llena de luz. "
            "Nunca dejes que nadie apague esa chispa que tienes. "
            "Hoy es tu día, y quiero recordarte cuánto te amo y admiro. 💖"
        )

    # Mostrar el mensaje seleccionado
    if st.session_state["mensaje"]:
        st.markdown(f'<p class="message">{st.session_state["mensaje"]}</p>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

