def safe_divide(numerator,denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print ("Eror:Cannot divide by zero.")
    except TypeError:
        print ("Error: Please enter numberic values only.")
    else: 
        return (f"The result of division is: {result}")
    
