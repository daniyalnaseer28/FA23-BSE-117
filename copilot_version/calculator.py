import operator
from typing import Callable, Dict


class CalculatorError(Exception):
    """Custom exception raised for calculator-related errors."""
    pass


class Calculator:
    """A simple calculator supporting basic arithmetic operations."""

    def __init__(self) -> None:
        self.operations: Dict[str, Callable[[float, float], float]] = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": self._safe_divide,
        }

    @staticmethod
    def _safe_divide(a: float, b: float) -> float:
        """Divide a by b, raising a CalculatorError on division by zero."""
        if b == 0:
            raise CalculatorError("Cannot divide by zero.")
        return a / b

    def calculate(self, a: float, op: str, b: float) -> float:
        """Perform the calculation for the given operator."""
        if op not in self.operations:
            raise CalculatorError(f"Unsupported operator: '{op}'")
        return self.operations[op](a, b)


def parse_expression(expression: str):
    """
    Parse a string like '5 + 3' into (num1, operator, num2).
    Raises CalculatorError if the format is invalid.
    """
    tokens = expression.strip().split()
    if len(tokens) != 3:
        raise CalculatorError("Expected format: <number> <operator> <number>")

    num1_str, op, num2_str = tokens

    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
    except ValueError as exc:
        raise CalculatorError("Both operands must be valid numbers.") from exc

    return num1, op, num2


def run() -> None:
    """Run the interactive calculator loop."""
    calculator = Calculator()

    print("=== Simple Calculator (Copilot-assisted) ===")
    print("Supported operators: +, -, *, /")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        try:
            expression = input("Enter expression: ").strip()

            if expression.lower() in ("exit", "quit"):
                print("Exiting calculator. Goodbye!")
                break

            num1, op, num2 = parse_expression(expression)
            result = calculator.calculate(num1, op, num2)
            print(f"Result: {result}\n")

        except CalculatorError as e:
            print(f"Error: {e}\n")
        except KeyboardInterrupt:
            print("\nExiting calculator. Goodbye!")
            break


if __name__ == "__main__":
    run()
