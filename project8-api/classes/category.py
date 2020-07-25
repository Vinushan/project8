from utils.database import get_pgsql_cursor

class category:

    def __init__(self):
        pass


    def get_category_by_city(self, city):
        cursor = get_pgsql_cursor()
        query = """ SELECT category_id, category_name FROM category 
            WHERE city_id = '{}' """.format(city)
        cursor.execute(query)
        category_list = list()
        for row in cursor.fetchall():
            category_obj = dict()
            category_obj["id"] = row["category_id"]
            category_obj["name"] = row["category_name"]
            category_list.append(category_obj)
        return {'category':category_list}