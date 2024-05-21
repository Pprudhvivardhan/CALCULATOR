from logic import do_addition, do_substraction

def main():
    print('Welcome to Calculator app')
    print('''
        Select the functionalities needed
        1. add
        2. sub
        ''')
    user_input = input('select the function: ')
    
    a = int(input('input of A: '))
    b = int(input('input of B: '))
    
    if user_input == '1':
        result = do_addition(a,b)
    elif user_input == '2':
        result = do_substraction(a,b)
        
    print('Result:',result)
    
if __name__=='__main__':
    main()
