class Solution:
    def searchMatrix(self, mat, x): 
    # 	row = -1
	    
    #     low = 0
    #     high = len(mat) - 1
    #     while low <= high:
    #         mid = low + (high - low) // 2
    #         if mat[mid][0] == x:
    #             return True
             
    #         if mat[mid][0] > x:
    #             high = mid - 1
    #         else:
    #             row = mid
    #             low = mid + 1
         
    #     if row == -1:
    #         return False
       
    #     low = 0
    #     high = len(mat[row]) - 1
    #     while low <= high:
    #         mid = low + (high - low) // 2
    #         if mat[row][mid] == x:
    #             return True
            
    #         if mat[row][mid] > x:
    #             high = mid - 1
    #         else:
    #             low = mid + 1
        
        '''  
        mat = [[1,  5,  9]
                [14, 20, 21]
                [30, 34, 43]]
        x = 14
        
        n = 3
        m = 3
        flatMat = [[1, 5, 9], [14, 20, 21], [30, 34, 43]]
                                mid
        1. let mid = 4 so mat[1][1] > x
        2. let mid = 2 so mat[0][2] > x
        3. let mid = 3 so mat[1][0] == x
        
        let mid so row = mid/m and col = mid%m
        '''

        n = len(mat)
        m = len(mat[0])
        low = 0
        high = m * n - 1
        while low <= high:
            mid = low + (high - low) // 2
            row = mid // m
            col = mid % m
            
            if mat[row][col] == x:
                return True
            
            if mat[row][col] > x:
                high = mid - 1
            else:
                low = mid + 1
        
        return False
    	
    	
