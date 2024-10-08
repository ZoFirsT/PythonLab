[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/k35IrvWx)
## Find Prime Numbers

จงเขียนโปรแกรมที่รับตัวเลขจำนวนเต็มบวก `n` โดย `1<n<1000` (โปรแกรมจะต้องวนรับ input ไปเรื่อย ๆ จนกว่าจะได้ค่า `n` ที่ตรงตามเงื่อนไข) จากนั้นจึงแสดงผลลัพธ์เป็นเลขจำนวนเฉพาะ (Prime number) ที่อยู่ระหว่าง 1 ถึง `n` และแสดงจำนวนของเลขจำนวนเฉพาะ

**หมายเหตุ:** เลขจำนวนเฉพาะ (Prime number) คือ จำนวนเต็มบวกที่มากกว่า 1 และมีตัวหารที่เป็นบวกอยู่ 2 ตัว คือ 1 และตัวมันเอง 
<hr>

**ตัวอย่างที่ 1:**
**Input:** `n=5`  
```
5
```
**Expected output:** โปรแกรมจะแสดงผลลัพธ์ดังต่อไปนี้
```
2 3 5 
Total prime numbers: 3
```
<hr>

**ตัวอย่างที่ 2:**

**Input:**
ในกรณีที่ input ไม่ตรงตามเงื่อนไข โปรแกรมจะวนรับค่า ไปเรื่อย ๆ จนกว่าจะได้ ค่า `n` ที่ `1<n<1000` คือ 19
```
-5
0
1
1000
19
```
**Expected output:**  โปรแกรมจะแสดงผลลัพธ์ดังต่อไปนี้
```
2 3 5 7 11 13 17 19 
Total prime numbers: 8
```
<hr>
