import streamlit as st
import datetime

# Definir la fecha de desbloqueo (8 de marzo a las 12:00)
unlock_date = datetime.datetime(2025, 3, 8, 12, 0)

# Obtener la fecha y hora actual
current_time = datetime.datetime.now()

# Si aún no es la fecha de desbloqueo, mostrar el mensaje de espera
if current_time < unlock_date:
    st.title("Oh, mi niña, todavía no es el tiempo ⏳")
    st.write(f"La página se desbloqueará el {unlock_date.strftime('%d de marzo a las %H:%M')}.")
else:
    # Página desbloqueada
    st.title("🌸 ¡Feliz Día, Mi Amor! 🌸")
    st.write("Selecciona un botón para leer tu mensaje especial:")

    # Estilos CSS
    st.markdown("""
        <style>
            body {
                background-color: #ffebf0;
                text-align: center;
                font-family: Arial, sans-serif;
            }
            .stButton>button {
                background-color: #ff66b2;
                color: white;
                font-size: 18px;
                padding: 10px;
                border-radius: 10px;
                border: none;
                cursor: pointer;
                margin: 10px;
            }
            .stButton>button:hover {
                background-color: #ff3385;
            }
        </style>
    """, unsafe_allow_html=True)

    # Botones con mensajes
    if st.button("💖 ¿Por qué me enamoré de ti? 💖"):
        st.write("Me enamoré de ti porque desde el principio hubo una conexión única. En nuestra primera salida, "
                 "yo estaba tan nervioso, algo que nunca me había pasado antes. Supe de inmediato que eras la mujer que quiero en mi vida.")

    if st.button("😍 Lo que más amo de ti 😍"):
        st.write("Amo tus ojos, tus abrazos (aunque a veces seas un poco distante con el cariño), "
                 "y cómo con una sola palabra puedes mejorar mi día. Amo cada maña tuya, porque eres única en todos los sentidos.")

    if st.button("🌍 Nuestro futuro juntos 🌍"):
        st.write("Lo que más me encanta imaginar es nuestro futuro juntos, lleno de momentos felices, "
                 "cumpliendo nuestros sueños y apoyándonos siempre. ¡Y obvio, el viaje al sur sí o sí! 😂")

    if st.button("🎉 Feliz Día 🎉"):
        st.write("Mi amor, en este día especial quiero recordarte lo increíble que eres. No solo eres la mejor pareja, "
                 "sino una mujer fuerte, inteligente y maravillosa. Gracias por ser parte de mi vida. ¡Te amo! 💖")

