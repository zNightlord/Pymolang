import pytest
import math
from pymolang import Scanner

def test_scan_parse():
  particle_age = 5
  particle_random3 = 16
  source = "variable.particle_age > 5.3 + math.sqrt(v.particle_random3)"
  scanner = Scanner(source)
  expr = scanner.output_pyexpression()
  print(f"\n Expected result: {particle_age > 5.3 + math.sqrt( particle_random3)}")
  print("\n")
  expr = f"import math\nprint({expr})"
  exec(expr, {"particle_age": particle_age, "particle_random3": particle_random3})
  
def test_float():
  scanner = Scanner("5")
  print(scanner.output_tokens())
  