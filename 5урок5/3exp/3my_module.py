import moda
from folderb.modb import foo, bar
# import modc # если указать просто его, то всё что в нём - отражиться в коде первым
from modc import foo # помимо foo всё равно выдаст и остальное

print(moda.foo)
moda.bar()

print(foo)
bar()