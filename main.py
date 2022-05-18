from dataclasses import dataclass,asdict
import csv
import sqlite3


@dataclass
class User:
    id:int
    name:str
    age:int

# User = typing.NamedTuple("User",[("id","int"),("name","str"),("age","int")])


class ControllerCsv:
    def write_to_csv(self,data:User)-> None:
        """
        param: data: data from user

        return:
        
        """
        try:
            user_data = asdict(data)
            with open('user.csv','a+',newline='') as f:
                header = ['id','name','age']
                writer = csv.DictWriter(f, fieldnames=header)
                writer.writerow(user_data)
            
        except IOError as e:
            print(e)


    def query_csv(self, obj_id:int):
        """
        param: obj_id: id value to query with

        return: record matching id value
        
        """
        try:
            with open('test.csv', newline='') as f:
                reader = csv.DictReader(f)
                for record in reader:
                    if str(obj_id) == record['id']:
                        return print(record)
                return print(f"Record with id {obj_id} does not exist")
        except IOError as e:
            print(e)

    
class ControllerSqlite:
    
    def save_to_db(self,data:User)-> None:
        """
        param: data: data from user
        return:
        """
        db_data = asdict(data)
        try:
            
            conn = sqlite3.connect('user.db')
            cur = conn.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS users (
                id integer,
                name text,
                age integer
            )""")
            
            cur.execute("INSERT INTO users VALUES ('{}','{}','{}')".format(db_data['id'],db_data['name'],db_data['age']))
            conn.commit()
            conn.close()

        except:
            print("Error has occurred")
        
    
    def query_db(self, obj_id:int):
        """
        param: obj_id
        
        """
        
        try:
            conn = sqlite3.connect('user.db')
            cur = conn.cursor()
            results = cur.execute("SELECT * FROM users WHERE id=?", (obj_id,)).fetchall()
            if results:
                for result in results:
                    return print(result)
            else:
                return print(f"Record with id {obj_id} not found")
            
        except sqlite3.Error as e:
            print(e)



def main():
    #test data sets
    csv_data_set = [
        User(1,'Alexis',25),
        User(2,'Alice',35),
        User(3,'Alicia',45)
    ]
    csv_query_set = [4,5,2]
    db_data_set = [
        User(5,'Alexis',25),
        User(6,'Alice',35),
        User(7,'Alicia',45)
    ]
    db_query_set = [1,2,7]
    
    
    print("Commencing saving to csv process...")
    csv_obj = ControllerCsv()
    for data in csv_data_set:
        csv_obj.write_to_csv(data)
    
    print("Saving to csv...")
    print("Saved to csv file \n")
    for data in csv_query_set:
        print(f"To find out if record of id {data} exists: ")
        csv_obj.query_csv(data)
    # print(f"To find out if record of id {csv_query_data2} exists: ")
    # csv_obj.query_csv(csv_query_data2)
    print("CSV process complete!")
    print("===================================================")


    print("Commencing saving to sqlite database...")
    db_obj = ControllerSqlite()
    for data in db_data_set:
        db_obj.save_to_db(data)
    
    print("Saving to db...")
    print("Successfully saved to db \n")
    for data in db_query_set:
        print(f"To find out if record of id {data} exists: ")
        db_obj.query_db(data)
    print("DB process complete!")
    print("==================================================")


    
if __name__ == '__main__':
    main()





