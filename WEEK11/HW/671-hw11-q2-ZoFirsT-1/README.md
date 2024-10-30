[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/68csOEbQ)
## List Manipulation

จงเขียนโปรแกรมที่จัดการกับ list โดยการเรียกใช้ function ที่ชื่อว่า `list_manipulation` ที่รับ 4 parameters ได้แก่ (`list`, `command`, `location`, `value`)

* ถ้า `command='remove'` และ `location='end'` function จะลบค่าสุดท้ายของ list ออกและ return list นั้นกลับมา
* ถ้า `command='remove'` และ `location='beginning'` function จะลบค่าแรกของ list ออกและ return list นั้นกลับมา
* ถ้า `command='add'` และ `location='end'` function จะเพิ่มค่า value เข้าไปใน ตำแหน่งสุดท้ายของ list ออกและ return list นั้นกลับมา
* ถ้า `command='add'` และ `location='beginning'` function จะเพิ่มค่า value เข้าไปในตำแหน่งแรกของ list และ return list นั้นกลับมา

การทำงานของโปรแกรมจะเริ่มจากการรับตัวเลข 3 จำนวน โดยใช้ loop โดยตัวเลขที่รับเข้ามาจะถูกเก็บไว้ใน list `A` จากนั้นรับ input `command`, จากนั้นรับ input `location`, จากนั้นรับ input `value` จากผู้ใช้ตามลำดับ

**Hint:**
* สามารถใช้ `list.pop()` ในการลบข้อมูลตัวสุดท้ายของ list ได้
* สามารถใช้ `list.pop(0)` ในการลบข้อมูลตัวสุดแรกของ list ได้
* สามารถใช้ `list.append(value)` ในการเพิ่มข้อมูลที่ตำแหน่งสุดท้ายของ list ได้
* สามารถใช้ `list.insert(0,value)` ในการเพิ่มข้อมูลที่ตำแหน่งแรกของ list ได้

**Note:** ถ้านักศึกษาไม่ได้สร้างหรือเรียกใช้ `list_manipulation` function เพื่อการคำนวณ จะไม่ได้คะแนนจากข้อนี้ 

**ตัวอย่างที่ 1:**
**Input:** `A=[1,2,3], command='remove', location='end', value=1`  
```
1
2
3
remove
end
1
```
**Expected output:** โปรแกรมจะแสดง list ดังต่อไปนี้
```
['1', '2']
```
<hr>

**ตัวอย่างที่ 2:**
**Input:** `A=[1,2,3], command='remove', location='beginning', value=1`  
```
1
2
3
remove
beginning
1
```
**Expected output:** โปรแกรมจะแสดง list ดังต่อไปนี้
```
['2', '3']
```
<hr>

**ตัวอย่างที่ 3:**
**Input:** `A=[1,2,3], command='add', location='beginning', value=20`  
```
1
2
3
add
beginning
20
```
**Expected output:** โปรแกรมจะแสดง list ดังต่อไปนี้
```
['20', '1', '2', '3']
```
<hr>

**ตัวอย่างที่ 4:**
**Input:** `A=[1,2,3], command='add', location='end', value=30`  
```
1
2
3
add
end
30
```
**Expected output:** โปรแกรมจะแสดง list ดังต่อไปนี้
```
['1', '2', '3', '30']
```
<hr>
