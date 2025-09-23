import re

ISBN_LEN = 10
def translate(ch):
    if ch.isdigit():
        return int(ch)
    if ch != 'X':
        raise ValueErro('Invalid character {ch}')   
    return 10  
    
def is_valid(isbn):
    sum  = 0
    if  re.search(r'[^X0-9-]',isbn):
        return False
    if  re.match(r'.*X.+',isbn):
        return False
    isbn = re.sub(r'[^0-9X]','', isbn )            
    if len(isbn) != ISBN_LEN:
        return False
    try:
            
        for index, ch in enumerate(isbn):
            sum += translate(ch) * (ISBN_LEN-index)
    except ValueErro:
        return False
        
    return (sum % 11) == 0
     
    
