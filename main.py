import argparse
import logging
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()

def main():
  logger.info("Hello world at react \n")



  logger.info("Process finished")


if __name__ == "__main__":
  # Instance arg parser
  parser = argparse.ArgumentParser()

  # Request Arguments in the prompt
  parser.add_argument('filename',
                      help='The path to the dirty data',
                      type=str)

  # Get parsed arguments
  arg = parser.parse_args() 

  main()