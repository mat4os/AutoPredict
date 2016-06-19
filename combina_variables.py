# Cálculo dominio variables
# Para todo x : X^2
# Para todo (x,y) =>
# (X-Y)/Y
# X + Y
# X*Y
# X/Y
# X-Y
data = {'A': [0.01, 0.03, 0.05, 0.07],
        'B': [2, 4, 6, 8],
        'C': [0.002, 0.004,0.006, 0.008],
        'D': [1, 3, 5, 7,]}
sample = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

print("Variable iniciales: " + str(len(sample.columns)))
contador_variables = 0
i = 0;
for x in range(0, len(sample.columns)-1):
    # x+y
    sample['var'+ str(contador_variables)] = sample.ix[:,x] + sample.ix[:,x+1]
    contador_variables = contador_variables +1
    # (x-y)/y
    sample['var'+ str(contador_variables)] = (sample.ix[:,x] - sample.ix[:,x+1])/sample.ix[:,x]
    contador_variables = contador_variables +1

    # x*y
    sample['var'+ str(contador_variables)] = sample.ix[:,x] * sample.ix[:,x+1]
    contador_variables = contador_variables +1

    # x/y
    sample['var'+ str(contador_variables)] = sample.ix[:,x] / sample.ix[:,x+1]
    contador_variables = contador_variables +1

    # x-y
    sample['var'+ str(contador_variables)] = sample.ix[:,x] - sample.ix[:,x+1]
    contador_variables = contador_variables +1

for x in range(0, len(sample.columns)):
    # x^2
    sample['var'+ str(contador_variables)] = sample.ix[:,x] * sample.ix[:,x]
    contador_variables = contador_variables +1

print("Variable finales: " + str(len(sample.columns)))

    


    
sample.head(4)

