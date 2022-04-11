#Julia Salerno, Jenna Esposito
#CS-175L
#bestsellers.py

def main():

    
    books = get_booklist()

    response = ''
    
    while response.upper() != "Q":
        response = menu()
        if response == '1':
            year_range(books)
        elif response =='2':
            search_month(books)
        elif response == '3':
            author(books)
        elif response == '4':
            title(books)
        else:
            print("I do not understand this command")
            response = menu()
    print("Done")
def get_booklist():
    
    file = open('bestsellers.txt', 'r')
    title = []
    author= []
    publisher = []
    pubDate= []
    books= []
    numbooks = 0
    for line in file:
        l = line.strip('\n')
        cols = l.split('\t')
        books.append(cols)
        numbooks= numbooks+1

    print(f"Read {numbooks} books")
    
    return books

def menu():
    
    menu_result = input("What would you like to do?\n\t1: Look up year range\n\t2:Look up month/year\n\t3:Search for author\n\t4:Search for title\n\tQ:Quit\n")
    
  
    return menu_result
    
def year_range(books):
    
    start = int(input("Enter start year: "))
    end = int(input("Enter end year: "))
    
    current_year = start
    year_diff = end - start
    
    for x in range(year_diff+ 1):

        for title in books:
            date = title[3].split('/')
            year = int(date[2])
            
            if int(current_year) == year:
                print( title[0], 'by: ',title[1], '(pub date: ', title[3], ')')
        current_year= current_year + 1

    
def search_month(books):
    input_month = int(input("Enter month (1-12): "))
    input_year = int(input("Enter  year: "))
    
    for title in books:
        date = title[3].split('/')
        month = int(date[0])
        year = int(date[2])
        if (input_month == month) and (input_year == year):
            print( title[0], 'by: ',title[1], '(pub date: ', title[3], ')')

def author(books):

    search_value = input("Enter search string: ")
    s = search_value.lower()
    
    print(search_value)
    for title in books:
        authors = title[1].lower()
        if authors.find(s)!= -1:
            print( title[0], 'by: ',title[1], '(pub date: ', title[3], ')')
        
    

def title(books):
    search_value = input("Enter search string: ")
    s = search_value.lower()
    
    print(search_value)
    for title in books:
        t = title[0].lower()
        if t.find(s)!= -1:
            print( title[0], 'by: ',title[1], '(pub date: ', title[3], ')')


main()
