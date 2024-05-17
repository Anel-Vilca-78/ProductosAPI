import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from infraestructure.controllers import ApiRest

if __name__ == '__main__':
    ApiRest.app.run(host='0.0.0.0', port=3001, debug=True)