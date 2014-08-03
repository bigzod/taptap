zone1=[4323454,226545643,34765757,57874266,23726464]
zone2=[2367576,986564654,47464796,49797876,63878676,38765412]
zone3=[3874541,687454638,74685413,74835432,37473465,37574354,87734548,37838786]
territoire=[zone1,zone2,zone3]
input=("saisissez votre zone")
liste=[]
def taptap_search(territoire):
    liste.append(territoire)
    for n in input:
        if n in liste:      
            s=liste.find(n)
        else:
            break
    return (liste)
print (taptap_search(zone1))

occupied=[4323454,34765757]
def number_search(zone1):
    v=(zone1[0])
    for v in zone1:
        if v in occupied:
            pass
        else:
            print (v)
print (number_search(zone1))

proche=[]
nearest=[226545643,57874266]
def proche_search(zone1):
    proche.append(number_search(zone1))
    for n in proche:
        if n in nearest:
            print (n)
        else:
            break
    return n
print (proche_search(nearest))
        
    
