import Logo_Variable
import Working

Ans = 0
Second_value = 0
digit_2 = 0
operation_in_use = ""

count = 1  # for Sequence
Logo_Variable.design_dee()

while True:
    print(count, ". [ Write Here ]")
    user_input = str(input(">> "))

    if user_input == "exit":
        print("| ThankYou! For Visiting [ DEE Maths ] |")
        break
    # -----------------------------
    # For main equation
    final_equation = Working.equation()

    if '' in final_equation:
        final_equation.remove('')
    elif ' ' in final_equation:
        final_equation.remove(' ')

    # For BODMAS Operation
    bodmas_list = ['0', '0', '0']
    break_out_flag = False

    for _ in Working.operator():
        # For 0 divisible error
        if break_out_flag:
            break

        # For sorting operation
        Sort_operation = Working.sort_operation()

        # -----------------------------
        # For operation in use
        for x, i in zip(Sort_operation[0], Sort_operation[1]):    # [0] = index Operation , [1] = sort_operater
            # Equal to[!]
            if "=" not in Sort_operation[1]:
                operation_in_use = Sort_operation[1][-1]

            if i == "=":
                Working.equal_operator(operation_in_use)
                break

            # For Short list
            elif i in Logo_Variable.opt:
                bodmas_list[0] = final_equation[x - 1]
                bodmas_list[1] = final_equation[x]
                bodmas_list[2] = final_equation[1 + x]
            elif i in Logo_Variable.single_opt:
                bodmas_list[0] = final_equation[x - 1]
                bodmas_list[1] = final_equation[x]

            # Factorial[!]
            if i == "!":
                f = 1
                value_copy = float(bodmas_list[0])
                Ans = float(bodmas_list[0])
                while f < value_copy:
                    Ans *= f
                    f += 1
                Working.clear_single(x, Ans)
                bodmas_list = ['0', '0', '0']
                break

            # Division[/]
            elif i == "/":
                Second_value = Working.last_value(operation_in_use)
                if bodmas_list[2] == "0" or bodmas_list[2] == "0 " or bodmas_list[2] == " 0" or bodmas_list[2] == " 0 ":
                    Ans = 0
                    print("| WARNING! :- Zero [0] Cannot Divisible Any Number |")
                    break_out_flag = True
                    break
                else:
                    Ans = float(bodmas_list[0]) / float(bodmas_list[2])
                    Working.clear_value(x, Ans)
                    bodmas_list = ['0', '0', '0']
                    break

            # multiplication[*]
            elif i == "*" or i == "x":
                Second_value = Working.last_value(operation_in_use)
                Ans = float(bodmas_list[0]) * float(bodmas_list[2])
                Working.clear_value(x, Ans)
                bodmas_list = ['0', '0', '0']
                break

            # Power or Exponent[^]
            elif i == "^" or i == "**":
                Second_value = Working.last_value(operation_in_use)
                Ans = float(bodmas_list[0]) ** float(bodmas_list[2])
                Working.clear_value(x, Ans)
                bodmas_list = ['0', '0', '0']
                break

            # Addition[+]
            elif i == "+":
                Second_value = Working.last_value(operation_in_use)
                Ans = float(bodmas_list[0]) + float(bodmas_list[2])
                Working.clear_value(x, Ans)
                bodmas_list = ['0', '0', '0']
                break

            # Subtraction[-]
            elif i == "-":
                Second_value = Working.last_value(operation_in_use)
                Ans = float(bodmas_list[0]) - float(bodmas_list[2])
                Working.clear_value(x, Ans)
                bodmas_list = ['0', '0', '0']
                break

    print("=", Ans)
    count += 1  # for counting
