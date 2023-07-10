"""
Kardinalität einer Menge ist die

Definition Zufallsexperiment
1. lassen sich unter gleichen äußeren Bedingungen beliebig oft wiederholen
2. haben mehrere sich ausschließende Ergebnisse
3. Ergebnisse sind nicht sicher vorhersagbar

Ein Zufallsexperiment habe endlich viele bzw. allenfalls abzählbar unendlich viele sich gegenseitig ausschließende
 Ergebnisse w1,w2,... die sogenannten Elementarereignisse.

w1,w2,... sind in der Menge Omega, Omega ist die Ergebnismenge des Zufallsexperiments und für eine Abbildung
   p: Omega -> [0,1] (Intervall von 0 bis 1) mit der Eigenschaft
   sum(p(w) for w in Omega) = 1 heißt das Tupel (Omega, p) diskreter Wahrscheinlichkeitsraum. Teilmengen A aus Omega
   nennen wir Ereignisse und bezeichnen A insbesondere als
    1. unmögliches Ereignis, falls A=Leer gilt
    2. Elementarereignis, falls |A| = 1 gilt
    3. Sicheres Ereignis. falls A = Omega gilt

Wahrscheinlichkeit nach den Kolmogorov-Axiomen
1. P(A) ist eine nichtnegative Zahl kleiner oder gleich 1, 0<=P(A)<=1
2. Für Fall A = Omega (sicheres Ereignis) gilt P(A)=1
3. für parweise disjunkte Ereignisse A1, A2,... gilt
P(A1 u A2 u ...) = P(A1)+P(A2)+...


Die Wahrscheinlichkeit für das Eintreten von B unter der Voraussetzung dass A bereitseinetreten ist heißt bedingte
  Wahrscheinlichkeit von B unter der Bedingung A, symbolisch P(B|A). Sie wird durch
       P(B|A)=P(A ^ B)/P(A)
  berechnet. Die Wahrscheinlichkeit für das gleichzeitige Eintreten von A und B ist dann durch
       P(A ^ B) = P(A) * P(B|A)
gegeben

Stochastisch unabhängig:
Gilt P(A ^ B) = P(A)*P(B) so heißen A und B stochastisch unabhängig

"""