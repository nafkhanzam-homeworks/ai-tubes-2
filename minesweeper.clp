
; (deffacts initial-states
;   (n 3)
; )

; (defrule r0
;   (n ?n)
;   (?x ?y 0)
;   (?x >= 0)
;   (?x < ?n)
;   (?y >= 0)
;   (?y < ?n)
;   =>
;   (assert ((- ?x 1) (- ?y 1) -2))
;   (assert (?x (- ?y 1) -2))
;   (assert ((+ ?x 1) (- ?y 1) -2))
;   (assert ((- ?x 1) ?y -2))
;   (assert ((+ ?x 1) ?y -2))
;   (assert ((- ?x 1) (+ ?y 1) -2))
;   (assert (?x (+ ?y 1) -2))
;   (assert ((+ ?x 1) (+ ?y 1) -2))
; )

; (defrule r1
;   (
;     (n ?n)
;     (?x ?y 0)
;     (?x >= 0)
;     (?x < ?n)
;     (?y >= 0)
;     (?y < ?n)
;   )
;   and
;   (
;     ((- ?x 1) (- ?y 1) -1) or
;     (?x (- ?y 1) -1) or
;     ((+ ?x 1) (- ?y 1) -1) or
;     ((- ?x 1) ?y -1) or
;     ((+ ?x 1) ?y -1) or
;     ((- ?x 1) (+ ?y 1) -1) or
;     (?x (+ ?y 1) -1) or
;     ((+ ?x 1) (+ ?y 1) -1)
;   )
; )

; -3 bomb
; -2 safe
; -1 unknown
; 0 <= x <= 4 element value

; (?bomb 0)

; (
;   defrule gt0
;     (?x ?y ?v)
;     (?v > 0)
;     (
;       (loop-for-count (?dx -1 2) do
;         (loop-for-count (?dy -1 2) do
;           if
;           (
;             ((+ ?x ?dx) (+ ?y ?dy) ?v2)
;             (?v2 is -3)
;           )
;           then
;             (?bomb (+ ?bomb 1))
;           (assert (?))
;         )
;       )
;     )
; )

; -3 bomb
; -2 safe
; -1 unknown
; 0 <= x <= 4 element value

(defrule rule1
  (coord ?x ?y ?v)
  (> ?v 0)
=>
  (bind ?unknown 0)
  (bind ?bomb 0)
  (loop-for-count (?dx -1 1) do
    (loop-for-count (?dy -1 1) do
        if (coord (+ ?x ?dx) (+ ?y ?dy) -1) then
          (bind ?unknown (+ ?unknown 1))
        else if (coord (+ ?x ?dx) (+ ?y ?dy) -3) then
          (bind ?bomb (+ ?bomb 1))
    )
  )
  if (eq ?unknown (- ?v ?bomb)) then
    (loop-for-count (?dx -1 1) do
      (loop-for-count (?dy -1 1) do
        if (coord (+ ?x ?dx) (+ ?y ?dy) -1) then
        (assert (coord (+ ?x ?dx) (+ ?y ?dy) -3))
      )
    )
)

; (defrule rule1
;   (coord ?x ?y ?v)
;   (> ?v 0)
; =>
;   (assert (unknown 0))
;   (assert (bomb 0))
;   (loop-for-count (?dx -1 1) do
;     (loop-for-count (?dy -1 1) do
;       (assert (iterate-unknown (+ ?x ?dx) (+ ?y ?dy)))
;       (assert (iterate-bomb (+ ?x ?dx) (+ ?y ?dy)))
;     )
;   )
;   (assert target-unknown (- ?v ?bomb))
;   if (eq ?unknown ) then
;     (loop-for-count (?dx -1 1) do
;       (loop-for-count (?dy -1 1) do
;         if (coord (+ ?x ?dx) (+ ?y ?dy) -1) then
;         (assert (coord (+ ?x ?dx) (+ ?y ?dy) -3))
;       )
;     )
; )

(defrule iterate-unknown
  (coord ?x ?y -1)
  (unknown ?u)
=>
  (assert unknown (+ ?u 1))
)

(defrule iterate-bomb
  (coord ?x ?y -3)
  (bomb ?u)
=>
  (assert bomb (+ ?u 1))
)

; -3 bomb
; -2 safe
; -1 unknown
; 0 <= x <= 4 element value

; (defrule rule2
;   (?x ?y ?v)
;   (?v > 0)
;   (bind ?bomb 0)
;   (
;     (loop-for-count (?dx -1 2) do
;       (loop-for-count (?dy -1 2) do
;         if ((+ ?x ?dx) (+ ?y ?dy) -3) then
;         (assert (?bomb (+ ?bomb 1)))
;       )
;     )
;   )
;   (?bomb is ?v)
;   =>
;   (
;     (loop-for-count (?dx -1 2) do
;       (loop-for-count (?dy -1 2) do
;         if ((+ ?x ?dx) (+ ?y ?dy) -1) then
;         (assert ((+ ?x ?dx) (+ ?y ?dy) -2))
;       )
;     )
;   )
; )