import sqlite3

# 전체 조회용 함수
def select_all_books():
    conn = sqlite3.connect('my_books.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM my_books')   # 조회용 SQL 실행

    print('[1] 전체 데이터 출력하기')

    books = cur.fetchall()
    for book in books :
        print(book)

    conn.close()

# 일부 조회용 함수
def select_some_books(number) :
    conn = sqlite3.connect('my_books.db')
    cur = conn.cursor()

    cur.execute('SELECT * FROM my_books')

    print('[2] 데이터 일부 출력하기')
    books = cur.fetchmany(number)

    for book in books :
        print(book)

    conn.close()

# 1개 조회용 함수
def select_one_book() :
    conn = sqlite3.connect('my_books.db')
    cur = conn.cursor()

    cur.execute('SELECT * FROM my_books')
    print(cur.fetchone())

    conn.close()

# 쪽수가 많은 책 조회용 함수
def find_big_books() :
    conn = sqlite3.connect('my_books.db')
    cur = conn.cursor()

    cur.execute('SELECT title, pages FROM my_books WHERE pages > 300')

    print('[4] 페이지가 많은 책 출력하기')
    books = cur.fetchall()

    for book in books :
        print(book)

    conn.close()

if __name__ == "__main__" :
    select_all_books()
    print('=============================================================')

    select_some_books(3)
    print('=============================================================')

    select_one_book()
    print('=============================================================')

    find_big_books()
    print('=============================================================')