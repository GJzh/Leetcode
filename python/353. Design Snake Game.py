class SnakeGame(object):
    '''
    move first and then check if the snake bites itself because the snake's head can move to its tail
    '''
    class Node():
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.next = None
            self.prev = None

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.head = self.tail = self.Node(0, 0)
        self.width = width
        self.height = height
        self.foodIdx = 0
        self.food = food
        self.score = 0
        self.directions = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}
        self.snake = {(0,0): True}
        
    def addHead(self, x, y):
        node = self.Node(x,y)
        node.next = self.head
        self.head.prev = node
        self.head = node
        
    def endToHead(self, x, y):
        self.tail.x = x
        self.tail.y = y
        if self.head == self.tail: return
        node = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node
        return
        

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        x = self.head.x + self.directions[direction][0]
        y = self.head.y + self.directions[direction][1]
        if x < 0 or x >= self.height or y < 0 or y >= self.width:
            return -1
        if self.foodIdx < len(self.food) and x == self.food[self.foodIdx][0] and y == self.food[self.foodIdx][1]:
            self.addHead(x, y)
            self.score += 1
            self.foodIdx += 1
        else:
            del self.snake[(self.tail.x, self.tail.y)]
            self.endToHead(x, y)
            if (x,y) in self.snake: return -1
        self.snake[(x,y)] = True
        return self.score