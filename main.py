import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
from random import random

st.title('streamlit 超入門')

st.write('Displey Image')

img = Image.open('2022-05-26.png')
st.image(img,caption='screenShot',use_column_width=True)

st.write('DataFrame')

df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})

st.write(df)

st.dataframe(df.style.highlight_max(axis=0),width=100,height=100)   #dataframeは縦と横の大きさを指定できる
st.dataframe(df.style.highlight_max(axis=0))    #ハイライトを表示、axis=0で横、１で縦

st.table(df)     #動的な表を使いたいときは「dataframe」,静的な表を使いたいときは「table」


"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""    #マジックコマンドの使用


df1 = pd.DataFrame(
    np.random.rand(20,3),
    columns = ['a','b','c']
)

st.line_chart(df1)    #グラフの作製


df2 = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns = ['lat','lon']
)

st.map(df2)   #マップの表示


st.write('インタラクティブなウィジェット')

if st.checkbox('Show Image'):
    img = Image.open('2022-05-26.png')
    st.image(img,caption='screenShot',use_column_width=True)

option = st.selectbox(
    'あなたの好きな数字を選んでください',
    list(range(1,11))
)
'あなたの好きな数字は、', option,'です。'

text = st.text_input('あなたの趣味を入力してください')
'あなたの趣味：', text

condition = st.slider('あなたの今の調子は？',0,100,50)
'コンディション：', condition


st.write('レイアウトを整える')

#sidebarの使用

text1 = st.sidebar.text_input('好きな色は？')
'好きな色は', text1

condition1 = st.sidebar.slider('テンション',0,100,50)
'コンディション：', condition1

#2columnレイアウトにする
left_column,right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

#expanderの使用
expander = st.expander('問い合わせ1')
expander.write('回答１')
expander = st.expander('問い合わせ2')
expander.write('回答2')

#プログレスバーの表示
st.write('プログレスバーの表示')

if st.checkbox('start!!!'):
    latest_interation = st.empty()
    bar = st.progress(0)

    for i in range(100):
        latest_interation.text(f'Interation{i+1}')
        bar.progress(i+1)
        time.sleep(0.1)

    'Done!!'