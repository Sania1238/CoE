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