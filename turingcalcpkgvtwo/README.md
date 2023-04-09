# Calculator Package

## Installation
`pip install -i https://test.pypi.org/simple/ turingcalcpkgvtwo==0.0.8`

## Usage
```python
c = calculator.Calculator()
c.add(5,3,2)
#Expected result = 10
```

This calculator can add, subtract, multiply, and divide any amount of numbers. It can also return the square root of one number.

    After every method call, unless you clear the memory, the next method used will use the resulting number from the previous method. To clear the memory, call the clear method. Example: object_instance.clear(). 
    
    To add, call the add method and type in the numbers that you want added separated by commas. Example: object_instance.add(2, 3, 6). The result of 11 will be printed.

    To subtract, call the subtract method and type in the numbers that you want subtracted separated by commas. Example: object_instance.subtract(10, 8, 2, 4). The printed result will be -4.

    To multiply, the call multiply method and type in the numbers that you want multiplied separated by commas. Example: object_instance.multiply(2, 2, 4) will result in 16.

    To divide, call the divide method and type in the numbers that you want divided but do NOT type in zero ('0'). Example: object_instance.divide(100, 4, 5) will result in 5.

    To find the nth root of a number, call the nthroot method and type in the number you want to find the root or, such as 27, and then separated by a comma, type in the root of the number that you want to find. Example: object_instance.nthroot(27, 3) will result in 3.0.

    To find the square root of a number, call the sqroot method and type in just one number (i.e. the number you want to find the square rood of). Example: object_instance.sqroot(4) will result in 2.0.
    
    You can call the method: .display() to display the current number that is in memory along with an indication if it has been cleared.