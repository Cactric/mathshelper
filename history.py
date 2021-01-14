#!/usr/bin/python

import math as maths
import sys, os

#print("History module loaded.")

class History():
    def __init__(self):
        self.history = [maths.pi]

        # Determine the best directory for us to save the history file in...
        
        #Fallback directory is to use the current directory
        self.directory = os.curdir
        
        # On Linux, see if the environment variable XDG_DATA_HOME exists, and if so we'll use that
        if sys.platform == "linux":
            env_xdg_data_home = os.environ.get("XDG_DATA_HOME")
            if env_xdg_data_home == None:
                # If it doesn't exist, use $HOME/.local/share if HOME exists
                env_home = os.environ.get("HOME")
                if env_home == None:
                    self.directory = '~'
                    self.directory += "/.mathshelper"
                else:
                    self.directory = env_home + "/.local/share"
                    self.directory += "/mathshelper"
            else:
                self.directory = env_xdg_data_home
                self.directory += "/mathshelper"
        print(self.directory)

        #If the file/directory doesn't exist, create it
        if not os.path.exists(self.directory):
            try:
                os.mkdir(self.directory)
            except:
                print("There was an error trying to create the data directory, so things like history will be held in memory only")
                #Just return so the history is empty
                return
        
        #Now that it the directory definitely exists, try to open the history file
        
        if not os.path.exists(self.directory + "/history"):
            print("Creating the history file...")
            history_file = open(self.directory + "/history", 'w')
            history_file.close()

    def load(self):
        #Warning: this will overwrite the history already in memory
        try:
            history_file = open(self.directory + "/history", 'r')
        except:
            print("There was an error accessing the history file, so the history will be held in memory only.")
            return
        
        history_text = history_file.readlines()
        history_file.close()
        
        for text in history_text:
            text.strip()
        
        self.history = []
        for text in history_text:
            try:
                value = float(text)
                if value.is_integer():
                    value = int(value)
                self.history.append(value)
            except TypeError:
                print("Error: The history file seems to be corrupt. The history may be overwritten")
                return

    def view(self):
        print("\nHistory:\n")
        for value in self.history:
            print("\t",value)
        input("Press [Enter] to return to the main menu")

    def pop(self):
        return self.history.pop()
    
    def push(self, value):
        return self.history.append(value)
    
    def clear(self):
        self.history.clear()
        
    def save(self):
        try:
            history_file = open(self.directory + "/history", 'w')
        except:
            print("Error: the history file couldn't be written to.")
        
        for value in self.history:
            history_file.write(str(value) + "\n")
        
        history_file.close()
        print("History file was saved successfully")
