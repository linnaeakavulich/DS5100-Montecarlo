import numpy as np
import pandas as pd

class Die():
    
    def __init__(self, faces):
        '''
        This is the initializer method
    
        PURPOSE: Given an array of faces, creates a die object 
        
        INPUTS
        faces    array of values to represent faces of a die
    
        OUTPUT
        self.df  dataframe of die faces and their relative weights
        '''
        faces = pd.array(faces)
        weights = []
        for i in range(len(faces)):
            weights.append(float(1))
                
        self.df = pd.DataFrame({'Weights': weights,
                               'Faces': faces})
        
    
    def change_weight(self, face, new_weight):
        '''
        This is a method that allows the faces of a die object to be weighted 
        differently
    
        PURPOSE: Will edit an existing die object given a face of an already 
        instantiated die object and the corresponding desired new weight. 
        
        INPUTS
        face    either a string, int or float of the face to be weighted
        new_weight an int or float of the desired magnitude      
    
        OUTPUT
        self.df  dataframe of die faces and their updated relative weights
        '''
        if type(face) == str:
            if ((self.df['Faces'].str.contains(str(face)).any()) == False):
                print('This die does not have a face ' + str(face))
            else:
                self.df.loc[self.df['Faces'] == face, 'Weights'] = new_weight
        
        elif (type(face) == int) or (type(face) == float):
            if (((face) in self.df['Faces'].values) == False):
                print('This die does not have a face ' + str(face))
            else:
                self.df.loc[self.df['Faces'] == face, 'Weights'] = new_weight
        
        elif(isinstance(float(new_weight), float) == False):
            print('Please enter a number!')
        
    
    def roll_die(self, num_rolls = 1):
        '''
        This is a method that allows a die object to be rolled in order to 
        generate a dataframe of values
    
        PURPOSE: Will roll an existing die instance to return the requested
        number of values
        
        INPUTS
        num_rolls int or float of the desired number of rolls      
    
        OUTPUT
        self.results  dataframe of die faces which appeared on each roll
        '''
        results = []
        for i in range(1,num_rolls+1):
            result = self.df.Faces.sample(weights=self.df.Weights).values[0]
            results.append(result)
        self.results = pd.Series(results)
        return self.results   
    
    
    def show(self):
        '''
        This is a method that shows the created die
        
        PURPOSE: Displays the die faces with their corresponding weights for
        each die instance
        
        INPUTS
        none     
    
        OUTPUT
        self.df  dataframe of die faces and respective weights
        '''
        return self.df
#___________________________________________________________________________________________________________________________

class Game():
  
    def __init__(self, die):
        '''
        This is the initializer method
    
        PURPOSE: Given a list of die objects, rolls the provided number of dice
        the requested number of times to return a dataframe with the results of
        each roll. 
        
        INPUTS
        die    a list of die objects; can contain 1 or more dice
    
        OUTPUT
        none
        '''
        self.die = die
        print(self.die)
        
    def play(self, n_rolls):
        '''
        This is a method that allows a collection of die objects to be rolled in 
        order to generate a dataframe of values
    
        PURPOSE: Will roll an the set of dice initialy passed and return the
        results for the required number of rolls. 
        
        INPUTS
        n_rolls int or float of the desired number of rolls      
    
        OUTPUT
        self.game_df  dataframe of die faces that appeared on each roll for each
        die provided. 
        '''
        self.N = [die.roll_die(n_rolls) for die in self.die]
        
        self.game_df = pd.DataFrame(self.N).T 
        self.game_df = self.game_df.rename_axis(index='Roll Number') 
        
    def show(self):
        '''
        This is a method that shows the results of a game
        
        PURPOSE: Displays the die faces which appeared on each of n rolls 
        
        INPUTS
        none     
    
        OUTPUT
        self.game_df  dataframe of die faces which appeared on each roll
        '''
        return self.game_df   

    
#__________________________________________________________________________________________________________
    
class Analyzer():
    
    def __init__(self, games):
        '''
        This is the initializer method
    
        PURPOSE: Given a defined instance of the game class, will analyze the 
        results of playing
        
        INPUTS
        games    a dataframe of results from a played instance of game. 
    
        OUTPUT
        none
        '''
        self.games = games
        

    def jackpot(self):
        '''
        This method counts the number of rolls in a game where all faces of your 
        dice display the same number (know as a 'jackpot').
        
        INPUTS
        none
        
        OUTPUTS
        num_jckpts a count of the number of jackpots (defined above) in the
        given game instance. 
        '''
        num_jckpts = len(self.games[self.games.apply(pd.Series.nunique, axis=1) == 1])
        print('You have', str(num_jckpts), 'jackpots')
        return num_jckpts
    
    def combo(self):
        '''
        This is a method that shows the unique combinations of faces that
        appeared in the duration of the game instance which was passed to 
        Analyzer. 
        
        PURPOSE: Displays the unique combinations of faces rolled
        
        INPUTS
        none     
    
        OUTPUT
        combos  dataframe of unique cominations of faces which occured in the 
        game
        '''
        combos = self.games.value_counts(ascending=True).reset_index(name='count')
        combos = combos.rename_axis(index='Index')
        print(combos)
                   
    def faces_per_roll(self):
        '''
        This is a method that shows the number of times each face of the a given
        die appeared in one roll.
        
        PURPOSE: Displays the number of instances of a given face on a die
        
        INPUTS
        none     
    
        OUTPUT
        faces_per_roll  dataframe of die faces and respective frequencies
        '''
        faces_per_roll = self.games.apply(pd.Series.value_counts, axis=1)
        return(faces_per_roll)

