"""Abre la maqueta con un servidor local. No requiere instalar paquetes."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Timer
import webbrowser


def main():
    folder = Path(__file__).resolve().parent
    handler = partial(SimpleHTTPRequestHandler, directory=str(folder))
    try:
        server = ThreadingHTTPServer(('127.0.0.1', 8000), handler)
    except OSError:
        # Elige otro puerto disponible si el 8000 está ocupado.
        server = ThreadingHTTPServer(('127.0.0.1', 0), handler)
    address = f'http://127.0.0.1:{server.server_port}/'
    print(f'Abre esta dirección: {address}')
    print('Mantén esta terminal abierta. Para detener: Ctrl+C.')
    timer = Timer(0.5, webbrowser.open, args=(address,))
    timer.daemon = True
    timer.start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        timer.cancel()
        server.server_close()


if __name__ == '__main__':
    main()
