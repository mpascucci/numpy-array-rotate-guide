import numpy as np
from functools import partial

def html_color(t, colors):
    return f"<text style=color:{colors.get(str(t),'black')}>{t}</text>"

def get_colors(array):
    symbols = set(array.flatten())
    symbols=[str(x) for x in symbols]
    color_list=["black","blue","red","green","#b676b1","#82caaf","#75c0e0","#fecf6a","#39a275","#df1c44","#8F3985","#194a8d"]
    colors={}
    i=0
    for s in sorted(symbols):
        colors[s]=color_list[i]
        i=(i+1)%len(color_list)
    return colors

def asvolume(ndarray, color=True, html=True):
    """return a 2D perspective table representation of ndarray.
    if colors is True, identical items will be colored with same color.
    """
    a=ndarray
    assert(len(a.shape)==3), "Expected 3D array, got {}D".format(len(a.shape))
    i,j,k=a.shape
    space="&nbsp"
    nl="<br>"
    n=2
    
    if color:
        color_dict=get_colors(a)
        fmt=partial(html_color, colors=color_dict)
    else:
        fmt=lambda x:x
        
    s=""
    d=np.empty((j+i-1,k+i-1),dtype='<U99')
    d[:]=space
    for z in range(i):
        d[z:j+z,z:z+k]=a[z,:,:]
    
    s+="<table>"
    for y in range(j+i-1):
        s+="<tr style='padding:3px!'>"
        s+=space.join([f"<td style=padding:3px>{fmt(t)}</td>" for t in d[y,:]])           
        s+="</tr>"
    s+="</table>"
    return(s)