# # inp = input()
# # # inp = '1234123402-1234123401:15 1234123401-1234123404:05 1234123404-1234123401:03 1234123402-1234123401:15 1234123401-1234123404:09 1234123402-1234123401:15 1234123401-1234123404:15 1234123404-1234123401:03 1234123405-1234123404:03'
# # inp = inp.split(' ')
# #
# # pr = []
# #
# # for i in inp:
# #     i = i.split(':')
# #     pr.append(i)
# #
# # flag = {}
# # for i in pr:
# #     j = i[0]
# #     if j in flag.keys():
# #         SUM = int(flag[j]) + int(i[1])
# #         flag[j] = SUM
# #     else:
# #         SUM = int(i[1])
# #         flag[j] = SUM
# #
# # print(f"1234123401-1234123404:{flag['1234123401-1234123404']}")
# # for i, j in flag.items():
# #     if not i == '1234123401-1234123404':
# #         print(f"{i}:{j}")
# chutiya=input().split()
# if len(chutiya)==0:
#   print('error')
# kk=1
# dic={}
# for randi in chutiya:
#   try:
#     mc,lund=randi.split(':')
#   except:
#     print('error')
#     kk=0
#     break
#   if mc in dic.keys():
#       dic[mc]+=int(lund)
#   else:
#     dic[mc]=int(lund)
# if kk==1:
#   for i in sorted(dic.keys()) :
#     print(i+':'+str(dic[i]))

# inp = '(5+6)-(7/6)*1'
# print(eval(inp))

def solve(calculation):
  operator_precedence = {"^": 4, "/": 3, "*": 2, "+": 1, "-": 1}

  bodmas_index = []

  for i in range(len(calculation)):
    if calculation[i] in operator_precedence:
      if len(bodmas_index) == 0:
        bodmas_index.append(i)
      else:
        for x in range(len(bodmas_index)):
          if operator_precedence[calculation[i]] < operator_precedence[calculation[bodmas_index[-1]]]:
            bodmas_index.append(i)
            break
          elif operator_precedence[calculation[i]] > operator_precedence[calculation[bodmas_index[x]]]:
            bodmas_index.insert(x, i)
            break
          elif operator_precedence[calculation[i]] == operator_precedence[calculation[bodmas_index[x]]]:
            if calculation[i] == "+" or calculation[i] == "-":
              bodmas_index.append(i)
              break
            else:
              bodmas_index.insert(x + 1, i)
              break
          else:
            continue

  while len(bodmas_index) != 0:

    if calculation[bodmas_index[0]] == '/':
      calculation_result = calculation[bodmas_index[0] - 1] / calculation[bodmas_index[0] + 1]
    elif calculation[bodmas_index[0]] == '*':
      calculation_result = calculation[bodmas_index[0] - 1] * calculation[bodmas_index[0] + 1]
    elif calculation[bodmas_index[0]] == '+':
      calculation_result = calculation[bodmas_index[0] - 1] + calculation[bodmas_index[0] + 1]
    else:
      calculation_result = calculation[bodmas_index[0] - 1] - calculation[bodmas_index[0] + 1]

    calculation[bodmas_index[0] - 1] = calculation_result
    calculation.pop(bodmas_index[0] + 1)
    calculation.pop(bodmas_index[0])

    print(bodmas_index)
    for i in range(len(bodmas_index)):
      if bodmas_index[i] > bodmas_index[0]:
        bodmas_index.insert(i, bodmas_index[i] - 2)
        bodmas_index.pop(i + 1)

    bodmas_index.pop(0)

  return calculation[0]


def bracket_pair_finder(calculation):
  start_bracket_index_array = []
  end_bracket_index_array = []
  bracket_pairs = {}

  for i in range(len(calculation)):
    if calculation[i] == '(':
      start_bracket_index_array.append(i)
    elif calculation[i] == ')':
      end_bracket_index_array.append(i)

  for i in range(len(start_bracket_index_array) - 1, -1, -1):
    for x in range(len(end_bracket_index_array)):
      if end_bracket_index_array[x] < start_bracket_index_array[i] or end_bracket_index_array[
        x] in bracket_pairs.values():
        continue
      else:
        bracket_pairs[start_bracket_index_array[i]] = end_bracket_index_array[x]
        break
    break
  if len(bracket_pairs) != 0:
    return bracket_pairs


def calculator(calculation):
  brackets = bracket_pair_finder(calculation)
  answer = []

  if brackets is None:
    return float(solve(calculation))
  else:
    start_bracket_index = list(brackets.keys())[0]
    end_bracket_index = brackets[start_bracket_index]
    answer.append(solve(calculation[start_bracket_index + 1:end_bracket_index]))
    calculation = calculation[:start_bracket_index] + answer + calculation[end_bracket_index + 1:]
    print(calculation)
    return calculator(calculation)


def calc_input():
  calculation_array = []
  calculation = input('Enter your calculation: ')
  number = ""

  for i in range(len(calculation)):

    if calculation[i].isnumeric() or calculation[i] == ".":

      number = number + calculation[i]

      if i == len(calculation) - 1:
        calculation_array.append(float(number))
    else:
      if number == "":
        calculation_array.append(calculation[i])


      else:
        calculation_array.append(float(number))
        calculation_array.append(calculation[i])
        number = ""

  print(calculation_array)
  return calculator(calculation_array)


answer = calc_input()
print(answer)