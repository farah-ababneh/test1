import logging
logging.basicConfig(level=logging.INFO)
with open("grades.txt","w",encoding="utf-8") as f:
    f.write("Ali, A")
    logging.info("grade saved to tese1")