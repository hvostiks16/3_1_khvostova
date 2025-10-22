import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoProject.settings')
django.setup()

from main.unit_of_work import UnitOfWork

def test_parent(uow):
    print("Всі батьки:")
    for parent in uow.parents.get_all():
        print(f"ID: {parent.idParent} | {parent.name} {parent.surname}")

    print("\nДодаємо нового батька:")
    new_parent = uow.parents.add({
        'name': 'Лілія',
        'surname': 'Сорока',
        'patronymic': 'Олєгівна',
        'phone_number': '0952525252',
        'email': 'semsor52@example.com'
    })
    if new_parent:
        print(f"Додано: ID {new_parent.idParent} | {new_parent.name} {new_parent.surname}")

    print("\nПошук по ID:")
    found = uow.parents.get_by_id(1)
    if found:
        print(f"Знайдено: {found.name} {found.surname} | Телефон: {found.phone_number}")
    else:
        print("Не знайдено")

def test_student(uow):
    print("Всі учні:")
    for student in uow.students.get_all():
        print(f"ID: {student.idStudent} | {student.name} {student.surname}")

    print("\nУчень по ID:")
    student = uow.students.get_by_id(2)
    if student:
        print(f"Знайдено: {student.name} {student.surname} | Email: {student.email}")
    else:
        print("Не знайдено")

def test_book(uow):
    print("Всі книги:")
    for book in uow.books.get_all():
        print(f"ID: {book.idBook} | {book.name} — {book.author}")

    print("\nДодаємо нову книгу:")
    new_book = uow.books.add({
        'name': 'Kazka',
        'author': 'Sh. Pero',
        'date_of_publication': '2005-05-08',
        'status': 'Lost'
    })
    if new_book:
        print(f"Додано: ID {new_book.idBook} | {new_book.name}")

    print("\nПошук книги по ID:")
    found = uow.books.get_by_id(1)
    if found:
        print(f"Знайдено: {found.name} — {found.author} | Статус: {found.status}")
    else:
        print("Не знайдено")

    print("\nДоступні книги: ")
    available_books = uow.books.get_by_status('Available')
    for book in available_books:
        print(book.idBook, book.name, book.author)


if __name__ == "__main__":
    uow = UnitOfWork()
    test_parent(uow)
    print("\n" + "="*50 + "\n")
    test_student(uow)
    print("\n" + "="*50 + "\n")
    test_book(uow)
    print("\n" + "=" * 50 + "\n")
