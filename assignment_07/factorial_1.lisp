
;Factorial of the number using recurssion

 (defun factorial(number)
    (if(= number 0) 1
        (* number (factorial(- number 1)))))

(princ "Enter a number :")
(setq number (read))
(princ "factorial of entered number is : ")
(format t " ~D" (factorial number))
