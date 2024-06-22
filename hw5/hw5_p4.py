def evaluation(eq, character):
    try:
        # evaluate the equation
        result = eval(eq)
        # unsupported character
        for c in eq:
            if c not in character:
                return "Error: Unsupported character " + str(c)
    except ZeroDivisionError:
        return "Error: Division by zero"
    except SyntaxError as s:
        s = str(s)
        # unbalanced parentheses
        if s == "unmatched ')' (<string>, line 1)" or s == "'(' was never closed (<string>, line 1)":
            return "Error: Unbalanced parentheses"
        # invalid syntax
        if s == "invalid syntax (<string>, line 1)":
            return "Error: Operand error"

    return "Result: " + str(result)

# character list
character = ["(", ")", "+", "-", "*", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
while True:
    eq = input("Enter an expression to evaluate or 'q' to quit: ")
    # if "q" then break
    if eq == "q":
        print()
        break
    result = evaluation(eq, character)
    print(result)
