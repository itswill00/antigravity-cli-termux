# agy web entry — delegates to server.main() via api+ui package
from .server import main as web_main

if __name__ == "__main__":
    web_main()
