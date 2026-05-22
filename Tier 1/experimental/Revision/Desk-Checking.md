| X | Y | Z | Output |
| --- | --- | --- | --- |
| 1 | 2 | 2 | 0 |
| 3 | 2 | 2 | 4 |
| 5 | 2 | 2 | 8 |
| 7 | 2 | 2 | 12 |
| 8 | 2 | 2 | 12 |
| 9 | 2 | 2 | 12 |

| X | Y | MSG |
| --- | --- | --- |
| 60 | 70 | Boundary |
| 150 | 30 | Nothing |

| Phrase | Len | NewPhrase | done |
| --- | --- | --- | --- |
| dddgX | 5 | - | False |
| dddgX | 5 | d | False |
| dddgX | 4 | d | False |
| ddgX | 4 | d | False |
| ddgX | 3 | d | False |
| dgX | 3 | d | True |
| gX | 2 | d | True |
| gX | 2 | d | False |
| gX | 2 | dg | False |
| gX | 2 | dg | True |
| X | 1 | dg | True |
| X | 1 | dg | False |
| X | 1 | dgX | False |

| OK | ProductCode | Len | ExtractedCharacter | Count | Display |
| --- | --- | --- | --- | --- | --- |
| F | p3 |

| Students | Mark | Max | Average |
| --- | --- | --- | --- |
| 0 | 20 | 100 | - |
| 1 | 20 | 100 | 20 |
| 1 | 60 | 100 | 20 |
| 2 | 60 | 100 | 30 |
| 2 | 30 | 100 | 30 |
| 3 | 30 | 100 | 10 |
| 3 | 40 | 100 | 10 |
| 4 | 40 | 100 | 10 |