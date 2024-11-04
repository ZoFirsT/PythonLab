[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/UdtubNs6)
## Remove Symbols from the Input String
จงเขียนโปรแกรมที่สามารถลบสัญลักษณ์ออกจากข้อความให้เหลือเฉพาะตัวอักษร A-Z, a-z และ 0-9

**ตัวอย่างข้อความ**
```
Hello World! 123 hEllO People:) 0986
```

โปรแกรมจะแสดงผลลัพธ์ดังต่อไปนี้
```
HelloWorld123hEllOPeople0986
```

ในกรณีที่ข้อความเป็นสัญลักษณ์ทั้งหมด เช่น `$__$` โปรแกรมจะแสดงผลลัพธ์เป็นข้อความ `empty`
 

**Hint**  สามารถใช้ฟังก์ชัน `isalnum()`, `isalpha()`, และ `isdecimal()` 
ในการตรวจสอบประเภทตัวอักษรได้
<hr>

**ตัวอย่างที่ 1:**

**Input:** 
```
Good Morning! Now is at 9:30am
```
**Expected output:** โปรแกรมจะแสดงผลลัพธ์ ดังนี้
```
GoodMorningNowisat930am
```
<hr>

**ตัวอย่างที่ 2:**
**Input:** 
```
!@#$!@#$%#$
```
**Expected output:** ในกรณีที่ input string เป็นสัญลักษณ์ทั้งหมด โปรแกรมจะแสดงผลลัพธ์ ดังนี้
```
empty
```
<hr>
