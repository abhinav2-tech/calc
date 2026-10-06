import streamlit as st
import math

# Page configuration
st.set_page_config(
    page_title="Conduction Heat Transfer Calculator",
    page_icon="🔥",
    layout="centered"
)

# Title
st.title("🔥Conduction Heat Transfer Calculator")
st.write("Calculate heat transfer through different geometries.")

# Geometry selection
geometry = st.selectbox(
    "Select Geometry",
    ["Plane Wall", "Cylindrical Wall", "Spherical Wall"]
)

st.divider()

# ---------------- PLANE WALL ----------------
if geometry == "Plane Wall":

    st.subheader("Plane Wall")

    k = st.number_input(
        "Thermal conductivity k (W/m·K)",
        min_value=0.0001,
        value=50.0
    )

    A = st.number_input(
        "Area A (m²)",
        min_value=0.0001,
        value=1.0
    )

    L = st.number_input(
        "Wall thickness L (m)",
        min_value=0.0001,
        value=0.1
    )

    T1 = st.number_input(
        "Hot-side temperature T₁ (°C)",
        value=100.0
    )

    T2 = st.number_input(
        "Cold-side temperature T₂ (°C)",
        value=50.0
    )

    if st.button("Calculate Heat Transfer", type="primary"):

        Q = (k * A * (T1 - T2)) / L

        st.success(f"Heat Transfer Rate = {Q:.2f} W")

        st.latex(
            r"Q = \frac{kA(T_1-T_2)}{L}"
        )


# ---------------- CYLINDRICAL WALL ----------------
elif geometry == "Cylindrical Wall":

    st.subheader("Cylindrical Wall")

    k = st.number_input(
        "Thermal conductivity k (W/m·K)",
        min_value=0.0001,
        value=50.0
    )

    L = st.number_input(
        "Cylinder length L (m)",
        min_value=0.0001,
        value=1.0
    )

    r1 = st.number_input(
        "Inner radius r₁ (m)",
        min_value=0.0001,
        value=0.05
    )

    r2 = st.number_input(
        "Outer radius r₂ (m)",
        min_value=0.0001,
        value=0.10
    )

    T1 = st.number_input(
        "Inner temperature T₁ (°C)",
        value=100.0
    )

    T2 = st.number_input(
        "Outer temperature T₂ (°C)",
        value=50.0
    )

    if st.button("Calculate Heat Transfer", type="primary"):

        if r2 <= r1:
            st.error("Outer radius r₂ must be greater than inner radius r₁.")
        else:

            Q = (
                2 * math.pi * k * L * (T1 - T2)
            ) / math.log(r2 / r1)

            st.success(f"Heat Transfer Rate = {Q:.2f} W")

            st.latex(
                r"Q = \frac{2\pi kL(T_1-T_2)}
                {\ln(r_2/r_1)}"
            )


# ---------------- SPHERICAL WALL ----------------
elif geometry == "Spherical Wall":

    st.subheader("Spherical Wall")

    k = st.number_input(
        "Thermal conductivity k (W/m·K)",
        min_value=0.0001,
        value=50.0
    )

    r1 = st.number_input(
        "Inner radius r₁ (m)",
        min_value=0.0001,
        value=0.05
    )

    r2 = st.number_input(
        "Outer radius r₂ (m)",
        min_value=0.0001,
        value=0.10
    )

    T1 = st.number_input(
        "Inner temperature T₁ (°C)",
        value=100.0
    )

    T2 = st.number_input(
        "Outer temperature T₂ (°C)",
        value=50.0
    )

    if st.button("Calculate Heat Transfer", type="primary"):

        if r2 <= r1:
            st.error("Outer radius r₂ must be greater than inner radius r₁.")
        else:

            Q = (
                4 * math.pi * k * (T1 - T2)
            ) / ((1 / r1) - (1 / r2))

            st.success(f"Heat Transfer Rate = {Q:.2f} W")

            st.latex(
                r"Q = \frac{4\pi k(T_1-T_2)}
                {(1/r_1)-(1/r_2)}"
            )


# Footer
st.divider()
st.caption("Conduction Heat Transfer Calculator | Engineering Application")
