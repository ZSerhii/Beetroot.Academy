print('Welcome!')
print('Select the operation from the list and enter its marking')
print('''Available operations:
 > +    - Sum of X and Y
 > -    - Difference of X and Y
 > *    - Product of X and Y
 > /    - Quotient of X and Y
 > //   - Floored quotient of X and Y
 > %    - Remainder of X / Y
 > neg  - X negated
 > abs  - Absolute value or magnitude of X
 > pow  - X to the power Y
 > sqr  - X to the power 2 (multiplying X by itself)
 > sqrt - Square root of X
 ''')

vOperationsList           = ('+', '-', '*', '/', '//', '%', 'neg', 'abs', 'pow', 'sqr', 'sqrt')
vOperationsWithOneOperand = ('neg', 'abs', 'sqr', 'sqrt')
vOperationsWithTwoOperand = ('pow')
vOperationsDivisionByZero = ('/', '//', '%')    

vOperation = input('Input your operation: ').strip().lower()

if vOperation in vOperationsList:
    vGreeting = '\nCongratulations!!! \nYou have selected the {} operation.'.format(vOperation)

    if vOperation in vOperationsWithOneOperand:
        vRequest  = 'Input one numeric.'
    else:
        vRequest  = 'Input two numerics.'

    print(vGreeting)
    print(vRequest, '\n')

    if vOperation in vOperationsWithOneOperand:
        vX_Input = 'Input X-operand for operation {}(X): '.format(vOperation)
    else:
        if vOperation in vOperationsWithTwoOperand:
            vX_Input = 'Input X-operand for operation {}(X , Y): '.format(vOperation)
        else:
            vX_Input = 'Input X-operand for operation X {} Y: '.format(vOperation)

    vX_Error = False
    vX_Neg   = False

    vX = input(vX_Input).strip()

    if vX.find(',') > 0:
        vX = vX.replace(',', '.')  

    if vX.find('-') == 0:
        vX     = vX.replace('-', '')
        vX_Neg = True
    
    vX_List = vX.split('.')
    
    if len(vX_List) == 1:
        vX = int(vX_List[0])
    else:
        if len(vX_List) == 2:
            vX = int(vX_List[0]) + int(vX_List[1]) / (10 ** len(str(vX_List[1])))
        else:
            vX_Error = True

    if not vX_Error:
        if vX_Neg:
            vX = -1 * vX

        if not vOperation in vOperationsWithOneOperand:
            if vOperation in vOperationsWithTwoOperand:
                vY_Input = 'Input Y-operand for operation {}({} , Y): '.format(vOperation, vX)
            else:
                vY_Input = 'Input Y-operand for operation {} {} Y: '.format(vX, vOperation)
        
            vY_Error = False
            vY_Neg   = False

            vY = input(vY_Input).strip()

            if vY.find(',') > 0:
                vY = vY.replace(',', '.')  

            if vY.find('-') == 0:
                vY     = vY.replace('-', '')
                vY_Neg = True
            
            vY_List = vY.split('.')
            
            if len(vY_List) == 1:
                vY = int(vY_List[0])
            else:
                if len(vY_List) == 2:
                    vY = int(vY_List[0]) + int(vY_List[1]) / (10 ** len(str(vY_List[1])))
                else:
                    vY_Error = True

            if not vY_Error:
                if vY_Neg:
                    vY = -1 * vY
                
                if vOperation in vOperationsWithTwoOperand:
                    vResult = '\nResult: {}({}, {}) ='.format(vOperation, vX, vY)
                else:
                    vResult = '\nResult: {} {} {} ='.format(vX, vOperation, vY)

                if (vOperation in vOperationsDivisionByZero) and (vY == 0):
                    print(vResult, 'Error! Division by zero!')
                else:
                    if vOperation == '+':
                        print(vResult, vX + vY)
                    else:
                        if vOperation == '-':
                            print(vResult, vX - vY)
                        else:
                            if vOperation == '*':
                                print(vResult, vX * vY)
                            else:
                                if vOperation == '/':
                                    print(vResult, vX / vY)
                                else:
                                    if vOperation == '//':
                                        print(vResult, vX // vY)
                                    else:
                                        if vOperation == '%':
                                            print(vResult, vX % vY)
                                        else:
                                            if vOperation == 'pow':
                                                print(vResult, vX ** vY)
            else:
                print('Wrong Y-operand. "{}" is not numeric value'.format(vY))    
        else:
            vResult = '\nResult: {}({}) ='.format(vOperation, vX)

            if vOperation == 'neg':
                print(vResult, -vX)
            else:
                if vOperation == 'abs':
                    print(vResult, abs(vX))
                else:
                    if vOperation == 'sqr':
                        print(vResult, vX * vX)
                    else:
                        if vOperation == 'sqrt':
                            if vX < 0:
                                print(vResult, 'Error! X-operand cannot be negative!')
                            else:
                                import math

                                print(vResult, math.sqrt(vX))
    else:
        print('Wrong X-operand. "{}" is not numeric value'.format(vX))    
else:    
    print('Wrong operation. Operation "{}" is not supported.'.format(vOperation))

print('')