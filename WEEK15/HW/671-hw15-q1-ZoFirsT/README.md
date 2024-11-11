[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/F1D9yEAG)
## Count Words 

จงเขียนโปรแกรมเพื่อนับจำนวนคำในไฟล์ `data.csv` ที่ให้มา โดยข้อมูลใน `data.csv` นั้นจะมีทั้งหมด 3 คอลัมน์ `sentiment` `text` และ `user` ดังตัวอย่างด้านล่าง

```
sentiment,text,user
"positive","Interesting new publication by the $LYEL team refer to inhibition of AKT as a way of increasing T Cell Stemness as… https://t.co/93TYuuzbRB","biotech_chris"
"neutral","@SongbirdTam_83 .@Pfizer vaccine DOES NOT cause Myocarditis in children above baseline levels ..... or in adults\n\nA… https://t.co/Mu8nUf7Nub","PLHartungRN"
...
```

ในโปรแกรมนี้ผู้ใช้งานจะเป็นคนกำหนดคำที่ต้องการนับ หลังจากนั้นโปรแกรมจะนับจำนวนคำเฉพาะในคอลัมน์ที่มีชื่อว่า `text` ในไฟล์ `data.csv` เท่านั้น (ไม่สนใจคำในคอลัมน์อื่น)

การนับคำให้ใช้คำสั่ง `count()` ของ string เท่านั่นเพื่อให้ได้ผลลัพธ์ที่ตรงกับข้อมูลที่ใช้ในการตรวจความถูกต้องของการบ้าน [[link](https://www.w3schools.com/python/ref_string_count.asp)]


**Hint**
* ต้องใช้ `import pandas as pd`
* สามารถอ่านข้อมูลจากไฟล์ `data.csv` โดยใช้ฟังก์ชัน `read_csv()` ได้
* คำที่มีตัวอักษรพิมพ์เล็กกับพิมพ์ใหญ่ไม่ตรงกันให้ถือว่าเป็นคนละคำกั (`'shows'` ไม่ใช่คำเดียวกันกับ `'Shows'`)
* ใช้ str.count() ในการนับ


<hr>

**ตัวอย่างที่ 1:**

**Input:** 
```
you
```
**Expected output:** โปรแกรมจะแสดงผลลัพธ์ ดังนี้
```
5
```
<hr>

**ตัวอย่างที่ 2:**

**Input:** 
```
shows
```
**Expected output:** โปรแกรมจะแสดงผลลัพธ์ ดังนี้
```
9
```

<hr>

**ตัวอย่างที่ 3:**

**Input:** 
```
Shows
```
**Expected output:** โปรแกรมจะแสดงผลลัพธ์ ดังนี้
```
0
```

<hr>

**ตัวอย่างที่ 4:**

**Input:**
```
neutral
```
**Expected output:** โปรแกรมจะแสดงผลลัพธ์ ดังนี้
```
0
```
<hr>
