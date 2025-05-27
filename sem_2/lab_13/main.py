import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QComboBox, QMessageBox
from vehicles import Car, Truck, Bus

class VehicleCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vehicle Calculator")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()

        # Выбор типа транспортного средства
        self.vehicle_type_label = QLabel("Select Vehicle Type:")
        self.layout.addWidget(self.vehicle_type_label)
        self.vehicle_type_combo = QComboBox()
        self.vehicle_type_combo.addItems(["Car", "Truck", "Bus"])
        self.layout.addWidget(self.vehicle_type_combo)

        # Ввод параметров
        self.distance_label = QLabel("Distance (km):")
        self.layout.addWidget(self.distance_label)
        self.distance_entry = QLineEdit()
        self.layout.addWidget(self.distance_entry)

        self.load_label = QLabel("Load (%):")
        self.layout.addWidget(self.load_label)
        self.load_entry = QLineEdit()
        self.layout.addWidget(self.load_entry)

        self.fuel_price_label = QLabel("Fuel Price ($/liter):")
        self.layout.addWidget(self.fuel_price_label)
        self.fuel_price_entry = QLineEdit()
        self.layout.addWidget(self.fuel_price_entry)

        # Кнопка расчета
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate)
        self.layout.addWidget(self.calculate_button)

        # Отображение результата
        self.result_label = QLabel("")
        self.layout.addWidget(self.result_label)

        self.central_widget.setLayout(self.layout)

    def calculate(self):
        try:
            vehicle_type = self.vehicle_type_combo.currentText()
            distance = float(self.distance_entry.text())
            load = float(self.load_entry.text())
            fuel_price = float(self.fuel_price_entry.text())

            if vehicle_type == "Car":
                vehicle = Car(distance, load, fuel_price)
            elif vehicle_type == "Truck":
                vehicle = Truck(distance, load, fuel_price)
            elif vehicle_type == "Bus":
                vehicle = Bus(distance, load, fuel_price)
            else:
                raise ValueError("Invalid vehicle type")

            fuel_consumption = vehicle.calculate_fuel_consumption()
            cost = vehicle.calculate_cost()
            time = vehicle.calculate_time()

            result = (
                f"Fuel Consumption: {fuel_consumption:.2f} liters\n"
                f"Cost: ${cost:.2f}\n"
                f"Time: {time:.2f} hours"
            )
            self.result_label.setText(result)
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VehicleCalculator()
    window.show()
    sys.exit(app.exec_())