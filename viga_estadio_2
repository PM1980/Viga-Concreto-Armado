import streamlit as st
import sympy as sp

def calculate_moment_of_resistance(b, d, Aaco, Eaco, Econc, sigma_aco, sigma_conc):
    n = Eaco / Econc
    x = sp.symbols('x')
    eq_linha_neutra = b * x**2/2 - n * Aaco * (d-x)
    sol = sp.solve(eq_linha_neutra)
    x = max(sol)
    Ieq = (b*x**3/12) + (b*x)*(x/2)**2 + n * Aaco * (d-x)**2
    Mconc = sigma_conc * Ieq / x
    Maco = sigma_aco * Ieq / ((d-x) * n)
    return min(Mconc, Maco)

def main():
    st.title("Moment of Resistance Calculator")
    st.write("Enter the values to calculate the moment of resistance")

    b = st.text_input("Base of the section (m)")
    d = st.text_input("Effective height of the section (m)")
    Aaco = st.text_input("Total area of reinforcement (m2)")
    Eaco = st.text_input("Elastic modulus of steel (GPa)")
    Econc = st.text_input("Elastic modulus of concrete (GPa)")
    sigma_aco = st.text_input("Allowable stress for steel (Pa)")
    sigma_conc = st.text_input("Allowable stress for concrete (Pa)")

    if st.button("Calculate"):
        try:
            b = float(b)
            d = float(d)
            Aaco = float(Aaco)
            Eaco = float(Eaco)
            Econc = float(Econc)
            sigma_aco = float(sigma_aco)
            sigma_conc = float(sigma_conc)

            moment_of_resistance = calculate_moment_of_resistance(
                b, d, Aaco, Eaco, Econc, sigma_aco, sigma_conc
            )

            st.success(f"The moment of resistance is: {moment_of_resistance} N.m")
        except ValueError:
            st.error("Please enter valid numerical values")

if __name__ == "__main__":
    main()
