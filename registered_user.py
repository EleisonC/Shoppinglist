class registered_user(object):
    def __init__(self,password,username):
        self.password = password
        self.username = username
    def log_in(self,username,password):
        if self.username == username and self.password == password:
            return  "Logged In"
        else:
            return "Clarify Your Data"

class user(registered_user):
    def __init__(self, shop_list={},items = []):
        self.shop_list = shop_list
        self.items = items

    def create_shopping_list(self, name_of_list=" ", items=[]):
        self.shop_list[name_of_list] = items
        return self.shop_list

    def delete_shopping_list(self, name_of_list):
        if name_of_list not in self.shop_list:
            return
        else:
            del self.shop_list[name_of_list]

    def update_shopping_list(self, name_of_list="", items=[], item=""):
        if name_of_list in self.shop_list:
            items.append(item)
        else:
            return

    def view_shopping_list(self, name_of_list):
        if name_of_list in self.shop_list:
            return self.shop_list[name_of_list]
        else:
            return


class shopping_list(user):
    def __init__(self,items= [],item = ""):
        self.item = "item"
        self.items = list(items)
        
    def add_item(self,item):
        self.items.append(item)
    def remove_item(self,item):
        if item in self.items:
            self.items.remove(item)

