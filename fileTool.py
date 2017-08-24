#! python3



import os, shutil, logging,random

# copy some kind of file to a certain folder
def copyCertainFile(file_ext, source, destination):
#    os.chdir(source)
    for foldername, subfolders, subfiles in os.walk(source):
        for subfile in subfiles:
            if (os.path.splitext(subfile)[1] == file_ext):
                shutil.copy(os.path.join(foldername, subfile), destination)
#        for subfolder in subfolders:
#            newsource = os.path.join(source, subfolder)
#            copyCertainFile(file_ext, newsource, destination)


#def findBigFile(path):


# reset the sequence of all files
def resetSequence(source):
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
    logging.debug('starting reset filenames:')
    files = []
    for foldername, subfolders, subfiles in os.walk(source):
        for subfile in subfiles:
            files.append(subfile)
    files.sort()
    for file in files:
        logging.debug('set file: ' + file + ' to ' + 'spam'+(str(files.index(file)+1)).zfill(3)+os.path.splitext(file)[1])
        shutil.move(os.path.join(source, file), os.path.join(source, 'spam'+(str(files.index(file)+1)).zfill(3)+os.path.splitext(file)[1]))
    logging.debug('end of reset filenmes')

#copyCertainFile('.txt','D:\\python\\test\\a', 'D:\\python\\test\\b')
#resetSequence('D:\\python\\test\\resetsequence')
#print ('done')

def guessCoin():
    guess = ''
    while guess not in ('heads', 'tails'):
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
    toss = random.randint(0, 1) # 0 is tails, 1 is heads
    if(toss == 0):
        toss = 'tails'
    elif(toss == 1):
        toss = 'heads'
    logging.debug('toss is ' + str(toss) + ' and guess is ' + guess)
    if toss == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guess = input()
        logging.debug('toss is ' + str(toss) + ' and guess is ' + guess)
        if toss == guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')