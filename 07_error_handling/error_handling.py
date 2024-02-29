file = open('youtube.txt', 'w')


# we can handle files in two ways :
# 1=>
try:
    file.write('chai aur code')
finally:
    file.close()

# 2=>
with open('youtube.txt', 'w') as file:
    file.write('chai aur python')