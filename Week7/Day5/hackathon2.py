import psycopg2


HOSTNAME = 'localhost'
USERNAME = 'davidshoen1'
DATABASE = 'hackathon2'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, dbname=DATABASE )
cursor = connection.cursor()


class Medication:

    def __init__ (self, items=None):
        self.l=items


    def find_medicine(self):
        symptom=input('What are your symptoms? Enter one word')
        self.query= f"SELECT * FROM drug_list where dragindication Like '%{symptom}%';"
        cursor.execute(self.query)
        results=cursor.fetchall()

        column_names = [desc[0] for desc in cursor.description]
        
        column_names_counter=0
        for i in results:
            column_names_counter=0
            for j in i:
                print(f"{column_names[column_names_counter]} : {j}")
                column_names_counter+=1
            print("")



Medication().find_medicine()