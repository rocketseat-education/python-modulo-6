from flask import Blueprint, jsonify, request
from src.calculators.calculator_1 import Calculator1

calc_route_bp = Blueprint("calc_routes", __name__)


@calc_route_bp.route("/calculator/1", methods=["POST"])
def calculator1():
    calc = Calculator1()
    calc.calculate(request)

    return jsonify({
        "success": True,
        }), 200
