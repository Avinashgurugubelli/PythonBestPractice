def add(num1):
    return num1+5
def mul(num1):
    return  num1*2

def main_fuc(function1,function2,numlist):
    # import pdb; pdb.set_trace()
    return_sum = 0
    for i in numlist:
        if(i%2==0):
            return_sum +=function1(i)
        else:
            return_sum +=function2(i)
    return return_sum

if __name__ == '__main__':
    numlst=[1,2,3,54,5,6,57,8,9]
#passing other function's as an argumentds here add, and mul
    result= main_fuc(add,mul,numlst)
    print(result)

