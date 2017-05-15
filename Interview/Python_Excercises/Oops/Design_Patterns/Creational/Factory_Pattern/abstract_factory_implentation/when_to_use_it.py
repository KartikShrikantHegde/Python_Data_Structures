# Since the Abstract Factory pattern is a generalization of the Factory Method pattern,
# it offers the same benefits: it makes tracking an object creation easier,
# it decouples an object creation from an object usage,
# and it gives us the potential to improve the memory usage and
# performance of our application.
#
# But a question is raised: how do we know when to use the Factory Method versus
# using an Abstract Factory? The answer is that we usually start with the Factory Method
# which is simpler. If we find out that our application requires many
# Factory Methods which it makes sense to combine for creating a family of objects,
# we end up with an Abstract Factory.