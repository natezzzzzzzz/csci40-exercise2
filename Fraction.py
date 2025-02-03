class Fraction(object):

    def init(self, numerator=0, denominator=1):

        # STRING INPUTS PROCESSED HERE
        if isinstance(numerator, str):

            termsList = numerator.strip().split("/")
            termsListLength = len(termsList)

            if termsListLength == 1:
                #numerator 
                if not termsList[0].strip("-").isdigit() or isinstance(termsList[0], float):
                    self.numerator = 0
                else:
                    self.numerator = int(termsList[0])

            elif termsListLength == 2:
                #numerator
                if not termsList[0].strip("-").isdigit() or isinstance(termsList[0], float):
                    self.numerator = 0
                else:
                    self.numerator = int(termsList[0])

                #denominator
                if not termsList[1].strip("-").isdigit() or isinstance(termsList[1], float):
                        self.denominator = 1
                else:
                    self.denominator = int(termsList[1]) 

            else:
                self.numerator = 0
                self.denominator = 1
            
        # NON-STRING INPUTS PROCESSED HERE
        else:
            # checks if numerator or denominator is a float and sets to default 0/1 if yes
            if isinstance(numerator, float) or isinstance(denominator, float):
                self.numerator = 0
                self.denominator = 1
            else:
                self.numerator = numerator
                self.denominator = denominator

    @staticmethod
    def gcd(a, b):

        if a == 0 or b == 0:
            return 0
        while b != 0:
            a, b = b, a % b
        return abs(a)

    def get_numerator(self):
        #TODO
        pass

    def get_denominator(self):
        #TODO
        pass

    def get_fraction(self):
        #TODO
        pass
