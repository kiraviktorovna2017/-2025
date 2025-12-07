# TODO Найдите количество книг, которое можно разместить на дискете
V_disket=1.44
total_page=100
number_strip=50
number_symbol=25
sumbol=4
s=total_page*number_strip*number_symbol*sumbol
number_V=V_disket*1024*1024
number_book=int(number_V // s)
print("Количество книг, помещающихся на дискету:", number_book)
