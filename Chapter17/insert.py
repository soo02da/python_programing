import sqlite3

def insert_books() :
    conn = sqlite3.connect('my_books.db')
    cur = conn.cursor()

    insert_sql = 'INSERT INTO my_books VALUES (?, ?, ?, ?, ?)'

    cur.execute(insert_sql, ('개발자의 코드', '2013.02.28', 'A', 200, 0))
    cur.execute(insert_sql, ('클린 코드', '2010.03.04', 'B', 584, 1))

    # 책의 정보를 담고 있는 튜플들의 리스트
    books = [
        ('빅데이터 마케팅', '2014.07.02', 'A', 296, 1),
        ('구글드', '2010.02.10', 'B', 526, 0),
        ('강의력', '2013.12.12', 'A', 248, 1)
    ]

    # 여러 데이터 입력
    cur.executemany(insert_sql, books)

    conn.commit()
    conn.close()

if __name__ == "__main__" :
    insert_books()
