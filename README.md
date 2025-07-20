# ☀️ Solar Feasibility Calculator

A simple and intuitive web application to calculate the feasibility and payback period of installing solar panels on your roof. Built with Python and Streamlit.

## 🎯 Features

- **System Sizing**: Calculate optimal solar system size based on available roof area
- **Financial Analysis**: Determine payback period and monthly savings
- **Energy Generation**: Estimate monthly electricity generation
- **Cost Analysis**: Calculate total system installation cost
- **Interactive UI**: Clean and user-friendly interface with real-time calculations
- **Smart Insights**: Coverage percentage and excess generation analysis

## 🔧 Technologies Used

- **Backend**: Python
- **Frontend**: Streamlit
- **Libraries**: Built-in Python libraries only 

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Raushani84-ag/solar-feasibility-calculator.git
   cd solar-feasibility-calculator
   ```

2. **Install required packages**
   ```bash
   pip install streamlit
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - If it doesn't open automatically, navigate to the URL shown in your terminal

## 📁 Project Structure

```
solar-feasibility-calculator/
│
├── app.py                 # Streamlit frontend application
├── solar_backend/
│   └── calculator.py      # Solar calculation logic
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
└── .gitignore            # Git ignore file
```

## 🔍 How It Works

### Input Parameters

1. **System Parameters**
   - **Roof Area**: Available roof space for solar panel installation (sq meters)
   - **Monthly Consumption**: Your average monthly electricity usage (kWh)

2. **Financial Parameters**
   - **Tariff Rate**: Current electricity cost per unit (₹/kWh)
   - **System Cost**: Solar installation cost per watt (₹/Watt)

3. **Environmental Parameter**
   - **Solar Irradiance**: Average daily solar irradiance in your location (kWh/m²/day)

### Calculations

- **System Size**: Based on roof area and panel efficiency (10%)
- **Monthly Generation**: System size × irradiance × 30 days × performance ratio (75%)
- **Monthly Savings**: Monthly consumption × tariff rate
- **Total Cost**: System size × cost per watt × 1000
- **Payback Period**: Total cost ÷ annual savings

## 💡 Usage Example

```python
from solar_backend.calculator import SolarCalculator

# Create calculator instance
calculator = SolarCalculator(
    roof_area_sqm=100,
    monthly_electricity_consumption_kwh=300,
    tariff_rate=5.0,
    cost_per_watt=50,
    irradiance=5.0
)

# Get results
results = calculator.get_summary()
print(results)
```

## 📊 Sample Output

```
System Size: 10.0 kW
Monthly Generation: 1125.0 kWh
Monthly Savings: ₹1,500.00
Total Cost: ₹5,00,000.00
Payback Period: 27.8 years
```

## ⚙️ Configuration

The calculator uses the following default assumptions:
- **Panel Efficiency**: 10% (real-world average)
- **Performance Ratio**: 75% (accounts for system losses)
- **Days per Month**: 30 (for calculation purposes)

## 🎯 Key Insights

- **Payback Analysis**:
  - ≤ 5 years: Excellent investment
  - 5-8 years: Good investment
  - > 8 years: Consider carefully

- **Coverage Analysis**:
  - Shows percentage of electricity needs covered
  - Highlights excess generation potential
  - Calculates remaining grid dependency

## 🔮 Future Enhancements

- [ ] Add battery storage calculations
- [ ] Include government subsidy calculations
- [ ] Add seasonal variation analysis
- [ ] Export results to PDF
- [ ] Add location-based solar irradiance database
- [ ] Include maintenance cost projections
- [ ] Add financing options calculator

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



## ⚠️ Disclaimer

This calculator provides estimates based on standard assumptions and should not be considered as professional advice. Actual results may vary based on:
- Local weather conditions
- Panel quality and installation
- System maintenance
- Regulatory changes
- Electricity tariff variations

For accurate assessments, please consult with certified solar installers and energy professionals.


---
