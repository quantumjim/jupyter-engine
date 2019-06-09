from ipywidgets import widgets  
from IPython.display import display


def run_game(game):
    '''
    Runs the given game.
    
    This game engine supports turn based play.
    In each turn, the player chooses first chooses an option for an input
    named `a`, and then chooses an option for `b` and one for `c`. The
    image and the possible options for each input can be altered based on
    the inputs given.
    '''
        
    input_a = widgets.ToggleButtons(options=game.options_a)
    input_b = widgets.ToggleButtons(options=[''])
    input_c = widgets.ToggleButtons(options=[''])

    boxes = widgets.VBox([input_a,input_b,input_c])
    display(boxes)

    def given_a(obs_a):
        if input_a.value not in ['',input_a.options[0]] and (input_a.value in input_a.options):
            game.given_a(input_a.value)
            input_b.options = game.options_b

    def given_b(obs_b):
        if input_b.value not in ['',input_b.options[0]] and (input_b.value in input_b.options):
            game.given_b(input_b.value)
            input_c.options = game.options_c

    def given_c(obs_c):
        if (input_c.value not in ['',input_c.options[0]]) and (input_c.value in input_c.options):
            game.given_c(input_c.value)
            input_a.options = game.options_a
            input_b.options = ['']
            input_c.options = ['']          

    input_a.observe(given_a)
    input_b.observe(given_b)
    input_c.observe(given_c)