from streamlit_option_menu import option_menu
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib as plt
import base64
from collections import Counter
import streamlit.components.v1 as components

main_bg = "lightgreen.jpeg"
main_bg_ext = "jpeg"

side_bg = "lightgreen.jpeg"
side_bg_ext = "jpeg"
video_html = open("human.mp4", 'rb').read()
color_bgg ="#f0f0f0"
opacity_bg = 0.6
mask = 'untitled.png' # path to your mask image
mask_width = 1920 # the width of your mask image
autoplay="true" # For autoplay
muted="true" # For mute
loop="true" # For Loop


st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
   .sidebar .sidebar-content {{
        background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)
display_images=[ {"name": "2.png", "likes": 0},{"Video": "3.png", "likes": 0},{"name": "Sonia <Monteiro Imobiliary.png", "likes": 0},{"Design": "star.png", "likes": 0}]

# Create an empty dictionary to store the number of likes per day of the week
likes_per_day = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
days_of_week = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}


days_of_week = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

# Create a list to store the likes per day of the week
likes_per_day = [0, 0, 0, 0, 0, 0, 0]

# Create a list to store the date of the like
date_likes = []

now=[]
# Create a function to display the histogram of likes per day of the week
st.title("                        O MEU PORTFOLIO")

def main():
    st.set_page_config(page_title="O MEU PORTEFOLIO", page_icon=":guardsman:", layout="centered")

    # 2. horizontal menu



    # 1. as sidebar menu
with st.sidebar:
    st.image('Me.jpg', width=300
             ,)
    selected = option_menu("Meu Menu", (["Home", 'VIdeo', 'Design 1', 'Dashboard2']),menu_icon="cast", default_index=1, )
                        #icons=['house', 'gear'],

# Create the responsive menu

def display_menu():
    
    
    #menu = ["Home", "About", "Art", "Design", "Video", "3D Games", "3D","IoT", "Graphics"]
    #choice = st.selectbox("Select an option", menu)
    
    choice = option_menu(None, ["Home", "About", "Art", "Design", "Video", "3D Games","3D","IoT", "Graphics"],
    icons=None,
    default_index=0, orientation="horizontal",)
    
    
    if choice == "Home":
        st.title("Welcome to My Gallery")
        st.write("Este é um exemplo de alguns projetos de 3D / web design / Design Gráfico e Video")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.header("Video")
            st.video("video1.mp4")
            button_1 = st.button("Gosto", key="abnormal")
        with col2:
            st.header("Design")
            st.image("image2.jpg")

            button_2 = st.button("Gosto", key="cool")
        with col3:
            st.header("3D Design")
            st.image("i love Summer.jpg")
            button_3 = st.button("Gosto", key="psy ")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.header("AI Art")
            st.image("3.png")
            button_1 = st.button("Gosto", key="sictemic")
        with col2:
            st.header("3D Animation")
            st.image("image5.jpeg")

            button_2 = st.button("Gosto", key="asian")
        with col3:
            st.header("Web Design")
            st.image("artesideias.gif")
            button_3 = st.button("Gosto", key="cutr ")
    elif choice == "About":
        st.title("About Me")
        st.write("O meu Nome é Paulo Ricardo Monteiro, formado em 2008 em Audiovisual e Multimédia, Actualmente formei-me com o mestrado em Engenharia Infromática - área de Multimedia"
                 "Tendo defendido a minha Tese no âmbito dos sistemas de Realidade Virtual e Realidade Aumentada para os Setores Museológicos e da Arte Digital")
        st.image('Me.jpg', width=300)

        def show_pdf(file_path):
            with open("CV - Paulo Monteiro - Mestrado 2022.pdf", "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

        show_pdf('CV - Paulo Monteiro - Mestrado 2022.pdf')
        st.title("Tese de Mestrado")
        components.iframe("https://flipbookpdf.net/web/site/11654bc27d8dbcd2cb769695cf3f88addc709f1c202305.pdf.html", width=750, height =600)
    elif choice == "3D Games":
        st.title("Exemple de Pequeno Jogo em Python e Blender")
        st.write("Jogo 3D em UPBGE")

        components.iframe("https://cdn.soft8soft.com/AROAJSY2GOEHMOFUVPIOE:85cf9c6521/Sub%20Python%20Game/Sub%20Python%20Game.html", width=750, height =600)
        st.video("https://youtu.be/ZfxPMMzyeX8")
       
    elif choice =="Art":
        st.video("human.mp4")
        video_html = f'''
        
        <video controls width="650" autoplay="true" muted="true" loop="true">
            <source 
            src="human.mp4" 
            type="video/mp4" />
        </video>
       '''
        
        st.markdown(video_html, unsafe_allow_html=True)
        mask = f'''
    <div style="position: absolute; bottom: 0; left: 0; width: 100%; height: {mask_width/2}px;">
        <img style="width: 100%; height: 100%; object-fit: cover;" src="{mask}">
    </div>
</div>

<div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">
    <h1 style="color: white; background: rgba(0, 0, 0, 0.5); padding: 10px;">I´m A Human and a Keep in Mind all The World´s Dream</h1>
</div>
'''

        st.markdown(mask, unsafe_allow_html=True)
    elif choice == "Video":
        st.title("Video - Reportagem Fura Dels Bhaus")
        st.write("O meu nome é Paulo Monteiro, e tenho interesse na realização de Videos e Curtas de animação e Reportagens .")
        st.video("https://www.youtube.com/watch?v=aT1X9w1yMwE&list=PLqUL-W6mtUu5dradixC0MJ9B46RZi6IhK&index=13")
        st.title("Video - Clip Sam the Kid - O RECADO ")
        st.write(
            "|Projeto Video  CLIP | o RECADO - SAM the Kid")
        st.video("SAM_THE_KID.mp4")
    elif choice == "3D":
        st.title("3D Gallery")
        st.write("Galeria de Criações 3D")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.header("Video")
            st.image("3.png")
            button_1 = st.button("Gosto", key="abnormal")
        with col2:
            st.header("Design")
            st.image("2.png")

            button_2 = st.button("Gosto", key="cool")
        with col3:
            st.header("3D ART")
            st.image("Carrinha.jpeg")
            button_3 = st.button("Gosto", key="psy ")
        col1, col2 = st.columns(2)
            
        with col1:
            st.header("Design")
            st.image("2.png")

            button_2 = st.button("Gosto", key="asian")
        with col2:
            st.header("3D ART")
            st.image("Carrinha.jpeg")
            button_3 = st.button("Gosto", key="cutr ")
       
            
        st.title("Video")
        st.video("Cutscene Final.mp4")
        button_1 = st.button("Gosto", key="sictemic")


        st.title("Cartoon")
        st.write("Galeria de Criações e Desenho")
        st.image("Drwaing.jpeg")
        st.image("Paulo_Image.PNG")
        st.image("3.png")
    elif choice == "IoT":
        st.title("Projetos Dashboarding e Data Science")
        st.write("Criação de Dashboarding e Infografias para Data Science .")
        import pandas as pd
        import streamlit as st
        import numpy as np
        import plotly.figure_factory as ff
        import plotly.figure_factory as px
        import plotly.figure_factory as line
        from pandas.api.types import (
            is_categorical_dtype,
            is_datetime64_any_dtype,
            is_numeric_dtype,
            is_object_dtype,
        )

        st.title("Esatisticas da Saúde Mental no Período de 2004 a 2020 ")

        st.write(
            """Estudo Efetuado pelo INE - Instiituto Nacional de Estatística sobre o estado da Saúde Mental dos Portugueses 
            divídidos por Género, Faixa Étaria e Ocupação Profissional
            """
        )
        def filter_data(df: pd.DataFrame) ->pd.DataFrame:
            options = st.multiselect("escolha a Cena ", options=df.columns)
            st.write('Voçê selecionou as seguintes opções', options)

        def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
            """
            Adds a UI on top of a dataframe to let viewers filter columns
            Args:
                df (pd.DataFrame): Original dataframe
            Returns:
                pd.DataFrame: Filtered dataframe
            """

            modify = st.text_input(
                "Escolha os Fatores 👇", df.columns,
                #label_visibility=st.session_state.visibility,
                #disabled=st.session_state.disabled,
                #placeholder=st.session_state.placeholder,

            )
            if not modify:
                return df

            df = df.copy()

            # Try to convert datetimes into a standard format (datetime, no timezone)
            for col in df.columns:
                if is_object_dtype(df[col]):
                    try:
                        df[col] = pd.to_datetime(df[col])
                    except Exception:
                        pass

                if is_datetime64_any_dtype(df[col]):
                    df[col] = df[col].dt.tz_localize(None)

            modification_container = st.container()

            with modification_container:
                to_filter_columns = st.multiselect("Filter dataframe on", df.columns)
                for column in to_filter_columns:
                    left, right = st.columns((1, 20))
                    left.write("↳")
                    # Treat columns with < 10 unique values as categorical
                    if is_categorical_dtype(df[column]) or df[column].nunique() < 10:
                        user_cat_input = right.multiselect(
                            f"Values for {column}",
                            df[column].unique(),
                            default=list(df[column].unique()),
                        )
                        df = df[df[column].isin(user_cat_input)]
                    elif is_numeric_dtype(df[column]):
                        _min = float(df[column].min())
                        _max = float(df[column].max())
                        step = (_max - _min) / 100
                        user_num_input = right.slider(
                            f"Values for {column}",
                            _min,
                            _max,
                            (_min, _max),
                            step=step,
                        )
                        df = df[df[column].between(*user_num_input)]
                    elif is_datetime64_any_dtype(df[column]):
                        user_date_input = right.date_input(
                            f"Values for {column}",
                            value=(
                                df[column].min(),
                                df[column].max(),
                            ),
                        )
                        if len(user_date_input) == 2:
                            user_date_input = tuple(map(pd.to_datetime, user_date_input))
                            start_date, end_date = user_date_input
                            df = df.loc[df[column].between(start_date, end_date)]
                    else:
                        user_text_input = right.text_input(
                            f"Substring or regex in {column}",
                        )
                        if user_text_input:
                            df = df[df[column].str.contains(user_text_input)]

            return df

            def filter_dataframe2(df: pd.DataFrame) -> pd.DataFrame:
                """
                Adds a UI on top of a dataframe to let viewers filter columns
                Args:
                    df (pd.DataFrame): Original dataframe
                Returns:
                    pd.DataFrame: Filtered dataframe
                """
                modify2 = st.text_input(
                    "Escolha os Fatores 👇",
                    #label_visibility=st.session_state.visibility,
                    #disabled=st.session_state.disabled,
                    #placeholder=st.session_state.placeholder,
                )

                if not modify2:
                    return df

                df = df.copy()

                # Try to convert datetimes into a standard format (datetime, no timezone)
                for col in df.columns:
                    if is_object_dtype(df[col]):
                        try:
                            df[col] = pd.to_datetime(df[col])
                        except Exception:
                            pass

                    if is_datetime64_any_dtype(df[col]):
                        df[col] = df[col].dt.tz_localize(None)

                modification_container = st.container()

                with modification_container:
                    to_filter_columns = st.multiselect("Selecione os Riscos", df.columns)
                    for column in to_filter_columns:
                        left, right = st.columns((1, 20))
                        left.write("↳")
                        # Treat columns with < 10 unique values as categorical
                        if is_categorical_dtype(df[column]) or df[column].nunique() < 10:
                            user_cat_input = right.multiselect(
                                f"Values for {column}",
                                df[column].unique(),
                                default=list(df[column].unique()),
                            )
                            df = df[df[column].isin(user_cat_input)]
                        elif is_numeric_dtype(df[column]):
                            _min = float(df[column].min())
                            _max = float(df[column].max())
                            step = (_max - _min) / 100
                            user_num_input = right.slider(
                                f"Values for {column}",
                                _min,
                                _max,
                                (_min, _max),
                                step=step,
                            )
                            df = df[df[column].between(*user_num_input)]
                        elif is_datetime64_any_dtype(df[column]):
                            user_date_input = right.date_input(
                                f"Values for {column}",
                                value=(
                                    df[column].min(),
                                    df[column].max(),
                                ),
                            )
                            if len(user_date_input) == 2:
                                user_date_input = tuple(map(pd.to_datetime, user_date_input))
                                start_date, end_date = user_date_input
                                df = df.loc[df[column].between(start_date, end_date)]
                        else:
                            user_text_input = right.text_input(
                                f"Substring or regex in {column}",
                            )
                            if user_text_input:
                                df = df[df[column].str.contains(user_text_input)]

                return df

            #df = pd.read_csv(
                #"MentalHealth.csv"
            #)
            #st.dataframe(filter_dataframe(df))

            df = pd.read_csv(
                "Mentalhealth3.csv"
            )

            st.dataframe(filter_dataframe2(df))

            chart_data = pd.DataFrame(
                np.random.randn( 22 , 5),
                columns=['Mulheres', 'Homens', 'Ensino Superior', 'Desempregados', 'Reformados' ])


                #column2=['25','50','75', '80', '100']
            st.area_chart(chart_data)

            # Example dataframe
            df = pd.read_csv('Mentalhealth3.csv')

            # plot
            st.area_chart(data = df, x= "Date1",y='Total')



            chart_data = pd.DataFrame(
                np.random.randn( 2 , 5),
                {

                'Date1': [2004,2008,2010,2015,2022],
                'columns':['Mulheres', 'Homens', 'Ensino Superior', 'Desempregados', 'Reformados' ] })


                #column2=['25','50','75', '80', '100']
            st.area_chart(chart_data)

            df = pd.read_csv('Mentalhealth3.csv')
            st.area_chart( df, x="Date1", y='Total')

            df = pd.DataFrame(
                {"Date1": [2008, 2011, 2018, 2020], "values": [0, 25, 50, 75], "values_2": [15, 25, 45, 85]}

            ).set_index("Date1")

            df_new = pd.DataFrame(
                {"steps": [4, 5, 6], "Homens": [0.5, 0.3, 0.5], "Mulheres": [0.8, 0.5, 0.3]}
            ).set_index("steps")

            df_all = pd.concat([df, df_new], axis=0)
            st.line_chart(chart_data, x=df.all,)
            #st.line_chart(df, x=df.index, y=["Homens", "Mulheres"])







            # Add histogram data
            x1 = np.random.randn(200) - 2
            x2 = np.random.randn(200)
            x3 = np.random.randn(200) + 2

            # Group data together
            hist_data = [x1, x2, x3]

            group_labels = ['Homens', 'Mulheres', 'Ensino superior']

            # Create distplot with custom bin_size
            fig = ff.create_distplot(
                    hist_data, group_labels, bin_size=[2008, 2010, 2020])

            # Plot!
            st.plotly_chart(fig, use_container_width=True)

            import streamlit as st
            import streamlit.components.v1 as components
            p = open("lda.html")
            components.html(p.read(), width=1000, height=800, )

            chart_data = pd.read_csv('Topicosbem.csv', sep=',')
            # Work with the dataframe
            st.dataframe(chart_data.head(15))
            columns = (['Length', 'Height', 'Width', 'Frequency', 'Word', ])

            chart_data = pd.DataFrame(
                np.random.randn(20, 5),
                columns=['Length', 'Height', 'Width', 'Frequency', 'Word'])
            st.bar_chart(chart_data)

            chart_data = pd.DataFrame(
                np.random.randn(20, 5),
                columns=['Length', 'Height', 'Width', 'Frequency', 'Word'])

            c = alt.Chart(chart_data).mark_circle().encode(
                x='Length', y='Frequency', size='Height', color='Word',
                tooltip=['Length', 'Height', 'Width', 'Frequency', 'Word'])

            st.altair_chart(c, use_container_width=True)


    elif choice == "Graphics":
        st.title("Graphics And Design ")
        st.write("Neste espaço está um exemplo de projetos de WEb Graphics and Design")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.header("Design Gráfico")
            st.image("i love Summer.jpg")
            button_1 = st.button("Gosto", key="abnormal3")
        with col2:
            st.header("Design")
            st.image("2.png")

            button_2 = st.button("Gosto", key="cool")
        with col3:
            st.header("3D Models")
            st.image("Carrinha.jpeg")
            button_3 = st.button("Gosto", key="psy ")
    elif choice == 'Dashboard 1':
        st.title('Dashboard 1')
        volume = [350, 220, 170, 150, 50]
        labels = ['Liquid\n volume: 350k', 'Savoury\n volume: 220k',
        'Sugar\n volume: 170k', 'Frozen\n volume: 150k',
        'Non-food\n volume: 50k']
        color_list = ['#0f7216', '#b2790c', '#ffe9a3',
        '#f9d4d4', '#d35158', '#ea3033']

        plt.rc('font', size=14)
        squarify.plot(sizes=volume, label=labels,
        color=color_list, alpha=0.7)
        plt.axis('off')
        st.pyplot()
display_menu()

