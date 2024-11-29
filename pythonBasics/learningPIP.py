import camelcase

c = camelcase.camelcase()
txt = "string is fucking serious task"
c.hump(txt)
print(txt)
