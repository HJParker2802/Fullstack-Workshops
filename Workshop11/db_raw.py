import MySQLdb

def get_connection():
    conn=MySQLdb.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        passwd="SEPS",
        db="bookstore",
        charset="utf8mb4"
        )
    return conn


def test_connection(): 
    conn = get_connection()
    cursor = conn.cursor() 
    cursor.execute("SELECT COUNT(*) FROM books;") 
    (count,) = cursor.fetchone()
    cursor.close() 
    conn.close() 
    return count

def fetch_all_books(): 
    conn = get_connection() 
    cursor = conn.cursor() 
    query = "SELECT id, title, author, year_published, publisher FROM books;" 
    cursor.execute(query) 
    rows = cursor.fetchall() 
    cursor.close()
    conn.close()
    return rows

def fetch_book_by_id(book_id: int): 
    conn = get_connection() 
    cursor = conn.cursor()
    query = """ SELECT id, title, author, year_published, publisher FROM books WHERE id = %s; """ 
    cursor.execute(query, (book_id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return row

def create_book_in_db(title: str, author: str, year_published=None, publisher=None): 
    conn = get_connection() 
    cursor = conn.cursor()
    query = """ INSERT INTO books (title, author, year_published, publisher) VALUES (%s, %s, %s, %s); """ 
    cursor.execute(query, (title, author, year_published, publisher))
    conn.commit()
    new_id = cursor.lastrowid 
    cursor.close()
    conn.close()
    return new_id


def update_book_in_db(book_id: int, title: str, author: str, year_published=None, publisher=None): 
    conn = get_connection()
    cursor = conn.cursor()
    query = """ 
        UPDATE books 
        SET title = %s, 
            author = %s,
            year_published = %s,
            publisher = %s 
        WHERE id = %s; 
    """ 
    cursor.execute(query, (title, author, year_published, publisher, book_id))
    conn.commit()
    rows_affected = cursor.rowcount 
    cursor.close()
    conn.close()
    return rows_affected


def delete_book_from_db(book_id: int): 
    conn = get_connection() 
    cursor = conn.cursor()
    query = "DELETE FROM books WHERE id = %s;"
    cursor.execute(query, (book_id,)) 
    conn.commit()
    rows_affected = cursor.rowcount 
    cursor.close()
    conn.close()
    return rows_affected