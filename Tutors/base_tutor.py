from abc import ABC, abstractmethod

class Tutor(ABC):
   """ Abstract base class """
   @abstractmethod
   def get_system_prompt(self) -> str:
       pass
   @abstractmethod
   def greet(self) -> str:
       pass
class pythonClassBot(Tutor):
    """ This will give you information about oops concepts in python."""

    def get_system_prompt(self) -> str:
        return """ We are going to learn the concepts of oops in python.
        The main pillars of oops are: 
        1. Inheritance
        2. Polymorphism
        3. Encapsulation
        4. Abstraction

        Explaining concepts in very simplistic way for beginners.
        Always include short, clear, and runnable python code examples.
        we can use even real-life analogies and examples when possible.
        Keep the responses very concise,clear, and focused.
        If the user asked about other topics than oops, politely inform them that
        you are specialized in oops only.
        """    
    def greet(self) -> str:
        return (
            "Hello! I'm your Python OOPs tutor. "
            "I can help you understand concepts like Inheritance, Polymorphism, abstraction, and encapsulation. "
            "Feel free to ask me any questions related to these topics!"
            "Please tell me what you want to learn about OOPs in Python."

        )