def clean_list(list_):
    '''
    This function clean the list from html format
    '''
    result=[]
    for item in list_:  
        v1=item.find('>')
        v2=item.find('<',2)
        result.append(item[v1+1:v2])
    return result

def clean_list_url(list_):
    '''
    This function clean the list to to get the https
    '''
    result=[]
    for item in list_:  
        v1=item.find('href=')
        v2=item.find('>')
        item=item[v1+5:v2]
        item=item.replace("\"","")
        result.append(item)
    return result