def number_pattern(n):
    output = ''
    if isinstance(n,int) and n >= 1:
        for n in range(n):
            output += str(n + 1) + " "
    elif isinstance(n,int):
        return('Argument must be an integer greater than 0.')
    else:
        return('Argument must be an integer value.')
    main_output = output.strip()
    return main_output
print(number_pattern(7))