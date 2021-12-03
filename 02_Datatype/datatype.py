
# int data type
# a=10
# b=10
# print(type(a))
# print( type(b))
# print(id(a))
# print(id(b))
# b=20
# print(id(b))

# int Binary form
# a=0b10
# b=0b10
# print(id(a))
# print(id(b))
# b=0b11
# print(id(b))


# int Octal form
# a=0o766
# b=0o466
# print(id(a))
# print(type(a))
# print(type(b))
# print(id(b))
# b=0o76
# print(id(b))

# int hexadecimal form
# a=0x766
# b=0x466
# print(id(a))
# print(type(a))
# print(type(b))
# print(id(b))
# b=0x76
# print(id(b))


# Base Conversion
# bin()
# Decimal to Binary
# a=205
# print(bin(a))

# Octal to Binary
# a=0o17
# print(bin(a))

# Hexa decimal to Binary
# a=0x1a
# print(bin(a))


# oct()
# Decimal to octal
# a=205
# print(oct(a))

# Binary to octal
# a=0b11
# print(oct(a))

# Hexa decimal to octal
# a=0x1a
# print(oct(a))


# hex()
# Decimal to hexa Decimal
# a=205
# print(hex(a))

# Binary to hexa Decimal
# a=0b11
# print(hex(a))

# Octal to Hexa decimal
# a=0b1
# print(hex(a))


# float data type
# a=10.5
# b=10.5
# print(type(a))
# print( type(b))
# print(id(a))
# print(id(b))
# b=20.5
# print(id(b))

# Complex data type
# a=5+4j
# a=5.5+4j
# a=5.5+4.5j
# a=5+4.5j


# a=0b11+4.5j
# a=0b11+0b11j It will show an error
# print(type(a))

# Arithmetic operation on complex data type
# a=5+3j
# b=4+2j
# print(a+b)
# print(a-b)
# print(a*b)

# print(a.real)
# print(a.imag)

# bool data type
# True and false
# a=10
# b=20
# c=a>b
# print(c)
# c=a<b
# print(c)

# print(True+True)
# print(False+True)

# String data type (str)
# a="Mritunjay"
# print(a)
# print(a[0])
# a='''Mritunjay
# Kumar
# Tiwari \t '''
# print(a)
# print(a[0])
# print(a[-1])
# print(a[0:40])
# print(a[0:])
# print(a[:2])
# print(a[:])
# print(a*3)
# print(len(a))

# bytes data type
# a=[1,2,3,4]
# print(type(a))
# x=bytes(a)
# print(type(x))
# x[5]=5 It will show an error
# for i in x : print(i)

# bytearray data type
# a=[1,2,3,4,5]
# b=bytearray(a)
# print(b)
# for i in b:
#     print(i)
# b[0]=2
# print("\n")
# for i in b:
#     print(i)


# list data type
# lst=[1,2,'jay',2.4]
# print(type(lst))
# print(lst)
# print(lst[0])
# print(lst[3])
# print(lst[4]) It will show an error

# tuple data type
# t = (1, 2, "jay", 2.4)
# print(type(t))
# t[0]=5 It will show an error
# t.append(10) It will show an error
# t.remove(1) It will show an error

# range data type
# form 1
# r=range(10)
# for i in r:
#     print(i)

# form 2
# r=range(1,11)
# for i in r:
#     print(i)

# form 3
# r=range(2,22,2)
# for i in r:
#     print(i)

# print(r[1])
# r[0]=100 It will show an error
# lst=list(range(10))
# print(lst)

# set data type
# s={1,2,3,'jay'}
# print(type(s))
# for i in s:
#     print(i)
# s.add(4)
# s.remove('jay')
# print(s)
# print(s[0]) It will show an error

# frozenset data type
# s={1,2,3,4}
# fs=frozenset(s)
# print(type(fs))
# print(fs)
# for i in fs:
#     print(i)
# fs.add(5) It will show an error

# dict data type
# d={1:'jay',2:'shiva',3:'naga'}
# print(d)
# print(type(d/))
# for i in d:
#     print(i)

# d[1]='Mritunjay'
# print(d)

# None data type
a=None
print(a)