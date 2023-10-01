import pytest
from pymolang import Scanner

def test_scan_parse():
  # [[variable, VAR], [., DOT], [particle_age, IDENTIFIER], [>, GREATER], [5.3, FLOAT], [+, PLUS], [v, VAR], [., DOT], [particle_random3, IDENTIFIER]]
  Scanner.output("variable.particle_age > 5.3 + math.sin(v.particle_random3)")
  
def test_float():
  Scanner.output("5")
  