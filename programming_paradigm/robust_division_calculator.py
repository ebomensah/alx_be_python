def safe_divide(numerator, denominator):

    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
    except ZeroDivisionError:
        print ("Eror:Cannot divide by zero.")
    except TypeError:
        print ("Error: Please enter numberic values only.")
    else: 
        print (f"The result of division is: {result}")
    

safe_divide(4,6)