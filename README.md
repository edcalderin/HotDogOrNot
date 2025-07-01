<div align="center" id="top"> 
  <img src="https://drive.google.com/uc?id=11ildP7IqK4UzBUXXnW53s-NJlVZZfQHM" alt="HotDogOrNot" />

  &#xa0;

  <!-- <a href="https://hotdogornot.netlify.app">Demo</a> -->
</div>

<h1 align="center">HotDog or Not</h1>
FastApi for hot dog detection with Tensorflow Keras and Transfer Learning using a pretrained model, it is exactly VGG16.

This project is based on <a href=https://pub.towardsai.net/fastapi-create-and-deploy-hot-dog-detector-cf89d9b51a3c > Towards Data Science: FastAPI Create and deploy hotdog detector</a> with a few variations and refactorizations.

Training data obtained from Kaggle: https://www.kaggle.com/c/hotdogornot

The model can classify between __chili dog__, __food__, __frankfurter__, __furniture__, __hotdog__, __people__ and __pets__.

## Steps to reproduce with Docker (recommended)
* Install Docker (only if you don't have it) from: https://www.docker.com/products/docker-desktop

* Inside project folder, run `docker-compose up`

* Open http://127.0.0.1/docs for Swagger documentation

* Finally, test the endpoint wih some images from Google

## Steps to reproduce without Docker (Manually)


* Run `pip3 install virtualenv`

* Inside the project folder, run `virtualenv new_env`

* Run `source new_env/Scripts/activate`

* Run `pip3 install --no-cache-dir --upgrade -r requirements.txt`

* Run `unzip app/models/variables.zip -d  app/models/`

* If you use VSCode, make sure to select Python environment created in previous steps.

* Run `python app/main.py`

* Open http://127.0.0.1/docs for Swagger documentation

* Finally, test the endpoint wih some images from Google

* To stop server press `Ctrl` + `C`

**I highly don't recommend to execute this project manually if you do not have a GPU setup, since the model needs a memory accelerator. Without GPU setting it will use CPU available**

## Notebook
You can download this notebook and read it with Jupyter or VSCode, if you want to try execute it then take in account it requires GPU configured.

You can also open it in Google Colab like this:

* Replace domain `github` for `githubtocolab.com/...`.
* Once opened, save a copy to your Google Drive and hands on!

## ✉️ Contact
**LinkedIn:** https://www.linkedin.com/in/erick-calderin-5bb6963b/  
**e-mail:** edcm.erick@gmail.com

## Enjoyed this content?
Explore more of my work on [Medium](https://medium.com/@erickcalderin) 

I regularly share insights, tutorials, and reflections on tech, AI, and more. Your feedback and thoughts are always welcome!
