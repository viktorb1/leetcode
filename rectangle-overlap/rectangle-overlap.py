class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # make sure no rectangles are actually lines
        if rec1[0] == rec1[2] or rec1[1] == rec1[3] or rec2[0] == rec2[2] or rec2[1] == rec2[3]:
            return False
        
        # get the highest point and see if it's lower than the lowest point
        if rec2[2] <= rec1[0] or rec2[3] <= rec1[1]:
            return False
        
        # get the lowest point and see if it's higher than the highest point
        if rec2[0] >= rec1[2] or rec2[1] >= rec1[3]:
            return False
        
        return True
