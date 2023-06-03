import os

cwd = os.getcwd()
if 'data' not in os.listdir(cwd):
    os.mkdir('data')