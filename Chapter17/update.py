import sqlite3
from Chapter17.select import select_one_book

# 데이터 수정용 함수
def update_books() :
    conn = sqlite3.connect('my_books.db')
    cur = conn.cursor()

    # 데이터 수정 SQL
    update_sql = 'UPDATE my_books SET recommendation = ? WHERE title = ?'

    # 수정 SQL 실행
    cur.execute(update_sql, (1, '개발자의 코드'))

    conn.commit()
    conn.close()

if __name__ == "__main__" :
    select_one_book()
    update_books()
    print('[데이터 수정 완료] ===========================')
    select_one_book()

