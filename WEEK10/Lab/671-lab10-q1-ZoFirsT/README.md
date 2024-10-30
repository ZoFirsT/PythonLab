[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/UtQ8Yd9_)
## Create a Dictionary for Student Grade
จงเขียนโปรแกรมเพื่อรับข้อมูลเกรดนักศึกษาโดยมี `name` และ `grade` ที่มีค่า `'a'`, `'b'`, `'c'`, หรือ `'d'` 
โปรแกรมจะเก็บข้อมูลใน dictionary `student` โดยมี `name` และ `grade` เป็น keys และ
 * ข้อมูลเกรดทั้งหมดจะเป็นตัวอักษรพิมพ์เล็ก (lowercase) คือ `'a'`, `'b'`, `'c'`, หรือ `'d'` 
 * ถ้า `grade` มีค่าเป็น a โปรแกรมจะเปลี่ยน key `grade` เป็นตัวหนังสือพิมพ์ใหญ่ (uppercase) `GRADE`
   
จากนั้น โปรแกรมจะแสดงผลลัพธ์ dictionary `student`

<hr>

**ตัวอย่างที่ 1:**

**Input:** 
```
thai
b
```
**Expected output:** 
```
{'name': 'thai', 'grade': 'b'}
```
<hr>

**ตัวอย่างที่ 2:**

**Input:** 
```
kitty
a
```
**Expected output:**
```
{'name': 'kitty', 'GRADE': 'a'}
```
<hr>

**ตัวอย่างที่ 3:**

**Input:** 
```
Hit
c
```
**Expected output:** 
```
{'name': 'Hit', 'grade': 'c'}
```
<hr>

