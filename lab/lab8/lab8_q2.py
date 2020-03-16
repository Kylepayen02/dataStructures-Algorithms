import ArrayStack from ArrayStack 

def eval_prefix(exp_str):
    """
    : exp type: str
    : return type: int
    """
    exp_lst = exp_str.split( )
    s = ArrayStack()
    for i in exp_lst:
        if len(s)==0:
            s.push(i)
            
                
            
    

exp_str = "- + * 16 5 * 8 4 20"
