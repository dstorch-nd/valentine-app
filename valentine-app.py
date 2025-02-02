import streamlit as st
import random

def main():
    if "no_button_position" not in st.session_state:
        st.session_state.no_button_position = (50, 50)

    if "valentine" not in st.session_state:
        st.session_state.valentine = False

    if not st.session_state.valentine:
        col1, col2, col3 = st.columns([1.75, 2, 1])
        with col2:
            st.image("snoopy-hugging-woodstock.jpg", width=150)
        st.markdown("<h1 style='text-align: center;'>Claire, will you be my Valentine?</h1>", unsafe_allow_html=True)

        button_style = """
            <style>
                .stButton button {
                    font-size: 24px;
                    padding: 20px;
                    width: 200px;
                    margin: 10px;
                }
                .stButton {
                    display: inline-block;
                    margin-left: 20px;
                    margin-right: 20px;
                }
            </style>
        """
        col1, col2, col3 = st.columns([2, 2, 1])
        with col2:
            if st.button("Yes 💖"):
                st.session_state.valentine = True
                st.rerun()
            
            no_x, no_y = st.session_state.no_button_position
            no_button = st.button("No ❌", key="no")
            
            if no_button:
                pass

    else:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image("snoopy-cheering.jpg", width = 500)
        st.markdown("<h1 style='text-align: center;'>Yay! Happy Valentine's Day! 💕</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center;'>T-Minus two weeks until I see you!</h2>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()