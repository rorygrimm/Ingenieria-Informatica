# -*- coding: utf-8 -*-
"""encadenament_endavant.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yWWxJ3I9bR0id-u-YUP3ANyaO_R1TuTd
"""

BD = ['A', 'C', 'D']
target = 'E'
rules_used = []
target_found = False
no_rules_to_be_used = False
num_rules = 5

def rules(id_rule, BD):
    if id_rule == 0:
       if 'A' in BD and 'B' in BD:
        return True, 'C'
       else:
        return False, ''
    if id_rule == 1:
      if 'C' in BD and 'D' in BD:
        return True, 'F'
      else:
        return False, ''
    if id_rule == 2:
      if 'F' in BD and 'B' in BD:
        return True, 'E'
      else:
        return False, ''
    if id_rule == 3:
      if 'F' in BD and 'A' in BD:
        return True, 'G'
      else:
        return False, ''
    if id_rule == 4:
      if 'G' in BD and 'F' in BD:
        return True, 'B'
      else:
        return False, ''

def select_rule(valid_rules):
  return valid_rules[0]
  
  
while not target_found and not no_rules_to_be_used:

    valid_rules = []
    for ii in range(num_rules):
        valid_rule, new_state = rules(ii,BD)
        if valid_rule and ii not in rules_used:
            valid_rules.append(ii)
            
    if len(valid_rules) > 0:
        selected_rule = select_rule(valid_rules)
        rules_used.append(selected_rule)
        valid_rule, new_state = rules(selected_rule,BD)
        if new_state not in BD:
            BD.append(new_state)
        print("selected_rule: " + str(selected_rule))
        print("BD: ")
        print(BD)
        if target in BD:
            target_found = True
            print("Target found!")
    else:
        no_rules_to_be_used = True
        print("Target not found and no rules can be used")
