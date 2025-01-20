import csv

def read_from_csv(filename):
    """Read data from a csv file and print them on screen.

    The first line of the file consists of a number of headings.
    The second line and after consist of data under the headings.

    Parameters
    ----------
    filename : str
        the name of the file to be read
        
    Returns
    -------
    None
    
    Side effects
    ------------
    Print the headings/data in the csv file with
    - " || " between adjacent headings and
    - " | " between adjacent data.
    
    """
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # get the header row to print woth two lines
        header = next(csv_reader)
        print(" || ".join(header))
        
        # other remaining rows if the row is not empty
        for row in csv_reader:
            # if there's elements on that row
            if len(row) != 0: 
                print(" | ".join(row))
    return

read_from_csv("sample.csv")