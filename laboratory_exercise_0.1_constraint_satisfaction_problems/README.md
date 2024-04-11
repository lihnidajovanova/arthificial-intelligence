## Задача 1 - meeting

Потребно е да се закаже состанок во петок за Марија, Петар и Симона. Симона како менаџер мора да присуствува на
состанокот со најмалку уште една личност. Состанокот трае еден час, и може да се закаже во периодот од 12:00 до 20:00.
Почетокот на состанокот може да биде на секој час, односно состанокот може да почне во 12:00, но не во 12:05, 12:10 итн.
За секој од членовите дадени се времињата во кои се слободни:

- Симона слободни термини: 13:00-15:00, 16:00-17:00, 19:00-20:00
- Марија слободни термини: 14:00-16:00, 18:00-19:00
- Петар слободни термини: 12:00-14:00, 16:00-20:00

Потребно е менаџерот Симона да ги добие сите можни почетни времиња за состанокот. Даден е почетен код со кој е креирана
класа за претставување на проблемот, на кој се додадени променливите. Потоа се повикува наоѓање на решение со
BacktrackingSolver. Ваша задача е да ги додадете домените на променливите, како и да ги додадете ограничувањата (
условите) на проблемот.

Потсетник: Во дадениот модул constraint веќе се имплементирани следните ограничувања како класи: AllDifferentConstraint,
AllEqualConstraint, MaxSumConstraint, ExactSumConstraint, MinSumConstraint, InSetConstraint, NotInSetConstraint,
SomeInSetConstraint, SomeNotInSetConstraint.

For example:

````
Result
{'Simona_prisustvo': 1, 'Marija_prisustvo': 1, 'Petar_prisustvo': 0, 'vreme_sostanok': 14}
{'Simona_prisustvo': 1, 'Marija_prisustvo': 0, 'Petar_prisustvo': 1, 'vreme_sostanok': 19}
{'Simona_prisustvo': 1, 'Marija_prisustvo': 0, 'Petar_prisustvo': 1, 'vreme_sostanok': 16}
{'Simona_prisustvo': 1, 'Marija_prisustvo': 0, 'Petar_prisustvo': 1, 'vreme_sostanok': 13}
````

## Задача 2 - paper_presentation_schedule

Потребно е да направите распоред за презентација на трудови за некоја конференција. На конференцијата треба да бидат
презентирани вкупно 10 трудови од неколку области: Вештачка интелигенција (AI), Машинско Учење (ML) и Обработка на
природни јазици (NLP). Ваша задача е да направите распоред за конференција по термини и при тоа да се земат предвид
следните ограничувања:
- Во секој од термините може да бидат презентирани најмногу 4 трудови.
- Ако бројот на трудови од дадена област е помал или еднаков на максималниот број трудови кои може да бидат презентирани
во даден термин, тогаш тие трудови треба да бидат распределени во ист термин.

Од стандарден влез се чита бројот на термини во кои треба да бидат распределени трудовите (Напомена: бројот на термини
секогаш ќе биде 3 или 4). Потоа се читаат информации за секој труд во следниот формат „ID област“.

На стандарден излез да се испечати терминот за презентација за секој труд. Напомена: решението ќе се смета за точно
доколку ги добиете истите групи на трудови распределени во различен термин. На пример, следните 2 можни распределби се
сметаат за идентични:
- Paper1 (AI): T1, Paper2 (AI): T1, Paper3 (ML): T2
- Paper1 (AI): T2, Paper2 (AI): T2, Paper3 (ML): T1

Даден е почетен код со кој е креирана класа за претставување на проблемот, на кој се додадени променливите. Потоа се
повикува наоѓање на решение со BacktrackingSolver. Ваша задача е да ги додадете домените на променливите, како и да ги
додадете ограничувањата (условите) на проблемот.

Потсетник: Во дадениот модул constraint веќе се имплементирани следните ограничувања како класи: AllDifferentConstraint,
AllEqualConstraint, MaxSumConstraint, ExactSumConstraint, MinSumConstraint, InSetConstraint, NotInSetConstraint,
SomeInSetConstraint, SomeNotInSetConstraint.
````
For example:
====================
Input
3
Paper1 AI
Paper2 ML
Paper3 AI
Paper4 AI
Paper5 NLP
Paper6 ML
Paper7 ML
Paper8 NLP
Paper9 NLP
Paper10 ML
end

Result
Paper1 (AI): T3
Paper2 (ML): T2
Paper3 (AI): T3
Paper4 (AI): T3
Paper5 (NLP): T1
Paper6 (ML): T2
Paper7 (ML): T2
Paper8 (NLP): T1
Paper9 (NLP): T1
Paper10 (ML): T2
====================
Input
4
Paper1 AI
Paper2 ML
Paper3 AI
Paper4 AI
Paper5 NLP
Paper6 ML
Paper7 ML
Paper8 NLP
Paper9 NLP
Paper10 ML
end

Result
Paper1 (AI): T4
Paper2 (ML): T3
Paper3 (AI): T4
Paper4 (AI): T4
Paper5 (NLP): T2
Paper6 (ML): T3
Paper7 (ML): T3
Paper8 (NLP): T2
Paper9 (NLP): T2
Paper10 (ML): T3
====================
Input
3
Paper1 AI
Paper2 AI
Paper3 AI
Paper4 AI
Paper5 NLP
Paper6 AI
Paper7 NLP
Paper8 NLP
Paper9 NLP
Paper10 NLP
end

Result
Paper1 (AI): T3
Paper2 (AI): T3
Paper3 (AI): T3
Paper4 (AI): T2
Paper5 (NLP): T2
Paper6 (AI): T2
Paper7 (NLP): T2
Paper8 (NLP): T1
Paper9 (NLP): T1
Paper10 (NLP): T3
====================
Input
4
Paper1 AI
Paper2 AI
Paper3 AI
Paper4 AI
Paper5 NLP
Paper6 AI
Paper7 NLP
Paper8 NLP
Paper9 NLP
Paper10 NLP
end

Result
Paper1 (AI): T4
Paper2 (AI): T4
Paper3 (AI): T4
Paper4 (AI): T3
Paper5 (NLP): T3
Paper6 (AI): T3
Paper7 (NLP): T3
Paper8 (NLP): T2
Paper9 (NLP): T2
Paper10 (NLP): T4
====================
Input
3
Paper1 AI
Paper2 AI
Paper3 AI
Paper4 AI
Paper5 AI
Paper6 AI
Paper7 AI
Paper8 NLP
Paper9 NLP
Paper10 NLP
end

Result
Paper1 (AI): T3
Paper2 (AI): T2
Paper3 (AI): T2
Paper4 (AI): T2
Paper5 (AI): T2
Paper6 (AI): T1
Paper7 (AI): T1
Paper8 (NLP): T3
Paper9 (NLP): T3
Paper10 (NLP): T3
````