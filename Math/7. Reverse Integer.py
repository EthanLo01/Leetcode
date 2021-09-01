class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if 2**31-1 <= x or  x <= -2**31-1:
            return 0


        num_list = list(str(x))
        car_ist = num_list[::-1]

        if car_ist[-1] == "-":
            car_ist.pop(-1)



        if x < 0:
            car_ist.insert(0, "-")

        anwser = int("".join(i for i in car_ist))

        if 2**31-1 <= anwser or anwser <= -2**31-1:
            return 0
        
        return anwser
    
# God
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        
        string = str(x)[::-1].replace("-", "")                # convert x into a string, reverse it and then delete any "-" sign
        integer = int(string)                             # convert our string we just created into an integer

        if x < 0:                                                
            integer = integer * -1                      # turn the resulting int into a negative number if x < 0

        if integer > 2**31 or integer < -2**31:       # if our result created from flipping the intial number "x" is bigger than 2^31 or lower than -2^31 then set the resulting number to 0
            integer = 0
        
        return integer
        