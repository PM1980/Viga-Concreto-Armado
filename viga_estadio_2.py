import streamlit as st

def calculate_moment_of_resistance(b, d, Aaço, Eaço, Econc, sigma_aço, sigma_conc):
    n = Eaço / Econc
    x = (-n*Aaço + ((n*Aaço)**2 +2*b*n*Aaço*d)**(1/2)) * (1/b)
    Ieq = (b*x**3/12) + (b*x)*(x/2)**2 + n * Aaço * (d-x)**2
    Mconc = sigma_conc * Ieq / x
    Maço = sigma_aço * Ieq / ((d-x) * n)
    Madm = min(Mconc, Maço)
    return x, Ieq, Mconc, Maço, Madm

def main():
    st.title("Moment of Resistance Calculator")
    st.write("Enter the values to calculate the moment of resistance")

    b = st.text_input("Base of the section (m)", value='0.20')
    d = st.text_input("Effective height of the section (m)", value='0.50')
    Aaço = st.text_input("Total area of reinforcement (m2)")
    Eaço = st.text_input("Elastic modulus of steel (GPa)", value='200')
    Econc = st.text_input("Elastic modulus of concrete (GPa)", value='20')
    sigma_aço = st.text_input("Allowable stress for steel (Pa)", value='250e6')
    sigma_conc = st.text_input("Allowable stress for concrete (Pa)", value='10e6')

    if st.button("Calculate"):
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

            st.success(f"x: {x} m")
            st.success(f"Ieq: {Ieq} m^4")
            st.success(f"Mconc: {Mconc} N.m")
            st.success(f"Maço: {Maço} N.m")
            st.success(f"Madm: {Madm} N.m")
        except ValueError:
            st.error("Please enter valid numerical values")

if __name__ == "__main__":
    main()
