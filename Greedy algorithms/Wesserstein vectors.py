class vector():
    
    def __init__(self, values):
        self.values = [x for x in values]
    

    def take_from_forward(self, index):
        
        self.values[index] = self.values[index] + 1
        self.values[index+1] = self.values[index+1] - 1
        
        
    def give_to_forward(self, index):

        self.values[index] = self.values[index] - 1
        self.values[index+1] = self.values[index+1] + 1
    

def Wasserstein(v1, v2):
    
    if sum(v1.values) != sum(v2.values):
        print("Sums are not equivalent")
        return False
    
    for i in range(len(v1.values)-1):
       
        if v1.values[i] == v2.values[i]:
            continue
        
        while v1.values[i] > v2.values[i]:
            
            print('Oddajemy')
            
            v1.give_to_forward(i)
            
            if v1.values[i] == v2.values[i]:
                break
            else:
                continue
            
        while v1.values[i] < v2.values[i]:
            
            print('Kradniemy')
            
            v1.take_from_forward(i)

            
            if v1.values[i] == v2.values[i]:
                break
            else:
                continue  
    
    return v1,v2
    
    
    
    
    
    
#Testing -------------------------------------------
    
val_first_vector = [4,3,2,5]
val_second_vector = [4,3,3,4]

vect_1 = vector(val_first_vector)
vect_2 = vector(val_second_vector)


#vect_1.give_to_forward(1)
#vect_1.give_to_forward(1)
#vect_1.take_from_forward(2)
#vect_1.take_from_forward(3)
#print(vect_1.values)

wyniki = Wasserstein(vect_1, vect_2)

print(wyniki[0].values)
print(wyniki[1].values)











