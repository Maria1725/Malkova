# TODO Найдите количество книг, которое можно разместить на дискете
Inf_volume = 1.44
Number_of_pages = 100
Number_of_lines_page = 50
Number_of_symbols_line = 25
one_symbol = 4
Total_number_symbols = Number_of_pages * Number_of_lines_page * Number_of_symbols_line
Volume_of_book = Total_number_symbols * one_symbol / 1024 / 1024
Number_of_books = round(Inf_volume // Volume_of_book)
print("Количество книг, помещающихся на дискету:", Number_of_books)
