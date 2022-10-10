class Test:
    @staticmethod
    def assert_equals(a, b, *args, **kwargs):
        assert a == b
        print('Passed')
# problem https://edabit.com/challenge/6R6gReGTGwzpwuffD (3 point)
print('num1')
def fun1( a ):
    for x in a:
        while x!=0:
            y=x
            x = int(x//10)
            if (y % 10) == 7:
                return "Boom!"
    return "there is no 7 in the array"
Test.assert_equals(fun1([2, 6, 7, 9, 3]), "Boom!")
Test.assert_equals(fun1([33, 68, 400, 5]), "there is no 7 in the array")
Test.assert_equals(fun1([86, 48, 100, 66]), "there is no 7 in the array")
Test.assert_equals(fun1([76, 55, 44, 32]), "Boom!")
Test.assert_equals(fun1([35, 4, 9, 37]), "Boom!")
#problem https://edabit.com/challenge/eCPim4XcssdZdvs32 (3 point)
print('num2')
def fun2(a):
    i=0
    while i<len(a):
        t = 0
        y = list(a[i])
        for z in y:
            if z.isdigit():
                t = 1
        if t != 1:
            a.remove(a[i])
            i=-1
        i+=1
    return a
Test.assert_equals(fun2(['abc', 'abc10']), ['abc10'])
Test.assert_equals(fun2(['abc', 'ab10c',  'a10bc', 'bcd']),['ab10c', 'a10bc'])
Test.assert_equals(fun2(['1', 'a',' ','b']), ['1'])
Test.assert_equals(fun2(['rct', 'ABC', 'Test', 'xYz']), [])
Test.assert_equals(fun2(['this IS','10xYZ', 'xy2K77', 'Z1K2W0', 'xYz']), ['10xYZ', 'xy2K77', 'Z1K2W0'])
Test.assert_equals(fun2(['-/>', '10bc', 'abc ']), ['10bc'])
#problem https://edabit.com/challenge/yXSTvCNen2DQHyrh6 (3 point)
print('num3')
def fun3 (a):
    y=list(a)
    s=0
    for x in y:
        if(type(x)==type([])):
            s+=fun3(x)
        else:
            s+=1
    return s
Test.assert_equals(fun3([1, [2,3]]), 3)
Test.assert_equals(fun3([1, [2, [3, 4]]]), 4)
Test.assert_equals(fun3([1, [2, [3, [4, [5, 6]]]]]), 6)
Test.assert_equals(fun3([1, 7, 8]), 3)
Test.assert_equals(fun3([2]), 1)
Test.assert_equals(fun3([2, [3], 4, [7]]), 4)
Test.assert_equals(fun3([2, [3, [5, 7]], 4, [7]]), 6)
Test.assert_equals(fun3([2, [3, [4, [5]]], [9]]), 5)
Test.assert_equals(fun3([]), 0)
#problem https://edabit.com/challenge/vEY5A5Kq8xsPTQG8S (3 point)
print('num4')
def fun4 (a,b,c):
    a=0 # оно не нужно тк пути одинаковые
    return (2*b*c/(b+c))
Test.assert_equals(fun4(18, 10, 30), 15)
Test.assert_equals(fun4(18, 20, 60), 30)
Test.assert_equals(fun4(30, 10, 30), 15)
Test.assert_equals(fun4(30, 8, 24), 12)
#problem https://edabit.com/challenge/yvJbdkmKHvCNtcZy9 (3 point)
print('num5')
def fun5 (a):
    s=0
    n=len(str(a))
    r=a
    for i in range(n):
        y =a
        a = int(a / 10)
        s += ((y % 10)**(n-i))
    if s == r:
        return True
    return False
num_vector, res_vector = [
  [6, 75, 135, 466, 372, 175, 1, 696, 876, 89, 518, 598],
  [True, False, True, False, False, True, True, False, False, True, True, True]]
for j, n in enumerate(num_vector): Test.assert_equals(fun5(n), res_vector[j])