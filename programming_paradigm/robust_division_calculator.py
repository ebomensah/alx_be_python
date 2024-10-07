def safe_divide [float(numerator),float(denominator)]:
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return ["Eror: Cannot divide by zero."]
    except TypeError:
        return ("Error: Please enter numeric values only.")
    else: 
        return (f"The result of division is: {result}")
    
