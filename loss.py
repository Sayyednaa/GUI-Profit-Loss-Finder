def loss(CP,SP):
    Result=(int(SP)-int(CP))
  
    res=(int(Result)/int(CP)*100)
    
    final=(f'Loss Of {Result} and {res}%')
    return final