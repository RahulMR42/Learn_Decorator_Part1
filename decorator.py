from colorama import init, Fore, Back, Style
import timeit

init(convert=True)


def plain_decorator(func):
    print(Back.BLACK , Fore.RED + "Inside The plain decorator")
    return func
    
def upper_case(function_as_argument):
    print(Fore.GREEN + "!!! Inside upper case decorator")
    def wrapper():
        print(Fore.GREEN + "!!! Inside the wrapper under upper case decorator")
        value_from_decoratoed_function = function_as_argument()
        print(Fore.GREEN + "!!! Intermediate result from function >>>" + value_from_decoratoed_function)
        new_Value_to_return_from_wrapper = value_from_decoratoed_function.upper()
        return new_Value_to_return_from_wrapper
    print(Fore.GREEN  + "!!! Finally sending the output from wrapper as an end result of this decorator")
    return wrapper

def timeit_decorator(func):
    def wrapper():
        value_from_timeit =  timeit.timeit()
        print("{} Execution time {}".format(Back.WHITE,value_from_timeit))
        print(Style.RESET_ALL)
        return(func())
    return wrapper


def decorate():
    """Decorators are callable objects which are used to modify functions or classes.
    Decorators allow you to define reusable building blocks that can change or extend 
    the behavior of other functions. And they let you do that without permanently modifying 
    the wrapped function itself. The function’s behavior changes only when it’s decorated."""
    print(Fore.GREEN + '!! start to explore decorator ')

    @plain_decorator
    @timeit_decorator
    def printfunction():
        return (Fore.RED + "response from print function with plain decorator")
    @upper_case
    @timeit_decorator
    def function_with_a_parameter_to_decorator():
        return(Fore.YELLOW + "Inside function with a decorator expecting a parameter")

    print(printfunction())
    print(function_with_a_parameter_to_decorator())

""""Sample execution of decorator with an optional arguments"""
@timeit_decorator
def start():
    print(Fore.GREEN + 'explain a function as an argument')
    
    def func1():
        print(Fore.BLUE + "Inside function 1")
    
    def fun2(functin_as_arg):
        print(Fore.BLUE + "Inside function 2")
        functin_as_arg()
    fun2(func1)
    decorate()
    


    

""""
Decorators modify the behavior of a callable through a wrapper so you don’t 
have to permanently modify the original. The callable isn’t permanently modified—its 
behavior changes only when decorated."""
    
        

if __name__ == "__main__":
    start()

    