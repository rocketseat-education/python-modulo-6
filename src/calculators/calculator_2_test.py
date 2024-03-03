from .calculator_2 import Calculator2
from typing import Dict


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculate():
    mock_request = MockRequest({
        "numbers": [2.12, 4.62, 1.32]
        })  # type: ignore

    calculator_2 = Calculator2
    formated_response = calculator_2.calculate(mock_request)

    assert isinstance(formated_response, dict)
    assert formated_response == {'data': {'Calculator': 2, 'result': 0.08}}
