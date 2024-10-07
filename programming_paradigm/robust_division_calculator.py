def safe_divide (float(numerator,denominator)):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print ("Eror:Cannot divide by zero.")
    except TypeError:
        print ("Error: Please enter numeric values only.")
    else: 
        return (f"The result of division is: {result}")
    
