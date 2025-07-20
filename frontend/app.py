import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solar_backend.calculator import SolarCalculator


import streamlit as st


# Page configuration
st.set_page_config(
    page_title="Solar Feasibility Calculator",
    page_icon="☀️",
    layout="centered"
)

# Title and description
st.title("☀️ Solar Feasibility Calculator")
st.markdown("Calculate the feasibility and payback period of installing solar panels on your roof.")

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    st.subheader(" System Parameters")
    roof_area = st.number_input(
        "Roof Area (sq meters)",
        min_value=1.0,
        max_value=1000.0,
        value=100.0,
        step=1.0,
        help="Available roof area for solar panel installation"
    )

    monthly_consumption = st.number_input(
        "Monthly Electricity Consumption (kWh)",
        min_value=1.0,
        max_value=10000.0,
        value=300.0,
        step=10.0,
        help="Your average monthly electricity usage"
    )

with col2:
    st.subheader("Financial Parameters")
    tariff_rate = st.number_input(
        "Electricity Tariff Rate (₹/kWh)",
        min_value=0.1,
        max_value=50.0,
        value=5.0,
        step=0.1,
        help="Cost per unit of electricity"
    )

    cost_per_watt = st.number_input(
        "Solar System Cost (₹/Watt)",
        min_value=10.0,
        max_value=200.0,
        value=50.0,
        step=1.0,
        help="Installation cost per watt of solar capacity"
    )

# Environmental parameter
st.subheader("Environmental Parameter")
irradiance = st.number_input(
    "Daily Solar Irradiance (kWh/m²/day)",
    min_value=1.0,
    max_value=10.0,
    value=5.0,
    step=0.1,
    help="Average daily solar irradiance in your location"
)

# Add some spacing
st.markdown("---")

# Calculate button
if st.button("Calculate Solar Feasibility", type="primary"):
    try:
        # Create calculator instance
        calculator = SolarCalculator(
            roof_area_sqm=roof_area,
            monthly_electricity_consumption_kwh=monthly_consumption,
            tariff_rate=tariff_rate,
            cost_per_watt=cost_per_watt,
            irradiance=irradiance
        )

        # Get results
        results = calculator.get_summary()

        # Display results in columns
        st.subheader("📊 Calculation Results")

        result_col1, result_col2 = st.columns(2)

        with result_col1:
            st.metric(
                label="System Size",
                value=f"{results['system_size_kw']} kW",
                help="Recommended solar system capacity"
            )

            st.metric(
                label="Monthly Generation",
                value=f"{results['monthly_electricity_generation_kwh']} kWh",
                help="Expected monthly electricity generation"
            )

        with result_col2:
            st.metric(
                label="Monthly Savings",
                value=f"₹{results['monthly_savings']:,.2f}",
                help="Expected monthly electricity bill savings"
            )

            st.metric(
                label="Total System Cost",
                value=f"₹{results['total_system_cost']:,.2f}",
                help="Total installation cost"
            )

        # Payback period with conditional formatting
        payback_years = results['payback_years']
        if payback_years:
            if payback_years <= 5:
                st.success(f" Excellent! Payback Period: {payback_years} years")
            elif payback_years <= 8:
                st.info(f" Good! Payback Period: {payback_years} years")
            else:
                st.warning(f" Consider carefully. Payback Period: {payback_years} years")
        else:
            st.error("Unable to calculate payback period. Check your inputs.")

        # Additional insights
        st.subheader(" Insights")
        generation = results['monthly_electricity_generation_kwh']
        consumption = monthly_consumption

        if generation >= consumption:
            excess = generation - consumption
            st.success(f"✅ Your system will generate {excess:.1f} kWh excess electricity monthly!")
        else:
            deficit = consumption - generation
            coverage = (generation / consumption) * 100
            st.info(
                f"Your system will cover {coverage:.1f}% of your electricity needs. You'll still need {deficit:.1f} kWh from the grid monthly.")

        # Annual savings
        annual_savings = results['monthly_savings'] * 12
        st.info(f" Estimated annual savings: ₹{annual_savings:,.2f}")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Add footer with information
st.markdown("---")
st.markdown("""
**Note:** This calculator provides estimates based on standard assumptions:
- Panel efficiency: 10% (real-world average)
- Performance ratio: 75% (accounting for losses)
- Results may vary based on actual conditions, panel quality, and installation factors.
""")
