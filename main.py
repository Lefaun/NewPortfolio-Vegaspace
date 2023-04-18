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
selected2 = option_menu(None, ["Home", "About Me", "Art", "Design", "Video", "3D", "IoT", "Graphics"],
    icons=None,
    default_index=0, orientation="horizontal")

    # 1. as sidebar menu
with st.sidebar:
    st.image('Me.jpg', width=300
             ,)
    selected = option_menu("Meu Menu", (["Home", 'VIdeo', 'Design 1', 'Dashboard2']),menu_icon="cast", default_index=1, )
                        #icons=['house', 'gear'],

# Create the responsive menu

def display_menu():
    menu = ["Home", "About", "Art", "Design", "Video", "3D", "IoT", "Graphics"]
    choice = st.selectbox("Select an option", menu)
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
            st.video("https://youtu.be/ZfxPMMzyeX8")

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
    elif choice == "3D Games ":
        st.title("Exemple de Pequeno Jogo em Python e Blender")
        st.write("Jogo 3D em UPBGE")

        components.iframe("https://cdn.soft8soft.com/AROAJSY2GOEHMOFUVPIOE:85cf9c6521/Sub%20Python%20Game/Sub%20Python%20Game.html")
       
   

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
        col1, col2, col3 = st.columns(3)

        with col1:
            st.header("Video")
            st.image("Cutscene Final.mp4")
            button_1 = st.button("Gosto", key="sictemic")
        with col2:
            st.header("Design")
            st.image("Portfolio/2.png")

            button_2 = st.button("Gosto", key="asian")
        with col3:
            st.header("3D ART")
            st.image("Carrinha.jpeg")
            button_3 = st.button("Gosto", key="cutr ")

        st.title("Cartoon")
        st.write("Galeria de Criações e Desenho")
        st.image("Drwaing.jpeg")
        st.image("Paulo_Image.png")
        st.image("3.png")
    elif choice == "IoT":
        st.title("Projetos Dashboarding e Data Science")
        st.write("Criação de Dashboarding e Infografias para Data Science .")
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

