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

The above code will change the weight for face A to 2000. The default weight for all faces is 1.
