count_page = 100
count_str = 50
count_char = 25
book = count_str * count_char * count_page * 4
total = 1.44 * 1024 * 1024

count_books = round(total // book)

print("Количество книг, помещающихся на дискету:", count_books)
