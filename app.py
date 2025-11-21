import streamlit as st

st.title("Timeline con Slider")

# Lista de imágenes en GitHub (raw URLs)
# Reemplaza USER, REPO y RUTA según tu repositorio
image_urls = [
    "https://raw.githubusercontent.com/USER/REPO/main/timeline_images/img1.png",
    "https://raw.githubusercontent.com/USER/REPO/main/timeline_images/img2.png",
    "https://raw.githubusercontent.com/USER/REPO/main/timeline_images/img3.png",
    "https://raw.githubusercontent.com/USER/REPO/main/timeline_images/img4.png",
    "https://raw.githubusercontent.com/USER/REPO/main/timeline_images/img5.png",
]

# Slider de 1 a 5
index = st.slider("Selecciona un punto del timeline", 1, 5, 1)

# Mostrar imagen correspondiente
st.image(image_urls[index - 1], caption=f"Imagen {index}", use_column_width=True)
