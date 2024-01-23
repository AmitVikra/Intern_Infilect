Create a Fast API service that accepts the matrix on a POST API and returns the largest
rectangle’s area and the number itself.

POST url: http://localhost:8000/largest_rectangle


Saved log (http://localhost:8000/logs)
Restul=
{"timestamp":"2024-01-24T01:23:51.802018","request":[[1,0,1,0,1,-9],[7,1,1,1,2,-9],[0,1,1,1,2,-9],[1,0,0,0,5,-9],[5,0,0,0,5,9]],"response":[1,6]},
{"timestamp":"2024-01-24T01:24:46.846043","request":[[1,0,1,0,1,-9],[1,1,1,1,2,-9],[1,1,1,1,2,-9],[1,0,0,0,5,-9],[5,0,0,0,5,9]],"response":[1,8]},
{"timestamp":"2024-01-24T01:25:06.030955","request":[[1,8,1,1,5],[1,1,1,1,2],[1,1,1,1,2],[1,1,1,1,5],[5,0,0,0,5]],"response":[1,12]}]}

**Here, I verified the function with some example data using the POST API.**

Input = 
    {
      "matrix": [
        [1, 8, 1, 1, 5],
        [1, 1, 1, 1, 2],
        [1, 1, 1, 1, 2],
        [1, 1, 1, 1, 5],
        [5, 0, 0, 0, 5]
      ]
    }
{"result":[1,12]}

Input=
    {
      "matrix": [
      [1, 0, 1, 0, 1, -9],
      [1, 1, 1, 1, 2, -9],
      [1, 1, 1, 1, 2, -9],
      [1, 0, 0, 0, 5, -9],
      [5, 0, 0, 0, 5, 9]
      ]
    }
{"result":[1,8]}

Input=
    {
      "matrix": [
      [1, 0, 1, 0, 1, -9],
      [7, 1, 1, 1, 2, -9],
      [0, 1, 1, 1, 2, -9],
      [1, 0, 0, 0, 5, -9],
      [5, 0, 0, 0, 5, 9]
      ]
    }
{"result":[1,6]}

Input=
    {
      "matrix": [
      [1, 1, 1, 0, 1, -9],
      [1, 2, 2, 2, 2, -9],
      [1, 2, 2, 2, 2, -9],
      [1, 0, 0, 0, 5, -9],
      [5, 0, 0, 0, 5, 9]
      ]
    }
{"result":[2,8]}
