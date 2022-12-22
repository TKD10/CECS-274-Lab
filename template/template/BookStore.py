import Book
import ArrayList
import ArrayQueue
import RandomQueue
import DLList
import SLLQueue
import ChainedHashTable
import BinarySearchTree 
import BinaryHeap 
import AdjacencyList 
import time
import MaxQueue
import algorithms as alg



class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''
    def __init__(self) :
        self.bookCatalog = None
        self.shoppingCart = MaxQueue.MaxQueue()
        self.bookIndices = ChainedHashTable.ChainedHashTable()
        self.sortedTitleIndices = BinarySearchTree.BinarySearchTree()

    def loadCatalog(self, fileName : str) :
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
        self.bookCatalog = ArrayList.ArrayList()
        with open(fileName, encoding="utf8") as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                s = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(s)
                self.bookIndices.add(key, self.bookCatalog.size() - 1)
                self.sortedTitleIndices.add(title, self.bookCatalog.size() - 1)
            # The following line is used to calculate the total time 
            # of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")

        
    def setRandomShoppingCart(self) :
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = RandomQueue.RandomQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting randomShoppingCart in {elapsed_time} seconds")
    
    def setShoppingCart(self) :
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = ArrayQueue.ArrayQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")


    def removeFromCatalog(self, i : int) :
        '''
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input: 
            i: positive integer    
        '''
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time 
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")

    def addBookByIndex(self, i : int) :
        '''
        addBookByIndex: Inserts into the playlist the song of the list at index i 
        input: 
            i: positive integer    
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

    def addBookByKey(self, key):
        # determine if key is inside ChainHashTable
        # if inside ChainedHashTable then get the index
        # get the book for adding shopping cart
        # put book inside shopping cart
        # print the title
        # if not inside print did not find
        start_time = time.time()
        a = self.bookIndicies.find(key)
        if a == None:
            print("Book not Found")
        else:
            elbook = self.bookCatalog.get(a)
            self.shoppingCart.add(elbook)
            elapsed_time = time.time() - start_time
            print(f"Added title: {elbook} Completed in {elapsed_time} seconds")



    def searchBookByInfix(self, infix : str) :
        '''
        searchBookByInfix: Search all the books that contains infix
        input: 
            infix: A string, substring
        '''
        start_time = time.time()
        # todo
        # we only print a max of 50 books
        # ""
        matches = 0
        n = self.bookCatalog.size()
        for i in range(n):
            book = self.bookCatalog.get(i)
            if infix in book.title:
                print("_"*25)
                print(book)
                print()
                matches += 1
            if matches == 50:
                break
        print(f"Infix Matches: {matches}")
            # remember the 'break' statement; search up what does break do in python
        elapsed_time = time.time() - start_time
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")

    def removeFromShoppingCart(self) :
        '''
        removeFromShoppingCart: remove one book from the shoppung cart  
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")

    def getCartBestSeller(self):
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            best_seller = self.shoppingCart.max().title
            elapsed_time = time.time() - start_time
            print(f"getCartBestSeller return \n{best_seller} \nCompleted in {elapsed_time} seconds")

    def addBookByPrefix(self, prefix: str):
        start_time = time.time()
        if len(prefix) == 0:
            print("Book not found")
            return False
        else:
            dabook = self.sortedTitleIndices.find(prefix)
            if dabook is not None:
                book = self.bookCatalog.get(dabook.v)
                self.shoppingCart.add(book)
                elapsed_time = time.time() - start_time
                print(f"Added first matched title: {book.title} \nCompleted in {elapsed_time} seconds")
                return True
            else:
                print("Book not found")
                return False

    def bestsellers_with(self, infix, structure, n = 0):
        bestsellers = None
        if structure == 1:
            bestsellers = BinarySearchTree.BinarySearchTree()
        elif structure == 2:
            bestsellers = BinaryHeap.BinaryHeap()
        else:
            print("Invalid Data Structure")

        if bestsellers is not None:
            if infix == '':
                print("invalid infix")
            else:
                start_time = time.time()

                iteration = 0
                for i in range(self.bookCatalog.size()):
                    book = self.bookCatalog.get(i)
                    if infix in book.title:
                        if structure == 1:
                            bestsellers.add(book.rank, book)
                        else:
                            book.rank = -1 * book.rank
                            bestsellers.add(book)
                    iteration += 1
                    if iteration == n:
                        break
                if structure == 1:
                    books = reversed(bestsellers.in_order())
                    for book in books:
                        print(book.v)
                        print()
                else:
                    while bestsellers.size() > 0:
                        book = bestsellers.remove()
                        book.rank = -1 * book.rank
                        print(book)
                elapsed_time = time.time() - start_time
                print(f"Displayed bestsellers_with({infix}, {structure},{n}) in {elapsed_time} seconds")

    def display_catalog(self, n):
        if n <= self.bookCatalog.size():
            for i in range(n):
                print(self.bookCatalog.get(i))

    def sort_catalog(self, s):
        start_time = time.time()
        if s == 1:
            alg.merge_sort(self.bookCatalog)
        elif s == 2:
            alg.quick_sort(self.bookCatalog, False)
        elif s == 3:
            alg.quick_sort(self.bookCatalog)
        elapsed_time = time.time() - start_time
        print(f"Sorted {self.bookCatalog.size()} books in {elapsed_time} seconds.")

    def search_by_prefix(self, prefix, algo):
        catalog_copy = ArrayList.ArrayList()
        for i in range(self.bookCatalog.size()):
            catalog_copy.append(self.bookCatalog.get(i))
        n = 0
        start_time = time.time()
        if algo == 1:
            func = alg.linear_search
        else:
            func = alg.binary_search
            alg.quick_sort(catalog_copy)

        if algo == 1 or algo == 2:
            prefix_book = Book.Book("PREFIX DUMMY", prefix, "PREFIX DUMMY", "0", "PREFIX DUMMY")
            index = func(catalog_copy, prefix_book)
            while index != -100:
                found_book = catalog_copy.get(index)
                if prefix.lower() in prefix_book.title[0:len(prefix)].lower():
                    print(found_book, "\n")
                    n += 1
                catalog_copy.remove(index)
                prefix_book = Book.Book("PREFIX DUMMY", prefix, "PREFIX DUMMY", "0", "PREFIX DUMMY")
                index = func(catalog_copy, prefix_book)
        else:
            print("Invalid Algorithm")
        elapsed_time = time.time() - start_time
        print(f"Found {n} books with prefix {prefix} in {elapsed_time} seconds.")

