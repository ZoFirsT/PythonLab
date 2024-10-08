[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/c_ermruo)
## Sum First and Last `k` Numbers in a List

จงเขียนโปรแกรมคำนวณหาผลรวมทั้งหมดของตัวเลข `k` ตัวแรกใน list และ `k` ตัวสุดท้ายใน list

โปรแกรมจะรับตัวเลขจำนวนเต็มบวก `k` เป็นลำดับแรก จากนั้นโปรแกรมจะวนรับ input ตัวเลขมาเก็บไว้ใน list `A` จนกว่าผู้ใช้จะ input ตัวอักษร `q`

เมื่อได้ input ครบถ้วนแล้ว โปรแกรมจะตรวจสอบว่าจำนวนข้อมูลใน list มีเพียงพอในการคำนวณข้างต้นหรือไม่ นั่นคือความยาวของ list ต้องไม่น้อยกว่า `k` หากความยาวของ list ไม่เพียงพอให้โปรแกรม print `Invalid` และจบการทำงาน

หาก input มีจำนวนเพียงพอ ให้คำนวณหาผลรวมทั้งหมดของตัวเลข `k` ตัวแรกใน list `A` และ `k` ตัวสุดท้ายใน list `A`

**ตัวอย่างการคำนวณ** เมื่อ `k = 2` และ `A = [-3, 4, -4]`
ผลรวมของ 2 ตัวแรก (-3 และ 4)ใน list กับ 2 ตัวสุดท้ายใน list (4 และ -4) คือ `(-3) + 4 + 4 + (-4) = 1`
            
**หมายเหตุ:** 
นักศึกษาสามารถสมมติได้ว่าผู้ใช้จะ input ตัวเลขจำนวนเต็มบวกเท่านั้นสำหรับ `k` และ ตัวเลขและตัวอักษร `q` เท่านั้นสำหรับการรับค่า list
<hr>

**ตัวอย่างที่ 1:**
**Input:**   `k = 3` และ `A = [1.5, -2.5, 3, 4, 5, 6]`
```
3
1.5
-2.5
3 
4
5 
6
q
```
**Expected output:** 
ผลรวมของ 3 ตัวแรก ได้แก่ 1,2,3 และ 3 ตัวสุดท้ายใน list ได้แก่ 4,5,6 คือ `1.5+(-2.5)+3+4+5+6=21`
```
17.0
```
<hr>

**ตัวอย่างที่ 2:**
**Input:** `k = 5` และ `A = [-1, 5, 11]`
```
5
-1
5
11
q
```
**Expected output:** เนื่องจากความยาวของ list เท่ากับ 3 แต่ `k = 5` ทำให้ความยาวของ list นี้ไม่เพียงพอในการคำนวณผลรวม  โปรแกรมจึงแสดงผลดังต่อไปนี้
```
Invalid
```
<hr>
