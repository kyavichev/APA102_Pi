"""Sample script to run a few colour tests on the strip."""
import colorschemes

NUM_LED = 60

# One Cycle with one step and a pause of one second. Hence one second of white light
print('Three Seconds of white light')
MY_CYCLE = colorschemes.Solid(num_led=NUM_LED, pause_value=3, num_steps_per_cycle=1, num_cycles=1)
MY_CYCLE.start()


while True:

	# Five quick trips through the rainbow
	print('Five quick trips through the rainbow')
	MY_CYCLE = colorschemes.TheaterChase(num_led=NUM_LED, pause_value=0.04, num_steps_per_cycle=35, num_cycles=5, global_brightness=10)
	MY_CYCLE.start()

print('Finished the test')
