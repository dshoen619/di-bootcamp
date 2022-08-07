import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'davidshoen1'
DATABASE = 'w6d5_menu'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, dbname=DATABASE )
cursor = connection.cursor()


class MenuItem:

    def __init__(self, item_name, price):
        self.item_name=item_name
        self.price=price

    def save(self):

        self.query=f"Insert into menu (item_name, cost) Values{self.item_name,self.price}"
        cursor.execute(self.query)
        connection.commit()

    def delete(self):
        self.query = f"DELETE FROM menu WHERE item_name='{self.item_name}'"
        cursor.execute(self.query)
        connection.commit()


    def update(self, item_to_change):
        self.item_to_change=item_to_change
        self.query = f"UPDATE menu SET item_name = '{self.item_name}', cost={self.price} WHERE item_name='{self.item_to_change}'"
        cursor.execute(self.query)
        connection.commit()

    def all(self):
        menu_list=[]
        query2 = "SELECT * FROM menu"
        cursor.execute(query2)
        results = cursor.fetchall()
        for item in results:
            menu_list.append(item)
        print(menu_list)

    def get_by_name(self,name_to_get):
        self.name_to_get=name_to_get
        self.query= f"SELECT * FROM menu where item_name='{name_to_get}'"
        cursor.execute(self.query)
        results=cursor.fetchall()
        if len(results)!=0:
            print(results)
        if len(results)==0:
            print('None')




    
m1=MenuItem('soda',5)



# query2 = "SELECT * FROM menu LIMIT 20;"
# cursor.execute(query2)
# results = cursor.fetchall()
# for item in results:
#         print(item)


