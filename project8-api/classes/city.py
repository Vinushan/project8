from utils.database import get_pgsql_cursor

class city:

    def __init__(self):
        pass


    def get_all(self):
        cursor = get_pgsql_cursor()
        query = """ SELECT city_id, city_name, country FROM city """
        cursor.execute(query)
        city_list = list()
        for row in cursor.fetchall():
            city_obj = dict()
            city_obj["id"] = row["city_id"]
            city_obj["name"] = row["city_name"]
            city_list.append(city_obj)
        return {'city':city_list}