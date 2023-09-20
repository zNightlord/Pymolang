import pytest
from Pymolang import Scanner

def test_scan_parse():
  Scanner.output("variable.particle_age > 5.3 + math.sin(v.particle_random3)")