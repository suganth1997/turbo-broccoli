
class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.dtype = 'f'

class ExpressionTree:
    def __init__(self, init_function = 'c'):
        self.root = TreeNode('c')
    
    def dfs(self, x):
        if x.dtype == 'f':
            return x.data
        
        return x.data + '(' + self.dfs(x.left) + ', ' + self.dfs(x.right) + ')'

    def getExpression(self):
        return self.dfs(self.root)
    
    def dfs_leaf(self, x, l):
        if x.dtype == 'f':
            l.append(x)
            return
        
        self.dfs_leaf(x.left, l)
        self.dfs_leaf(x.right, l)

        return

    def getLeafNodes(self):
        leaf_nodes = []
        self.dfs_leaf(self.root, leaf_nodes)
        return leaf_nodes