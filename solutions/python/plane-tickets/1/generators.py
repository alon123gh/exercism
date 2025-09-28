"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    letters = tuple("ABCD")
    count = 0
    while count < number:
        yield (letters[count% len(letters)])
        count +=1
        

def inc_row(row):
    row += 1
    if row == 13 :
        row +=1 
    return row    
    
def generate_rows(seats_in_row):
    row = 0
    seats = 0
    while True:
        if (seats % seats_in_row) == 0:
            row = inc_row(row)
        seats +=1    
        yield row
      
def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
  
    SEATS_IN_ROW = 4
    generated_seats_count = 0
    rows = generate_rows(SEATS_IN_ROW)
    seats_letter = generate_seat_letters(number)
    while generated_seats_count < number: 
        for row_seat in range(min(SEATS_IN_ROW, number - generated_seats_count)):
            yield f"{next(rows)}{next(seats_letter)}"
            generated_seats_count += 1
            

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    seats = generate_seats(len(passengers)) 
    return {passenger: next(seats) for passenger in passengers}
 
def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        yield f"{seat}{flight_id}".ljust(12, '0')
    
