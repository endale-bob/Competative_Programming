class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        image = [image[i][::-1] for i in range(len(image))]
        return [[0 if image[i][j] == 1 else 1 for j in range(len(image[0]))] for i in range(len(image))]