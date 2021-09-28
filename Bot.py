import Logo_Variable
import Working

Ans = 0
count = 1  # for Sequence count
Logo_Variable.design_dee()

while True:
    print(count, ". [ Write Here ]")
    user_input = str(input(">> "))

    if user_input == "exit":
        print("| ThankYou! For Visiting [ DEE Maths ] |")
        break
    # -----------------------------
    # for main equation
    final_equation = Working.equation()

    # for BODMAS
    bodmas_list = ['0', '0', '0']
    break_out_flag = False
    for _ in Working.operator():
        # for 0 divisible error
        if break_out_flag:
            break

        # for sorting operation
        Sort_operation = Working.sort_operation()

        # -----------------------------
        # for multi operation in use
        for x, i in zip(Sort_operation[0], Sort_operation[1]):
            if i in Logo_Variable.opt:
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
                Ans = float(bodmas_list[0]) * float(bodmas_list[2])
                Working.clear_value(x, Ans)
                bodmas_list = ['0', '0', '0']
                break

            # power or exponent[^]
            elif i == "^" or i == "**":
                Ans = float(bodmas_list[0]) ** float(bodmas_list[2])
                Working.clear_value(x, Ans)
                bodmas_list = ['0', '0', '0']
                break

            # Addition[+]
            elif i == "+":
                Ans = float(bodmas_list[0]) + float(bodmas_list[2])
                Working.clear_value(x, Ans)
                bodmas_list = ['0', '0', '0']
                break

            # Subtraction[-]
            elif i == "-":
                Ans = float(bodmas_list[0]) - float(bodmas_list[2])
                Working.clear_value(x, Ans)
                bodmas_list = ['0', '0', '0']
                break

    print("=", Ans)
    count += 1  # for counting
