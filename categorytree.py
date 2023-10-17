class CategoryTree():
    root_category = []
    children_category = {}
    child_list = []
    def __init__(self):
        pass

    def add_category(self, category, parent):
        
        if parent is None:
            self.root_category.append(category)
            print(self.root_category)
        elif parent in self.root_category:
            self.child_list.append(category)
            self.children_category[parent] = self.child_list
            print(self.children_category)
        else:
            raise KeyError        

    def get_children(self, parent):
        if parent in self.root_category:
            return self.children_category[parent]

if __name__ == "__main__":
    c = CategoryTree()
    c.add_category('A',None)
    c.add_category('B','A')
    c.add_category('C','A')
    print(','.join(c.get_children('A')))
