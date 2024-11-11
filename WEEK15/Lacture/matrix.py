import numpy as np

# # arr = np.array([1.1, 2.1, 3.1], dtype=np.float64)
# # print("Original array:", arr)
# # print("Original dtype:", arr.dtype)

# # int32_arr = arr.astype(np.int32)
# # int64_arr = arr.astype(np.int64)
# # print("\nConverted to int32:", int32_arr)
# # print("int32 dtype:", int32_arr.dtype)
# # print("Converted to int64:", int64_arr) 
# # print("int64 dtype:", int64_arr.dtype)

# # float32_arr = int32_arr.astype(np.float32)
# # float64_arr = int64_arr.astype(np.float64)
# # print("\nConverted to float32:", float32_arr)
# # print("float32 dtype:", float32_arr.dtype)
# # print("Converted to float64:", float64_arr)
# # print("float64 dtype:", float64_arr.dtype)

# # print("\nArray operations:")
# # print("Sum:", arr.sum())
# # print("Mean:", arr.mean())
# # print("Standard deviation:", arr.std())
# # print("Min:", arr.min())
# # print("Max:", arr.max())


# import numpy as np
# arr1 = np.array([10, 11, 12, 13, 14, 15])
# arr2 = np.array([20, 21, 22, 23, 24, 25])
# out = np.add(arr1, arr2)
# # arr1 + arr2 (element-wise)
# print(out)

# # บวก

# out = np.subtract(arr1, arr2)
# # # arr1 - arr2 (element-wise)
# print(out)

# # ลบ

# out = np.multiply(arr1, arr2)
# print(out)

# # คูณ

# out = np.divide(arr1, arr2)
# print(out) 

# # หาร

# arr1 = np.array([10, 11, 12, 13, 14, 15])
# arr2 = np.array([20, 21, 22, 23, 24, 25])
# print(np.add(arr1, arr2))

a = np.array([[1,2], [3,4], [5,6]])
print(a, a.shape)
print(np.sum(a))
print(np.sum(a, axis=0))
print(np.sum(a, axis=1))

print("===============================")

print(np.mean(a))
print(np.std(a, axis=0))
print(np.max(a, axis=1))