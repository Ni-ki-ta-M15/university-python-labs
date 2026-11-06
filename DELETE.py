# # class INF1:
# #     def __init__(self, udk_number, author, title):
# #         self.udk_number = udk_number
# #         self.author = author
# #         self.title = title
# #
# # class INF2:
# #     def __init__(self, book_count, book_price):
# #         self.book_count = book_count
# #         self.book_price = book_price
# #
# # class INFORMATION:
# #     def __init__(self, inf1, inf2):
# #         self.inf1 = inf1
# #         self.inf2 = inf2
# #
# # def input_data():
# #     data = []
# #     N = int(input("Введіть кількість елементів: "))
# #     for _ in range(N):
# #         udk_number = input("Введіть номер УДК: ")
# #         author = input("Введіть прізвище та ініціали автора: ")
# #         title = input("Введіть назву: ")
# #         book_count = int(input("Введіть кількість книг в бібліотеці: "))
# #         book_price = float(input("Введіть вартість книги: "))
# #         inf1 = INF1(udk_number, author, title)
# #         inf2 = INF2(book_count, book_price)
# #         information = INFORMATION(inf1, inf2)
# #         data.append(information)
# #     return data
# #
# # def sort_by_author(data):
# #     return sorted(data, key=lambda x: x.inf1.author)
# #
# # def sort_by_price(data):
# #     return sorted(data, key=lambda x: x.inf2.book_price)
# #
# # def max_books(data):
# #     return max(data, key=lambda x: x.inf2.book_count)
# #
# # def print_data(data):
# #     for information in data:
# #         print(f"Номер УДК: {information.inf1.udk_number}, Автор: {information.inf1.author}, Назва: {information.inf1.title}, Кількість книг: {information.inf2.book_count}, Вартість: {information.inf2.book_price}")
# #
# # data = input_data()
# # data = sort_by_author(data)
# # print("Дані, відсортовані за автором:")
# # print_data(data)
# # data = sort_by_price(data)
# # print("Дані, відсортовані за ціною:")
# # print_data(data)
# # max_books_info = max_books(data)
# # print("Максимальна кількість книг:")
# # print(f"Номер УДК: {max_books_info.inf1.udk_number}, Автор: {max_books_info.inf1.author}, Назва: {max_books_info.inf1.title}, Кількість книг: {max_books_info.inf2.book_count}, Вартість: {max_books_info.inf2.book_price}")
# #
# # body {
# #   font-family: 'Monotype Corsiva', Tahoma, Geneva, Verdana, sans-serif;
# #   display: flex;
# #   justify-content: center;
# #   align-items: center;
# #   height: 720px;
# #   margin: 0;
# #   background: #0FDB78;
# #   color: #004080;
# #   font-size:40px
# # }
# # #countdown {
# #   background: rgba(255, 0, 0, 0.2);
# #   padding: 40px 60px;
# #   border-radius: 15px;
# #   box-shadow: 0 30px 25px rgba(255, 0, 0, 0.3);
# #   text-align: center;
# # }
# #
# # #timer {
# #   font-size: 1.6em;
# #   letter-spacing: 3px;
# # }
# #
# # .timer-unit {
# #   font-size: 32px;
# #   text-transform: lowercase;
# #   letter-spacing: 3px;
# #   margin-top: 10px;
# #   display: block;
# # }
#
# # include <iostream>
# # include <string>
#
# # include <iostream>
# # include <string>
#
# # include <iostream>
# # include <string>
#
# class Worker {
# private:
#     std:
#
# :string
# surname;
# std::string
# position;
# double
# salary;
#
# public:
# // Конструктор
# без
# параметрів
# Worker(): surname(""), position(""), salary(0.0)
# {
#     std:: cout << "Викликано конструктор без параметрів" << std::endl;
# }
#
# // Конструктор
# з
# параметрами
# Worker(std::string
# s, std::string
# p, double
# sal): surname(s), position(p), salary(sal)
# {
#     std:: cout << "Викликано конструктор з параметрами: surname=" << surname << ", position=" << position << ", salary=" << salary << std::endl;
# if (surname.find("Іван") == 0)
# {
#     position = "інженер";
# std::cout << "Працівнику з прізвищем, що починається на 'Іван', присвоєно посаду 'інженер'" << std::endl;
# }
# salary += salary * 0.15;
# std::cout << "Зарплата збільшена на 15%, нова зарплата: " << salary << std::endl;
# }
#
# // Деструктор
# ~Worker()
# {
#     std:: cout << "Викликано деструктор для об'єкта з параметрами: surname=" << surname << ", position=" << position << ", salary=" << salary << std::endl;
# }
#
# // Геттери
# та
# сеттери
# std::string
# getSurname()
# {
# return surname;}
# void
# setSurname(std::string
# s) {surname = s;}
#
# std::string
# getPosition()
# {
# return position;}
# void
# setPosition(std::string
# p) {position = p;}
#
# double
# getSalary()
# {
# return salary;}
# void
# setSalary(double
# sal) {salary = sal;}
# };
#
# class ExtendedWorker: public
#
#
# Worker
# {
#     private:
#         int experienceYears; // Досвід
# роботи
# std::string
# education; // Освіта
# int
# rating; // Рейтинг(в
# 100 - бальній
# системі)
#
# public:
# ExtendedWorker(std::string
# s, std::string
# p, double
# sal, int
# expYrs, std::string
# edu, int
# rat)
# : Worker(s, p, sal), experienceYears(expYrs), education(edu), rating(rat)
# {
#     std:: cout << "Конструктор похідного класу" << std::endl;
# }
#
# void
# processData()
# {
# // Функція
# обробки
# даних
# if (rating >= 60 & & rating < 75)
# {
#     setSalary(getSalary() * 1.2); // Збільшити
# зарплату
# на
# 20 %
# } else if (rating >= 75 & & rating < 90) {
# setSalary(getSalary() * 1.4); // Збільшити зарплату на 40 %
# } else if (rating >= 90) {
# setSalary(getSalary() * 1.6); // Збільшити зарплату на 60 %
# }
# std::
#     cout << "Обробка даних..." << std::endl;
# }
#
# std::string
# getInfo()
# {
# return "Прiзвище: " + getSurname() + ", Посада: " + getPosition() +
# ", Зарплата: " + std::to_string(getSalary()) +
# ", Досвiд роботи: " + std::to_string(experienceYears) +
# ", Освiта: " + education +
# ", Рейтинг: " + std::to_string(rating);
# }
# };
#
# class Person{
# private:
#     std:
#
# :string
# name;
#
# public:
# Person(std::string
# n){
#     name = n;
# std::cout << "Конструктор для " << name << std::endl;
# }
# };
#
# int
# main()
# {
#     ExtendedWorker
# ew("Петров", "менеджер", 12000, 5, "Вища", 95);
# ew.processData();
# std::cout << ew.getInfo() << std::endl;
#
# Person
# person1("Іван");
#
# return 0;
# }
#

#include <iostream>
#include <string>

class Student {
protected:
    std::string name;
    std::string faculty;
    int course;
    int min_grade;
public:
    Student(std::string n, std::string f, int c, int g) : name(n), faculty(f), course(c), min_grade(g) {}
    virtual void NextCourse() {
        if (min_grade >= 3) course++;
    }
    virtual int Stipend() {
        if (min_grade <= 3) return 0;
        else if (min_grade == 4) return 200;
        else return 300;
    }
    std::string Info() {
        return "\n-------------------------\nСтудент: " + name + "\nФакультет: " + faculty + "\nКурс: " + std::to_string(course) + "\nМінімальна оцінка: " + std::to_string(min_grade) + "\nСтипендія: " + std::to_string(Stipend()) + " грн\n-------------------------\n";
    }
};

class ContractStudent : public Student {
private:
    bool paid;
public:
    ContractStudent(std::string n, std::string f, int c, int g, bool p) : Student(n, f, c, g), paid(p) {}
    void NextCourse() override {
        if (min_grade >= 3 && paid) course++;
    }
    int Stipend() override {
        return 0;
    }
};

int main() {
    Student s("Іванов Іван Іванович", "Факультет інформатики", 1, 4);
    Student s2("Малий Нікіта Михайлович", "Факультет кібербезпеки", 2, 5);
    ContractStudent cs1("Петров Петро Петрович", "Факультет математики", 2, 5, true);
    ContractStudent cs2("Сидоров Сидор Сидорович", "Факультет фізики", 3, 2, false);

    std::cout << s.Info();
    std::cout << s2.Info();
    std::cout << cs1.Info();
    std::cout << cs2.Info();

    s.NextCourse();
    s2.NextCourse();
    cs1.NextCourse();
    cs2.NextCourse();

    std::cout << "\nПісля переводу на наступний курс:\n";
    std::cout << s.Info();
    std::cout << s2.Info();
    std::cout << cs1.Info();
    std::cout << cs2.Info();

    return 0;
}


#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

struct Book {
    std::string title;
    std::string author;
    int pages;
    std::string genre;
};

struct Word {
    std::string word;
    std::vector<int> pageNumbers;
    Book* book; // Змінено на покажчик
};

std::vector<Word*> words; // Змінено на покажчик

bool compareWords(const Word* a, const Word* b) { // Змінено на покажчик
    return a->word < b->word; // Змінено на покажчик
}

void sortWords() {
    std::sort(words.begin(), words.end(), compareWords);
}

void addWord() {
    Word* newWord = new Word; // Змінено на покажчик
    newWord->book = new Book; // Змінено на покажчик
    std::cout << "Enter word: ";
    std::cin >> newWord->word;
    int pageNumber;
    std::cout << "Enter page number: ";
    std::cin >> pageNumber;
    newWord->pageNumbers.push_back(pageNumber);
    std::cout << "Enter book details\n";
    std::cout << "Title: ";
    std::cin >> newWord->book->title;
    std::cout << "Author: ";
    std::cin >> newWord->book->author;
    std::cout << "Pages: ";
    std::cin >> newWord->book->pages;
    std::cout << "Genre: ";
    std::cin >> newWord->book->genre;
    words.push_back(newWord);
}

void printWords() {
    for (const Word* word : words) { // Змінено на покажчик
        std::cout << "Word: " << word->word << "\n";
        std::cout << "Occurs on pages: ";
        for (int page : word->pageNumbers) {
            std::cout << page << " ";
        }
        std::cout << "\n";
        std::cout << "Book: " << word->book->title << ", " << word->book->author << ", " << word->book->pages << ", " << word->book->genre << "\n";
    }
}

void deleteWord() {
    std::string wordToDelete;
    std::cout << "Enter word to delete: ";
    std::cin >> wordToDelete;
    for (int i = 0; i < words.size(); i++) {
        if (words[i]->word == wordToDelete) { // Змінено на покажчик
            delete words[i]; // Видалення об'єкта
            words.erase(words.begin() + i);
            break;
        }
    }
}

void replaceWord() {
    std::string wordToReplace;
    std::cout << "Enter word to replace: ";
    std::cin >> wordToReplace;
    for (Word* word : words) { // Змінено на покажчик
        if (word->word == wordToReplace) {
            std::cout << "Enter new word: ";
            std::cin >> word->word;
            break;
        }
    }
}

void printFromIndex() {
    int index;
    std::cout << "Enter index to start printing from: ";
    std::cin >> index;
    for (int i = index; i < words.size(); i++) {
        std::cout << "Word: " << words[i]->word << "\n"; // Змінено на покажчик
        std::cout << "Occurs on pages: ";
        for (int page : words[i]->pageNumbers) { // Змінено на покажчик
            std::cout << page << " ";
        }
        std::cout << "\n";
        std::cout << "Book: " << words[i]->book->title << ", " << words[i]->book->author << ", " << words[i]->book->pages << ", " << words[i]->book->genre << "\n";
    }
}

void deleteArray() {
    for (Word* word : words) { // Змінено на покажчик
        delete word; // Видалення об'єкта
    }
    words.clear();
}

int main() {
    int choice;
    do {
        std::cout << "1. Add word\n";
        std::cout << "2. Print words\n";
        std::cout << "3. Delete word\n";
        std::cout << "4. Replace word\n";
        std::cout << "5. Print from index\n";
        std::cout << "6. Delete array\n";
        std::cout << "7. Sort words\n";
        std::cout << "8. Exit\n";
        std::cout << "Enter choice: ";
        std::cin >> choice;
        switch (choice) {
            case 1:
                addWord();
                break;
            case 2:
                printWords();
                break;
            case 3:
                deleteWord();
                break;
            case 4:
                replaceWord();
                break;
            case 5:
                printFromIndex();
                break;
            case 6:
                deleteArray();
                break;
            case 7:
                sortWords();
                break;
        }
    } while (choice != 8);
    return 0;
}