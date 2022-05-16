step_23 = {"MESON": [8, "stop"], "LEX": [9, "stop"]}
step_22 = {"MESON": [6, "stop"], "LEX": [7, "stop"]}
step_21 = {"ECL": [3, "stop"], "GO": [4, "stop"], "SVG": [5, "stop"]}
step_20 = {1959: [0, "stop"], 1997: [1, "stop"], 1994: [2, "stop"]}
step_11 = {1959: [step_22, 2], 1997: [step_23, 3], 1994: [10, "stop"]}
step_10 = {"MESON": [step_20, 0], "LEX": [step_21, 1]}
step_00 = {"TEX": [step_10, 0], "STAN": [step_11, 1], "OZ": [11, "stop"]}
list_of_steps = [[step_00],
                 [step_10, step_11],
                 [step_20, step_21, step_22, step_23]]


def main(x):
    result = {}
    cnt = 0
    where_to_search = 0
    while isinstance(result, dict):
        item = list_of_steps[cnt][where_to_search]
        for item_of_x in x:
            if item_of_x in item:
                cnt += 1
                result = item[item_of_x][0]
                where_to_search = item[item_of_x][1]
                break
    return result


print(main(['STAN', 1959, 'LEX', 'ECL']))
print(main(['TEX', 1959, 'MESON', 'GO']))

