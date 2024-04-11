import copy


class Node:
    def __init__(self) -> None:
        self.key = None
        self.left = None
        self.right = None
        self.tree = None
    
    def insert(self, value):
        subtree = copy.copy(self.tree)

        def ins(sub, value):
            if sub is None:
                sub = {'key': value,
                            'left': None, 
                            'right': None}
                print('sub none =', sub)
                return sub
            if value < sub.get('key'):
                # tr = tr.get('left')
                print('sub left =', sub)
                ins(value, sub.get('left'))
            else:
                # tr = self.tree.get('right')
                print('sub right =', sub)
                ins(value, sub.get('right'))
            # self.insert(value, tr)
            print('sub =', sub)
            return sub
        
        self.tree = ins(subtree, value)
        
    
    def left(self):
        self.tree = self.tree.get('left')
        # if not self.tree.values([0]):
        #     return None
        # else:
        #     return self.tree.values[0]
    
    def right(self):
        self.tree = self.tree.get('right')
    
    def key(self):
        return self.tree.get('key')
    
    def pr(self):
        print(self.tree.get('key'))
        print(self.tree.get('left'))
        print(self.tree.get('right'))


if __name__ == '__main__':
    tree = Node()
    tree.insert(9)
    #tree.insert(17)
    print(tree.key)
    #tree.pr()