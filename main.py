words = {
    3:'Fizz',
    5:'Buzz'
}

for num in range(1,101):
    output = ''
    for div in words:
        output+=words[div]*int(not bool(num%div))
    output = str(num)*int(bool(output == ''))+(output*int(bool(output != '')))
    print(output)