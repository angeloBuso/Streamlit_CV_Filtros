# importar pacotes
import streamlit as st
import numpy as np
import cv2
from PIL import Image, ImageEnhance

# variavel global - controle de tamanho
TamanhoImagem = 450


def filtros():
    our_imagem = Image.open("empty.jpg")

    # função principal
    st.title("Trabalhando com Visão Computacional")
    st.markdown("""
    Desenvolvido por:
    [Angelo Buso](https://github.com/angeloBuso)
    
    Uma imagem é uma matriz de números?!?!? :confused::confused::confused: .... pelo menos é assim para os :computer:.
    Usando técnicas da Visão Computacional, podemos aplicar filtros em nossas imagens!
    """)
    st.sidebar.title("Menu")

    opcoes_menu = ["Filtros", "Sobre"]
    escolha = st.sidebar.selectbox("Escolha uma opção", opcoes_menu)

    if escolha == "Filtros":
        # 1. Carregar e Exibir a imagem

        arq_imagem = st.file_uploader("Carregue uma foto e aplique um filtro no menu lateral",
                                      type=['jpg', 'png', 'jpeg'])

        if arq_imagem is not None:
            our_imagem = Image.open(arq_imagem)
            st.sidebar.text("Imagem Original")
            st.sidebar.image(our_imagem, width=150)

        filtros = st.sidebar.radio("Filtros", ['Original', 'Escala de Cinza', 'Desenho',
                                               'Sépia', 'Embaçada', 'Detecção de Bordas', 'Contraste'])

        if filtros == 'Escala de Cinza':
            converter_imagem = np.array(our_imagem.convert('RGB'))
            gray_imagem = cv2.cvtColor(converter_imagem, cv2.COLOR_RGB2GRAY)
            st.image(gray_imagem, width=TamanhoImagem)

        elif filtros == 'Desenho':
            converter_imagem = np.array(our_imagem.convert('RGB'))
            gray_imagem_etp1 = cv2.cvtColor(converter_imagem, cv2.COLOR_RGB2GRAY)
            invertendo_cor_etp2 = 255 - gray_imagem_etp1
            blur_imagem_etp3 = cv2.GaussianBlur(invertendo_cor_etp2, (21, 21), 0, 0)
            imagem_desenho_etp4 = cv2.divide(gray_imagem_etp1, 255 - blur_imagem_etp3, scale=256)
            st.image(imagem_desenho_etp4, width=TamanhoImagem)

        elif filtros == 'Sépia':
            converter_imagem = np.array(our_imagem.convert('RGB'))
            converter_imagem = cv2.cvtColor(converter_imagem, cv2.COLOR_RGB2BGR)
            kernel = np.array([[0.272, 0.534, 0.131],
                               [0.349, 0.686, 0.168],
                               [0.393, 0.769, 0.189]])
            sepia_image = cv2.filter2D(converter_imagem, -1, kernel)
            st.image(sepia_image, channels='BGR', width=TamanhoImagem)


        elif filtros == 'Embaçada':
            b_amount = st.sidebar.slider("Kernel (n x n)", 3, 81, 9, step=2)
            converter_imagem = np.array(our_imagem.convert('RGB'))
            converter_imagem = cv2.cvtColor(converter_imagem, cv2.COLOR_RGB2BGR)
            blur_imagem = cv2.GaussianBlur(converter_imagem, (b_amount, b_amount), 0, 0)
            st.image(blur_imagem, channels='BGR', width=TamanhoImagem)

        elif filtros == 'Detecção de Bordas':
            c_amount = st.sidebar.slider("Kernel (n x n)", 3, 500, 9)
            converter_imagem = np.array(our_imagem.convert('RGB'))
            converter_imagem = cv2.cvtColor(converter_imagem, cv2.COLOR_RGB2BGR)
            blur_image = cv2.GaussianBlur(converter_imagem, (11, 11), 0)
            canny_image = cv2.Canny(blur_image, c_amount, c_amount)
            st.image(canny_image, width=TamanhoImagem)

        elif filtros == 'Contraste':
            d_amount = st.sidebar.slider("Contraste", 0.0, 2.0, 1.0)
            enhancer = ImageEnhance.Contrast(our_imagem)
            contrast_imag = enhancer.enhance(d_amount)
            st.image(contrast_imag, width=TamanhoImagem)


        elif filtros == 'Original':
            st.image(our_imagem, width=TamanhoImagem)
        else:
            st.image(our_imagem, width=TamanhoImagem)

    elif escolha == "Sobre":
        st.subheader("Este é um projeto usando apenas linguagem Python e técnicas de *Computer Vision*")
        st.text("""
        Visão computacional é um ramo de *Data Science* bastante amplo.
        É como o computador processa imagens e frames.
        Podemos trabalhar com *deep-learning*, detecção de pessoas e objetos, entre outros.
        """)
        st.markdown("Para saber mais informações **fale comigo**")
        st.markdown("[Portifólio](https://github.com/angeloBuso/data_science_portifolio)")
        st.markdown("[GitHub](https://github.com/angeloBuso)")
        st.markdown("[LinkedIn](https://www.linkedin.com/in/angelo-buso/)")



if __name__ == '__main__':
    filtros()