from requests import Session

class DogCeo:
	def __init__(self) -> None:
		self.api = "https://dog.ceo/api"
		self.session = Session()
		self.session.headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
		}
	
	def get_all_breeds(self) -> dict:
		return self.session.get(f"{self.api}/breeds/list/all").json()
	
	def get_random_image(self, count: int = 1) -> dict:
		return self.session.get(
			f"{self.api}/breeds/image/random/{count}").json()
	
	def get_images_from_breed(self) -> dict:
		return self.session.get(
			f"{self.api}/breed/hound/images").json()
	
	def get_random_breed_image(self, count: int = 1) -> dict:
		return self.session.get(
			f"{self.api}/breed/hound/images/random/{count}").json()
	
	def get_all_sub_breeds(self) -> dict:
		return self.session.get(f"{self.api}/breed/hound/list").json()
	
	def get_all_sub_breed_images(self) -> dict:
		return self.session.get(
			f"{self.api}/breed/hound/afghan/images").json()
	
	def get_random_sub_breed_image(
			self,
			count: int = 1) -> dict:
		return self.session.get(
			f"{self.api}/breed/hound/afghan/images/random/{count}").json()
