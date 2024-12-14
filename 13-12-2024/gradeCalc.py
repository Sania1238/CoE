import streamlit as st
st.title("EVEN OR ODD")
num1 = st.number_input("Enter number",min_value=1,step=1)

if st.button("Even/Odd"):
    if num1%2 == 0:
        st.success("Even number")
    else:
        st.error("Odd number")

===========================================================

import streamlit as st
st.title("Gross Salary Calculator")
st.header("Lets calculate")
st.subheader("Chin up")
st.text("You ready?")
st.image('im1.jpg')

basic_salary = st.number_input("Enter your Basic Salary: ",min_value=0, step=1)
if st.button("Calculate Gross Salary"):
    hra = 0
    da = 0

    if basic_salary < 10000:
        hra = basic_salary*0.67
        da = basic_salary*0.73
    elif 10000 <= basic_salary <= 20000:
        hra = basic_salary*0.69
        da = basic_salary*0.76
    else:
        hra = basic_salary*0.73
        da = basic_salary*0.89
    gs= hra + da + basic_salary
    st.success(gs)

=============================================================


import streamlit as st

def grade (project,internal,external):
   if project < 50:
       st.error(f"Failed in project, score: {project}")
   if internal < 50:
       st.error(f"Failed in internal , score: {internal}")
   if external < 50:
       st.error(f"Failed in external , score: {external}")
   elif project>=50 and internal>=50 and external>=50:
        project = project * 0.70
        internal = internal * 0.10
        external = external * 0.20
        total_marks = project*0.70+internal*0.10+external*0.20
        if total_marks>90:
            st.success("'A' grade")
        elif 80<total_marks<=90:
            st.success("'B' grade")
        else:
            st.success("'C' grade")


st.title("Check your score")
project = st.number_input("Enter the marks in project:", min_value=0, max_value=100, step=1)
internal = st.number_input("Enter the marks in internal:", min_value=0, max_value=100, step=1)
external = st.number_input("Enter the marks in external:", min_value=0, max_value=100, step=1)
if st.button("Calculate Grade"):
    grade(project, internal, external)
    