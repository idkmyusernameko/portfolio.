import streamlit as st
st.title(" ✨ Mohammed Shayan.")
st.subheader("A 12 year old Python developer.")
cols = st.columns(2)
st.subheader('About me')
about = cols[0]
about.write('''Hello There! I am Mohammed Shayan 
                         I am a 12 year old Python developer.
                         I am currently learning in Class 7.
                         I study in Devamatha which is situated in Kerala, India. 
                         I started coding only a few months ago.
                         So don't bully me😭 
                      ''')
st.subheader('Socials')
social = cols[1]
social.markdown(f'<a href="https://instagram.com/idkmyusernameko"><b>Instagram</b></a>', unsafe_allow_html=True)
social.markdown(f'<a href="https://github.com/idkmyusernameko">GitHub</a>', unsafe_allow_html=True)
st.balloons()
st.write('Reach out to me')
st.write('I know this is trash so tell me the improvements I should make')
