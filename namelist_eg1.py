bucket=[1,2,3,4,'cep','cec','ieee',4.5,6.7,12.6,10,20,30]
bucket2=[5,6,7,8,9.0,5.7,7.8,3.6,'arun',100,200,'anisha','aishu','parthiv']
listint=bucket[:4]+bucket[10:13]+bucket2[:4]+bucket2[9:11]
name=bucket[4:7]+bucket2[8:9]+bucket2[11:14]
listfloat=bucket[7:10]+bucket2[4:8]
listint.sort()
listfloat.sort()
print listint
print name
print listfloat
