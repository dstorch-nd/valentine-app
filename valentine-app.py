import streamlit as st
import random

def main():
    if "no_button_position" not in st.session_state:
        st.session_state.no_button_position = (50, 50)

    if "valentine" not in st.session_state:
        st.session_state.valentine = False

    if not st.session_state.valentine:
        st.image("valentine_photo.jpg", use_column_width=True)
        st.title("Will you be my Valentine?")
        
        col1, col2 = st.columns([1,1])
        with col1:
            if st.button("Yes 💖"):
                st.session_state.valentine = True
                st.experimental_rerun()
        
        with col2:
            no_x, no_y = st.session_state.no_button_position
            no_button = st.button("No ❌", key="no")
            
            if no_button:
                new_x = random.randint(0, 90)
                new_y = random.randint(0, 90)
                st.session_state.no_button_position = (new_x, new_y)
                st.experimental_rerun()
            
    else:
        st.image("happy_photo.jpg", use_column_width=True)
        st.title("Yay! Happy Valentine's Day! 💕")
        st.write("You made the right choice! 😊")

if __name__ == "__main__":
    main()