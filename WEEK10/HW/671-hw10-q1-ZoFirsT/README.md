[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/QwUZis86)
## Odd and Even Dictionary

จงเขียนโปรแกรมเพื่อรับ input เป็นตัวเลขเพื่อเก็บใน list `nums` เป็นจำนวน `n` ตัวเลข
จากนั้นโปรแกรมจะสร้าง dictionary โดย
* ตัวเลขใน list `nums` จะเป็น key
* ส่วน value จะมีค่าเป็นข้อความตามประเภทตัวเลข คือ `'even'` เมื่อตัวเลขเป็นเลขคู่ และ`'odd'` เมื่อตัวเลขเป็นเลขคี่

จากนั้น โปรแกรมจะแสดงผลลัพธ์ dictionary 

**หมายเหตุ:** 
* สามารถสมมติได้ว่าผู้ใช้จะ input ตัวเลขเท่านั้น
* สามารถสมมติได้ว่าตัวเลขที่ใส่เข้ามาต้องไม่ซ้ำกัน เนื่องจาก key ใน dictionary ต้องไม่ซ้ำกัน (unique key)
<hr>

**ตัวอย่างที่ 1:**

**Input:** ผู้ใช้ input `n` = 3
```
3
1
2
3
```
**Expected output:** 
```
{1: 'odd', 2: 'even', 3: 'odd'}
```
<hr>

**ตัวอย่างที่ 2:**

**Input:** ผู้ใช้ input `n` = 6
```
6
1
3
5
7
9
2
```
**Expected output:** 
```
{1: 'odd', 3: 'odd', 5: 'odd', 7: 'odd', 9: 'odd', 2: 'even'}
```
<hr>

**ตัวอย่างที่ 3:**

**Input:** ผู้ใช้ input `n` = 2
```
2
8
10
```
**Expected output:** 
```
{8: 'even', 10: 'even'}
```
<hr>
