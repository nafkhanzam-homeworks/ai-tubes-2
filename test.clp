; -3 bomb
; -2 safe
; -1 unknown
; 0 <= x <= 4 element value


(defrule initfacts
  =>
  (assert (is-0 1 1))
  (assert (is-0 1 2))
  )

(defrule print-bombs
  (is-0 ?x ?y)
  =>
  (printout t "bomb on (" ?x ", " ?y ")" crlf)
  )