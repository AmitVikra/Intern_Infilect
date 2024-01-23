from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World, My name is Amit Vikram"}
class MatrixInput(BaseModel):
    matrix: List[List[int]]

@app.post("/largest_rectangle")
def largest_rectangle(matrix_input: MatrixInput):
    matrix = matrix_input.matrix

    rows, cols = len(matrix), len(matrix[0])

    def largest_area(heights):
        stack = []
        max_area = 0
        i = 0
        while i < len(heights):
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, heights[top] * (width + 1))
        while stack:
            top = stack.pop()
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, heights[top] * width)
        return max_area

    max_area = 0
    max_num = None
    heights = [0] * cols

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == matrix[i - 1][j] == matrix[i][j - 1] == matrix[i - 1][j - 1]:
                heights[j] = heights[j] + 1
            else:
                heights[j] = 1

            area = largest_area(heights)

            if area > max_area:
                max_area = area
                max_num = matrix[i][j]
    ans=(max_num, max_area)
    return ans
