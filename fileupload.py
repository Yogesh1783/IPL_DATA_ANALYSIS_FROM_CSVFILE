import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
import numpy as np 
import pandas as pd

import seaborn as sns 
import matplotlib.pyplot as plt

# Plotly Libraris
import plotly.express as px
import plotly.graph_objects as go


import warnings
warnings.filterwarnings("ignore")

filename = ""

def UploadAction():
    global filename
    filename = askopenfilename()
    print('Selected:', filename)
    label1['text'] = filename.split('/')[len(filename.split('/'))-1]

def dataset():
    try:
        global team
        team=pd.read_excel(filename)
    except Exception as e:
        print(e)
        
    df=team.copy()
    print(df.head())
    print(df.info())

    print(df.shape)

    print(df.columns)

    print(df.describe().T)

    print(df.isnull().values.any())

    print(df.isnull().sum())

    print(df[df.duplicated() == True])
    
    df_team=df['TEAM'].value_counts().to_frame().reset_index().rename(columns={'index':'TEAM','TEAM':'Count'})

    fig = go.Figure(go.Bar(
        y=df_team['Count'],x=df_team['Count'],orientation="h",
    
        text=df_team['Count'],
        textposition = "outside",
    ))
    fig.update_layout(title_text='ipl MATCHES',xaxis_title="TEAM",yaxis_title="Count",title_x=0.5)
    fig.show()



root= tk.Tk()
root.title('IPL STATISTICAL REPORT')
root.geometry('1300x700')
img = ImageTk.PhotoImage(Image.open("C:\Yogesh\IPL_DATASET\photo.jpg"))


label2=tk.Label(text='INDIAN PRIMEIR LEAGUE DATA ANALYSIS',font=('verdana',14))
button1 = tk.Button(text='Select a File', command=UploadAction, bg='blue', fg='white',font=('verdana',14))
button2=tk.Button(text='Get Statistical Data',command=dataset,bg='blue',fg='white',font=('verdana',14))    
button3=tk.Button(text='Exit',command='',bg='blue',fg='white',font=('verdana',14))
button1.pack(padx=2, pady=5)
button1.place(x=575,y=460,height=50,width=200)
label1 = tk.Label(text='Select File',font=('verdana',14))
label1.pack(padx=2, pady=2)
label1.place(x=575,y=510,height=50,width=200)
button2.place(x=560,y=560,height=50,width=220)
button3.place(x=620,y=620,height=50,width=100)
label2.place(x=450,y=10,height=50,width=500)
label3=tk.Label(root,image=img)
label3.place(x=300,y=50,height=400,width=800)
root.mainloop()

