import itertools as itt

def interpret(command, variables):
    command = command.strip()
    if command.startswith('NOT'):
        var = command.split('NOT')[-1].strip()
        return  ~int(variables[var])
    if 'AND' in command:
        var_1 = command.split('AND')[0].strip()
        var_2 = command.split('AND')[1].strip()
        if var_1 in variables.keys():
            var_1 = variables[var_1]
        if var_2 in variables.keys():
            var_2 = variables[var_2]
        try:
            return int(var_1) & int(var_2)
        except ValueError as err:
            raise KeyError
            
    if 'OR' in command:
        var_1 = command.split('OR')[0].strip()
        var_2 = command.split('OR')[1].strip()
        return int(variables[var_1]) | int(variables[var_2])
    if 'LSHIFT' in command:
        var_1 = command.split('LSHIFT')[0].strip()
        var_2 = command.split('LSHIFT')[1].strip()
        return int(variables[var_1]) << int(var_2)
    if 'RSHIFT' in command:
        var_1 = command.split('RSHIFT')[0].strip()
        var_2 = command.split('RSHIFT')[1].strip()
        return int(variables[var_1]) >> int(var_2)
    if command.strip() in variables.keys():
        return variables[command.strip()]
    try:
        return int(command.strip())
    except ValueError as err:
        raise KeyError

def reorder(command_lines):
    temp_vars = {}
    ordered = []
    for command_line in itt.cycle(command_lines):
        command_line = command_line.rstrip()
        if len(ordered) <= len(command_lines) and not command_line in ordered:
            inst, var = command_line.split('->')
            inst = inst.strip()
            var = var.strip()
            try:
                interpret(inst, temp_vars)
                temp_vars[var] = 0
                ordered.append(command_line)
            except KeyError:
                pass
        elif len(ordered) >= len(command_lines):
            break
    return ordered
        





variables = {}

with open('input') as f:
    lines = f.readlines()

ordered_commands = reorder(lines)

for command in ordered_commands:
    inst, var = command.split('->')
    var = var.strip().rstrip()
    inst = inst.strip()
    variables[var] = interpret(inst, variables)

print('part 1 :', variables['a'])

variables = {'b': variables['a']}
for command in ordered_commands:
    inst, var = command.split('->')
    var = var.strip().rstrip()
    inst = inst.strip()
    if var != 'b':
        variables[var] = interpret(inst, variables)

print('part_2 :', variables['a'])

