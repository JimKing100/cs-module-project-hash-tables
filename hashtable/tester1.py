from hashtable1 import HashTable

ht = HashTable(8)

ht.put("key-0", "val-0")
ht.put("key-1", "val-1")
ht.put("key-2", "val-2")
ht.put("key-3", "val-3")
ht.put("key-4", "val-4")
ht.put("key-5", "val-5")
ht.put("key-6", "val-6")
ht.put("key-7", "val-7")
ht.put("key-8", "val-8")
ht.put("key-9", "val-9")

return_value = ht.get("key-0")
print(return_value)
return_value = ht.get("key-1")
print(return_value)
return_value = ht.get("key-2")
print(return_value)
return_value = ht.get("key-3")
print(return_value)
return_value = ht.get("key-4")
print(return_value)
return_value = ht.get("key-5")
print(return_value)
return_value = ht.get("key-6")
print(return_value)
return_value = ht.get("key-7")
print(return_value)
return_value = ht.get("key-8")
print(return_value)
return_value = ht.get("key-9")
print(return_value)

ht.put("key-0", "new-val-0")
ht.put("key-1", "new-val-1")
ht.put("key-2", "new-val-2")
ht.put("key-3", "new-val-3")
ht.put("key-4", "new-val-4")
ht.put("key-5", "new-val-5")
ht.put("key-6", "new-val-6")
ht.put("key-7", "new-val-7")
ht.put("key-8", "new-val-8")
ht.put("key-9", "new-val-9")

return_value = ht.get("key-0")
print(return_value)
return_value = ht.get("key-1")
print(return_value)
return_value = ht.get("key-2")
print(return_value)
return_value = ht.get("key-3")
print(return_value)
return_value = ht.get("key-4")
print(return_value)
return_value = ht.get("key-5")
print(return_value)
return_value = ht.get("key-6")
print(return_value)
return_value = ht.get("key-7")
print(return_value)
return_value = ht.get("key-8")
print(return_value)
return_value = ht.get("key-9")
print(return_value)

ht.put("key-0", "val-0")
ht.put("key-1", "val-1")
ht.put("key-2", "val-2")
ht.put("key-3", "val-3")
ht.put("key-4", "val-4")
ht.put("key-5", "val-5")
ht.put("key-6", "val-6")
ht.put("key-7", "val-7")
ht.put("key-8", "val-8")
ht.put("key-9", "val-9")

return_value = ht.get("key-0")
print(return_value)
return_value = ht.get("key-1")
print(return_value)
return_value = ht.get("key-2")
print(return_value)
return_value = ht.get("key-3")
print(return_value)
return_value = ht.get("key-4")
print(return_value)
return_value = ht.get("key-5")
print(return_value)
return_value = ht.get("key-6")
print(return_value)
return_value = ht.get("key-7")
print(return_value)
return_value = ht.get("key-8")
print(return_value)
return_value = ht.get("key-9")
print(return_value)

ht.delete("key-7")
ht.delete("key-6")
ht.delete("key-5")
ht.delete("key-4")
ht.delete("key-3")
ht.delete("key-2")
ht.delete("key-1")
ht.delete("key-0")

return_value = ht.get("key-0")
print(return_value)
return_value = ht.get("key-1")
print(return_value)
return_value = ht.get("key-2")
print(return_value)
return_value = ht.get("key-3")
print(return_value)
return_value = ht.get("key-4")
print(return_value)
return_value = ht.get("key-5")
print(return_value)
return_value = ht.get("key-6")
print(return_value)
return_value = ht.get("key-7")
print(return_value)
return_value = ht.get("key-8")
print(return_value)
return_value = ht.get("key-9")
print(return_value)

ht.delete("key-9")
ht.delete("key-8")

return_value = ht.get("key-8")
print(return_value)
return_value = ht.get("key-9")
print(return_value)
