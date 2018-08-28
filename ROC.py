
import numpy as np
np.set_printoptions(threshold=np.nan)

mi = np.matrix('0 1 0 1 0 0 1; 0 0 1 0 1 0 0; 1 1 0 1 0 0 1; 1 0 1 0 0 1 0; 0 0 1 1 1 1 0')

#switch the rows using the weight of each row calculated by the ROC algorithm formnulae
def switch_rows(matrix):
    weight ={}
    for i in range(matrix.shape[0]):
        sum1=0
        for j in range(matrix.shape[1]):
                sum1 += matrix[i,j]*(2**(matrix.shape[1]-j-1))
        weight[i]=sum1
    
    
    matrix = matrix[sorted(weight, key=weight.get,reverse=True)]
    return matrix

#switch the columns using the weight of each columns calculated by the ROC algorithm formnulae
def switch_columns(matrix):
    weight ={}
    for i in range(matrix.shape[1]):
         sum1=0
         for j in range(matrix.shape[0]):
                 sum1 += matrix[j,i]*(2**(matrix.shape[0]-j-1))
         weight[i]=sum1
    matrix = matrix[:,sorted(weight, key=weight.get,reverse=True)]
    return matrix

#apply the switch_rows and switch_columns in a matrix untill there's no difference between the switched and the original
def roc_algo(matrix):
    while True:
        copy=matrix
        matrix = switch_columns(switch_rows(matrix))
        if np.array_equal(matrix,copy)==True:
            return matrix
        
        

print(roc_algo(mi))



