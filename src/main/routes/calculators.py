from flask import Blueprint, jsonify, request

calc_route_bp = Blueprint("calc_routes", __name__)


@calc_route_bp.route("/calculator/1", methods=["POST"])
def calculator1():
    print(request)
    return jsonify({
        "success": True,
        }), 200
