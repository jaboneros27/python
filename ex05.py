my_name = 'Jabby Eros'
my_age = 52 # absolutely relative to this year
my_height = (5 * 12) + 6 * 2.54 # in centimeters
my_weight = 160 * 0.453592 # in kilos
my_eyes = 'brown'
my_teeth = 'yellow'
my_hair = 'black'

print "Let's talk about %s." % my_name
print "He's %r centimeters tall." % my_height
print "He's %r kilos heavy." % my_weight
print "Actually that's not too heavy."
print "He's eyes are %s and his hair is %s." % (my_eyes, my_hair)
print "He's teeth is %s and badly needs cleaning." % my_teeth

print "If I add %d (my age), %r (my height), and %r (my weight) I get %r" % (my_age, my_height, 
	my_weight, my_age + my_height + my_weight)
