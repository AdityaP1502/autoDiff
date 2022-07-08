from expression import Expression
from evaluate import np

class AutoDiff:
    @classmethod
    def __forwardPass(cls, list_input : list[Expression]) -> np.ndarray:
        NotImplemented
    
    @classmethod
    def __backwardPass(cls, list_output : list[Expression], list_input_val : list[tuple[Expression, float]]) -> np.ndarray:
        """Find all output partial derivatives using backward auto diff

        Args:
            list_output (list[Expression]): All output node -> for now only support for one output

        Returns:
            np.ndarray: Partial Derivatives of all output
        """
        def doForwardPass():
            # in conn, 0 = from, 1 = to
            # Do Forward Pass to get the value for each node
            # pick the first node to explore 
            # If a node need to value, and the other node val is None, backtrack to find another node to explore
            
            stack = [] # stack to backtrack, keep node that has another node to explore
            for (inputNode, val) in list_input_val:
                inputNode.val = val
                stack = [[inputNode, 0]] # store the node and the to index that want to be explored
                
                while len(stack) != 0:
                    node, conn_idx = stack[-1]
                      
                    if conn_idx < len(node.conn[1]):
                        node = node.conn[1][conn_idx] # visit the node
                        
                        stack[-1][1] += 1 # update the node that want to be search
                        noneValNode = False # flag if there are none node value in from connection 
                        
                        # check if can get value
                        for i in range(len(node.conn[0])):
                            if not node.conn[0][i].val:
                                # need extra node value, can't get this node value
                                noneValNode = True # update the flag
                                break
                            
                        if not noneValNode:
                            # update the value
                            args = [0, 0, 0]
                            for i in range(len(node.conn[0])):
                                args[i] = node.conn[0][i].val
                                
                            args[2] = node.param if node.param else 0
                            
                            node.val = node.eval(*args) # evaluate 
                            
                            # store in stack to be explored
                            # update the conn_idx in current stack
                            if stack[-1][1] > len(node.conn[1]):
                                # if the last node doesn't have any connection, replace
                                stack[-1] = [node, 0]
                                
                            else:
                                # append the new node
                                stack.append([node, 0])
                                
                    else:
                        del stack[-1]
                                

                                
        doForwardPass()
        print(list_output[0].val)
                          
        
    @classmethod
    def partialDerivatives(cls, list_input_val : list[tuple[Expression, float]], list_output : list[Expression], method : str = None) -> np.ndarray:
        """Calculate partial derivatives using auto differentiation. 

        Args:
            list_input_val(list[tuple[Expression, float]]) : all of the system input variable value
            list_output(list[Expression]) : all of the system output expression / equation
            method (str, optional): Auto differentiation method(args : 
            "forward" = calculate partial derivatives using forward auto differentiation. Efficient for input > output.
            "reverse" = calculate partial derivatives using reverse auto differentiation). Efficient for output < input. Defaults to None (auto). 

        Returns:
            np.ndarray: All Partial Derivatives for all given input for a given input value and also the system output
        """
    
        if method == None and len(list_input_val) < len(list_output) or method == "forward":
            # Do a forward auto diff
            cls.__forwardPass(list_input_val)
            
        elif method == None and len(list_input_val) >= len(list_output) or method == "reverse":
            # do a reverse auto diff
            cls.__backwardPass(list_output, list_input_val)
            
        else:
            # throw an error, method isn't recognized
            NotImplemented
            
        
        
        
        
        