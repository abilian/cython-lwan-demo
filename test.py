import time

import multiprocessing
import requests
import lwan_demo


def app(env, start_response):
    start_response("200 ok", [])
    return b"hello"


def start_server():
    lwan_demo.run()


def test_server():
    try:
        server = multiprocessing.Process(target=start_server)
        server.start()
        time.sleep(0.5)

        r = requests.get("http://127.0.0.1:8080/")
        assert r.status_code == 200
        # Hardcoded in the server demo
        assert r.text.strip() == "Hello, World!"

        r = requests.get("http://127.0.0.1:8080/fibonacci")
        assert r.status_code == 200
        assert r.text.strip() == "Fibonacci(10^6) = 1884755131 (with overflow)"

    finally:
        server.kill()
        server.join()
