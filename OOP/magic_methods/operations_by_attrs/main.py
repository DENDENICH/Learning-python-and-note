

# __getattr__ - вызывается тогда, когда атрибут не найден
# __getattribute__ - вызывается тогда, когда атрибут найден
#   def __getattribute__(self, name):
#       return object.__getattribute__(self, name)

# __setattr__ - вызывается тогда, когда атрибут присваивается
#   def __setattr__(self, attr, name):
#       return object.__setattr__(self, attr, name)