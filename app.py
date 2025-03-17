from flask import Flask,jsonify
import requests

auto = Flask(__name__)

cars = [
    {'id': 1,
     'name': 'Toyota',
     'price': 200000,
     'year': 2020
     },
     {'id': 2,
      'name': 'Honda',
      'price': 250000,
      'year': 2019
      },
      {'id': 3,
       'name': 'Ford',
       'price': 300000,
       'year': 2018
      }
      ]

@auto.route('/cars-list',methods = ['GET'])
def get_cars():
    return jsonify({'cars': cars})

@auto.route('/cars/get/<int:id>',methods = ['GET'])
def get_car(id):
    for car in cars:
        if car['id'] == id:
            return jsonify({'car': car})
        
@auto.route('/cars/get/<string:name>',methods = ['GET'])        
def get_car_name(name):
    for car in cars:
        if car['name'] == name:
            return jsonify({'car': car})
        else:
            return jsonify({'message': 'Car not found'})
        


     
if __name__ == "__main__":
    auto.run(
        host="0.0.0.0",
        port=5000,
        debug=True)

