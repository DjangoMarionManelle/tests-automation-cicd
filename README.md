Bonjour Monsieur Messaoudene, 

Pour tester notre projet veuillez :
- veiler à avoir python (3.8.0 minimum)
- lancer la commande pour commancer à tester : python calculator.py

Voici 6 expressions arithmétiques (souhaitées dans la consigne) pour tester notre calculatrice:

Enter an expression: 5 + 10
Result: 15

Enter an expression: 15 - 7
Result: 8

Enter an expression: 3 * 8
Result: 24

Enter an expression: 20 / 5
Result: 4.0

Enter an expression: 20% * 50
Result: 10.0

Enter an expression: (2 + 3) * (4 - 1)
Result: 15.0

Pour la partie tests unitaires "BDD" nous avons établi un plan avec des scénarios en amont de l'implémentation, cela nous a également permis de prévoir d'une certaine manière dans 
quel ordre nous allions concevoir la calculatrice. 

Les différents tests effectués sont les suivants:

"test_addition" : teste si la fonction calcule correctement l'addition de deux nombres.
"test_subtraction" : teste si la fonction calcule correctement la soustraction de deux nombres.
"test_multiplication" : teste si la fonction calcule correctement la multiplication de deux nombres.
"test_division" : teste si la fonction calcule correctement la division de deux nombres.
"test_division_by_zero" : teste si la fonction renvoie "Infinity" en cas de division par zéro.
"test_negative_number" : teste si la fonction calcule correctement le produit d'un nombre négatif par un nombre positif.
"test_parentheses" : teste si la fonction calcule correctement une expression contenant des parenthèses.
"test_percent_operator" : teste si la fonction calcule correctement l'opérateur pourcentage (%).
"test_exponentiation_operator" : teste si la fonction calcule correctement l'opérateur exponentiel (^).
"test_decimal_result" : teste si la fonction renvoie un résultat décimal correct.
"test_invalid_expression" : teste si la fonction détecte correctement une expression invalide et renvoie le message d'erreur "Invalid expression!".

Chaque test est un cas de test qui vérifie le comportement de la fonction dans une situation donnée. Si la fonction ne se comporte pas comme attendu, le test échoue et une erreur est renvoyée. 

Suite à l'implémentation, nous avons mis en place des tests unitaires "TDD" qui nous ont permis de corriger grâce à des fonctions les potentielles erreurs qu'il y aurait pu y avoir dans notre fonction "calculate" (fichier calculator.py).
