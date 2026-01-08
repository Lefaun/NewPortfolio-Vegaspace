from streamlit_option_menu import option_menu
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib as plt
import base64
from collections import Counter
import streamlit.components.v1 as components
import pandas as pd
import streamlit as st
import smtplib
import numpy as np
import plotly.figure_factory as ff
import plotly.figure_factory as px
import plotly.figure_factory as line
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,)
from datasets import (filter_data, filter_dataframe)
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet_v2 import ResNet50V2, preprocess_input, decode_predictions
import numpy as np
import pandas as pd
import csv
###########################
st.set_page_config(
    page_title="Le Faun's Portfolio",
    layout="wide"
)

# Define the CSS to hide Streamlit UI elements and set the background iframe
custom_css = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp {
        background: transparent;
    }
    .background {
        position: fixed;
        top: 0;
        left: 0;
        height: 100%;
        width: 100%;
        z-index: -1;
        overflow: hidden;
    }
    .foreground {
        position: relative;
        z-index: 1;
    }
    .iframe {
        position: fixed;
        top: 0;
        left: 0;
        height: 100%;
        width: 100%;
        border: none;
        z-index: -1;
    }
    @media (max-width:768px) {
        .foreground {
            padding: 10px;
            align-items: center;
            color: white;
        }
    }
    .stApp {
        foreground: orange;
    }
    </style>
"""

# HTML to embed the OpenProcessing iframe
openprocessing_iframe = """
    <div class="background">
        <iframe src="https://openprocessing.org/sketch/2257597/embed/" width="100%" height="100%"></iframe>
    </div>
"""

# Inject the CSS and HTML into the Streamlit app
st.markdown(custom_css, unsafe_allow_html=True)
st.markdown(openprocessing_iframe, unsafe_allow_html=True)

# Wrap your Streamlit content inside a div with the 'foreground' class
st.markdown('<div class="foreground">', unsafe_allow_html=True)

################################################




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


#st.markdown(
   # f"""
    #<style>
   # .reportview-container {{
    #    background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    #}}
   #.sidebar .sidebar-content {{
     #   background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})
   # }}
   # </style>
   # """,
   # unsafe_allow_html=True
#)
display_images=[ {"name": "video1.mp4", "path":"video1.mp4",  "likes": 0},{"Video": "3.png", "likes": 0},{"name": "Sonia <Monteiro Imobiliary.png", "likes": 0},{"Design": "star.png", "likes": 0}]

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
def send_mail(email, subject, message):
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        username = 'maillefaun@gmail.com'
        password = 'qftabgvjolpfjniw'
        server.login(username, password)
        to_email = 'maillefaun@gmail.com'
        server.sendmail(username, to_email, mensagem)
        
        server.close()
    except Exception as e:
        st.error(f' Ocorreu um Erro ao enviar o e-mail, Desculpe: {e}')

    # 1. as sidebar menu
with st.sidebar:
   
    st.image('Me.png', width=300,)

    selected = option_menu("Meu Menu", (["Home", 'VIdeo', 'Contacte Me']),menu_icon="cast", default_index=1, )

              #icons=['house', 'gear'],

    if selected == 'Contacte Me':
        
        email_form = st.form(key='my_email_form', clear_on_submit=False)
        email = email_form.text_input(label='Por Favor Escreva o Seu Endereço de e-mail')
        
        subject = email_form.text_input (label = ' Escreva aqui o Assunto ' )
        message = email_form.text_area (label = ' Escreva a sua Mensagem ')
            
        if email_form.form_submit_button(label=' Enviar '):
            mensagem = f'Subject:{subject}\n\n De: {email}\n\n Assunto: {message}'.encode('utf-8')
            send_mail(email, subject, message)
            st.subheader('  Mensagem enviada com Sucesso!') 
                    
            # Create the responsive menu

def display_menu():
    
    
    menu = ["Home", "About", "Art", "Architecture", "Video", "3D Games", "3D","IoT", "Graphics", "IMAGE - Classifier APP"]
    #choice = st.selectbox("Select an option", menu)
    
    choice = option_menu(None, ["Home", "About", "Art", "Architecture", "Video", "3D Games","3D","IoT", "Graphics", "IMAGE - Classifier APP"],
    icons=None,
    default_index=0, orientation="horizontal",)
    
    
    if choice == "Home":
        st.title("Welcome to My Gallery")
        st.write("Este é um exemplo de alguns projetos de 3D / web design / Design Gráfico e Video")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.header("Video")
            st.video("6.mp4")
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
            
            st.image ("3.png")   
            button_4 = st.button("Gosto", key="sictemic")
            
                
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
        st.write("O meu Nome é Paulo Ricardo Monteiro, formado em 2008 em Audiovisual e Multimédia, Actualmente formei-me com o mestrado em Engenharia Informática - área de Multimedia"
                 "Tendo defendido a minha Tese com 15 valores no âmbito dos sistemas de Realidade Virtual e Realidade Aumentada para os Setores Museológicos e da Arte Digital")
        #st.image('Me.jpg', width=300)
        st.image('CV2.png', width=600)

        #def show_pdf(file_path):
            #with open("CV - Paulo Monteiro - Mestrado 2023 com interesses_vs_atualizada2.pdf", "rb") as f:
                #base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            #pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
            #st.markdown(pdf_display, unsafe_allow_html=True)

        #show_pdf('CV - Paulo Monteiro - Mestrado 2022.pdf')
        st.title("Tese de Mestrado")
        components.iframe("https://www.flipbookpdf.net/web/site/2d28aac1582b9a814985f06ad159247e52a9b869202601.pdf.html", width=750, height =600)
    elif choice == "3D Games":
        st.title("Exemple de Pequeno Jogo em Python e Blender")
        st.write("Jogo 3D em UPBGE")
        components.iframe("https://sketchfab.com/models/ed63f59358354f6da8061fbcaeeaead2/embed", width=750, height=600)
        #Comentado components.iframe("https://cdn.soft8soft.com/AROAJSY2GOEHMOFUVPIOE:85cf9c6521/Sub%20Python%20Game/Sub%20Python%20Game.html", width=750, height =600)
        st.video("https://youtu.be/ZfxPMMzyeX8")
    elif choice == "Architecture":    
        
        st.header("Architecture")
        col1 , col2 = st.columns(2)
        with col1:
            st.header("Ecological Towers")
            components.iframe("https://sketchfab.com/models/076138e049d34dad974e4dc47c8755ff/embed", width=650, height=600)
            #st.video("aero_recording 2.mp4",)
            st.header("Architecture Exterior")
            st.image("Image-Architectura.png")
            
        with col2:
            st.header("Architecture Interior2")
            st.video("IMG_5277.mp4")
            st.header("Architecture Home")
            st.video("IMG_5278.mp4")
            st.header("Building City")
            st.video("Screen Recording 2023-09-20 at 19.29.53.mp4")
            st.header("Architecture Interior4")
            st.video("IMG_0371.mp4")

        components.iframe("https://sketchfab.com/models/3e99cbb8b0e34e4485e7accfa421f8e0/embed" , width=700, height=600)
        st.markdown(components.iframe, unsafe_allow_html=True)
    elif choice == "Art":   
    
        button_2 = st.button("Gosto", key="asian")
   
        st.title(" The Faun´s Tree House - 2D")
        components.iframe("https://renderstuff.com/tools/360-panorama-web-viewer-sharing/?image=https://live.staticflickr.com/65535/52915761092_c09c7bf9ec_k.jpg", width=750, height=600)
       
        st.title(" The Faun´s Tree House - 3D")
        components.iframe("https://renderstuff.com/tools/360-panorama-web-viewer-sharing/?image=https://live.staticflickr.com/65535/52916746725_26db08b7c8_k.jpg",  width=750, height=600)
        st.video("human.mp4")
        
    elif choice == "Video":
        st.title("Video - Reportagem Fura Dels Bhaus")
        st.write("O meu nome é Paulo Monteiro, e tenho interesse na realização de Videos e Curtas de animação e Reportagens Realizei alguns projetos de Audiovisual com budget enixistente ou de baixo custo, sempre com interesse em novas narrativas e algum processo experimental.Nesta Reportagem com a equipe dos Fura dels Baus a bordo do navio NAUMON , assistimos a experimentos à muito testados com seres humanos num jogo sobre o erotismo o sonho a dor e a condição humana")
        st.video("https://youtu.be/4xGbR5gUoTc")
        st.title("|Projeto Video  CLIP | o RECADO - SAM the Kid- Video CLIP")        
        st.video("SAM_THE_KID.mp4")
        
    elif choice == "3D":
        st.title("3D Gallery")
        st.write("Galeria de Criações 3D")
        col1, col2, col3 = st.columns(3)
   
        #st.markdown(video_html, unsafe_allow_html=Tr
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
        
        #Atualização de Galeria 3D
        
        with col1:
            st.header("Video")
            st.video("Portf3.mp4")
            button_1 = st.button("Gosto", key="xisp")
        with col2:
            st.header("Design")
            st.video("Ptfolio1.mp4")

            button_2 = st.button("Gosto", key="local")
        with col3:
            st.title("Magician Xamã")
            components.iframe("https://sketchfab.com/models/6750052d34c54f5b97570b6852be2848/embed",  width=350, height=300)
            button_3 = st.button("Gosto", key="safe")
        
        
        st.title("Video")
        st.video("Cutscene Final.mp4")
        button_1 = st.button("Gosto", key="sictemic")

        st.title("  - Virtual Museum - ")
        st.video("https://www.youtube.com/watch?v=s5DxZX29Rjo")
        st.title("Cartoon")
        st.write("Galeria de Criações e Desenho")
        st.image("Drwaing.jpeg")
        st.image("Paulo_Image.PNG")
        st.image("3.png")
    elif choice == "IoT":
        st.title("Projetos Dashboarding e Data Science")
        st.write("Criação de Dashboarding e Infografias para Data Science .")
      

        st.title("Estatisticas da Saúde Mental no Período de 2004 a 2020 ")

        st.write(
            """Estudo Efetuado pelo INE - Instiituto Nacional de Estatística sobre o estado da Saúde Mental dos Portugueses 
            divídidos por Género, Faixa Étaria e Ocupação Profissional
            """
        )
        p = open("lda.html")
        components.html(p.read(), width=1000, height=800, )
        df = pd.read_csv(
                "Mentalhealth3.csv"
            )
       
        #d= load_datasets()
        


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
        #fig = ff.create_distplot(
                #hist_data, group_labels, bin_size=[2008, 2010, 2020])

        # Plot!
        #st.plotly_chart(fig, use_container_width=True)




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
        
        
            

            #df = pd.read_csv(
                #"MentalHealth.csv"
            #)
            #st.dataframe(filter_dataframe(df))

           


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
        st.title("Animation")
        components.iframe("https://v3d.net/j8b", width=600, height=300
                        )
        st.title(" Experiencia de Realidade Virtual - Virtual Museum ")
        st.video("https://www.youtube.com/watch?v=s5DxZX29Rjo")
    elif choice == 'IMAGE - Classifier APP':
         
        model = ResNet50V2(weights='imagenet')

        # título da página
        st.title('Detecção e classificação de imagens')

        # layout da página
        col1, col2 = st.columns(2)
        with col1:
            # uploader de imagem
            st.header('Upload da imagem')
            uploaded_file = st.file_uploader("Escolha uma imagem...", type=["jpg", "jpeg", "png", "csv", 'GIF'])
            
        with col2:
            st.header('Imagem de exemplo')
            st.image(uploaded_file)
        st.subheader("O Erro Apresentado é de TESTES - Podem continuar Fazendo o UPload")
        if uploaded_file is not None:
            # carregando a imagem
            img = image.load_img(uploaded_file, target_size=(224, 224))

            # exibindo a imagem
            st.image(img, caption='Imagem carregada', use_column_width=True)

            # pré-processamento da imagem
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)

            # passando a imagem pelo modelo para realizar a classificação
            preds = model.predict(x)

            # decodificando as previsões
            decoded_preds = decode_predictions(preds, top=3)[0]

            # exibindo as previsões
            if len(decoded_preds) > 0:
                st.subheader("Previsões:")
                for result in decoded_preds:
                    label = result[1]
                    prob = result[2]
                    st.subheader(f'{label} : {prob * 100} %')
                with open('results.csv', 'a') as f:
                    with csv.DictWriter(f, fieldnames = [ "Label", "Probabilidades"]):
                        writer.writeheader()
                for r in results:
                    writer.writerow(r)
            else:
                st.write("A imagem n é valida")
            # for label, prob in decoded_preds:
            chart_data = pd.read_csv('results.csv', sep=',')
            # if len(decoded_preds) >=2:
            #  label,_,prob = decoded_preds[0]
            # st.write('%s (%.2f%%)' % (label, prob * 100))
            # label,_,prob = decoded_preds[1]
            # st.write(f'{label}:{prob:2%}')
            
        

            c = alt.Chart(chart_data).mark_circle().encode(x='label', y='prob', size='prob', color='label',
            tooltip=['label', 'prob'])

            st.altair_chart(c, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)
display_menu()   

#######################################################

#NEW Part of Code

import streamlit as st
import pandas as pd
import requests
import os
from io import StringIO
import base64
import json

# GitHub repo and file information
GITHUB_REPO = "Lefaun/submitform"
GITHUB_FILE_PATH = "ideas.csv"

# Use environment variable or Streamlit secrets for the token
#GITHUB_ACCESS_TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")  # For local use
GITHUB_ACCESS_TOKEN = st.secrets["general"]["GITHUB_ACCESS_TOKEN"]  # For Streamlit sharing

# Function to load CSV file from GitHub
def load_csv(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = StringIO(response.text)
        df = pd.read_csv(data)
        return df
    else:
        st.error("Falha ao atualizar no Portfolio.")
        return pd.DataFrame(columns=["Name", "Idea"])

# Function to get the SHA of the file
def get_file_sha(repo, path, token):
    url = f"https://api.github.com/repos/{repo}/contents/{path}"
    headers = {"Authorization": f"token {token}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        file_info = response.json()
        return file_info['sha']
    else:
        st.error(f"Falha ao atualizar dados online: {response.status_code}")
        st.error(f"Response: {response.text}")
        return None

# Function to update CSV on GitHub
def update_csv_on_github(repo, path, token, content, sha):
    url = f"https://api.github.com/repos/{repo}/contents/{path}"
    headers = {
        "Authorization": f"token {token}",
        "Content-Type": "application/json"
    }

    message = "A atualizar dados dos comentários"
    content_encoded = base64.b64encode(content.encode()).decode("utf-8")

    data = {
        "message": message,
        "content": content_encoded,
        "sha": sha
    }

    response = requests.put(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        st.success("O seu comentário foi adicionado, obrigado")
    else:
        st.error(f"Falha ao Atualizar dados do Portfolio: {response.status_code}")
        st.error(response.json())

# Load existing ideas from GitHub CSV
csv_url = f"https://raw.githubusercontent.com/{GITHUB_REPO}/main/{GITHUB_FILE_PATH}"
df_ideas = load_csv(csv_url)

# Streamlit form to submit ideas
st.title("Deixe aqui sua ideia ou comentário")
name = st.text_input("O seu Nome:")
idea = st.text_area("Qual a Ideia:")

# Handle form submission
if st.button("Enviar"):
    if name and idea:
        new_row = pd.DataFrame([[name, idea]], columns=["Name", "Idea"])
        df_ideas = pd.concat([df_ideas, new_row], ignore_index=True)

        csv_content = df_ideas.to_csv(index=False)

        sha = get_file_sha(GITHUB_REPO, GITHUB_FILE_PATH, GITHUB_ACCESS_TOKEN)
        if sha:
            update_csv_on_github(GITHUB_REPO, GITHUB_FILE_PATH, GITHUB_ACCESS_TOKEN, csv_content, sha)
    else:
        st.error("Por favor preencha primeiro os campos de NOME e Mensagem")

# Display submitted ideas
st.subheader("Ideias e Comentários:")
for i, row in df_ideas.iterrows():
    st.write(f"{i + 1}. **{row['Name']}**: {row['Idea']}")
 


