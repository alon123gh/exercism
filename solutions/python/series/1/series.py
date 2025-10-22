
def validate(series, length):
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if  length < 0:
        raise ValueError("slice length cannot be negative")
    if not series:
        raise ValueError("series cannot be empty") 
    if len(series) < length:
        raise ValueError("slice length cannot be greater than series length")

def slices(series, length):

    validate(series, length)
    start = 0
    end = len(series)  - length + 1
    return [series[pos:pos+length] for pos  in range(start,end)]
        
        
