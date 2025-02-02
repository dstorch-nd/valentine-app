import streamlit as st
import random

def main():
    if "no_button_position" not in st.session_state:
        st.session_state.no_button_position = (50, 50)

    if "valentine" not in st.session_state:
        st.session_state.valentine = False

    if not st.session_state.valentine:
        st.image("snoopy-hugging-woodstock.jpg", use_container_width=True)
        #st.title("Claire, will you be my Valentine?")
        st.markdown("<h1 style='text-align: center;'>Will you be my Valentine?</h1>", unsafe_allow_html=True)
        st.markdown("""
            <div style='display: flex; justify-content: center; gap: 20px;'>
                <button onclick='yesClicked()' style='font-size: 24px; padding: 20px 40px;'>Yes 💖</button>
                <button onclick='noClicked()' style='font-size: 24px; padding: 20px 40px;'>No ❌</button>
            </div>
        """, unsafe_allow_html=True)
        
        #col1, col2 = st.columns([1,1], gap='large')
        #with col1:
        #    if st.button("Yes 💖"):
        #        st.session_state.valentine = True
        #        st.rerun()
        
        #with col2:
        #    no_x, no_y = st.session_state.no_button_position
        #    no_button = st.button("No ❌", key="no")
            
        #    if no_button:
        #        new_x = random.randint(0, 90)
        #        new_y = random.randint(0, 90)
        #        st.session_state.no_button_position = (new_x, new_y)
        #        st.rerun()

        if st.button("Yes 💖", key="yes", help="Click to accept!"):
            st.session_state.valentine = True
            st.rerun()
        
        no_x, no_y = st.session_state.no_button_position
        no_button = st.button("No ❌", key="no", help="Click to refuse!")
        
        if no_button:
            new_x = random.randint(0, 90)
            new_y = random.randint(0, 90)
            st.session_state.no_button_position = (new_x, new_y)
            st.rerun()
            
    else:
        st.image("snoopy-cheering.jpg", use_container_width=True)
        st.markdown("<h1 style='text-align: center;'>Yay! Happy Valentine's Day! 💕</h1>", unsafe_allow_html=True)
        #st.title("Yay! Happy Valentine's Day! 💕")
        st.write("You made the right choice! 😊")

if __name__ == "__main__":
    main()