class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # // the L and R are for the row search 
        L = 0
        R = len(matrix) - 1

        while(L<=R):

            m = (L+R)//2
            if matrix[m][-1] == target:
                return True

            if  matrix[m][0] <= target <= matrix[m][-1]:

                # the small l and r are for the column search
                # That is only if the target is within that row 
                l = 0
                r = len(matrix[m])-1
                while(l<=r):
                    sm = (l+r)//2
                    if matrix[m][sm] == target:
                        return True
                    if matrix[m][sm] < target:
                        l = sm+1
                    if matrix[m][sm] > target:
                        r = sm-1

            if matrix[m][-1] < target:
                L = m + 1

            elif matrix[m][-1] > target:
                R = m - 1

        return False    
            