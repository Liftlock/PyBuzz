

class PyBuzz():

    def __init__(self, count_to):
        for i in range(count_to): 
            result = self.check(i+1)
            print(result)

    def check(self, value_to_check):
        if value_to_check % 15 == 0:
            return 'PyBuzz'

        if value_to_check % 3 == 0:
            return 'Py'

        if value_to_check % 5 == 0:
            return 'Buzz'
        
        return value_to_check


        