REM === BASIC COMPILER TEST SUITE ===
REM Arithmetic and PRINT
LET A = 1 + 2 * 3
LET B = (10 - 5) / 2
LET C% = -B + 7
PRINT "A=", A, "  B=", B, "  C%=", C%
PRINT "Is C% > 0?"; C% > 0

REM === IF / THEN / ELSE ===
LET X = 5
IF X = 5 THEN PRINT "X is five" ELSE PRINT "X is not five"
IF X < 0 THEN PRINT "Negative" ELSE PRINT "Non-negative"
IF X > 10 THEN PRINT "Big"

REM === GOTO / LABELS ===
START:
PRINT "Loop start"
LET CNT = 1
IF CNT > 3 THEN GOTO END_LOOP
PRINT "Count="; CNT
LET CNT = CNT + 1
GOTO START
END_LOOP:
PRINT "Loop ended"

REM === FOR / NEXT ===
FOR I = 1 TO 5 STEP 1
    PRINT "I="; I
NEXT I

REM === WHILE / WEND ===
LET J = 0
WHILE J < 4
    PRINT "J="; J
    LET J = J + 1
WEND

REM === GOSUB / RETURN ===
PRINT "Calling subroutine"
GOSUB SUB1
PRINT "Back from SUB1"
GOTO CONTINUE

SUB1:
    PRINT "In SUB1"
    RETURN

CONTINUE:
PRINT "After subroutine"

REM === INPUT ===
INPUT "Enter your name: ", NAME$
INPUT V1, V2%
PRINT "Hello "; NAME$
PRINT "V1="; V1; "  V2%="; V2%

REM === DIM and DATA/READ ===
DIM ARR(3)
DATA 10, 20, 30, 40
READ ARR(0), ARR(1), ARR(2), ARR(3)
PRINT "Array values:"
FOR K = 0 TO 3
    PRINT ARR(K)
NEXT K

REM === Complex expressions and nesting ===
LET D = (A + B) * (C% - X) / (I + J)
IF (D >= 0) THEN
    PRINT "D positive or zero: "; D
ELSE
    PRINT "D negative: "; D
END IF

REM === End of Test ===
PRINT "All tests completed."
END
