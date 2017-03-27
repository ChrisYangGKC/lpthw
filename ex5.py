my_name = 'Chris Yang'
my_age = 38
my_height = 74

my_weight = 95

my_eyes = 'blue'

my_teeth = 'White'

my_hair = 'Brown'

print "Let's talk about %r." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair with %d years old." % (my_eyes, my_hair, my_age)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight) 