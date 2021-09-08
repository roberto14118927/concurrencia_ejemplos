
import os
import time
import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def procesos( time_to_sleep = 0 ):
    logging.info('Start procesos')
    time.sleep(time_to_sleep)
    logging.info('End procesos')

def main():
    logging.info('Start main')
    
    proceso = multiprocessing.Process(target=procesos, name='procesos',args=(1,), daemon=False)
    proceso.start()
    proceso.join()

    logging.info('End main')

if __name__ == '__main__':
    main()


