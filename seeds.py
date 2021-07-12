from todo.models import Todo

t1 = Todo(title="Wash dogs", description="Wash them with shampoo")
t1.save()

t2 = Todo(title="Cut grass", description="Mow, weed, edge, and blow before it rains this week")
t2.save()

t3 = Todo(title="Sweep", description="Sweep the hardwood floors")
t3.save()
