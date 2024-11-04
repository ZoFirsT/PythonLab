[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Ilv6EA5k)


## String Formatting

จงเขียนโปรแกรมที่สามารถเปลี่ยนจากข้อความที่ถูกแบ่งคำด้วยเครื่องหมายจุลภาค หรือ comma (`,`) แล้วนำคำต่าง ๆ มาเรียงใหม่ให้เป็นประโยคที่เข้าใจง่าย
โดยข้อความที่โปรแกรมจะรับมานั้นจะมีรูปแบบดังนี้

```
<ชื่อ>,<นามสกุล>,<อายุ>,<เพศ>
```

เช่น

```
Akara,Supratak,25,male
```

หลังจากนั้นโปรแกรมจะทำการแยกคำด้วย `,` แล้วนำเอาคำต่าง ๆ มาเรียงใหม่ให้เป็นประโยคดังนี้

```
<นามสกุล>, <ชื่อ> is a <เพศ> student and is <อายุ> years old.
```

เช่น

```
Supratak, Akara is a male student and is 25 years old.
```

ในกรณีที่ input ในตำแหน่งที่ 3 ที่เป็นข้อมูลตัวเลขเพื่อบ่งบอกอายุ **ไม่ใช่ตัวเลข** ให้โปรแกรมแสดงผลลัพธ์ว่า `invalid input` เช่น

```
Akara,Supratak,twenty-five,male
invalid input
```


**Hint** สามารถใช้ฟังก์ชัน `split()` ในการแยกคำได้

<hr>

**ตัวอย่างที่ 1:**

**Input:** 
```
Jidapa,Kraisangka,26,female
```
**Expected output:** โปรแกรมจะแสดงผลลัพธ์ ดังนี้
```
Kraisangka, Jidapa is a female student and is 26 years old.
```
<hr>

**ตัวอย่างที่ 2:**

**Input:** 
```
A,A,A,A
```
**Expected output:** ในกรณีนี้ input ในตำแหน่งที่ 3 ไม่ใช่ตัวเลข โปรแกรมจะแสดงผลลัพธ์ ดังนี้
```
invalid input
```
<hr>
