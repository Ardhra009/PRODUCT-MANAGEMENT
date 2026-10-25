from mysql import connector

class Product_connect:
    def get_connected(self):
        try:
            self.connection=connector.connect(
               host="localhost",
               user="root",
               password="Ardhra@17",
               database="shop_db"
            )
            return self.connection
        except Exception as e:
            return None
class ProductManager(Product_connect):
    def get(self):
        try:
            self.connect=super().get_connected()
            self.cursor=self.connect.cursor()
            query="select * from product"
            record=self.cursor.fetchall()
            print(record)
        except Exception as e:
            print(e)
    def get_object(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from product where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            return record
        except Exception as e:
            return None
    def retrieve(self,id=None):
        try:
            self.connect=super().get_connected()
            self.cursor=self.connect.cursor()
            query="select * from product where id =%s"
            values=(id,)
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            print(record)
        except Exception as e:
            print(e)
    def post(self,**kwargs):
        try:
            self.connect = super().get_connected()
            self.cursor = self.connect.cursor()
            query = "insert into product(name,category ,price,quantity,manufacturer) values(%s,%s,%s,%s,%s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connect.commit()
            print("product added successfully")

        except Exception as e:
            print(e)

    def put(self,id=None,**kwargs):
        try:
            record=self.get_object(id=id)
            if record!=None:
               self.cursor= self.connection.cursor()
               placeholder=""
               for k in kwargs.keys():
                   placeholder +=k + "=%s, "
                   placeholder=placeholder.rstrip(", ")
                   query=f"update product SET {placeholder} where id=%s"
                   values=[v for v in kwargs.values()]
                   values.append(id)
                   self.cursor.execute(query, values)
                   self.connection.commit()
               print("product updated successfully")
            else:
                print("product not found")
        except Exception as e:
            print(e)
    def delete(self,id=None):
        try:
            query = "select * from product where id=%s"
            values = (id,)
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            if record != None:
                query = "delete from product where id=%s"
                self.cursor.execute(query, values)
                self.connection.commit()
                print("product deleted successfully....!")
            else:
                print("product not found")
        except Exception as e:
            print(e)

obj=ProductManager()
obj.get()
# obj.post(name="meera",category="solid",price=500.5,quantity=8,manufacturer="delhi")
# obj.post(name="kiran",category="liquid",price=550.5,quantity=9,manufacturer="kolkata")
obj.retrieve(id=2)
# obj.put(id=2,price=800.5)
obj.delete(id=1)
obj.post(name="anula",category="liquid",price=700.5,quantity=8,manufacturer="kochi")
obj.post(name="sera",category="solid",price=420.5,quantity=10,manufacturer="pune")



