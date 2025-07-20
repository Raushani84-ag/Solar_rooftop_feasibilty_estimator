class SolarCalculator:
    def __init__ (self , roof_area_sqm, monthly_electricity_consumption_kwh ,tariff_rate,cost_per_watt , irradiance):

        # user input data
        self.roof_area_sqm = roof_area_sqm
        self.monthly_electricity_consumption_kwh = monthly_electricity_consumption_kwh
        self.tariff_rate = tariff_rate
        self.cost_per_watt = cost_per_watt
        self.irradiance = irradiance


        # required constant values.
        self.panel_efficiency_factor = 0.10    #  avg efficiency in real world = 10%
        self.performance_ratio = 0.75

    def calculate_system_size(self):
        return   round(self.roof_area_sqm * self.panel_efficiency_factor ,2)

    def calculate_monthly_electricity_generation(self):
        size = self.calculate_system_size()
        return round(size* self.irradiance * 30 * self.performance_ratio,2)

    def calculate_monthly_savings(self):
        return  round(self.monthly_electricity_consumption_kwh * self.tariff_rate ,2)


    def calculate_total_cost(self):
        return round(self.calculate_system_size() * self.cost_per_watt * 1000 , 2)

    def calculate_payback_years(self):
        annual_savings = self.calculate_monthly_savings() * 12
        total_cost = self.calculate_total_cost()
        return round(total_cost / annual_savings ,1) if annual_savings > 0 else None

    def get_summary(self):
        return {
            "system_size_kw": self.calculate_system_size(),
            "monthly_electricity_generation_kwh": self.calculate_monthly_electricity_generation(),
            "monthly_savings": self.calculate_monthly_savings(),
            "total_system_cost" : self.calculate_total_cost(),
            "payback_years" : self.calculate_payback_years()
        }


if __name__ == "__main__":
    try:
        # Test the calculator
        calculator = SolarCalculator(
            roof_area_sqm=100,
            monthly_electricity_consumption_kwh=300,
            tariff_rate=9.5,
            cost_per_watt=50,
            irradiance=5.0
        )

        print("=== Solar Feasibility Calculator Results ===")
        results = calculator.get_summary()

        for key, value in results.items():
            print(f"{key.replace('_', ' ').title()}: {value}")

    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"Calculation Error: {e}")
