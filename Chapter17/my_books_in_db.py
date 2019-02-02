import sqlite3

def create_table() :
    conn = sqlite3.connect('my_books.db')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE my_books (
                    title text,
                    published_date text,
                    publisher text,
                    pages integer,
                    recommendation integer    
                )'''
    )

    conn.commit()
    conn.close()

if __name__ == "__main__" :
    create_table()


