from flask import Flask, json
from uid_reader import uid_reader

companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

api = Flask(__name__)

@api.route('/companies', methods=['GET'])
def get_companies():
  return json.dumps(companies)


@api.route('/read_id_from_reader', methods=['GET'])
def read_tag():
  id_tag = [{"uid_unic": "12vcvx3-sdvcxv=cxv=xcvxcv=xcvxc=vxcv=xcvs"}]
  return json.dumps(id_tag)

if __name__ == '__main__':
    api.run() 