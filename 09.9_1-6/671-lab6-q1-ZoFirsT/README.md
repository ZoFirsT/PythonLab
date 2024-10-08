[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/cVy17_-8)
## Print Coordinate Matrix
จงเขียนโปรแกรมที่แสดงผลลัพธ์เป็นตำแหน่งของเมทริกซ์ขนาด `nxn` จนถึงตำแหน่งที่ต้องการ เช่น `(x,y)`

โปรแกรมจะรับค่านำเข้าเป็นตัวเลขจำนวนเต็ม `n`,`x`,และ `y` ตามลำดับ โดย
* `n` คือ ขนาดของเมทริกซ์
* `x`,`y` คือ ตำแหน่งใด ๆ ของแถวและหลักตามลำดับ โดย**ตำแหน่งของเมทริกซ์**จะเริ่มจาก `(0,0)` จนถึง `(n-1,n-1)`

เมื่อรับค่าต่าง ๆ แล้วโปรแกรมจะแสดงผลลัพธ์เป็นตำแหน่งของเมทริกซ์ เริ่มจากตำแหน่ง `(0,0)` จนถึง `(x,y)` แล้วจึงหยุดการทำงาน

**ตัวอย่าง:** `n=3`,`x=1`,`y=2`
จากเมทริกซ์ `3x3` โปรแกรมจะแสดงผลลัพธ์จากตำแหน่ง `(0,0)` จนถึงตำแหน่ง`(1,2)` แล้วหยุดการทำงาน
```
(0,0) (0,1) (0,2) 
(1,0) (1,1) (1,2)
```

**หมายเหตุ:**
* นักศึกษาสามารถสมมติได้ว่า ผู้ใช้จะ input ค่า `x<n` และ `y<n` เสมอ
* คำสั่ง `break` จะหยุดการทำงานของ Loop เพียงชั้นเดียว

<hr>

**ตัวอย่างที่ 1:**
**Input:** `n=3`,`x=2`,`y=2`
```
3
2
2
```
**Expected output:**
```
(0,0) (0,1) (0,2) 
(1,0) (1,1) (1,2) 
(2,0) (2,1) (2,2) 
```
<hr>

**ตัวอย่างที่ 2:**
**Input:** `n=3`,`x=1`,`y=1`
```
3
1
1
```
**Expected output:**
```
(0,0) (0,1) (0,2) 
(1,0) (1,1) 
```
<hr>

**ตัวอย่างที่ 2:**
**Input:** `n=3`,`x=0`,`y=0`
```
3
0
0
```
**Expected output:**
```
(0,0) 
```
