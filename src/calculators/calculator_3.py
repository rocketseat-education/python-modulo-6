from flask import request as FlaskRequest
from typing import Dict
from src.drivers.interfaces.driver_handler_interface import (
    DriverHandlerInterface
)


class Calculator3:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
        pass
