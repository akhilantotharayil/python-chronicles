'''List--> data structure which can hold multiple values of  ltiple type
    array --> data structure  which can hold multiple values of same type'''

list_of_cloud=["AWS","Azure","GCP","digital ocean","utho","alibaba","oracle"]
cloud = "GCP" #variable

print(list_of_cloud)

#add a new cloud Salesforce

list_of_cloud.append("Akhil's_Salesforce")

#add a new cloud IBM

list_of_cloud.append("IBM")

print(list_of_cloud)

list_of_cloud.insert(2,"Heraku")

print(list_of_cloud)

#Insert Hello Cloud to 0th index of  list
list_of_cloud.insert(0,"CLOUD")

print(list_of_cloud)

#Iteration of a list
for cloud in list_of_cloud:
    print(" ")
    print(cloud)


for i in range(1,11):
    print(i)
