import timeit
import random
import threading
from graphviz import Digraph

class Task:
  name = ""
  reads = []
  writes = []
  run = None

  def __init__(self, name, function, reads=[], writes=[]):
    self.name = name
    self.reads = reads
    self.writes = writes
    self.run = function


class TaskSystem:
  tasks = []
  dependencies = dict()
  
  print("test") 

  def __init__(self, tasks, dependencies):
      self.tasks = tasks
      self.dependencies = {}

  def addTask(self, task):
       # Vérification de la validité de la tâche
        if task.name == "":
            raise ValueError("Le nom de la tâche ne peut pas être vide.")
        for t in self.tasks:
            if t.name == task.name:
                raise ValueError("Le nom de la tâche existe déjà.")
        for r in task.reads:
            if r == "":
                raise ValueError("Le nom d'une lecture ne peut pas être vide.")
            if r not in [t.name for t in self.tasks]:
                raise ValueError("La tâche de lecture n'existe pas.")
        for w in task.writes:
            if w == "":
                raise ValueError("Le nom d'une écriture ne peut pas être vide.")
            if w not in [t.name for t in self.tasks]:
                raise ValueError("La tâche d'écriture n'existe pas.")

        self.tasks.append(task)
        self.dependencies[task.name] = set(task.reads)

  def TestBernstein(self,task):
      
      print("Lancement TestBernstein")
       
      # On test toutes les conditions de Bernstein 
      # s'il y a une interference, on retourne True
      for read in task.reads:
          if read in task.writes:
              return True

      for write in task.writes:
          if write in task.reads:
              return True
           
      for write in task.writes:
          if write in task.writes:
              return True
   
      # si on retourne False, il n'y a pas d'interférence
      return False
  
  def getDependencies(self, nomTache):

# stocke les noms de tâches dépendants
      nameTask = []
      dependencies = self.dependencies[nomTache]

# parcourt toutes les tâches et vérifie si leur nom correspond à une dépendance donnée
      for dep_name in dependencies:
          for task in self.tasks:
        # si oui, on l'ajoute à la liste des tâches et on sort de la boucle avec break
            if task.name == dep_name:
              nameTask.append(task.name)
              break

          return nameTask

    # L'exécution séquentielle
  def runSeq(self):
      
      print("Lancement runSeq")
      """
      Exécute les tâches du système de façon séquentielle en respectant l'ordre imposé
      par la relation de précédence.
      """
      # On initialise la liste des tâches exécutées
      tasksExecuted = []


      # Boucle 'while' tant qu'il reste des tâches à exécuter
      while len(tasksExecuted) < len(self.tasks):
          # Recherche de la première tâche non exécutée qui satisfait les conditions de précédence
          for task in self.tasks:
              if task.name not in tasksExecuted:
                  dependencies = self.getDependencies(task.name)
                  if all(dep in tasksExecuted for dep in dependencies):
                      task.run()
                      tasksExecuted.append(task.name)
                      break
      return True
  
  def run(self):
      executedTask = []
      dependencies = self.getDependencies()
      
      while len(executedTask)< len(self.tasks):
          taskInWait = []
          
          for tasks in self.tasks:
              
              if task.name in executedTask:
                  continue
              
              threads = []
              
              for task in taskInWait:
                  thread = threading.Thread(target=task.run)
                  threads.append(thread)
                  thread.start()
                  
                  for thread in threads:
                      thread.join()
                      
                  for task in taskInWait:
                      executedTask.append(task.name)
                          
                      taskInWait.clear()
                          

  
  
  def run(self):
      print("lancement séquentiel")
      self.runSeq()
      print("Fin runSeq")
      print("lancement parallèle")
      self.run()
      print("Fin run")
      

  
        
def detTestRnd(self, num_tests):
    """
    Teste la déterminisme du système de tâches en exécutant le système avec des jeux de valeurs
    aléatoires pour les variables de façon simple.
    """
    for i in range(num_tests):
        # Initialiser les valeurs aléatoires pour les tâches
        for task in self.tasks:
            for var in task.reads + task.writes:
                var.value = random.randint(0, 100)

        # Exécuter le système en mode séquentiel et en mode parallèle
        results_seq = []
        results_par = []
        for task in self.tasks:
            result = task.run()
            results_seq.append(result)

        for task in self.tasks:
            result = task.runPar(self.max_parallelism)
            results_par.append(result)

        # Comparer les résultats des deux modes d'exécution
        if results_seq != results_par:
            return False

    return True
        
        
  # on fait le test 5x car les premières exécutions peuvent être plus lentes que les suivantes

def parCost(self, number=5):
    
      print("Lancement parCost")
        
      # On lance l'exécution séquentielle et on calcule le temps de son exécution 
      runSeq_time = timeit.timeit(lambda: self.runSeq(), number)
        
      # On lance l'exécution parallèle et on calcule le temps de son exécution 
      run_time = timeit.timeit(lambda: self.run(), number)
        
      # On affiche les temps d'exécution puis on les comparent
      print("Temps d'exécution de runSeq moyens :", runSeq_time, "sec")
      print("Temps d'exécution de run moyens :", run_time, "sec")
      print("Différence de temps d'exécution :",
            abs(run_time - runSeq_time), "sec")
        
        
# Ne fonctionne pas

def draw(self):
    graphe = Digraph()

    # La déclaration des noeuds
    for task in self.tasks:
        graphe.node(task.name)
        

    # La création des arrêtes
    for task in self.tasks:
            graphe.edge(task.name)

    graphe.view()        