import numpy as np

class Evaluate():
    @staticmethod
    def add(x : float, y : float, extra_param : float = None) -> None:
        # add value of the input (from)
        return x + y
        
    @staticmethod
    def sub(x : float, y : float, extra_param : float = None) -> None:
        # subtract value of the input (from)
        return x - y
    
    @staticmethod
    def mul(x : float, y : float, extra_param : float = None) -> None:
        # multiply value of the input (from)
        return x * y
        
    @staticmethod
    def div(x : float, y : float, extra_param : float = None) -> None:
        # divide value of the input (from)
        return x / y
        
    @staticmethod
    def pow(x : float, y : float = None, extra_param : float = None) -> None:
        return x ** extra_param
        
    @staticmethod
    def exponent(x : float, y : float = None, extra_param : float = None) -> None:
        return np.e ** (x)
        
    @staticmethod
    def ln(x : float, y : float = None, extra_param : float = None) -> None:
        return np.log(x)
        
    @staticmethod
    def sin(x : float, y : float = None, extra_param : float = None) -> None:
        return np.sin(x)
        
    @staticmethod
    def cos(x : float, y : float = None, extra_param : float = None) -> None:
        return np.cos(x)
      
    @staticmethod
    def tan(x : float, y : float = None, extra_param : float = None) -> None:
        return np.tan(x)
        
    @staticmethod
    def asin(x : float, y : float = None, extra_param : float = None) -> None:
        return np.arcsin(x)
    
    @staticmethod   
    def acos(x : float, y : float = None, extra_param : float = None) -> None:
        return np.arccos(x)
        
    @staticmethod    
    def atan(x : float, y : float = None, extra_param : float = None) -> None:
        return np.arctan(x)
        
    @staticmethod    
    def abs(x : float, y : float = None, extra_param : float = None) -> None:
        return np.abs(x)
    
class Rules():
    """Derivative Rules. 
    For Reveres Method : Rules Function Evaluate dn_i / dn_j where n_i is the to node and n_j is the from node.
    """
    @staticmethod
    def add(method : str, extra_param : any) -> int:
        if method == "reverse":
            return 1
        
        elif method ==  "forward":
            NotImplemented
            
        else:
            NotImplemented
            
    @staticmethod
    def sub(method : str, extra_param : any) -> int:
        isPositive = extra_param[0]
        
        if method == "reverse":
            return 1 if isPositive else -1
        
        elif method == "forward":
            NotImplemented
            
        else:
            NotImplemented
            
    @staticmethod
    def mul(method : str, extra_param : any) -> float:
        other_input_val = extra_param[0]
        
        if method == "reverse":
            return other_input_val
        
        elif method == "forward":
            NotImplemented
            
        else:
            NotImplemented
            
    @staticmethod        
    def div(method : str, extra_param : any) -> float:
        isNumerator, from_node_val =  extra_param[:2]
        
        # numerator = 0, denominator = 1
        numenVal, denomVal = from_node_val
        
        if method == "reverse":
            return 1 / denomVal if isNumerator else -1 * (numenVal / (denomVal ** 2))
        
        elif method == "forward":
            NotImplemented
            
        else:
            NotImplemented
            
    @staticmethod        
    def pow(method : str, extra_param : any) -> float:
        power, from_node_val = extra_param[:2]
        
        if method == "reverse":
            return power * from_node_val ** (power - 1)
        
        elif method == "forward":
            NotImplemented
            
        else:
            NotImplemented
            
    @staticmethod        
    def exponent(method : str, extra_param : any) -> float:
        node_val = extra_param[0]
        
        if method == "reverse":
            return node_val
        
        elif method == "forward":
            NotImplemented
            
        else:
            NotImplemented
            
    @staticmethod        
    def ln(method : str, extra_param : any) -> float:
        from_node_val = extra_param[0]
        if method == "reverse":
            return 1 / from_node_val
        
        elif method == "forward":
            NotImplemented
            
        else:
            NotImplemented
            
    @staticmethod    
    def sin(method : str, extra_param : any) -> float:
        from_node_val = extra_param[0]
        if method == "reverse":
            return np.cos(from_node_val)
        
        elif method == "forward":
            NotImplemented
            
        else:
            NotImplemented
            
    @staticmethod        
    def cos(method : str, extra_param : any) -> float:
        from_node_val = extra_param[0]
        if method == "reverse":
            return -1 * (np.sin(from_node_val))
        
        elif method == "forward":
            NotImplemented
            
        else:
            NotImplemented
            
    @staticmethod        
    def tan(method : str, extra_param : any) -> float:
        from_node_val = extra_param[0]
        if method == "reverse":
            return (1 / np.cos(from_node_val)) ** 2
        
        elif method == "forward":
            NotImplemented
            
        else:
            NotImplemented
            
    @staticmethod        
    def asin(method : str, extra_param : any) -> float:
        from_node_val = extra_param[0]
        if method == "reverse":
            return 1 / np.sqrt(1 - from_node_val ** 2)
        
        elif method == "forward":
            NotImplemented
            
        else:
            NotImplemented
            
    @staticmethod        
    def acos(method : str, extra_param : any) -> float:
        from_node_val = extra_param[0]
        if method == "reverse":
            return -1 * (1 / np.sqrt(1 - from_node_val ** 2))
        
        elif method == "forward":
            NotImplemented
            
        else:
            NotImplemented
            
    @staticmethod        
    def atan(method : str, extra_param : any) -> float:
        from_node_val = extra_param[0]
        if method == "reverse":
            return 1 / (1 + from_node_val ** 2)
        
        elif method == "forward":
            NotImplemented
            
        else:
            NotImplemented
            
    @staticmethod        
    def abs(method : str, extra_param : any) -> int:
        from_node_val = extra_param[0]
        if method == "reverse":
            if from_node_val == 0:
                # division 0 with 0
                NotImplemented
                
            else:
                return 1 if from_node_val > 0 else -1
            
        
        elif method == "forward":
            NotImplemented
            
        else:
            NotImplemented
            