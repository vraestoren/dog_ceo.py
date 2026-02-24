# dog_ceo.py
Web-API for [dog.ceo](https://dog.ceo) website that allows developers to access and integrate over 20,000 images of dogs from over 120 breeds with other applications

## Example
```python
from dog_ceo import DogCeo

dog_ceo = DogCeo()
random_image = dog_ceo.get_random_image()
print(random_image)
```
