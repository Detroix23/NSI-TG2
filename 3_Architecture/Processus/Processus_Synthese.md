# NSI Architecture: processus.
Synthèse.

## Définition: processus.

**Processus**: instance d'execution d'un programme. Comprends l'ensemble des ressources, 
de la mémoire, des registres.
Enregistre:
- `PID`: Processus ID;
- `PPID`: Parent PID;
- `t`: temps d'exécution restant.

**États d'un processus**:
- Prêt (le processus est _réveillé_ ou est _débloqué_).
- Elu (le processus passe l'_élection, il peut ensuite se finir).
- Bloqué (s'il ne s'ai pas fini, le processus subit le _blocage_).

**Création des processus**: il y a une hiérarchie.
Les premiers processus, qui naissent du `swapper` ou du `processus 0`, sont:
- `init` ou `systemd`;
- `khtreadd`.


## Ordonnancement ou _Scheduling_.

L'OS sert d'ordonnanceur, c'est-à-dire qu'il "gère l'ordre" d'exécution des processus.

Les métriques:
- **temps d'arrivage** $t_0$ d'un processus;
- **temps d'execution** $t_x$ ou durée d'un processus;
- **temps de terminaison** d'un processus;
- **temps de séjour**, utile pour les moyennes.
- **temps d'attente**, utile pour les moyennes.



### Ordonnanceurs non-préemptifs.

**Non-préemptif**: l'ordonnanceur n'arrête aucun processus en cours; 
dès qu'un est lancé, l'OS attends qu'il se finisse entièrement. 
- **temps de séjour** $t_s = t_t - t_0$;
- **temps d'attente** $t_a = t_s - t_x$.

**Premier Arrivé, Premier Servi (PAPS)** ou **First-Come, First-Served (FCFS)**:
liste d'attente pour les processus.

**Plus court d'abord** ou **Short Job First (SJF)**:
compare les processus en dans la liste d'attente et prends celui pour le quel 
le temps d'exécution est minimum. 


### Ordonnanceurs préemptifs.

**Quantum**: un ordonnanceur préemptif divise le temps entre les processus.
Ainsi, si un processus dépasse la limite en temps, le quantum $q$, il est mis en pause. 

**Shortest Remaining Time (SRT)**:
Tout les $q$ temps, l'OS execute le processus dans la file d'attente
avec le plus petit temps d'exécution restant.

**Round Robin (RR)**:
Les nouveaux processus sont enfilés dans une file _FIFO_. 
Tout les $q$ temps, l'OS arrête et enfile le processus courant
et le remplace par le processus défilé.

### L'interblocage ou étreinte fatale ou _deadlock_.
Phénomène en programmation concurrente: 2 processus s'attendent mutuellement.
- peut être représenté par un graphe (orienté) de dépendances:
_si_ il y a un cycle entres ses arcs, _alors_ il y a interblocage.

## Pratique:

Programmes Linux:

Liste les processus à l'instant.
```bash
ps -aef
```

Affichage dynamique des processus (liste ou arborescence):
```bash
top
```

Tuer des processus:
```bash
kill <PID>
pkill <name>
killall <name>
```
Trouver le PID:
```bash
pgrep <name>
```
