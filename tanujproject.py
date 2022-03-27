#load all the required tools & LIBARY 
import time
import requests
import pandas as pd
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import plotly.express as px
from PIL import Image

#USE LOTTIE FUNCTION TO ANIMATE LOTTIES ON OUR WEBPAGE 

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#TOP OF PAGE 

st.set_page_config(page_title='TANUJ PROJECT' ,page_icon=":bar_chart:", layout="wide")
st.header('H-1B VISA APPROVAL')
st.subheader('PROJECT BY TANUJ')

#1ST LOTTIE HELLO FILE 

lottie_url_hello = "https://assets9.lottiefiles.com/packages/lf20_jrpzvtqz.json"
lottie_hello = load_lottieurl(lottie_url_hello)

st_lottie(lottie_hello, key="hello")

#2nd lottie file 
lottie_url_data = "https://assets4.lottiefiles.com/packages/lf20_4syqy0rw.json"
lottie_data = load_lottieurl(lottie_url_data)

st_lottie(lottie_data, key="data")





### --- LOAD DATAFRAME
# excel_file = r"C:\Users\ASUS--VIVOBOOK\Downloads\Tanuj_TechnolabSoftwareIntern_H1BVISA_Project\demofile.xlsx"
excel_file = "demofile.xlsx"
sheet_name = 'visa'


df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A:J',
                   nrows=1000,
                   header=3)

df_c = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='M:N',
                   header=3)
df_c.dropna(inplace=True)

df_v = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='P:Q',
                   header=3)
df_v.dropna(inplace=True)




st.dataframe(df)            
st.dataframe(df_c)
st.dataframe(df_v)



# --- STREAMLIT SELECTION
st.sidebar.header("Please Filter Here:")
visa = df['VISA_CLASS'].unique().tolist()


visa_selection = st.sidebar.multiselect('VISA_CLASS:',
                                    visa,
                                    default=visa)


h = df['H-1B_DEPENDENT'].unique().tolist()


h_selection = st.sidebar.multiselect('H-1B_DEPENDENT:',
                                    h,
                                    default=h)

soc = df['SOC_TITLE'].unique().tolist()


soc_selection = st.sidebar.multiselect('SOC_TITLE:',
                                    soc,
                                    default=soc)

will = df['WILLFUL_VIOLATOR'].unique().tolist()


will_selection = st.sidebar.multiselect('WILLFUL_VIOLATOR:',
                                    will,
                                    default=will)


master = df['MASTERS_EXEMPTION'].unique().tolist()


master_selection = st.sidebar.multiselect('MASTERS_EXEMPTION:',
                                    master,
                                    default=master)


position = df['FULL_TIME_POSITION'].unique().tolist()


position_selection = st.sidebar.multiselect('FULL_TIME_POSITION:',
                                    position,
                                    default=position)


emp = df['CONTINUED_EMPLOYMENT'].unique().tolist()

emp_selection = st.slider('CONTINUED_EMPLOYMENT:',
                        min_value= min(emp),
                        max_value= max(emp),
                        value=(min(emp),max(emp)))

status = df['CASE_STATUS'].unique().tolist()


status_selection = st.sidebar.multiselect('CASE_STATUS:',
                                    status,
                                    default=status)
                      

 #FILTER DATAFRAME BASED ON SELECTION
mask = (df['CONTINUED_EMPLOYMENT'].between(*emp_selection)) & (df['CASE_STATUS'].isin(status_selection))  & (df['FULL_TIME_POSITION'].isin(position_selection)) & (df['MASTERS_EXEMPTION'].isin(master_selection)) & (df['WILLFUL_VIOLATOR'].isin(will_selection))  & (df['H-1B_DEPENDENT'].isin(h_selection)) & (df['SOC_TITLE'].isin(soc_selection)) & (df['VISA_CLASS'].isin(visa_selection))
number_of_result = df[mask].shape[0]
st.markdown(f'*Available Results: {number_of_result}*')


# --- GROUP DATAFRAME AFTER SELECTION
df_grouped = df[mask].groupby(by=['CASE_STATUS','VISA_CLASS',]).count()

df_grouped = df_grouped.reset_index()

#PLOT IMAGE AND BARPLOT
col1, col2 = st.columns(2)
# image = Image.open(r"C:\Users\ASUS--VIVOBOOK\Downloads\Tanuj_TechnolabSoftwareIntern_H1BVISA_Project\h-1b visa image.jpg")
image = Image.open("h-1b visa image.jpg")
print(image)
col1.image(image,
        caption='PROJECT CREATOR TANUJ',
        use_column_width=True)
col2.dataframe(df[mask])

#3rd lottie file animation of animated visa 
lottie_url_visa = "https://assets7.lottiefiles.com/packages/lf20_tsmRqX.json"
lottie_visa = load_lottieurl(lottie_url_visa)

st_lottie(lottie_visa, key="visa")

#4th lottie show bar chart
lottie_url_show = "https://assets7.lottiefiles.com/private_files/lf30_0dui3jqg.json"
lottie_show = load_lottieurl(lottie_url_show)

st_lottie(lottie_show, key="show")



# --- PLOT BAR CHART
bar_chart = px.bar(df_grouped,
                   x='VISA_CLASS',
                   y='CASE_STATUS',
        
                   color_discrete_sequence = ['#F63366']*len(df_grouped),
                   template= 'plotly_white')
st.plotly_chart(bar_chart)



# --- PLOT PIE CHART
pie_chart = px.pie(df_c,
                title='ANALYSIS OF APPROVED STATUS',
                values='NUMBER OF APPROVED',
                names='CASES_STATUS')

st.plotly_chart(pie_chart)

pie_chart = px.pie(df_v,
                title='ANALYSIS OF VISA CLASS ',
                values='NUMBER OF APPLICANT',
                names='VISAS_CLASS')

st.plotly_chart(pie_chart)

#5th animated lottie file for passport 

lottie_url_passport = "https://assets10.lottiefiles.com/packages/lf20_8isnqscj.json"
lottie_passport = load_lottieurl(lottie_url_passport)

st_lottie(lottie_passport, key="passport")

#6th lottie animation of aeroplane 
lottie_url_air = "https://assets5.lottiefiles.com/packages/lf20_civw5ajz.json"
lottie_air = load_lottieurl(lottie_url_air)

st_lottie(lottie_air, key="air")

#7 animation of worlds tour 
lottie_url_tour = "https://assets5.lottiefiles.com/packages/lf20_ccdz2hzz.json"
lottie_tour = load_lottieurl(lottie_url_tour)

st_lottie(lottie_tour, key="tour")





#8th project ending thanksgiving note 
lottie_url_thanks = "https://assets10.lottiefiles.com/packages/lf20_j0qwy5q5.json"
lottie_thanks = load_lottieurl(lottie_url_thanks)

st_lottie(lottie_thanks, key="thanks")



