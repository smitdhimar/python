a = int(input("enter the value more than or equal to 0"));

try:
    if(a<0):
        raise Exception({"error code": 23,"msg":"new aeasdlfsd"});
except Exception as e:
    print(e);
finally:
    print("smit")