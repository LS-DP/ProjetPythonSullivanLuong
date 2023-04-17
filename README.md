# ProjetPythonSullivanLuong

La méthode addTask prend en entrée un objet de type "task" et l'ajoute à une liste appelée "tasks". Elle effectue également des vérifications pour s'assurer que la tâche est valide avant de l'ajouter à la liste.

La méthode TestBernstein prend en entrée un objet de type "task". Cette méthode vise à tester s'il y a des interférences entre les lectures et les écritures de la tâche, en utilisant les conditions de Bernstein.

La méthode getDependencies prend en entrée un nom de tâche "nomTache" et retourne une liste contenant les noms des tâches dont la tâche "nomTache" dépend.

La méthode runSeq exécute les tâches du système de façon séquentielle en respectant l'ordre imposé par la relation de précédence.

La méthode run ne fonctionne pas. Elle est censée exécuter les tâches du système de façon paralèlle en utilisant des threads. 

La méthode detTestRnd permet de tester le déterminisme du système de tâches en exécutant le système avec des jeux de valeurs aléatoires pour les variables de façon simple.

La méthode parCost sert à comparer les temps d'exécution de l'exécution séquentielle (runSeq) et de l'exécution parallèle (run) du système de tâches. Elle prend en argument un nombre de fois (number) que l'on veut exécuter chaque méthode afin de pouvoir calculer des temps d'exécution moyens plus représentatifs.

La méthode draw permet de visualiser le graphe de dépendances du système de tâches à l'aide de la bibliothèque graphviz.
