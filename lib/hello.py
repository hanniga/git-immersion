require 'greeter'

print "What's your name"
my_name = gets.strip

greeter = Greeter.new(my_name)
print greeter.greet