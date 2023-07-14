{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mRunning cells with 'c:\\Users\\Sricharan\\AppData\\Local\\Microsoft\\WindowsApps\\python3.7.exe' requires ipykernel package.\n",
      "\u001b[1;31mRun the following command to install 'ipykernel' into the Python environment. \n",
      "\u001b[1;31mCommand: 'c:/Users/Sricharan/AppData/Local/Microsoft/WindowsApps/python3.7.exe -m pip install ipykernel -U --user --force-reinstall'"
     ]
    }
   ],
   "source": [
    "from rank_bm25 import BM25Okapi\n",
    "import glob\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "from nltk.tokenize import word_tokenize\n",
    "\n",
    "# List the files in the directory\n",
    "# file_list = os.listdir('/content/drive/MyDrive/tweet_files')\n",
    "data_dir = '/content/drive/MyDrive/tweet_files/'\n",
    "DATA_SET_DIR = data_dir\n",
    "print('\\nGetting List of text files from' + DATA_SET_DIR)\n",
    "files = os.listdir(DATA_SET_DIR)\n",
    "print((files[11]))\n",
    "print('\\nFile list retrieved from ' + DATA_SET_DIR)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 16:30:00) [MSC v.1900 64 bit (AMD64)]"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "f21c6045f170b622cc5cdf49d23e45d81cd353c1d34e05b260529b713e28859f"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
