import streamlit as st
import math

st.title("🔥 Conduction Heat Transfer Calculator")

g = st.selectbox("Select Geometry", ["Plane Wall", "Cylindrical Wall", "Spherical Wall"])

k = st.number_input("Thermal Conductivity k (W/m·K)", min_value=0.01)
T1 = st.number_input("Hot Temperature T₁ (°C)")
T2 = st.number_input("Cold Temperature T₂ (°C)")

if g == "Plane Wall":
    A = st.number_input("Area A (m²)", min_value=0.01)
    L = st.number_input("Thickness L (m)", min_value=0.01)

    if st.button("Calculate"):
        Q = k * A * (T1 - T2) / L
        st.success(f"Heat Transfer Rate = {Q:.2f} W")

elif g == "Cylindrical Wall":
    r1 = st.number_input("Inner Radius r₁ (m)", min_value=0.01)
    r2 = st.number_input("Outer Radius r₂ (m)", min_value=0.01)
    L = st.number_input("Length L (m)", min_value=0.01)

    if st.button("Calculate"):
        if r2 <= r1:
            st.error("r₂ must be greater than r₁")
        else:
            Q = 2 * math.pi * k * L * (T1 - T2) / math.log(r2 / r1)
            st.success(f"Heat Transfer Rate = {Q:.2f} W")

else:
    r1 = st.number_input("Inner Radius r₁ (m)", min_value=0.01)
    r2 = st.number_input("Outer Radius r₂ (m)", min_value=0.01)

    if st.button("Calculate"):
        if r2 <= r1:
            st.error("r₂ must be greater than r₁")
        else:
            Q = 4 * math.pi * k * (T1 - T2) / (1/r1 - 1/r2)
            st.success(f"Heat Transfer Rate = {Q:.2f} W")
