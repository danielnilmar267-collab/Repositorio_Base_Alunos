import streamlit as st
st.title("Atacadão fc - contrata mais que o Atacadao")

st.sidebar.image("logo.png")
nome = st.text_input("Digite o nome do Funcionário")
idade = st.number_input("Digite a idade", min_value=18, max_value=100, step=1)
email = st.text_input("Digite o e-mail")
salario = st.text_input("Digite o salario do Funcionario")
cargo = st.text_input("Digite o cargo")

if st.button("cadastrar"):
    st.warning(f"O fucionario {nome}, foi cadastrado com sucesso")
    st.balloons()
    st.image('https://thispersondoesnotexist.com/')