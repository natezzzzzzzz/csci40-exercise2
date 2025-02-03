class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        
        if isinstance(numerator, str):

            termsList = numerator.strip().split("/")
       
            if len(termsList) == 1:
                #numerator 
                if not termsList[0].isdigit() or isinstance(termsList[0], float):
                    self.numerator = 0
                else:
                    self.numerator = int(termsList[0])
            
            elif len(termsList) == 2:
                #numerator
                if not termsList[0].isdigit() or isinstance(termsList[0], float):
                    self.numerator = 0
                else:
                    self.numerator = int(termsList[0])

                #denominator
                if not termsList[1].isdigit() or isinstance(termsList[1], float):
                        self.denominator = 1
                else:
                    self.denominator = int(termsList[1]) 

            else:
                self.numerator = 0
                self.denominator = 1

        else:
            #TODO
            pass

    def gcd(a, b):
        #TODO
        pass

    def get_numerator(self):
        #TODO
        pass

    def get_denominator(self):
        #TODO
        pass

    def get_fraction(self):
        #TODO
        pass
