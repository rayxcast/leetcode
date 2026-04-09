class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = 0
        r = len(matrix)-1
        mid_row = (r+l)//2

        # find the right row
        while l <= r:
            print(l, r, mid_row)
            if target >= matrix[mid_row][0] and target <= matrix[mid_row][-1]:
                # print("found row:", mid_row)
                break
            elif target > matrix[mid_row][0]:
                # print("larger:", target, matrix[mid_row][0])
                l = mid_row+1
                mid_row = (l+r)//2
            elif target < matrix[mid_row][0]:
                # print("smaller:", target, matrix[mid_row][0])
                r = mid_row-1
                mid_row = (l+r)//2
            
        l = 0
        r = len(matrix[mid_row])-1
        mid_col = (l+r)//2
        while l <= r:
            # print(l, r, mid_col)
            if target > matrix[mid_row][mid_col]:
                # print("larger:", target, matrix[mid_row][mid_col])
                l = mid_col+1
                mid_col = (r+l)//2
            elif target < matrix[mid_row][mid_col]:
                # print("smaller:", target, matrix[mid_row][mid_col])
                r = mid_col-1
                mid_col = (r+l)//2
            else:
                return True
        
        return False