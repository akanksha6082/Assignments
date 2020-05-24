
;factorial without recurrsion


(defun facto(number)
    (setf fact 1)
    ( loop for x from 2 to number
           do(setq fact (* x fact))
    )
    fact
)

(princ "Enter a number: ")
(setq number (read))
(princ "The factorial of entered number using non-recurrsive method :")
(format t " ~D" (facto number))