#print("hello world")

def findMyCar(cars,find):
    for car in cars:
        if car == find:
            print ("hey i found you car "+ find)
        else:
            print("Oops Car not found, Try other car.")    
                
cars=["ford","honda","hyundai","bmw","maruthi","maserati","hummer"]
findMyCar(cars,"hummer")