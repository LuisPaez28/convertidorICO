import streamlit as st
from PIL import Image
import io

def convert_to_ico(uploaded_file, sizes=[(16, 16), (32, 32), (48, 48), (256, 256)]):
    """
    Convierte una imagen cargada a formato .ico manteniendo varios tamaños.
    """
    try:
        img = Image.open(uploaded_file)
        
        # Convertir a RGBA para asegurar compatibilidad con transparencia
        if img.mode != "RGBA":
            img = img.convert("RGBA")
            
        # El formato ICO soporta múltiples resoluciones en un solo archivo
        ico_buffer = io.BytesIO()
        img.save(ico_buffer, format="ICO", sizes=sizes)
        return ico_buffer.getvalue()
    except Exception as e:
        st.error(f"Error al procesar la imagen: {e}")
        return None

# --- Configuración de la Interfaz ---
st.set_page_config(page_title="Icon Generator", page_icon="🎨")

st.title("🖼️ PNG/JPG to ICO Converter")
st.write("Sube tu imagen y descárgala en formato de icono para Windows o aplicaciones.")

uploaded_file = st.file_uploader("Elige una imagen...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Mostrar vista previa
    st.image(uploaded_file, caption="Imagen original", width=200)
    
    if st.button("Generar Icono"):
        with st.spinner("Procesando..."):
            ico_data = convert_to_ico(uploaded_file)
            
            if ico_data:
                st.success("¡Conversión exitosa!")
                
                # Botón de descarga
                st.download_button(
                    label="📥 Descargar .ico",
                    data=ico_data,
                    file_name="favicon.ico",
                    mime="image/x-icon"
                )