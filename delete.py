import os

for i in os.listdir('./data/temp/'):
    os.remove('./data/temp/'+i)
    os.listdir('../dest/')