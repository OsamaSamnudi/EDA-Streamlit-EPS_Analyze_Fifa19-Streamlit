import streamlit as st
# st.cache_resource()
st.set_page_config(
        layout = 'wide',
        page_title = 'EDA FIFA 201',
        page_icon= '📊')
# ______________________________________________________________________________________________________________________________________________________________________________________________________
# Import Libraries
import streamlit as st
import plotly.express as px
import pandas as pd

# with st.container():
About = st.sidebar.checkbox(":blue[Show About FIFA 2019]")
Planning = st.sidebar.checkbox(":orange[Show About Application]")
About_me = st.sidebar.checkbox(":green[Show About me]")
if About:
    st.sidebar.header(":blue[About EDA & Application Info]")
    st.sidebar.write("""
    * :blue[*id:*] The player's unique identifier.
    * :blue[*name:*] The player's name.
    * :blue[*age:*] The player's age.
    * :blue[*nationality:*] The player's nationality.
    * :blue[*overall:*] The player's overall rating. This is a measure of the player's overall ability.
    * :blue[*potential:*] The player's potential rating. This is a measure of the player's potential ability.
    * :blue[*club:*] The player's club.
    * :blue[*value:*] The player's market value. This is the estimated value of the player in terms of transfer fees.
    * :blue[*wage:*] The player's weekly wage.
    * :blue[*preferred foot:*] The player's preferred foot. This is the foot that the player prefers to use when shooting, passing, and dribbling.
    * :blue[*international reputation:*] The player's international reputation. This is a measure of the player's popularity and recognition outside of their home country.
    * :blue[*skill moves:*] The number of skill moves that the player can perform.
    * :blue[*position:*] The player's position on the field.
    * :blue[*joined:*] The date that the player joined their current club.
    * :blue[*contract valid until:*] The date that the player's contract expires.
    * :blue[*height:*] The player's height in meters.
    * :blue[*weight:*] The player's weight in kilograms.
    * :blue[*release clause:*] The player's release clause. This is the amount of money that a club must pay to sign the player from their current club.
    * :red[So let us see the insights 👀]
    """)
# ______________________________________________________________________________________________________________________________________________________________________________________________________
if Planning :
    st.sidebar.header(":orange[Application Planning]")
    st.sidebar.write("""
    * 1) Year Over Year :
        * Bar Plot :
            * joined , nationality , club , preferred foot , skill moves , position
            * age , overall , potential , value , international reputation	 , weight , height
        * Line Plot :
            * value , release_clause_log
    * 2) Top 10 Nationalities :
        * Top 10 : 
            * joined , club , skill moves
            * overall , potential , value , international reputation , weight , height
    
    * 3) Top 10 Clubs :
        * Top 10:
            * joined , club , skill moves
            * overall , potential , value , international reputation , weight , height
    """)
# ______________________________________________________________________________________________________________________________________________________________________________________________________
if About_me :
    st.sidebar.header(":green[About me]")
    st.sidebar.write("""
    - Osama SAAD
    - Student Data Scaience & Machine Learning @ Epsilon AI
    - Infor ERP Consaltant @ Ibnsina Pharma
    - Email : osamasamnudi86@gamil.com
    - LinkedIn: 
        https://www.linkedin.com/in/ossama-ahmed-saad-525785b2
    - Github : 
        https://github.com/OsamaSamnudi
    """)
# "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
# Make 3 Tabs (Year Over Year 📈 YoY ↗️ , Top 10 Nationalities 🏆 , Top 10 Clubs 🎖️)
Data_Info , YoY , Nat_club = st.tabs (['Data Information 💾' , 'Year Over Year 📈 YoY ↗️' , 'Top 10 Nationalities 🏆 and Clubs 🎖️'])

pd.options.display.float_format = '{:,.2f}'.format
df = pd.read_csv('fifa_eda v1.csv', index_col=0 )

with Data_Info:
    # st.cache_resource()
    with st.container():
        st.header("Data Describe")
        DI_select = st.selectbox('Please select:',['Please select','All Columns' , 'Categorical' , 'Numerical' , 'custom'])
        if DI_select == 'Please select':
            st.write(":red[Please Choise a column from the list:]")
        elif DI_select == 'All Columns':
            st.write(":violet[Describe Table (All Columns):]")
            st.dataframe(data=df.describe().T , use_container_width=True)
        elif DI_select == 'Numerical':
            st.write(":orange[*Describe Table (All Numerical):*]")
            st.dataframe(data=df.describe(exclude = ['object']).T , use_container_width=True)
        elif DI_select == 'Categorical':
            st.write(":orange[*Describe Table (All Categorical):*]")
            st.dataframe(data=df.describe(include = ['object']).T , use_container_width=True)
        else:
            columns = st.selectbox('Please select:',df.columns.tolist())
            st.write(":orange[*Describe Table for :*]",columns)
            st.dataframe(data=df[columns].describe(), use_container_width=True)

    with st.container():
        pd.options.display.float_format = '{:,.0f}'.format
        st.header("Data Information")
        DataInfo = st.checkbox("Show Data Info")
        if DataInfo :
            st.dataframe(data=df.dtypes.reset_index(name='Type'), hide_index=True, use_container_width=True)
            
    with st.container():
        st.subheader('Heatmap Corrolation')
        corrolation = st.checkbox('Show Corrolations')
        if corrolation :
            cor = df.select_dtypes(exclude='object').corr()
            fig_corr = px.imshow(cor , text_auto=True , width= 1500 , height= 1500  , color_continuous_scale='tropic')
            st.plotly_chart(fig_corr,use_container_width=True,theme="streamlit")
# "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
with YoY:
    with st.container():
        st.subheader('Year Over Year (Bar Plot)')
        lst = ['Please select','age','overall','potential','value','value_log','release clause','release_clause_log','wage', 'weight','height']
        lst_select = st.selectbox("YoY Analysis" , lst)
        st.subheader('bar Plot/Count')
        if lst_select == 'Please select':
            st.write(":red[Please Choise a column from the list:]")
        else:
            msk = df.groupby(['joined'])[lst_select].mean().reset_index(name='count')
            fig = px.bar(msk, x = 'joined', y = 'count'  , text_auto=True)
            st.plotly_chart(fig,use_container_width=True)
        
    with st.container():
        st.subheader('Year Over Year (Line Plot)')
        lst_1 = ['Please select','age' , 'value' , 'release clause']
        lst_select_1 = st.selectbox("YoY Analysis" , lst_1)
        if lst_select_1 == 'Please select':
            st.write(":red[Please Choise a column from the list:]")
        else:
            msk_2 = df.groupby(['joined'])[lst_select_1].mean().reset_index()
            fig_2 = px.line(msk_2 , x= 'joined' , y=lst_select_1 ,color_discrete_sequence=['red'] , line_shape='spline')
            st.plotly_chart(fig_2,use_container_width=True)

with Nat_club:
    with st.container():
        st.subheader('Nationality Analysis (Bar Plot)')
        cat_columns_2 = ['Please select','value','value_log','release clause','release_clause_log','wage', 'weight','height']
        col1_select_2 = st.selectbox("Nationality Analysis" , cat_columns_2)
        if col1_select_2 == 'Please select':
            st.write(":red[Please Choise a column from the list:]")
        else:
            msk_2 = df.groupby(['nationality'])[col1_select_2].mean().nlargest(10).sort_values().reset_index(name='count')
            fig_2 = px.bar(msk_2, x = 'nationality', y = 'count' , text_auto=True , color_discrete_sequence = px.colors.qualitative.Plotly_r)
            st.plotly_chart(fig_2,use_container_width=True)

    with st.container():
        st.subheader('Club Analysis (Bar Plot)')
        cat_columns_3 = ['Please select','value','value_log','release clause','release_clause_log','wage', 'weight','height']
        col1_select_3 = st.selectbox("Club Analysis" , cat_columns_3)
        if col1_select_2 == 'Please select':
            st.write(":red[Please Choise a column from the list:]")
        else:
            msk_3 = df.groupby(['club'])[col1_select_3].mean().nlargest(10).sort_values().reset_index(name='count')
            fig_3 = px.bar(msk_3, x = 'club', y = 'count' , text_auto=True , color_discrete_sequence = px.colors.qualitative.Pastel1)
            st.plotly_chart(fig_3,use_container_width=True)
