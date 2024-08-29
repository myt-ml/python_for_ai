import together
import dotenv
import os

dotenv.load_dotenv()
together.api_key = os.getenv("5fae359f0463529f9c96f45ea101a5c966ddefcaa7648b938d1e766dd67e0435")


model_list = together.Models.list()
print(f"{len(model_list)} models available")
