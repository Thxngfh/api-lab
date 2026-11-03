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

## Part B

1. การทดสอบ API กับ Server จริงช่วยตรวจเจอปัญหาการเชื่อมต่อเครือข่าย และปัญหาการทำงานร่วมกันระหว่าง Client กับ Server จริง ซึ่ง Unit Test ที่ใช้ Stub ไม่สามารถตรวจเจอได้ ส่วน Unit Test ยังจำเป็นเพราะใช้ทดสอบโค้ดแต่ละส่วนแยกกันได้ รวดเร็ว และช่วยหาข้อผิดพลาดได้ง่าย

2. การสร้าง User ใหม่ในแต่ละ Test ช่วยให้ข้อมูลของแต่ละ Test แยกจากกัน และป้องกันไม่ให้ข้อมูลชนกันหรือกระทบกับ Test อื่น ส่วน Public Token เป็น Token ที่ใช้ร่วมกัน ไม่ได้แยกข้อมูลตามผู้ใช้ ใน Project 2 จะนำแนวคิดนี้ไปใช้โดยสร้าง Account และข้อมูล Shop หรือ Hotel แยกกันในแต่ละ Test เพื่อไม่ให้การทดสอบแต่ละครั้งรบกวนกัน

3. การใช้ Session เดียวกันช่วยให้ Request แต่ละครั้งใช้การเชื่อมต่อและ Cookie ชุดเดิม ทำให้ Server สามารถจดจำการทำงานต่อเนื่องของผู้ใช้ได้ หากไม่ใช้ Session อาจเกิดปัญหาในการยืนยันตัวตน จากการทดลอง Step 0.12 รอบที่ 1 ไม่ผ่าน ได้ Status Code 401 ส่วนรอบที่ 2 และ 3 ผ่าน ได้ Status Code 200

4. ข้อผิดพลาดใน Step 0.16 พบจากกรณีที่เลือกไม่ใช้เครื่องมือทั้ง 3 อย่าง ได้แก่ Knife, Pizza cutter และ Scissors ทำให้ API ตอบกลับเป็น HTTP 500 และไม่มีข้อความแจ้งข้อผิดพลาด ซึ่งแย่กว่า HTTP 400 ที่มีข้อความอธิบาย เพราะผู้พัฒนาสามารถรู้สาเหตุของปัญหาและจัดการได้ง่ายกว่า ส่วนการเก็บ Test ไว้เป็น xfail เพื่อบันทึกว่าปัจจุบันยังมีข้อผิดพลาดนี้อยู่ และสามารถตรวจสอบได้เมื่อมีการแก้ไขในอนาคต

5. Base Choice Coverage ต้องใช้ Test ทั้งหมด 9 กรณี โดยเลือกค่าพื้นฐานของแต่ละ Characteristic มา 1 ชุด และทดสอบค่าที่เหลือของแต่ละกลุ่มให้ครบ ส่วน All Combinations Coverage ต้องใช้ Test ทั้งหมด 72 กรณี โดยนำจำนวน Block ของแต่ละ Characteristic มาคูณกัน (3 × 4 × 2 × 3 = 72)

6. จากการทดสอบ Step A4 พบว่า เมื่อผู้ใช้อื่นพยายามอ่าน Rating ได้ Status Code 404 ส่วนการแก้ไขและลบได้ Status Code 400 โดยคาดหวังว่าจะได้ Status Code 403 Forbidden อย่างไรก็ตาม ไม่ถือว่าเป็น Bug เพราะ API ปฏิเสธคำขอทั้งหมดและไม่อนุญาตให้ผู้ใช้อื่นเข้าถึงหรือแก้ไขข้อมูลของเจ้าของ Rating ได้

7. เมื่อใช้ Token ปลอม 0000000000000000 เรียก API เพื่ออ่านข้อมูล Rating พบว่าได้ Status Code 200 OK และสามารถอ่านข้อมูล Rating กลับมาได้ แสดงว่า API ยอมรับ Token ที่ไม่ได้ผ่านการยืนยันตัวตน ซึ่งถือเป็นข้อผิดพลาดด้านความปลอดภัย เพราะบุคคลทั่วไปอาจใช้ Token ปลอมเข้ามาอ่านข้อมูลของผู้ใช้อื่นได้ ดังนั้น API ควรตรวจสอบ Token ก่อนอนุญาตให้เข้าถึงข้อมูล

8. API Test สามารถตรวจสอบ Status Code และข้อมูล JSON ที่ Server ส่งกลับมาได้โดยตรง ทำให้ตรวจสอบการทำงานของ API ได้ละเอียด ส่วนการทดสอบผ่านหน้าเว็บสามารถตรวจสอบการแสดงผลและการใช้งานหน้าเว็บไซต์ เช่น ปุ่ม เมนู และการจัดวางหน้าจอ ซึ่ง API Test ไม่สามารถตรวจสอบได้

