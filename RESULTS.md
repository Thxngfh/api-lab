# API Lab Results

- Step 0.1, the number of pizza names: 18
- Step 0.2, HTTP status: 200
    - Content-Type: application/json
    - Set-Cookie: AWSALB, AWSALBCORS
- Step 0.3, status code of the request without a token: 401
- Step 0.3, status code with a token: 200
    - Available tools: Knife, Pizza cutter, Scissors
- Step 0.4, the name of your pizza: The Dead Bolognese
- Step 0.12, ผลการทดสอบ 3 รอบโดยไม่ใช้ Session (ไม่บังคับ): รอบที่ 1 ไม่ผ่าน (401), รอบที่ 2 ผ่าน (200), รอบที่ 3 ผ่าน (200)
- Step 0.16, blocks of "how many of the three tools are excluded": 0, 1, 2, 3

## Defect report
- Title: API returns HTTP 500 when all three tools are excluded
- Request: POST /api/pizza with {"excludedTools": ["Knife", "Pizza cutter", "Scissors"]}
- Expected result: HTTP 400 with a JSON error message
- Actual result: HTTP 500 with an empty response body
- Severity: Medium

## Part A

- Step A4, status codes when the other user reads, changes and deletes the rating:
  - Read: 404 Not Found
  - Update: 400 Bad Request
  - Delete: 400 Bad Request
