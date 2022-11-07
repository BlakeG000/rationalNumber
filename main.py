from math import gcd
class Rational:

    def __init__(self, numer, denom):
        #TODO: Implement this!
      self.numer = numer
      self.denom = denom
      self.simplify()

  
    def simplify(self):
      divisor = gcd(self.numer,self.denom)
      self.numer = self.numer // divisor
      self.denom = self.denom // divisor
      
      
      
    def __add__(self, other):
        #TODO: Implement this
      if type(other) is int:
        other = Rational(other,1)
      new_numer = (self.numer * other.denom) + (other.numer * self.denom)
      new_denom = self.denom * other.denom
      return Rational(new_numer, new_denom)
                      
    def __radd__(self,other):
      return self+other
        

    def __sub__(self, other):
        # TODO: Implement this!
      if type(other) is int:
        other = Rational(other,1)
      new_numer = (self.numer * other.denom) - (other.numer * self.denom)
      new_denom = self.denom * other.denom
      return Rational(new_numer, new_denom)
      
    def __rsub__(self,other):
      return self-other
      
    def __mul__(self, other):
        # TODO: Implement this!
      if type(other) is int:
        other = Rational(other,1)
      new_numer = self.numer * other.numer
      new_denom = self.denom * other.denom
      return Rational(new_numer,new_denom)

    def __rmul__(self,other):
      return self*other
    def __truediv__(self, other):
        # TODO: Implement this!
      if type(other) is int:
        other = Rational(other,1)
      new_numer = self.numer * other.denom
      new_denom = self.denom * other.numer
      return Rational(new_numer,new_denom)
    def __rtruediv__(self,other):
      return self/other
    

    #TODO: you will need to put your numerator and denominator
    #TODO: in lowest terms in multiple functions. Maybe it's a
    #TODO: good idea to make that it's own function?

def main():
  a = Rational(1, 3)
  b = Rational(1, 6)

  c = 2 + b

  print(f"{c.numer}/{c.denom}")

  


if __name__ == '__main__':
    main()
