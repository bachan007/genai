import openai
import requests
from PIL import Image
from io import BytesIO
import os

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# # Text description for image generation
# text_description = "A colorful sunset over a mountain lake."

# # Call OpenAI's DALL-E API
# response = openai.Completion.create(
#   engine="dall-e",
#   prompt=text_description,
#   n=1,
#   stop=None,
#   temperature=0.7,
# )

client = openai.OpenAI()

esponse = client.images.generate(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="standard",
  n=1,
)

# image_url = response.data[0].url

# # Extract the image URL from the API response
# image_url = response['choices'][0]['image']

# # Download and display the generated image
# image_data = requests.get(image_url).content
# img = Image.open(BytesIO(image_data))
# img.show()

print(esponse)
