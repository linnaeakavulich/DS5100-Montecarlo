import unittest
from montecarlo import Die
from montecarlo import Game
from montecarlo import Analyzer
import pandas as pd

class DieTestSuite(unittest.TestCase):

    def test_1_change_weight(self):
        '''
        '''
        new = Die([1,2,3])
        new.change_weight(2,1000)
        self.assertTrue(max(new.df["Weights"]) == 1000)
        
        
    
    def test_2_roll_die(self):
        '''
        '''
        new = Die([1,2,3])
        new.roll_die(5)
        self.assertTrue(len(new.results == 5))
    
    def test_3_show(self):
        '''
        '''
        new = Die([1,2,3])
        new.roll_die(5)
        new.df

    
class GameTestSuite(unittest.TestCase):
    
    def test_4_play(self):
        '''
        '''
        x1 = Die([1,2,3])
        x2 = Die([1,2,3])
        x3 = Die([1,2,3])                
        newtst = Game([x1, x2, x3])
        newtst.play(5)
        newtst = newtst.show()
        newtst
        self.assertTrue(len(newtst) == 5)
    
    def test_5_show(self):
        '''
        '''
        x1 = Die([1,2,3])
        x2 = Die([1,2,3])
        x3 = Die([1,2,3])
        newtst = Game([x1, x2, x3])
        newtst.play(5)
        newtst = newtst.show()
        newtst
    

class AnalyzerTestSuite(unittest.TestCase):
    
    def test_6_jackpot(self):
        '''
        '''
        x2 = Die([1,1,1])
        x3 = Die([1,1,1])

        bar = Game([x2, x3])
        bar.play(5)
        bar = bar.show()
        test = Analyzer(bar)
        test.jackpot()
        self.assertTrue(len(test.games[test.games.apply(pd.Series.nunique, axis=1) == 1]) == 5)
    
    def test_7_combo(self):
        b1 = Die([1,1,1])
        b2 = Die([1,1,1])

        jckpt = Game([b1, b2])
        jckpt.play(5)
        jckpt = jckpt.show()
        
        test2 = Analyzer(jckpt)
        
        test_df = test2.games.value_counts(ascending=True).reset_index(name='count')
        type(test_df)
        test_df['count']
        print(test_df['count'])
        self.assertTrue(int(test_df['count']) == 5)
    
    def test_8_faces_per_roll(self):
        k1 = Die([1,1,1])
        k2 = Die([1,1,1])
        k3 = Die([1,1,1])

        only_ones = Game([k1, k2, k3])
        only_ones.play(5)
        only_ones = only_ones.show()
        
        test8 = Analyzer(only_ones)
        test8.faces_per_roll()

        df_of_ones = pd.DataFrame(test8.faces_per_roll())
        self.assertTrue((df_of_ones[1].values[0]) == 3)

if __name__ == '__main__':
    unittest.main(verbosity=2)