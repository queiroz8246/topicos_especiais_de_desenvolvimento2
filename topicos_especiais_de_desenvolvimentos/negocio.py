import streamlit as st

st.title("Calculadora de Saúde Inteligente")
st.text("Analise seu estado fisico e receba recomendações para sua saúde.")
st.divider()

with st.form("Preencha o formulario abaixo com seus dados"):
    coluna1, coluna2, coluna3,   = st.columns(3)

    with coluna1:
       idade = st.number_input("Idade (anos)", 1, 100)

    with coluna2:
       peso = st.number_input( "Peso(Kg)")

    with coluna3:
       natv = st.selectbox("Nivel de atividade", ["Saldavel", "Normal", "Sedentário"])   

    coluna4, coluna5 = st.columns(2)
    with coluna4:
       sex = st.selectbox("Sexo", ["Masculino", "Feminino"]) 

    with coluna5:
      altura =  st.number_input("Altura (cm)", 30,200) 

    st.form_submit_button("enviar")  
st.divider()   


imc = peso / altura ** 2

col1, col2, col3 = st.columns(3)
with col1:
   st.metric(label="idade" , value = idade )
   st.metric(label="peso", value = peso)  
   st.metric(label="Nivel de atividade",  value = natv)
   st.metric(label="sexo", value = sex)   
   st.metric(label="altura", value = altura)

with col3:
   st.success("Matenha a dieta e continue com atividade fisica")