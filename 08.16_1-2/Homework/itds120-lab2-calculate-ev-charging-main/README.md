## Calculate the EV Car Charging
จงเขียนโปรแกรมเพื่อคำนวณจำนวนชั่วโมงที่ต้องชาร์จรถไฟฟ้าให้เต็ม และค่าไฟในการชาร์จรถยนต์ไฟฟ้าตามลำดับ โดย
* รับ input เป็นขนาดของแบตเตอรี่ของรถ (kW) และอัตราความเร็วในการชาร์จไฟของรถ (kW/hr)
* สมมติว่าแบตเตอรี่ต้องชาร์จจาก 0 ไปจนเต็ม 100% ของขนาดแบตเตอรี่
* กำหนดให้อัตราค่าไฟคงที่เป็น 4.5 บาทต่อ kW
* ผลลัพธ์ต้องแสดงเป็นทศนิยม 2 ตำแหน่งโดยสามารถใช้คำสั่ง round เช่น round(x,2) จะเป็นการปัดค่าของตัวแปร x ให้อยู่ในรูปทศนิยม 2 ตำแหน่ง
<hr>

**ตัวอย่างที่ 1:**

**Input:** `capacity=45` และ `charge_rate=7.4` โดยพิมพ์ 45 และ 7.4 ตามลำดับ
```
45
7.4
```
**Expected output:** หลังจากโปรแกรมคำนวณแล้ว โปรแกรมควรแสดงผลลัพธ์เป็นจำนวนชั่วโมงและจำนวนเงินบาทตามลำดับ
```
6.08
202.5
```
<hr>

**ตัวอย่างที่ 2:**

**Input:** `capacity=10.7` และ `charge_rate=3.7` โดยพิมพ์ 10.7 และ 3.7 ตามลำดับ
```
10.7
3.7
```
**Expected output:** หลังจากโปรแกรมคำนวณแล้ว โปรแกรมควรแสดงผลลัพธ์เป็นจำนวนชั่วโมงและจำนวนเงินบาทตามลำดับ
```
2.89
48.15
```
<hr>
