import streamlit as st
from datetime import datetime

# Inicializar estado de los botones si no existen
if 'mostrar_razon' not in st.session_state:
    st.session_state.mostrar_razon = False
if 'mostrar_amo' not in st.session_state:
    st.session_state.mostrar_amo = False
if 'mostrar_futuro' not in st.session_state:
    st.session_state.mostrar_futuro = False
if 'mostrar_feliz' not in st.session_state:
    st.session_state.mostrar_feliz = False

# Estilo CSS para mejorar el diseño
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
    }
    .button-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 20px;
    }
    .stButton>button {
        background-color: #d6336c;
        color: white;
        font-size: 18px;
        padding: 10px;
        margin: 5px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título principal
st.markdown('<h1 class="title">Carta para Catita 💖</h1>', unsafe_allow_html=True)

# Botón de prueba para desbloquear antes de la fecha real
if st.button("🔑 Desbloquear (Solo Prueba)"):
    fecha_actual = datetime(2025, 3, 8, 12, 0)  # Simula el 8 de marzo a las 12:00
else:
    fecha_actual = datetime.now()  # Usa la fecha real si no presionas el botón

# Fecha real de desbloqueo
fecha_desbloqueo = datetime(2025, 3, 8, 12, 0)

# Verificar si la fecha ya llegó
if fecha_actual < fecha_desbloqueo:
    st.markdown('<p class="message">Oh, mi niña, todavía no es el tiempo. ⏳</p>', unsafe_allow_html=True)
else:
    st.markdown('<p class="message">¡Bienvenida, mi amor! 💖</p>', unsafe_allow_html=True)
    
    # Contenedor de botones
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    
    # Botón 1: ¿Por qué me enamoré de ti?
    if st.button("💘 ¿Por qué me enamoré de ti?"):
        st.session_state.mostrar_razon = True
    if st.session_state.mostrar_razon:
        st.write("Me enamoré de ti porque, desde que comenzamos a hablar, sentí una conexión única. "
                 "Nuestra primera salida me puso nervioso como nunca antes, y supe que eras la mujer que quería en mi vida. "
                 "Aunque a veces te hagas la dura, eres una niña increíble que se preocupa por su futuro, y eso me encanta. ❤️")

    # Botón 2: Lo que más amo de ti
    if st.button("😍 Lo que más amo de ti"):
        st.session_state.mostrar_amo = True
    if st.session_state.mostrar_amo:
        st.write("Amo tus ojos, tus abrazos, aunque a veces seas un poco distante con el cariño. "
                 "Me encanta cómo con una sola palabra puedes mejorar mi día. "
                 "Amo tu forma única de ser, incluyendo tus mañas, porque eres única en todos los sentidos. 💕")

    # Botón 3: Nuestro futuro juntos
    if st.button("🌍 Nuestro futuro juntos"):
        st.session_state.mostrar_futuro = True
    if st.session_state.mostrar_futuro:
        st.write("Waaa, esto es lo que más me gusta hablar contigo. Me imagino un futuro juntos lleno de momentos hermosos, "
                 "puro leseo y cumpliendo nuestros sueños. Quiero estar contigo en todo, apoyarte y amarte cada día. "
                 "Ah, y lo de ir al sur... ¡sí o sí! 😂❤️")

    # Botón 4: Feliz día
    if st.button("🌹 Feliz día"):
        st.session_state.mostrar_feliz = True
    if st.session_state.mostrar_feliz:
        st.write("Feliz Día de la Mujer, mi niña preciosa. 🌸 "
                 "Eres una persona maravillosa, fuerte, luchadora y llena de luz. "
                 "Nunca dejes que nadie apague esa chispa que tienes. "
                 "Hoy es tu día, y quiero recordarte cuánto te amo y admiro. 💖")
    
    st.markdown('</div>', unsafe_allow_html=True)
