def arithmetic_arranger(problems, answers=False):
    error_msg = valid_input(problems)
    if error_msg == 'no_errors':
        arranged_problems_list = organize_problems(problems)
        arranged_problems = list_to_str(arranged_problems_list, answers)
        return arranged_problems
    else:
        return error_msg


def valid_input(problems):
    problems_quantity = len(problems)

    if problems_quantity > 5:
        return 'Error: Too many problems.'

    for i in range(problems_quantity):
        sectioned_problem = problems[i].split()
        if sectioned_problem[1] != '+' and sectioned_problem[1] != '-':
            return "Error: Operator must be '+' or '-'."

        if len(sectioned_problem[0]) >= 5 or len(sectioned_problem[2]) >= 5:
            return 'Error: Numbers cannot be more than four digits.'

        if not sectioned_problem[0].isdigit() or not sectioned_problem[2].isdigit():
            return 'Error: Numbers must only contain digits.'

    return 'no_errors'


def organize_problems(problems):
    problems_list = [
        [],
        [],
        [],
        []
    ]

    for i in range(len(problems)):
        individual_problem = problems[i].split()
        first_operand = individual_problem[0]
        operator = individual_problem[1]
        second_operand = individual_problem[2]

        if operator == '+':
            result = int(first_operand) + int(second_operand)
        else:
            result = int(first_operand) - int(second_operand)

        longest_operand = max(len(first_operand), len(second_operand))

        if i == (len(problems) - 1):
            problems_list[0].append(order_operands(first_operand, longest_operand))
            problems_list[1].append(order_operands((operator + second_operand), longest_operand))
            problems_list[2].append(order_operands('-', longest_operand))
            problems_list[3].append(order_operands(str(result), longest_operand, True))
        else:
            problems_list[0].append(order_operands(first_operand, longest_operand) + '    ')
            problems_list[1].append(order_operands((operator + second_operand), longest_operand) + '    ')
            problems_list[2].append(order_operands('-', longest_operand) + '    ')
            problems_list[3].append(order_operands(str(result), longest_operand, True) + '    ')
    return problems_list


def order_operands(string, longest_operand, result_flag=False):
    if string == '-':
        return ('-' * (2 + longest_operand))
    if result_flag is True:
        spaces = (longest_operand + 1) - len(string)
        return ' ' + (' ' * spaces) + string
    if string[0] == '+' or string[0] == '-':
        spaces = (longest_operand + 2) - len(string)
        return (string[0] + ' ' * spaces) + string[1:]
    else:
        spaces = (longest_operand + 1) - len(string)
        return ' ' + (' ' * spaces) + string


def list_to_str(raw_list, answers):
    converted_str = ''
    count = 1
    if answers is True:
        for i in range(len(raw_list)):
            for element in raw_list[i]:
                converted_str += element
            if count < 4:
                converted_str += '\n'
            count += 1
    else:
        for i in range(len(raw_list) - 1):
            for element in raw_list[i]:
                converted_str += element
            if count < 3:
                converted_str += '\n'
            count += 1
    return converted_str