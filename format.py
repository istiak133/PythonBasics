# x = 3.14159
# print(f"{x:.2f}")
# print(f"{x:.4f}")
# print(f"{x:.0f}")

# # ❌ Bad — loop এ + ব্যবহার
# result = ""
# for i in range(10):
#     result = result + str(i)   # প্রতিবার নতুন string তৈরি হয়

# print(result)    

# # ✅ Good — join ব্যবহার
# result = "".join([str(i) for i in range(10)])

# print(result)

# a = "hello"
# b = "hello"
# print(a == b)    # True  — value same
# print(a is b)    # True  — Python string interning করে

# a = "hello world"
# b = "hello world"
# print(a == b)    # True
# print(a is b)    # False — লম্বা string interning হয় না সবসময়a = [1, 2]
a = 10
b = 10
print(a == b)  # True
print(a is b)  # False