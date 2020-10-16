'''
Created on Dec 18, 2019

@author: roy.hsieh
'''

def num_to_str(number):
    if number == 0:
        print("zero")
    number = [int(x) for x in str(number)]
    soln = ""
    tens = [ "","","Twenty","Thirty","Forty", "Fifty","Sixty","Seventy","Eighty","Ninety"]
    under_20 = ["","One","Two","Three","Four","Five", "Six","Seven","Eight","Nine",
                "Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen",
                "Nineteen"]
    if len(number)>3:
        soln = under_20[number[-4]] +" Thousand "
    if len(number) >2:
        soln += under_20[number[-3]] +" Hundred "
    if len(number) > 1:
        if number[-2] == 1:
            soln += under_20[number[-1]+10]
        else:
            if number[-2] > 0:
                soln += tens[number[-2]] + " "
            soln += under_20[number[-1]]
    else:
        soln = under_20[number[-1]]
    print(soln)
    
num_to_str(raw_input("Enter number here: "))