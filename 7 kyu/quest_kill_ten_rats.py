"""
This kata honors a recurring troupe of many online games.
The origin of this tradition can be traced to the classic Black Isle pc game Baldur's Gate. The very first quest requires you to kill 10 rats. One rather humble start for what later becomes a epic adventure. Honor awaits!

Its intended to be a easy but entertaining exercise on classes and conditions.

You must instantiate and interact with a World() object. On this kata the following methods are available:

talk(target, what): Interact with npcs. The only valid npc on this kata has the name "npc".
pickup(what): Pickup a thing to throw. Default is "rock".
throw(target): If you are holding a thing, throw it at a target. The throw may miss. Will return True if hit, False if missed.

Ex.:
world.talk("npc", "hello")
world.pickup("rock")
world.throw("rat")

Talking to the "npc" will give you further instructions on what to do. The talk replies will be in the Output panel. Be careful when using while loops because if the script timeouts you wont see any output.

Your function should return the world object instance after all tasks are completed.
The tests will call the done() method on the returned object. This method will check the internal flags of the object to see if you completed the quest line.
Replacing or changing the World class and instance (other than calling the documented methods) is not allowed. The full tests include a few type checks.

https://www.codewars.com/kata/58985ffa8b43145ac900015a/train/python
"""

def world_quest():
    world = World()
    world.talk("npc", "hello")
    world.talk("npc", "Bob")
    world.talk("npc", "Yes")
    killed = 0
    while killed < 10:
        world.pickup("rock")
        if world.throw("rat"):
            killed += 1
    world.talk("npc", "I killed 10 rats")
    world.talk("npc", "You're welcome")
    
    return world