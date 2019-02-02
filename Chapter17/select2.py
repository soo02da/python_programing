import sqlite3

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

if __name__ == '__main__' :
    select_some_books(3)
    print('===========================================================')
