# AirPenguins


Follow steps on tutorial https://gitlab.uzh.ch/ivda/ivda-tutorial until step 4.
We used docker, so move the file stack.yml in the backend folder end run this comand after the download of docker:

docker-compose -f stack.yml up


(optional) download mongodb compas


run then these comands in the backend folder:

pip install fastapi
pip install flask_pymongo
pip install pymongo
pip install flask_cors


to start the backend then on terminal of PyCharm:

python app.py run


to start the frontend then on terminal of WebStornm:

npm run 