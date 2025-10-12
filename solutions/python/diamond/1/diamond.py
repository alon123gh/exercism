
def get_row(letter, internal_padding, max_row_size, single_letter):
    row = None
    if single_letter:
           row = letter          
    else:
           row = f"{letter}{' '*internal_padding}{letter}"
    return  f"{row: ^{max_row_size}}"     
   
   
def rows(letter):
    
    output = []
    num_of_rows = (ord(letter) - ord("A")) * 2 +1 
    letter_pos = ord(letter) - ord("A") 
    max_row_size  = (2*letter_pos-1) + 2 #middle dots + Letter on each side  
    ranges = [ [letter_pos+1], [letter_pos-1,-1,-1 ]  ]
    for rng in ranges:
        for row_num in range(*rng ):    
          letter = chr(ord("A")+row_num)  
          output.append(get_row(letter, max(0,2*row_num -1), max_row_size, row_num==0))
    return output
    

