class Expression:
    def __init__(self, operation_id : int, connection : list["Expression"] = [], value : float = None, extra_param : int = None) -> None:
        # Extra param only accessed by a specific function such as power and general logartihm and exponent
        self.op = operation_id
        self.conn = connection
        self.val = value
        self.param = extra_param

    @classmethod
    def variable(cls) -> "Expression":
        """Create a variable expression     
        Returns:
            Expression: Variable expression used to define a function 
        """
        
        return cls(0)

    @classmethod
    def function(cls, operation_id : int, connection : list["Expression"]) -> "Expression":
        """Create a function expression node    
        Args:
            operation_id (int): (1 = Addition, 2 = Subtraction, 3 = Multiplication,4 = Division,
            5 = Power (x ** (0.5), x ** (2)),6 = Exponent (e^x),
            7 = Natural Logarithm (ln(x) / log_e (x)),
            8 = Sin ,9 = Cos,10 = Tan,11 = Absolute Value)
            connection (list[Expression]): The function input expression

        Returns:
            Expression: Function Expression
        """

        return cls(operation_id, connection)

    def __operation(self, op_id : int, b : "Expression" = None, extra_param = None) -> "Expression":
        """Create an operation node and update the input connection to include the new operation node   
        Args:
            b (Expression): other expression 
            op_id (int): operation id   
        Returns:
            Expression: Expression node that represent the operation
        """

        # Create a new node with operation add that connect to node a
        func_node = self.function(op_id, [self])
        self.conn.append(func_node)
        
        # If exist another input
        if b != None:
            func_node.conn.append(b)
            b.conn.append(func_node)    
            
        return func_node    
    
    # Basic Arithmetic Operation 
    def __add__(self, b : "Expression") -> "Expression":
        return self.__operation(1, b)

    def __sub__(self, b : "Expression") -> "Expression":
        return self.__operation(2, b)

    def __mul__(self, b : "Expression") -> "Expression":
        return self.__operation(3, b)

    def __truediv__(self, b : "Expression") -> "Expression":
        return self.__operation(4, b)
    
    def __pow__(self, b : float) -> "Expression":
        # extra param to store the power 
        return self.__operation(5, extra_param = b)
    
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
    def abs(cls, a : "Expression") -> "Expression":
        return cls.__operation(a, 11)



if __name__ == "__main__":
    # initialize a variable
    x = Expression.variable()
    y = Expression.variable()
    
    # create an function equation
    expr = Expression.abs(x + x*(y ** 2))
    print(expr)