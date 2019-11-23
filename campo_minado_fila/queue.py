import zmq
import sys

class Queue:

   def server(self):
        try:
            context = zmq.Context(1)
            # Socket do cliente
            frontend = context.socket(zmq.XREP)
            frontend.bind("tcp://*:5559")
            # Socket do servidor
            backend = context.socket(zmq.XREQ)
            backend.bind("tcp://*:5560")

            zmq.device(zmq.QUEUE, frontend, backend)
        except :
            for val in sys.exc_info():
                print(val)
            print("Desativa a fila") 
        finally:
            pass
            frontend.close()
            backend.close()
            context.term()

if __name__ == "__main__":
    fila = Queue()
    fila.server()