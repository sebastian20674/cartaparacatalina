import streamlit as st

def main():
    st.set_page_config(page_title="Carta para Catita 💖", page_icon="💌", layout="centered")
    
    # Título
    st.title("Carta para Catita 💖")
    
    # Pedir código
    codigo = st.text_input("Ingresa el código para ver la carta 💌", type="password")
    
    if codigo == "250225":
        st.success("Código correcto! Aquí está tu carta, mi wawa 💖")
        
        st.markdown(
            """
            **Catita,**  
            Cada día que me despierto, lo primero en lo que pienso eres tú. El pensamiento de ti, de lo que compartimos y de lo que somos, es lo que me da fuerzas para empezar el día con una sonrisa. A veces, aunque esté en medio de mil cosas, mi mente siempre regresa a ti, a cómo haces que mi vida sea más bonita, más tranquila, más feliz.  
            
            Sé que las cosas no siempre son fáciles, que a veces los problemas nos rodean y las dudas intentan colarse. Pero quiero que sepas que, pase lo que pase, siempre estaré a tu lado. No importa la distancia ni lo que nos toque enfrentar, lo que siento por ti es más fuerte que cualquier obstáculo. Estoy convencido de que no hay nada que pueda separar lo que hemos construido juntos.  
            
            Aunque a veces el futuro se vea incierto, y aunque tenga que irme por un tiempo, quiero que sepas que eso no cambiará lo que siento. Un año puede parecer mucho, pero nuestro amor no se mide en días ni en kilómetros. Lo que más quiero en este mundo es que sigamos juntos, que cada paso que dé sea contigo, que todo lo que viva, lo viva con la esperanza de que, al final del día, siempre habrá un regreso a tus brazos.  
            
            Este tiempo que me pueda ir no será más que una prueba de lo que somos, de lo fuerte que es lo que tenemos. No quiero que pienses ni por un momento que eso afectará lo que tenemos, porque estoy seguro de que esto solo hará que valoremos aún más todo lo que compartimos. No hay distancia que pueda alejarnos del todo, y aunque no estemos físicamente cerca, te llevo conmigo en cada segundo.  
            
            Quiero que sepas que el futuro que tengo en mente está lleno de nosotros. En mis sueños, en mis planes, siempre estás tú. Lo que más deseo es que sigamos construyendo juntos, que todo lo que venga lo hagamos de la mano. Me veo a tu lado en cada paso de la vida, compartiendo todo lo que somos y lo que podemos ser.  
            
            Te amo más de lo que las palabras pueden decir, y estoy agradecido por cada momento que hemos compartido. No importa lo que venga, porque mientras tú y yo estemos juntos, todo será posible.  
            
            **Con todo mi amor,**  
            **Sebita 💞**
            """, unsafe_allow_html=True
        )
    elif codigo:
        st.error("Código incorrecto. Intenta de nuevo.")
    
if __name__ == "__main__":
    main()
