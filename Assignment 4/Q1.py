# What is the difference between List and Tuple in Python?
# Explain in terms of:
# 1.Mutability
# 2.Memory
# 3.Performance
# 4.Use cases

#--------------------------------------------------------------------------------------------------
# Terms                     List                                        Tuple
#--------------------------------------------------------------------------------------------------
# Mutability        Mutable(Can be modified)                    Immutable(cannot be modified)

# Memory            Can Store mixed data types                  Used for fixed data types

# Performance       Slower than tuple                           Faster than list

# Use cases         stores multiple values in a                 same like list, but data cannot be 
#                   single variable.data can be changed         changed after creation.

#--------------------------------------------------------------------------------------------------


# lst = [10,20,30]
# tpl = (10,20,30)

# lst[0]=100
# tpl

s = "Python"
print(id(s))
s=s+"3"
print(id(s))