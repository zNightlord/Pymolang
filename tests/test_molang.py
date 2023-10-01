import pytest
import math
from pymolang import Scanner

def test_scan_parse():
  particle_age = 5
  particle_random3 = 1
  scanner = Scanner("variable.particle_age > 5.3 + math.sin(v.particle_random3)")
  print(scanner.output_tokens())
  expr = scanner.output_pyexpression()  
  print("\n")
  print(expr)
  print("\n") 
  try: 
    print(eval(expr, {"particle_age": particle_age, "particle_random3": particle_random3}))
  except Exception as e:
    print("error ", e )
    
  print(f"\n Expected: {particle_age > 5.3 + math.sin( particle_random3)}")
  
def test_float():
  scanner = Scanner("5")
  print(scanner.output_tokens())
  