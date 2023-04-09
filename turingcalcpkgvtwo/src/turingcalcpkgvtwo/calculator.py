class Calculator():

  result = 0
  cleared = True

  def display(self):
    """Display method to show current state of memory."""
    print('Result: ', self.result)
    print('Memory Cleared: ', self.cleared)

  def add(self, *args:float)-> float:
    """Addition method. Can take one number or more than one number. 
    If more than one number, separate each number with a comma""" 
    for i in args:
      self.result = self.result + i
    self.cleared = False
    return self.result

  def subtract(self, *args: float)-> float:
    """Subtraction method. Can take one number or more than one number. 
    If more than one number, separate each number with a comma""" 
    for i in args:
      self.result = self.result - i
    self.cleared = False
    return self.result    

  def multiply(self, *args:float)-> float:
    """Multiplication method. Can take one number or more than one number. 
    If more than one number, separate each number with a comma""" 
    for i in args:
      self.result = self.result * i
    self.cleared = False
    return self.result

  def divide(self, *args:float)-> float:
    """Division method. Can take one number or more than one number. 
    If more than one number, separate each number with a comma""" 
    for i in args:
      if i == 0:
        print('Cannot divide by zero.')
        break
      self.result = self.result / i
    self.cleared = False
    return self.result

  def nroot(self, n:float)-> float:
    """Root method. Can take one number that is the root number. 
    This method will then find the root of the number already in memory, 
    however number in memory must be non-negative.
    """ 
    x = self.result
    if n == 0:
      return 'undefined...'
    elif x < 0:
      return 'NaN'
    else:
      self.result = x**(1/n)
      self.result = round(self.result,4)
      self.cleared = False
      return self.result

  def nthroot(self, x:float, n:float)-> float:
    """Nth root method. Method takes two numbers, first is the number
    that you want to find the root of. The second number is the root number.""" 
    if x < 0:
      return 0
    else:
      return x**(1/n)

  def sqroot(self, number:float)-> float:
    """Square root method. Find the square root of the given number.""" 
    return number**(1/2)

  def clear(self):
    self.result = 0
    self.cleared = True 

  def instructions(self):
    print("""This calculator can add, subtract, multiply, and divide any amount of numbers. It can also return the square root of one number.

    After every method call, unless you clear the memory, the next method used will use the resulting number from the previous method. To clear the memory, call the clear method. Example: object_instance.clear(). 
    
    To add, call the add method and type in the numbers that you want added separated by commas. Example: object_instance.add(2, 3, 6). The reult of 11 will be printed.
    
    To subtract, call the subtract method and type in the numbers that you want subtracted separated by commas. Example: object_instance.subtract(10, 8, 2, 4). The printed result will be -4.
    
    To multiply, the call multiply method and type in the numbers that you want multiplied separated by commas. Example: object_instance.multiply(2, 2, 4) will result in 16.
    
    To divide, call the divide method and type in the numbers that you want divided but do NOT type in zero ('0'). Example: object_instance.divide(100, 4, 5) will result in 5.
    
    To find the (n) root of a number with that number being the number in the calculator's memory, call the nroot method. Please note, that to take the root of the number that you wnat, you will have to clear the memory first with 'obj_instance.clear()' then use the '.add()' method, adding the number that you want to find the root of. Example: obj_instance.nroot(2) will find the square root of whatever number is in memory. 

    To find the nth root of a number, call the nthroot method and type in the number you want to find the root or, such as 27, and then separated by a comma, type in the root of the number that you want to find. Example: object_instance.nthroot(27, 3) will result in 3.0.

    To find the square root of a number, call the sqroot method and type in just one number (i.e. the number you want to find the square rood of). Example: object_instance.sqroot(4) will result in 2.0.
    
    You can call the method: .display() to display the current number that is in memory along with an indication if it has been cleared.""")