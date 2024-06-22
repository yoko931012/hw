library = {}
def add_book():

    # add books to the library dict
	book = input('\nEnter the title, genre, and price of the book(separated by 1): ').split('|')
	title = book[0]
	library[title] = (book[1], float(book[2]))
	print('\nAdded %s to the library.\n'%(title))
	print('%s, (%s, $%.2f)\n'%(title, library[title][0], library[title][1]))

def remove_book():
    # your code here
	r_book = input('\nEnter the title of a book to remove: ')
	# delete book and return True
	if r_book not in library.keys():
		print('Error: %s not found in the library'%(r_book))
	else:
		print('\nRemove %s from the library.\n'%(r_book))
		del library[r_book]
		return True

def get_book_info():
    # your code here
	info_book = input('Enter the title of a book: ')
		# print the information
	if info_book not in library:
		print('\n%s not found in the library.\n'%(info_book))
	else:
		print('\nTitle: ', info_book)
		print('Genre: ', library[info_book][0])
		print('Price: %.1f\n'%(library[info_book][1]))

def list_books():
	if library =={}:
		print('\nThe library is empty\n')
		return False
	for title, (genre, price) in sorted(library.items()):
		print('%s (%s, $%.2f)'%(title, genre, price))
	print()
	return True

def list_books_by_genre():
	gen_book = input('Enter the genre to search for: \n')

    # genre list->為了檢察我想要找的genre是否存在在Library裡面，所以我才要設置一個list去存放所有的種類
	genre_all_kinds = []
	# store all genres
	for (gen, pri) in library.values():
		if gen not in genre_all_kinds:
			genre_all_kinds.append(gen)
	if gen_book not in genre_all_kinds:
		print('\nError: No books found in %s genre.\n'%(gen_book))
		# storing book of given genre
	else:
		genre_search = {} #要去存放我找的那個種類的所有書
        # print the specific genre books
		for title, (gen, pri) in library.items():
			if gen == gen_book:
				genre_search[title] = (gen, pri)
		#print
		for title, (gen, pri) in sorted(genre_search.items()):
			print('%s %s ($%.2f)'%(title, gen, pri))
		print()
while True:
	print('Menu')
	opt_1 = '1. Add a book'
	opt_2 = '2. Remove a book'
	opt_3 = '3. Get book information'
	opt_4 = '4. List all books'
	opt_5 = '5. List books by genre'
	opt_6 = 'Quit'
	print(opt_1,'\n', opt_2, '\n', opt_3, '\n', opt_4, '\n', opt_5, '\n', sep = '')
	opt = int(input('Enter your choice: '))
	if opt == 1:
		add_book_return = add_book()
		if add_book_return:
			list_books()
	elif opt == 2:
		remove_book_return = remove_book()
		if remove_book_return:
			list_books()
	elif opt == 3:
		get_book_info_return = get_book_info()
	elif opt == 4:
		list_books_return = list_books()
	elif opt == 5:
		list_books_by_genre_return = list_books_by_genre()
	elif opt == 6:
		break


