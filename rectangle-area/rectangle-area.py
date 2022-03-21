class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = (ay2-ay1)*(ax2-ax1)
        area2 = (by2-by1)*(bx2-bx1)
        common_h = min(ay2, by2) - max(ay1, by1)
        common_w = min(ax2, bx2) - max(ax1, bx1)
        common_h = max(0, common_h)
        common_w = max(0, common_w)
        return area1 + area2 - common_h*common_w