from flask import Flask, request, jsonify
from sympy import symbols, Eq, solve
import re

app = Flask(__name__)

# Tabla simple de masas molares
molar_masses = {
    "H": 1.008,
    "O": 16.00,
    "C": 12.01,
    "Na": 22.99,
    "Cl": 35.45
}

def calculate_molar_mass(formula):
    elements = re.findall(r'([A-Z][a-z]*)(\d*)', formula)
    mass = 0
    for element, count in elements:
        count = int(count) if count else 1
        if element in molar_masses:
            mass += molar_masses[element] * count
    return mass

@app.route("/molar_mass", methods=["GET"])
def molar_mass():
    formula = request.args.get("formula")
    mass = calculate_molar_mass(formula)
    return jsonify({
        "formula": formula,
        "molar_mass": mass
    })

@app.route("/")
def home():
    return "API de Química funcionando"

if __name__ == "__main__":
    app.run(debug=True)
