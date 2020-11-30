; is-edge -> dinding
; is-unknown -> belum terbuka
; is-bomb -> flagged oleh clips
; is-{0, 1, 2, 3, 4} -> terbuka
; is-open -> terbuka

(defrule check-1-1
  (
    or (is-edge)
  )
)

(defrule check-1

)