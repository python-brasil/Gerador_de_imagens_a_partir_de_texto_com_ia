import openai
import requests
import os
from io import BytesIO
from PIL import Image
def gerar_imagem(prompt):
    openai.api_key = os.getenv('sua key da Openai')
    response = openai.Image.create(
        prompt = prompt,
        n=1,
        size = '1024x1024',
        response_format = 'url'
    )
    image_url = response["data"][0]["url"]
    image_data = requests.get(image_url).content
    # Converter imagem para objeto Pillow Image
    image = Image.open(BytesIO(image_data))
    # Exibir imagem
    image.show()
gerar_imagem('escreva o quer quiser para que a IA gere') 


