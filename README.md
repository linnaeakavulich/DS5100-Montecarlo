# DS5100 Final Project: A Game to Die for
## Metadata
Author: Linnaea Kavulich

Contact: pqk4kp@virginia.edu

## In Breif
An installable package which allows the user to create a one or many n-sided dice, alter the weights of each face, initiate games in which these dice are rolled n-times and analyze key attributes of the results.

## Installing
Download this repository. Ensure you are in the same directory as this repo. From the command line run:

```
$pip install –e .
```

## Importing
There are three classes included in the montecarlo package: Die, Game, and Analyzer. Import them all at once in your text file or notebook using:

```
import montecarlo as mc
from montecarlo import montecarlo
```

Alternatively, each class can be imported individually using:


```
from montecarlo import Die
from montecarlo import Game
from montecarlo import Analyzer
```

## Instantiating Die
To instantiate a Die object, call the Die class and pass an array of the desired faces

```
example_die1 = Die([1, 2, 3, 4, 5, 6])
example_die2 = Die(['A', 'B', 'C', 'D'])
```

Once a Die has been created, you can change the weight of a face

```
example_die2.change_weight('A', 2000)
```

The above code will change the weight for face A to 2000. The default weight for all faces is 1. If desired, the instantiated Die can be rolled directly from the Die class by calling 

```
example_die1.roll_die(5)
```

This code will roll example_die1 five times and return a dataframe with the results. Please note that the Game class will allow you to roll multiple die objects at once. To see the die that has been created, along with the respective weights for each face, call:

```
example_die1.show()
```

## Instantiating Game
To instantiate a Game object, you must first create one or more Die objects. Pass the created dice to Game as a list

```
example_game = Game([example_die1, example_die1, example_die1])
```

This code will create a game with three six-sided dice. To roll these dice n=50 times, call

```
example_game.play(50)
```

This will roll your three example_die1 50 times and record the results of each roll in a dataframe. To see this dataframe call 

```
example_game = example_game.show()
example_game
```

## Instantiating Analyzer
To analyze the results of an instance of Game, pass it to the Analyzer class as

```
example_analysis = Analyzer(example_game)
```

A 'jackpot' is when a roll results in all the same face showing. Using example_game, this would manifest as a roll which results in three '1s' or three '2s' or three '3s' and so on. To determine the number of jackpots that occurred in your game

```
example_analysis.jackpot()
```

The above code will return an integer which is the number of jackpots in your game. To see the unique combinations of faces that occurred in your game 

```
example_analysis.combo()
```

To see how many times each face appeared in a given roll

```
example_analysis.faces_per_roll()
```

The above code returns a dataframe that catalogs the number of times each face appeared, roll-by-roll

## API Description: Die
```
def __init__(self, faces):
        '''
        This is the initializer method
    
        PURPOSE: Given an array of faces, creates a die object 
        
        INPUTS
        faces    array of values to represent faces of a die
    
        OUTPUT
        self.df  dataframe of die faces and their relative weights
        '''

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
```

## API Description: Game
```
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

    def show(self):
        '''
        This is a method that shows the results of a game
        
        PURPOSE: Displays the die faces which appeared on each of n rolls 
        
        INPUTS
        none     
    
        OUTPUT
        self.game_df  dataframe of die faces which appeared on each roll
        '''
```

## API Description: Analyzer
```
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
```
