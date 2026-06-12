# NSI Architecture: sécurisation des communications.
Synthèse.

## Chiffrement symétrique.

Entre $A$ et $B$.

Repose sur:
- un message $m$ qu'on veut transmettre secrètement;
- une clé $k$ commune à $A$ et $B$;
- une chaîne chiffrée $s$.
- une fonction de chiffrement $c: \mathbb{N} \times \mathbb{N} \to \mathbb{N}$:
$$
c(m, k) = s
$$
- une fonction de déchiffrement $d$:
$$
d(s, k) = m
$$

**Exemples**:
- chiffrement César;
- la méthode XOR ($m \oplus k = s, s \oplus k = m$).

**Faiblesse**:
- Comment se passer de manière sécure la clé ?

## Chiffrement asymétrique.

Chaque bord $A$ et $B$ à:
- $k_{pub}X$: clé publique;
- $k_{pri}X$: clé privé.

**Diffie-Hellman (DH)**:
Soit:
- une clé publique commune $p \in \mathbb{N}$.
- une clé secrète pour $A$ et $B$, respectivement, $a, b \in \mathbb{N}$.
- une fonction $M$ connue et publique: $M: \mathbb{N} \times \mathbb{N} \to \mathbb{N}$:
    - tel qu'avec $M(p, x)$, il soit "difficile" de retrouver $x$.

La méthode _DH_:
$$
M(M(p, a), b) = M(M(p, b), a)
$$
Permet à chaque bord de partager un secret commun, en échangeant seulement des information publiques.

**Rivest-Shamir-Adlemn (RSA)**:
Soit:
- un message $m$ qui doit être envoyé de manière sécure;
- une clé secrète pour $A$ et $B$, respectivement, $k_{pri}A, k_{pri}B \in \mathbb{N}$.
- une clé publique pour $A$ et $B$, respectivement, $k_{pub}A, k_{pub}B \in \mathbb{N}$.
- une fonction $M$ connue et publique: $M: \mathbb{N} \times \mathbb{N} \to \mathbb{N}$:
    - tel qu'avec $M(m, x) $, il soit "difficile" de retrouver $m$.

Le système _RSA_:
$$
M(M(m, k_{pub}A), k_{pri}A) = m
$$

**Exemple**:
- le protocole *HyperText Transfer Protocol Secure* (`HTTPS`) dans un tunnel sécurisé `SSL/TLS`:
    - requête `HTTPS` du client $A$ vers le server $S$;
    - $S$ renvoie sa clé publique $k_{pub}S$;
    - $A$ chiffre la future clé secrète commune $K$. _Soit_: 
    $$
    K\prime = M(K, k_{pub}S)
    $$
    - $K\prime$ est envoyé à $S$;
    - $S$ déchiffre le secret commun grâce à sa clé commune. _Ainsi_, chez $S$: 
    $$
    K = M(K\prime, k_{pri}S) = M(M(K, k_{pub}S), k_{pri}S)
    $$
    - Échange de données chiffrées.

**Faiblesses**:
- L'attaque de l'homme du milieu.
- Remédiation par des certificats d'authentification.
