

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

subjects = ["house that Jack built.",
"malt",
"rat",
"cat",
"dog",
"cow with the crumpled horn",
"maiden all forlorn",
"man all tattered and torn",
"priest all shaven and shorn",
"rooster that crowed in the morn",
"farmer sowing his corn",
"horse and the hound and the horn",
]



repeate_lines = [

	"lay in",
	"ate",
	"killed",
	"worried",
	"tossed",
	"milked",
	"kissed",
	"married",
	"woke",
	"kept",
	"belonged to",
]


def print_verse(current_line, lines, output):

    
	output.append("This is the " + subjects[current_line])
	for  index, line in enumerate(reversed(lines[0:current_line])):
         output.append(f"that {repeate_lines[current_line-index-1]} the {subjects[current_line-index-1]}")

	 


def recite(start_verse, end_verse):
    rhyme  = []
    
    lines = list(reversed(subjects[0:start_verse]))
    for index in range(start_verse-1,end_verse):
      subject =subjects[index]
      
      lines.insert(0,subject)
      verse = []  
      print_verse(index,lines,verse)
      rhyme.append(" ".join(verse))  
    return rhyme 

