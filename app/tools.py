from datetime import datetime


def get_current_date() -> str:
    """Return the current date."""

    return datetime.now().strftime("%Y-%m-%d")


def calculator(a: float, b: float, operation: str):

    operations = {
        "add": lambda: a + b,
        "subtract": lambda: a - b,
        "multiply": lambda: a * b,
        "divide": lambda: a / b if b != 0 else "Cannot divide by zero"
    }

    operation_function = operations.get(operation.lower())

    if operation_function is None:
        return "Unsupported operation"

    return operation_function()
