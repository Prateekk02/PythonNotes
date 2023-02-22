import logging
logging.basicConfig(filename="Dummy4.log", level=logging.DEBUG, format="%(asctime)s %(name)s %(message)s")
l = [1,2,3,4,5,[2,3,4],'prateek','kumar']

l1_int = []
l2_str = []
for i in l:
    logging.info("We are iterating through our list and our local var is {}".format(l))
    if type(i)==list:
        logging.info("I am inside if statement and I am trying to check list type")
        for j in i:
            logging.info("I am in another for loop for list inside list element")
            if type(j) == int:
                logging.info("I am inside if statement")
                l1_int.append(j)
    elif type(i) == int:
        l1_int.append(i)
    else:
        if type(i) == str:
            l2_str.append(i)
logging.info("MY FINAL RESULT FOR int is {l1} and str is {l2}".format(l1=l1_int, l2=l2_str))