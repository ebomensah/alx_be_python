def safe_divide (numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator/denominator
    except ZeroDivisionError:
        raise [Error: Cannot divide by zero.]
    except TypeError:
        raise ("Error: Please enter numeric values only.")
    else: 
        return (f"The result of division is {result}")
    
