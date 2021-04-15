N  =int(input("\n"))

remaining = N % 100 

note100 = int(N / 100)
note50 = int(remaining/50)
note10 = int(((remaining)%50) / 10)
note5 = int((((remaining)%50) % 10) / 5)
note2 = int(((((remaining)%50) % 10) % 5)/2)
note1 = int(((((remaining)%50) % 10) % 5)%2)

print(note100 + note50 + note10 + note5 + note2 + note1)