class Trees:
    """ Trees: a class representing a grid of trees. 
    
    This class does everything for the AoC puzzle.
    """
    def __init__(self, filename:str):
        self.trees = []
        self.load(filename)
    
    def load(self, filename:str):
        with open(filename) as input_file:
            line = input_file.readline()
            self.trees = [int(x) for x in line if x != '\n']
            self.width = len(self.trees)
            for line in input_file:
                self.trees += [int(x) for x in line if x != '\n']
            self.height = len(self.trees) // self.width


    def __str__(self):
        return f"""{self.width}\n{self.height}\n{self.trees}"""

    def _to_index(self, x:int, y:int):
        """Trees are stored in a linear list, so this converts a coordinate to an index"""
        return y * self.width + x

    def _get(self, x:int, y:int):
        return self.trees[self._to_index(x, y)]

    def _num_edge_trees(self):
        return self.width * 2 + (self.height - 2) * 2

    def _is_blocked(self, x1, y1, x2, y2):
        return self._get(x1, y1) <= self._get(x2, y2)

    def _is_visible_from_outside(self, x, y):
        """ Checks whether a tree is visible from the outside.
        
        If a tree is blocked, decrement a counter. If that counter is greater
        than zero at the end, then the tree is visible from the outside """
        count = 4

        for otherx in range(0, x):
            if self._is_blocked(x, y, otherx, y):
                count -= 1
                break
        
        for otherx in range(x + 1, self.width):
            if self._is_blocked(x, y, otherx, y):
                count -= 1
                break

        for othery in range(0, y):
            if self._is_blocked(x, y, x, othery):
                count -= 1
                break

        for othery in range(y + 1, self.height):
            if self._is_blocked(x, y, x, othery):
                count -=1
                break

        return count > 0

    def get_number_visible_trees(self):
        count = 0
        for x in range(1, self.width-1):
            for y in range(1, self.height-1):
                if self._is_visible_from_outside(x, y):
                    count += 1
        # edge trees are always visible
        return count + self._num_edge_trees()


    def _calculate_scenic_score(self, x, y):
        """ Calculate the product of the scene scores for a tree
        in each of the cardinal directions. """
        left = 0
        for otherx in range(x-1, -1, -1):
            # Even an adjacent tree counts, so add to the score first
            left += 1
            if self._is_blocked(x, y, otherx, y):
                break
        
        right = 0
        for otherx in range(x+1, self.width):
            right += 1
            if self._is_blocked(x, y, otherx, y):
                break

        top = 0
        for othery in range(y-1, -1, -1):
            top += 1
            if self._is_blocked(x, y, x, othery):
                break

        bottom = 0
        for othery in range(y+1, self.height):
            bottom += 1
            if self._is_blocked(x, y, x, othery):
                break
             
        return left * right * top * bottom

    def get_most_scenic_tree(self):
        best = 0
        for x in range(0, self.width):
            for y in range(0, self.height):
                score = self._calculate_scenic_score(x, y)
                best = max(best, score)
        return best


def main():
    forest = Trees("input/day8.txt")
    print(forest.get_number_visible_trees())
    print(forest.get_most_scenic_tree())
main()
    

    