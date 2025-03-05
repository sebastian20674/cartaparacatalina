import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Para Catita", page_icon="💖")

# Estilos CSS
st.markdown(
    """
    <style>
        .titulo {
            text-align: center;
            font-size: 30px;
            font-weight: bold;
            color: #ff4081;
        }
        .mensaje {
            text-align: center;
            font-size: 20px;
            margin-top: 10px;
        }
        .boton {
            display: flex;
            justify-content: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Mostrar imagen (ahora más pequeña)
st.image("amor.jpg", width=300)

# Título principal
st.markdown('<p class="titulo">Para Catita 💖</p>', unsafe_allow_html=True)

# Campo para ingresar la clave
clave = st.text_input("Ingresa la clave para desbloquear:", type="password")

# Clave correcta
clave_correcta = "desbloqueo4356"

# Si la clave es correcta, se desbloquea el contenido
if clave == clave_correcta:
    st.markdown('<p class="mensaje">¡Bienvenida, mi wawa! 💕</p>', unsafe_allow_html=True)

    # Botones con mensajes
    if st.button("¿Por qué me enamoré de ti?"):
        st.write(
            "Me enamoré de ti porque al comenzar a hablar estabas un poco dura, "
            "pero tuvimos una conexión inmediata. En nuestra primera salida, "
            "yo estaba full nervioso, cosa que nunca me había pasado, y supe que "
            "eras la mujer que quiero. A pesar de tus actitudes, eres una niña de "
            "bien que se preocupa por su futuro, aunque a veces te hagas la dura, "
            "y eso me encanta de ti. 💖"
        )

    if st.button("Lo que más amo de ti"):
        st.write(
            "Amo tus ojos, tus abrazos (aunque a veces seas un poco distante con el cariño), "
            "y que con una sola palabra puedas mejorar mi ánimo. Amo tu forma única de ser, "
            "incluyendo tus mañas. Eres una persona única en todos los sentidos, y eso me "
            "encanta de ti. 💕"
        )

    if st.button("Nuestro futuro juntos"):
        st.write(
            "¡Waa! Esto es lo que más me encanta hablar contigo. Me imagino un futuro a tu lado, "
            "lleno de leseras, riendo y cumpliendo las cosas que queremos. Quiero estar contigo "
            "en todo, apoyarte y amarte todos los días. ¡Ah! Y lo de ir al sur sí o sí, jajaja. 🌄💑"
        )

    if st.button("Feliz Día 💐"):
        st.write(
            "Mi amor, hoy es un día especial porque celebramos lo increíble que eres. "
            "Eres una mujer fuerte, hermosa y maravillosa. Te mereces todo lo lindo del mundo. "
            "Gracias por estar en mi vida. ¡Feliz Día de la Mujer! 💖🌸"
        )
else:
    st.markdown('<p class="mensaje">Oh, mi niña, todavía no es el tiempo...</p>', unsafe_allow_html=True)
