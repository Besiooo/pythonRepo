from abc import ABC, abstractmethod;

class Library(ABC):
    capacity = 10;
    __address = "Bookey Av. 66, Woodlands CO";
    __books = [];

    def __init__(self):
        self.Name = "Prince Yoel's Royal Library";

    def addBook(self):
        title = input("Title: ");
        author = input("Author: ");
        genre = input("Genre: ");
        year = input("Year: ");

        newBook = Book(title, author, genre, year);
        self.__books.append(newBook);

    def showBooks(self):
        j = 0;
        for i in self.__books:
            print(str(j+1) + ' |');
            print(i);
            j += 1;

    def deleteBook(self):
        self.showBooks();
        i = input("Which one? --> ");
        del self.__books[int(i) - 1]; #interface counts 1...n whereas compiler on 0...n-1


class Book(Library):
    def __init__(self, title, author, genre, year):
        self.Title = title;
        self.Author = author;
        self.Genre = genre;
        self.Year = year;

    def __str__(self):
        info = "'" + self.Title + "' by " + self.Author + ", a " + self.Genre + " written in " + self.Year + "\n";
        return info;




