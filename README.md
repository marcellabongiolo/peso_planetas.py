# 🪐 Planetary Weight Calculator (`peso_planetas.py`)

<p align="center">
  <!-- Ícone animado simulando o espaço/planetas -->
  <img src="https://raw.githubusercontent.com/ABSphreak/ABSphreak/master/gitHub-config/gitHub-stats.svg" width="100%" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="License">
</p>

---

## 🌌 About the Project

**`peso_planetas.py`** is an interactive Python script that calculates your body weight on different planets of our Solar System based on your Earth weight and the specific surface gravity of each celestial body. 

As a Software Engineering student at UNESC, I developed this project to practice control structures, mathematical formulas, and clean input/output formatting in Python.

---

## 🌍 Planetary Gravity Reference

The script uses standard physics formulas based on the surface gravity acceleration ($g$) of each planet compared to Earth ($1g$):

| Planet | Gravity Factor ($g$) | Description |
| :--- | :---: | :--- |
| **Mercury** | $0.38$ | Lighter due to smaller mass |
| **Venus** | $0.91$ | Slightly lower than Earth |
| **Mars** | $0.38$ | Red planet's reduced gravity |
| **Jupiter** | $2.34$ | Massive gas giant (very heavy!) |
| **Saturn** | $1.06$ | Ringed giant, close to Earth's feel |
| **Uranus** | $0.92$ | Ice giant |
| **Neptune** | $1.19$ | Outer ice giant |

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/marcellabongiolo/peso_planetas.git](https://github.com/marcellabongiolo/peso_planetas.git)
cd peso_planetas
python peso_planetas.py
# Quick look at how the calculation logic works:
gravity_factors = {
    "Mercury": 0.38,
    "Venus": 0.91,
    "Mars": 0.38,
    "Jupiter": 2.34,
    "Saturn": 1.06,
    "Uranus": 0.92,
    "Neptune": 1.19
}

earth_weight = float(input("Enter your weight on Earth (kg): "))
for planet, factor in gravity_factors.items():
    planet_weight = earth_weight * factor
    print(f"Your weight on {planet}: {planet_weight:.2f} kg")
    👩‍💻 Author
Marcella Bongiolo

Software Engineering Student at UNESC

GitHub: github.com/marcellabongiolo

LinkedIn: linkedin.com/in/marcellabongiolo

   
