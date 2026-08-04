from app import create_app
from configs import Configs

if __name__ == "__main__":
    app = create_app()
    app.run(host=Configs.HOST, port=Configs.PORT, debug=Configs.DEBUG)
