
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BOOL DIVIDE EQUAL EQUAL_EQUAL FALSE FLOAT FLOAT_NUMBER FOR GREATER GREATER_EQUAL ID IF INPUT INT INT_NUMBER LEFT_BR LEFT_BR_CURLY LESS LESS_EQUAL MINUS MULTIPLY NOT_EQUAL OR PLUS PRINT PROGRAM RIGHT_BR RIGHT_BR_CURLY SEMICOLON STRING TEXT TRUE VAR\n    start_symbol : program\n    \n    program : PROGRAM LEFT_BR_CURLY instructions RIGHT_BR_CURLY\n            | empty\n    \n    instructions : instruction\n        | instruction instructions\n    \n    instruction : for_loop\n        | if_statement\n        | assignment\n        | empty\n        | var_declaration\n        | print\n        | input\n    \n    for_loop : for_loop_statement LEFT_BR_CURLY change_tab_number instructions RIGHT_BR_CURLY\n    \n    for_loop_statement : FOR LEFT_BR INT VAR EQUAL INT_NUMBER SEMICOLON VAR LESS INT_NUMBER SEMICOLON VAR EQUAL VAR PLUS number RIGHT_BR\n    \n    if_statement : IF LEFT_BR comparisons RIGHT_BR LEFT_BR_CURLY change_tab_number instructions RIGHT_BR_CURLY\n    \n    comparisons : comparison\n        | comparison conjunction comparisons\n    \n    comparison : value comparator value\n    \n    comparator : LESS\n        | LESS_EQUAL\n        | GREATER\n        | GREATER_EQUAL\n        | EQUAL_EQUAL\n        | NOT_EQUAL\n    \n    operator : PLUS\n        | MINUS\n        | MULTIPLY\n        | DIVIDE\n    \n    type : INT\n        | STRING\n        | BOOL\n        | FLOAT\n    \n    conjunction : AND\n        | OR\n    \n    number : INT_NUMBER\n        | FLOAT_NUMBER\n    \n    bool_value : TRUE\n        | FALSE\n    \n    value : number\n        | VAR\n        | TEXT\n        | bool_value\n        | math_operation\n    \n    math_operation : VAR operator VAR\n        | VAR operator number\n        | number operator VAR\n        | number operator number\n    \n    assignment : VAR EQUAL value SEMICOLON\n               | VAR EQUAL VAR SEMICOLON\n    \n    var_declaration : type VAR SEMICOLON\n        | type VAR EQUAL value SEMICOLON\n        | type VAR EQUAL VAR SEMICOLON\n    \n    print : PRINT LEFT_BR out RIGHT_BR SEMICOLON\n    \n    out : TEXT\n        | VAR\n        | number\n    \n    input : INPUT LEFT_BR VAR RIGHT_BR SEMICOLON\n    \n    empty :\n    change_tab_number : '
    
_lr_action_items = {'PROGRAM':([0,],[3,]),'$end':([0,1,2,4,26,],[-58,0,-1,-3,-2,]),'LEFT_BR_CURLY':([3,15,59,110,],[5,28,84,-14,]),'IF':([5,7,8,9,10,11,12,13,14,28,35,50,76,77,83,84,91,92,93,94,96,100,],[16,16,-6,-7,-8,-9,-10,-11,-12,-59,16,-50,-49,-48,-13,-59,-52,-51,-53,-57,16,-15,]),'VAR':([5,7,8,9,10,11,12,13,14,18,22,23,24,25,28,29,30,32,33,35,50,51,57,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,83,84,91,92,93,94,96,99,100,104,106,],[17,17,-6,-7,-8,-9,-10,-11,-12,31,-29,-30,-31,-32,-59,40,48,54,56,17,-50,78,82,40,-33,-34,40,-19,-20,-21,-22,-23,-24,88,-25,-26,-27,-28,89,-49,-48,-13,-59,-52,-51,-53,-57,17,101,-15,105,107,]),'PRINT':([5,7,8,9,10,11,12,13,14,28,35,50,76,77,83,84,91,92,93,94,96,100,],[19,19,-6,-7,-8,-9,-10,-11,-12,-59,19,-50,-49,-48,-13,-59,-52,-51,-53,-57,19,-15,]),'INPUT':([5,7,8,9,10,11,12,13,14,28,35,50,76,77,83,84,91,92,93,94,96,100,],[20,20,-6,-7,-8,-9,-10,-11,-12,-59,20,-50,-49,-48,-13,-59,-52,-51,-53,-57,20,-15,]),'FOR':([5,7,8,9,10,11,12,13,14,28,35,50,76,77,83,84,91,92,93,94,96,100,],[21,21,-6,-7,-8,-9,-10,-11,-12,-59,21,-50,-49,-48,-13,-59,-52,-51,-53,-57,21,-15,]),'INT':([5,7,8,9,10,11,12,13,14,28,34,35,50,76,77,83,84,91,92,93,94,96,100,],[22,22,-6,-7,-8,-9,-10,-11,-12,-59,57,22,-50,-49,-48,-13,-59,-52,-51,-53,-57,22,-15,]),'STRING':([5,7,8,9,10,11,12,13,14,28,35,50,76,77,83,84,91,92,93,94,96,100,],[23,23,-6,-7,-8,-9,-10,-11,-12,-59,23,-50,-49,-48,-13,-59,-52,-51,-53,-57,23,-15,]),'BOOL':([5,7,8,9,10,11,12,13,14,28,35,50,76,77,83,84,91,92,93,94,96,100,],[24,24,-6,-7,-8,-9,-10,-11,-12,-59,24,-50,-49,-48,-13,-59,-52,-51,-53,-57,24,-15,]),'FLOAT':([5,7,8,9,10,11,12,13,14,28,35,50,76,77,83,84,91,92,93,94,96,100,],[25,25,-6,-7,-8,-9,-10,-11,-12,-59,25,-50,-49,-48,-13,-59,-52,-51,-53,-57,25,-15,]),'RIGHT_BR_CURLY':([5,6,7,8,9,10,11,12,13,14,27,28,35,50,58,76,77,83,84,91,92,93,94,96,98,100,],[-58,26,-4,-6,-7,-8,-9,-10,-11,-12,-5,-59,-58,-50,83,-49,-48,-13,-59,-52,-51,-53,-57,-58,100,-15,]),'LEFT_BR':([16,19,20,21,],[29,32,33,34,]),'EQUAL':([17,31,82,105,],[30,51,95,106,]),'TEXT':([29,30,32,51,60,61,62,63,64,65,66,67,68,69,],[41,41,53,41,41,-33,-34,41,-19,-20,-21,-22,-23,-24,]),'INT_NUMBER':([29,30,32,51,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,95,102,108,],[44,44,44,44,44,-33,-34,44,-19,-20,-21,-22,-23,-24,44,-25,-26,-27,-28,44,97,103,44,]),'FLOAT_NUMBER':([29,30,32,51,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,108,],[45,45,45,45,45,-33,-34,45,-19,-20,-21,-22,-23,-24,45,-25,-26,-27,-28,45,45,]),'TRUE':([29,30,51,60,61,62,63,64,65,66,67,68,69,],[46,46,46,46,-33,-34,46,-19,-20,-21,-22,-23,-24,]),'FALSE':([29,30,51,60,61,62,63,64,65,66,67,68,69,],[47,47,47,47,-33,-34,47,-19,-20,-21,-22,-23,-24,]),'SEMICOLON':([31,39,41,42,43,44,45,46,47,48,49,78,79,80,81,87,88,89,90,97,103,],[50,-39,-41,-42,-43,-35,-36,-37,-38,76,77,91,92,93,94,-47,-46,-44,-45,99,104,]),'RIGHT_BR':([36,37,39,40,41,42,43,44,45,46,47,52,53,54,55,56,85,86,87,88,89,90,109,],[59,-16,-39,-40,-41,-42,-43,-35,-36,-37,-38,80,-54,-55,-56,81,-17,-18,-47,-46,-44,-45,110,]),'AND':([37,39,40,41,42,43,44,45,46,47,86,87,88,89,90,],[61,-39,-40,-41,-42,-43,-35,-36,-37,-38,-18,-47,-46,-44,-45,]),'OR':([37,39,40,41,42,43,44,45,46,47,86,87,88,89,90,],[62,-39,-40,-41,-42,-43,-35,-36,-37,-38,-18,-47,-46,-44,-45,]),'LESS':([38,39,40,41,42,43,44,45,46,47,87,88,89,90,101,],[64,-39,-40,-41,-42,-43,-35,-36,-37,-38,-47,-46,-44,-45,102,]),'LESS_EQUAL':([38,39,40,41,42,43,44,45,46,47,87,88,89,90,],[65,-39,-40,-41,-42,-43,-35,-36,-37,-38,-47,-46,-44,-45,]),'GREATER':([38,39,40,41,42,43,44,45,46,47,87,88,89,90,],[66,-39,-40,-41,-42,-43,-35,-36,-37,-38,-47,-46,-44,-45,]),'GREATER_EQUAL':([38,39,40,41,42,43,44,45,46,47,87,88,89,90,],[67,-39,-40,-41,-42,-43,-35,-36,-37,-38,-47,-46,-44,-45,]),'EQUAL_EQUAL':([38,39,40,41,42,43,44,45,46,47,87,88,89,90,],[68,-39,-40,-41,-42,-43,-35,-36,-37,-38,-47,-46,-44,-45,]),'NOT_EQUAL':([38,39,40,41,42,43,44,45,46,47,87,88,89,90,],[69,-39,-40,-41,-42,-43,-35,-36,-37,-38,-47,-46,-44,-45,]),'PLUS':([39,40,44,45,48,78,107,],[71,71,-35,-36,71,71,108,]),'MINUS':([39,40,44,45,48,78,],[72,72,-35,-36,72,72,]),'MULTIPLY':([39,40,44,45,48,78,],[73,73,-35,-36,73,73,]),'DIVIDE':([39,40,44,45,48,78,],[74,74,-35,-36,74,74,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start_symbol':([0,],[1,]),'program':([0,],[2,]),'empty':([0,5,7,35,96,],[4,11,11,11,11,]),'instructions':([5,7,35,96,],[6,27,58,98,]),'instruction':([5,7,35,96,],[7,7,7,7,]),'for_loop':([5,7,35,96,],[8,8,8,8,]),'if_statement':([5,7,35,96,],[9,9,9,9,]),'assignment':([5,7,35,96,],[10,10,10,10,]),'var_declaration':([5,7,35,96,],[12,12,12,12,]),'print':([5,7,35,96,],[13,13,13,13,]),'input':([5,7,35,96,],[14,14,14,14,]),'for_loop_statement':([5,7,35,96,],[15,15,15,15,]),'type':([5,7,35,96,],[18,18,18,18,]),'change_tab_number':([28,84,],[35,96,]),'comparisons':([29,60,],[36,85,]),'comparison':([29,60,],[37,37,]),'value':([29,30,51,60,63,],[38,49,79,38,86,]),'number':([29,30,32,51,60,63,70,75,108,],[39,39,55,39,39,39,87,90,109,]),'bool_value':([29,30,51,60,63,],[42,42,42,42,42,]),'math_operation':([29,30,51,60,63,],[43,43,43,43,43,]),'out':([32,],[52,]),'conjunction':([37,],[60,]),'comparator':([38,],[63,]),'operator':([39,40,48,78,],[70,75,75,75,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start_symbol","S'",1,None,None,None),
  ('start_symbol -> program','start_symbol',1,'p_start_symbol','syntaxChecker.py',110),
  ('program -> PROGRAM LEFT_BR_CURLY instructions RIGHT_BR_CURLY','program',4,'p_program','syntaxChecker.py',119),
  ('program -> empty','program',1,'p_program','syntaxChecker.py',120),
  ('instructions -> instruction','instructions',1,'p_instructions','syntaxChecker.py',130),
  ('instructions -> instruction instructions','instructions',2,'p_instructions','syntaxChecker.py',131),
  ('instruction -> for_loop','instruction',1,'p_instruction','syntaxChecker.py',141),
  ('instruction -> if_statement','instruction',1,'p_instruction','syntaxChecker.py',142),
  ('instruction -> assignment','instruction',1,'p_instruction','syntaxChecker.py',143),
  ('instruction -> empty','instruction',1,'p_instruction','syntaxChecker.py',144),
  ('instruction -> var_declaration','instruction',1,'p_instruction','syntaxChecker.py',145),
  ('instruction -> print','instruction',1,'p_instruction','syntaxChecker.py',146),
  ('instruction -> input','instruction',1,'p_instruction','syntaxChecker.py',147),
  ('for_loop -> for_loop_statement LEFT_BR_CURLY change_tab_number instructions RIGHT_BR_CURLY','for_loop',5,'p_for_loop','syntaxChecker.py',161),
  ('for_loop_statement -> FOR LEFT_BR INT VAR EQUAL INT_NUMBER SEMICOLON VAR LESS INT_NUMBER SEMICOLON VAR EQUAL VAR PLUS number RIGHT_BR','for_loop_statement',17,'p_for_loop_statement','syntaxChecker.py',170),
  ('if_statement -> IF LEFT_BR comparisons RIGHT_BR LEFT_BR_CURLY change_tab_number instructions RIGHT_BR_CURLY','if_statement',8,'p_if_statement','syntaxChecker.py',180),
  ('comparisons -> comparison','comparisons',1,'p_comparisons','syntaxChecker.py',189),
  ('comparisons -> comparison conjunction comparisons','comparisons',3,'p_comparisons','syntaxChecker.py',190),
  ('comparison -> value comparator value','comparison',3,'p_comparison','syntaxChecker.py',200),
  ('comparator -> LESS','comparator',1,'p_comparator','syntaxChecker.py',207),
  ('comparator -> LESS_EQUAL','comparator',1,'p_comparator','syntaxChecker.py',208),
  ('comparator -> GREATER','comparator',1,'p_comparator','syntaxChecker.py',209),
  ('comparator -> GREATER_EQUAL','comparator',1,'p_comparator','syntaxChecker.py',210),
  ('comparator -> EQUAL_EQUAL','comparator',1,'p_comparator','syntaxChecker.py',211),
  ('comparator -> NOT_EQUAL','comparator',1,'p_comparator','syntaxChecker.py',212),
  ('operator -> PLUS','operator',1,'p_operator','syntaxChecker.py',219),
  ('operator -> MINUS','operator',1,'p_operator','syntaxChecker.py',220),
  ('operator -> MULTIPLY','operator',1,'p_operator','syntaxChecker.py',221),
  ('operator -> DIVIDE','operator',1,'p_operator','syntaxChecker.py',222),
  ('type -> INT','type',1,'p_type','syntaxChecker.py',229),
  ('type -> STRING','type',1,'p_type','syntaxChecker.py',230),
  ('type -> BOOL','type',1,'p_type','syntaxChecker.py',231),
  ('type -> FLOAT','type',1,'p_type','syntaxChecker.py',232),
  ('conjunction -> AND','conjunction',1,'p_conjunction','syntaxChecker.py',239),
  ('conjunction -> OR','conjunction',1,'p_conjunction','syntaxChecker.py',240),
  ('number -> INT_NUMBER','number',1,'p_number','syntaxChecker.py',247),
  ('number -> FLOAT_NUMBER','number',1,'p_number','syntaxChecker.py',248),
  ('bool_value -> TRUE','bool_value',1,'p_bool_value','syntaxChecker.py',255),
  ('bool_value -> FALSE','bool_value',1,'p_bool_value','syntaxChecker.py',256),
  ('value -> number','value',1,'p_value','syntaxChecker.py',266),
  ('value -> VAR','value',1,'p_value','syntaxChecker.py',267),
  ('value -> TEXT','value',1,'p_value','syntaxChecker.py',268),
  ('value -> bool_value','value',1,'p_value','syntaxChecker.py',269),
  ('value -> math_operation','value',1,'p_value','syntaxChecker.py',270),
  ('math_operation -> VAR operator VAR','math_operation',3,'p_math_operation','syntaxChecker.py',277),
  ('math_operation -> VAR operator number','math_operation',3,'p_math_operation','syntaxChecker.py',278),
  ('math_operation -> number operator VAR','math_operation',3,'p_math_operation','syntaxChecker.py',279),
  ('math_operation -> number operator number','math_operation',3,'p_math_operation','syntaxChecker.py',280),
  ('assignment -> VAR EQUAL value SEMICOLON','assignment',4,'p_assignment','syntaxChecker.py',287),
  ('assignment -> VAR EQUAL VAR SEMICOLON','assignment',4,'p_assignment','syntaxChecker.py',288),
  ('var_declaration -> type VAR SEMICOLON','var_declaration',3,'p_var_declaration','syntaxChecker.py',296),
  ('var_declaration -> type VAR EQUAL value SEMICOLON','var_declaration',5,'p_var_declaration','syntaxChecker.py',297),
  ('var_declaration -> type VAR EQUAL VAR SEMICOLON','var_declaration',5,'p_var_declaration','syntaxChecker.py',298),
  ('print -> PRINT LEFT_BR out RIGHT_BR SEMICOLON','print',5,'p_print','syntaxChecker.py',308),
  ('out -> TEXT','out',1,'p_out','syntaxChecker.py',315),
  ('out -> VAR','out',1,'p_out','syntaxChecker.py',316),
  ('out -> number','out',1,'p_out','syntaxChecker.py',317),
  ('input -> INPUT LEFT_BR VAR RIGHT_BR SEMICOLON','input',5,'p_input','syntaxChecker.py',324),
  ('empty -> <empty>','empty',0,'p_empty','syntaxChecker.py',331),
  ('change_tab_number -> <empty>','change_tab_number',0,'p_change_tab_number','syntaxChecker.py',337),
]
