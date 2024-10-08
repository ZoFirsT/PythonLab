[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/W7AeFjIg)
## Divisible by 'd'
จงเขียนโปรแกรมโดยใช้ **for loop** เพื่อแสดง และนับจำนวนตัวเลขใน range `[x,y]` ที่สามารถหารด้วย `d` ลงตัว โปรแกรมนี้รับ 3 input ดังนี้
* `x` ตัวเลขเริ่มต้นของ range
* `y` ตัวเลขสุดท้ายของ range (รวม`y`ด้วย)
* `d` ตัวหาร

**หมายเหตุ:** 
* นักศึกษาสามารถสมมติได้ว่าผู้ใช้จะ input ตัวเลขจำนวนเต็มเท่านั้น `d` ไม่เท่ากับ 0 และ input `y` ต้องมากกว่า `x`

<hr>

**ตัวอย่างที่ 1:**
**Input:** `x=5`, `y=21`, และ `d=3`
```
5
21
3
```
**Expected output:** หลังจากโปรแกรมรับค่า `x`, `y` และ `d` แล้ว โปรแกรมจะแสดงตัวเลขใน range [5, 21] ที่ 3 หารลงตัว ซึ่งมีจำนวนทั้งหมด 6 จำนวน ดังต่อไปนี้
```
6 9 12 15 18 21 count=6
```
<hr>

**ตัวอย่างที่ 2:**
**Input:** `x=-10`, `y=10`, และ `d=4`
```
-10
10
4
```
**Expected output:** หลังจากโปรแกรมรับค่า `x`, `y` และ `d` แล้ว โปรแกรมจะแสดงตัวเลขใน range [-10, 10] ที่ 4 หารลงตัว ซึ่งมีจำนวนทั้งหมด 5 จำนวน ดังต่อไปนี้
```
-8 -4 0 4 8 count=5
```
<hr>

**ตัวอย่างที่ 3:**
**Input:** `x=-5`, `y=5`, และ `d=-1`
```
-5
5
-1
```
**Expected output:** หลังจากโปรแกรมรับค่า `x`, `y` และ `d` แล้ว โปรแกรมจะแสดงตัวเลขใน range [-5, 5] ที่ -1 หารลงตัว ซึ่งมีจำนวนทั้งหมด 11 จำนวน ดังต่อไปนี้
```
-5 -4 -3 -2 -1 0 1 2 3 4 5 count=11
```
