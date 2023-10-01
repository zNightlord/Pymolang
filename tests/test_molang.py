import pytest
from pymolang import Scanner

def test_scan_parse():
  # [[variable, VAR], [., DOT], [particle_age, IDENTIFIER], [>, GREATER], [5.3, FLOAT], [+, PLUS], [v, VAR], [., DOT], [particle_random3, IDENTIFIER]]
  scanner = Scanner("variable.particle_age > 5.3 + math.sin(v.particle_random3)")
  print(scanner.output_tokens())
  expr = scanner.output_pyexpression()  
  print("\n")
  print(expr)
  print("\n") 
  
  import math
  try: 
    print(eval(expr, {"particle_age":  5, "particle_random3": 1}))
  except Exception as e:
    print("error ", e )
  
def test_float():
  scanner = Scanner("5")
  print(scanner.output_tokens())
  