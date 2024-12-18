from django.shortcuts import render
import math


def calculate(request):
    result = None
    error_message = None

    if request.method == "POST":
        # Get input values from the form
        num1 = request.POST.get('num1', '')
        num2 = request.POST.get('num2', '')
        operation = request.POST.get('operation', '')

        try:
            # Convert input strings to floats for calculation
            num1 = float(num1) if num1 else 0
            num2 = float(num2) if num2 else 0

            # Perform calculations based on the operation
            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 != 0:
                    result = num1 / num2
                else:
                    error_message = "Cannot divide by zero"
            elif operation == "sqrt":
                if num1 >= 0:
                    result = math.sqrt(num1)
                else:
                    error_message = "Cannot calculate square root of a negative number"
            elif operation == "power":
                result = math.pow(num1, num2)
            else:
                error_message = "Invalid operation"
        except ValueError:
            error_message = "Invalid input. Please enter valid numbers."

    return render(request, 'calculator/index.html', {
        'result': result,
        'error_message': error_message,
    })

