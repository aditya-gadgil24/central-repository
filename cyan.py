"""This file and its code blocks illustrate the core functionality of python including control flow, loops, logical/arithematic
operators, functions"""

# 1

upper_bracket = True
age = 37
if age < 35 or upper_bracket:
    print('send-interest')
else:
    print('no-action!')
# end


# 2

x = 1
while x < 99999:
    print(x)
    x = x * 2.75

# end






#Write function to evaluate tyre pressure values using standard value
psi_value = 33
if psi_value < 33:
    print('The tyre pressure is low')
elif psi_value == 33:
    print('The pressure matches the standard value')
else:
    print('The pressure exceeds the standard value')
#Print the output to console


#Write function to compute the value of gbp in inr
def gbpinrfx(gbp, exr):
    return gbp * exr
#This will return the value of the arguments of the function
curconverter = gbpinrfx(17989, 108.75)
print(curconverter)
#Print the output to console or terminal
#The convereted value of gbp to inr is 1956303.75



#Write code to compute the value of mathematical operations on int values
ab = 4545644
cd = 7845656
ef = 561240
gh = 983456
alv = ab + cd - ef * gh
#Print the output to console
print('The result of the compute operation is:', alv)
#The result of the compute operation is: -551942454140


#Write code to use the while loop for executing code block

axy = 23
while axy < 1000:
    print(axy)
    axy = axy * 1.75

#Write code to index a string
ods = 'steveclairejobs'
#Print the output to console
print(ods[11])
#The resultant value will be passed on to the terminal


#Write code to index a list
tsil = ['earth', 'water', 'fire', 'sky', 'ocean', 'soil', 'trees']
print(tsil[3])
#This will print the output to terminal


#Write code to slice a string
xing = 'bobbdiamondthegreat'
#Print the output to console
print(xing[:6])


#Write function to compute the cost of litigation for a client
def litfee(dc, lf, hc, ac):
    return dc + lf + hc + ac
#Calling the function with values for arguments
lawfee = litfee(25000, 75000, 185000, 95750)
#Print the output to console
print('The total cost for client abc is:', lawfee)
#litfee represents the total cost for client for availing law firm services


"""End of script file"""