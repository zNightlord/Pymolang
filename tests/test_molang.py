import pytest
import math
from pymolang import Scanner

def test_scan_parse():
  particle_age = 5
  particle_random3 = 16
  source = "variable.particle_age > 5.3 + math.sqrt(v.particle_random3)"
  scanner = Scanner(source)
  print("\n")
  expr = scanner.output_pyexpression()
  print(f"Expected result: {particle_age > 5.3 + math.sqrt( particle_random3)}")
  expr = f"from math import sqrt\nprint(variable.particle_age > 5.3 + math.sqrt(v.particle_random3): {expr})"
  exec(expr, {"particle_age": particle_age, "particle_random3": particle_random3})
  
def test_float():
  scanner = Scanner("5")
  print("\n")
  print(scanner.output_tokens())

def test_query_animtime():
  scanner = Scanner("-5.0 * Math.cos(297.9380535 * query.anim_time) - 5.0")
  print("\n")
  expr = scanner.output_pyexpression()
  print(expr)

def test_variable():
  source ="v.fall_acc = -0.3;v.wind_acc = 2;v.curve_len = 15;"
  scanner = Scanner(source)
  print("\n")
  expr = scanner.output_pyexpression()
  print(expr)
  