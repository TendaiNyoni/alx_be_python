class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method that returns the sum of two numbers.
        It does not need access to class or instance data.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method that returns the product of two numbers.
        It has access to class-level data through the 'cls' parameter.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
