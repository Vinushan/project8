from utils.database import get_pgsql_cursor, pgsql_commit
from utils.logger import get_logger
from utils.image import compress


class product:
    def __init__(self):
        pass


    def get_for_city(self, city, offset=0, limit=20):
        cursor = get_pgsql_cursor()
        query = """ SELECT product_id, product_name, product_desc, category_name, updated_date,
            price, merchant_name, merchant_location, merchant_phone, product_image, product_condition
            FROM product WHERE city_id = '{}' AND active = true 
            ORDER BY updated_date DESC LIMIT {} OFFSET {} """.format(city, offset, limit)
        cursor.execute(query)
        product_list = list()
        for row in cursor.fetchall():
            product_dict = dict()
            product_dict["id"] = row["product_id"]
            product_dict["name"] = row["product_name"]
            product_dict["desc"] = row["product_desc"]
            product_dict["category"] = row["category_name"]
            product_dict["date"] = row["updated_date"]
            product_dict["merchant"] = row["merchant_name"]
            product_dict["location"] = row["merchant_location"]
            product_dict["phone"] = row["merchant_phone"]
            product_dict["image"] = row["product_image"]
            product_list.append(product_dict)
        return {'products':product_list}


    def get_for_city_category(self, city, category, offset=0, limit=20):
        cursor = get_pgsql_cursor()
        query = """ SELECT product_id, product_name, product_desc, category_name, updated_date,
            price, merchant_name, merchant_location, merchant_phone, product_image, product_condition 
            FROM product WHERE city_id = '{}' category_id = '{}' AND active = true 
            ORDER BY updated_date DESC LIMIT {} OFFSET {} """.format(city, category, offset, limit)
        cursor.execute(query)
        product_list = list()
        for row in cursor.fetchall():
            product_dict = dict()
            product_dict["id"] = row["product_id"]
            product_dict["name"] = row["product_name"]
            product_dict["desc"] = row["product_desc"]
            product_dict["category"] = row["category_name"]
            product_dict["date"] = row["updated_date"]
            product_dict["merchant"] = row["merchant_name"]
            product_dict["location"] = row["merchant_location"]
            product_dict["phone"] = row["merchant_phone"]
            product_dict["image"] = row["product_image"]
            product_list.append(product_dict)
        return {'products':product_list}


    def get_for_merchant(self, username, offset=0, limit=20):
        cursor = get_pgsql_cursor()
        query = """ SELECT product_id, product_name, product_desc, category_name, updated_date,
            price, merchant_name, merchant_location, merchant_phone, product_image, product_condition 
            FROM product WHERE username = '{}' AND active = true 
            ORDER BY updated_date DESC LIMIT {} OFFSET {} """.format(username, offset, limit)
        cursor.execute(query)
        product_list = list()
        for row in cursor.fetchall():
            product_dict = dict()
            product_dict["id"] = row["product_id"]
            product_dict["name"] = row["product_name"]
            product_dict["desc"] = row["product_desc"]
            product_dict["category"] = row["category_name"]
            product_dict["date"] = row["updated_date"]
            product_dict["merchant"] = row["merchant_name"]
            product_dict["location"] = row["merchant_location"]
            product_dict["phone"] = row["merchant_phone"]
            product_dict["image"] = row["product_image"]
            product_list.append(product_dict)
        return {'products':product_list}


    def insert_product(self, data, files):
        cursor = get_pgsql_cursor()
        params = (data.get("name"), data.get("desc"), data.get("city"), data.get("username"),
                  data.get("cat_id"), data.get("cat_name"), data.get("price"), data.get("status"),
                  data.get("seller"), data.get("location"), data.get("phone"), 
                  compress(files.get("image")), data.get("condition"))
        query = """ INSERT INTO  product (product_name, product_desc, city_id, username, 
            category_id, category_name, price, active, merchant_name, merchant_location,
            merchant_phone, product_image, product_condition) VALUES 
            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """
        cursor.execute(query, params)
        if cursor.rowcount:
            pgsql_commit()
            response = {'text':'Hola!! Your product is ready for display',
                        'status_code':201}
        else:
            response = {'text':'Oops!! Something went wrong, try again',
                        'status_code':500}            
        return response