from utils.database import get_pgsql_cursor, pgsql_commit
from utils.logger import get_logger


class product:
    def __init__(self):
        pass


    def get_all(self, page_start, page_limit):
        cursor = get_pgsql_cursor()
        query = """ SELECT * FROM products WHERE active = true \
            ORDER BY created_date DESC LIMIT {} OFFSET {} """.format(page_limit, page_start)
        cursor.execute()
        return cursor.fetchall()


    def get_for_category(self, category):
        cursor = get_pgsql_cursor()
        query = """ SELECT * FROM products WHERE category = {} AND active = true \
            ORDER BY created_date DESC """.format(category)
        cursor.execute()
        return cursor.fetchall()


    def get_for_seller(self, username):
        cursor = get_pgsql_cursor()
        query = """ SELECT * FROM products WHERE seller = {} AND active = true \
            ORDER BY created_date DESC """.format(username)
        cursor.execute()
        return cursor.fetchall()


    def insert_product(self, product):
        cursor = get_pgsql_cursor()