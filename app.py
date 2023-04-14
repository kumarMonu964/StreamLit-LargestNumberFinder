#import the streamlit library as st
import streamlit as st

st.image("https://tse3.explicit.bing.net/th?id=OIP.LkW3JWqDBuB6RdixIdypZAHaBO&pid=Api&P=0",width=700)
with st.form("form3"):
    st.markdown("<u><h1 style='color:maroon;background-color:DarkBlue;text-align:center'>Largest Number Calculator</h1></u>",unsafe_allow_html=True)
    st.markdown("><i>  This calculator outputs the greatest of the 3 numbers.</i>",unsafe_allow_html=True)
    col1,col2,col3=st.columns(3)
    first_number=col1.number_input("Enter first number:",step=1)
    second_number=col2.number_input("Enter second number:",step=1)
    third_number=col3.number_input("Enter third number:",step=1)
    
    res=max(first_number,second_number,third_number)
    
    col5,col6,col7=st.columns(3)
    
    col6.write(f"The largest number is {res} .")
    c1,c2,c3=st.columns(3)
    c1.form_submit_button("Display",help="Click on it to get the output!")
    
with st.container():
    st.markdown("## > About the coder:")
    st.image("monu_pic.jpeg",width=100)
    st.markdown("### Name: Monu")
    st.markdown("### Roll No.: 21f1003892")
    st.markdown("### Email id : 21f1003892@ds.study.iitm.ac.in")
    st.markdown("### Course : Tools in Data Science")
    st.markdown("### LinkedIn : https://www.linkedin.com/in/monu-kumar-1b2064207")
    


#css styling
st.markdown("""
<style>
.css-h5rgaw.egzxvld1 {visibility:hidden;}
.css-9s5bis.edgvbvh3 {visibility:hidden;}
.css-uf99v8.egzxvld5 {background-color:SkyBlue;}
.css-12ttj6m.epcbefy1 {background-color:LightSeaGreen ;}
.css-5rimss.e16nr0p34 {background-color:MidnightBlue ;text-align:center;color:white;}
.css-10trblm.e16nr0p30 {color:white;text-align:left}
.css-1v0mbdj.etr89bj1 {display: block;
  margin-left: auto;
  margin-right: auto;}
.css-18ni7ap.e8zbici2 {background-color:deepskyblue;}
</style>
""",unsafe_allow_html=True)
