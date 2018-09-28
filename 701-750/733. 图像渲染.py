class Solution:
    def floodFill(self, image, sr, sc, newColor):
        tmp=image[sr][sc]
        flag=[[False for l in line] for line in image]
        self.count(sr, sc,image,flag,tmp,newColor)
        return image
    def count(self,i,j,grid,flag,tmp,newColor):
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or flag[i][j] or grid[i][j]!=tmp:
            return
        flag[i][j]=True
        grid[i][j]=newColor
        self.count(i-1,j,grid,flag,tmp,newColor)
        self.count(i,j-1,grid,flag,tmp,newColor)
        self.count(i+1,j,grid,flag,tmp,newColor)
        self.count(i,j+1,grid,flag,tmp,newColor)