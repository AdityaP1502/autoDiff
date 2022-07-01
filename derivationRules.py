import numpy as np

class Rules():
    """Derivative Rules. 
    For Reveres Method : Rules Function Evaluate dn_i / dn_j where n_i is the to node and n_j is the from node.
    """
    @staticmethod
    def add(method : str) -> int:
        if method == "reverse":
            return 1
        
        elif method ==  "forward":
            NotImplemented
            
        else:
            NotImplemented
            
    @staticmethod
    def sub(method : str, isPositive : bool) -> int:
        if method == "reverse":
            return 1 if isPositive else -1
        
        elif method == "forward":
            NotImplemented
            
        else:
            NotImplemented
            
    @staticmethod
    def mul(method : str, other_input_val : float) -> float:
        """n_i = n_j * n_k

        Args:
            method (str): "reverse" or "forward"
            other_input_val (float): if try to find dn_i / dn_j then other_input_val would be n_k.val, etv

        Returns:
            float : result
        """
        
        if method == "reverse":
            return other_input_val
        
        elif method == "forward":
            NotImplemented
            
        else:
            NotImplemented
            
    @staticmethod        
    def div(method : str, isNumerator : bool, from_node_val : list[int]):
        # numerator = 0, denominator = 1
        numenVal, denomVal = from_node_val
        
        if method == "reverse":
            return 1 / denomVal if isNumerator else -1 * (numenVal / (denomVal ** 2))
        
        elif method == "forward":
            NotImplemented
            
        else:
            NotImplemented
            
    @staticmethod        
    def pow(method : str, power : int, from_node_val):
        if method == "reverse":
            return power * from_node_val ** (power - 1)
        
        elif method == "forward":
            NotImplemented
            
        else:
            NotImplemented
            
    @staticmethod        
    def exponent(method : str, node_val : float):
        if method == "reverse":
            return node_val
        
        elif method == "forward":
            NotImplemented
            
        else:
            NotImplemented
            
    @staticmethod        
    def ln(method : str, from_node_val : float):
        if method == "reverse":
            return 1 / from_node_val
        
        elif method == "forward":
            NotImplemented
            
        else:
            NotImplemented
            
    @staticmethod    
    def sin(method : str, from_node_val : float):
        if method == "reverse":
            return np.cos(from_node_val)
        
        elif method == "forward":
            NotImplemented
            
        else:
            NotImplemented
            
    @staticmethod        
    def cos(method : str, from_node_val : float):
        if method == "reverse":
            return -1 * (np.sin(from_node_val))
        
        elif method == "forward":
            NotImplemented
            
        else:
            NotImplemented
            
    @staticmethod        
    def tan(method : str, from_node_val : float):
        if method == "reverse":
            return (1 / np.cos(from_node_val)) ** 2
        
        elif method == "forward":
            NotImplemented
            
        else:
            NotImplemented
    @staticmethod        
    def asin(method : str, from_node_val : float):
        if method == "reverse":
            return 1 / np.sqrt(1 - from_node_val ** 2)
        
        elif method == "forward":
            NotImplemented
            
        else:
            NotImplemented
            
    @staticmethod        
    def acos(method : str, from_node_val : float):
        if method == "reverse":
            return -1 * (1 / np.sqrt(1 - from_node_val ** 2))
        
        elif method == "forward":
            NotImplemented
            
        else:
            NotImplemented
            
    @staticmethod        
    def atan(method : str, from_node_val : float):
        if method == "reverse":
            return 1 / (1 + from_node_val ** 2)
        
        elif method == "forward":
            NotImplemented
            
        else:
            NotImplemented
            
    @staticmethod        
    def abs(method : str, from_node_val : float):
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
            