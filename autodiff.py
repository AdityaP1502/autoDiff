from copy import deepcopy
from expression import Expression
from evaluate import Evaluate, np

class AutoDiff:
    @classmethod
    def __copyGraph(cls, list : list):
        # create a new copy of the computation graph before calcualting the partial derivatives
        list_copy = deepcopy(list)
        return list_copy
        
 
    @classmethod
    def __forwardPass(cls, list_input : list[Expression]) -> np.ndarray:
        NotImplemented
    
    @classmethod
    def __backwardPass(cls, list_input_val : list[tuple[Expression, float]]) -> np.ndarray:
        """Find all output partial derivatives using backward auto diff

        Args:
            list_output (list[Expression]): All output node -> for now only support for one output

        Returns:
            np.ndarray: Partial Derivatives of all output
        """
        def doForwardPass() -> list[Expression]:
            list_output = []
            
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
                    if len(node.conn[1]) == 0:
                        list_output.append(node) # output node doesn't have to conncetion
                    
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
                        
            return list_output
        
        def findDerivatives():
            # start from the output node, set the value of the partial to one
            stack : list[Expression]  = []
            extra_param = [0, 0, 0, 0, 0]
            
            for out_node in list_output:
                out_node.partialValue = 1
                stack.append(out_node)
                while len(stack) > 0:
                    node = stack.pop()
                    
                    for i in range(len(node.conn[0])):
                        from_node = node.conn[0][i]
                        extra_param[0] = i
                        extra_param[1] = node.val
                        for i in range(len(node.conn[0])):
                            extra_param[2 + i] = node.conn[0][i].val
                        
                        extra_param[-1] = node.param if node.param else 0
                        
                        # use chain rule to find the partial value 
                        from_node.partialValue += node.partialValue * node.derivativeRules("reverse", extra_param)
                        
                        # append to stack to be search later
                        stack.append(from_node)
                        
            # read the output
            partial_derivatives = np.array([])
            for i in range(len(list_input_val)):
                partial_derivatives = np.append(partial_derivatives, list_input_val[i][0].partialValue)
                
            return partial_derivatives
                        
        list_output = doForwardPass()
        return findDerivatives()
                          
        
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
            der = cls.__forwardPass(list_input_val)
            
        elif method == None and len(list_input_val) >= len(list_output) or method == "reverse":
            list_input_val_copy = cls.__copyGraph(list_input_val)
            # do a reverse auto diff
            der = cls.__backwardPass(list_input_val_copy)
            
        else:
            # throw an error, method isn't recognized
            NotImplemented
            
        return der
        
        
        
        
        