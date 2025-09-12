# MANGO GARDEN PROGRAM

class Tree:
    def __init__(self, code, height, width, amt):
        self.__code = code
        self.__height = height
        self.__width = width
        self.__amount = amt

    def set_code(self, code):       # setter methods
        self.__code = code
    def get_code(self):       # getter methods
        return self.__code
    
    def set_height(self, height):
        self.__height = height
    def get_height(self):
        return self.__height
    
    def set_width(self, width):
        self.__width = width
    def get_width(self):
        return self.__width
    
    def set_amount(self, amt):
        self.__amount = amt
    def get_amount(self):
        return self.__amount
    
    def annual_update(self, htt, wdd, amtt):
        self.__height += htt
        self.__width += wdd
        self.__amount += amtt

    def display_tree(self):
        print(f"Tree Code: {self.get_code()}, Height: {self.get_height()}, Width: {self.get_width()}, Amount spent: {self.get_amount()}...")

tree1 = Tree("Tree001", 12, 5, 10000)
tree1.display_tree()
tree1.annual_update(4, 1, 5000)
tree1.display_tree()



class MangoTree(Tree):
    def __init__(self, code, height, width, amt, yld):
        self.__yield = yld
        super(MangoTree, self).__init__(code, height, width, amt)

    def set_yield(self, yld):
        self.__yield = yld

    def get_yield(self):
        return self.__yield
    
    def annual_update(self, htt, wdd, amtt, yldd):
        super(MangoTree, self).annual_update(htt, wdd, amtt)
        self.__yield += yldd

    def display_mangotree(self):
        super(MangoTree, self).display_tree()
        print(f"And Yield: {self.get_yield()}...")

mango1 = MangoTree("Mango101", 12, 5, 20000, 5500)
mango1.display_mangotree()
mango1.annual_update(4, 1, 5000, 1500)
mango1.display_mangotree()



class Garden:
    def __init__(self, m1, m2, m3, t1, t2):
        self.__mango1 = m1
        self.__mango2 = m2
        self.__mango3 = m3
        self.__tree1 = t1
        self.__tree2 = t2

    def total_yield(self):
        return self.__mango1.get_yield() + self.__mango2.get_yield() + self.__mango3.get_yield()
    
    def total_amount_spent(self):
        return self.__mango1.get_amount() + self.__mango2.get_amount() + self.__mango3.get_amount() + self.__tree1.get_amount() + self.__tree2.get_amount()
    
    def display_garden(self):
        print("Please find garden tree details:")
        self.__mango1.display_mangotree()
        self.__mango2.display_mangotree()
        self.__mango3.display_mangotree()
        self.__tree1.display_tree()
        self.__tree2.display_tree()

grd = Garden(MangoTree("Himsagar", 12, 5, 20000, 5500),
            MangoTree("Mangaluru", 12.5, 5, 10000, 3500), 
            MangoTree("Mangalore", 11.5, 5.5, 21000, 4400), 
            Tree("Tree001", 12, 5.5, 15000), 
            Tree("Tree002", 12, 4.5, 20000))

print(f"Total Yield: {grd.total_yield()}...")
print(f"Total Amount Spent: {grd.total_amount_spent()}...")
grd.display_garden()