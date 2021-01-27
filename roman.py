def int_to_roman(num):
    num_tuple = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    roman_tuple = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    result = ""
     #遍歷所有的數字
    for i in range(len(num_tuple)):
            #如果數字比當前數字大，則羅馬數字中加上該數字對應的羅馬符號
        while num >= num_tuple[i]:
            result += roman_tuple[i]
            num -= num_tuple[i]

    return result

num = int(input('請輸入數字： '))
print(int_to_roman(num))