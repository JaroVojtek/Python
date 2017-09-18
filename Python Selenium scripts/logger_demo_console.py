import logging

class LoggerDemoConsole():

    def testLog(self):
        #create logger
        logger = logging.getLogger(LoggerDemoConsole.__name__)
        logger.setLevel(logging.INFO)

        #create console hadler and set level to info
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.INFO)

        #create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')

        #add formater to console hnadler -> ch
        chandler.setFormatter(formatter)

        #add console handler to logger
        logger.addHandler(chandler)

        #logging messages

        logger.debug("debug message")
        logger.info("info message")
        logger.warning("warn message")
        logger.error("error message")
        logger.critical("critical message")

demo = LoggerDemoConsole()
demo.testLog()