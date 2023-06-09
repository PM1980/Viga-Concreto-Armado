import streamlit as st
from PIL import Image

def calculate_moment_of_resistance(b, d, Aaço, Eaço, Econc, sigma_aço, sigma_conc):
    n = Eaço / Econc
    x = (-n*Aaço + ((n*Aaço)**2 +2*b*n*Aaço*d)**(1/2)) * (1/b)
    Ieq = (b*x**3/12) + (b*x)*(x/2)**2 + n * Aaço * (d-x)**2
    Mconc = sigma_conc * Ieq / x
    Maço = sigma_aço * Ieq / ((d-x) * n)
    Madm = min(Mconc, Maço)
    return x, Ieq, Mconc, Maço, Madm

def main():
    st.title("Calculadora para verificação de vigas em concreto armado no Estádio II - seção retangular")
    img = Image.open("secao_homogenea_concreto.png")
    st.image(img)
    st.markdown(
        '''
        <div style="border: 1px solid black; padding: 10px;">
            Universidade Federal de Pernambuco - UFPE / Departamento de Engenharia Civil - DECIV <br>
            Aplicativo desenvolvido para a disciplina CI219 - Resistência dos Materiais 2A <br>
            Autor: Paulo M. V. Ribeiro <br>
            Data: 06/2023
        </div>
        ''',
        unsafe_allow_html=True
    )
    
    st.markdown('<span style="color: red;">*Digite os valores nos campos abaixo para a avaliação do momento fletor admissível*</span>', unsafe_allow_html=True)

    b = st.text_input("Base da seção - b (m)", value='0.20')
    d = st.text_input("Altura útil - d (m)", value='0.50')
    Aaço = st.text_input("Área de aço - Aaço (m2)", value ='0.000314')
    Eaço = st.text_input("Módulo de elasticidade do aço - Eaço (GPa)", value='200')
    Econc = st.text_input("Módulo de elasticidade do concreto - Econc (GPa)", value='20')
    sigma_aço = st.text_input("Tensão admissível do aço (Pa)", value='250e6')
    sigma_conc = st.text_input("Tensão admissível do concreto (Pa)", value='10e6')

    if st.button("Calcular"):
        try:
            b = float(b)
            d = float(d)
            Aaço = eval(Aaço)
            Eaço = float(Eaço)
            Econc = float(Econc)
            sigma_aço = eval(sigma_aço)
            sigma_conc = eval(sigma_conc)

            x, Ieq, Mconc, Maço, Madm = calculate_moment_of_resistance(
                b, d, Aaço, Eaço, Econc, sigma_aço, sigma_conc
            )

            st.text(f"Posição da linha neutra (x): {x} m")
            st.text(f"Momento de inércia da seção transformada (Ieq): {Ieq} m^4")
            st.text(f"Momento fletor admissível para o concreto: {Mconc} N.m")
            st.text(f"Momento fletor admissível para o aço: {Maço} N.m")
            st.text(f"Momento fletor admissível da viga: {Madm} N.m")
            
            if Mconc < Maço:
                st.markdown("**Concreto governa o problema**")
            else:
                st.markdown("**Aço governa o problema**")
            
        except ValueError:
            st.error("Please enter valid numerical values")

if __name__ == "__main__":
    main()
