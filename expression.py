# Need to Find a way to able to create value for multiple output, it will be a waste to create a new graph for each output
# For now only support for one output

import numpy as np
from derivationRules import Rules

class Evaluate():
    @staticmethod
    def add(node : "Expression") -> float:
        # add value of the input (from)
        node.val = node.conn[0][0].val + node.conn[0][1].val
        
    @staticmethod
    def sub(node : "Expression") -> float:
        # add value of the input (from)
        node.val = node.conn[0][0].val - node.conn[0][1].val
    
    @staticmethod
    def mul(node : "Expression") -> float:
        # add value of the input (from)
        node.val = node.conn[0][0].val * node.conn[0][1].val
        
    @staticmethod
    def div(node : "Expression") -> float:
        # add value of the input (from)
        node.val = node.conn[0][0].val / node.conn[0][1].val
        
    @staticmethod
    def pow(node : "Expression"):
        node.val = node.conn[0][0].val ** node.param
        
    @staticmethod
    def exponent(node : "Expression", x : float):
        node.val = np.e ** (x)
        
    @staticmethod
    def ln(node : "Expression", x : float):
        node.val = np.log(x)
        
    @staticmethod
    def sin(node : "Expression", x : float):
        node.val = np.sin(x)
        
    @staticmethod
    def cos(node : "Expression", x : float):
        node.val = np.cos(x)
      
    @staticmethod
    def tan(node : "Expression", x : float):
        node.val = np.tan(x)
        
    @staticmethod
    def asin(node : "Expression", x : float):
        node.val = np.arcsin(x)
    
    @staticmethod   
    def acos(node : "Expression", x : float):
        node.val = np.arccos(x)
        
    @staticmethod    
    def atan(node : "Expression", x : float):
        node.val = np.arctan(x)
        
    @staticmethod    
    def abs(node : "Expression", x : float):
        node.val = np.abs(x)
        
class Expression:
    def __init__(self, operation_id : int, dRules : function = None, evalFunc  : function = None, connection : list[list["Expression"]] = [[], []], value : float = None, extra_param : int = None) -> None:
        # connection is a 2D array. 0th index = From and 1th index = To
        # Extra param only accessed by a specific function such as power and general logartihm and exponent
        self.op = operation_id
        self.conn = connection
        self.val = value # used when calculating the partial derivatives
        self.param = extra_param
        self.derivativeRules = dRules # used to calculate the derivatives
        self.eval = evalFunc # used to evaluate the node value

    @classmethod
    def constant(cls, value : float) -> "Expression":
        """Create a constant

        Returns:
            Expression: Constant Expression
        """
        
        return cls(-1, value = value)
    
    @classmethod
    def variable(cls) -> "Expression":
        """Create a variable expression     
        Returns:
            Expression: Variable expression used to define a function 
        """
        
        return cls(0)

    @classmethod
    def function(cls, operation_id : int, connection : list[list["Expression"]], evalFunc : function, dRules : function) -> "Expression":
        """Create a function expression node    
        Args:
            operation_id (int): (1 = Addition, 2 = Subtraction, 3 = Multiplication, 4 = Division,
            5 = Power (x ** (0.5), x ** (2)), 6 = Exponent (e^x),
            7 = Natural Logarithm (ln(x) / log_e (x)),
            8 = Sin, 9 = Cos,10 = Tan, 11 = asin, 12 = acos, 13 = atan, 14 = abs)
            connection (list[Expression]): The function input expression

        Returns:
            Expression: Function Expression
        """

        return cls(operation_id, dRules, evalFunc, connection)

    @classmethod
    def __operation(cls, a : "Expression", op_id : int, evalFunc : function, dRules : function, b : "Expression" = None, extra_param = None, ) -> "Expression":
        """Create an operation node and update the input connection to include the new operation node   
        Args:
            b (Expression): other expression 
            op_id (int): operation id   
        Returns:
            Expression: Expression node that represent the operation
        """

        # Create a new node with operation add that connect to node a. New Node Will From A. a will go to new Node
        func_node = cls.function(op_id, dRules, evalFunc, [[a], []]) # put a in from array
        a.conn[1].append(func_node) # Put in in to array
        
        # If exist another input
        if b != None:
            func_node.conn[0].append(b) # new Node also from b
            b.conn[1].append(func_node) # add new node in to conn in b  
            
        return func_node    
    
    # Basic Arithmetic Operation 
    def __add__(self, b : "Expression") -> "Expression":
        return self.__operation(self, 1, b)

    def __sub__(self, b : "Expression") -> "Expression":
        return self.__operation(self, 2, b)

    def __mul__(self, b : "Expression") -> "Expression":
        return self.__operation(self, 3, b)

    def __truediv__(self, b : "Expression") -> "Expression":
        return self.__operation(self, 4, b)
    
    def __pow__(self, b : float) -> "Expression":
        # extra param to store the power 
        return self.__operation(self, 5, extra_param = b)
    
    # Math Function
    @classmethod 
    def exponent(cls, a : "Expression") -> "Expression":
        return cls.__operation(a, 6)
    
    @classmethod
    def ln(cls, a : "Expression") -> "Expression":
        return cls.__operation(a, 7)
    
    @classmethod
    def sin(cls, a : "Expression") -> "Expression":
        return cls.__operation(a, 8)
    
    @classmethod
    def cos(cls, a : "Expression") -> "Expression":
        return cls.__operation(a, 9)
    
    @classmethod
    def tan(cls, a : "Expression") -> "Expression":
        return cls.__operation(a, 10)
    
    @classmethod
    def asin(cls, a : "Expression") -> "Expression":
        return cls.__operation(a, 11)
    
    @classmethod
    def acos(cls, a : "Expression") -> "Expression":
        return cls.__operation(a, 12)
    
    @classmethod
    def atan(cls, a : "Expression") -> "Expression":
        return cls.__operation(a, 13)
    
    @classmethod
    def abs(cls, a : "Expression") -> "Expression":
        return cls.__operation(a, 14)



if __name__ == "__main__":
    # initialize a variable
    x = Expression.variable()
    y = Expression.variable()
    
    # create an function equation
    expr = Expression.sin(x + x*(y ** 2)) + Expression.cos(x * y) + Expression.constant(5)
    print(expr)