# NSI Langages: paradigmes de programmation.
Synthèse.

## Différent paradigmes.

**Paradigme**: ensemble de manières et de règles pour programmer.

**Impérative**: suite d'instruction, de commandes.
- _Exemple_:  
```python
a: int = 0
while a < 10:
    a += 1
    print(f"a={a}")
a //= 2
```

**Fonctionnelle**: fonction sans effets secondaires, collatéraux, 
qui n'agissent que dans un cadre fermé, fini et bien défini.
- _Exemple_:
```ocaml
match [1; 2; 3] with
  | x :: y :: u -> y
  | x :: u -> x
  | [] -> raise Exit;;
```

**Orienté objet**: interaction entre objet (attributs et méthodes).

**Événementiel**: réaction à différent événements.
- _Exemple_: `javascript`.
