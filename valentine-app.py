import streamlit as st
import random

def main():
    if "no_button_position" not in st.session_state:
        st.session_state.no_button_position = (50, 50)

    if "valentine" not in st.session_state:
        st.session_state.valentine = False

    if not st.session_state.valentine:
        #st.markdown("<div style='text-align: center;'><img src='snoopy-hugging-woodstock.jpg' width='400'></div>", unsafe_allow_html=True)
        #st.image("snoopy-hugging-woodstock.jpg", width=400)
        #st.image("snoopy-hugging-woodstock.jpg", width = 400)
        #st.title("Claire, will you be my Valentine?")
        col1, col2, col3 = st.columns([1, 2, 1])  # 2 is the main column width
        with col2:
            st.image("snoopy-hugging-woodstock.jpg", width=400)
        
        st.markdown("<h1 style='text-align: center;'>Claire, will you be my Valentine?</h1>", unsafe_allow_html=True)

        col = st.columns([1])[0]
        with col:
            # Increase the button size by applying a style
            button_style = """
                <style>
                    .stButton button {
                        font-size: 24px;
                        padding: 20px;
                    }
                </style>
            """
            st.markdown(button_style, unsafe_allow_html=True)

            if st.button("Yes 💖"):
                st.session_state.valentine = True
                st.rerun()
        
            no_x, no_y = st.session_state.no_button_position
            no_button = st.button("No ❌", key="no")
            
            if no_button:
                pass

    else:
        #st.markdown("<div style='text-align: center;'><img src='snoopy-cheering.jpg' width='500'></div>", unsafe_allow_html=True)
        st.image("snoopy-cheering.jpg", width = 500)
        st.markdown("<h1 style='text-align: center;'>Yay! Happy Valentine's Day! 💕</h1>", unsafe_allow_html=True)
        #st.title("Yay! Happy Valentine's Day! 💕")
        #st.write("You made the right choice! 😊")
        st.markdown("<h2 style='text-align: center;'>T-Minus two weeks until I see you!</h2>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()