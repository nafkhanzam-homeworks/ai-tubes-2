; is-edge -> dinding
; is-unknown -> belum terbuka
; is-bomb -> flagged oleh clips
; is-{0, 1, 2, 3, 4} -> terbuka
; is-open -> terbuka
; is-safe -> safe cell oleh clips

(defrule new-positions
    (x-pos $?xpos)
    (y-pos $?ypos)
=>
    (assert (new-x-pos nil ?xpos nil))
    (assert (new-y-pos nil ?ypos nil))
)

(defrule check-1-1
  (new-x-pos $? ?x ?x1 ?x2 ?x3 $?)
  (new-y-pos $? ?y ?y1 $?)
  (
    or
      (is-edge ?x ?y)
      (is-open ?x ?y)
  )
  (
    or
      (is-edge ?x ?y1)
      (is-open ?x ?y1)
  )
  (is-unknown ?x1 ?y)
  (is-unknown ?x2 ?y)
  (is-1 ?x1 ?y1)
  (is-1 ?x2 ?y1)
=>
  (assert (is-safe ?x3 ?y))
)

(defrule check-1-2
  (new-x-pos $? ?x ?x1 ?x2 ?x3 $?)
  (new-y-pos $? ?y ?y1 $?)
  (
    or
      (is-edge ?x ?y)
      (is-open ?x ?y)
  )
  (
    or
      (is-edge ?x ?y1)
      (is-open ?x ?y1)
  )
  (is-unknown ?x1 ?y)
  (is-unknown ?x2 ?y)
  (is-1 ?x1 ?y1)
  (is-2 ?x2 ?y1)
=>
  (assert (is-bomb ?x3 ?y))
)